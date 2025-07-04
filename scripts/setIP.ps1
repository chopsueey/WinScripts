# Write-Host "Interface Names:"
# Write-Host ""
# (Get-NetAdapter | Select-Object -Property Name).Name
# Write-Host ""

# Write-Host "Choose the interface"
# Write-Host ""

# $InterfaceAlias = Read-Host "Interface name"
# $IPv4Address = Read-Host "New IP"
# $PrefixLength = [int](Read-Host "Cidr/Prefix Length (e.g: 24)")                   # For 255.255.255.0
# $Gateway = Read-Host "Gateway"
# $DnsServers = @("1.1.1.1", "8.8.8.8")

# Write-Host "Setting static IP on interface: $InterfaceAlias"

# New-NetIPAddress -InterfaceAlias $InterfaceAlias -IPAddress $IPv4Address -PrefixLength $PrefixLength -DefaultGateway $Gateway -ErrorAction SilentlyContinue

# Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $DnsServers

# Write-Host "Interface Names:"
# Write-Host ""
# (Get-NetAdapter | Select-Object -Property Name).Name
# Write-Host ""

# Write-Host "Choose the interface"
# Write-Host ""

# $InterfaceAlias = Read-Host "Interface name"
# $IPv4Address = Read-Host "New IP"
# $PrefixLength = [int](Read-Host "Cidr/Prefix Length (e.g: 24)") # For 255.255.255.0
# $Gateway = Read-Host "Gateway"
# $DnsServers = @("1.1.1.1", "8.8.8.8")

# Write-Host "Setting static IP on interface: $InterfaceAlias"

# # --- Add this section to clear existing IP addresses ---
# Write-Host "Clearing existing IP addresses for $InterfaceAlias..."
# Get-NetIPAddress -InterfaceAlias $InterfaceAlias -AddressFamily IPv4 | Remove-NetIPAddress -Confirm:$false -ErrorAction SilentlyContinue

# # --- Add this section to clear existing DNS server addresses ---
# Write-Host "Clearing existing DNS server addresses for $InterfaceAlias..."
# Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ResetServerAddresses -ErrorAction SilentlyContinue


# New-NetIPAddress -InterfaceAlias $InterfaceAlias -IPAddress $IPv4Address -PrefixLength $PrefixLength -DefaultGateway $Gateway -ErrorAction SilentlyContinue

# Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $DnsServers

Write-Host "Interface Names:"
Write-Host ""
(Get-NetAdapter | Select-Object -Property Name).Name
Write-Host ""

Write-Host "Choose the interface"
Write-Host ""

$InterfaceAlias = Read-Host "Interface name"
$IPv4Address = Read-Host "New IP"
$PrefixLength = [int](Read-Host "Cidr/Prefix Length (e.g: 24)") # For 255.255.255.0
$Gateway = Read-Host "Gateway"
$DnsServers = @("1.1.1.1", "8.8.8.8")

Write-Host "Setting static IP on interface: $InterfaceAlias"

# --- Clear existing IP addresses ---
Write-Host "Clearing existing IP addresses for $InterfaceAlias..."
Get-NetIPAddress -InterfaceAlias $InterfaceAlias -AddressFamily IPv4 | Remove-NetIPAddress -Confirm:$false -ErrorAction SilentlyContinue

# --- Clear existing DNS server addresses ---
Write-Host "Clearing existing DNS server addresses for $InterfaceAlias..."
Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ResetServerAddresses -ErrorAction SilentlyContinue

# --- Disable DHCP ---
Write-Host "Disabling DHCP for IPv4 on $InterfaceAlias..."
Set-NetIPInterface -InterfaceAlias $InterfaceAlias -Dhcp Disabled -ErrorAction SilentlyContinue


New-NetIPAddress -InterfaceAlias $InterfaceAlias -IPAddress $IPv4Address -PrefixLength $PrefixLength -DefaultGateway $Gateway -ErrorAction SilentlyContinue

Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $DnsServers

# --- Restart the Network Adapter ---
Write-Host "Restarting network adapter '$InterfaceAlias' to apply changes..."
Disable-NetAdapter -Name $InterfaceAlias -Confirm:$false -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2 # Give it a moment to fully disable
Enable-NetAdapter -Name $InterfaceAlias -Confirm:$false -ErrorAction SilentlyContinue

Write-Host "IP configuration complete for $InterfaceAlias."

Read-Host "Press enter to exit"