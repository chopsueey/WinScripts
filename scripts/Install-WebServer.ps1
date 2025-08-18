#Requires -RunAsAdministrator
<#
.SYNOPSIS
Installs the Internet Information Services (IIS) web server role.

.DESCRIPTION
This script installs the IIS Web Server role and its common management tools.
It can also create a default test page and open it in a browser.

.PARAMETER InstallDefaultPage
A switch that, if present, creates a basic 'index.html' file in the default web root directory.

.PARAMETER OpenInBrowser
A switch that, if present, opens the local website in the default browser after installation.

.EXAMPLE
.\Install-WebServer.ps1 -InstallDefaultPage -OpenInBrowser
#>
[CmdletBinding(SupportsShouldProcess=$true)]
param(
    [switch]$InstallDefaultPage,
    [switch]$OpenInBrowser
)

# Import the administration module
try {
    Import-Module (Join-Path $PSScriptRoot "modules\WinAdmin.psm1") -ErrorAction Stop
}
catch {
    Write-Host "FATAL: Could not import WinAdmin module. Ensure 'WinAdmin.psm1' exists in the 'modules' subdirectory. ERROR: $($_.Exception.Message)"
    exit 1
}

# --- Prerequisite Checks ---
Write-Log "Performing prerequisite checks..."

if (-not (Test-AdminPrivileges)) {
    Write-ErrorLog "This script must be run with Administrator privileges."
    exit 1
}
Write-Log "Administrator check passed."

# --- Main Logic ---
try {
    if ($PSCmdlet.ShouldProcess("Windows Features", "Install IIS Web Server role")) {
        Write-Log "Installing IIS Web Server role..."
        Install-WindowsFeature -Name Web-Server -IncludeManagementTools -ErrorAction Stop
        Write-Log "IIS Web Server role installed successfully."

        if ($InstallDefaultPage.IsPresent) {
            if ($PSCmdlet.ShouldProcess("file 'C:\inetpub\wwwroot\index.html'", "Create default test page")) {
                Write-Log "Creating default test page..."
                $htmlContent = @"
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to IIS</title>
    <style>body { font-family: sans-serif; text-align: center; padding-top: 50px; }</style>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Your IIS Web Server has been installed successfully by a PowerShell script.</p>
</body>
</html>
"@
                Set-Content -Path "C:\inetpub\wwwroot\index.html" -Value $htmlContent -Force -ErrorAction Stop
                Write-Log "Default test page created at 'C:\inetpub\wwwroot\index.html'."
            }
        }

        if ($OpenInBrowser.IsPresent) {
            Write-Log "Opening test page in default browser..."
            Start-Process "http://localhost"
        }
    }
}
catch {
    Write-ErrorLog "Failed to install IIS Web Server. ERROR: $($_.Exception.Message)"
    exit 1
}
