# lib/ui_helpers.py
"""
This file provides helper functions for creating styled Tkinter widgets.
When a ttktheme is active, these helpers ensure that standard widgets
are used, allowing the theme to control their appearance.
"""

import tkinter as tk
from tkinter import ttk


def StyledButton(master, **kwargs):
    """Creates a primary action button."""
    return ttk.Button(master, **kwargs)

def StyledSecondaryButton(master, **kwargs):
    """Creates a secondary action button."""
    return ttk.Button(master, **kwargs)

def StyledLabel(master, **kwargs):
    """Creates a standard body text label."""
    return ttk.Label(master, **kwargs)

def StyledHeading(master, **kwargs):
    """Creates a heading label."""
    # The theme will handle heading styles, but we can add a font increase as a basic default
    # Note: This might be overridden by the theme.
    kwargs.setdefault('font', ('Segoe UI', 12, 'bold'))
    return ttk.Label(master, **kwargs)

def StyledTitle(master, **kwargs):
    """Creates a title label."""
    kwargs.setdefault('font', ('Segoe UI', 16, 'bold'))
    return ttk.Label(master, **kwargs)

def StyledEntry(master, **kwargs):
    """Creates an entry widget."""
    return ttk.Entry(master, **kwargs)

def StyledCombobox(master, **kwargs):
    """Creates a combobox widget."""
    return ttk.Combobox(master, **kwargs)

def StyledFrame(master, **kwargs):
    """Creates a standard frame."""
    return ttk.Frame(master, **kwargs)

def StyledCard(master, **kwargs):
    """Creates a card-like frame. The theme will determine the appearance."""
    # We can add a border to simulate a card if the theme doesn't provide one
    kwargs.setdefault('borderwidth', 1)
    kwargs.setdefault('relief', 'solid')
    return ttk.Frame(master, **kwargs)

def StyledCheckbutton(master, **kwargs):
    """Creates a checkbutton."""
    return ttk.Checkbutton(master, **kwargs)

def StyledRadiobutton(master, **kwargs):
    """Creates a radiobutton."""
    return ttk.Radiobutton(master, **kwargs)

def StyledProgressbar(master, **kwargs):
    """Creates a progressbar."""
    return ttk.Progressbar(master, **kwargs)

def StyledLabelframe(master, **kwargs):
    """Creates a labelframe."""
    return ttk.Labelframe(master, **kwargs)
