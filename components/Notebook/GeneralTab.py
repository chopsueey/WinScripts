import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd, run_ps1_script


class GeneralTab(ttk.Frame):
    def __init__(self, master):
        super().__init__()

        self.open_standard_pwsh = ttk.Button(
            self,
            text="Open PowerShell",
            command=lambda: run_ps1_cmd("Start-Process powershell.exe -Verb RunAs"),
        )
        self.open_standard_pwsh.pack()
        self.open_new_pwsh = ttk.Button(
            self,
            text="Open PowerShell 7",
            command=lambda: run_ps1_cmd("Start-Process pwsh.exe -Verb RunAs"),
        )
        self.open_new_pwsh.pack()
        self.RDP_button = ttk.Button(
            self,
            text="Activate RDP",
            command=lambda: run_ps1_script(master.construct_path("activateRDP.ps1")),
        )
        self.RDP_button.pack()
