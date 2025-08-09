# This script connects to Azure.
# It will open a browser window to authenticate.

Write-Host "Connecting to Azure..."

try {
    # Check if the Az module is installed
    if (Get-Module -ListAvailable -Name Az) {
        Write-Host "Az module is already installed."
    } else {
        Write-Host "Az module not found. Installing..."
        Install-Module -Name Az -AllowClobber -Scope CurrentUser -Force
    }

    Connect-AzAccount -ErrorAction Stop
    Write-Host "Successfully connected to Azure."
}
catch {
    Write-Error "Failed to connect to Azure. Error: $($_.Exception.Message)"
}

Read-Host "Press enter to exit"
