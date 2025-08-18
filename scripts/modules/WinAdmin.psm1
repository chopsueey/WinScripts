# WinAdmin PowerShell Module
#
# This module provides a collection of reusable functions to standardize
# and simplify administrative scripts. It includes functions for logging,
# prerequisite checking, and other common operations.
#

# --- Logging Functions ---

function Write-Log {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [string]$Message,
        [string]$Level = "INFO"
    )
    process {
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Write-Output "[$timestamp] [$Level] $Message"
    }
}

function Write-VerboseLog {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [string]$Message
    )
    process {
        Write-Log -Message $Message -Level "VERBOSE"
    }
}

function Write-ErrorLog {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [string]$Message
    )
    process {
        Write-Log -Message $Message -Level "ERROR"
        Write-Error $Message
    }
}

# --- Prerequisite Checking Functions ---

function Test-AdminPrivileges {
    [CmdletBinding()]
    param ()
    try {
        $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
        $isAdmin = (New-Object Security.Principal.WindowsPrincipal $currentUser).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
        return $isAdmin
    }
    catch {
        Write-ErrorLog -Message "Could not determine administrator status. Error: $($_.Exception.Message)"
        return $false
    }
}

function Test-StaticIPAddress {
    [CmdletBinding()]
    param()

    $adapters = Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }
    if (-not $adapters) {
        Write-ErrorLog "No active network adapters found."
        return $false
    }

    $staticIPFound = $false
    foreach ($adapter in $adapters) {
        # Check for non-DHCP assigned IPv4 addresses
        $ipAddresses = Get-NetIPAddress -InterfaceIndex $adapter.InterfaceIndex -AddressFamily IPv4 -ErrorAction SilentlyContinue
        foreach($ip in $ipAddresses){
            if($ip.PrefixOrigin -ne 'Dhcp'){
                Write-Log "Static IP address $($ip.IPAddress) found on adapter '$($adapter.Name)'."
                $staticIPFound = $true
                # We can break here since we found at least one
                break
            }
        }
        if($staticIPFound){
            break
        }
    }

    if(-not $staticIPFound){
        Write-ErrorLog "No static IPv4 address found on any active adapter. A static IP is required for a Domain Controller."
    }

    return $staticIPFound
}

function Test-DnsResolution {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$DomainName
    )

    try {
        # We query for Service Records (SRV) for Kerberos, which is a reliable way to check for a domain controller.
        $result = Resolve-DnsName -Name "_kerberos._tcp.$DomainName" -Type SRV -ErrorAction Stop
        if ($result) {
            Write-Log "DNS resolution for domain '$DomainName' successful. Found DC: $($result.NameTarget)"
            return $true
        }
    }
    catch {}

    Write-ErrorLog "DNS resolution for domain '$DomainName' failed. Could not find a Kerberos SRV record. Ensure this computer's DNS is set to a server that can resolve this domain."
    return $false
}

function Test-NetworkAdapterExists {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$InterfaceAlias
    )

    $adapter = Get-NetAdapter -Name $InterfaceAlias -ErrorAction SilentlyContinue
    if ($adapter) {
        Write-Log "Network adapter '$InterfaceAlias' found."
        return $true
    }
    else {
        Write-ErrorLog "Network adapter with alias '$InterfaceAlias' not found."
        return $false
    }
}

# --- Module Exports ---
# Export all functions to make them available to scripts that import this module.
Export-ModuleMember -Function *-*
