mode con: cols=17 lines=1
:loop
@tasklist /fi "ImageName eq nfscblcr.exe" /fo csv 2>NUL | find /I "nfscblcr.exe">NUL
@if "%ERRORLEVEL%"=="0" taskkill /F /PID "nfscblcr.exe" >nul & start "BlackScreen" "mathe\praesentation.exe"
@goto loop