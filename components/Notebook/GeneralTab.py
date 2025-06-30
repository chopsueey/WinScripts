import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd, run_ps1_script, run_ps1_script_elevated


class GeneralTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

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
            command=lambda: run_ps1_script_elevated(app.construct_path("activateRDP.ps1")),
        )
        self.RDP_button.pack()

        self.activateAdmin = ttk.Button(
            self,
            text="Activate Admin",
            command=lambda: run_ps1_script_elevated(app.construct_path("activateAdmin.ps1"), window=True),
        )
        self.activateAdmin.pack()

        self.activateAdmin = ttk.Button(
            self,
            text="Set IP",
            command=lambda: run_ps1_script_elevated(app.construct_path("setIP.ps1"), window=True),
        )
        self.activateAdmin.pack()

        self.activateAdmin = ttk.Button(
            self,
            text="Install BGInfo",
            command=lambda: run_ps1_script_elevated(app.construct_path("installBGInfo.ps1"), window=True),
        )
        self.activateAdmin.pack()

        self.activateAdmin = ttk.Button(
            self,
            text="Set ComputerName",
            command=lambda: run_ps1_script_elevated(app.construct_path("setComputerName.ps1"), window=True),
        )
        self.activateAdmin.pack()