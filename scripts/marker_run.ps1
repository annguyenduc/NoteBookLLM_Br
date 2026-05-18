param(
    [Parameter(Mandatory = $true)]
    [string]$InputPdf,
    [string]$OutputDir = "scratch\\marker_output",
    [string]$Langs = "Vietnamese,English",
    [switch]$ForceOcr
)

$env:INFERENCE_RAM = "3.5"
$env:TORCH_DEVICE = "cuda"
$env:MODEL_CACHE_DIR = "D:\\NoteBookLLM_Br\\scratch\\marker_cache\\models"
$env:HF_HOME = "D:\\NoteBookLLM_Br\\scratch\\marker_cache\\hf"

if (-not (Test-Path $InputPdf)) {
    throw "Input PDF not found: $InputPdf"
}

if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

foreach ($cacheDir in @($env:MODEL_CACHE_DIR, $env:HF_HOME)) {
    if (-not (Test-Path $cacheDir)) {
        New-Item -ItemType Directory -Path $cacheDir -Force | Out-Null
    }
}

$cmd = @(
    "D:\\NoteBookLLM_Br\\.venv_marker\\Scripts\\marker_single.exe",
    $InputPdf,
    "--output_dir", $OutputDir
)

if ($ForceOcr) {
    $cmd += "--force_ocr"
}

# marker-pdf 1.10.2 does not expose a --langs CLI flag on marker_single.
if ($Langs -and $Langs -ne "Vietnamese,English") {
    Write-Warning "Langs='$Langs' was requested, but marker_single.exe does not expose a --langs option in this build."
}

& $cmd[0] $cmd[1..($cmd.Length - 1)]

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

$outputFiles = Get-ChildItem -Path $OutputDir -Recurse -File -ErrorAction SilentlyContinue
if (-not $outputFiles) {
    Write-Warning "Marker completed without writing files to $OutputDir"
}
