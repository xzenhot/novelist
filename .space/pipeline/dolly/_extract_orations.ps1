$out = 'd:\lab\github\writer\.space\pipeline\dolly\_write_all_orations.txt'
Remove-Item $out -ErrorAction SilentlyContinue
$root = 'd:\lab\github\writer\.space\pipeline\dolly\chapters'
foreach ($i in 1..60) {
  $p = Join-Path $root "$i\chapter.md"
  if (Test-Path $p) {
    $lines = Get-Content $p
    $o = ($lines | Where-Object { $_ -like 'The poem should begin*' }) -join ' '
    $bl = ($lines | Where-Object { $_ -like 'Let the closing blessing*' }) -join ' '
    Add-Content $out "[$i] ORATION: $o"
    Add-Content $out "[$i] BENEDICT: $bl"
  }
}
Write-Output 'done'
