# --- User Input Section ---
Write-Host "--- Network Configuration ---"
Write-Host ""
(Get-NetAdapter | Select-Object -Property Name).Name
Write-Host ""

$InterfaceAlias = Read-Host "Enter the name of the network interface (e.g., Ethernet)"

$DnsPrimary = Read-Host "Enter the primary DNS server IPv4 address"
$DnsSecondary = Read-Host "Enter the secondary DNS server IPv4 address (leave blank if none)"

$ServerDnsServers = @($DnsPrimary)
if ($DnsSecondary) {
    $ServerDnsServers += $DnsSecondary
}

Write-Host "`n--- Active Directory Configuration ---"
$DomainName = Read-Host "Enter the full domain name (e.g., yourdomain.local)"
$DomainNetBiosName = Read-Host "Enter the NetBIOS name for the domain (e.g., YOURDOMAIN)"

# Get a secure password for DSRM
$SafeModeAdminPassword = Read-Host -AsSecureString -Prompt "Enter the Directory Services Restore Mode (DSRM) password"

Write-Host "`n--- DNS Forwarder Configuration ---"
$ForwarderPrimary = Read-Host "Enter the primary DNS forwarder IPv4 address (e.g., 1.1.1.1)"
$ForwarderSecondary = Read-Host "Enter the secondary DNS forwarder IPv4 address (e.g., 8.8.8.8) (leave blank if none)"

$DnsForwarderIPs = @($ForwarderPrimary)
if ($ForwarderSecondary) {
    $DnsForwarderIPs += $ForwarderSecondary
}

# --- Script Logic ---

Write-Host "`nSetting DNS Client Server Address..."
Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $ServerDnsServers -ErrorAction Stop

Write-Host "Disabling IPv6 on interface: $InterfaceAlias..."
Disable-NetAdapterBinding -Name $InterfaceAlias -ComponentID ms_tcpip6 -ErrorAction Stop

Write-Host "Installing Active Directory Domain Services feature..."
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools -IncludeAllSubFeature -ErrorAction Stop

Write-Host "Installing Active Directory Forest..."
Install-ADDSForest `
    -DomainName $DomainName `
    -DomainNetBiosName $DomainNetBiosName `
    -DomainMode WinThreshold `
    -ForestMode WinThreshold `
    -SkipPreChecks `
    -InstallDns:$true `
    -SafeModeAdministratorPassword $SafeModeAdminPassword `
    -Force -ErrorAction Stop

Write-Host "Registering DNS records..."
ipconfig /registerdns

Write-Host "Setting DNS Server Forwarders..."
Set-DnsServerForwarder -IPAddress $DnsForwarderIPs -ErrorAction Stop

Write-Host "`nScript execution complete."

Read-Host "Press enter to exit"
