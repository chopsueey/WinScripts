from tkinter import ttk
import tkinter as tk

# --- Define a Modern Dark Mode Color Palette ---
# Based on a modern, minimal aesthetic inspired by the Nord palette.
DARK_PALETTE = {
    "primary": "#81A1C1",
    "primary_variant": "#8FBCBB",
    "secondary": "#88C0D0",
    "secondary_variant": "#A3BE8C",
    "background": "#2E3440",
    "surface": "#3B4252",
    "error": "#BF616A",
    "on_primary": "#2E3440",
    "on_secondary": "#2E3440",
    "on_background": "#E5E9F0",
    "on_surface": "#E5E9F0",
    "on_error": "#2E3440",
    "border": "#4C566A",
}
# For compatibility with existing style definitions that might use these.
# This can be removed after a full refactor.
PALETTE = DARK_PALETTE


# --- Styling Function ---
def init_style():
    """Initializes and configures modern-looking ttk.Style for dark mode widgets."""
    style = ttk.Style()

    # 'clam' is still a good base for custom modern styles as it's quite neutral.
    # We will override most of its default colors.
    style.theme_use("clam")

    # --- General Font Configuration ---
    base_font = ("Segoe UI", 10)
    heading_font = ("Segoe UI", 12, "bold")
    large_font = ("Segoe UI", 12)

    # --- TFrame Style ---
    style.configure(
        "TFrame",
        background=PALETTE["background"],
        relief="flat",
        borderwidth=0,
        padding=10,
    )
    # A specific style for panels or cards
    style.configure(
        "Card.TFrame",
        background=PALETTE["surface"],
        relief="flat",
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=15,
    )

    # --- TLabel Style ---
    style.configure(
        "TLabel",
        font=base_font,
        foreground=PALETTE["on_background"],
        background=PALETTE["background"],
        relief="flat",
    )
    # Heading Label
    style.configure(
        "Heading.TLabel",
        font=heading_font,
        foreground=PALETTE["on_background"],
        background=PALETTE["background"],
    )
    # Accent Label (e.g., for disabled text or secondary info)
    style.configure(
        "Accent.TLabel",
        font=base_font,
        foreground=PALETTE["secondary"],  # Using secondary for subtle text
        background=PALETTE["background"],
    )

    # --- TButton Style (Modern Flat) ---
    # Default Button (primary action)
    style.configure(
        "TButton",  # Default TButton style
        font=large_font,
        foreground=PALETTE["on_primary"],
        background=PALETTE["primary"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],
    )
    style.map(
        "TButton",
        background=[
            ("active", PALETTE["primary_variant"]),
            ("pressed", PALETTE["primary_variant"]),
        ],
        foreground=[("active", PALETTE["on_primary"])],
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )

    # Secondary Button
    style.configure(
        "Secondary.TButton",
        font=large_font,
        foreground=PALETTE["on_secondary"],
        background=PALETTE["secondary"],
        relief="solid",
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[15, 8],
    )
    style.map(
        "Secondary.TButton",
        background=[
            ("active", PALETTE["secondary_variant"]),  # Darker accent on hover
            ("pressed", PALETTE["secondary_variant"]),
        ],
        foreground=[("active", PALETTE["on_secondary"])],
        relief=[("pressed", "solid"), ("!pressed", "solid")],
        bordercolor=[("active", PALETTE["primary"])],
    )

    # Danger Button
    style.configure(
        "Danger.TButton",
        font=large_font,
        foreground=PALETTE["on_error"],
        background=PALETTE["error"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],
    )
    style.map(
        "Danger.TButton",
        background=[
            ("active", "#cc7a73"),  # Slightly darker red on hover
            ("pressed", "#bf6b62"),
        ],
        foreground=[("active", PALETTE["on_error"])],
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )

    # --- TEntry Style (Modern Input Field) ---
    style.configure(
        "TEntry",
        font=base_font,
        fieldbackground=PALETTE["surface"],
        foreground=PALETTE["on_surface"],
        insertcolor=PALETTE["primary"],
        relief="solid",
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[5, 5],
    )
    style.map(
        "TEntry",
        bordercolor=[("focus", PALETTE["primary"])],
        fieldbackground=[
            ("readonly", PALETTE["background"]),
            ("disabled", PALETTE["background"]),
        ],
        foreground=[
            ("disabled", PALETTE["on_surface"]), # Muted text for disabled entry
        ]
    )

    # --- TCombobox Style ---
    style.configure(
        "TCombobox",
        font=base_font,
        fieldbackground=PALETTE["surface"],
        foreground=PALETTE["on_surface"],
        selectbackground=PALETTE["primary"],
        selectforeground=PALETTE["on_primary"],
        bordercolor=PALETTE["border"],
        borderwidth=1,
        relief="solid",
        padding=[5, 5],
    )
    style.map(
        "TCombobox",
        bordercolor=[("focus", PALETTE["primary"])],
        fieldbackground=[("readonly", PALETTE["background"])],
        foreground=[("disabled", PALETTE["on_surface"])], # Muted text for disabled combobox
        background=[
            ("hover", PALETTE["secondary_variant"]) # Darker accent on hover for dropdown button
        ],
    )
    # Styles for the dropdown list itself
    style.configure("TCombobox.Border",
                    foreground=PALETTE["border"],
                    background=PALETTE["surface"])
    style.configure("TCombobox.Listbox",
                    font=base_font,
                    foreground=PALETTE["on_surface"],
                    background=PALETTE["surface"],
                    selectforeground=PALETTE["on_primary"],
                    selectbackground=PALETTE["primary"])

    # --- TCheckbutton and TRadiobutton ---
    style.configure(
        "TCheckbutton",
        font=base_font,
        foreground=PALETTE["on_background"],
        background=PALETTE["background"],
        indicatorcolor=PALETTE["surface"], # Indicator background
        indicatorrelief="flat",
    )
    style.map(
        "TCheckbutton",
        foreground=[("disabled", PALETTE["on_background"])],
        background=[("active", PALETTE["background"])],
        indicatorcolor=[
            ("selected", PALETTE["primary"]), # Checked color
            ("disabled", PALETTE["secondary_variant"]), # Disabled indicator background
            ("!selected", PALETTE["surface"]), # Unchecked color
        ],
        # Overlay color for the checkmark itself - often controlled by element options
        # This might require using `element create` for full control, but this is a good start.
        # Otherwise, the default 'clam' theme's checkmark color will be used.
    )
    style.configure(
        "TRadiobutton",
        font=base_font,
        foreground=PALETTE["on_background"],
        background=PALETTE["background"],
        indicatorcolor=PALETTE["surface"], # Indicator background
        indicatorrelief="flat",
    )
    style.map(
        "TRadiobutton",
        foreground=[("disabled", PALETTE["on_background"])],
        background=[("active", PALETTE["background"])],
        indicatorcolor=[
            ("selected", PALETTE["primary"]), # Selected color
            ("disabled", PALETTE["secondary_variant"]), # Disabled indicator background
            ("!selected", PALETTE["surface"]), # Unselected color
        ],
    )


    # --- TNotebook (Tabs) Style ---
    style.configure(
        "TNotebook",
        background=PALETTE["background"],
        borderwidth=0,
        tabposition="nw",
        padding=[5, 5],
    )
    style.configure(
        "TNotebook.Tab",
        font=base_font,
        background=PALETTE["surface"],  # Tab background (unselected)
        foreground=PALETTE["on_surface"], # Muted text for unselected tabs
        padding=[10, 5],
        borderwidth=0,
        relief="flat",
    )
    style.map(
        "TNotebook.Tab",
        background=[
            ("selected", PALETTE["background"]),  # Selected tab is background color
            ("active", PALETTE["surface"]), # Hover over unselected tab
        ],
        foreground=[
            ("selected", PALETTE["on_background"]), # Vibrant text for selected tab
            ("active", PALETTE["on_surface"]), # Vibrant text for active/hovered tab
        ],
        expand=[("selected", [0, 0, 0, 0])],
    )
    style.configure(
        "TNotebook.Client", background=PALETTE["background"], borderwidth=0
    )

    # --- TLabelframe Style (Modern Look) ---
    style.configure(
        "TLabelframe",
        background=PALETTE["surface"],
        foreground=PALETTE["on_surface"],
        font=base_font,
        relief="solid",
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[10, 10, 10, 10],
    )
    style.configure(
        "TLabelframe.Label",
        background=PALETTE["surface"],
        foreground=PALETTE["on_surface"],
        font=heading_font,
        padding=[5, 2],
    )
    style.map(
        "TLabelframe",
        bordercolor=[("active", PALETTE["primary"])], # Border color change on active/hover
    )