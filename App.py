import tkinter as tk
from tkinter import ttk
from style import init_style
from components.State import State
from lib.functions import center_window, run_ps1_cmd, run_ps1_script
import socket, platform, getpass, subprocess, os, sys, psutil, time, datetime


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
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

        # State
        self.script_dir_relative = "scripts"
        self.current_script_dir = os.path.dirname(os.path.abspath(__file__))

        init_style()

        # Menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # Statusbar
        self.status_bar = ttk.Frame(self, relief="groove", padding=4, border=4)
        self.status_bar.pack(fill="x", padx=4, pady=4)

        sys_info = self.get_system_status()
        for i, info in enumerate(sys_info):
            label = ttk.Label(self.status_bar, text=info, anchor="w")
            label.grid(row=0, column=i, padx=4, sticky="we")
            self.status_bar.columnconfigure(i, weight=1)

        nic_info = self.get_nic_info()
        for i, nic in enumerate(nic_info):
            label = ttk.Label(self.status_bar, text=nic, anchor="w")
            label.grid(row=1, column=i, padx=5, sticky="we")
            self.status_bar.columnconfigure(i, weight=1)

        # Notebook
        self.notebook = ttk.Notebook(self, name="test123", padding=4)
        self.notebook.pack(expand=True, fill="both")
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        # General Tab (Tab 0)
        self.general_tab = ttk.Frame(self.notebook)
        # self.general_tab_label = ttk.Label(
        #     self.general_tab, text="test-tab", anchor="center"
        # )
        # self.general_tab_label.pack(expand=True, fill="both")
        self.open_standard_pwsh = ttk.Button(
            self.general_tab,
            text="Open PowerShell",
            command=lambda: run_ps1_cmd("Start-Process powershell.exe -Verb RunAs"),
        )
        self.open_standard_pwsh.pack()
        self.open_new_pwsh = ttk.Button(
            self.general_tab,
            text="Open PowerShell 7",
            command=lambda: run_ps1_cmd("Start-Process pwsh.exe -Verb RunAs"),
        )
        self.open_new_pwsh.pack()
        self.RDP_button = ttk.Button(
            self.general_tab,
            text="Activate RDP",
            command=lambda: run_ps1_script(self._construct_path("activateRDP.ps1")),
        )
        self.RDP_button.pack()

        # Shell Tab (Tab 1)
        self.shell_tab = ttk.Frame(self.notebook)

        # Command input
        self.input_frame = ttk.Frame(self.shell_tab)
        self.input_frame.pack(fill="x", pady=4)
        self.input_frame.grid_rowconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=0)
        self.script_input = ttk.Entry(self.input_frame, font="18")
        self.script_input.grid(row=0, column=0, sticky="ew", padx=4)

        # Run Button
        self.run_script_button = ttk.Button(
            self.input_frame, text="Run", command=self.run_script_and_display_output
        )
        self.run_script_button.grid(row=0, column=1, padx=4)

        self.bind("<Return>", lambda e: self.run_script_and_display_output())

        # Output Text Widget with Scrollbar
        output_frame = ttk.Frame(self.shell_tab)
        output_frame.pack(expand=True, fill="both", padx=4)

        self.script_output_text = tk.Text(output_frame, wrap="word")
        self.script_output_text.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(
            output_frame, orient="vertical", command=self.script_output_text.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.script_output_text.config(yscrollcommand=scrollbar.set)

        # Other Tab (Tab 2)
        self.other_tab = ttk.Frame(self.notebook)

        # Another Tab (Tab 3)
        self.another_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.general_tab, text="General")
        self.notebook.add(self.other_tab, text="Stuff")
        self.notebook.add(self.another_tab, text="Advanced")
        self.notebook.add(self.shell_tab, text="QuickShell")

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

    def on_tab_change(self, event):
        selected_tab = event.widget.select()
        tab_index = event.widget.index(selected_tab)

        if tab_index == 0:
            print("0 tab")
            # self.get_system_status()
        elif tab_index == 1:
            print("1 tab opened")
        elif tab_index == 2:
            print("2 tab opened")
        elif tab_index == 3:
            print("3 tab opened")
            self.script_input.focus()

    def run_script_and_display_output(self):
        output = run_ps1_cmd(self.script_input.get())
        self.script_output_text.delete("1.0", tk.END)
        self.script_output_text.insert(tk.END, output)

    def get_system_status(self) -> list[str]:
        try:
            # hostname = socket.gethostname()
            user = getpass.getuser()
            os_version = platform.platform()

            # Get uptime (in seconds)
            uptime_seconds = time.time() - psutil.boot_time()
            uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))

            # Remote Desktop enabled?
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
            rdp_status = "RDP: Unknown"
            if "0x0" in result.stdout:
                rdp_status = "RDP: ON"
            elif "0x1" in result.stdout:
                rdp_status = "RDP: OFF"

            # Get domain/workgroup
            domain = os.environ.get("USERDOMAIN", "Unknown")

            return [
                f"Domain\\User: {domain}\\{user}",
                # f"Host: {hostname}",
                # f"Domain: {domain}",
                rdp_status,
                f"OS: {os_version}",
                f"Uptime: {uptime_str}",
            ]
        except Exception as e:
            return [f"Error: {e}"]

    def get_nic_info(self) -> list[str]:
        nic_data = []
        net_if_addrs = psutil.net_if_addrs()
        for nic, addrs in net_if_addrs.items():
            ipv4s = [a.address for a in addrs if a.family.name == "AF_INET"]
            if ipv4s:
                for ip in ipv4s:
                    nic_data.append(f"{nic}: {ip}")
        return nic_data

    def _construct_path(self, script_name: str) -> str:
        return os.path.join(
            self.current_script_dir, self.script_dir_relative, script_name
        )
    
    def bring_to_front(self):
        self.lift()
        self.attributes('-topmost', True)
        self.attributes('-topmost', False)
        self.focus_force() # Force keyboard focus to this window

    def run(self):
        self.update_idletasks()
        self.width = self.winfo_reqwidth()
        self.height = self.winfo_reqheight()

        center_window(self, self.width, self.height)
        self.after(100, self.bring_to_front)
        self.deiconify()
        self.mainloop()
