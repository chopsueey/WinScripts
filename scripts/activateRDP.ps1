$RdpRegKey = "HKLM:\System\CurrentControlSet\Control\Terminal Server"
$RdpFirewallRule = "Remote Desktop"

try {
    $rdpStatus = Get-ItemProperty -Path $RdpRegKey -Name "fDenyTSConnections" -ErrorAction Stop

    if ($rdpStatus.fDenyTSConnections -eq 0) {
        # RDP is currently enabled, so we will disable it
        Write-Host "Remote Desktop is currently ENABLED. Disabling it now..."
        Set-ItemProperty -Path $RdpRegKey -Name "fDenyTSConnections" -Value 1
        Disable-NetFirewallRule -DisplayGroup $RdpFirewallRule
        Write-Host "Remote Desktop has been DISABLED."
    } else {
        # RDP is currently disabled, so we will enable it
        Write-Host "Remote Desktop is currently DISABLED. Enabling it now..."
        Set-ItemProperty -Path $RdpRegKey -Name "fDenyTSConnections" -Value 0
        Enable-NetFirewallRule -DisplayGroup $RdpFirewallRule
        Write-Host "Remote Desktop has been ENABLED."
    }
}
catch {
    # If the key doesn't exist, fDenyTSConnections is effectively 1 (disabled)
    Write-Host "Remote Desktop is currently DISABLED (registry key not found). Enabling it now..."
    Set-ItemProperty -Path $RdpRegKey -Name "fDenyTSConnections" -Value 0
    Enable-NetFirewallRule -DisplayGroup $RdpFirewallRule
    Write-Host "Remote Desktop has been ENABLED."
}

Read-Host "Press enter to exit"
