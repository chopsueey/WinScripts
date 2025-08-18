import customtkinter
import platform, getpass, subprocess, os, psutil, time, datetime
from lib.utils import resource_path
from PIL import Image


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

class Statusbar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.system_info = SystemInfo()
        self.info_labels = {}
        self.nic_combobox = None

        self.grid_columnconfigure(0, weight=1) # Make the flow_frame expand

        self.flow_frame = customtkinter.CTkFrame(self)
        self.flow_frame.grid(row=0, column=0, sticky="ew")

        self.image_path = resource_path(r"./icons/refresh-ccw.png")
        self.refresh_image = customtkinter.CTkImage(light_image=Image.open(self.image_path), dark_image=Image.open(self.image_path), size=(20, 20))
        self.refresh_button = customtkinter.CTkButton(
            self, image=self.refresh_image, text="", command=self.update_status, width=20
        )
        self.refresh_button.grid(row=0, column=1, padx=5)

        # Theme toggle button
        self.light_icon = customtkinter.CTkImage(light_image=Image.open(resource_path(r"icons/sun.ico")),
                                     dark_image=Image.open(resource_path(r"icons/sun.ico")),
                                     size=(20, 20))
        self.dark_icon = customtkinter.CTkImage(light_image=Image.open(resource_path(r"icons/moon.ico")),
                                    dark_image=Image.open(resource_path(r"icons/moon.ico")),
                                    size=(20, 20))

        self.theme_button = customtkinter.CTkButton(
            self, text="", command=master.toggle_theme, width=20
        )
        self.theme_button.grid(row=0, column=2, padx=5)

        # Set initial icon based on theme
        if master.app_config.theme == "dark":
            self.theme_button.configure(image=self.light_icon)
        else:
            self.theme_button.configure(image=self.dark_icon)

        self._create_groups()
        self.update_status()

    def _create_groups(self):
        # System Group
        sys_group = customtkinter.CTkFrame(self.flow_frame)
        sys_group.pack(side="left", padx=5, pady=2, anchor="nw")
        customtkinter.CTkLabel(sys_group, text="System").pack()
        sys_keys = ["User", "RDP", "OS", "Uptime", "Type"]
        self._create_info_labels(sys_group, sys_keys)

        # Hardware Group
        hw_group = customtkinter.CTkFrame(self.flow_frame)
        hw_group.pack(side="left", padx=5, pady=2, anchor="nw")
        customtkinter.CTkLabel(hw_group, text="Hardware").pack()
        hw_keys = ["CPU", "Memory", "Disk"]
        self._create_info_labels(hw_group, hw_keys)

        # Network Group
        net_group = customtkinter.CTkFrame(self.flow_frame)
        net_group.pack(side="left", padx=5, pady=2, anchor="nw")
        customtkinter.CTkLabel(net_group, text="Network").pack()
        self.nic_combobox = customtkinter.CTkComboBox(net_group, state="readonly", width=300)
        self.nic_combobox.pack(padx=5, pady=5)

    def _create_info_labels(self, parent, keys):
        for key in keys:
            frame = customtkinter.CTkFrame(parent)
            frame.pack(side="top", anchor="w", padx=5, pady=2, fill="x")
            key_label = customtkinter.CTkLabel(frame, text=f"{key}:")
            key_label.pack(side="left")
            val_label = customtkinter.CTkLabel(frame, text="N/A", anchor="w")
            val_label.pack(side="left")
            self.info_labels[key] = val_label

    def update_status(self):
        # System Info
        sys_data = self.system_info.get_system_status()
        for key, value in sys_data.items():
            if key in self.info_labels:
                self.info_labels[key].configure(text=value)

        # Hardware Info
        hw_data = self.system_info.get_hardware_info()
        for key, value in hw_data.items():
            if key in self.info_labels:
                self.info_labels[key].configure(text=value)

        # Network Info
        nic_data = self.system_info.get_nic_info()
        if nic_data and "Error" not in nic_data:
            self.nic_combobox.configure(values=[f"{k}: {v}" for k, v in nic_data.items()])
            self.nic_combobox.set(next(iter(self.nic_combobox.cget("values"))))
        else:
            self.nic_combobox.configure(values=[])
            self.nic_combobox.set("No active NICs found")

        self.after(5000, self.update_status)

    def update_theme_icon(self):
        """Updates the theme toggle button icon."""
        if self.master.app_config.theme == "dark":
            self.theme_button.configure(image=self.light_icon)
        else:
            self.theme_button.configure(image=self.dark_icon)
