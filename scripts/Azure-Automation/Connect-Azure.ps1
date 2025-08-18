#Requires -RunAsAdministrator
<#
.SYNOPSIS
Connects to an Azure account.

.DESCRIPTION
This script authenticates to Azure using an interactive browser login.
It will check if the required 'Az.Accounts' PowerShell module is installed and, if not, will prompt to install it.

.PARAMETER Force
A switch that, if present, will cause the script to install the 'Az.Accounts' module without prompting if it is not found.

.EXAMPLE
.\Connect-Azure.ps1
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [switch]$Force
)

# Import the administration module
try {
    # Note the relative path is different as this script is in a subdirectory
    Import-Module (Join-Path $PSScriptRoot "..\modules\WinAdmin.psm1") -ErrorAction Stop
}
catch {
    Write-Host "FATAL: Could not import WinAdmin module. Ensure 'WinAdmin.psm1' exists in the 'modules' subdirectory of the 'scripts' folder. ERROR: $($_.Exception.Message)"
    exit 1
}

# --- Prerequisite: Az.Accounts Module ---
try {
    Write-Log "Checking for 'Az.Accounts' PowerShell module..."
    $azModule = Get-Module -Name Az.Accounts -ListAvailable

    if (-not $azModule) {
        Write-Log "'Az.Accounts' module not found."

        $shouldInstall = $false
        if ($Force.IsPresent) {
            $shouldInstall = $true
        } else {
            $response = Read-Host "The 'Az.Accounts' module is required. Do you want to install it from the PowerShell Gallery? (y/n)"
            if ($response -eq 'y') {
                $shouldInstall = $true
            }
        }

        if ($shouldInstall) {
            if ($PSCmdlet.ShouldProcess("PowerShell Gallery", "Install module 'Az.Accounts'")) {
                Write-Log "Installing 'Az.Accounts' module. This may take a few moments..."
                # Installing for the current user is safer and doesn't require elevation.
                Install-Module -Name Az.Accounts -Repository PSGallery -Scope CurrentUser -AllowClobber -Force -ErrorAction Stop
                Write-Log "'Az.Accounts' module installed successfully."
            }
        } else {
            Write-ErrorLog "Cannot proceed without the 'Az.Accounts' module. Aborting."
            exit 1
        }
    } else {
        Write-Log "'Az.Accounts' module is already installed."
    }

    # --- Main Logic ---
    if ($PSCmdlet.ShouldProcess("Azure", "Connect to account")) {
        Write-Log "Attempting to connect to Azure. A browser window may open for authentication."
        Connect-AzAccount -ErrorAction Stop
        $context = Get-AzContext
        Write-Log "Successfully connected to Azure. Account: $($context.Account.Id), Tenant: $($context.Tenant.Id)"
    }
}
catch {
    Write-ErrorLog "An error occurred. ERROR: $($_.Exception.Message)"
    exit 1
}
