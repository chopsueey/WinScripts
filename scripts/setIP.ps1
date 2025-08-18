#Requires -RunAsAdministrator
<#
.SYNOPSIS
Configures a static IP address for a network adapter.

.DESCRIPTION
This script sets a static IPv4 address, subnet mask, default gateway, and DNS servers for a specified network adapter.
It clears any existing IP and DNS configurations before applying the new settings.

.PARAMETER InterfaceAlias
The name of the network adapter to configure (e.g., 'Ethernet').

.PARAMETER IPAddress
The static IPv4 address to set.

.PARAMETER PrefixLength
The subnet mask prefix length (e.g., 24 for 255.255.255.0).

.PARAMETER Gateway
The default gateway address.

.PARAMETER DnsServers
An array of DNS server addresses.

.EXAMPLE
.\setIP.ps1 -InterfaceAlias 'Ethernet' -IPAddress '192.168.1.100' -PrefixLength 24 -Gateway '192.168.1.1' -DnsServers '8.8.8.8', '1.1.1.1'
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [Parameter(Mandatory=$true)]
    [string]$InterfaceAlias,

    [Parameter(Mandatory=$true)]
    [string]$IPAddress,

    [Parameter(Mandatory=$true)]
    [int]$PrefixLength,

    [string]$Gateway,

    [string[]]$DnsServers
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

if (-not (Test-NetworkAdapterExists -InterfaceAlias $InterfaceAlias)) {
    # The function writes the specific error
    exit 1
}
Write-Log "Network adapter check passed."


# --- Main Logic ---
try {
    if ($PSCmdlet.ShouldProcess("network adapter '$InterfaceAlias'", "Set static IP to '$IPAddress'")) {

        Write-Log "Clearing any existing IP addresses from '$InterfaceAlias'..."
        Get-NetIPAddress -InterfaceAlias $InterfaceAlias -AddressFamily IPv4 | Remove-NetIPAddress -Confirm:$false -ErrorAction SilentlyContinue

        Write-Log "Setting IP address..."
        $ipParams = @{
            InterfaceAlias = $InterfaceAlias
            IPAddress      = $IPAddress
            PrefixLength   = $PrefixLength
            ErrorAction    = 'Stop'
        }
        if ($PSBoundParameters.ContainsKey('Gateway')) {
            $ipParams.Add('DefaultGateway', $Gateway)
        }
        New-NetIPAddress @ipParams

        if ($PSBoundParameters.ContainsKey('DnsServers')) {
            Write-Log "Setting DNS servers to $($DnsServers -join ', ')..."
            Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $DnsServers -ErrorAction Stop
        } else {
            Write-Log "No DNS servers specified, clearing existing DNS settings."
            Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ResetServerAddresses -ErrorAction Stop
        }

        Write-Log "Restarting network adapter '$InterfaceAlias' to apply changes..."
        Restart-NetAdapter -Name $InterfaceAlias -Confirm:$false

        Write-Log "IP configuration complete for '$InterfaceAlias'."
    }
}
catch {
    Write-ErrorLog "Failed to set IP configuration. ERROR: $($_.Exception.Message)"
    exit 1
}
