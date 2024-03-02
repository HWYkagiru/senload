Write-Host "Starting senload..."
Start-Sleep -Seconds 1

# Download senload.exe
$url = 'https://github.com/HWYkagiru/senload/releases/download/senload/senload.exe'
$output = 'senload.exe'
Invoke-WebRequest -Uri $url -OutFile $output

# Check download
if ($?) {
    Write-Host "Senload downloaded successfully."
} else {
    Write-Host "Error: Failed to download senload.exe."
    exit
}

# Start senload.exe
Write-Host "Running senload..."
Start-Process -Wait -FilePath .\senload.exe

# Check if success
if ($?) {
    Write-Host "Senload executed successfully."
} else {
    Write-Host "Error: Failed to execute senload.exe."
    exit
}

Write-Host "Senload installed successfully."
pause
