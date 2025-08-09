# lib/material_constants.py
"""
This file defines the constants for the Material Design theme.
It includes the color palette and font styles, based on the specifications
in UI_STYLE_GUIDE.md.
"""

# --- Material Design Color Palette (Light Theme) ---
# Based on Google's Material Design color system.
# Primary colors from the chat conversation and UI_STYLE_GUIDE.md.
LIGHT_PALETTE = {
    "primary": "#6200EE",
    "primary_variant": "#3700B3",  # A darker variant for hover/active states
    "secondary": "#03DAC6",
    "secondary_variant": "#018786", # A darker variant for hover/active states
    "background": "#e9ecef",       # Using the existing app's light background for consistency
    "surface": "#FFFFFF",          # White for component surfaces like cards and frames
    "error": "#B00020",
    "on_primary": "#FFFFFF",       # Text color on primary background
    "on_secondary": "#000000",     # Text color on secondary background
    "on_background": "#000000",    # Text color on main background
    "on_surface": "#000000",       # Text color on component surfaces
    "on_error": "#FFFFFF",         # Text color on error background
    "border": "#E0E0E0",           # A light grey for borders
}

# --- Typography ---
# Font family: Roboto is the standard for Material Design.
# The style_material.py file will handle fallbacks if Roboto is not available.
FONT_FAMILY = "Roboto"

TITLE_FONT = (FONT_FAMILY, 20, "bold")
HEADING_FONT = (FONT_FAMILY, 16, "bold")
BODY_FONT = (FONT_FAMILY, 12, "normal")
BUTTON_FONT = (FONT_FAMILY, 12, "bold")
