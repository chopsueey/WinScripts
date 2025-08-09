import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd, run_ps1_script_2
from lib.utils import construct_path
from components.AdminButton import AdminButton


class GeneralTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

        self.open_standard_pwsh = AdminButton(
            self,
            text="Open PowerShell",
            command=lambda: run_ps1_cmd("Start-Process powershell.exe -Verb RunAs"),
        )
        self.open_standard_pwsh.pack(pady=4)

        self.open_new_pwsh = AdminButton(
            self,
            text="Open PowerShell 7",
            command=lambda: run_ps1_cmd("Start-Process pwsh.exe -Verb RunAs"),
        )
        self.open_new_pwsh.pack(pady=4)

        self.RDP_button = AdminButton(
            self,
            text="Activate RDP",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "activateRDP.ps1"
                )
            ),
        )
        self.RDP_button.pack(pady=4)

        self.activateAdmin = AdminButton(
            self,
            text="Activate Admin",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "activateAdmin.ps1",
                )
            ),
        )
        self.activateAdmin.pack(pady=4)

        self.setIP_button = AdminButton(
            self,
            text="Set IP",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "setIP.ps1"
                )
            ),
        )
        self.setIP_button.pack(pady=4)

        self.installBGInfo_button = AdminButton(
            self,
            text="Install BGInfo",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "installBGInfo.ps1",
                )
            ),
        )
        self.installBGInfo_button.pack(pady=4)

        self.setComputerName_button = AdminButton(
            self,
            text="Set ComputerName",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "setComputerName.ps1",
                )
            ),
        )
        self.setComputerName_button.pack(pady=4)

        self.setup_AD = AdminButton(
            self,
            text="Install AD",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "setupAD.ps1"
                )
            ),
        )
        self.setup_AD.pack(pady=4)

        self.join_Domain = AdminButton(
            self,
            text="Join Domain",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "joinDomain.ps1"
                )
            ),
        )
        self.join_Domain.pack(pady=4)

        self.enable_remote = AdminButton(
            self,
            text="Enable PSRemote",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "enableRemoting.ps1",
                )
            ),
        )
        self.enable_remote.pack(pady=4)
