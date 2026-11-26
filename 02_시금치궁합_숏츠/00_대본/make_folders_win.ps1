$root = "$env:USERPROFILE\Desktop\02_시금치궁합_숏츠"
"00_대본","09_BGM_효과음","10_최종출력" + (1..8 | ForEach-Object { "Scene_{0:D2}" -f $_ }) | ForEach-Object { New-Item -ItemType Directory -Force -Path "$root\$_" | Out-Null }
