import tkinter as tk
from tkinter import ttk
import tkinter.font
from PIL import Image, ImageDraw

# --- Rounded Corner Asset Generator ---

# Store PhotoImage objects to prevent garbage collection
_photo_images = {}

def create_rounded_bordered_image(width, height, radius, fill_color, border_color=None, border_width=0):
    """Creates a rounded rectangle image, optionally with a border."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if border_width > 0 and border_color:
        # Draw the outer rectangle (border)
        draw.rounded_rectangle((0, 0, width, height), radius, fill=border_color)
        # Draw the inner rectangle (fill)
        inner_radius = max(0, radius - border_width)
        inner_box = (border_width, border_width, width - border_width, height - border_width)
        draw.rounded_rectangle(inner_box, inner_radius, fill=fill_color)
    else:
        # Draw a single-color rounded rectangle
        draw.rounded_rectangle((0, 0, width, height), radius, fill=fill_color)
    return img

def get_photo_image(image, name_prefix):
    """Caches and returns a PhotoImage."""
    key = f"{name_prefix}_{image.tobytes()}"
    if key not in _photo_images:
        unique_name = f"img_{len(_photo_images)}"
        _photo_images[key] = tk.PhotoImage(image, name=unique_name)
    return _photo_images[key]

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
    border_radius = 6
    border_width = 1
    img_size = 32  # A small, scalable size for the images

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

    # Card Style
    card_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["surface"], p["border"], border_width)
    photo_card = get_photo_image(card_img, "card")
    style.element_create("Card.background", "image", photo_card, border=border_radius, sticky="nsew")
    style.layout("Card.TFrame", [("Card.background", {"sticky": "nsew"})])
    style.configure("Card.TFrame", relief="flat", borderwidth=0)

    # --- Label Styles ---
    style.configure("TLabel", background=p["background"], foreground=p["on_background"], font=BODY_FONT)
    style.configure("Heading.TLabel", font=HEADING_FONT, foreground=p["on_background"], background=p["background"])
    style.configure("Title.TLabel", font=TITLE_FONT, foreground=p["on_background"], background=p["background"])
    style.configure("Accent.TLabel", foreground=p["secondary"], background=p["background"])

    # --- Button Styles ---
    # Primary Button
    btn_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["primary"])
    btn_img_active = create_rounded_bordered_image(img_size, img_size, border_radius, p["primary_variant"])
    photo_btn = get_photo_image(btn_img, "btn")
    photo_btn_active = get_photo_image(btn_img_active, "btn_active")
    style.element_create("Button.background", "image", photo_btn, ("active", photo_btn_active), border=border_radius, sticky="nsew")
    style.layout("TButton", [("Button.background", {"sticky": "nsew", "children": [("Button.padding", {"sticky": "nsew", "children": [("Button.label", {"sticky": "nsew"})]})]})])
    style.configure("TButton", foreground=p["on_primary"], font=BUTTON_FONT, padding=(12, 6), relief="flat", borderwidth=0)
    style.map("TButton", background=[], relief=[]) # Clear maps

    # Secondary Button
    sec_btn_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["surface"], p["border"], border_width)
    sec_btn_img_active = create_rounded_bordered_image(img_size, img_size, border_radius, p["border"], p["primary"], border_width)
    photo_sec_btn = get_photo_image(sec_btn_img, "sec_btn")
    photo_sec_btn_active = get_photo_image(sec_btn_img_active, "sec_btn_active")
    style.element_create("Secondary.Button.background", "image", photo_sec_btn, ("active", photo_sec_btn_active), border=border_radius, sticky="nsew")
    style.layout("Secondary.TButton", [("Secondary.Button.background", {"sticky": "nsew", "children": [("Button.padding", {"sticky": "nsew", "children": [("Button.label", {"sticky": "nsew"})]})]})])
    style.configure("Secondary.TButton", foreground=p["primary"], font=BUTTON_FONT, padding=(12, 6), relief="flat", borderwidth=0)
    style.map("Secondary.TButton", foreground=[("active", p["primary"])], background=[], relief=[], bordercolor=[])

    # --- Entry Style ---
    entry_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["surface"], p["border"], border_width)
    entry_img_focus = create_rounded_bordered_image(img_size, img_size, border_radius, p["surface"], p["primary"], border_width)
    photo_entry = get_photo_image(entry_img, "entry")
    photo_entry_focus = get_photo_image(entry_img_focus, "entry_focus")
    style.element_create("Entry.background", "image", photo_entry, ("focus", photo_entry_focus), border=border_radius, sticky="nsew")
    style.layout("TEntry", [("Entry.background", {"sticky": "nsew", "children": [("Entry.padding", {"sticky": "nsew", "children": [("Entry.textarea", {"sticky": "nsew"})]})]})])
    style.configure("TEntry", foreground=p["on_surface"], insertcolor=p["primary"], font=BODY_FONT, padding=5, relief="flat", borderwidth=0)
    style.map("TEntry", fieldbackground=[], bordercolor=[], lightcolor=[], darkcolor=[])

    # --- Combobox Style ---
    style.configure("TCombobox", foreground=p["on_surface"], arrowcolor=p["primary"], selectbackground=p["primary"], selectforeground=p["on_primary"], font=BODY_FONT, padding=5, relief="flat", borderwidth=0)
    style.layout("TCombobox", [("Entry.background", {"sticky": "nsew", "children": [("Combobox.padding", {"sticky": "nsew", "children": [("Combobox.textarea", {"sticky": "nsew"})]}), ('Combobox.down_arrow', {'side': 'right', 'sticky': 'ns'})]})])
    style.map("TCombobox", fieldbackground=[], bordercolor=[])
    style.configure("TCombobox.Listbox", background=p["surface"], foreground=p["on_surface"], selectbackground=p["primary"], selectforeground=p["on_primary"])

    # --- Checkbutton and Radiobutton Styles ---
    style.configure("TCheckbutton", background=p["background"], foreground=p["on_background"], font=BODY_FONT)
    style.map("TCheckbutton", indicatorcolor=[("selected", p["primary"]), ("!selected", p["on_surface"])], background=[("active", p["background"])])
    style.configure("TRadiobutton", background=p["background"], foreground=p["on_background"], font=BODY_FONT)
    style.map("TRadiobutton", indicatorcolor=[("selected", p["primary"]), ("!selected", p["on_surface"])], background=[("active", p["background"])])

    # --- Notebook (Tabs) Style ---
    style.configure("TNotebook", background=p["background"], borderwidth=0)
    # Tab itself is not easily rounded, leave as is for now to avoid visual glitches.
    style.configure("TNotebook.Tab", background=p["surface"], foreground=p["on_surface"], font=BUTTON_FONT, padding=(10, 5), borderwidth=0)
    style.map("TNotebook.Tab", background=[("selected", p["background"]), ("active", p["border"])], foreground=[("selected", p["primary"])])

    # --- Labelframe Style ---
    lf_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["surface"], p["border"], border_width)
    photo_lf = get_photo_image(lf_img, "labelframe")
    style.element_create("Labelframe.background", "image", photo_lf, border=border_radius, sticky="nsew")
    style.layout("TLabelframe", [("Labelframe.background", {"sticky": "nsew", "children": [("Labelframe.padding", {"sticky": "nsew", "children": [("Labelframe.label", {"side": "top", "sticky": "w"}), ("Labelframe.child", {"sticky": "nsew"})]})]})])
    style.configure("TLabelframe", relief="flat", borderwidth=0, padding=10)
    style.configure("TLabelframe.Label", background=p["surface"], foreground=p["primary"], font=HEADING_FONT)

    # --- Progressbar Style ---
    # Progressbar doesn't have a simple border element, but we can round the trough and bar
    bar_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["primary"])
    trough_img = create_rounded_bordered_image(img_size, img_size, border_radius, p["border"])
    photo_bar = get_photo_image(bar_img, "prog_bar")
    photo_trough = get_photo_image(trough_img, "prog_trough")
    style.element_create("Progressbar.trough", "image", photo_trough, border=border_radius)
    style.element_create("Progressbar.bar", "image", photo_bar, border=border_radius)
    style.layout("TProgressbar", [("Progressbar.trough", {"children": [("Progressbar.bar", {"sticky": "nswe"})]})])
    style.configure("TProgressbar", borderwidth=0, thickness=8, background=p["primary"])
