param (
    [string]$isoFile,
    [string]$vmName,
    [string]$pass,
    [string]$iso_edition,
    [string]$version_name,
    [string]$nameSwitch,
    [string]$script_path,
    # New parameters for numerical and IP settings
    [int]$MemoryStartupGB,       # Expects an integer, e.g., 4
    [int]$VMProcessorCount,      # Expects an integer, e.g., 2
    [int]$VHDXSizeGB,           # Expects an integer, e.g., 60
    [string]$IPAddress,
    [int]$PrefixLength,
    [string]$DefaultGateway,
    [string]$DnsAddresses,      # Will receive "8.8.8.8,8.8.4.4" as a string
    [string]$NetworkCategory
)

# $isoFile = 'C:\ISOs\Windows-Server-2025.iso'
# $vmName = 'ServerTest'
# $pass = 'P@ssw0rd'
Get-Location
# Will see if this still works as .exe file
Set-Location $script_path
Get-Location
Write-Host "`n--- DEBUG: Calling New-VMFromWindowsImage.ps1 ---"
Write-Host "isoFile: $isoFile"
Write-Host "Edition: $iso_edition"
Write-Host "VMName: $vmName"
Write-Host "VHDXSizeBytes: $($VHDXSizeGB * 1GB)"
Write-Host "AdministratorPassword: $pass"
Write-Host "Version: $version_name"
Write-Host "MemoryStartupBytes: $($MemoryStartupGB * 1GB)"
Write-Host "VMProcessorCount: $VMProcessorCount"
Write-Host "VMSwitchName: $nameSwitch"

write-host "Installing $iso_edition..."

.\New-VMFromWindowsImage.ps1 `
    -SourcePath $isoFile `
    -Edition $iso_edition `
    -VMName $vmName `
    -VHDXSizeBytes ($VHDXSizeGB * 1GB) ` # Convert GB to bytes for VHDX
    -AdministratorPassword $pass `
    -Version $version_name `
    -MemoryStartupBytes ($MemoryStartupGB * 1GB) ` # Convert GB to bytes for RAM
    -VMProcessorCount $VMProcessorCount `
    -VMSwitchName 'Internet'

# Split DNS addresses if they come as a comma-separated string
$dnsArray = $DnsAddresses -split ',' | ForEach-Object { $_.Trim() }

$sess = .\New-VMSession.ps1 -VMName $vmName -AdministratorPassword $pass

.\Set-NetIPAddressViaSession.ps1 `
    -Session $sess `
    -IPAddress $IPAddress `
    -PrefixLength $PrefixLength `
    -DefaultGateway $DefaultGateway `
    -DnsAddresses $dnsArray ` # Use the array here
    -NetworkCategory $NetworkCategory

.\Enable-RemoteManagementViaSession.ps1 -Session $sess

# You can run any commands on VM with Invoke-Command:
Invoke-Command -Session $sess {
    echo "Hello, world! (from $env:COMPUTERNAME)"

    # Install chocolatey
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

    # Install 7-zip
    choco install 7zip -y
}

Remove-PSSession -Session $sess