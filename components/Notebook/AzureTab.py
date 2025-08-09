import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_script_2
from lib.utils import construct_path
from components.AdminButton import AdminButton


class AzureTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

        self.connect_azure_button = AdminButton(
            self,
            text="Connect to Azure",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "Azure-Automation/Connect-Azure.ps1",
                )
            ),
        )
        self.connect_azure_button.pack(pady=4)

        self.get_rg_button = AdminButton(
            self,
            text="Get Resource Groups",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "Azure-Automation/Get-AzureResourceGroup.ps1",
                )
            ),
        )
        self.get_rg_button.pack(pady=4)

        self.get_storage_button = AdminButton(
            self,
            text="Get Storage Accounts",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "Azure-Automation/Get-AzureStorageAccount.ps1",
                )
            ),
        )
        self.get_storage_button.pack(pady=4)

        self.create_vm_button = AdminButton(
            self,
            text="Create Azure VM",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir,
                    app.script_dir_relative,
                    "Azure-Automation/New-AzureVM.ps1",
                )
            ),
        )
        self.create_vm_button.pack(pady=4)
