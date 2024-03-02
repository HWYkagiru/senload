@echo off
echo Starting senload...
timeout /t 1
REM Download senload.exe
powershell -Command "$url = 'https://github.com/HWYkagiru/senload/releases/download/senload/senload.exe'; $output = 'senload.exe'; Invoke-WebRequest -Uri $url -OutFile $output"

REM Check download
if %errorlevel% neq 0 (
    echo Error: Failed to download senload.exe.
    exit /b %errorlevel%
)

REM Verify Downloadd

REM start senload.exe
echo Running senload...
start /wait senload.exe

REM Check if succes
if %errorlevel% neq 0 (
    echo Error: Failed to execute senload.exe.
    exit /b %errorlevel%
)

echo Senload installed successfully.
pause
