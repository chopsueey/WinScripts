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
            command=self.prompt_for_join_domain
        )
        self.join_Domain.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        self.setup_AD = customtkinter.CTkButton(
            domain_frame,
            text="Install AD",
            command=self.prompt_for_setup_ad # Updated command
        )
        self.setup_AD.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")

    def run_script(self, script_name, ps_args=None):
        if ps_args is None:
            ps_args = []
        script_path = construct_path(
            self.app.current_script_dir, self.app.script_dir_relative, script_name
        )
        run_ps1_script_async(script_path, ps_args=ps_args, elevated=True)

    def prompt_for_join_domain(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Join Domain")
        dialog.geometry("400x200")
        dialog.transient(self.app)
        dialog.columnconfigure(1, weight=1)
        domain_label = customtkinter.CTkLabel(dialog, text="Domain FQDN:")
        domain_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        domain_entry = customtkinter.CTkEntry(dialog)
        domain_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        ou_label = customtkinter.CTkLabel(dialog, text="OU Path (Optional):")
        ou_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ou_entry = customtkinter.CTkEntry(dialog)
        ou_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        def run_with_args():
            domain_name = domain_entry.get()
            if not domain_name:
                return
            ps_args = ["-DomainName", domain_name]
            ou_path = ou_entry.get()
            if ou_path:
                ps_args.extend(["-OUPath", ou_path])
            self.run_script("joinDomain.ps1", ps_args)
            dialog.destroy()
        run_button = customtkinter.CTkButton(dialog, text="Run", command=run_with_args)
        run_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        dialog.grab_set()
        domain_entry.focus()


    def prompt_for_setup_ad(self):
        dialog = customtkinter.CTkToplevel(self)
        dialog.title("Install Active Directory")
        dialog.geometry("400x200")
        dialog.transient(self.app)

        dialog.columnconfigure(1, weight=1)

        # Domain Name
        domain_label = customtkinter.CTkLabel(dialog, text="New Domain FQDN:")
        domain_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        domain_entry = customtkinter.CTkEntry(dialog)
        domain_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        def run_with_args():
            domain_name = domain_entry.get()
            if not domain_name:
                return

            ps_args = ["-DomainName", domain_name]
            # The script will prompt for the password itself
            self.run_script("setupAD.ps1", ps_args)
            dialog.destroy()

        run_button = customtkinter.CTkButton(dialog, text="Run", command=run_with_args)
        run_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        dialog.grab_set()
        domain_entry.focus()
