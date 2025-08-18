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
            command=self.prompt_for_connect_azure # Updated
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

    def run_script(self, script_name, ps_args=None): # Updated
        if ps_args is None:
            ps_args = []
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        run_ps1_script_async(script_path, ps_args=ps_args, elevated=True)

    def prompt_for_connect_azure(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Connect to Azure")
        dialog.geometry("350x120")
        dialog.transient(self.app)

        force_var = customtkinter.StringVar(value="off")

        customtkinter.CTkCheckBox(dialog, text="Force install 'Az.Accounts' module without prompt", variable=force_var, onvalue="on", offvalue="off").pack(padx=20, pady=(10,5), anchor="w")

        def run_with_args():
            ps_args = []
            if force_var.get() == "on":
                ps_args.append("-Force")
            self.run_script("Azure-Automation/Connect-Azure.ps1", ps_args)
            dialog.destroy()

        customtkinter.CTkButton(dialog, text="Connect", command=run_with_args).pack(padx=20, pady=(10,10), fill="x", expand=True)
        dialog.grab_set()
