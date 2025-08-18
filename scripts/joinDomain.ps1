#Requires -RunAsAdministrator
<#
.SYNOPSIS
Joins a computer to an Active Directory domain.

.DESCRIPTION
This script joins a computer to a specified Active Directory domain.
It performs prerequisite checks for admin privileges and DNS resolution of the domain.

.PARAMETER DomainName
The fully qualified domain name of the domain to join.

.PARAMETER Credential
The domain user credential with permissions to join computers to the domain.

.PARAMETER OUPath
The distinguished name of the OU to create the computer object in.
e.g., "OU=Workstations,DC=yourdomain,DC=com"

.PARAMETER Restart
Switch to automatically restart the computer after the domain join.

.EXAMPLE
.\joinDomain.ps1 -DomainName 'ad.contoso.com' -Credential (Get-Credential) -Restart
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [Parameter(Mandatory=$true)]
    [string]$DomainName,

    [Parameter(Mandatory=$false)] # Now optional
    [System.Management.Automation.PSCredential]$Credential,

    [string]$OUPath,

    [switch]$Restart
)

# If credential is not provided via parameter, prompt for it
if (-not $PSBoundParameters.ContainsKey('Credential')) {
    try {
        $Credential = Get-Credential -Message "Enter credentials to join domain '$DomainName'"
        if (-not $Credential) {
            Write-Host "FATAL: Credentials are required to join a domain. Aborting."
            exit 1
        }
    } catch {
        Write-Host "FATAL: Could not get credentials. Aborting."
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

if (-not (Test-AdminPrivileges)) {
    Write-ErrorLog "This script must be run with Administrator privileges."
    exit 1
}
Write-Log "Administrator check passed."

if (-not (Test-DnsResolution -DomainName $DomainName)) {
    # The function writes the specific error
    exit 1
}
Write-Log "Domain DNS resolution check passed."

# --- Main Logic ---
try {
    $joinParams = @{
        DomainName = $DomainName
        Credential = $Credential
        ErrorAction = 'Stop'
    }
    if ($PSBoundParameters.ContainsKey('OUPath')) {
        $joinParams.Add('OUPath', $OUPath)
    }
    if ($Restart.IsPresent) {
        $joinParams.Add('Restart', $true)
    }

    if ($PSCmdlet.ShouldProcess("computer '$env:COMPUTERNAME'", "join to domain '$DomainName'")) {
        Write-Log "Attempting to join domain '$DomainName'..."
        Add-Computer @joinParams
        Write-Log "Successfully joined domain '$DomainName'."
        if ($Restart.IsPresent) {
            Write-Log "The computer will now restart."
        } else {
            Write-Log "A restart is required for the changes to take full effect."
        }
    }
}
catch {
    Write-ErrorLog "Failed to join domain. ERROR: $($_.Exception.Message)"
    exit 1
}
