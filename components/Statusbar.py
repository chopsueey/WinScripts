import tkinter as tk
from tkinter import ttk
import platform, getpass, subprocess, os, psutil, time, datetime



class Statusbar(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._create_labels()
        self.image_path = master.resource_path(r"./icons/refresh-ccw.png")
        self.refresh_image = tk.PhotoImage(file=self.image_path)
        self.refresh_button = ttk.Button(self, image=self.refresh_image, command=self._create_labels)
        self.refresh_button.configure(padding=2)
        self.refresh_button.grid(row=1, column=4)

    def _create_labels(self):
        self.sys_info = self._get_system_status()
        for i, info in enumerate(self.sys_info):
            label = ttk.Label(self, text=info, anchor="w")
            label.grid(row=0, column=i, padx=4, sticky="we")
            self.columnconfigure(i, weight=1)

        self.nic_info = self._get_nic_info()
        for i, nic in enumerate(self.nic_info):
            label = ttk.Label(self, text=nic, anchor="w")
            label.grid(row=1, column=i, padx=5, sticky="we")
            self.columnconfigure(i, weight=1)

    def _get_system_status(self) -> list[str]:
        try:
            # hostname = socket.gethostname()
            user = getpass.getuser()
            os_version = platform.platform()

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
                creationflags=subprocess.CREATE_NO_WINDOW,
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

    def _get_nic_info(self) -> list[str]:
        nic_data = []
        net_if_addrs = psutil.net_if_addrs()
        for nic, addrs in net_if_addrs.items():
            ipv4s = [a.address for a in addrs if a.family.name == "AF_INET"]
            if ipv4s:
                for ip in ipv4s:
                    nic_data.append(f"{nic}: {ip}")
        return nic_data