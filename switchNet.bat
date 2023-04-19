@echo off

setlocal enabledelayedexpansion

set adapter1Name=Ping Ruim
set adapter2Name=Ping Bom

set adapter1Status=
set adapter2Status=

REM Check the current status of each adapter
for /f "tokens=1,9 delims=:" %%a in ('netsh interface show interface ^| find /i "%adapter1Name%" ^| find /i "%adapter2Name%"') do (
    if "%%a"=="%adapter1Name%" set adapter1Status=%%b
    if "%%a"=="%adapter2Name%" set adapter2Status=%%b
)

REM Disable adapter1Name if it is currently enabled
if "%adapter1Status%"=="Connected" (
    echo Disabling %adapter1Name%
    netsh interface set interface "%adapter1Name%" admin=disable
)

REM Enable adapter2Name if it is currently disabled
if "%adapter2Status%"=="Disconnected" (
    echo Enabling %adapter2Name%
    netsh interface set interface "%adapter2Name%" admin=enable
)

pause
