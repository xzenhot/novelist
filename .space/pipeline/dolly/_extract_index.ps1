$out = 'd:\lab\github\writer\.space\pipeline\dolly\_write_all_index.txt'
Remove-Item $out -ErrorAction SilentlyContinue
$root = 'd:\lab\github\writer\.space\pipeline\dolly\chapters'
foreach ($i in 1..60) {
  $p = Join-Path $root "$i\chapter.md"
  if (Test-Path $p) {
    $lines = Get-Content $p
    $t = $lines[0] -replace '^#\s*',''
    $o = ($lines | Where-Object { $_ -like '*specific charge is:*' }) -join ' '
    $charge = $o -replace '.*specific charge is: ','' -replace ' The poem opens.*$','' -replace ' The poem establishes.*$','' -replace ' The poet considers.*$',''
    $bl = ($lines | Where-Object { $_ -like '*carried toward*' }) -join ' '
    $b = $bl -replace '.*toward ','' -replace "'.*$",''
    $v3 = Test-Path (Join-Path $root "$i\segments\1\writer\chapter_v3.md")
    Add-Content $out ("[{0}] {1} | {2} | next={3} | v3={4}" -f $i, $t, $charge, $b, $v3)
  }
}
Write-Output 'done'
