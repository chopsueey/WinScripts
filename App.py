import tkinter as tk
from tkinter import ttk
from style import init_style
from components.State import State
from lib.functions import center_window, run_ps1_script
import socket, platform, getpass, subprocess, os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.withdraw()

        self.master = master
        self.title("App")
        icon_path = resource_path("favicon.ico")
        self.iconbitmap(icon_path)
        # self.iconbitmap(r"./favicon.ico")

        init_style()

        # Menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # Statusbar
        self.status_bar = ttk.Label(
            self, text="Loading system info...", anchor="w", relief="sunken"
        )
        self.status_bar.pack(fill="x", side="top")

        # Notebook
        notebook = ttk.Notebook(self, name="test123")
        notebook.pack(expand=True, fill="both")

        # Shell Tab (Tab 1)
        shell_tab = ttk.Frame(notebook)

        # Test Tab (Tab 2)
        test_tab = ttk.Frame(notebook)
        test_tab_label = ttk.Label(test_tab, text="test-tab")
        test_tab_label.pack(expand=True, fill="both")

        # Command entry
        input_frame = ttk.Frame(shell_tab)
        input_frame.pack(expand=True, fill="both")
        self.script_input = ttk.Entry(input_frame)
        self.script_input.pack(expand=True, fill="x")
        self.script_input.focus()

        # Output Text Widget with Scrollbar
        output_frame = ttk.Frame(shell_tab)
        output_frame.pack(expand=True, fill="both")

        self.script_output_text = tk.Text(output_frame, wrap="word")
        self.script_output_text.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(
            output_frame, orient="vertical", command=self.script_output_text.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.script_output_text.config(yscrollcommand=scrollbar.set)

        # PowerShell Button
        self.run_script_button = ttk.Button(
            shell_tab, text="Run", command=self.run_script_and_display_output
        )
        self.run_script_button.pack()

        self.bind("<Return>", lambda e: self.run_script_and_display_output())

        notebook.add(shell_tab, text="shelltab")
        notebook.add(test_tab, text="test-tab")

        self.status_bar.config(text=self.get_system_status())

    def run_script_and_display_output(self):
        output = run_ps1_script(self.script_input.get())
        self.script_output_text.delete("1.0", tk.END)
        self.script_output_text.insert(tk.END, output)

    def get_system_status(self) -> str:
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            user = getpass.getuser()
            os_version = platform.platform()

            # Check if Remote Desktop is enabled via registry (for example)
            result = subprocess.run(
                [
                    "reg",
                    "query",
                    r"HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server",
                    "/v",
                    "fDenyTSConnections",
                ],
                capture_output=True,
                text=True,
            )

            if "0x0" in result.stdout:
                rdp_status = "Remote Desktop: ON"
            elif "0x1" in result.stdout:
                rdp_status = "Remote Desktop: OFF"
            else:
                rdp_status = "Remote Desktop: Unknown"

            return f"{user}@{hostname} | IP: {ip} | {rdp_status} | {os_version}"
        except Exception as e:
            return f"Error: {e}"

    def run(self):
        self.update_idletasks()
        self.width = self.winfo_reqwidth()
        self.height = self.winfo_reqheight()

        center_window(self, self.width, self.height)

        self.deiconify()
        self.mainloop()
