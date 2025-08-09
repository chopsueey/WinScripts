# This script lists all Azure Storage Accounts.

Write-Host "Getting Azure Storage Accounts..."

try {
    # Check if the user is connected to Azure
    $context = Get-AzContext
    if ($null -eq $context) {
        Write-Error "You are not connected to Azure. Please run Connect-Azure.ps1 first."
    }
    else {
        Get-AzStorageAccount | Format-Table -AutoSize
        Write-Host "Successfully retrieved Storage Accounts."
    }
}
catch {
    Write-Error "Failed to get Azure Storage Accounts. Error: $($_.Exception.Message)"
}

Read-Host "Press enter to exit"
