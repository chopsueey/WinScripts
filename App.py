import tkinter as tk
from style import init_style
from components import Menubar, Statusbar, Notebook
from lib.functions import center_window
from lib.utils import resource_path
import os, sys


class App(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.withdraw()

        self.master = master
        self.title("App")
        icon_path = resource_path("favicon.ico")
        self.iconbitmap(icon_path)
        # self.iconbitmap(r"./favicon.ico")

        # State
        self.script_dir_relative = "scripts"
        self.current_script_dir = os.path.dirname(os.path.abspath(__file__))

        init_style()

        # Menubar
        self.menubar = Menubar(self)
        self.config(menu=self.menubar)

        # Statusbar
        self.status_bar = Statusbar(self, relief="groove", padding=4, border=4)
        self.status_bar.pack(fill="x", padx=4, pady=4)

        # Notebook
        self.notebook = Notebook(self, name="test123", padding=4)
        self.notebook.pack(expand=True, fill="both")

    # METHODS
    def get_root_path(self):
        path_to_main = os.path.abspath(sys.modules["__main__"].__file__)
        root_dir = os.path.dirname(path_to_main)
        return root_dir

    def _bring_to_front(self):
        self.lift()
        self.attributes("-topmost", True)
        self.attributes("-topmost", False)
        self.focus_force()  # Force keyboard focus to this window

    def run(self):
        self.update_idletasks()
        self.width = self.winfo_reqwidth()
        self.height = self.winfo_reqheight()

        center_window(self, self.width, self.height)
        self.after(100, self._bring_to_front)
        self.deiconify()
        self.mainloop()
