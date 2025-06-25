$NewComputerName = Read-Host "Choose new name"
Rename-Computer -NewName $NewComputerName -Force

Add-Type -AssemblyName System.Windows.Forms

# Define the message box parameters
$Message = "Are you sure you want to restart this computer?"
$Title = "Confirm Computer Restart"
$Buttons = [System.Windows.Forms.MessageBoxButtons]::YesNo
$Icon = [System.Windows.Forms.MessageBoxIcon]::Question

# Display the message box and capture the result
# The Show method returns a DialogResult enumeration value (e.g., Yes, No, Cancel)
$Result = [System.Windows.Forms.MessageBox]::Show($Message, $Title, $Buttons, $Icon)

# Check the user's response
if ($Result -eq [System.Windows.Forms.DialogResult]::Yes) {
    Restart-Computer -Force
} else {
    Write-Host "User cancelled restart. Computer will not be restarted."
}
