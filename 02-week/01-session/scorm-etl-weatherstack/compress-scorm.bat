@echo off
REM Script para comprimir paquete SCORM - ETL Weatherstack
REM IMPORTANTE: Comprime los archivos EN LA RAIZ, NO la carpeta misma
REM Esto arregla el error: "imsmanifest.xml no está en la raíz"

setlocal enabledelayedexpansion

REM Navigate to the parent directory
cd /d "%~dp0"

echo.
echo ========================================
echo   SCORM Packaging Script (CORRECCIÓN)
echo   ETL Weatherstack for Moodle
echo ========================================
echo.

REM Check if PowerShell is available
powershell -Command "Write-Host 'PowerShell Check: OK'" >nul 2>&1

if %errorlevel% neq 0 (
    echo ERROR: PowerShell is required but not found!
    pause
    exit /b 1
)

REM Define paths
set "SCORM_DIR=%cd%"
set "PARENT_DIR=%~dp0.."
set "ZIP_NAME=scorm-etl-weatherstack.zip"
set "ZIP_PATH=%PARENT_DIR%\%ZIP_NAME%"

echo Source directory: %SCORM_DIR%
echo Output file: %ZIP_PATH%
echo.

REM Create the ZIP file - IMPORTANTE: usar * para comprimir contenido, no la carpeta
echo Creating ZIP package...
echo ⭐ Comprimiendo el contenido EN LA RAIZ (no la carpeta misma)
echo.

powershell -Command ^
    "if(Test-Path '%ZIP_PATH%') {Remove-Item '%ZIP_PATH%' -Force}; ^
    Compress-Archive -Path '%SCORM_DIR%\*' -DestinationPath '%ZIP_PATH%' -Force; ^
    Write-Host 'Successfully created: %ZIP_PATH%' -ForegroundColor Green; ^
    Get-Item '%ZIP_PATH%' | Select-Object @{Name='Filename'; Expression={$_.Name}}, @{Name='Size (KB)'; Expression={[math]::Round($_.Length/1KB, 2)}}; ^
    Write-Host 'imsmanifest.xml está en la RAÍZ ✓' -ForegroundColor Green"

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   SUCCESS!
    echo ========================================
    echo.
    echo Your SCORM package is ready to upload to Moodle:
    echo.
    echo   File: %ZIP_NAME%
    echo   Location: %PARENT_DIR%
    echo.
    echo Next steps:
    echo 1. Download: %ZIP_NAME%
    echo 2. Log in to Moodle
    echo 3. Go to your course and enable Edit mode
    echo 4. Add activity: SCORM
    echo 5. Upload the ZIP file above
    echo 6. Click "Save and display"
    echo.
    echo ========================================
) else (
    echo.
    echo ERROR creating ZIP file!
    echo Please check the paths and try again.
    echo.
)

pause
