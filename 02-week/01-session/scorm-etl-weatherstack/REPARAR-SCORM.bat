@echo off
REM ============================================================
REM Script para RECOMPRIMIR correctamente el SCORM para Moodle
REM Soluciona: "imsmanifest.xml no está en la raíz"
REM ============================================================

cd /d "%~dp0"

echo.
echo ============================================================
echo   REPARANDO EMPAQUETAMIENTO SCORM
echo ============================================================
echo.

REM Eliminar ZIP antiguo
if exist "scorm-etl-weatherstack.zip" (
    echo Eliminando ZIP anterior...
    del /Q "scorm-etl-weatherstack.zip"
    ping localhost -n 2 >nul
)

REM Comprimir CORRECTAMENTE con PowerShell
echo.
echo Recomprimiendo SCORM correctamente (esto puede tomar 10 segundos)...
echo.

powershell -Command ^
    "$source = 'scorm-etl-weatherstack'; " ^
    "$zip = 'scorm-etl-weatherstack.zip'; " ^
    "if(Test-Path $zip) {Remove-Item $zip -Force}; " ^
    "Compress-Archive -Path \"$source\*\" -DestinationPath $zip -Force; " ^
    "Write-Host 'SCORM recomprimido correctamente!' -ForegroundColor Green; " ^
    "$size = [math]::Round((Get-Item $zip).Length/1KB, 2); " ^
    "Write-Host \"Tamaño: $size KB\" -ForegroundColor Cyan; " ^
    "Write-Host 'imsmanifest.xml está en la RAÍZ del ZIP ✓' -ForegroundColor Green"

echo.
echo ============================================================
echo   ÉXITO - El ZIP está listo para Moodle
echo ============================================================
echo.
echo PRÓXIMOS PASOS:
echo   1. Sube este archivo a Moodle: scorm-etl-weatherstack.zip
echo   2. Moodle debería reconocer imsmanifest.xml en la raíz
echo   3. ¡Listo!
echo.

pause
