#Requires -RunAsAdministrator
<#
.SYNOPSIS
Creates a new local user account.

.DESCRIPTION
This script creates a new local user account on the machine. It can also add the user to local groups.

.PARAMETER UserName
The username for the new local account.

.PARAMETER Password
The password for the new user. This must be a SecureString.

.PARAMETER FullName
The full name of the user.

.PARAMETER Description
A description for the user account.

.PARAMETER AddToGroup
An array of local groups to which the user should be added (e.g., 'Administrators', 'Remote Desktop Users').

.EXAMPLE
$secPass = Read-Host -AsSecureString -Prompt "Enter password"
.\Create-LocalUser.ps1 -UserName 'testuser' -Password $secPass -AddToGroup 'Users', 'Remote Desktop Users'
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [Parameter(Mandatory=$true)]
    [string]$UserName,

    [Parameter(Mandatory=$false)] # Now optional
    [System.Security.SecureString]$Password,

    [string]$FullName,

    [string]$Description,

    [string[]]$AddToGroup
)

# If password is not provided via parameter, prompt for it
if (-not $PSBoundParameters.ContainsKey('Password')) {
    try {
        $Password = Read-Host -AsSecureString -Prompt "Enter password for new user '$UserName'"
        if (-not $Password) {
            Write-Host "FATAL: A password is required. Aborting."
            exit 1
        }
    } catch {
        Write-Host "FATAL: Could not get password. Aborting."
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

# --- Main Logic ---
try {
    if ($PSCmdlet.ShouldProcess("local user '$UserName'", "Create")) {
        Write-Log "Creating local user '$UserName'..."

        $userParams = @{
            Name = $UserName
            Password = $Password
            ErrorAction = 'Stop'
        }
        if ($PSBoundParameters.ContainsKey('FullName')) { $userParams.Add('FullName', $FullName) }
        if ($PSBoundParameters.ContainsKey('Description')) { $userParams.Add('Description', $Description) }

        New-LocalUser @userParams

        Write-Log "User '$UserName' created successfully."

        if ($PSBoundParameters.ContainsKey('AddToGroup')) {
            foreach ($group in $AddToGroup) {
                if ($PSCmdlet.ShouldProcess("user '$UserName'", "Add to group '$group'")) {
                    Write-Log "Adding user '$UserName' to group '$group'..."
                    Add-LocalGroupMember -Group $group -Member $UserName -ErrorAction Stop
                    Write-Log "Successfully added '$UserName' to group '$group'."
                }
            }
        }
    }
}
catch {
    Write-ErrorLog "Failed to create or modify local user '$UserName'. ERROR: $($_.Exception.Message)"
    exit 1
}
