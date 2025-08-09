from tkinter import ttk
import tkinter.font
from lib.material_constants import LIGHT_PALETTE

def init_style():
    """
    Initializes and configures a ttk.Style based on Material Design principles.
    """
    style = ttk.Style()
    style.theme_use("clam")

    p = LIGHT_PALETTE

    # --- Font Handling ---
    # Check for Roboto and set a fallback
    font_family = "Roboto"
    if "Roboto" not in tkinter.font.families():
        font_family = "Segoe UI"

    # Define font styles dynamically
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
    # Primary Button (for main actions)
    style.configure("TButton",
                    background=p["primary"],
                    foreground=p["on_primary"],
                    font=BUTTON_FONT,
                    padding=(12, 6),
                    relief="flat",
                    borderwidth=0)
    style.map("TButton",
              background=[("active", p["primary_variant"]), ("pressed", p["primary_variant"])])

    # Secondary Button (for less prominent actions)
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
