Write-Host "Setting background to black..."

$BlackWallpaperPath = "$env:SystemRoot\Web\Wallpaper\BlackWallpaper.bmp"
# Create a black bitmap if it doesn't exist
if (-not (Test-Path $BlackWallpaperPath)) {
    Write-Host "Creating black wallpaper file..."
    Add-Type -AssemblyName System.Drawing
    $bmp = New-Object System.Drawing.Bitmap 1920, 1080
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.Clear([System.Drawing.Color]::Black)
    $bmp.Save($BlackWallpaperPath, [System.Drawing.Imaging.ImageFormat]::Bmp)
    $g.Dispose()
    $bmp.Dispose()
}

# Apply the wallpaper (Current User)
Write-Host "Applying wallpaper..."
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value $BlackWallpaperPath
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

Write-Host "Background set to black."
Read-Host "Press enter to exit"
