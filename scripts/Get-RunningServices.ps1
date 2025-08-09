Write-Host "Getting running services..."

Get-Service | Where-Object { $_.Status -eq "Running" } | Format-Table -AutoSize

Write-Host "Running services retrieved."
Read-Host "Press enter to exit"
