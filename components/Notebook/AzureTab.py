import customtkinter
from lib.functions import run_ps1_script_async
from lib.utils import construct_path


class AzureTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")
        self.app = app

        self.connect_azure_button = customtkinter.CTkButton(
            self,
            text="Connect to Azure",
            command=lambda: self.run_script("Azure-Automation/Connect-Azure.ps1")
        )
        self.connect_azure_button.pack(pady=4)

        self.get_rg_button = customtkinter.CTkButton(
            self,
            text="Get Resource Groups",
            command=lambda: self.run_script("Azure-Automation/Get-AzureResourceGroup.ps1")
        )
        self.get_rg_button.pack(pady=4)

        self.get_storage_button = customtkinter.CTkButton(
            self,
            text="Get Storage Accounts",
            command=lambda: self.run_script("Azure-Automation/Get-AzureStorageAccount.ps1")
        )
        self.get_storage_button.pack(pady=4)

        self.create_vm_button = customtkinter.CTkButton(
            self,
            text="Create Azure VM",
            command=lambda: self.run_script("Azure-Automation/New-AzureVM.ps1")
        )
        self.create_vm_button.pack(pady=4)

    def run_script(self, script_name):
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        # Assuming elevation might be needed for Azure CLI operations
        run_ps1_script_async(script_path, elevated=True)
