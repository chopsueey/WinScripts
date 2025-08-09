# UI Style Guide

This document outlines the design and style specifications for the WinScripts application. All new UI components should adhere to these guidelines to ensure a consistent and high-quality user experience. This guide is based on the principles of Google's Material Design, adapted for a Python/Tkinter desktop application.

## 1. Design Foundation
The UI is based on **Material Design 3**. The core principles are clarity, consistency, and ease of use. The interface should be clean, with a clear hierarchy of information.

## 2. Color Palette
The application uses a specific color palette for light and dark modes. These colors are defined in `lib/material_constants.py` and should be used for all UI elements.

- **Primary**: `#6200EE` - Used for primary actions, buttons, and highlights.
- **Secondary**: `#03DAC6` - Used for secondary accents and highlights.
- **Surface**: `#FFFFFF` (Light Mode) / `#2d2e31` (Dark Mode) - The background color for widgets like frames and entry boxes.
- **Background**: `#e9ecef` (Light Mode) / `#202124` (Dark Mode) - The main window background color.
- **On Surface (text)**: `#000000` (Light Mode) / `#e8eaed` (Dark Mode) - The primary text color.
- **Error**: `#B00020` - Used for error messages and danger actions.

**Accessibility Note**: All text colors must maintain a minimum contrast ratio of 4.5:1 (WCAG AA) against their background.

## 3. Typography
The application uses the "Roboto" font family, which is the standard for Material Design. If "Roboto" is not available, "Segoe UI" or "Helvetica" can be used as fallbacks. Font definitions are stored in `lib/material_constants.py`.

- **Title**: Roboto 20px Bold
- **Heading**: Roboto 16px Semi-Bold
- **Body**: Roboto 12px Regular
- **Button**: Roboto 12px Regular

## 4. Spacing & Layout
- **Base Unit**: Use an 8px grid system for all padding and margins.
- **Padding**:
  - Window padding: 10px.
  - Frame padding: 15px.
  - Widget padding: 5px inner padding for elements like entries and buttons.
- **Layout**: Use `grid()` for structured layouts like forms and tables. Use `pack()` for simple vertical or horizontal stacks.
- **Spacing**: Leave at least 16px of space between unrelated UI components.

## 5. Widget Style Helpers
To ensure consistency, use the helper functions provided in `lib/ui_helpers.py` to create styled widgets. These functions automatically apply the correct styles from the theme.

**Example Usage:**
```python
from lib.ui_helpers import StyledButton, StyledLabel

# Create a styled button
my_button = StyledButton(parent, text="Click Me", command=my_command)
my_button.pack()

# Create a styled label
my_label = StyledLabel(parent, text="This is a styled label.")
my_label.pack()
```

### Available Helpers:
- `StyledButton(master, text, command)`: Creates a primary action button.
- `StyledLabel(master, text)`: Creates a standard body text label.
- `StyledHeading(master, text)`: Creates a heading label.
- ... (more helpers to be added)

## 6. How to Apply the Theme
The application theme is controlled by the `init_style()` function called in `App.py`. To change themes, modify the import statement to point to the desired style file (e.g., `from style_material import init_style`).

By following these guidelines, we can ensure that the WinScripts application remains visually consistent, professional, and easy for our users to navigate.
