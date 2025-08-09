import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd, run_ps1_script_2
from lib.utils import construct_path
from components.AdminButton import AdminButton
from lib.ui_helpers import StyledLabelframe


class GeneralTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

        # Configure the grid layout for the main tab
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # --- Group 1: System & Access ---
        access_frame = StyledLabelframe(self, text="System & Access")
        access_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        access_frame.columnconfigure(0, weight=1)

        self.RDP_button = AdminButton(
            access_frame,
            text="Activate RDP",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "activateRDP.ps1"
                )
            ),
        )
        self.RDP_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.activateAdmin = AdminButton(
            access_frame,
            text="Activate Admin",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "activateAdmin.ps1",
                )
            ),
        )
        self.activateAdmin.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.enable_remote = AdminButton(
            access_frame,
            text="Enable PSRemote",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "enableRemoting.ps1",
                )
            ),
        )
        self.enable_remote.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")


        # --- Group 2: PowerShell ---
        ps_frame = StyledLabelframe(self, text="PowerShell")
        ps_frame.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="nsew")
        ps_frame.columnconfigure(0, weight=1)

        self.open_standard_pwsh = AdminButton(
            ps_frame,
            text="Open PowerShell",
            command=lambda: run_ps1_cmd("Start-Process powershell.exe -Verb RunAs"),
        )
        self.open_standard_pwsh.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.open_new_pwsh = AdminButton(
            ps_frame,
            text="Open PowerShell 7",
            command=lambda: run_ps1_cmd("Start-Process pwsh.exe -Verb RunAs"),
        )
        self.open_new_pwsh.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")


        # --- Group 3: Machine Configuration ---
        config_frame = StyledLabelframe(self, text="Machine Configuration")
        config_frame.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")
        config_frame.columnconfigure(0, weight=1)

        self.setComputerName_button = AdminButton(
            config_frame,
            text="Set ComputerName",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "setComputerName.ps1",
                )
            ),
        )
        self.setComputerName_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setIP_button = AdminButton(
            config_frame,
            text="Set IP",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "setIP.ps1"
                )
            ),
        )
        self.setIP_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.installBGInfo_button = AdminButton(
            config_frame,
            text="Install BGInfo",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "installBGInfo.ps1",
                )
            ),
        )
        self.installBGInfo_button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")


        # --- Group 4: Domain Management ---
        domain_frame = StyledLabelframe(self, text="Domain Management")
        domain_frame.grid(row=1, column=1, padx=(5, 10), pady=10, sticky="nsew")
        domain_frame.columnconfigure(0, weight=1)

        self.join_Domain = AdminButton(
            domain_frame,
            text="Join Domain",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "joinDomain.ps1"
                )
            ),
        )
        self.join_Domain.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setup_AD = AdminButton(
            domain_frame,
            text="Install AD",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "setupAD.ps1"
                )
            ),
        )
        self.setup_AD.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")
