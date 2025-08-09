# lib/ui_helpers.py
"""
This file provides helper functions for creating styled Tkinter widgets
that conform to the application's Material Design style guide.

Using these helpers ensures consistency and simplifies UI code. Each function
wraps a standard ttk widget and applies the appropriate style from the
style_material.py theme.
"""

import tkinter as tk
from tkinter import ttk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Draw a rounded rectangle on a canvas."""
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

class RoundedButton(tk.Canvas):
    def __init__(self, master=None, text="", radius=25, btn_fg="#000000", btn_bg="#ffffff", cmd=None, **kwargs):
        super().__init__(master, relief="flat", highlightthickness=0, **kwargs)
        self.radius = radius
        self.btn_fg = btn_fg
        self.btn_bg = btn_bg
        self.command = cmd

        self.bind("<Configure>", self._draw)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

        self.text_id = self.create_text(0, 0, text=text, fill=btn_fg, font=("Segoe UI", 12, "bold"))

    def _draw(self, event=None):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()

        create_rounded_rectangle(self, 0, 0, width, height, self.radius, fill=self.btn_bg, outline="")

        # Center the text
        bbox = self.bbox(self.text_id)
        x_center = (width - (bbox[2] - bbox[0])) / 2
        y_center = (height - (bbox[3] - bbox[1])) / 2
        self.coords(self.text_id, x_center, y_center)
        self.itemconfig(self.text_id, text=self.itemcget(self.text_id, "text"))

    def _on_press(self, event=None):
        if self.command:
            self.command()

    def _on_release(self, event=None):
        pass

def StyledButton(master, text, **kwargs):
    """Creates a primary action button with a rounded shape."""
    # This is a temporary implementation.
    # In a real scenario, we would get the colors from the theme.
    return RoundedButton(master, text=text, btn_bg="#5E81AC", btn_fg="#FFFFFF", **kwargs)

def StyledSecondaryButton(master, text, **kwargs):
    """Creates a secondary action button with the 'Secondary.TButton' style."""
    return ttk.Button(master, text=text, style="Secondary.TButton", **kwargs)

def StyledLabel(master, text, **kwargs):
    """Creates a standard body text label with the 'TLabel' style."""
    return ttk.Label(master, text=text, style="TLabel", **kwargs)

def StyledHeading(master, text, **kwargs):
    """Creates a heading label with the 'Heading.TLabel' style."""
    return ttk.Label(master, text=text, style="Heading.TLabel", **kwargs)

def StyledTitle(master, text, **kwargs):
    """Creates a title label with the 'Title.TLabel' style."""
    return ttk.Label(master, text=text, style="Title.TLabel", **kwargs)

def StyledEntry(master, **kwargs):
    """Creates an entry widget with the 'TEntry' style."""
    return ttk.Entry(master, style="TEntry", **kwargs)

def StyledCombobox(master, **kwargs):
    """Creates a combobox widget with the 'TCombobox' style."""
    return ttk.Combobox(master, style="TCombobox", **kwargs)

def StyledFrame(master, **kwargs):
    """Creates a standard frame with the 'TFrame' style."""
    return ttk.Frame(master, style="TFrame", **kwargs)

def StyledCard(master, **kwargs):
    """Creates a card-like frame with the 'Card.TFrame' style."""
    return ttk.Frame(master, style="Card.TFrame", **kwargs)

def StyledCheckbutton(master, text, **kwargs):
    """Creates a checkbutton with the 'TCheckbutton' style."""
    return ttk.Checkbutton(master, text=text, style="TCheckbutton", **kwargs)

def StyledRadiobutton(master, text, **kwargs):
    """Creates a radiobutton with the 'TRadiobutton' style."""
    return ttk.Radiobutton(master, text=text, style="TRadiobutton", **kwargs)

def StyledProgressbar(master, **kwargs):
    """Creates a progressbar with the 'TProgressbar' style."""
    return ttk.Progressbar(master, style="TProgressbar", **kwargs)

def StyledLabelframe(master, text, **kwargs):
    """Creates a labelframe with the 'TLabelframe' style."""
    return ttk.Labelframe(master, text=text, style="TLabelframe", **kwargs)
