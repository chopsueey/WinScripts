# --- User Input ---
Write-Host "--- Domain Join Configuration ---"

# The fully qualified domain name (FQDN) of your new domain
$DomainName = Read-Host "Enter the FQDN of your Active Directory Domain (e.g., zm.modul3.local)"

# Get credentials for a domain user with permission to join computers
# This will open a pop-up window for username and password input
$DomainJoinCredential = Get-Credential -Message "Enter credentials for a domain user with permission to join computers"

# (Optional) You can specify an Organizational Unit (OU) path if you want the computer to go into a specific OU
# $OUPath = Read-Host "Enter the OU path (e.g., OU=Workstations,DC=zm,DC=modul3,DC=local) (leave blank for default 'Computers' container)"

# (Optional) Rename the computer before joining the domain.
# This will require an additional restart if done separately, but Add-Computer can do it at once.
# $NewComputerName = Read-Host "Enter the new computer name (leave blank to keep current name)"


Write-Host "`nAttempting to join '$env:COMPUTERNAME' to domain '$DomainName'..."

try {
    # Join the computer to the domain
    # -Force: Suppresses prompts for existing domain membership or workgroup.
    # -Restart: Restarts the computer after successful join. This is crucial for changes to take effect.

    # If you want to rename the computer at the same time:
    # if ($NewComputerName) {
    #     Add-Computer -DomainName $DomainName -Credential $DomainJoinCredential -NewName $NewComputerName -Restart -Force -ErrorAction Stop
    # } else {
    #     Add-Computer -DomainName $DomainName -Credential $DomainJoinCredential -Restart -Force -ErrorAction Stop
    # }

    # Standard domain join (without renaming at the same time, if not needed)
    Add-Computer -DomainName $DomainName -Credential $DomainJoinCredential -Restart -Force -ErrorAction Stop

    # If you want to specify an OU, uncomment the lines below and the OUPath variable above
    # Add-Computer -DomainName $DomainName -Credential $DomainJoinCredential -OUPath $OUPath -Restart -Force -ErrorAction Stop

    Write-Host "`nSuccessfully initiated domain join. The computer will now restart."

}
catch {
    Write-Error "Failed to join the domain: $($_.Exception.Message)"
    Write-Host "Please ensure:"
    Write-Host "- DNS is correctly configured on this client to point to your Domain Controller."
    Write-Host "- There is network connectivity to the Domain Controller."
    Write-Host "- The provided domain credentials have permission to join computers to the domain."
}

# or:
# Add-Computer -DomainName "zm.modul3.local" -Credential (Get-Credential) -Restart

Read-Host "Press enter to exit"
