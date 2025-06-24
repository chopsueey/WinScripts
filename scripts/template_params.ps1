param (
    [string]$TargetComputer,
    [int]$Port = 3389, # Default value if not provided
    [switch]$Force # A boolean switch parameter
)

Write-Host "Script started!"
Write-Host "Target Computer: $TargetComputer"
Write-Host "Port: $Port"

if ($Force) {
    Write-Host "Force switch is enabled."
} else {
    Write-Host "Force switch is NOT enabled."
}