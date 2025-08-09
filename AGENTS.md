# Agent Instructions for WinScripts (Hyper-V GUI Automation Tool)

This document provides guidance for AI agents working on this codebase. It outlines the project's architecture, key components, development workflow, and conventions. Following these guidelines will ensure smooth collaboration and efficient development.

## 1. Quick Start for New Sessions

Before starting any work, read these files in order to get a comprehensive understanding of the project:

1.  **`AGENTS.md`** (this file): To understand the workflow and conventions.
2.  **`documentation/project_overview.md`**: For a high-level overview of the project's purpose and architecture.
3.  **`changelog.md`**: To understand the latest changes and the project's history.
4.  **`documentation/components.md`** and **`documentation/scripts.md`**: To dive deeper into the UI and backend script implementation.

## 2. Development Workflow

Follow this story-driven workflow for all tasks.

### A. Story Selection & Planning
1.  Receive a task (a story) from the user.
2.  Review the task's requirements and acceptance criteria.
3.  Explore the codebase to understand the implementation details.
4.  Create a brief implementation plan and confirm it with the user before proceeding.

### B. Implementation
1.  Implement the story according to the plan.
2.  Write clean, well-structured code that follows existing patterns.
3.  Ensure proper error handling is in place for new functionality.

### C. Testing & Verification
1.  Manually test the changes to ensure they work as expected.
2.  Run the application and verify that there are no new console errors or warnings.
3.  Remember that most scripts require **administrator privileges**. Run your development environment accordingly.

### D. Human Verification Request
When you have completed and tested your changes, request verification from the human user in the following format:

---

**Implementation Complete!**

**Changes made:**
*   [Bulleted list of key changes]

**Please verify in the app:**
*   [Specific, step-by-step instructions for the user to test the functionality]
*   [Describe the expected behavior or output]

**Ready for your verification!**

---

### E. Story Completion
Once the user confirms that the changes are working correctly:
1.  Update **`changelog.md`** with a summary of the changes. This is a mandatory step.
2.  If the change was significant, consider whether any documents in `documentation/` need to be updated.

## 3. Knowledge Capture

To ensure we retain important information and decisions, we use a `technical_considerations.md` file.

*   **Location:** `documentation/technical_considerations.md`
*   **Purpose:** This file is for documenting key technical decisions, lessons learned, solutions to tricky bugs, and rationale for architectural choices.
*   **Your Task:** If you encounter a complex issue, make a significant technical decision, or discover a "gotcha," please add an entry to this file. If the file doesn't exist, you should create it.

## 4. Project Overview

This project is a desktop application with a graphical user interface (GUI) built using Python's `tkinter` library. Its main purpose is to provide a user-friendly frontend for a collection of PowerShell scripts that automate tasks related to Hyper-V virtual machine management.

- **Main Technologies:** Python, Tkinter, PowerShell
- **Core Functionality:** The application acts as a graphical wrapper for PowerShell scripts.

For a more detailed overview, please read **[`documentation/project_overview.md`](./documentation/project_overview.md)**.

## 5. Architecture & Components

The application is composed of two main parts: the Python/Tkinter frontend and the PowerShell backend.

### UI Components (Frontend)
The UI is built with `tkinter` and is organized into modular components. The main window (`App.py`) assembles the `Menubar`, `Statusbar`, and a tabbed `Notebook`. Each tab is a separate module.

For a detailed breakdown of each component, please read **[`documentation/components.md`](./documentation/components.md)**.

### PowerShell Scripts (Backend)
The application's backend is a suite of PowerShell scripts found in the `scripts/` directory. The Python application uses the `subprocess` module to execute these scripts.

For details on the key scripts and how they are used, please read **[`documentation/scripts.md`](./documentation/scripts.md)**.

## 6. Development Guidelines

- **Administrator Privileges:** Most PowerShell scripts require administrator privileges. Ensure you run the application or your development environment with elevated permissions.
- **Dependencies:** Install all Python packages using `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```
- **Changelog:** All new features, bug fixes, or significant refactors **must** be documented in `changelog.md`.
- **Code Style:** Follow existing code patterns and aim for clarity and maintainability.
- **UI Development and Styling:** All UI development must adhere to the official style guide.
  - **Read the Guide:** Before creating or modifying any UI, you **must** read the **[`UI_STYLE_GUIDE.md`](./UI_STYLE_GUIDE.md)** to understand the design system.
  - **Use UI Helpers:** To ensure consistency, you **must** use the helper functions provided in **`lib/ui_helpers.py`** for creating styled widgets. Do not style widgets manually.
  - **Example:**
    ```python
    # Correct way to create a button:
    from lib.ui_helpers import StyledButton
    button = StyledButton(parent, text="Submit", command=submit_form)

    # Incorrect way (manual styling):
    # button = ttk.Button(parent, text="Submit", ...)
    # button.configure(...)
    ```
