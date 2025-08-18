#Requires -RunAsAdministrator
<#
.SYNOPSIS
Installs and configures an Active Directory Domain Controller.

.DESCRIPTION
This script installs the Active Directory Domain Services role and promotes the server to a Domain Controller for a new forest.
It performs prerequisite checks for administrator privileges and a static IP address.

.PARAMETER DomainName
The fully qualified domain name for the new forest (e.g., 'ad.contoso.com').

.PARAMETER SafeModeAdministratorPassword
The password for the Directory Services Restore Mode (DSRM). The script will prompt for it if not provided.

.PARAMETER DomainMode
The domain functional level. Defaults to 'WinThreshold'.

.PARAMETER ForestMode
The forest functional level. Defaults to 'WinThreshold'.

.EXAMPLE
.\setupAD.ps1 -DomainName 'ad.contoso.com'
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [Parameter(Mandatory=$true)]
    [string]$DomainName,

    [Parameter(Mandatory=$false)] # Now optional
    [System.Security.SecureString]$SafeModeAdministratorPassword,

    [ValidateSet("Win2008", "Win2008R2", "Win2012", "Win2012R2", "WinThreshold")]
    [string]$DomainMode = "WinThreshold",

    [ValidateSet("Win2008", "Win2008R2", "Win2012", "Win2012R2", "WinThreshold")]
    [string]$ForestMode = "WinThreshold"
)

# If password is not provided via parameter, prompt for it
if (-not $PSBoundParameters.ContainsKey('SafeModeAdministratorPassword')) {
    try {
        $SafeModeAdministratorPassword = Read-Host -AsSecureString -Prompt "Enter the Directory Services Restore Mode (DSRM) password"
        if (-not $SafeModeAdministratorPassword) {
            Write-Host "FATAL: DSRM password is required. Aborting."
            exit 1
        }
    } catch {
        Write-Host "FATAL: Could not get DSRM password. Aborting."
        exit 1
    }
}

# Import the administration module
try {
    Import-Module (Join-Path $PSScriptRoot "modules\WinAdmin.psm1") -ErrorAction Stop
}
catch {
    Write-Host "FATAL: Could not import WinAdmin module. Ensure 'WinAdmin.psm1' exists in the 'modules' subdirectory. ERROR: $($_.Exception.Message)"
    exit 1
}

# --- Prerequisite Checks ---
Write-Log "Performing prerequisite checks..."

# Check for Admin privileges - Note: #Requires -RunAsAdministrator is the primary guard
if (-not (Test-AdminPrivileges)) {
    Write-ErrorLog "This script must be run with Administrator privileges."
    exit 1
}
Write-Log "Administrator check passed."

# Check for a static IP address
if (-not (Test-StaticIPAddress)) {
    # The function itself writes the specific error
    exit 1
}
Write-Log "Static IP address check passed."

# --- Main Logic ---
try {
    # Derive NetBIOS name from the domain name (takes the first part of the FQDN)
    $netbiosName = ($DomainName.Split('.'))[0].ToUpper()
    Write-Log "Derived NetBIOS Name: $netbiosName"

    if ($PSCmdlet.ShouldProcess("server '$env:COMPUTERNAME'", "Install AD Domain Services and promote to Domain Controller for domain '$DomainName'")) {

        Write-Log "Installing Active Directory Domain Services role..."
        Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -ErrorAction Stop
        Write-Log "AD Domain Services role installed successfully."

        Write-Log "Promoting server to a Domain Controller for forest '$DomainName'..."
        Install-ADDSForest `
            -DomainName $DomainName `
            -DomainNetbiosName $netbiosName `
            -DomainMode $DomainMode `
            -ForestMode $ForestMode `
            -SafeModeAdministratorPassword $SafeModeAdministratorPassword `
            -InstallDns:$true `
            -CreateDnsDelegation:$false `
            -NoRebootOnCompletion:$false `
            -Force:$true `
            -ErrorAction Stop

        Write-Log "Domain Controller promotion successful. The server will restart automatically."
    }
}
catch {
    Write-ErrorLog "Failed to set up Active Directory. ERROR: $($_.Exception.Message)"
    exit 1
}
