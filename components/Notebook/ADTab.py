import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_script_2
from lib.utils import construct_path
from components.AdminButton import AdminButton
from lib.ui_helpers import StyledLabelframe


class ADTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

        # Configure the grid layout for the main tab
        self.columnconfigure(0, weight=1)

        # --- Group 4: Domain Management ---
        domain_frame = StyledLabelframe(self, text="Domain Management")
        domain_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
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