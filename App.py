import customtkinter
from tkinter import messagebox
from style import init_style
from components import Menubar, Statusbar, Notebook
from lib.functions import center_window
from lib.utils import resource_path
from lib.Config import Config
import os, sys

class App(customtkinter.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        # Config
        self.app_config = Config()

        # Set appearance
        customtkinter.set_appearance_mode(self.app_config.theme)
        customtkinter.set_default_color_theme("blue")

        if not self.app_config.admin_rights_message_shown:
            messagebox.showinfo(
                "Admin Rights",
                "For most scripts, you need to run this app as an administrator.",
            )
            self.app_config.admin_rights_message_shown = True

        self.master = master
        self.title("App")
        icon_path = resource_path("favicon.ico")
        # self.iconbitmap(icon_path) # customtkinter does not support .ico files on linux

        # State
        self.script_dir_relative = "scripts"
        self.current_script_dir = os.path.dirname(os.path.abspath(__file__))

        # init_style(self.app_config.theme)

        # Menubar
        self.menubar = Menubar(self)
        # self.config(menu=self.menubar) # CTk does not have a config method

        # Statusbar
        self.status_bar = Statusbar(self)
        self.status_bar.pack(fill="both", expand=True, padx=4, pady=4)

        # Notebook
        self.notebook = Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=4, pady=4)

    # METHODS
    def get_root_path(self):
        path_to_main = os.path.abspath(sys.modules["__main__"].__file__)
        root_dir = os.path.dirname(path_to_main)
        return root_dir

    def toggle_theme(self):
        if self.app_config.theme == "dark":
            self.app_config.theme = "light"
        else:
            self.app_config.theme = "dark"

        customtkinter.set_appearance_mode(self.app_config.theme)

    def restart(self):
        """Restarts the application."""
        self.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def _bring_to_front(self):
        self.lift()
        self.attributes("-topmost", True)
        self.attributes("-topmost", False)
        self.focus_force()  # Force keyboard focus to this window

    def run(self):
        self.update_idletasks()

        # Calculate the required size based on the largest tab
        tabs = self.notebook.get_all_tabs()
        max_width = 0
        max_height = 0
        for tab in tabs:
            max_width = max(max_width, tab.winfo_reqwidth())
            max_height = max(max_height, tab.winfo_reqheight())

        # Add padding and the height of other components
        # Get the height of the notebook's tab bar
        notebook_req_height = self.notebook.winfo_reqheight()
        children = self.notebook.winfo_children()
        if children:
            first_child_height = children[0].winfo_reqheight()
            notebook_tab_bar_height = notebook_req_height - first_child_height
        else:
            notebook_tab_bar_height = 0 # Fallback

        statusbar_height = self.status_bar.winfo_reqheight()

        # Total padding: 4px top, 4px between notebook and statusbar, 4px bottom
        vertical_padding = 4 + 4 + 4
        # Total padding: 4px left, 4px right
        horizontal_padding = 4 + 4

        width = max_width + horizontal_padding
        height = max_height + notebook_tab_bar_height + statusbar_height + vertical_padding

        self.width = width
        self.height = height

        center_window(self, self.width, self.height)
        self.after(100, self._bring_to_front)
        self.mainloop()
