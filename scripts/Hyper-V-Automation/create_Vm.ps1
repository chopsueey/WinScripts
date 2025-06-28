$isoFile = 'C:\ISOs\Windows-Server-2025.iso'
$vmName = 'W-Server2025'
$pass = 'P@ssw0rd'

.\New-VMFromWindowsImage.ps1 `
    -SourcePath $isoFile `
    -Edition 'Windows Server 2025 Standard Evaluation (Desktopdarstellung)' `
    -VMName $vmName `
    -VHDXSizeBytes 60GB `
    -AdministratorPassword $pass `
    -Version 'Server2025Standard' `
    -MemoryStartupBytes 4GB `
    -VMProcessorCount 2

$sess = .\New-VMSession.ps1 -VMName $vmName -AdministratorPassword $pass

.\Set-NetIPAddressViaSession.ps1 `
    -Session $sess `
    -IPAddress 10.0.0.10 `
    -PrefixLength 8 `
    -DefaultGateway 10.0.0.10 `
    -DnsAddresses '8.8.8.8','8.8.4.4' `
    -NetworkCategory 'Public'

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