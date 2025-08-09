# This script creates a new Azure VM.

Write-Host "Creating a new Azure VM. This will take a few minutes."

# Parameters
$ResourceGroupName = Read-Host "Enter the Resource Group name"
$Location = Read-Host "Enter the location (e.g., westeurope)"
$VMName = Read-Host "Enter the VM name"
$AdminUsername = Read-Host "Enter the admin username"
$AdminPassword = Read-Host -AsSecureString "Enter the admin password"

try {
    # Check if the user is connected to Azure
    $context = Get-AzContext
    if ($null -eq $context) {
        Write-Error "You are not connected to Azure. Please run Connect-Azure.ps1 first."
    }
    else {
        Write-Host "Creating VM..."
        New-AzVm `
            -ResourceGroupName $ResourceGroupName `
            -Name $VMName `
            -Location $Location `
            -Credential (New-Object System.Management.Automation.PSCredential($AdminUsername, $AdminPassword)) `
            -OpenPublicIpAddress `
            -ImageName "Win2019Datacenter"

        Write-Host "VM '$VMName' created successfully."
    }
}
catch {
    Write-Error "Failed to create Azure VM. Error: $($_.Exception.Message)"
}

Read-Host "Press enter to exit"
