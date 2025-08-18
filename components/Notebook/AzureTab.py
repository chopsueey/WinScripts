import customtkinter
from tkinter import messagebox
from lib.functions import run_ps1_script_no_json
from lib.exceptions import ScriptError
from lib.utils import construct_path


class AzureTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")
        self.app = app

        self.connect_azure_button = customtkinter.CTkButton(
            self,
            text="Connect to Azure",
            command=lambda: self.run_script("Azure-Automation/Connect-Azure.ps1", "Connect to Azure")
        )
        self.connect_azure_button.pack(pady=4)

        self.get_rg_button = customtkinter.CTkButton(
            self,
            text="Get Resource Groups",
            command=lambda: self.run_script("Azure-Automation/Get-AzureResourceGroup.ps1", "Get Resource Groups")
        )
        self.get_rg_button.pack(pady=4)

        self.get_storage_button = customtkinter.CTkButton(
            self,
            text="Get Storage Accounts",
            command=lambda: self.run_script("Azure-Automation/Get-AzureStorageAccount.ps1", "Get Storage Accounts")
        )
        self.get_storage_button.pack(pady=4)

        self.create_vm_button = customtkinter.CTkButton(
            self,
            text="Create Azure VM",
            command=lambda: self.run_script("Azure-Automation/New-AzureVM.ps1", "Create Azure VM")
        )
        self.create_vm_button.pack(pady=4)

    def run_script(self, script_name, command_name):
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        try:
            output = run_ps1_script_no_json(script_path)
            messagebox.showinfo(f"{command_name} Succeeded", f"Successfully executed {command_name}.\n\nOutput:\n{output}")
        except ScriptError as e:
            messagebox.showerror(f"{command_name} Failed", f"An error occurred while trying to {command_name.lower()}:\n\n{e}")
