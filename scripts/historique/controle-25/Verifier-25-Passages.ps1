param(
    [string]$VadModel = "",
    [switch]$TestPremierSeulement
)
$ErrorActionPreference = 'Stop'
$racine = Split-Path -Parent $MyInvocation.MyCommand.Path
$cheminWhisper = Join-Path $env:APPDATA 'Subtitle Edit\SpeechToText\CppCuBlas\whisper-cli.exe'
$modele = Join-Path $env:APPDATA 'Subtitle Edit\SpeechToText\Cpp\Models\large-v2.bin'
$dossierAudio = Join-Path $racine 'audio'
$dossierResultats = Join-Path $racine 'resultats'
$dossierWav = Join-Path $dossierResultats 'wav_temp'
$csv = Join-Path $racine 'Prema_Kavali_verification_audio_25_extraits.csv'
foreach ($p in @($cheminWhisper,$modele,$csv,$dossierAudio)) {
    if (-not (Test-Path -LiteralPath $p)) { throw "Fichier/dossier introuvable : $p" }
}
$ffmpegCmd = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpegCmd) { throw 'FFmpeg introuvable. Installez FFmpeg, puis ajoutez son dossier bin au PATH Windows.' }
if ($VadModel -and -not (Test-Path -LiteralPath $VadModel)) { throw "Modele VAD introuvable : $VadModel" }
New-Item -ItemType Directory -Force -Path $dossierResultats,$dossierWav | Out-Null
$rows = @(Import-Csv -LiteralPath $csv -Encoding UTF8)
if ($TestPremierSeulement) { $rows = @($rows | Select-Object -First 1) }
$rapport = New-Object System.Collections.Generic.List[object]
function Format-SrtTime([timespan]$t) {
    if ($t.TotalMilliseconds -lt 0) { $t = [timespan]::Zero }
    $h = [math]::Floor($t.TotalHours)
    return ('{0:00}:{1:00}:{2:00},{3:000}' -f $h,$t.Minutes,$t.Seconds,$t.Milliseconds)
}
function Recale-Srt([string]$source,[string]$destination,[double]$secondes) {
    $content = [System.IO.File]::ReadAllText($source,[System.Text.Encoding]::UTF8)
    $pattern = '(?m)(\d{2}:\d{2}:\d{2}[,.]\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}[,.]\d{3})'
    $offset = [timespan]::FromSeconds($secondes)
    $converted = [regex]::Replace($content,$pattern,{
        param($m)
        $a = [timespan]::ParseExact($m.Groups[1].Value.Replace(',','.'),'hh\:mm\:ss\.fff',[cultureinfo]::InvariantCulture).Add($offset)
        $b = [timespan]::ParseExact($m.Groups[2].Value.Replace(',','.'),'hh\:mm\:ss\.fff',[cultureinfo]::InvariantCulture).Add($offset)
        return "$(Format-SrtTime $a) --> $(Format-SrtTime $b)"
    })
    [System.IO.File]::WriteAllText($destination,$converted,(New-Object System.Text.UTF8Encoding($false)))
}
$index=0
foreach ($r in $rows) {
    $index++
    $name=[IO.Path]::GetFileNameWithoutExtension($r.fichier_audio)
    $clip=Join-Path $dossierAudio $r.fichier_audio
    $wav=Join-Path $dossierWav ($name + '.wav')
    $prefix=Join-Path $dossierResultats ($name + '_whisper')
    $raw=$prefix+'.srt'
    $recaled=Join-Path $dossierResultats ($name + '_film.srt')
    Write-Host "[$index/$($rows.Count)] $($r.fichier_audio)" -ForegroundColor Cyan
    if (-not (Test-Path -LiteralPath $clip)) { Write-Warning "Absent : $clip"; continue }
    & $ffmpegCmd.Source -hide_banner -loglevel error -y -i $clip -ar 16000 -ac 1 -c:a pcm_s16le $wav
    if ($LASTEXITCODE -ne 0) { Write-Warning "FFmpeg erreur pour $name"; continue }
    # Cette version de whisper.cpp utilise --max-context, PAS --no-context.
    $arguments=@('--language','hi','--model',$modele,'--output-srt','--temperature','0','--temperature-inc','0','--beam-size','5','--max-context','0','--output-file',$prefix)
    if ($VadModel) { $arguments+=@('--vad','--vad-model',$VadModel) }
    $arguments+=@($wav)
    & $cheminWhisper @arguments
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $raw)) { Write-Warning "Whisper erreur pour $name"; continue }
    $debut = [double]::Parse($r.debut_extrait_secondes,[cultureinfo]::InvariantCulture)
    Recale-Srt $raw $recaled $debut
    $sub=[System.IO.File]::ReadAllText($raw,[System.Text.Encoding]::UTF8)
    $lignes = $sub -split '\r?\n' | Where-Object { $_.Trim() -ne '' -and $_ -notmatch '^\d+$' -and $_ -notmatch '^\d{2}:\d{2}:\d{2}' }
    $rapport.Add([pscustomobject]@{
        rang=$r.rang; numero_SRT=$r.numero_SRT; debut_film=$r.debut_film;
        fin_film=$r.fin_film; anomalies=$r.anomalies;
        texte_reference=$r.texte_SRT; youtube_1=$r.YouTube_1; youtube_2=$r.YouTube_2;
        whisper_nouveau=($lignes -join ' / '); fichier_srt_recale=([IO.Path]::GetFileName($recaled));
        statut='A_VERIFIER_AVEC_AUDIO'
    })
}
$rapportPath=Join-Path $dossierResultats 'comparaison_25_passages.csv'
$rapport | Export-Csv -LiteralPath $rapportPath -Encoding UTF8 -NoTypeInformation
Write-Host "`nTermine. Fichiers dans $dossierResultats" -ForegroundColor Green
Write-Host "Rapport : $rapportPath"
Write-Host 'Les divergences ne sont PAS corrigees automatiquement : une nouvelle transcription reste une hypothese.'
