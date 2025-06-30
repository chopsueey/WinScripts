param (
    [string]$IsoPath
)

$ErrorActionPreference = 'Stop' # Critical for catching errors

try {
    $drive_letter = (Mount-DiskImage -ImagePath $IsoPath -PassThru | Get-Volume).DriveLetter

    # Get all image names and convert them to JSON
    $image_names_list = @(Get-WindowsImage -ImagePath "$($drive_letter):\sources\install.wim" | Select-Object -ExpandProperty ImageName)
    $image_names_list | ConvertTo-Json -Depth 10 -Compress
    
    Dismount-DiskImage -ImagePath $IsoPath
}
catch {
    # Write the error to the PowerShell error stream (which subprocess.run captures in stderr)
    Write-Error $_.Exception.Message
    exit 1 # Indicate an error to Python by exiting with a non-zero code
}