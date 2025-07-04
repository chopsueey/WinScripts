import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd
from .GeneralTab import GeneralTab
from .AdvancedTab import AdvancedTab
from .ADTab import ADTab
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
        self.active_directory_tab = ADTab(self, app=master)

        # Tab 3
        self.create_vm_tab = CreateVMTab(self, app=master)

        # Tab 4
        self.quick_shell = QuickShellTab(self, app=master)

        self.add(self.general_tab, text="General")
        self.add(self.advanced_tab, text="Advanced")
        self.add(self.active_directory_tab, text="Active Directory")
        self.add(self.create_vm_tab, text="Create VM")
        self.add(self.quick_shell, text="QuickShell")

    def _on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_index = event.widget.index(selected_tab)

        if tab_index == 0:
            print("0 tab")
        elif tab_index == 1:
            print("1 tab opened")
        elif tab_index == 2:
            print("2 tab opened")
        elif tab_index == 3:
            print("3 tab opened")
        elif tab_index == 4:
            print("4 tab opened")
            self.quick_shell.script_input.focus()
        elif tab_index == 5:
            print("5 tab opened")