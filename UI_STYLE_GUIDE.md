# UI Style Guide

This document outlines the design and style specifications for the WinScripts application. All new UI components should adhere to these guidelines to ensure a consistent and high-quality user experience.

## 1. Design Foundation
The UI is built with the **CustomTkinter** library, which provides modern, themed widgets. The core principles are clarity, consistency, and ease of use. The interface should be clean, with a clear hierarchy of information.

## 2. Theming
The application uses the built-in theming capabilities of CustomTkinter. It supports both **light** and **dark** modes.

- **Appearance Mode**: The appearance mode (theme) can be set to "light", "dark", or "system". This is controlled in `App.py`.
- **Color Themes**: CustomTkinter comes with default color themes like "blue", "dark-blue", and "green". The default theme is set in `App.py`.

## 3. Typography
The application uses the default font provided by CustomTkinter, which is platform-dependent (e.g., "Segoe UI" on Windows).

## 4. Spacing & Layout
- **Layout**: Use `grid()` for structured layouts like forms and tables. Use `pack()` for simple vertical or horizontal stacks.
- **Padding**: Use the `padx` and `pady` options to add space around widgets.

## 5. Widget Usage
To ensure consistency, use the widgets provided by the `customtkinter` library. Do not use standard `tkinter` or `ttk` widgets.

**Example Usage:**
```python
import customtkinter

# Create a CustomTkinter button
my_button = customtkinter.CTkButton(parent, text="Click Me", command=my_command)
my_button.pack()

# Create a CustomTkinter label
my_label = customtkinter.CTkLabel(parent, text="This is a label.")
my_label.pack()
```

### Available Widgets:
CustomTkinter provides a wide range of widgets, including:
- `CTkButton`
- `CTkLabel`
- `CTkEntry`
- `CTkFrame`
- `CTkTabview`
- `CTkComboBox`
- `CTkTextbox`
- and more...

Refer to the [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/) for a complete list of available widgets and their options.

## 6. How to Apply the Theme
The application theme is controlled by the following functions in `App.py`:
- `customtkinter.set_appearance_mode()`
- `customtkinter.set_default_color_theme()`

By following these guidelines, we can ensure that the WinScripts application remains visually consistent, professional, and easy for our users to navigate.
