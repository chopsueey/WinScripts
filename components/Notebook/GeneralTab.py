import customtkinter
from tkinter import messagebox
from lib.functions import run_ps1_cmd
from lib.exceptions import ScriptError


class GeneralTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")
        self.app = app

        self.columnconfigure(0, weight=1)

        ps_frame = customtkinter.CTkFrame(self)
        ps_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        ps_frame.columnconfigure(0, weight=1)

        self.open_standard_pwsh = customtkinter.CTkButton(
            ps_frame,
            text="Open PowerShell",
            command=lambda: self.run_command("Start-Process powershell.exe -Verb RunAs", "Open PowerShell")
        )
        self.open_standard_pwsh.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.open_new_pwsh = customtkinter.CTkButton(
            ps_frame,
            text="Open PowerShell 7",
            command=lambda: self.run_command("Start-Process pwsh.exe -Verb RunAs", "Open PowerShell 7")
        )
        self.open_new_pwsh.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_command(self, command, command_name):
        try:
            run_ps1_cmd(command)
        except ScriptError as e:
            messagebox.showerror(f"{command_name} Failed", f"An error occurred while trying to {command_name.lower()}:\n\n{e}")
