Enable-LocalUser -Name "Administrator"

# Then, set the password securely
$AdminPassword = Read-Host -AsSecureString "Enter Administrator password"
Set-LocalUser -Name "Administrator" -Password $AdminPassword

Read-Host "Press enter to exit"
