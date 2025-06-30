import tkinter as tk
from tkinter import ttk, filedialog
from lib.functions import run_ps1_script, run_ps1_script_elevated
import os, json


class CreateVMTab(tk.Frame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        # State

        self.app = app
        self.editions = []
        self.selected_edition = tk.StringVar(self)
        self.version_name = ""
        self.vm_switches = []
        self.selected_vm_switch = tk.StringVar(self)

        # Get ISOpath and get image names of that ISO
        self.iso_path = tk.StringVar(value="")

        self.iso_path_label = ttk.Label(self, textvariable=self.iso_path)
        self.iso_path_label.pack(pady=5)

        self.choose_iso = ttk.Button(
            self, text="Choose ISO", command=self.get_windows_image_editions
        )
        self.choose_iso.pack()

        self.edition_label = ttk.Label(self, text="Select Edition:")
        self.edition_label.pack(pady=5)

        self.edition_combobox = ttk.Combobox(
            self, textvariable=self.selected_edition, state="readonly"
        )
        self.edition_combobox.pack(pady=5)
        self.edition_combobox.set("Choose an iso first...")
        self.edition_combobox.bind("<<ComboboxSelected>>", self.on_edition_selected)

        self.edition_info_label = ttk.Label(self, text="No edition selected yet.")
        self.edition_info_label.pack(pady=10)

        # Get all current virtual switches in Hyper-V
        self.vm_switches_combobox = ttk.Combobox(
            self, textvariable=self.selected_vm_switch, state="readonly"
        )
        self.vm_switches_combobox.pack(pady=5)
        self.vm_switches_combobox.set("Choose a switch...")
        self.vm_switches_combobox.bind(
            "<<ComboboxSelected>>", self.on_vm_switch_selected
        )
        self.vm_switches_info_label = ttk.Label(self, text="No switch selected yet.")
        self.vm_switches_info_label.pack(pady=10)

        # Create VM
        self.create_vm_button = ttk.Button(
            self, text="Create VM", command=self.create_vm
        )
        self.create_vm_button.pack()

        # Simple example for LabelFrames and options (May add later)

        # options_frame = tk.LabelFrame(self, text="User Options", padx=10, pady=10)
        # options_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # # Add widgets inside the LabelFrame
        # tk.Checkbutton(options_frame, text="Enable Feature A").pack(anchor="w")
        # tk.Checkbutton(options_frame, text="Enable Feature B").pack(anchor="w")
        # tk.Entry(options_frame, width=30).pack(pady=5)

        # # --- Example 2: LabelFrame with a custom label position ---
        # settings_frame = tk.LabelFrame(
        #     self, text="Application Settings", padx=10, pady=10, labelanchor="n"
        # )  # "n" for North (top center)
        # settings_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # tk.Radiobutton(settings_frame, text="Option 1", value=1).pack(anchor="w")
        # tk.Radiobutton(settings_frame, text="Option 2", value=2).pack(anchor="w")

    # METHODS

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
        # Now we want to get them into here.
        # Python itself cannot access data from a powershell process with elevated rights (which is needed for above script).
        # Maybe all of this is not necessary if the app itself is run with admin rights from the beginning?

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

        # Get userinput for:
        # -MemoryStartupBytes 4GB `
        # -VMProcessorCount 2 `
        #     -VMName $vmName `
        # -pass
        # -VHDXSizeBytes 60GB `
        # -IPAddress 10.0.0.10 `
        # -PrefixLength 8 `
        # -DefaultGateway 10.0.0.10 `
        # -DnsAddresses '8.8.8.8', '8.8.4.4' `
        # -NetworkCategory 'Public', 'Private', 'Domain'?

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
