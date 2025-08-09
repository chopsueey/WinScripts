# lib/material_constants.py
"""
This file defines the constants for the Material Design theme.
It includes the color palette and font styles, based on the specifications
in UI_STYLE_GUIDE.md.
"""

# --- Material Design Color Palette (Light Theme) ---
# Based on a modern, minimal aesthetic inspired by the Nord palette.
LIGHT_PALETTE = {
    "primary": "#5E81AC",
    "primary_variant": "#4C6A8D",
    "secondary": "#88C0D0",
    "secondary_variant": "#79A8B8",
    "background": "#ECEFF4",
    "surface": "#FFFFFF",
    "error": "#BF616A",
    "on_primary": "#FFFFFF",
    "on_secondary": "#2E3440",
    "on_background": "#2E3440",
    "on_surface": "#2E3440",
    "on_error": "#FFFFFF",
    "border": "#D8DEE9",
}

# --- Typography ---
# Font family: Roboto is the standard for Material Design.
# The style_material.py file will handle fallbacks if Roboto is not available.
FONT_FAMILY = "Roboto"

TITLE_FONT = (FONT_FAMILY, 20, "bold")
HEADING_FONT = (FONT_FAMILY, 16, "bold")
BODY_FONT = (FONT_FAMILY, 12, "normal")
BUTTON_FONT = (FONT_FAMILY, 12, "bold")
