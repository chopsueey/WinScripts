import customtkinter
from lib.functions import run_ps1_script_async
from lib.utils import construct_path


class AdvancedTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")
        self.app = app

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        access_frame = customtkinter.CTkFrame(self)
        access_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        access_frame.columnconfigure(0, weight=1)

        self.RDP_button = customtkinter.CTkButton(
            access_frame,
            text="Activate RDP",
            command=lambda: self.run_script("activateRDP.ps1")
        )
        self.RDP_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.activateAdmin = customtkinter.CTkButton(
            access_frame,
            text="Activate Admin",
            command=lambda: self.run_script("activateAdmin.ps1")
        )
        self.activateAdmin.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.enable_remote = customtkinter.CTkButton(
            access_frame,
            text="Enable PSRemote",
            command=lambda: self.run_script("enableRemoting.ps1")
        )
        self.enable_remote.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")

        config_frame = customtkinter.CTkFrame(self)
        config_frame.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")
        config_frame.columnconfigure(0, weight=1)

        self.setComputerName_button = customtkinter.CTkButton(
            config_frame,
            text="Set ComputerName",
            command=lambda: self.run_script("setComputerName.ps1")
        )
        self.setComputerName_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setIP_button = customtkinter.CTkButton(
            config_frame,
            text="Set IP",
            command=lambda: self.run_script("setIP.ps1")
        )
        self.setIP_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.installBGInfo_button = customtkinter.CTkButton(
            config_frame,
            text="Install BGInfo",
            command=lambda: self.run_script("installBGInfo.ps1")
        )
        self.installBGInfo_button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_script(self, script_name):
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        # These scripts require elevation
        run_ps1_script_async(script_path, elevated=True)