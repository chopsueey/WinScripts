$Username = "newuser"
$PasswordPlain = "P@ssw0rd"
$FullName = "New User"
$Description = "Created via PowerShell"

$SecurePassword = ConvertTo-SecureString $PasswordPlain -AsPlainText -Force

New-LocalUser -Name $Username `
              -Password $SecurePassword `
              -FullName $FullName `
              -Description $Description `
              -PasswordNeverExpires:$true `
              -UserMayNotChangePassword:$false

# === Optional: Add User to Local Group (e.g., Administrators) ===
# Add-LocalGroupMember -Group "Administrators" -Member $Username

write-Host "User '$Username' created successfully."

Read-Host "Press enter to exit"
