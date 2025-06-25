Write-Host "Interface Names:"
Write-Host ""
(Get-NetAdapter | Select-Object -Property Name).Name
Write-Host ""

Write-Host "Choose the interface"
Write-Host ""

$InterfaceAlias = Read-Host "Interface name"
$IPv4Address = Read-Host "New IP"
$PrefixLength = [int](Read-Host "Cidr/Prefix Length (e.g: 24)")                   # For 255.255.255.0
$Gateway = Read-Host "Gateway"
$DnsServers = @("1.1.1.1", "8.8.8.8")

Write-Host "Setting static IP on interface: $InterfaceAlias"

New-NetIPAddress -InterfaceAlias $InterfaceAlias -IPAddress $IPv4Address -PrefixLength $PrefixLength -DefaultGateway $Gateway -ErrorAction SilentlyContinue

Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $DnsServers