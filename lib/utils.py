import os
import sys


# construct_path is for getting the right path for the specified scriptname in ./scripts
def construct_path(current_script_dir: str, script_dir_relative: str, script_name: str) -> str:
    return os.path.join(
        current_script_dir, script_dir_relative, script_name
    )

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
