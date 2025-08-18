import tkinter as tk
import subprocess
import json
import os
from .exceptions import ScriptError # Use explicit relative import


def center_window(window, width, height):
    """Centers a tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def run_ps1_cmd(cmd: str) -> str:
    """
    Runs a PowerShell command string.

    Args:
        cmd: The PowerShell command to run.

    Returns:
        The script's stdout as a string.

    Raises:
        ScriptError: If the command returns a non-zero exit code.
        FileNotFoundError: If 'powershell.exe' is not found.
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


def run_ps1_script(script_path: str, ps_args: list = None) -> list:
    """
    Runs a PowerShell script that is expected to return JSON output.

    Args:
        script_path: The absolute path to the .ps1 script.
        ps_args: A list of arguments to pass to the script.

    Returns:
        A list or dictionary decoded from the script's JSON output.

    Raises:
        ScriptError: If the script returns a non-zero exit code, fails to run,
                     or returns invalid JSON.
        FileNotFoundError: If 'powershell.exe' is not found.
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
            check=False,  # We will check the return code manually
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
            # If stderr has content, it's likely a non-terminating error message.
            if stderr:
                raise ScriptError(
                    f"PowerShell script '{os.path.basename(script_path)}' returned no JSON output but produced errors.",
                    stderr=stderr,
                )
            return [] # Script ran successfully but produced no output

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
        # Catch any other unexpected errors
        raise ScriptError(f"An unexpected error occurred while running '{os.path.basename(script_path)}'.") from e


def run_ps1_script_no_json(script_path: str, ps_args: list = None) -> str:
    """
    Runs a PowerShell script that does not necessarily return JSON.

    Args:
        script_path: The absolute path to the .ps1 script.
        ps_args: A list of arguments to pass to the script.

    Returns:
        The script's stdout as a string.

    Raises:
        ScriptError: If the script returns a non-zero exit code or fails to run.
        FileNotFoundError: If 'powershell.exe' is not found.
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
        # Using Popen to stream output could be an alternative for long-running scripts,
        # but for now, 'run' is simpler and captures all output at the end.
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False, # Manually check return code
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        stderr = process.stderr.strip()

        if process.returncode != 0:
            raise ScriptError(
                f"PowerShell script '{os.path.basename(script_path)}' failed with exit code {process.returncode}.",
                stderr=stderr
            )

        return process.stdout.strip()

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Error: 'powershell.exe' not found. Make sure PowerShell is installed and in your system's PATH."
        ) from e
    except Exception as e:
        raise ScriptError(f"An unexpected error occurred while running '{os.path.basename(script_path)}'.") from e
