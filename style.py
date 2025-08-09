from tkinter import ttk
import tkinter.font

# --- Define Color Palettes ---
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

def init_style(theme="light"):
    """
    Initializes and configures a ttk.Style based on the selected theme.
    """
    style = ttk.Style()
    style.theme_use("clam")

    p = LIGHT_PALETTE if theme == "light" else DARK_PALETTE

    # --- Font Handling ---
    font_family = "Roboto"
    if "Roboto" not in tkinter.font.families():
        font_family = "Segoe UI"

    TITLE_FONT = (font_family, 20, "bold")
    HEADING_FONT = (font_family, 16, "bold")
    BODY_FONT = (font_family, 12, "normal")
    BUTTON_FONT = (font_family, 12, "bold")

    # --- General Widget Configurations ---
    style.configure(".",
                    background=p["background"],
                    foreground=p["on_background"],
                    font=BODY_FONT,
                    borderwidth=0,
                    relief="flat")

    # --- Frame Styles ---
    style.configure("TFrame", background=p["background"])
    style.configure("Card.TFrame", background=p["surface"], relief="solid", borderwidth=1, bordercolor=p["border"])

    # --- Label Styles ---
    style.configure("TLabel", background=p["background"], foreground=p["on_background"], font=BODY_FONT)
    style.configure("Heading.TLabel", font=HEADING_FONT, foreground=p["on_background"], background=p["background"])
    style.configure("Title.TLabel", font=TITLE_FONT, foreground=p["on_background"], background=p["background"])
    style.configure("Accent.TLabel", foreground=p["secondary"], background=p["background"])

    # --- Button Styles ---
    style.configure("TButton",
                    background=p["primary"],
                    foreground=p["on_primary"],
                    font=BUTTON_FONT,
                    padding=(12, 6),
                    relief="flat",
                    borderwidth=0)
    style.map("TButton",
              background=[("active", p["primary_variant"]), ("pressed", p["primary_variant"])])

    style.configure("Secondary.TButton",
                    background=p["surface"],
                    foreground=p["primary"],
                    font=BUTTON_FONT,
                    padding=(12, 6),
                    relief="solid",
                    borderwidth=1,
                    bordercolor=p["border"])
    style.map("Secondary.TButton",
              background=[("active", p["border"]), ("pressed", p["border"])],
              bordercolor=[("active", p["primary"])])

    # --- Entry Style ---
    style.configure("TEntry",
                    fieldbackground=p["surface"],
                    foreground=p["on_surface"],
                    insertcolor=p["primary"],
                    font=BODY_FONT,
                    padding=5,
                    relief="solid",
                    borderwidth=1,
                    bordercolor=p["border"])
    style.map("TEntry",
              bordercolor=[("focus", p["primary"])],
              fieldbackground=[("readonly", p["background"])])

    # --- Combobox Style ---
    style.configure("TCombobox",
                    fieldbackground=p["surface"],
                    foreground=p["on_surface"],
                    arrowcolor=p["primary"],
                    selectbackground=p["primary"],
                    selectforeground=p["on_primary"],
                    font=BODY_FONT,
                    padding=5,
                    relief="solid",
                    borderwidth=1,
                    bordercolor=p["border"])
    style.map("TCombobox",
              bordercolor=[("focus", p["primary"])])
    style.configure("TCombobox.Listbox",
                    background=p["surface"],
                    foreground=p["on_surface"],
                    selectbackground=p["primary"],
                    selectforeground=p["on_primary"])

    # --- Checkbutton and Radiobutton Styles ---
    style.configure("TCheckbutton",
                    background=p["background"],
                    foreground=p["on_background"],
                    font=BODY_FONT)
    style.map("TCheckbutton",
              indicatorcolor=[("selected", p["primary"]), ("!selected", p["on_surface"])],
              background=[("active", p["background"])])

    style.configure("TRadiobutton",
                    background=p["background"],
                    foreground=p["on_background"],
                    font=BODY_FONT)
    style.map("TRadiobutton",
              indicatorcolor=[("selected", p["primary"]), ("!selected", p["on_surface"])],
              background=[("active", p["background"])])

    # --- Notebook (Tabs) Style ---
    style.configure("TNotebook", background=p["background"], borderwidth=0)
    style.configure("TNotebook.Tab",
                    background=p["surface"],
                    foreground=p["on_surface"],
                    font=BUTTON_FONT,
                    padding=(10, 5),
                    borderwidth=0)
    style.map("TNotebook.Tab",
              background=[("selected", p["background"]), ("active", p["border"])],
              foreground=[("selected", p["primary"])])

    # --- Labelframe Style ---
    style.configure("TLabelframe",
                    background=p["surface"],
                    foreground=p["on_surface"],
                    font=HEADING_FONT,
                    relief="solid",
                    borderwidth=1,
                    bordercolor=p["border"],
                    padding=10)
    style.configure("TLabelframe.Label",
                    background=p["surface"],
                    foreground=p["primary"],
                    font=HEADING_FONT)

    # --- Progressbar Style ---
    style.configure("TProgressbar",
                    background=p["primary"],
                    troughcolor=p["border"],
                    borderwidth=0,
                    thickness=8)
