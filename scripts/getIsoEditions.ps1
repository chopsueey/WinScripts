param (
    [string]$IsoPath,
    [string]$AppRootPath
)

write-host $AppRootPath

$drive_letter = (Mount-DiskImage -ImagePath $IsoPath -PassThru | Get-Volume).DriveLetter

$image_name = Get-WindowsImage -ImagePath "$($drive_letter):\sources\install.wim"

$image_names_list = @($image_name | Select-Object -ExpandProperty ImageName)

$output_json_path = Join-Path $AppRootPath "image_names.json"

$image_names_list | ConvertTo-Json -Depth 10 | Set-Content -Path $output_json_path -Encoding UTF8

Dismount-DiskImage -ImagePath $IsoPath