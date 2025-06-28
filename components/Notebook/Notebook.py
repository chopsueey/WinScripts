import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd, run_ps1_script
from .GeneralTab import GeneralTab
from .AdvancedTab import AdvancedTab
from .QuickShellTab import QuickShellTab
from .CreateVMTab import CreateVMTab


class Notebook(ttk.Notebook):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.bind("<<NotebookTabChanged>>", self._on_tab_change)

        # Tab 0
        self.general_tab = GeneralTab(self, app=master)

        # Tab 1
        self.advanced_tab = AdvancedTab(self, app=master)

        # Tab 2
        self.create_vm_tab = CreateVMTab(self, app=master)

        # Tab 3
        self.quick_shell = QuickShellTab(self, app=master)

        self.add(self.general_tab, text="General")
        self.add(self.advanced_tab, text="Advanced")
        self.add(self.create_vm_tab, text="Create VM")
        self.add(self.quick_shell, text="QuickShell")

        # Template for getting user input for script parameters

        # ttk.Label(main_frame, text="Target Computer:").pack(anchor="w", padx=(0, 5))
        # self.target_computer_entry = ttk.Entry(main_frame, width=40)
        # self.target_computer_entry.pack(fill="x", pady=2)
        # self.target_computer_entry.insert(0, "localhost") # Default value

        # # Port
        # ttk.Label(main_frame, text="Port (e.g., 3389):").pack(anchor="w", padx=(0, 5))
        # self.port_entry = ttk.Entry(main_frame, width=40)
        # self.port_entry.pack(fill="x", pady=2)
        # self.port_entry.insert(0, "3389") # Default value

        # # Force Switch
        # self.force_var = tk.BooleanVar()
        # self.force_checkbox = ttk.Checkbutton(main_frame, text="Force Operation", variable=self.force_var)
        # self.force_checkbox.pack(anchor="w", pady=5)

        # target_computer = self.target_computer_entry.get()
        # port_str = self.port_entry.get()

        # ps_arguments = [
        #         "-TargetComputer", target_computer,
        #         "-Port", str(port)
        #     ]
        # if force_switch:
        #     ps_arguments.append("-Force") # Add switch parameter if checked

        # run_ps1_script(script_full_path, ps_args=ps_arguments)

    def _on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_index = event.widget.index(selected_tab)

        if tab_index == 0:
            print("0 tab")
        elif tab_index == 1:
            print("1 tab opened")
        elif tab_index == 2:
            print("2 tab opened")
            self.quick_shell.script_input.focus()
        elif tab_index == 3:
            print("3 tab opened")
