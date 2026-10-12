$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (!(Test-Path $python)) { throw 'Run Installer.ps1 first.' }
& $python '.\traduire_tout.py' @args
if ($LASTEXITCODE -ne 0) { throw "Translation failed with error code $LASTEXITCODE" }
