import customtkinter
from lib.functions import run_ps1_script_2
from lib.utils import construct_path


class ADTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        # Configure the grid layout for the main tab
        self.columnconfigure(0, weight=1)

        # --- Group 4: Domain Management ---
        domain_frame = customtkinter.CTkFrame(self)
        domain_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        domain_frame.columnconfigure(0, weight=1)

        self.join_Domain = customtkinter.CTkButton(
            domain_frame,
            text="Join Domain",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "joinDomain.ps1"
                )
            ),
        )
        self.join_Domain.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setup_AD = customtkinter.CTkButton(
            domain_frame,
            text="Install AD",
            command=lambda: run_ps1_script_2(
                construct_path(
                    app.current_script_dir, app.script_dir_relative, "setupAD.ps1"
                )
            ),
        )
        self.setup_AD.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")