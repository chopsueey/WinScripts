import tkinter as tk
from tkinter import ttk, filedialog
from lib.functions import run_ps1_script, run_ps1_script_elevated
import os, json


class CreateVMTab(tk.Frame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        # State
        self.app = app
        self.iso_path = tk.StringVar(value="No ISO choosen yet.")
        self.editions = []
        self.selected_edition = tk.StringVar(value="No edition selected.")
        self.version_name = ""
        self.vm_switches = []
        self.selected_vm_switch = tk.StringVar(value="No switch selected.")
        self.selected_network_category = tk.StringVar()
        self.selected_network_category.set("Private")  # default
        self.network_category_options = ["Public", "Private", "Domain"]

        # Topframe (ISO, Edition and VMSwitches)
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(expand=True, fill="both")

        self.iso_frame = ttk.Labelframe(self.top_frame, text="ISO")
        self.iso_frame.pack(
            expand=True, fill="both", padx=4
        )  # anchor='center' without fill, to center children
        self.iso_path_label = ttk.Label(self.iso_frame, textvariable=self.iso_path)
        self.iso_path_label.pack(side="left", padx=4)
        self.choose_iso = ttk.Button(
            self.iso_frame, text="Choose ISO", command=self.get_windows_image_editions
        )
        self.choose_iso.pack(side="left", padx=4)

        self.edition_frame = ttk.Labelframe(self.top_frame, text="Edition")
        self.edition_frame.pack(expand=True, fill="both", padx=4)
        self.edition_info_label = ttk.Label(
            self.edition_frame, textvariable=self.selected_edition
        )
        self.edition_info_label.pack(side="left", padx=4)
        self.edition_combobox = ttk.Combobox(
            self.edition_frame, textvariable=self.selected_edition, state="readonly"
        )
        self.edition_combobox.pack(side="left", padx=4)
        self.edition_combobox.set("Choose an iso first...")
        self.edition_combobox.bind("<<ComboboxSelected>>", self.on_edition_selected)

        self.vm_switches_frame = ttk.Labelframe(self.top_frame, text="Virtual switch")
        self.vm_switches_frame.pack(expand=True, fill="both", padx=4)
        self.vm_switches_info_label = ttk.Label(
            self.vm_switches_frame, text="No switch selected yet."
        )
        self.vm_switches_info_label.pack(side="left", padx=4)
        self.vm_switches_combobox = ttk.Combobox(
            self.vm_switches_frame,
            textvariable=self.selected_vm_switch,
            state="readonly",
        )
        self.vm_switches_combobox.pack(side="left", padx=4)
        self.vm_switches_combobox.set("Choose a switch...")
        self.vm_switches_combobox.bind(
            "<<ComboboxSelected>>", self.on_vm_switch_selected
        )

        # Bottomframe
        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.pack(expand=True, fill="both")

        self.name_pass_frame = ttk.Labelframe(
            self.bottom_frame, text="Name and password"
        )
        self.name_pass_frame.pack(expand=True, fill="both", padx=4)
        self.vm_name_label = ttk.Label(self.name_pass_frame, text="VM Name: ")
        self.vm_name_label.pack(side="left", padx=4)
        self.vm_name_entry = ttk.Entry(self.name_pass_frame)
        self.vm_name_entry.pack(side="left", padx=4)
        self.password_label = ttk.Label(self.name_pass_frame, text="Password: ")
        self.password_label.pack(side="left", padx=4)
        self.password_entry = ttk.Entry(self.name_pass_frame)
        self.password_entry.pack(side="left", padx=4)

        # -MemoryStartupBytes 4GB `
        # -VMProcessorCount 2 `
        # -VHDXSizeBytes 60GB `
        self.resources_frame = ttk.Labelframe(self.bottom_frame, text="Resources")
        self.resources_frame.pack(expand=True, fill="both", padx=4)
        self.ram_label = ttk.Label(self.resources_frame, text="RAM in GB: ")
        self.ram_label.pack(side="left", padx=4)
        self.ram_entry = ttk.Entry(self.resources_frame)
        self.ram_entry.pack(side="left", padx=4)
        self.processor_count_label = ttk.Label(
            self.resources_frame, text="Processor count: "
        )
        self.processor_count_label.pack(side="left", padx=4)
        self.processor_count_entry = ttk.Entry(self.resources_frame)
        self.processor_count_entry.pack(side="left", padx=4)
        self.vhdx_size_label = ttk.Label(self.resources_frame, text="VHDX Size: ")
        self.vhdx_size_label.pack(side="left", padx=4)
        self.vhdx_size_entry = ttk.Entry(self.resources_frame)
        self.vhdx_size_entry.pack(side="left", padx=4)

        # -IPAddress 10.0.0.10 `
        # -PrefixLength 8 `
        # -DefaultGateway 10.0.0.10 `
        # -DnsAddresses '8.8.8.8', '8.8.4.4' `
        # -NetworkCategory 'Public', 'Private', 'Domain'?
        self.network_settings_frame = ttk.Labelframe(
            self.bottom_frame, text="Network settings"
        )
        self.network_settings_frame.pack(expand=True, fill="both", padx=4)
        self.ip_label = ttk.Label(self.network_settings_frame, text="IPv4 address: ")
        self.ip_label.pack(side="left", padx=4)
        self.ip_entry = ttk.Entry(self.network_settings_frame)
        self.ip_entry.pack(side="left", padx=4)
        self.prefix_length_label = ttk.Label(
            self.network_settings_frame, text="Prefix length (CIDR): "
        )
        self.prefix_length_label.pack(side="left", padx=4)
        self.prefix_length_entry = ttk.Entry(self.network_settings_frame)
        self.prefix_length_entry.pack(side="left", padx=4)
        self.gateway_label = ttk.Label(
            self.network_settings_frame, text="Default gateway: "
        )
        self.gateway_label.pack(side="left", padx=4)
        self.gateway_entry = ttk.Entry(self.network_settings_frame)
        self.gateway_entry.pack(side="left", padx=4)
        self.dns_label = ttk.Label(self.network_settings_frame, text="DNS Addresses: ")
        self.dns_label.pack(side="left", padx=4)
        self.dns_entry = ttk.Entry(self.network_settings_frame)
        self.dns_entry.pack(side="left", padx=4)
        self.network_category_option_menu = ttk.OptionMenu(
            self.network_settings_frame,
            self.selected_network_category,
            self.selected_network_category.get(),
            *self.network_category_options,
            # command=self.on_network_category_selected,
        )
        self.network_category_option_menu.pack(side="left", padx=4)

        # Create VM (TODO: Show all choosen options for the VM and ask for the user to accept them, and only then start the script)
        self.create_vm_button = ttk.Button(
            self, text="Create VM", command=self.create_vm
        )
        self.create_vm_button.pack()

    # METHODS
    # def on_network_category_selected(self, network_category):
    # self.status_label.config(text=f"Choosen network category: {network_category}")
    # print(self.selected_network_category.get())

    def get_windows_image_editions(self):
        isopath = filedialog.askopenfilename()
        self.iso_path.set(isopath)

        run_ps1_script_elevated(
            self.app.construct_path("getIsoEditions.ps1"),
            window=False,
            ps_args=[
                "-IsoPath",
                f"{self.iso_path.get()}",
                "-AppRootPath",
                f"{self.app.get_root_path()}",
            ],
        )

        json_file_path = os.path.join(self.app.get_root_path(), "image_names.json")

        # Above script creates a json file with the image edition names of the iso.
        # Note: This step is not necessary when app run as administrator (see self.load_switches)

        with open(json_file_path, "r", encoding="utf-8-sig") as file:
            self.editions = json.loads(file.read())

        self.load_editions()
        self.load_switches()

    def load_editions(self):
        if self.editions:
            # self.editions is a single string if the iso just has one available edition
            # else it is a list
            if type(self.editions) == str:
                self.edition_combobox["values"] = [self.editions]
                self.edition_combobox.set(self.editions)
            else:
                self.edition_combobox["values"] = self.editions
                self.edition_combobox.set(self.editions[0])

            self.edition_info_label.config(
                text=f"Loaded {len(self.editions)} editions."
            )
        else:
            self.edition_combobox["values"] = []
            self.edition_combobox.set("No editions found.")
            self.edition_info_label.config(
                text="No editions found or an error occurred."
            )

    def on_edition_selected(self, event):
        selected = self.selected_edition.get()
        self.edition_info_label.config(text=f"You selected: {selected}")
        self.version_name = self.get_validate_set_string()

        print(f"Selected edition: {selected}", self.version_name)

    def load_switches(self):
        self.vm_switches = run_ps1_script(
            self.app.construct_path("getVMSwitches.ps1"),
            ps_args=[
                "-IsoPath",
                f"{self.iso_path.get()}",
                "-AppRootPath",
                f"{self.app.get_root_path()}",
            ],
        )

        if self.vm_switches:
            # self.editions is a single string if the iso just has one available edition
            # else it is a list
            if type(self.vm_switches) == str:
                self.vm_switches_combobox["values"] = [self.vm_switches]
                self.vm_switches_combobox.set(self.vm_switches)
            else:
                self.vm_switches_combobox["values"] = self.vm_switches
                self.vm_switches_combobox.set(self.vm_switches[0])

            self.vm_switches_info_label.config(
                text=f"Loaded {len(self.vm_switches)} switches."
            )
        else:
            self.vm_switches_combobox["values"] = []
            self.vm_switches_combobox.set("No switches found.")
            self.vm_switches_info_label.config(
                text="No switches found or an error occurred."
            )

    def on_vm_switch_selected(self, event):
        selected = self.selected_vm_switch.get()
        self.vm_switches_info_label.config(text=f"You selected: {selected}")

        print(f"Selected switch: {selected}")

    def get_validate_set_string(self):
        # Replace unnecessary substrings
        normalized_edition = (
            self.selected_edition.get()
            .lower()
            .replace("windows ", "")
            .replace("server ", "")
            .replace(" evaluation", "")
            .replace("(desktopdarstellung)", "")
            .replace("(desktop experience)", "")
            .strip()
        )

        # Return specific Versionname for choosen selected_edition
        if "2025 datacenter" in normalized_edition:
            return "Server2025Datacenter"
        elif "2025 standard" in normalized_edition:
            return "Server2025Standard"
        elif "2022 datacenter" in normalized_edition:
            return "Server2022Datacenter"
        elif "2022 standard" in normalized_edition:
            return "Server2022Standard"
        elif "2019 datacenter" in normalized_edition:
            return "Server2019Datacenter"
        elif "2019 standard" in normalized_edition:
            return "Server2019Standard"
        elif "2016 datacenter" in normalized_edition:
            return "Server2016Datacenter"
        elif "2016 standard" in normalized_edition:
            return "Server2016Standard"
        elif "11 enterprise" in normalized_edition:
            return "Windows11Enterprise"
        elif "11 professional" in normalized_edition:
            return "Windows11Professional"
        elif "10 enterprise" in normalized_edition:
            return "Windows10Enterprise"
        elif "10 professional" in normalized_edition:
            return "Windows10Professional"
        elif (
            "81 professional" in normalized_edition
            or "8.1 professional" in normalized_edition
        ):
            return "Windows81Professional"

        return None

    def create_vm(self):
        print(self.app.construct_path(r".\\Hyper-V-Automation\\create_Vm.ps1"))

        # Get all user input
        # self.vm_name_entry
        # self.password_entry
        # self.ram_entry
        # self.processor_count_entry
        # self.vhdx_size_entry
        # self.ip_entry
        # self.prefix_length_entry
        # self.gateway_entry
        # self.dns_entry
        # self.selected_network_category

        run_ps1_script_elevated(
            self.app.construct_path(r".\\Hyper-V-Automation\\create_Vm.ps1"),
            window=True,
            ps_args=[
                "-isoFile",
                f"{self.iso_path.get()}",
                "-vmName",
                f"{'test123'}",
                "-pass",
                f"P@ssw0rd",
                "-iso_edition",
                f"{self.selected_edition.get()}",
                "-version_name",
                f"{self.version_name}",
                "-VMSwitch",
                f"{self.selected_vm_switch.get()}",
                "-script_path",
                f"{self.app.construct_path(r'.\\Hyper-V-Automation\\')}",
            ],
        )
