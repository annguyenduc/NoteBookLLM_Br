# Graphify Setup & Bootstrap Script for Antigravity v3.0
# Alignment: ECC Structural Memory Mastery

$ProjectRoot = "d:\NoteBookLLM_Br"

Write-Host "Starting Graphify Bootstrap for $ProjectRoot..."

# Ensure dependencies
Write-Host "Checking dependencies..."
# Use graphifyy (distributed name)
pip install graphifyy[office] --quiet

# Run bootstrap using the robust python script
Write-Host "Weaving Knowledge Graph (this may take a few minutes)..."
python scripts/setup_graphify_bootstrap.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "Graph Bootstrap Complete!"
    Write-Host "Report generated at: $ProjectRoot\graphify-out\GRAPH_REPORT.md"
} else {
    Write-Host "Graphify failed with exit code $LASTEXITCODE"
}
