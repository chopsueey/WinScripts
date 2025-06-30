$ErrorActionPreference = 'Stop' # Critical for catching errors

try {
    $vm_switch_names_list = @(Get-VMSwitch | Select-Object -ExpandProperty Name)
    $vm_switch_names_list | ConvertTo-Json -Depth 10 -Compress
}
catch {
    # Write the error to the PowerShell error stream (which subprocess.run captures in stderr)
    Write-Error $_.Exception.Message
    exit 1 # Indicate an error to Python by exiting with a non-zero code
}