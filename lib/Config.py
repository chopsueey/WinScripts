import json
import os
from .utils import resource_path

class Config:
    def __init__(self, filename="config.json"):
        self.config_path = resource_path(filename)
        self.config = self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                return json.load(f)
        else:
            return {"admin_rights_message_shown": False}

    def _save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    @property
    def admin_rights_message_shown(self):
        return self.config.get("admin_rights_message_shown", False)

    @admin_rights_message_shown.setter
    def admin_rights_message_shown(self, value):
        self.config["admin_rights_message_shown"] = value
        self._save_config()

    @property
    def theme(self):
        return self.config.get("theme", "light")

    @theme.setter
    def theme(self, value):
        self.config["theme"] = value
        self._save_config()
