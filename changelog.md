# Changelog

All notable changes to this project will be documented in this file.

## [2025-08-09] - Global UI Styling with Rounded Corners

### Summary of Changes

This update implements a global styling change to introduce rounded corners for all major UI elements, fulfilling the second part of the "theme-toggle-and-rounded-corners" feature. This provides a more modern and visually consistent user interface.

- **Feature: Rounded Corners:** All major interactive and container widgets (Buttons, Cards, Input Fields, etc.) now have rounded corners.
- **Refactor: Style Engine:** The `style.py` module was significantly refactored to support rounded corners. This was achieved by programmatically generating rounded border/background images using the `Pillow` library.
- **Technical Implementation:**
    - Created a new helper function, `create_rounded_bordered_image`, to generate `tkinter.PhotoImage` objects on the fly.
    - Used `tkinter.ttk.Style`'s `element_create` and `layout` methods to replace the default rectangular widget borders with the custom-generated rounded images.
    - This technique was applied to `TButton`, `TFrame` (for cards), `TEntry`, `TCombobox`, `TLabelframe`, and `TProgressbar`.
- **Fix:** Corrected an `AttributeError` caused by calling `ttk.PhotoImage` instead of the correct `tk.PhotoImage`.

## [2025-08-09] - Statusbar Visibility Fix

### Summary of Changes

- **Fix: Statusbar Layout:** Fixed a bug where items in the status bar would get cut off and become invisible when the window was resized. The layout logic has been corrected to ensure the status bar container expands vertically to fit all content as it wraps to new lines.
- **Refactor: Layout Management:** The `Statusbar` and its child `FlowFrame` now use `tkinter`'s `pack` options (`fill='both'`, `expand=True`) to manage their size, which is a more robust solution than manual height calculation. The `FlowFrame`'s repack logic was also simplified to prevent it from incorrectly hiding widgets.

## [2025-08-09] - New UI Style Guide (Material Design)

### Summary of Changes

This update introduces a comprehensive, Material Design-based UI style guide to ensure visual consistency and improve the application's overall look and feel.

- **Feature: Material Design Theme:** A new theme, `style_material.py`, has been created to give the application a modern, professional appearance based on Google's Material Design principles. The application now uses this theme by default.
- **Feature: UI Style Guide:** A new `UI_STYLE_GUIDE.md` has been added to the project root. This document outlines the color palette, typography, spacing, and other design rules for all developers to follow.
- **Feature: UI Helper Functions:** A new module, `lib/ui_helpers.py`, has been created. It provides a set of helper functions (e.g., `StyledButton`, `StyledLabel`) for easily creating widgets that conform to the new design system.
- **New Constants:** A `lib/material_constants.py` file was added to centralize the color and font definitions for the new theme.
- **Documentation:** Updated `AGENTS.md` to instruct agents on using the new style guide and created `documentation/technical_considerations.md` to document the decision.

## [2025-08-09] - Statusbar Refactor and Enhancement

### Summary of Changes

This update introduces a complete overhaul of the `Statusbar` component to provide more valuable information in a clean, responsive, and user-friendly manner.

- **Feature: Enhanced System Information:** The status bar now displays a wider range of valuable information for administrators, including **CPU Usage**, **Memory Usage**, **Disk Usage**, and whether the system is a **Virtual Machine**.
- **Feature: Responsive and Organized Layout:** The status bar has been redesigned to be fully responsive. Information is logically grouped into `System`, `Hardware`, and `Network` categories. The layout automatically wraps to new lines when the window is resized, and hides less critical information to prevent clutter in very narrow windows.
- **Feature: Compact Network Information:** To handle systems with many network interfaces, the NIC information is now presented in a clean, space-saving **dropdown menu (`Combobox`)**.
- **Refactor: Modular Architecture:** The `Statusbar` code was completely refactored. Data-gathering logic has been moved into a dedicated `SystemInfo` class, separating it from the UI. The UI now updates periodically without recreating widgets, resulting in a smoother user experience.

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
