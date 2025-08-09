# UI Components

The application's user interface is built from several modular components, each encapsulated in its own Python module. These components are located in the `components/` directory.

## Main Application (`App.py`)

`App.py` is the main class for the application. It inherits from `tkinter.Tk` and serves as the root window. Its responsibilities include:
- Initializing the main application window.
- Setting up the main components: `Menubar`, `Statusbar`, and `Notebook`.
- Handling the application's lifecycle.

## Notebook (`components/Notebook/Notebook.py`)

The `Notebook` class creates the main tabbed interface of the application using `ttk.Notebook`. It is responsible for:
- Creating and managing the different tabs.
- Adding each tab to the notebook interface.

### Notebook Tabs

Each tab in the notebook is a separate class, allowing for a clean separation of concerns. The main tabs are:

- **`GeneralTab.py`**: Provides buttons for general system administration tasks, such as activating RDP, setting an IP address, or joining a domain.
- **`AdvancedTab.py`**: Intended for more advanced configuration options.
- **`ADTab.py`**: Contains functionalities related to Active Directory management.
- **`CreateVMTab.py`**: Offers a detailed form for creating a new Hyper-V virtual machine, with options for specifying the ISO, edition, resources, and network settings. This is one of the core features of the application.
- **`QuickShellTab.py`**: Provides a simple interface for running quick PowerShell commands.

## Other Components

- **`Menubar.py`**: Defines the application's top menu bar.
- **`Statusbar.py`**: Creates the status bar at the bottom of the application window.
- **`State.py`**: Manages the application's shared state (not fully implemented in the current version).
