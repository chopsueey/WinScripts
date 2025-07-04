# This script should be run on the client machine, with Administrator privileges.

Write-Host "--- Enabling PowerShell Remoting (WinRM) for Domain-Joined Client ---"
Write-Host "This will configure the system to securely receive PowerShell remote commands."

try {
    # This cmdlet configures the computer to receive PowerShell remote commands.
    # It performs several operations:
    # - Starts the WinRM service.
    # - Sets the WinRM service startup type to Automatic.
    # - Creates a listener to accept requests on any IP address.
    # - Enables a firewall exception for WS-Management (WinRM) communications.
    #
    # -Force: Suppresses confirmation prompts.
    # -SkipNetworkProfileCheck: This is often useful, especially during initial setup or if a machine briefly detects a public network profile.
    #                         Once domain-joined, the network profile should ideally become 'DomainAuthenticated'.
    Enable-PSRemoting -Force -SkipNetworkProfileCheck -ErrorAction Stop

    Write-Host "Successfully enabled PowerShell Remoting."
    Write-Host "WinRM service should now be running and configured for secure remote access."
    Write-Host "Default authentication for domain-joined systems is Kerberos (most secure)."

}
catch {
    Write-Error "Failed to enable PowerShell Remoting: $($_.Exception.Message)"
    Write-Host "Please ensure:"
    Write-Host "- You are running PowerShell as Administrator."
    Write-Host "- The WinRM service is not manually disabled or blocked by other security software."
    Write-Host "- The client is able to communicate with the Domain Controller (for Kerberos authentication)."
}

Write-Host "`nTo verify WinRM is listening:"
Write-Host "winrm enumerate winrm/config/listener"
Write-Host "`nTo test remoting from your Domain Controller (or another administrative workstation):"
Write-Host "Test-WsMan -ComputerName $($env:COMPUTERNAME)"
Write-Host "Invoke-Command -ComputerName $($env:COMPUTERNAME) -ScriptBlock { hostname }"

Read-Host "Press enter to exit"
