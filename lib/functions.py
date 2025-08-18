import tkinter as tk
import subprocess
import json
import os
from .exceptions import ScriptError # Use explicit relative import


def increment(var: tk.IntVar):
    var.set(var.get() + 1)


def decrement(var: tk.IntVar):
    var.set(var.get() - 1)


def center_window(window, width, height):
    """Centers a tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def run_command_async(command: str) -> None:
    """
    Runs a command asynchronously in a new process without a visible window.
    This is for simple, non-interactive, fire-and-forget commands.
    """
    subprocess.Popen(
        ["powershell.exe", "-Command", command],
        creationflags=subprocess.CREATE_NO_WINDOW
    )


def run_ps1_cmd(cmd: str) -> str:
    """
    Runs a PowerShell command string and captures its output.
    This is a BLOCKING call and is intended for quick commands
    like in the QuickShell tab.
    """
    if not cmd:
        return ""
    try:
        process = subprocess.run(
            ["powershell", "-Command", cmd],
            capture_output=True,
            text=True,
            check=False,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        stderr = process.stderr.strip()
        if process.returncode != 0:
            raise ScriptError(
                f"PowerShell command failed with exit code {process.returncode}.",
                stderr=stderr
            )
        return process.stdout.strip()
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Error: 'powershell.exe' not found. Make sure PowerShell is installed and in your system's PATH."
        ) from e
    except Exception as e:
        raise ScriptError(f"An unexpected error occurred while running command.") from e


def run_ps1_script_async(script_path: str, ps_args: list = None, elevated: bool = False) -> None:
    """
    Runs a PowerShell script in a new, visible window and does NOT block the GUI.
    This is "fire-and-forget" and uses the 'Start-Process' cmdlet to ensure
    a new window is created, which is necessary for interactive scripts.
    """
    if ps_args is None:
        ps_args = []

    # Build the argument list for the script file itself
    script_argument_list = [
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        f'"{script_path}"',  # Quote the script path to handle spaces
    ]

    # Add additional script arguments
    for arg in ps_args:
        # Simple quoting for arguments with spaces
        script_argument_list.append(f'"{arg}"' if " " in arg else arg)

    argument_string = " ".join(script_argument_list)

    # Determine if elevation is needed
    verb = "-Verb RunAs" if elevated else ""

    # Construct the final command to be executed by the initial PowerShell process
    # This command's job is to launch the second, visible PowerShell process
    command_to_execute = f"Start-Process powershell.exe -ArgumentList '{argument_string}' {verb}"

    # Use Popen with CREATE_NO_WINDOW to run the launcher command silently.
    # The launched process itself will be visible.
    subprocess.Popen(
        ["powershell.exe", "-Command", command_to_execute],
        creationflags=subprocess.CREATE_NO_WINDOW
    )


def run_ps1_script(script_path: str, ps_args: list = None) -> list:
    """
    Runs a PowerShell script, captures its JSON output, and blocks until complete.
    Intended for fast scripts that return data to the GUI, like populating comboboxes.
    """
    if ps_args is None:
        ps_args = []

    command = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ] + ps_args

    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        stdout = process.stdout.strip()
        stderr = process.stderr.strip()

        if process.returncode != 0:
            raise ScriptError(
                f"PowerShell script '{os.path.basename(script_path)}' failed with exit code {process.returncode}.",
                stderr=stderr
            )

        if not stdout:
            if stderr:
                raise ScriptError(
                    f"PowerShell script '{os.path.basename(script_path)}' returned no JSON output but produced errors.",
                    stderr=stderr,
                )
            return []

        return json.loads(stdout)

    except json.JSONDecodeError as e:
        raise ScriptError(
            f"Failed to decode JSON from '{os.path.basename(script_path)}'.",
            stderr=f"JSONDecodeError: {e}\nRaw Output: {stdout}",
        ) from e
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Error: 'powershell.exe' not found. Make sure PowerShell is installed and in your system's PATH."
        ) from e
    except Exception as e:
        raise ScriptError(f"An unexpected error occurred while running '{os.path.basename(script_path)}'.") from e
