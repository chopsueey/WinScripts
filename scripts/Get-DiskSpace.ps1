Write-Host "Getting disk space information..."

Get-WmiObject -Class Win32_LogicalDisk |
    Select-Object -Property DeviceID, @{Name="Size (GB)";Expression={[math]::Round($_.Size / 1GB, 2)}}, @{Name="Free Space (GB)";Expression={[math]::Round($_.FreeSpace / 1GB, 2)}} |
    Format-Table -AutoSize

Write-Host "Disk space information retrieved."
Read-Host "Press enter to exit"
