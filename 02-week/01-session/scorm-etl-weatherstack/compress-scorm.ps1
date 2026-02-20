# PowerShell Script para Empaquetar SCORM - ETL Weatherstack
# IMPORTANTE: Comprende los archivos EN LA RAIZ, NO la carpeta misma
# Uso: .\compress-scorm.ps1

param(
    [Parameter(Mandatory=$false)]
    [string]$SCORMPath = (Split-Path -Parent $PSCommandPath),
    
    [Parameter(Mandatory=$false)]
    [string]$OutputPath = (Split-Path -Parent (Split-Path -Parent $PSCommandPath))
)

function Show-Header {
    Write-Host "`n" -BackgroundColor DarkBlue -ForegroundColor White
    Write-Host "╔════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║   SCORM Packaging Script (CORRECCIÓN)          ║" -ForegroundColor Cyan
    Write-Host "║   ETL Weatherstack para Moodle                 ║" -ForegroundColor Cyan
    Write-Host "╚════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host "`n"
}

function Show-Info {
    param([string]$Message)
    Write-Host "ℹ️  $Message" -ForegroundColor Cyan
}

function Show-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Show-Error {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

# Main Script
Show-Header

# Validate paths
if (-not (Test-Path $SCORMPath)) {
    Show-Error "SCORM directory not found: $SCORMPath"
    exit 1
}

if (-not (Test-Path "$SCORMPath\imsmanifest.xml")) {
    Show-Error "imsmanifest.xml not found. Make sure you're in the SCORM package directory."
    exit 1
}

Show-Info "SCORM directory: $SCORMPath"
Show-Info "Output directory: $OutputPath"

# Get current date/time for backup naming
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$zipName = "scorm-etl-weatherstack.zip"
$zipBackupName = "scorm-etl-weatherstack_backup_$timestamp.zip"
$zipPath = Join-Path $OutputPath $zipName
$zipBackupPath = Join-Path $OutputPath $zipBackupName

# Backup existing ZIP if it exists
if (Test-Path $zipPath) {
    Show-Info "Existing ZIP found. Creating backup: $zipBackupName"
    try {
        Copy-Item $zipPath $zipBackupPath -Force
        Show-Success "Backup created: $zipBackupPath"
    }
    catch {
        Show-Error "Failed to create backup: $_"
    }
}

# Create new ZIP - IMPORTANTE: Comprimir archivos EN LA RAIZ, no la carpeta
try {
    Show-Info "Creating new SCORM package (with files in root)..."
    
    # Remove old zip if exists to avoid issues
    if (Test-Path $zipPath) {
        Remove-Item $zipPath -Force
    }
    
    # ⭐ CORRECCIÓN: Comprimir el contenido de la carpeta (*), no la carpeta misma
    Compress-Archive -Path "$SCORMPath\*" -DestinationPath $zipPath -Force -ErrorAction Stop
    
    # Get file info
    $fileInfo = Get-Item $zipPath
    $fileSizeMB = [math]::Round($fileInfo.Length / 1MB, 2)
    $fileSizeKB = [math]::Round($fileInfo.Length / 1KB, 2)
    
    Show-Success "ZIP package created successfully!"
    Write-Host "`n"
    Write-Host "╔════════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "║   PACKAGE DETAILS                              ║" -ForegroundColor Green
    Write-Host "╚════════════════════════════════════════════════╝" -ForegroundColor Green
    
    Write-Host "📦 File: $zipName"
    Write-Host "📍 Location: $zipPath"
    Write-Host "📊 Size: $fileSizeKB KB ($fileSizeMB MB)"
    Write-Host "🕐 Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    Write-Host "✅ imsmanifest.xml está en la RAÍZ del ZIP"
    Write-Host "`n"
    
    Write-Host "╔════════════════════════════════════════════════╗" -ForegroundColor Yellow
    Write-Host "║   NEXT STEPS - Upload to Moodle                ║" -ForegroundColor Yellow
    Write-Host "╚════════════════════════════════════════════════╝" -ForegroundColor Yellow
    Write-Host "`n"
    Write-Host "1. Log in to Moodle"
    Write-Host "2. Go to your course and enable 'Edit mode'"
    Write-Host "3. Click 'Add an activity or resource'"
    Write-Host "4. Search for and select 'SCORM'"
    Write-Host "5. Upload the ZIP file: $zipName"
    Write-Host "6. Click 'Save and display'"
    Write-Host "`n"
    
    # Open file explorer to show the file
    Show-Info "Opening file explorer..."
    Invoke-Item $OutputPath
}
catch {
    Show-Error "Failed to create ZIP package: $_"
    exit 1
}

Show-Success "Process completed successfully! 🎉"
Write-Host "`nPress any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
