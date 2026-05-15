[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet('micro', 'vault', 'dev', 'ingest', 'full')]
    [string]$Mode,
    [string]$ConfigPath,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

# Policy:
# - Inspect and DryRun are safe to automate.
# - Actual profile switching changes external MCP state and requires explicit AN approval.

function Resolve-ConfigPath {
    param([string]$ExplicitPath)

    if ($ExplicitPath) {
        return $ExplicitPath
    }

    $candidates = @(
        'D:\anngu\.gemini\antigravity\mcp_config.json',
        (Join-Path $env:APPDATA '.gemini\mcp.json')
    )

    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path -LiteralPath $candidate)) {
            return $candidate
        }
    }

    throw 'MCP config not found in supported default paths. Use -ConfigPath.'
}

function Read-JsonObject {
    param([string]$Path)

    $raw = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    return $raw | ConvertFrom-Json
}

function Get-FullBackupPath {
    param([string]$Path)

    return $Path + '.full.bak'
}

function Get-SchemaInfo {
    param([object]$Config)

    if ($null -ne $Config.PSObject.Properties['mcpServers']) {
        $names = @($Config.mcpServers.PSObject.Properties.Name)
        return [pscustomobject]@{
            Schema = 'mcpServers'
            Names = $names
        }
    }

    if ($null -ne $Config.PSObject.Properties['servers']) {
        $names = @($Config.servers | ForEach-Object { $_.name })
        return [pscustomobject]@{
            Schema = 'servers'
            Names = $names
        }
    }

    return [pscustomobject]@{
        Schema = 'unknown'
        Names = @()
    }
}

function Copy-TopLevel {
    param([object]$Config)

    $copy = [ordered]@{}
    foreach ($prop in $Config.PSObject.Properties) {
        $copy[$prop.Name] = $prop.Value
    }
    return $copy
}

function Get-ProfileServerSet {
    param([string]$Profile)

    switch ($Profile) {
        'micro'  { return @('filesystem') }
        'vault'  { return @('filesystem', 'sqlite') }
        'dev'    { return @('filesystem', 'sqlite', 'git', 'github-mcp-server') }
        'ingest' { return @('filesystem', 'sqlite', 'notebooklm-mcp-server') }
        default  { throw ('Unsupported profile: ' + $Profile) }
    }
}

function Build-SubsetConfig {
    param(
        [object]$Config,
        [string]$Schema,
        [string[]]$KeepServers
    )

    if ($Schema -eq 'mcpServers') {
        $serverNames = @($Config.mcpServers.PSObject.Properties.Name)
        $missing = @($KeepServers | Where-Object { $_ -notin $serverNames })
        if ($missing.Count) {
            throw ('Required servers missing for requested profile: ' + ($missing -join ', '))
        }

        $copy = Copy-TopLevel -Config $Config
        $subset = [ordered]@{}
        foreach ($name in $KeepServers) {
            $subset[$name] = $Config.mcpServers.$name
        }
        $copy['mcpServers'] = $subset
        return [pscustomobject]@{
            Config = $copy
            Active = @($KeepServers)
            Disabled = @($serverNames | Where-Object { $_ -notin $KeepServers })
        }
    }

    if ($Schema -eq 'servers') {
        $servers = @($Config.servers)
        $serverNames = @($servers | ForEach-Object { $_.name })
        $missing = @($KeepServers | Where-Object { $_ -notin $serverNames })
        if ($missing.Count) {
            throw ('Required servers missing for requested profile: ' + ($missing -join ', '))
        }

        $copy = Copy-TopLevel -Config $Config
        $selectedServers = foreach ($name in $KeepServers) {
            $servers | Where-Object { $_.name -eq $name } | Select-Object -First 1
        }
        $copy['servers'] = @($selectedServers)
        $active = @($copy['servers'] | ForEach-Object { $_.name })
        $disabled = @($servers | Where-Object { $_.name -notin $KeepServers } | ForEach-Object { $_.name })
        return [pscustomobject]@{
            Config = $copy
            Active = $active
            Disabled = $disabled
        }
    }

    throw 'Unsupported MCP schema.'
}

function Get-RenderSource {
    param(
        [string]$ConfigPath,
        [bool]$PreferFullBackup
    )

    $fullBackupPath = Get-FullBackupPath -Path $ConfigPath
    if ($PreferFullBackup -and (Test-Path -LiteralPath $fullBackupPath)) {
        return [pscustomobject]@{
            Path = $fullBackupPath
            Exists = $true
        }
    }

    return [pscustomobject]@{
        Path = $ConfigPath
        Exists = $false
    }
}

function Ensure-FullBackup {
    param([string]$Path)

    $fullBackup = Get-FullBackupPath -Path $Path
    if (-not (Test-Path -LiteralPath $fullBackup)) {
        Copy-Item -LiteralPath $Path -Destination $fullBackup -Force:$false
    }
    return $fullBackup
}

function New-TimestampBackup {
    param([string]$Path)

    $timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $backupPath = $Path + '.bak_' + $timestamp
    Copy-Item -LiteralPath $Path -Destination $backupPath -Force:$false
    return $backupPath
}

function Write-ValidatedJsonAtomically {
    param(
        [string]$Path,
        [object]$ConfigObject
    )

    $dir = Split-Path -Parent $Path
    $tempPath = Join-Path $dir ([System.IO.Path]::GetRandomFileName() + '.tmp')
    $json = $ConfigObject | ConvertTo-Json -Depth 100
    [System.IO.File]::WriteAllText($tempPath, $json, [System.Text.UTF8Encoding]::new($false))

    try {
        $null = Get-Content -LiteralPath $tempPath -Raw -Encoding UTF8 | ConvertFrom-Json
    }
    catch {
        Remove-Item -LiteralPath $tempPath -Force -ErrorAction SilentlyContinue
        throw 'Temporary JSON validation failed; aborting write.'
    }

    Move-Item -LiteralPath $tempPath -Destination $Path -Force
}

$configPathResolved = Resolve-ConfigPath -ExplicitPath $ConfigPath
$config = Read-JsonObject -Path $configPathResolved
$schemaInfo = Get-SchemaInfo -Config $config
$schema = $schemaInfo.Schema
$serverNames = @($schemaInfo.Names)

if ($schema -eq 'unknown') {
    throw 'Unknown MCP schema.'
}

Write-Output ('Detected schema: ' + $schema)
Write-Output ('Config path: ' + $configPathResolved)
Write-Output ('Current servers: ' + (($serverNames -join ', ')))
if (-not $DryRun) {
    Write-Output 'Policy: actual MCP profile switching requires explicit AN approval.'
}

if ($Mode -in @('micro', 'vault', 'dev', 'ingest')) {
    $source = Get-RenderSource -ConfigPath $configPathResolved -PreferFullBackup $true
    $sourceConfig = Read-JsonObject -Path $source.Path
    $sourceSchemaInfo = Get-SchemaInfo -Config $sourceConfig
    if ($sourceSchemaInfo.Schema -eq 'unknown') {
        throw 'Source config for profile rendering has unknown schema.'
    }

    $keepServers = Get-ProfileServerSet -Profile $Mode
    $profileResult = Build-SubsetConfig -Config $sourceConfig -Schema $sourceSchemaInfo.Schema -KeepServers $keepServers
    $active = @($profileResult.Active)
    $disabled = @($profileResult.Disabled)

    if ($DryRun) {
        Write-Output 'DryRun: no files modified.'
        if ($source.Exists) {
            Write-Output ('Rendered from full backup: ' + $source.Path)
        }
        else {
            Write-Output 'Rendered from active config because full backup does not exist yet.'
        }
        Write-Output ('Active servers after ' + $Mode + ': ' + ($active -join ', '))
        Write-Output ('Disabled servers: ' + ($(if ($disabled.Count) { $disabled -join ', ' } else { 'none' })))
        Write-Output 'Reload/restart MCP or the agent session to apply changes after an actual switch.'
        exit 0
    }

    $fullBackup = Ensure-FullBackup -Path $configPathResolved
    $timestampBackup = New-TimestampBackup -Path $configPathResolved
    Write-ValidatedJsonAtomically -Path $configPathResolved -ConfigObject $profileResult.Config

    Write-Output ('Full backup: ' + $fullBackup)
    Write-Output ('Timestamp backup: ' + $timestampBackup)
    Write-Output ('Active servers after ' + $Mode + ': ' + ($active -join ', '))
    Write-Output ('Disabled servers: ' + ($(if ($disabled.Count) { $disabled -join ', ' } else { 'none' })))
    Write-Output 'Reload/restart MCP or the agent session to apply changes.'
    exit 0
}

if ($Mode -eq 'full') {
    $fullBackupPath = Get-FullBackupPath -Path $configPathResolved
    if (-not (Test-Path -LiteralPath $fullBackupPath)) {
        throw 'Full backup not found; aborting restore.'
    }

    $restoreConfig = Read-JsonObject -Path $fullBackupPath
    $restoreSchemaInfo = Get-SchemaInfo -Config $restoreConfig
    if ($restoreSchemaInfo.Schema -eq 'unknown') {
        throw 'Backup JSON has unknown schema; aborting restore.'
    }

    if ($DryRun) {
        Write-Output 'DryRun: no files modified.'
        Write-Output ('Active servers after full restore: ' + (($restoreSchemaInfo.Names -join ', ')))
        Write-Output 'Disabled servers: none'
        Write-Output 'Reload/restart MCP or the agent session to apply changes after an actual switch.'
        exit 0
    }

    $timestampBackup = New-TimestampBackup -Path $configPathResolved
    $restorePayload = Copy-TopLevel -Config $restoreConfig
    Write-ValidatedJsonAtomically -Path $configPathResolved -ConfigObject $restorePayload

    Write-Output ('Timestamp backup: ' + $timestampBackup)
    Write-Output ('Active servers after full restore: ' + (($restoreSchemaInfo.Names -join ', ')))
    Write-Output 'Disabled servers: none'
    Write-Output 'Reload/restart MCP or the agent session to apply changes.'
    exit 0
}
