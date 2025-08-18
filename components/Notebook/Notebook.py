import customtkinter
from lib.functions import run_ps1_cmd
from .GeneralTab import GeneralTab
from .AdvancedTab import AdvancedTab
from .ADTab import ADTab
from .QuickShellTab import QuickShellTab
from .CreateVMTab import CreateVMTab
from .AzureTab import AzureTab


class Notebook(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # self.bind("<<NotebookTabChanged>>", self._on_tab_change) # CTkTabView does not have this event

        # Add tabs
        self.add("General")
        self.add("Advanced")
        self.add("Active Directory")
        self.add("Create VM")
        self.add("Azure")
        self.add("QuickShell")

        # Create tab content
        self.general_tab = GeneralTab(self.tab("General"), app=master)
        self.advanced_tab = AdvancedTab(self.tab("Advanced"), app=master)
        self.active_directory_tab = ADTab(self.tab("Active Directory"), app=master)
        self.create_vm_tab = CreateVMTab(self.tab("Create VM"), app=master)
        self.azure_tab = AzureTab(self.tab("Azure"), app=master)
        self.quick_shell = QuickShellTab(self.tab("QuickShell"), app=master)

    def _on_tab_change(self, event):
        # selected_tab = event.widget.select()
        # tab_index = event.widget.index(selected_tab)
        # if tab_index == 5:
        #     self.quick_shell.script_input.focus()
        pass