<#
.SYNOPSIS
Retrieves a summary of the system's health.

.DESCRIPTION
This script gathers key performance and configuration metrics to provide a snapshot of the system's health.
It retrieves information about the OS, CPU, memory, disk space, uptime, and top processes.

.EXAMPLE
.\Get-SystemHealth.ps1 | Format-List
#>
[CmdletBinding()]
param()

# Import the administration module
try {
    Import-Module (Join-Path $PSScriptRoot "modules\WinAdmin.psm1") -ErrorAction Stop
}
catch {
    Write-Host "FATAL: Could not import WinAdmin module. Ensure 'WinAdmin.psm1' exists in the 'modules' subdirectory. ERROR: $($_.Exception.Message)"
    exit 1
}

try {
    Write-Log "Gathering system health information..."

    # --- OS and Uptime ---
    $osInfo = Get-CimInstance -ClassName Win32_OperatingSystem
    $uptime = (Get-Date) - $osInfo.LastBootUpTime
    $osVersion = "$($osInfo.Caption) $($osInfo.Version)"

    # --- CPU ---
    $cpuInfo = Get-CimInstance -ClassName Win32_Processor | Select-Object -First 1
    $cpuName = $cpuInfo.Name
    # This gets a snapshot of CPU usage. For a more accurate reading over time, this would need to be sampled.
    $cpuUsage = (Get-CimInstance -ClassName Win32_PerfFormattedData_PerfOS_Processor | Where-Object { $_.Name -eq '_Total' }).PercentProcessorTime

    # --- Memory ---
    $totalMemoryGB = [math]::Round($osInfo.TotalVisibleMemorySize / 1MB, 2)
    $freeMemoryGB = [math]::Round($osInfo.FreePhysicalMemory / 1MB, 2)
    $usedMemoryGB = $totalMemoryGB - $freeMemoryGB
    $memoryUsagePercent = [math]::Round(($usedMemoryGB / $totalMemoryGB) * 100, 2)

    # --- Disks ---
    $diskInfo = Get-CimInstance -ClassName Win32_LogicalDisk | Where-Object { $_.DriveType -eq 3 } | ForEach-Object {
        [pscustomobject]@{
            DeviceID = $_.DeviceID
            SizeGB = [math]::Round($_.Size / 1GB, 2)
            FreeSpaceGB = [math]::Round($_.FreeSpace / 1GB, 2)
            PercentFree = [math]::Round(($_.FreeSpace / $_.Size) * 100, 2)
        }
    }

    # --- Top Processes ---
    # Getting process CPU usage requires a delay, so this is a simplified version.
    $processes = Get-Process
    $topCpuProcesses = $processes | Sort-Object -Property CPU -Descending | Select-Object -First 5 | Select-Object Name, Id, @{Name="CPU_s"; Expression={$_.CPU}}
    $topMemoryProcesses = $processes | Sort-Object -Property WorkingSet -Descending | Select-Object -First 5 | Select-Object Name, Id, @{Name="Memory_MB"; Expression={[math]::Round($_.WorkingSet / 1MB, 2)}}

    # --- Output Object ---
    $healthReport = [pscustomobject]@{
        OSVersion = $osVersion
        Uptime = "$($uptime.Days) days, $($uptime.Hours) hours, $($uptime.Minutes) minutes"
        CPUName = $cpuName
        CurrentCpuUsagePercent = $cpuUsage
        TotalMemoryGB = $totalMemoryGB
        UsedMemoryGB = $usedMemoryGB
        MemoryUsagePercent = "$memoryUsagePercent %"
        Disks = $diskInfo
        TopCpuProcesses = $topCpuProcesses
        TopMemoryProcesses = $topMemoryProcesses
    }

    Write-Log "System health report generated."
    return $healthReport
}
catch {
    Write-ErrorLog "Failed to get system health. ERROR: $($_.Exception.Message)"
    exit 1
}
