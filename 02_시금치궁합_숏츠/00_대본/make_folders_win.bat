@echo off
chcp 65001 >nul
set ROOT=%USERPROFILE%\Desktop\02_시금치궁합_숏츠
for %%D in (00_대본 09_BGM_효과음 10_최종출력 Scene_01 Scene_02 Scene_03 Scene_04 Scene_05 Scene_06 Scene_07 Scene_08) do mkdir "%ROOT%\%%D"
