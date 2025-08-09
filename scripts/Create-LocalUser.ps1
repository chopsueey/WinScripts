Write-Host "This script will create a new local user."

$Username = Read-Host "Enter the username for the new user"
$Password = Read-Host -AsSecureString "Enter the password for the new user"
$FullName = Read-Host "Enter the full name of the new user"
$Description = Read-Host "Enter a description for the new user"

try {
    New-LocalUser -Name $Username -Password $Password -FullName $FullName -Description $Description -ErrorAction Stop
    Write-Host "User '$Username' created successfully."
}
catch {
    Write-Error "Failed to create user '$Username'. Error: $($_.Exception.Message)"
}

Read-Host "Press enter to exit"
