import tkinter as tk
import subprocess


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
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def run_ps1_script(script_path: str, ps_args: list = None) -> None:
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

    formatted_args_for_powershell = []
    for arg in script_argument_list:
        # If the argument contains spaces, or is a quoted string itself, we need to handle it.
        # For simplicity, we'll just wrap each argument in single quotes.
        # This handles spaces but assumes arguments don't contain literal single quotes themselves.
        formatted_args_for_powershell.append(f"'{arg}'")

    argument_list_string = ", ".join(formatted_args_for_powershell)

    command_to_execute = (
        f"Start-Process powershell.exe "
        f"-ArgumentList {argument_list_string} "
        f"-Verb RunAs -WindowStyle Hidden"
    )

    subprocess.Popen(
        ["powershell.exe", "-NoProfile", "-Command", command_to_execute],
        shell=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
