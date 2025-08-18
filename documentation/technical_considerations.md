# Technical Considerations

This document records key technical decisions, architectural choices, and important lessons learned during the development of the WinScripts application.

---

## 2025-08-18: Non-Blocking, Visible Script Execution is a Key Feature

### Context
The application's primary function is to act as a GUI wrapper for long-running PowerShell scripts. A key aspect of the user experience is that the application should remain responsive (non-blocking) while these scripts execute. Furthermore, some scripts may require interactive user input directly in the PowerShell console (e.g., for credential prompts or confirmations).

### Decision
All long-running or potentially interactive scripts **must** be executed asynchronously. The `lib/functions.py` module provides a dedicated function for this purpose: `run_ps1_script_async`.

This function uses `subprocess.Popen` without any flags that would hide the window or redirect I/O. This achieves two critical goals:
1.  **Non-Blocking GUI:** `Popen` is non-blocking, so the Python application's main thread does not freeze. The user can continue to interact with the GUI while the script runs.
2.  **Visible & Interactive Console:** A new PowerShell console window appears, allowing the user to see the script's live output and, crucially, to provide any input the script might require.

### Rationale
This architectural pattern is a core feature. Any attempt to change this to a blocking call (like `subprocess.run`) or to hide the console window (e.g., to capture output for in-app display) will be considered a **major regression**. It would break interactivity and make the application unusable during long operations.

For short, synchronous scripts that need to return data to the application (like populating a dropdown), the blocking functions `run_ps1_script` (for JSON) and `run_ps1_cmd` (for string output) should be used. These are exceptions to the rule and should only be used for quick, non-interactive tasks.

---

## 2025-08-09: Adoption of a Formal UI Style Guide

### Context
The application's UI was developed without a formal, centralized design system. This led to inconsistencies in styling and made it difficult for developers (especially AI agents) to create new UI components that matched the existing design. There was no single source of truth for colors, fonts, spacing, or widget styles.

### Decision
A formal UI style guide based on Google's Material Design was implemented to address this issue. The implementation consists of the following new assets:

1.  **`UI_STYLE_GUIDE.md`**: A markdown document in the root directory that serves as the official specification for the design system.
2.  **`lib/material_constants.py`**: A Python file containing all the color and font constants for the theme.
3.  **`style_material.py`**: A new theme file that uses the constants to apply Material Design styles to all `ttk` widgets.
4.  **`lib/ui_helpers.py`**: A set of helper functions (e.g., `StyledButton`, `StyledLabel`) that abstract the creation of styled widgets, making it easy to apply the design system consistently.

The application was updated to use this new theme by default in `App.py`.

### Rationale
Adopting a formal design system provides several key benefits:
-   **Consistency:** Ensures that all UI elements across the application have a consistent look and feel.
-   **Clarity:** Provides a clear set of rules for both human and AI developers to follow, reducing ambiguity.
-   **Efficiency:** The use of `ui_helpers.py` speeds up development by providing ready-to-use, pre-styled components.
-   **Maintainability:** Centralizing style definitions in `style_material.py` and `lib/material_constants.py` makes the theme easier to manage and update in the future.
-   **Professionalism:** A consistent, well-designed UI provides a more professional and intuitive user experience.
