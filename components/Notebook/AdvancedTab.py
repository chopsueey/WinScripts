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

        # --- Access Frame ---
        access_frame = customtkinter.CTkFrame(self)
        access_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")
        access_frame.columnconfigure(0, weight=1)

        self.create_user_button = customtkinter.CTkButton(access_frame, text="Create Local User", command=self.prompt_for_create_user)
        self.create_user_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.RDP_button = customtkinter.CTkButton(access_frame, text="Activate RDP", command=lambda: self.run_script("activateRDP.ps1"))
        self.RDP_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.activateAdmin = customtkinter.CTkButton(access_frame, text="Activate Admin", command=lambda: self.run_script("activateAdmin.ps1"))
        self.activateAdmin.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.enable_remote = customtkinter.CTkButton(access_frame, text="Enable PSRemote", command=lambda: self.run_script("enableRemoting.ps1"))
        self.enable_remote.grid(row=3, column=0, padx=10, pady=(5, 10), sticky="ew")

        # --- Config Frame ---
        config_frame = customtkinter.CTkFrame(self)
        config_frame.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")
        config_frame.columnconfigure(0, weight=1)

        self.setComputerName_button = customtkinter.CTkButton(config_frame, text="Set Computer Name", command=self.prompt_for_set_computer_name)
        self.setComputerName_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setIP_button = customtkinter.CTkButton(config_frame, text="Set IP Address", command=self.prompt_for_set_ip)
        self.setIP_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.installWebServer_button = customtkinter.CTkButton(config_frame, text="Install Web Server (IIS)", command=self.prompt_for_install_web_server)
        self.installWebServer_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.installBGInfo_button = customtkinter.CTkButton(config_frame, text="Install BGInfo", command=lambda: self.run_script("installBGInfo.ps1"))
        self.installBGInfo_button.grid(row=3, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_script(self, script_name, ps_args=None):
        if ps_args is None:
            ps_args = []
        script_path = construct_path(self.app.current_script_dir, self.app.script_dir_relative, script_name)
        run_ps1_script_async(script_path, ps_args=ps_args, elevated=True)

    def prompt_for_create_user(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Create Local User")
        dialog.geometry("400x250")
        dialog.transient(self.app)
        dialog.columnconfigure(1, weight=1)

        customtkinter.CTkLabel(dialog, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        user_entry = customtkinter.CTkEntry(dialog)
        user_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="Full Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        full_name_entry = customtkinter.CTkEntry(dialog)
        full_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="Description:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        desc_entry = customtkinter.CTkEntry(dialog)
        desc_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="Groups (comma-sep):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        groups_entry = customtkinter.CTkEntry(dialog, placeholder_text="e.g., Administrators,Users")
        groups_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        def run_with_args():
            username = user_entry.get()
            if not username: return
            ps_args = ["-UserName", username]
            if full_name_entry.get(): ps_args.extend(["-FullName", full_name_entry.get()])
            if desc_entry.get(): ps_args.extend(["-Description", desc_entry.get()])
            if groups_entry.get(): ps_args.extend(["-AddToGroup", f"'{groups_entry.get()}'"])
            self.run_script("Create-LocalUser.ps1", ps_args)
            dialog.destroy()

        customtkinter.CTkButton(dialog, text="Create User", command=run_with_args).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        dialog.grab_set()
        user_entry.focus()

    def prompt_for_set_computer_name(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Set Computer Name")
        dialog.geometry("400x150")
        dialog.transient(self.app)
        dialog.columnconfigure(1, weight=1)

        customtkinter.CTkLabel(dialog, text="New Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        name_entry = customtkinter.CTkEntry(dialog)
        name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        restart_var = customtkinter.StringVar(value="on")
        customtkinter.CTkCheckBox(dialog, text="Restart after rename", variable=restart_var, onvalue="on", offvalue="off").grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        def run_with_args():
            name = name_entry.get()
            if not name: return
            ps_args = ["-NewName", name]
            if restart_var.get() == "on": ps_args.append("-Restart")
            self.run_script("setComputerName.ps1", ps_args)
            dialog.destroy()

        customtkinter.CTkButton(dialog, text="Set Name", command=run_with_args).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        dialog.grab_set()
        name_entry.focus()

    def prompt_for_set_ip(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Set Static IP Address")
        dialog.geometry("400x280")
        dialog.transient(self.app)
        dialog.columnconfigure(1, weight=1)

        customtkinter.CTkLabel(dialog, text="Interface Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        iface_entry = customtkinter.CTkEntry(dialog, placeholder_text="e.g., Ethernet")
        iface_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="IP Address:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ip_entry = customtkinter.CTkEntry(dialog, placeholder_text="e.g., 192.168.1.100")
        ip_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="Prefix Length:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        prefix_entry = customtkinter.CTkEntry(dialog, placeholder_text="e.g., 24")
        prefix_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="Gateway:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        gateway_entry = customtkinter.CTkEntry(dialog, placeholder_text="e.g., 192.168.1.1")
        gateway_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        customtkinter.CTkLabel(dialog, text="DNS Servers:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        dns_entry = customtkinter.CTkEntry(dialog, placeholder_text="e.g., 8.8.8.8,1.1.1.1")
        dns_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        def run_with_args():
            if not (iface_entry.get() and ip_entry.get() and prefix_entry.get()): return
            ps_args = ["-InterfaceAlias", iface_entry.get(), "-IPAddress", ip_entry.get(), "-PrefixLength", prefix_entry.get()]
            if gateway_entry.get(): ps_args.extend(["-Gateway", gateway_entry.get()])
            if dns_entry.get(): ps_args.extend(["-DnsServers", f"'{dns_entry.get()}'"])
            self.run_script("setIP.ps1", ps_args)
            dialog.destroy()

        customtkinter.CTkButton(dialog, text="Set IP", command=run_with_args).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        dialog.grab_set()
        iface_entry.focus()

    def prompt_for_install_web_server(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Install Web Server (IIS)")
        dialog.geometry("300x150")
        dialog.transient(self.app)

        page_var = customtkinter.StringVar(value="on")
        browser_var = customtkinter.StringVar(value="on")

        customtkinter.CTkCheckBox(dialog, text="Create default test page", variable=page_var, onvalue="on", offvalue="off").pack(padx=20, pady=(10,5), anchor="w")
        customtkinter.CTkCheckBox(dialog, text="Open in browser after install", variable=browser_var, onvalue="on", offvalue="off").pack(padx=20, pady=5, anchor="w")

        def run_with_args():
            ps_args = []
            if page_var.get() == "on": ps_args.append("-InstallDefaultPage")
            if browser_var.get() == "on": ps_args.append("-OpenInBrowser")
            self.run_script("Install-WebServer.ps1", ps_args)
            dialog.destroy()

        customtkinter.CTkButton(dialog, text="Install", command=run_with_args).pack(padx=20, pady=(10,10), fill="x", expand=True)
        dialog.grab_set()
