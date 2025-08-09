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


def StyledButton(master, **kwargs):
    """Creates a primary action button with the 'TButton' style."""
    return ttk.Button(master, style="TButton", **kwargs)

def StyledSecondaryButton(master, **kwargs):
    """Creates a secondary action button with the 'Secondary.TButton' style."""
    return ttk.Button(master, style="Secondary.TButton", **kwargs)

def StyledLabel(master, **kwargs):
    """Creates a standard body text label with the 'TLabel' style."""
    return ttk.Label(master, style="TLabel", **kwargs)

def StyledHeading(master, **kwargs):
    """Creates a heading label with the 'Heading.TLabel' style."""
    return ttk.Label(master, style="Heading.TLabel", **kwargs)

def StyledTitle(master, **kwargs):
    """Creates a title label with the 'Title.TLabel' style."""
    return ttk.Label(master, style="Title.TLabel", **kwargs)

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

def StyledCheckbutton(master, **kwargs):
    """Creates a checkbutton with the 'TCheckbutton' style."""
    return ttk.Checkbutton(master, style="TCheckbutton", **kwargs)

def StyledRadiobutton(master, **kwargs):
    """Creates a radiobutton with the 'TRadiobutton' style."""
    return ttk.Radiobutton(master, style="TRadiobutton", **kwargs)

def StyledProgressbar(master, **kwargs):
    """Creates a progressbar with the 'TProgressbar' style."""
    return ttk.Progressbar(master, style="TProgressbar", **kwargs)

def StyledLabelframe(master, **kwargs):
    """Creates a labelframe with the 'TLabelframe' style."""
    return ttk.Labelframe(master, style="TLabelframe", **kwargs)
