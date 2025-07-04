# Remote Restart Script (PowerShell 7+)
# Run on your local machine

$VMNameOrIP = "192.168.178.118"
$Username = "administrator"
$Password = "P@ssw0rd"


$SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential ($Username, $SecurePassword)

Read-Host "Press enter to exit"

Restart-Computer -ComputerName $VMNameOrIP -Credential $Cred -Force 


# if (Test-Connection -ComputerName $VMNameOrIP -Count 1 -Quiet) {
#     Write-Host "VM is reachable. Attempting remote restart..." -ForegroundColor Green

#     try {
#         Restart-Computer -ComputerName $VMNameOrIP -Credential $Cred -Force -Confirm:$false
#         Write-Host "Restart command sent successfully." -ForegroundColor Cyan
#     }
#     catch {
#         Write-Host "Failed to send restart command: $_" -ForegroundColor Red
#     }
# }
# else {
#     Write-Host "VM is not reachable. Check network or IP address." -ForegroundColor Yellow
# }
