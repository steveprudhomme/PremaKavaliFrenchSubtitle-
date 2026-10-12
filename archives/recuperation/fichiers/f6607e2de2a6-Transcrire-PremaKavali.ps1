param(
    [string]$AudioPath = "",
    [int]$StartSeconds = 0,
    [int]$DurationSeconds = 900,
    [ValidateSet('comparaison','reference')][string]$Mode = 'comparaison',
    [string]$FfmpegPath = ''
)
$ErrorActionPreference = 'Stop'
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$whisper = Join-Path $env:APPDATA 'Subtitle Edit\SpeechToText\CppCuBlas\whisper-cli.exe'
$model = Join-Path $env:APPDATA 'Subtitle Edit\SpeechToText\Cpp\Models\large-v2.bin'
if (-not (Test-Path -LiteralPath $whisper)) { throw "Whisper introuvable : $whisper" }
if (-not (Test-Path -LiteralPath $model)) { throw "Modele introuvable : $model" }
if (-not $AudioPath) {
  $audios = @(Get-ChildItem -LiteralPath $base -File | Where-Object { $_.Extension -in @('.m4a','.mp3','.mp4','.wav') })
  if ($audios.Count -eq 1) { $AudioPath = $audios[0].FullName }
  else { throw "Place un seul fichier M4A/MP3/MP4/WAV a cote du script, ou indique -AudioPath 'C:\chemin\audio.m4a'." }
}
if (-not (Test-Path -LiteralPath $AudioPath)) { throw "Audio introuvable : $AudioPath" }
if (-not $FfmpegPath) {
  $ffcmd = Get-Command ffmpeg.exe -ErrorAction SilentlyContinue
  if ($ffcmd) { $FfmpegPath = $ffcmd.Source }
  else {
    $possible = @(Get-ChildItem -Path "$env:LOCALAPPDATA\Programs", "$env:APPDATA\Subtitle Edit", 'C:\ffmpeg' -Filter ffmpeg.exe -Recurse -File -ErrorAction SilentlyContinue | Select-Object -First 1)
    if ($possible.Count) { $FfmpegPath = $possible[0].FullName }
    else { throw 'FFmpeg introuvable. Installe FFmpeg et ajoute-le au PATH, ou utilise -FfmpegPath C:\chemin\ffmpeg.exe' }
  }
}
if ($StartSeconds -lt 0 -or $DurationSeconds -le 0) { throw 'Les durees doivent etre positives.' }
$out = Join-Path $base 'resultats'
New-Item -ItemType Directory -Path $out -Force | Out-Null
$stamp = '{0:D5}-{1:D5}' -f $StartSeconds, ($StartSeconds + $DurationSeconds)
$wav = Join-Path $out "audio_$stamp.wav"
$prefix = Join-Path $out "PremaKavali_hi_${stamp}_$Mode"
Write-Host "[1/3] Preparation audio depuis $StartSeconds s pour $DurationSeconds s..."
& $FfmpegPath -hide_banner -loglevel error -y -ss $StartSeconds -t $DurationSeconds -i $AudioPath -vn -ar 16000 -ac 1 -c:a pcm_s16le $wav
if ($LASTEXITCODE -ne 0) { throw 'Erreur FFmpeg.' }
Write-Host '[2/3] Transcription hindi avec GPU NVIDIA...'
$argsWhisper = @('--language','hi','--model',$model,'--output-srt','--print-progress','--temperature','0','--output-file',$prefix)
if ($Mode -eq 'comparaison') { $argsWhisper += @('--max-context','64','--beam-size','8') }
else { $argsWhisper += @('--max-context','0','--temperature-inc','0','--beam-size','5') }
$argsWhisper += $wav
& $whisper @argsWhisper
if ($LASTEXITCODE -ne 0) { throw "Whisper a echoue (code $LASTEXITCODE)." }
$srt = "$prefix.srt"
if (-not (Test-Path -LiteralPath $srt)) { throw "SRT introuvable : $srt" }
Write-Host '[3/3] Conversion des timecodes vers ceux du film...'
# Whisper timestamps start at zero for extracted clip. Restore the offset in a separate SRT.
$aligned = "${prefix}_timecodes_film.srt"
$utf8 = New-Object System.Text.UTF8Encoding($false)
$data = [System.IO.File]::ReadAllText($srt, [System.Text.Encoding]::UTF8)
$pattern = '(?m)(\d{2,}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2,}:\d{2}:\d{2}[,.]\d{3})'
$shift = {
 param($m)
 $converted = @()
 foreach ($j in 1,2) {
   $tc = $m.Groups[$j].Value.Replace(',', '.')
   $ts = [TimeSpan]::Parse($tc, [System.Globalization.CultureInfo]::InvariantCulture).Add([TimeSpan]::FromSeconds($StartSeconds))
   $hours = [math]::Floor($ts.TotalHours)
   $converted += ('{0:D2}:{1:D2}:{2:D2},{3:D3}' -f [int]$hours,$ts.Minutes,$ts.Seconds,$ts.Milliseconds)
 }
 return ($converted -join ' --> ')
}
$data = [System.Text.RegularExpressions.Regex]::Replace($data, $pattern, [System.Text.RegularExpressions.MatchEvaluator]$shift)
[System.IO.File]::WriteAllText($aligned, $data, $utf8)
Write-Host "TERMINE. Fichier a comparer : $aligned" -ForegroundColor Green
Write-Host 'Le SRT original est conserve. Tu peux m envoyer le nouveau fichier SRT.'
