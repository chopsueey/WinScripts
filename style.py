from tkinter import ttk

# --- Define a Modern Color Palette ---
PALETTE = {
    "primary": "#007bff",  # Blue for main actions
    "primary_dark": "#0056b3",  # Darker blue for active states
    "accent": "#6c757d",  # Gray for secondary elements
    "accent_dark": "#5a6268",  # Darker gray
    "background": "#f8f9fa",  # Light gray for general background
    "surface": "#ffffff",  # White for widget backgrounds
    "text": "#343a40",  # Dark gray for general text
    "text_light": "#e9ecef",  # Very light gray for text on dark backgrounds
    "border": "#ced4da",  # Light gray-blue for borders
    "success": "#28a745",  # Green for success
    "danger": "#dc3545",  # Red for danger
    "warning": "#ffc107",  # Yellow for warning
    "info": "#17a2b8",  # Cyan for info
}


# --- Styling Function ---
def init_style():
    """Initializes and configures modern-looking ttk.Style for base widgets."""
    style = ttk.Style()

    # Set the overall theme if desired (e.g., 'clam', 'alt', 'default', 'classic')
    # 'clam' is often a good base for custom modern styles as it's quite neutral.
    style.theme_use("clam")

    # --- General Font Configuration ---
    # Using a common font family and base size for consistency
    base_font = ("Segoe UI", 10)  # 'Segoe UI' is a good modern system font.
    # Fallback to 'Helvetica' or 'Arial' if not available.
    heading_font = ("Segoe UI", 12, "bold")
    large_font = ("Segoe UI", 12)

    # --- TFrame Style ---
    style.configure(
        "TFrame",
        background=PALETTE["background"],
        relief="flat",  # No 3D effect
        borderwidth=0,  # No border by default
        padding=10,  # Some internal padding
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
        background=PALETTE["background"],  # Matches frame background for blend
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
        foreground=PALETTE["text_light"],  # White text on primary button
        background=PALETTE["primary"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],  # [left/right, top/bottom]
    )
    style.map(
        "TButton",
        background=[
            ("active", PALETTE["primary_dark"]),
            ("pressed", PALETTE["primary_dark"]),
        ],
        foreground=[("active", PALETTE["text_light"])],
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
        foreground=PALETTE["text_light"],
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
        foreground=[("active", PALETTE["text_light"])],
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
        selectbackground=PALETTE["primary"],  # Background of selected item in dropdown
        selectforeground=PALETTE["text_light"],  # Text of selected item
        bordercolor=PALETTE["border"],
        borderwidth=1,
        relief="solid",
        padding=[5, 5],
    )
    style.map(
        "TCombobox",
        bordercolor=[("focus", PALETTE["primary"])],
        fieldbackground=[("readonly", PALETTE["background"])],
        background=[
            ("hover", PALETTE["primary_dark"])
        ],  # Background of the dropdown button
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
        foreground=[("selected", PALETTE["text_light"]), ("active", PALETTE["text"])],
        expand=[("selected", [0, 0, 0, 0])],  # No expansion on selected tab
    )
    style.configure(
        "TNotebook.Client", background=PALETTE["surface"], borderwidth=0
    )  # Background of the tab content area
