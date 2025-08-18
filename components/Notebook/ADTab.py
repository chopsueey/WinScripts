import customtkinter
from lib.functions import run_ps1_script_async
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
            command=lambda: self.run_script("joinDomain.ps1")
        )
        self.join_Domain.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setup_AD = customtkinter.CTkButton(
            domain_frame,
            text="Install AD",
            command=lambda: self.run_script("setupAD.ps1")
        )
        self.setup_AD.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_script(self, script_name):
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        # These scripts require elevation
        run_ps1_script_async(script_path, elevated=True)