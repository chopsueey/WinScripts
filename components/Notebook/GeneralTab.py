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

        # --- Group 2: PowerShell ---
        ps_frame = StyledLabelframe(self, text="PowerShell")
        ps_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
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
