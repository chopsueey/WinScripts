from tkinter import ttk

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


def _configure_frame_styles(style, palette):
    """Configure TFrame styles."""
    style.configure(
        "TFrame",
        background=palette["background"],
        relief="flat",
        borderwidth=0,
        padding=10,
    )
    style.configure(
        "Card.TFrame",
        background=palette["surface"],
        relief="flat",
        borderwidth=1,
        bordercolor=palette["border"],
        padding=15,
    )


def _configure_label_styles(style, palette, base_font, heading_font):
    """Configure TLabel styles."""
    style.configure(
        "TLabel",
        font=base_font,
        foreground=palette["text"],
        background=palette["background"],
        relief="flat",
    )
    style.configure(
        "Heading.TLabel",
        font=heading_font,
        foreground=palette["text"],
        background=palette["background"],
    )
    style.configure(
        "Accent.TLabel",
        font=base_font,
        foreground=palette["accent"],
        background=palette["background"],
    )


def _configure_button_styles(style, palette, large_font):
    """Configure TButton styles."""
    # Default Button (primary action)
    style.configure(
        "TButton",
        font=large_font,
        foreground=palette["surface"],
        background=palette["primary"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],
    )
    style.map(
        "TButton",
        background=[("active", palette["primary_dark"]), ("pressed", palette["primary_dark"])],
        foreground=[("active", palette["surface"])],
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )

    # Secondary Button
    style.configure(
        "Secondary.TButton",
        font=large_font,
        foreground=palette["text"],
        background=palette["surface"],
        relief="solid",
        borderwidth=1,
        bordercolor=palette["border"],
        padding=[15, 8],
    )
    style.map(
        "Secondary.TButton",
        background=[("active", palette["background"]), ("pressed", palette["background"])],
        foreground=[("active", palette["text"])],
        relief=[("pressed", "solid"), ("!pressed", "solid")],
        bordercolor=[("active", palette["accent"])],
    )

    # Danger Button
    style.configure(
        "Danger.TButton",
        font=large_font,
        foreground=palette["surface"],
        background=palette["danger"],
        relief="flat",
        borderwidth=0,
        padding=[15, 8],
    )
    style.map(
        "Danger.TButton",
        background=[("active", "#c82333"), ("pressed", "#bd2130")],
        foreground=[("active", palette["surface"])],
        relief=[("pressed", "flat"), ("!pressed", "flat")],
    )


def _configure_entry_styles(style, palette, base_font):
    """Configure TEntry styles."""
    style.configure(
        "TEntry",
        font=base_font,
        fieldbackground=palette["surface"],
        foreground=palette["text"],
        insertcolor=palette["primary"],
        relief="solid",
        borderwidth=1,
        bordercolor=palette["border"],
        padding=[5, 5],
    )
    style.map(
        "TEntry",
        bordercolor=[("focus", palette["primary"])],
        fieldbackground=[("readonly", palette["background"]), ("disabled", palette["background"])],
    )


def _configure_combobox_styles(style, palette, base_font):
    """Configure TCombobox styles."""
    style.configure(
        "TCombobox",
        font=base_font,
        fieldbackground=palette["surface"],
        foreground=palette["text"],
        bordercolor=palette["border"],
        borderwidth=1,
        relief="solid",
        padding=[5, 5],
    )
    style.map(
        "TCombobox",
        bordercolor=[("focus", palette["primary"])],
        fieldbackground=[("readonly", palette["background"])],
        background=[("hover", palette["primary_dark"])],
        foreground=[("readonly", palette["text"])],
    )
    style.configure(
        "TCombobox.Listbox",
        font=base_font,
        foreground=palette["text"],
        background=palette["surface"],
        selectbackground=palette["primary"],
        selectforeground=palette["surface"],
    )


def _configure_check_radio_styles(style, palette, base_font):
    """Configure TCheckbutton and TRadiobutton styles."""
    style.configure(
        "TCheckbutton",
        font=base_font,
        foreground=palette["text"],
        background=palette["background"],
        indicatorcolor=palette["primary"],
        indicatorrelief="flat",
    )
    style.map(
        "TCheckbutton",
        foreground=[("disabled", palette["accent"])],
        background=[("active", palette["background"])],
        indicatorcolor=[
            ("selected", palette["primary"]),
            ("disabled", palette["accent"]),
            ("!selected", palette["surface"]),
        ],
    )

    style.configure(
        "TRadiobutton",
        font=base_font,
        foreground=palette["text"],
        background=palette["background"],
        indicatorcolor=palette["primary"],
        indicatorrelief="flat",
    )
    style.map(
        "TRadiobutton",
        foreground=[("disabled", palette["accent"])],
        background=[("active", palette["background"])],
        indicatorcolor=[
            ("selected", palette["primary"]),
            ("disabled",palette["accent"]),
            ("!selected", palette["surface"]),
        ],
    )


def _configure_notebook_styles(style, palette, base_font):
    """Configure TNotebook styles."""
    style.configure(
        "TNotebook",
        background=palette["background"],
        borderwidth=0,
        tabposition="nw",
        padding=[5, 5],
    )
    style.configure(
        "TNotebook.Tab",
        font=base_font,
        background=palette["background"],
        foreground=palette["text"],
        padding=[10, 5],
        borderwidth=0,
        relief="flat",
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", palette["primary"]), ("active", palette["border"])],
        foreground=[("selected", palette["surface"]), ("active", palette["text"])],
        expand=[("selected", [0, 0, 0, 0])],
    )
    style.configure(
        "TNotebook.Client", background=palette["surface"], borderwidth=0
    )


def _configure_labelframe_styles(style, palette, base_font, heading_font):
    """Configure TLabelframe styles."""
    style.configure(
        "TLabelframe",
        background=palette["surface"],
        foreground=palette["text"],
        font=base_font,
        relief="solid",
        borderwidth=1,
        bordercolor=palette["border"],
        padding=[10, 10, 10, 10],
    )
    style.configure(
        "TLabelframe.Label",
        background=palette["surface"],
        foreground=palette["text"],
        font=heading_font,
        padding=[5, 2],
    )
    style.map(
        "TLabelframe",
        bordercolor=[("active", palette["accent"])],
    )


def _configure_progressbar_styles(style, palette):
    """Configure TProgressbar styles."""
    style.configure(
        "TProgressbar",
        background=palette["primary"],
        troughcolor=palette["border"],
        bordercolor=palette["border"],
        thickness=15,
        relief="flat",
        borderwidth=1,
    )
    style.map(
        "TProgressbar",
        background=[("active", palette["primary_dark"])],
    )


def init_style():
    """Initializes and configures modern-looking ttk.Style for slightly darker light mode widgets."""
    style = ttk.Style()
    style.theme_use("clam")

    # --- General Font Configuration ---
    base_font = ("Segoe UI", 10)
    heading_font = ("Segoe UI", 12, "bold")
    large_font = ("Segoe UI", 12)

    # --- Apply Styles ---
    _configure_frame_styles(style, PALETTE)
    _configure_label_styles(style, PALETTE, base_font, heading_font)
    _configure_button_styles(style, PALETTE, large_font)
    _configure_entry_styles(style, PALETTE, base_font)
    _configure_combobox_styles(style, PALETTE, base_font)
    _configure_check_radio_styles(style, PALETTE, base_font)
    _configure_notebook_styles(style, PALETTE, base_font)
    _configure_labelframe_styles(style, PALETTE, base_font, heading_font)
    _configure_progressbar_styles(style, PALETTE)
