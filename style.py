from tkinter import ttk
import tkinter as tk

# --- Define a Modern Slightly Darker Light Mode Color Palette ---
PALETTE = {
    "primary": "#007bff",  # Blue for main actions
    "primary_dark": "#0056b3",  # Darker blue for active states
    "accent": "#5a6268",  # Slightly darker gray for secondary elements
    "accent_dark": "#495057",  # Darker gray for active accent states
    # Adjusted for a slightly darker light mode look
    "background": "#e9ecef",  # Deeper light gray for general background
    "surface": "#f0f2f5",  # Subtle off-white for widget backgrounds
    "text": "#343a40",  # Dark gray for general text (unchanged, good contrast)
    "text_light": "#6c757d",  # More prominent light text for better readability on darker light backgrounds
    "border": "#adb5bd",  # Darker light gray-blue for borders
    "success": "#28a745",  # Green for success
    "danger": "#dc3545",  # Red for danger
    "warning": "#ffc107",  # Yellow for warning
    "info": "#17a2b8",  # Cyan for info
}


# --- Styling Function ---
def init_style():
    """Initializes and configures modern-looking ttk.Style for slightly darker light mode widgets."""
    style = ttk.Style()

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
        foreground=PALETTE["accent"],
        background=PALETTE["background"],
    )

    # --- TButton Style (Modern Flat) ---
    # Default Button (primary action)
    style.configure(
        "TButton",  # Default TButton style
        font=large_font,
        foreground=PALETTE["surface"],  # Very light text for contrast on primary button
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
        foreground=[
            ("active", PALETTE["surface"])
        ],  # Maintain light text on active state
        relief=[("pressed", "flat"), ("!pressed", "flat")],  # Ensure flat on press
    )

    # Secondary Button (e.g., cancel, less prominent actions)
    style.configure(
        "Secondary.TButton",
        font=large_font,
        foreground=PALETTE["text"],
        background=PALETTE["surface"],
        relief="solid",  # A subtle border
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[15, 8],
    )
    style.map(
        "Secondary.TButton",
        background=[
            ("active", PALETTE["background"]),
            ("pressed", PALETTE["background"]),
        ],  # Background changes to lighter shade
        foreground=[("active", PALETTE["text"])],
        relief=[("pressed", "solid"), ("!pressed", "solid")],
        bordercolor=[("active", PALETTE["accent"])],  # Border changes on hover
    )

    # Danger Button (e.g., delete)
    style.configure(
        "Danger.TButton",
        font=large_font,
        foreground=PALETTE["surface"],  # Very light text for contrast on danger button
        background=PALETTE["danger"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],
    )
    style.map(
        "Danger.TButton",
        background=[
            ("active", "#c82333"),
            ("pressed", "#bd2130"),
        ],  # Darker red on hover
        foreground=[
            ("active", PALETTE["surface"])
        ],  # Maintain light text on active state
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )

    # --- TEntry Style (Modern Input Field) ---
    style.configure(
        "TEntry",
        font=base_font,
        fieldbackground=PALETTE["surface"],  # Background of the input field
        foreground=PALETTE["text"],
        insertcolor=PALETTE["primary"],  # Cursor color
        relief="solid",  # A subtle border
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[5, 5],  # Internal padding
    )
    style.map(
        "TEntry",
        bordercolor=[("focus", PALETTE["primary"])],  # Border color changes on focus
        fieldbackground=[
            ("readonly", PALETTE["background"]),
            ("disabled", PALETTE["background"]),
        ],
    )

    # --- TCombobox Style ---
    style.configure(
        "TCombobox",
        font=base_font,
        fieldbackground=PALETTE["surface"],
        foreground=PALETTE["text"],
        bordercolor=PALETTE["border"],
        borderwidth=1,
        relief="solid",
        padding=[5, 5],
    )

    style.map(
        "TCombobox",
        bordercolor=[("focus", PALETTE["primary"])],
        fieldbackground=[("readonly", PALETTE["background"])],
        background=[("hover", PALETTE["primary_dark"])],
        foreground=[("readonly", PALETTE["text"])],
    )

    style.configure(
        "TCombobox.Listbox",
        font=base_font,
        foreground=PALETTE["text"],
        background=PALETTE["surface"],
        selectbackground=PALETTE["primary"],  # Your primary blue for highlight
        selectforeground=PALETTE["surface"],  # Light text on primary blue, very visible
    )

    # --- TCheckbutton and TRadiobutton ---
    style.configure(
        "TCheckbutton",
        font=base_font,
        foreground=PALETTE["text"],
        background=PALETTE["background"],
        indicatorcolor=PALETTE["primary"],  # Color of the checkmark/radio dot
        indicatorrelief="flat",
    )
    style.map(
        "TCheckbutton",
        foreground=[("disabled", PALETTE["accent"])],
        background=[
            ("active", PALETTE["background"])
        ],  # Active background remains same
        indicatorcolor=[
            ("selected", PALETTE["primary"]),
            ("disabled", PALETTE["accent"]),
            ("!selected", PALETTE["surface"]),  # Unselected indicator background
        ],
    )

    style.configure(
        "TRadiobutton",
        font=base_font,
        foreground=PALETTE["text"],
        background=PALETTE["background"],
        indicatorcolor=PALETTE["primary"],
        indicatorrelief="flat",
    )
    style.map(
        "TRadiobutton",
        foreground=[("disabled", PALETTE["accent"])],
        background=[("active", PALETTE["background"])],
        indicatorcolor=[
            ("selected", PALETTE["primary"]),
            ("disabled", PALETTE["accent"]),
            ("!selected", PALETTE["surface"]),  # Unselected indicator background
        ],
    )

    # --- TNotebook (Tabs) Style ---
    style.configure(
        "TNotebook",
        background=PALETTE["background"],
        borderwidth=0,
        tabposition="nw",  # Tabs at north-west
        padding=[5, 5],
    )
    style.configure(
        "TNotebook.Tab",
        font=base_font,
        background=PALETTE["background"],  # Default tab background
        foreground=PALETTE["text"],
        padding=[10, 5],
        borderwidth=0,  # Remove default tab border
        relief="flat",
    )
    style.map(
        "TNotebook.Tab",
        background=[
            ("selected", PALETTE["primary"]),
            ("active", PALETTE["border"]),
        ],  # Selected tab is primary, hover is border
        foreground=[
            (
                "selected",
                PALETTE["surface"],
            ),  # ***CHANGED: Light text on selected (primary) tab***
            ("active", PALETTE["text"]),
        ],
        expand=[("selected", [0, 0, 0, 0])],  # No expansion on selected tab
    )
    style.configure(
        "TNotebook.Client", background=PALETTE["surface"], borderwidth=0
    )  # Background of the tab content area

    # --- TLabelframe Style (Modern Look) ---
    style.configure(
        "TLabelframe",
        background=PALETTE["surface"],  # Background of the Labelframe's content area
        foreground=PALETTE["text"],  # Color of the label text
        font=base_font,
        relief="solid",  # A subtle solid border
        borderwidth=1,
        bordercolor=PALETTE["border"],
        padding=[10, 10, 10, 10],  # Padding around the content inside the frame
    )
    style.configure(
        "TLabelframe.Label",
        background=PALETTE["surface"],  # Matches the Labelframe background
        foreground=PALETTE["text"],  # Label text color
        font=heading_font,  # Use heading font for the label for prominence
        padding=[5, 2],  # Padding around the label itself
    )
    style.map(
        "TLabelframe",
        bordercolor=[
            ("active", PALETTE["accent"])
        ],  # Border color change on active/hover
    )

    # --- TProgressbar Style ---
    style.configure(
        "TProgressbar",
        background=PALETTE["primary"],  # Color of the filled portion
        troughcolor=PALETTE["border"],  # Color of the empty portion (trough)
        bordercolor=PALETTE["border"],  # Border around the trough
        thickness=15,  # Height/width of the bar
        relief="flat",  # Flat appearance
        borderwidth=1,  # Subtle border
    )
    # Map for indeterminate mode (if used)
    style.map(
        "TProgressbar",
        background=[("active", PALETTE["primary_dark"])],  # Slightly darker when active
    )
