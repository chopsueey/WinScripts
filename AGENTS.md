# Agent Instructions for Hyper-V GUI Automation Tool

This document provides guidance for AI agents working on this codebase. It outlines the project's architecture, key components, and development conventions.

## 1. Project Overview

This project is a desktop application with a graphical user interface (GUI) built using Python's `tkinter` library. Its main purpose is to provide a user-friendly frontend for a collection of PowerShell scripts that automate tasks related to Hyper-V virtual machine management.

- **Main Technologies:** Python, Tkinter, PowerShell
- **Core Functionality:** The application acts as a graphical wrapper for PowerShell scripts, allowing users to perform complex Hyper-V operations without using the command line.

## 2. Project Structure

The repository is organized into the following directories:

- **`main.py`, `App.py`**: The main entry point and root class for the application.
- **`components/`**: Contains the Python modules for the different UI components (e.g., tabs, menubar, statusbar).
- **`lib/`**: Includes shared library files, such as utility functions (`utils.py`), helper functions for running scripts (`functions.py`), and configuration management (`Config.py`).
- **`scripts/`**: Houses all the PowerShell scripts used for automation. The core logic for Hyper-V management resides here, especially in the `scripts/Hyper-V-Automation/` subdirectory.
- **`documentation/`**: Contains markdown files with detailed project documentation.
- **`icons/`**: Stores icon files used in the application.
- **`requirements.txt`**: Lists the Python dependencies for the project.
- **`changelog.md`**: A log of all notable changes to the project.

## 3. UI Components

The UI is built with `tkinter` and is modular. The main components are located in the `components/` directory:

- **`Notebook.py`**: Manages the main tabbed interface.
- **Tab Modules (`CreateVMTab.py`, `GeneralTab.py`, etc.)**: Each file defines a specific tab in the UI, encapsulating its layout and functionality. The `CreateVMTab.py` is a core component for VM creation.
- **`Menubar.py`, `Statusbar.py`**: Define the application's menu and status bars.

## 4. PowerShell Scripts

The application's backend is a suite of PowerShell scripts found in the `scripts/` directory.

- The Python application uses the `subprocess` module to execute these scripts. Helper functions in `lib/functions.py` manage the execution and data exchange.
- **`scripts/Hyper-V-Automation/create_Vm.ps1`**: The primary script for creating new VMs.
- **`scripts/getIsoEditions.ps1`**, **`scripts/getVMSwitches.ps1`**: Scripts used to populate dropdown menus in the UI.

## 5. Development Guidelines

When working on this codebase, please adhere to the following guidelines:

- **Administrator Privileges:** Most PowerShell scripts require administrator privileges to run correctly. Ensure that you run the application or any development environment (like your editor) as an administrator. The application is designed to show a one-time notification about this requirement.

- **Dependencies:** Install all necessary Python packages using the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

- **Changelog:** All new features, bug fixes, or significant refactors **must** be documented in `changelog.md`. Please follow the existing format: create a new entry with the date and a summary of changes, including a high-level description and a list of specific modifications.

- **Documentation:** If you introduce a new feature that significantly alters the application's functionality or architecture, you **must** update the documentation in the `documentation/` directory. For example, a new major UI component should be described in `documentation/components.md`.

- **Code Style:** Follow existing code patterns and aim for clarity and maintainability. Refactoring for quality is encouraged, as seen in the changelog entry for `[2025-08-09] - Refactoring`.
