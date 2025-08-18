# WinScripts: Hyper-V & System Administration GUI

WinScripts is a user-friendly desktop application for Windows that provides a graphical interface for common, and often complex, IT administration tasks. It simplifies the management of Hyper-V virtual machines, Azure resources, and local system configurations by wrapping powerful PowerShell scripts in an intuitive GUI.

The Hyper-V-Automation scripts are from: https://github.com/fdcastel/Hyper-V-Automation

https://github.com/user-attachments/assets/916d5d7a-05a6-4485-87c6-db1028254cd3


## Key Features

- **Intuitive GUI:** A clean, tabbed interface built with Python and Tkinter, designed to make complex tasks accessible.
- **Hyper-V Automation:** Create, configure, and manage Hyper-V virtual machines without touching the command line. The app helps with everything from creating a new VM from an ISO to configuring its network settings.
- **Azure Integration:** Perform basic Azure management tasks, such as connecting to your account, listing resources, and spinning up new VMs.
- **System Administration Utilities:** A collection of scripts to streamline common tasks like activating RDP, managing local users, changing computer names, and more.
- **Real-time System Info:** A dynamic status bar displays key system metrics like CPU, memory, and disk usage at a glance.
- **Admin-Aware Components:** Actions that require elevated privileges are clearly marked with a shield icon, providing clarity on when administrator rights are needed.

## Technologies Used

- **Frontend:** Python 3, Tkinter
- **Backend:** PowerShell
- **Core Libraries:** `customtkinter`, `Pillow`

## Getting Started


### Prerequisites

- Windows Operating System
- Hyper-V enabled for virtual machine management features.
- PowerShell 5.1 or later.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/chopsueey/WinScripts.git
    cd WinScripts
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python main.py
    ```

## Important Notes

- **Run as Administrator:** For most of its functionality, especially tasks related to Hyper-V and system configuration, the application must be run with administrator privileges.

## Build Instructions

You can create a standalone executable using PyInstaller. The recommended way to build the application is by using the provided spec file, which contains all the necessary configurations.

### Building the Executable

1.  **Ensure PyInstaller is installed:**
    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command from the project root:**
    ```bash
    pyinstaller build.spec
    ```

This command will create a `dist/` directory containing the single-file executable (`WinScripts.exe`). The `build.spec` file is pre-configured to handle all data files, including icons and theme assets, ensuring the application works correctly when compiled.
