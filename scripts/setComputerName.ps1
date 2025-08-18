#Requires -RunAsAdministrator
<#
.SYNOPSIS
Renames the local computer.

.DESCRIPTION
This script changes the name of the computer and can optionally restart it to apply the change.

.PARAMETER NewName
The new name for the computer.

.PARAMETER Restart
A switch that, if present, causes the computer to restart after the rename operation.

.EXAMPLE
.\setComputerName.ps1 -NewName 'NEW-PC-NAME' -Restart
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [Parameter(Mandatory=$true)]
    [string]$NewName,

    [switch]$Restart
)

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
    if ($PSCmdlet.ShouldProcess("computer '$env:COMPUTERNAME'", "Rename to '$NewName'")) {
        Write-Log "Renaming computer to '$NewName'..."
        Rename-Computer -NewName $NewName -Force -ErrorAction Stop

        Write-Log "Computer name has been changed to '$NewName'."

        if ($Restart.IsPresent) {
            Write-Log "Restarting computer to apply the new name..."
            Restart-Computer -Force
        } else {
            Write-Log "A restart is required for the name change to take effect."
        }
    }
}
catch {
    Write-ErrorLog "Failed to rename computer. ERROR: $($_.Exception.Message)"
    exit 1
}
