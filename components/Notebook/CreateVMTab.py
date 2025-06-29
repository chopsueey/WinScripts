import tkinter as tk
from tkinter import ttk, filedialog
from lib.functions import run_ps1_script
import os, json


class CreateVMTab(tk.Frame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.editions = []
        self.iso_path = tk.StringVar(value="")

        self.iso_path_label = ttk.Label(self, textvariable=self.iso_path)
        self.iso_path_label.pack(pady=5)

        self.choose_iso = ttk.Button(
            self, text="Choose ISO", command=self.get_windows_image_editions
        )
        self.choose_iso.pack()

        self.edition_label = ttk.Label(self, text="Select Edition:")
        self.edition_label.pack(pady=5)

        self.selected_edition = tk.StringVar(self)
        self.edition_combobox = ttk.Combobox(
            self, textvariable=self.selected_edition, state="readonly"
        )
        self.edition_combobox.pack(pady=5)
        self.edition_combobox.set("Choose an iso first...")
        self.edition_combobox.bind("<<ComboboxSelected>>", self.on_edition_selected)

        self.info_label = ttk.Label(self, text="")
        self.info_label.pack(pady=10)

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

    def get_windows_image_editions(self):
        isopath = filedialog.askopenfilename()
        self.iso_path.set(isopath)

        run_ps1_script(
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

            self.info_label.config(text=f"Loaded {len(self.editions)} editions.")
        else:
            self.edition_combobox["values"] = []
            self.edition_combobox.set("No editions found.")
            self.info_label.config(text="No editions found or an error occurred.")

    def on_edition_selected(self, event):
        selected = self.selected_edition.get()
        self.info_label.config(text=f"You selected: {selected}")
        print(f"Selected edition: {selected}")

    def create_vm(self):
        print(self.app.construct_path(r".\\Hyper-V-Automation\\create_Vm.ps1"))
        run_ps1_script(
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
                "-script_path",
                f"{self.app.construct_path(r'.\\Hyper-V-Automation\\')}",
            ],
        )
