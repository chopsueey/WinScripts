from tkinter import ttk
import tkinter as tk

# --- Define a Modern Dark Mode Color Palette ---
PALETTE = {
    "primary": "#8ab4f8",  # Lighter blue for main actions (Google Material Blue 300/400 equivalent)
    "primary_dark": "#6a9df8",  # Slightly darker primary for active states
    "accent": "#9aa0a6",  # Muted light gray for secondary elements
    "accent_dark": "#7b8086",  # Darker gray for active accent states
    "background": "#202124",  # Very dark gray for general background (Google Dark Mode BG)
    "surface": "#2d2e31",  # Slightly lighter dark gray for widget backgrounds (cards, frames)
    "text": "#e8eaed",  # Light gray for general text
    "text_light": "#bdc1c6",  # Muted light gray for less prominent text (originally for text on dark bg, now for secondary)
    "border": "#5f6368",  # Medium-dark gray for subtle borders
    "success": "#85c485",  # Muted green for success
    "danger": "#f28b82",  # Muted red for danger
    "warning": "#fdd663",  # Muted yellow for warning
    "info": "#78d0ea",  # Muted cyan for info
}


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
        foreground=PALETTE["text"],
        background=PALETTE["background"],
        relief="flat",
    )
    # Heading Label
    style.configure(
        "Heading.TLabel",
        font=heading_font,
        foreground=PALETTE["text"],
        background=PALETTE["background"],
    )
    # Accent Label (e.g., for disabled text or secondary info)
    style.configure(
        "Accent.TLabel",
        font=base_font,
        foreground=PALETTE["text_light"],  # Using text_light for subtle text
        background=PALETTE["background"],
    )

    # --- TButton Style (Modern Flat) ---
    # Default Button (primary action)
    style.configure(
        "TButton",  # Default TButton style
        font=large_font,
        foreground=PALETTE["background"],  # Dark text on lighter primary button
        background=PALETTE["primary"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],
    )
    style.map(
        "TButton",
        background=[
            ("active", PALETTE["primary_dark"]),
            ("pressed", PALETTE["primary_dark"]),
        ],
        foreground=[("active", PALETTE["background"])],
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )

    # Secondary Button
    style.configure(
        "Secondary.TButton",
        font=large_font,
        foreground=PALETTE["text"],  # Light text on dark surface
        background=PALETTE["surface"],
        relief="solid",
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[15, 8],
    )
    style.map(
        "Secondary.TButton",
        background=[
            ("active", PALETTE["accent_dark"]),  # Darker accent on hover
            ("pressed", PALETTE["accent_dark"]),
        ],
        foreground=[("active", PALETTE["text"])],
        relief=[("pressed", "solid"), ("!pressed", "solid")],
        bordercolor=[("active", PALETTE["accent"])],
    )

    # Danger Button
    style.configure(
        "Danger.TButton",
        font=large_font,
        foreground=PALETTE["background"],  # Dark text on danger button
        background=PALETTE["danger"],
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
        foreground=[("active", PALETTE["background"])],
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )

    # --- TEntry Style (Modern Input Field) ---
    style.configure(
        "TEntry",
        font=base_font,
        fieldbackground=PALETTE["surface"],
        foreground=PALETTE["text"],
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
            ("disabled", PALETTE["text_light"]), # Muted text for disabled entry
        ]
    )

    # --- TCombobox Style ---
    style.configure(
        "TCombobox",
        font=base_font,
        fieldbackground=PALETTE["surface"],
        foreground=PALETTE["text"],
        selectbackground=PALETTE["primary"],
        selectforeground=PALETTE["background"], # Dark text on primary selected item
        bordercolor=PALETTE["border"],
        borderwidth=1,
        relief="solid",
        padding=[5, 5],
    )
    style.map(
        "TCombobox",
        bordercolor=[("focus", PALETTE["primary"])],
        fieldbackground=[("readonly", PALETTE["background"])],
        foreground=[("disabled", PALETTE["text_light"])], # Muted text for disabled combobox
        background=[
            ("hover", PALETTE["accent_dark"]) # Darker accent on hover for dropdown button
        ],
    )
    # Styles for the dropdown list itself
    style.configure("TCombobox.Border",
                    foreground=PALETTE["border"],
                    background=PALETTE["surface"])
    style.configure("TCombobox.Listbox",
                    font=base_font,
                    foreground=PALETTE["text"],
                    background=PALETTE["surface"],
                    selectforeground=PALETTE["background"],
                    selectbackground=PALETTE["primary"])

    # --- TCheckbutton and TRadiobutton ---
    style.configure(
        "TCheckbutton",
        font=base_font,
        foreground=PALETTE["text"],
        background=PALETTE["background"],
        indicatorcolor=PALETTE["surface"], # Indicator background
        indicatorrelief="flat",
    )
    style.map(
        "TCheckbutton",
        foreground=[("disabled", PALETTE["text_light"])],
        background=[("active", PALETTE["background"])],
        indicatorcolor=[
            ("selected", PALETTE["primary"]), # Checked color
            ("disabled", PALETTE["accent_dark"]), # Disabled indicator background
            ("!selected", PALETTE["surface"]), # Unchecked color
        ],
        # Overlay color for the checkmark itself - often controlled by element options
        # This might require using `element create` for full control, but this is a good start.
        # Otherwise, the default 'clam' theme's checkmark color will be used.
    )
    style.configure(
        "TRadiobutton",
        font=base_font,
        foreground=PALETTE["text"],
        background=PALETTE["background"],
        indicatorcolor=PALETTE["surface"], # Indicator background
        indicatorrelief="flat",
    )
    style.map(
        "TRadiobutton",
        foreground=[("disabled", PALETTE["text_light"])],
        background=[("active", PALETTE["background"])],
        indicatorcolor=[
            ("selected", PALETTE["primary"]), # Selected color
            ("disabled", PALETTE["accent_dark"]), # Disabled indicator background
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
        foreground=PALETTE["text_light"], # Muted text for unselected tabs
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
            ("selected", PALETTE["text"]), # Vibrant text for selected tab
            ("active", PALETTE["text"]), # Vibrant text for active/hovered tab
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
        foreground=PALETTE["text"],
        font=base_font,
        relief="solid",
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[10, 10, 10, 10],
    )
    style.configure(
        "TLabelframe.Label",
        background=PALETTE["surface"],
        foreground=PALETTE["text"],
        font=heading_font,
        padding=[5, 2],
    )
    style.map(
        "TLabelframe",
        bordercolor=[("active", PALETTE["primary"])], # Border color change on active/hover
    )