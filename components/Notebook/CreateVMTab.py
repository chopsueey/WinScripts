import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from lib.functions import run_ps1_script_2, run_ps1_script
from lib.utils import construct_path
from lib.ui_helpers import (
    StyledFrame,
    StyledLabelframe,
    StyledLabel,
    StyledButton,
    StyledCombobox,
    StyledEntry,
)
import os


class CreateVMTab(StyledFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app

        self._initialize_state()
        self._create_widgets()
        self._pack_widgets()
        self._bind_events()

        self.load_switches()

    def _initialize_state(self):
        """Initializes the state variables for the tab."""
        self.iso_path = tk.StringVar(value="No ISO chosen yet.")
        self.editions = []
        self.selected_edition = tk.StringVar(value="No edition selected.")
        self.version_name = ""
        self.vm_switches = []
        self.selected_vm_switch = tk.StringVar(value="No switch selected.")
        self.selected_network_category = tk.StringVar(value="Private")
        self.network_category_options = ["Public", "Private"]

    def _create_widgets(self):
        """Creates all the widgets for the tab."""
        # Frames
        self.top_frame = StyledFrame(self)
        self.iso_frame = StyledLabelframe(self.top_frame, text="ISO")
        self.edition_frame = StyledLabelframe(self.top_frame, text="Edition")
        self.vm_switches_frame = StyledLabelframe(self.top_frame, text="Virtual switch")
        self.bottom_frame = StyledFrame(self)
        self.name_pass_frame = StyledLabelframe(self.bottom_frame, text="Name and password")
        self.resources_frame = StyledLabelframe(self.bottom_frame, text="Resources")
        self.network_settings_frame = StyledLabelframe(self.bottom_frame, text="Network settings")

        # ISO Widgets
        self.iso_path_label = StyledLabel(self.iso_frame, textvariable=self.iso_path)
        self.choose_iso_button = StyledButton(self.iso_frame, text="Choose ISO", command=self.get_windows_image_editions)

        # Edition Widgets
        self.edition_info_label = StyledLabel(self.edition_frame, textvariable=self.selected_edition)
        self.edition_combobox = StyledCombobox(self.edition_frame, textvariable=self.selected_edition, state="readonly", width=70)
        self.edition_combobox.set("Choose an ISO first...")

        # VM Switches Widgets
        self.vm_switches_info_label = StyledLabel(self.vm_switches_frame, text="No switch selected yet.")
        self.vm_switches_combobox = StyledCombobox(self.vm_switches_frame, textvariable=self.selected_vm_switch, state="readonly", width=40)
        self.vm_switches_combobox.set("Choose a switch...")

        # Name and Password Widgets
        self.vm_name_label = StyledLabel(self.name_pass_frame, text="VM Name:")
        self.vm_name_entry = StyledEntry(self.name_pass_frame)
        self.password_label = StyledLabel(self.name_pass_frame, text="Password:")
        self.password_entry = StyledEntry(self.name_pass_frame, show="*")

        # Resources Widgets
        self.ram_label = StyledLabel(self.resources_frame, text="RAM (GB):")
        self.ram_entry = StyledEntry(self.resources_frame)
        self.processor_count_label = StyledLabel(self.resources_frame, text="Processors:")
        self.processor_count_entry = StyledEntry(self.resources_frame)
        self.vhdx_size_label = StyledLabel(self.resources_frame, text="VHDX Size (GB):")
        self.vhdx_size_entry = StyledEntry(self.resources_frame)

        # Network Settings Widgets
        self.ip_label = StyledLabel(self.network_settings_frame, text="IPv4 Address:")
        self.ip_entry = StyledEntry(self.network_settings_frame)
        self.prefix_length_label = StyledLabel(self.network_settings_frame, text="Prefix (CIDR):")
        self.prefix_length_entry = StyledEntry(self.network_settings_frame)
        self.gateway_label = StyledLabel(self.network_settings_frame, text="Gateway:")
        self.gateway_entry = StyledEntry(self.network_settings_frame)
        self.dns_label = StyledLabel(self.network_settings_frame, text="DNS:")
        self.dns_entry = StyledEntry(self.network_settings_frame)

        # Replace OptionMenu with a more modern Combobox
        self.network_category_label = StyledLabel(self.network_settings_frame, text="Network Category:")
        self.network_category_combobox = StyledCombobox(
            self.network_settings_frame,
            textvariable=self.selected_network_category,
            state="readonly"
        )
        self.network_category_combobox["values"] = self.network_category_options
        self.network_category_combobox.set(self.selected_network_category.get())


        # Create VM Button
        self.create_vm_button = StyledButton(self, text="Create VM", command=self.create_vm)

    def _pack_widgets(self):
        """Packs all the widgets in the tab."""
        # Standardized padding
        PAD_X = 5
        PAD_Y = 5

        self.top_frame.pack(expand=True, fill="both", padx=PAD_X, pady=PAD_Y)
        self.iso_frame.pack(expand=True, fill="x", padx=PAD_X, pady=PAD_Y)
        self.iso_path_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.choose_iso_button.pack(side="left", padx=PAD_X, pady=PAD_Y)

        self.edition_frame.pack(expand=True, fill="x", padx=PAD_X, pady=PAD_Y)
        self.edition_info_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.edition_combobox.pack(side="left", padx=PAD_X, pady=PAD_Y)

        self.vm_switches_frame.pack(expand=True, fill="x", padx=PAD_X, pady=PAD_Y)
        self.vm_switches_info_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.vm_switches_combobox.pack(side="left", padx=PAD_X, pady=PAD_Y)

        self.bottom_frame.pack(expand=True, fill="both", padx=PAD_X, pady=PAD_Y)
        self.name_pass_frame.pack(expand=True, fill="x", padx=PAD_X, pady=PAD_Y)
        self.vm_name_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.vm_name_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.password_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.password_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)

        self.resources_frame.pack(expand=True, fill="x", padx=PAD_X, pady=PAD_Y)
        self.ram_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.ram_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.processor_count_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.processor_count_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.vhdx_size_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.vhdx_size_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)

        self.network_settings_frame.pack(expand=True, fill="x", padx=PAD_X, pady=PAD_Y)
        self.ip_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.ip_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.prefix_length_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.prefix_length_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.gateway_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.gateway_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.dns_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.dns_entry.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.network_category_label.pack(side="left", padx=PAD_X, pady=PAD_Y)
        self.network_category_combobox.pack(side="left", padx=PAD_X, pady=PAD_Y)

        self.create_vm_button.pack(pady=10)

    def _bind_events(self):
        """Binds events to widgets."""
        self.edition_combobox.bind("<<ComboboxSelected>>", self.on_edition_selected)
        self.vm_switches_combobox.bind("<<ComboboxSelected>>", self.on_vm_switch_selected)

    def _populate_combobox_from_ps(self, script_name, ps_args, combobox, info_label, data_list, no_items_msg):
        """Helper to populate a combobox by running a PowerShell script."""
        script_path = construct_path(self.app.current_script_dir, self.app.script_dir_relative, script_name)
        items = run_ps1_script(script_path, window=False, ps_args=ps_args)

        if isinstance(items, str):
            items = [items]

        data_list[:] = items if items else []

        if data_list:
            combobox["values"] = data_list
            combobox.set(data_list[0])
            if info_label:
                info_label.config(text=f"Loaded {len(data_list)} items.")
        else:
            combobox["values"] = []
            combobox.set(no_items_msg)
            if info_label:
                info_label.config(text=no_items_msg)

    def get_windows_image_editions(self):
        isopath = filedialog.askopenfilename(filetypes=[("ISO files", "*.iso")])
        if not isopath:
            return
        self.iso_path.set(isopath)

        ps_args = ["-IsoPath", f"{self.iso_path.get()}"]
        self._populate_combobox_from_ps(
            "getIsoEditions.ps1", ps_args, self.edition_combobox, self.edition_info_label, self.editions, "No editions found."
        )

    def on_edition_selected(self, event):
        selected = self.selected_edition.get()
        self.edition_info_label.config(text=f"You selected: {selected}")
        self.version_name = self._get_version_name_from_edition()
        print(f"Selected edition: {selected}", self.version_name)

    def load_switches(self):
        ps_args = ["-AppRootPath", f"{self.app.get_root_path()}"]
        self._populate_combobox_from_ps(
            "getVMSwitches.ps1", ps_args, self.vm_switches_combobox, self.vm_switches_info_label, self.vm_switches, "No switches found."
        )

    def on_vm_switch_selected(self, event):
        selected = self.selected_vm_switch.get()
        self.vm_switches_info_label.config(text=f"You selected: {selected}")
        print(f"Selected switch: {selected}")

    def _get_version_name_from_edition(self):
        """Gets the script-friendly version name from the selected edition string."""
        edition_map = {
            "2025 datacenter": "Server2025Datacenter",
            "2025 standard": "Server2025Standard",
            "2022 datacenter": "Server2022Datacenter",
            "2022 standard": "Server2022Standard",
            "2019 datacenter": "Server2019Datacenter",
            "2019 standard": "Server2019Standard",
            "2016 datacenter": "Server2016Datacenter",
            "2016 standard": "Server2016Standard",
            "11 enterprise": "Windows11Enterprise",
            "11 professional": "Windows11Professional",
            "10 enterprise": "Windows10Enterprise",
            "10 professional": "Windows10Professional",
            "81 professional": "Windows81Professional",
            "8.1 professional": "Windows81Professional",
        }

        normalized_edition = self.selected_edition.get().lower()
        for key, value in edition_map.items():
            if key in normalized_edition:
                return value
        return None

    def create_vm(self):
        """Gathers VM parameters, confirms with the user, and runs the creation script."""
        vm_params = {
            "isoFile": self.iso_path.get(),
            "vmName": self.vm_name_entry.get(),
            "pass": self.password_entry.get(),
            "iso_edition": self.selected_edition.get(),
            "version_name": self.version_name,
            "nameSwitch": self.selected_vm_switch.get(),
            "script_path": construct_path(self.app.current_script_dir, self.app.script_dir_relative, r".\\Hyper-V-Automation\\"),
            "MemoryStartupGB": self.ram_entry.get(),
            "VMProcessorCount": self.processor_count_entry.get(),
            "VHDXSizeGB": self.vhdx_size_entry.get(),
            "IPAddress": self.ip_entry.get(),
            "PrefixLength": self.prefix_length_entry.get(),
            "DefaultGateway": self.gateway_entry.get(),
            "DnsAddresses": self.dns_entry.get(),
            "NetworkCategory": self.selected_network_category.get(),
        }

        summary = "Please confirm the VM creation with the following settings:\n\n"
        for key, value in vm_params.items():
            display_value = '******' if key == 'pass' and value else value
            summary += f"{key}: {display_value}\n"
        summary += "\nDo you want to proceed?"

        if not messagebox.askyesno("Confirm VM Creation", summary):
            print("VM creation canceled by user.")
            return

        ps_args = []
        for key, value in vm_params.items():
            ps_args.extend([f"-{key}", str(value)])

        script_path = construct_path(self.app.current_script_dir, self.app.script_dir_relative, r".\\Hyper-V-Automation\\create_Vm.ps1")
        run_ps1_script_2(script_path, ps_args=ps_args)
