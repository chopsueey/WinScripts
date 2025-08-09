from tkinter import ttk
import tkinter.font
from lib.material_constants import LIGHT_PALETTE, DARK_PALETTE, FONT_FAMILY, TITLE_FONT, HEADING_FONT, BODY_FONT, BUTTON_FONT


def init_style(theme="light"):
    """
    Initializes and configures a ttk.Style based on the selected theme.
    """
    style = ttk.Style()
    style.theme_use("clam")

    p = LIGHT_PALETTE if theme == "light" else DARK_PALETTE

    # --- Font Handling ---
    # Check if the primary font is available, otherwise use a fallback.
    # Note: The font tuples are imported but we need to resolve the family name dynamically.
    font_family = FONT_FAMILY
    if FONT_FAMILY not in tkinter.font.families():
        font_family = "Segoe UI"

    title_font = (font_family, TITLE_FONT[1], TITLE_FONT[2])
    heading_font = (font_family, HEADING_FONT[1], HEADING_FONT[2])
    body_font = (font_family, BODY_FONT[1], BODY_FONT[2])
    button_font = (font_family, BUTTON_FONT[1], BUTTON_FONT[2])

    # --- General Widget Configurations ---
    style.configure(".",
                    background=p["background"],
                    foreground=p["on_background"],
                    font=body_font,
                    borderwidth=0,
                    relief="flat")

    # --- Frame Styles ---
    style.configure("TFrame", background=p["background"])
    style.configure("Card.TFrame", background=p["surface"], relief="solid", borderwidth=1, bordercolor=p["border"])

    # --- Label Styles ---
    style.configure("TLabel", background=p["background"], foreground=p["on_background"], font=body_font)
    style.configure("Heading.TLabel", font=heading_font, foreground=p["on_background"], background=p["background"])
    style.configure("Title.TLabel", font=title_font, foreground=p["on_background"], background=p["background"])
    style.configure("Accent.TLabel", foreground=p["secondary"], background=p["background"])

    # --- Button Styles ---
    style.configure("TButton",
                    background=p["primary"],
                    foreground=p["on_primary"],
                    font=button_font,
                    padding=(12, 6),
                    relief="flat",
                    borderwidth=0)
    style.map("TButton",
              background=[("active", p["primary_variant"]), ("pressed", p["primary_variant"])])

    style.configure("Secondary.TButton",
                    background=p["surface"],
                    foreground=p["primary"],
                    font=button_font,
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
                    font=body_font,
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
                    font=body_font,
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
                    font=body_font)
    style.map("TCheckbutton",
              indicatorcolor=[("selected", p["primary"]), ("!selected", p["on_surface"])],
              background=[("active", p["background"])])

    style.configure("TRadiobutton",
                    background=p["background"],
                    foreground=p["on_background"],
                    font=body_font)
    style.map("TRadiobutton",
              indicatorcolor=[("selected", p["primary"]), ("!selected", p["on_surface"])],
              background=[("active", p["background"])])

    # --- Notebook (Tabs) Style ---
    style.configure("TNotebook", background=p["background"], borderwidth=0)
    style.configure("TNotebook.Tab",
                    background=p["surface"],
                    foreground=p["on_surface"],
                    font=button_font,
                    padding=(10, 5),
                    borderwidth=0)
    style.map("TNotebook.Tab",
              background=[("selected", p["background"]), ("active", p["border"])],
              foreground=[("selected", p["primary"])])

    # --- Labelframe Style ---
    style.configure("TLabelframe",
                    background=p["surface"],
                    foreground=p["on_surface"],
                    font=heading_font,
                    relief="solid",
                    borderwidth=1,
                    bordercolor=p["border"],
                    padding=10)
    style.configure("TLabelframe.Label",
                    background=p["surface"],
                    foreground=p["primary"],
                    font=heading_font)

    # --- Progressbar Style ---
    style.configure("TProgressbar",
                    background=p["primary"],
                    troughcolor=p["border"],
                    borderwidth=0,
                    thickness=8)
