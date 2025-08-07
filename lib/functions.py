import tkinter as tk
from tkinter import messagebox
import subprocess, json


def increment(var: tk.IntVar):
    var.set(var.get() + 1)


def decrement(var: tk.IntVar):
    var.set(var.get() - 1)


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def run_ps1_cmd(cmd: str) -> str:
    result = subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True,
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def run_ps1_script_elevated(
    script_path: str, window=False, ps_args: list = None
) -> None:
    if ps_args is None:
        ps_args = []

    script_argument_list = [
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ]

    script_argument_list.extend(ps_args)

    # Build a single string: each argument quoted and joined with spaces (NOT commas)
    argument_list_string = " ".join(
        [
            f'"{arg}"' if " " in arg or "(" in arg or ")" in arg else arg
            for arg in script_argument_list
        ]
    )

    command_to_execute = (
        f"Start-Process powershell.exe "
        f"-ArgumentList '{argument_list_string}' "
        f"-Wait "  # remove for non-blocking
        f"-Verb RunAs "
        f"{'-WindowStyle Hidden' if not window else ''}"
    )

    # changed to .run to block python execution, as it takes a while to create the json file
    # in CreateVMTab.py (see self.get_windows_image_editions). Was subprocess.Popen before.
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", command_to_execute],
        shell=True,
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )


def run_ps1_script_2(script_path: str, ps_args: list = None) -> tuple[bool, str, str]:
    if ps_args is None:
        ps_args = []

    cmd = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ] + ps_args

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,  # Don't raise exception on non-zero exit code, we will check it manually
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        if result.returncode == 0:
            return True, result.stdout, result.stderr
        else:
            return False, result.stdout, result.stderr

    except FileNotFoundError:
        return (
            False,
            "",
            f"Error: 'powershell.exe' or script '{script_path}' not found. Make sure PowerShell is in your PATH.",
        )
    except Exception as e:
        return False, "", f"An unexpected error occurred: {e}"


def run_ps1_script(
    script_path: str,
    ps_args: list = None,
    window: bool = True,
) -> list:
    if ps_args is None:
        ps_args = []

    powershell_command_args = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ]
    powershell_command_args.extend(ps_args)

    creationflags = subprocess.CREATE_NO_WINDOW if not window else 0

    try:
        result = subprocess.Popen(
            powershell_command_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=creationflags,
        )

        stdout, stderr = result.communicate()
        json_output = stdout.decode().strip()

        if not json_output:
            if stderr:
                error_message = (
                    f"PowerShell script '{script_path}' returned no output to stdout, but wrote to stderr:\n\n"
                    f"{stderr.decode().strip()}"
                )
                messagebox.showwarning("PowerShell Warning", error_message)
            return []

        return json.loads(json_output)

    except subprocess.CalledProcessError as e:
        error_message = (
            f"Error executing PowerShell script '{script_path}':\n\n"
            f"Return code: {e.returncode}\n"
            f"STDOUT: {e.stdout.strip()}\n"
            f"STDERR: {e.stderr.strip()}"
        )
        messagebox.showerror("PowerShell Execution Error", error_message)
        return None
    except json.JSONDecodeError as e:
        error_message = (
            f"Error decoding JSON from PowerShell output for script '{script_path}':\n\n"
            f"{e}\n\n"
            f"Raw PowerShell output (STDOUT): '{json_output}'"
        )
        if stderr:
            error_message += f"\nPowerShell STDERR: {stderr.decode().strip()}"
        messagebox.showerror("JSON Decode Error", error_message)
        return None
    except FileNotFoundError:
        error_message = f"Error: 'powershell.exe' or script '{script_path}' not found. Make sure PowerShell is in your PATH."
        messagebox.showerror("File Not Found Error", error_message)
        return None
