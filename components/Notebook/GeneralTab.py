import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd, run_ps1_script_2, run_ps1_script_elevated


class GeneralTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

        self.open_standard_pwsh = ttk.Button(
            self,
            text="Open PowerShell",
            command=lambda: run_ps1_cmd("Start-Process powershell.exe -Verb RunAs"),
        )
        self.open_standard_pwsh.pack(pady=4)

        self.open_new_pwsh = ttk.Button(
            self,
            text="Open PowerShell 7",
            command=lambda: run_ps1_cmd("Start-Process pwsh.exe -Verb RunAs"),
        )
        self.open_new_pwsh.pack(pady=4)

        self.RDP_button = ttk.Button(
            self,
            text="Activate RDP",
            command=lambda: run_ps1_script_2(app.construct_path("activateRDP.ps1")),
        )
        self.RDP_button.pack(pady=4)

        self.activateAdmin = ttk.Button(
            self,
            text="Activate Admin",
            command=lambda: run_ps1_script_2(app.construct_path("activateAdmin.ps1")),
        )
        self.activateAdmin.pack(pady=4)

        self.activateAdmin = ttk.Button(
            self,
            text="Set IP",
            command=lambda: run_ps1_script_2(app.construct_path("setIP.ps1")),
        )
        self.activateAdmin.pack(pady=4)

        self.activateAdmin = ttk.Button(
            self,
            text="Install BGInfo",
            command=lambda: run_ps1_script_2(app.construct_path("installBGInfo.ps1")),
        )
        self.activateAdmin.pack(pady=4)

        self.activateAdmin = ttk.Button(
            self,
            text="Set ComputerName",
            command=lambda: run_ps1_script_2(app.construct_path("setComputerName.ps1")),
        )
        self.activateAdmin.pack(pady=4)

        self.setup_AD = ttk.Button(
            self,
            text="Install AD",
            command=lambda: run_ps1_script_2(app.construct_path("setupAD.ps1")),
        )
        self.setup_AD.pack(pady=4)

        self.join_Domain = ttk.Button(
            self,
            text="Join Domain",
            command=lambda: run_ps1_script_2(app.construct_path("joinDomain.ps1")),
        )
        self.join_Domain.pack(pady=4)

        self.enable_remote = ttk.Button(
            self,
            text="Enable PSRemote",
            command=lambda: run_ps1_script_2(app.construct_path("enableRemoting.ps1")),
        )
        self.enable_remote.pack(pady=4)
