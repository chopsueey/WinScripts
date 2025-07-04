param (
    [string]$isoFile,
    [string]$iso_edition,
    [string]$version_name,
    [string]$nameSwitch,
    [string]$script_path,
    [string]$vmName,
    [string]$passPlainText,
    [int]$MemoryStartupGB,
    [int]$VMProcessorCount,
    [int]$VHDXSizeGB,
    [string]$IPAddress,
    [int]$PrefixLength,
    [string]$DefaultGateway,
    [string]$DnsAddresses,
    [string]$NetworkCategory
)

Get-Location
Set-Location $script_path
Get-Location

Write-Host "`n--- DEBUG: Calling New-VMFromWindowsImage.ps1 ---"
Write-Host "isoFile: $isoFile"
Write-Host "Edition: $iso_edition"
Write-Host "VMName: $vmName"
Write-Host "VHDXSizeBytes: $($VHDXSizeGB * 1GB)"
Write-Host "AdministratorPassword: $passPlainText"
Write-Host "Version: $version_name"
Write-Host "MemoryStartupBytes: $($MemoryStartupGB * 1GB)"
Write-Host "VMProcessorCount: $VMProcessorCount"
Write-Host "VMSwitchName: $nameSwitch"

Write-Host "Installing $iso_edition..."

& "$PSScriptRoot\New-VMFromWindowsImage.ps1" `
    -SourcePath $isoFile `
    -Edition $iso_edition `
    -VMName $vmName `
    -VHDXSizeBytes ($VHDXSizeGB * 1GB) `
    -AdministratorPassword $passPlainText `
    -Version $version_name `
    -MemoryStartupBytes ($MemoryStartupGB * 1GB) `
    -VMProcessorCount $VMProcessorCount `
    -VMSwitchName $nameSwitch

$dnsArray = $DnsAddresses -split ',' | ForEach-Object { $_.Trim() }

$sess = & "$PSScriptRoot\New-VMSession.ps1" -VMName $vmName -AdministratorPassword $passPlainText

& "$PSScriptRoot\Set-NetIPAddressViaSession.ps1" `
    -Session $sess `
    -IPAddress $IPAddress `
    -PrefixLength $PrefixLength `
    -DefaultGateway $DefaultGateway `
    -DnsAddresses $dnsArray `
    -NetworkCategory $NetworkCategory

& "$PSScriptRoot\Enable-RemoteManagementViaSession.ps1" -Session $sess

Invoke-Command -Session $sess {
    echo "Hello, world! (from $env:COMPUTERNAME)"

    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

    choco install 7zip -y
}

Remove-PSSession -Session $sess
