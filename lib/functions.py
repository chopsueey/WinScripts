import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import subprocess, os


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
        ["powershell", "-Command", cmd], capture_output=True, text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def run_ps1_script(script_path: str) -> None:
    command_to_execute = (
        f"Start-Process powershell.exe "
        f"-ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', '{script_path}' "
        f"-Verb RunAs -WindowStyle Hidden"
    )

    subprocess.Popen(
        ["powershell.exe", "-NoProfile", "-Command", command_to_execute], shell=True
    )
