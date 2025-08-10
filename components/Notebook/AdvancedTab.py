import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_script_2
from lib.utils import construct_path
from components.AdminButton import AdminButton
from lib.ui_helpers import StyledLabelframe


class AdvancedTab(ttk.Frame):
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