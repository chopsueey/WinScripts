# PowerShell Scripts

The core functionality of this application is provided by a collection of PowerShell scripts located in the `scripts/` directory. The Python GUI acts as a frontend to these scripts, gathering user input and passing it as arguments to the appropriate script.

## Main Automation Scripts

The most important scripts are located in the `scripts/Hyper-V-Automation/` subdirectory. These scripts are responsible for the heavy lifting of Hyper-V management.

- **`create_Vm.ps1`**: This is the main script for creating a new virtual machine. It accepts a wide range of parameters, including the VM name, password, ISO file, edition, resources (RAM, CPU, VHDX size), and network settings. The "Create VM" tab in the GUI is specifically designed to work with this script.

- **`getIsoEditions.ps1`**: This script inspects a Windows ISO file and returns a list of the available Windows editions that can be installed. This is used to populate the "Edition" dropdown in the "Create VM" tab.

- **`getVMSwitches.ps1`**: This script retrieves a list of the available Hyper-V virtual switches on the host machine. This is used to populate the "Virtual switch" dropdown.

## Utility Scripts

The `scripts/` directory also contains several smaller utility scripts for performing specific tasks, such as:

- `activateRDP.ps1`: Toggles Remote Desktop Protocol (RDP) on or off.
- `activateAdmin.ps1`
- `setIP.ps1`
- `joinDomain.ps1`
- `enableRemoting.ps1`
- `Get-DiskSpace.ps1`: Displays disk space information for all logical drives.
- `Get-RunningServices.ps1`: Lists all currently running services.
- `Create-LocalUser.ps1`: Creates a new local user with a password, full name, and description.

These scripts are typically called from the "General" tab in the application.

## Azure Automation Scripts

A new set of scripts for Azure automation has been added to the `scripts/Azure-Automation/` subdirectory.

- `Connect-Azure.ps1`: Connects to an Azure account.
- `Get-AzureResourceGroup.ps1`: Lists all resource groups in the current Azure subscription.
- `Get-AzureStorageAccount.ps1`: Lists all storage accounts in the current Azure subscription.
- `New-AzureVM.ps1`: Creates a new Azure Virtual Machine.

## How They Are Called

The Python application uses the `subprocess` module to execute these PowerShell scripts. The `lib/functions.py` file contains helper functions (`run_ps1_script`, `run_ps1_script_2`, etc.) that abstract the process of running the scripts and capturing their output.
