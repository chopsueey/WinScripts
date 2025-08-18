import customtkinter
from lib.functions import run_command_async, run_ps1_script_async
from lib.utils import construct_path


class GeneralTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")
        self.app = app

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # --- PowerShell Frame ---
        ps_frame = customtkinter.CTkFrame(self)
        ps_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        ps_frame.columnconfigure(0, weight=1)

        self.open_standard_pwsh = customtkinter.CTkButton(
            ps_frame,
            text="Open PowerShell",
            command=lambda: run_command_async("Start-Process powershell.exe -Verb RunAs")
        )
        self.open_standard_pwsh.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.open_new_pwsh = customtkinter.CTkButton(
            ps_frame,
            text="Open PowerShell 7",
            command=lambda: run_command_async("Start-Process pwsh.exe -Verb RunAs")
        )
        self.open_new_pwsh.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

        # --- Diagnostics Frame ---
        diag_frame = customtkinter.CTkFrame(self)
        diag_frame.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")
        diag_frame.columnconfigure(0, weight=1)

        self.health_check_button = customtkinter.CTkButton(
            diag_frame,
            text="Get System Health",
            command=lambda: self.run_script("Get-SystemHealth.ps1")
        )
        self.health_check_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.event_log_button = customtkinter.CTkButton(
            diag_frame,
            text="Get Recent Errors",
            command=lambda: self.run_script("Get-EventLogErrors.ps1")
        )
        self.event_log_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_script(self, script_name, ps_args=None):
        if ps_args is None:
            ps_args = []
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        # These scripts might need elevation to read all logs/info
        run_ps1_script_async(script_path, ps_args=ps_args, elevated=True)
