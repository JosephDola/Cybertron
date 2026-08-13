$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

if (-not (Test-Path ".venv-win\Scripts\python.exe")) {
    py -m venv .venv-win
}

$Python = ".venv-win\Scripts\python.exe"
& $Python -m pip install --upgrade pip
& $Python -m pip install -r requirements-used.txt
& $Python -m pip install "pyinstaller>=6.21,<7"

Remove-Item -Recurse -Force build, dist -ErrorAction SilentlyContinue

& $Python -m PyInstaller `
    --noconfirm `
    --clean `
    --windowed `
    --onedir `
    --name Cybertron `
    --add-data "voice/browser_bridge.html:voice" `
    main.py

Write-Host "Built dist\Cybertron\Cybertron.exe"
