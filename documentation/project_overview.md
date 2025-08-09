# Project Overview

This project is a desktop application with a graphical user interface (GUI) built using Python's `tkinter` library. The primary purpose of the application is to provide a user-friendly frontend for a collection of PowerShell scripts that automate tasks related to Hyper-V virtual machine management.

## Key Features

- **GUI Frontend:** The application offers an intuitive interface for interacting with complex PowerShell scripts, eliminating the need for users to run commands manually.
- **Hyper-V Automation:** The backend consists of a suite of PowerShell scripts designed to automate various Hyper-V tasks, such as creating virtual machines, configuring network settings, and managing system properties.
- **Modular Design:** The application is structured into modular components, including a main application window, a tabbed notebook interface, and distinct tabs for different functionalities (e.g., General, Create VM, Active Directory).

## Main Technologies

- **Python:** The core language for the GUI application.
- **Tkinter:** The standard Python interface to the Tcl/Tk GUI toolkit, used for creating the desktop application.
- **PowerShell:** The scripting language used for all the backend automation tasks related to Hyper-V.

## Project Structure

The project is organized into the following main directories:

- **`components/`**: Contains the Python modules for the different UI components of the application.
- **`lib/`**: Includes library files, such as shared functions and utilities.
- **`scripts/`**: Houses all the PowerShell scripts used for automation.
- **`icons/`**: Stores icon files for the application.
- **`documentation/`**: Contains markdown files with project documentation.
