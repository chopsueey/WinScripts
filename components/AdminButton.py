import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class AdminButton(ttk.Button):
    _shield_icon = None

    def __init__(self, master, text, command, **kwargs):
        if AdminButton._shield_icon is None:
            try:
                # Construct the path to the icon
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                icon_path = os.path.join(base_dir, "icons", "shield.png")

                # Open the image and resize it
                img = Image.open(icon_path)
                img = img.resize((16, 16), Image.Resampling.LANCZOS)
                AdminButton._shield_icon = ImageTk.PhotoImage(img)
            except FileNotFoundError:
                # If the icon is not found, create a placeholder
                # This helps in development even without the actual icon
                placeholder = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
                AdminButton._shield_icon = ImageTk.PhotoImage(placeholder)
            except Exception as e:
                print(f"Error loading shield icon: {e}")
                AdminButton._shield_icon = None # Fallback to no icon

        super().__init__(
            master,
            text=text,
            command=command,
            image=AdminButton._shield_icon,
            compound=tk.LEFT,
            style="TButton",
            **kwargs
        )
