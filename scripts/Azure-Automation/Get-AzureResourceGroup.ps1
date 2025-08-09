# This script lists all Azure Resource Groups.

Write-Host "Getting Azure Resource Groups..."

try {
    # Check if the user is connected to Azure
    $context = Get-AzContext
    if ($null -eq $context) {
        Write-Error "You are not connected to Azure. Please run Connect-Azure.ps1 first."
    }
    else {
        Get-AzResourceGroup | Format-Table -AutoSize
        Write-Host "Successfully retrieved Resource Groups."
    }
}
catch {
    Write-Error "Failed to get Azure Resource Groups. Error: $($_.Exception.Message)"
}

Read-Host "Press enter to exit"
