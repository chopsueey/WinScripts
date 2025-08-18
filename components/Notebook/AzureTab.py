import customtkinter
from lib.functions import run_ps1_script_2
from lib.utils import construct_path


class AzureTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        self.connect_azure_button = customtkinter.CTkButton(
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

        self.get_rg_button = customtkinter.CTkButton(
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

        self.get_storage_button = customtkinter.CTkButton(
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

        self.create_vm_button = customtkinter.CTkButton(
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
