# UI Components

The application's user interface is built from several modular components, each encapsulated in its own Python module. These components are located in the `components/` directory.

## Main Application (`App.py`)

`App.py` is the main class for the application. It inherits from `customtkinter.CTk` and serves as the root window. Its responsibilities include:
- Initializing the main application window and its theme (light/dark mode).
- Assembling the main components: `Menubar`, `Statusbar`, and `Notebook`.
- Handling the application's lifecycle and theme toggling.

## Notebook (`components/Notebook/Notebook.py`)

The `Notebook` class creates the main tabbed interface of the application using `customtkinter.CTkTabview`. It is responsible for:
- Creating and managing the different tabs.
- Instantiating the content for each tab.

### Notebook Tabs

Each tab in the notebook is a `customtkinter.CTkFrame` subclass, allowing for a clean separation of concerns. The main tabs are:

- **`GeneralTab.py`**: Provides buttons for launching PowerShell consoles.
- **`AdvancedTab.py`**: Contains buttons for various system and machine configuration tasks (e.g., activating RDP, setting computer name).
- **`ADTab.py`**: Contains functionalities related to Active Directory management (e.g., joining a domain, installing AD).
- **`CreateVMTab.py`**: Offers a detailed form for creating a new Hyper-V virtual machine, with options for specifying the ISO, edition, resources, and network settings. This is one of the core features of the application.
- **`AzureTab.py`**: Provides buttons for common Azure administrative tasks.
- **`QuickShellTab.py`**: Provides a simple interface for running quick PowerShell commands and viewing their output.

## Other Components

- **`Menubar.py`**: Defines the application's top menu bar (currently unused by default in the `customtkinter` version).
- **`Statusbar.py`**: Creates a dynamic status bar at the bottom of the application window. It provides at-a-glance information about the system's health and configuration.
  - **Features:**
    - **Comprehensive Info:** Displays key data such as User, OS, RDP Status, Uptime, CPU/Memory/Disk Usage, and VM Detection.
    - **Grouped Information:** Data is organized into logical groups (`System`, `Hardware`, `Network`) for clarity.
    - **Compact Network Display:** Uses a `CTkComboBox` to list all network interfaces, preventing UI clutter.
  - **Implementation:** It contains a `SystemInfo` class for data gathering logic, which is separate from the UI.
- **`State.py`**: Manages the application's shared state (not fully implemented in the current version).
