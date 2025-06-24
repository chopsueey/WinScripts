$InterfaceAlias = "Ethernet"
$IPv4Address = "192.168.1.100"
$PrefixLength = 24                   # For 255.255.255.0
$Gateway = "192.168.1.1"
$DnsServers = @("1.1.1.1", "8.8.8.8")

Write-Host "Setting static IP on interface: $InterfaceAlias"

New-NetIPAddress -InterfaceAlias $InterfaceAlias -IPAddress $IPv4Address -PrefixLength $PrefixLength -DefaultGateway $Gateway -ErrorAction SilentlyContinue

Set-DnsClientServerAddress -InterfaceAlias $InterfaceAlias -ServerAddresses $DnsServers