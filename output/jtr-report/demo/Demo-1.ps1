$ErrorActionPreference = 'Stop'
$labRoot = (Resolve-Path (Join-Path $PSScriptRoot '../lab')).Path
$johnExe = Join-Path $labRoot 'tools/john-1.9.0-jumbo-1-win64/run/john.exe'
$demoResults = Join-Path $labRoot ('results/demo-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Path $demoResults | Out-Null
$env:OMP_NUM_THREADS = '4'
& $johnExe '--format=raw-sha256' "--wordlist=$labRoot/data/wordlist.txt" "--pot=$demoResults/wordlist.pot" "$labRoot/data/sha256.txt"
& $johnExe "--config=$labRoot/configs/experiment.conf" '--format=raw-sha256' "--wordlist=$labRoot/data/wordlist.txt" '--rules=Lab' "--pot=$demoResults/rules.pot" "$labRoot/data/sha256.txt"
& $johnExe '--format=raw-sha256' '--mask=?l?l?d?d?d?d' "--pot=$demoResults/mask.pot" "$labRoot/data/sha256.txt"
& $johnExe '--format=raw-sha256' '--mask=?d?d?d?d?d?d' "--pot=$demoResults/wrong-mask.pot" "$labRoot/data/sha256.txt"
Write-Host "Ket qua demo: $demoResults"
