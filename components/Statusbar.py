import tkinter as tk
from tkinter import ttk
import platform, getpass, subprocess, os, psutil, time, datetime
from lib.utils import resource_path

class SystemInfo:
    """Gathers system and network information."""
    def __init__(self):
        # Initialize cpu_percent, the first call is non-blocking
        psutil.cpu_percent(interval=None)
        self.vm_flag = self.is_vm()

    def is_vm(self) -> bool:
        """Check if the system is a virtual machine."""
        try:
            result = subprocess.run(
                ["wmic", "computersystem", "get", "manufacturer,model"],
                capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW, check=True
            )
            output = result.stdout.lower()
            vm_keywords = ["vmware", "virtual", "xen", "hyper-v", "oracle", "qemu", "kvm", "microsoft corporation"]
            for keyword in vm_keywords:
                if keyword in output and "virtual machine" in output:
                    return True
            return False
        except (FileNotFoundError, subprocess.CalledProcessError): # wmic not on PATH or command fails
            return False # Cannot determine
        except Exception:
            return False

    def get_hardware_info(self) -> dict[str, str]:
        """Returns a dictionary of hardware information."""
        try:
            cpu_usage = psutil.cpu_percent(interval=None)
            memory_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage(os.path.abspath(os.sep))

            return {
                "CPU": f"{cpu_usage:.1f}%",
                "Memory": f"{memory_info.percent}%",
                "Disk": f"{disk_info.percent}%",
            }
        except Exception as e:
            return {"CPU": "N/A", "Memory": "N/A", "Disk": "N/A", "Error": str(e)}

    def get_system_status(self) -> dict[str, str]:
        """Returns a dictionary of system information."""
        try:
            user = getpass.getuser()
            os_version = platform.platform()
            uptime_seconds = time.time() - psutil.boot_time()
            uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))
            domain = os.environ.get("USERDOMAIN", "Unknown")

            # RDP Status
            rdp_status = "Unknown"
            try:
                result = subprocess.run(
                    [
                        "reg", "query",
                        r"HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server",
                        "/v", "fDenyTSConnections",
                    ],
                    capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
                )
                if "0x0" in result.stdout:
                    rdp_status = "ON"
                elif "0x1" in result.stdout:
                    rdp_status = "OFF"
            except FileNotFoundError: # reg.exe not on PATH
                rdp_status = "N/A"

            system_type = "VM" if self.vm_flag else "Physical"

            return {
                "User": f"{domain}\\{user}",
                "RDP": rdp_status,
                "OS": os_version,
                "Uptime": uptime_str,
                "Type": system_type,
            }
        except Exception as e:
            return {"Error": str(e)}

    def get_nic_info(self) -> dict[str, str]:
        """Returns a dictionary of NICs and their IPv4 addresses."""
        nic_data = {}
        try:
            net_if_addrs = psutil.net_if_addrs()
            for nic, addrs in net_if_addrs.items():
                for addr in addrs:
                    if addr.family.name == "AF_INET":
                        nic_data[nic] = addr.address
                        break # Take the first IPv4 address
        except Exception as e:
            return {"Error": str(e)}
        return nic_data

class FlowFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Configure>", self._on_configure)

    def _on_configure(self, event):
        self.repack()

    def repack(self):
        for widget in self.winfo_children():
            widget.place_forget()

        x = 0
        y = 0
        row_height = 0
        available_width = self.winfo_width()

        for widget in self.winfo_children():
            widget.update_idletasks()
            width = widget.winfo_reqwidth()
            height = widget.winfo_reqheight()

            if x + width > available_width:
                x = 0
                y += row_height
                row_height = 0

            widget.place(x=x, y=y)

            x += width
            if height > row_height:
                row_height = height

class Statusbar(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.system_info = SystemInfo()
        self.info_labels = {}
        self.nic_combobox = None

        self.flow_frame = FlowFrame(self)
        self.flow_frame.pack(side="left", fill="both", expand=True, padx=5, pady=2)

        self.image_path = resource_path(r"./icons/refresh-ccw.png")
        self.refresh_image = tk.PhotoImage(file=self.image_path)
        self.refresh_button = ttk.Button(
            self, image=self.refresh_image, command=self.update_status
        )
        self.refresh_button.pack(side="right", anchor="e", padx=5)

        self.theme_button = ttk.Button(
            self, text="Toggle Theme", command=master.toggle_theme
        )
        self.theme_button.pack(side="right", anchor="e", padx=5)

        self._create_groups()
        self.update_status()

    def _create_groups(self):
        # System Group
        sys_group = ttk.Labelframe(self.flow_frame, text="System")
        sys_group.pack(side="left", padx=5, pady=2, anchor="nw")
        sys_keys = ["User", "RDP", "OS", "Uptime", "Type"]
        self._create_info_labels(sys_group, sys_keys)

        # Hardware Group
        hw_group = ttk.Labelframe(self.flow_frame, text="Hardware")
        hw_group.pack(side="left", padx=5, pady=2, anchor="nw")
        hw_keys = ["CPU", "Memory", "Disk"]
        self._create_info_labels(hw_group, hw_keys)

        # Network Group
        net_group = ttk.Labelframe(self.flow_frame, text="Network")
        net_group.pack(side="left", padx=5, pady=2, anchor="nw")
        self.nic_combobox = ttk.Combobox(net_group, state="readonly", width=30)
        self.nic_combobox.pack(padx=5, pady=5)

    def _create_info_labels(self, parent, keys):
        for key in keys:
            frame = ttk.Frame(parent)
            frame.pack(side="top", anchor="w", padx=5, pady=2)
            key_label = ttk.Label(frame, text=f"{key}:")
            key_label.pack(side="left")
            val_label = ttk.Label(frame, text="N/A", anchor="w")
            val_label.pack(side="left")
            self.info_labels[key] = val_label

    def update_status(self):
        # System Info
        sys_data = self.system_info.get_system_status()
        for key, value in sys_data.items():
            if key in self.info_labels:
                self.info_labels[key].config(text=value)

        # Hardware Info
        hw_data = self.system_info.get_hardware_info()
        for key, value in hw_data.items():
            if key in self.info_labels:
                self.info_labels[key].config(text=value)

        # Network Info
        nic_data = self.system_info.get_nic_info()
        if nic_data and "Error" not in nic_data:
            self.nic_combobox['values'] = [f"{k}: {v}" for k, v in nic_data.items()]
            self.nic_combobox.set(next(iter(self.nic_combobox['values'])))
        else:
            self.nic_combobox['values'] = []
            self.nic_combobox.set("No active NICs found")

        self.after(5000, self.update_status)
