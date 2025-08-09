# Changelog

All notable changes to this project will be documented in this file.

## [2025-08-09] - Admin Rights Indicator

### Summary of Changes

- **Feature: Admin Rights Indicator:** Added a visual indicator (a shield icon) to buttons that execute scripts requiring administrator privileges. This provides immediate feedback to the user about the permission level of each action.
- **New Component: `AdminButton`:** Created a new reusable `AdminButton` class in `components/AdminButton.py`. This custom button handles the logic for displaying the icon next to the text.
- **Refactor: `GeneralTab` updated:** The `GeneralTab` was refactored to use the new `AdminButton` for all its actions, as analysis showed all its scripts require elevation.
- **Fix: Missing `Pillow` Dependency:** Added `Pillow` to `requirements.txt`. This dependency was introduced to handle image manipulation for the icon and was missed in the initial commit, causing a `ModuleNotFoundError`.

## [2025-08-09] - Admin Rights Notification

### Summary of Changes

- **Added an admin rights notification:** A pop-up message is now displayed to the user on the first launch of the application, informing them that administrative privileges are required for most scripts. This message is only shown once and is managed through a `config.json` file.
- **Created a `Config` class:** A new `Config` class was introduced in `lib/Config.py` to handle loading and saving application settings.
- **Updated `App.py`:** The main application class now uses the `Config` class to check whether the admin rights message has been shown and displays it if necessary.

## [2025-08-09] - Refactoring

This release focuses on a significant refactoring of the Python codebase to improve its quality, readability, and maintainability. No new features have been added, and the existing functionality remains unchanged.

### Summary of Changes

The main goal of this refactoring was to address several code quality issues, including large and complex functions, duplicated code, and poor organization. The following is a summary of the key changes:

### 1. **Utility Function Abstraction**

- **Change:** The `construct_path` and `resource_path` utility functions, which were originally methods of the `App` class, have been moved to a new `lib/utils.py` module.
- **Reasoning:** These functions are general-purpose utilities and did not belong in the main `App` class. Moving them to a separate module improves separation of concerns and makes them easier to reuse.

### 2. **Style Code Reorganization**

- **Change:** The monolithic `init_style` function in `style.py` has been broken down into several smaller, private functions, each responsible for styling a specific type of widget (e.g., `_configure_button_styles`, `_configure_entry_styles`).
- **Reasoning:** The original `init_style` function was very long and difficult to navigate. This change makes the styling code more modular, readable, and easier to maintain.

### 3. **`CreateVMTab` Component Refactoring**

The `CreateVMTab.py` component, being one of the most complex parts of the application, received a major overhaul:

- **`__init__` Method Decomposition:** The large `__init__` method was broken down into smaller methods (`_initialize_state`, `_create_widgets`, `_pack_widgets`, `_bind_events`) for better organization.
- **Dictionary-based Mapping:** The `get_validate_set_string` method, which used a long and cumbersome `if/elif` chain to map Windows editions to version names, was refactored to use a dictionary lookup. This makes the code cleaner, more efficient, and easier to update.
- **Code Deduplication:** A generic helper function, `_populate_combobox_from_ps`, was created to eliminate the redundant code between the `get_windows_image_editions` and `load_switches` methods.
- **Parameter Consolidation:** The `create_vm` method was refactored to gather all VM parameters into a single dictionary, making the code cleaner and the process of passing arguments to the PowerShell script more robust.

### 4. **Code Cleanup**

- **Change:** Unnecessary `print` statements, which were likely used for debugging, were removed from the `_on_tab_change` method in `components/Notebook/Notebook.py`.
- **Reasoning:** Removing debug code makes the application cleaner and avoids unnecessary output to the console.
