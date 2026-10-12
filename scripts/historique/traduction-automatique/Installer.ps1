$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (!(Get-Command py -ErrorAction SilentlyContinue)) {
  Write-Host 'Python is not installed. Install Python 3.11 or 3.12 from python.org and reopen PowerShell.'
  exit 1
}
py -3 -m venv .venv
$python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
& $python -m pip install --upgrade pip
& $python -m pip install 'torch>=2.2' --index-url https://download.pytorch.org/whl/cu128
& $python -m pip install 'transformers==4.44.2' 'sentencepiece>=0.2' 'sacremoses>=0.1.1'
Write-Host 'Installation complete. Run: .\Traduire-Tout.ps1'
