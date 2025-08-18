#Requires -RunAsAdministrator
<#
.SYNOPSIS
Creates a new scheduled task.

.DESCRIPTION
This script simplifies the creation of a new scheduled task on the local machine.
It acts as a wrapper for the Register-ScheduledTask cmdlet, providing standardized logging.

.PARAMETER TaskName
The name for the new scheduled task.

.PARAMETER Action
The action to be performed by the scheduled task (e.g., created with New-ScheduledTaskAction).

.PARAMETER Trigger
The trigger that starts the task (e.g., created with New-ScheduledTaskTrigger).

.PARAMETER User
The user account to run the task under. Defaults to 'SYSTEM'.

.PARAMETER RunLevel
Specifies the security context. Use 'Highest' to run with elevated privileges.

.EXAMPLE
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-Command "& { Get-Process > C:\temp\procs.txt }"'
$trigger = New-ScheduledTaskTrigger -Daily -At 3am
.\New-ScheduledTask.ps1 -TaskName 'DailyProcessLog' -Action $action -Trigger $trigger
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [Parameter(Mandatory=$true)]
    [string]$TaskName,

    [Parameter(Mandatory=$true)]
    [CimInstance]$Action,

    [Parameter(Mandatory=$true)]
    [CimInstance[]]$Trigger,

    [string]$User = "SYSTEM",

    [ValidateSet('Limited', 'Highest')]
    [string]$RunLevel = 'Limited'
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
    if ($PSCmdlet.ShouldProcess("Scheduled Tasks", "Register new task '$TaskName'")) {
        Write-Log "Registering new scheduled task '$TaskName'..."

        $taskParams = @{
            TaskName = $TaskName
            Action = $Action
            Trigger = $Trigger
            User = $User
            RunLevel = $RunLevel
            ErrorAction = 'Stop'
        }

        Register-ScheduledTask @taskParams -Force

        Write-Log "Scheduled task '$TaskName' registered successfully."
    }
}
catch {
    Write-ErrorLog "Failed to register scheduled task '$TaskName'. ERROR: $($_.Exception.Message)"
    exit 1
}
