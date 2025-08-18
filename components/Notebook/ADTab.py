import customtkinter
from tkinter import messagebox
from lib.functions import run_ps1_script_no_json
from lib.exceptions import ScriptError
from lib.utils import construct_path


class ADTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")
        self.app = app

        self.columnconfigure(0, weight=1)

        domain_frame = customtkinter.CTkFrame(self)
        domain_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        domain_frame.columnconfigure(0, weight=1)

        self.join_Domain = customtkinter.CTkButton(
            domain_frame,
            text="Join Domain",
            command=lambda: self.run_script("joinDomain.ps1", "Join Domain")
        )
        self.join_Domain.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setup_AD = customtkinter.CTkButton(
            domain_frame,
            text="Install AD",
            command=lambda: self.run_script("setupAD.ps1", "Install AD")
        )
        self.setup_AD.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_script(self, script_name, command_name):
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        try:
            output = run_ps1_script_no_json(script_path)
            messagebox.showinfo(f"{command_name} Succeeded", f"Successfully executed {command_name}.\n\nOutput:\n{output}")
        except ScriptError as e:
            messagebox.showerror(f"{command_name} Failed", f"An error occurred while trying to {command_name.lower()}:\n\n{e}")