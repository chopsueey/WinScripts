import tkinter as tk
import subprocess, os, time


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


def run_ps1_script(script_path: str, window=False, ps_args: list = None) -> None:
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
    # was .Popen
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", command_to_execute],
        shell=True,
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
