mode con: cols=17 lines=1
:loop
@tasklist /fi "ImageName eq notepad.exe" /fo csv 2>NUL | find /I "notepad.exe">NUL
@if "%ERRORLEVEL%"=="0" taskkill /F /PID "notepad.exe" >nul & start "BlackScreen" "mathe\praesentation.exe"
@goto loop