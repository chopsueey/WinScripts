#Requires -RunAsAdministrator
<#
.SYNOPSIS
Searches for recent errors and warnings in Windows Event Logs.

.DESCRIPTION
This script queries the specified Windows Event Logs for Critical, Error, and Warning events that have occurred within a given time frame.

.PARAMETER LogName
The name of the event log(s) to query. Defaults to 'System' and 'Application'.

.PARAMETER HoursSince
The number of hours in the past to search for events. Defaults to 24.

.EXAMPLE
.\Get-EventLogErrors.ps1 -HoursSince 1
#>
[CmdletBinding()]
param(
    [string[]]$LogName = @('System', 'Application'),
    [int]$HoursSince = 24
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
    Write-Log "WARNING: Administrator privileges are recommended to ensure all event logs can be read."
    # Don't exit, as some logs might still be readable.
} else {
    Write-Log "Administrator check passed."
}


# --- Main Logic ---
try {
    $startTime = (Get-Date).AddHours(-$HoursSince)
    Write-Log "Searching for Critical, Error, and Warning events in '$($LogName -join ', ')' logs since $startTime..."

    $filter = @{
        LogName = $LogName
        StartTime = $startTime
        Level = 1,2,3 # 1=Critical, 2=Error, 3=Warning
    }

    $events = Get-WinEvent -FilterHashtable $filter -ErrorAction SilentlyContinue

    if ($events) {
        Write-Log "Found $($events.Count) matching events."
        # Returning the object directly is more flexible than Format-Table
        $events | Select-Object TimeCreated, LogName, LevelDisplayName, ProviderName, Id, Message
    } else {
        Write-Log "No Critical, Error, or Warning events found in the specified logs within the last $HoursSince hours."
    }
}
catch {
    Write-ErrorLog "Failed to retrieve event log errors. ERROR: $($_.Exception.Message)"
}

Read-Host -Prompt "Press Enter to exit"
