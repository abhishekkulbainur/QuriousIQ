# styles.py

LIGHT_THEME = {
    "bg": "#ffffff",
    "fg": "#000000",
    "button_bg": "#f0f0f0",
    "button_fg": "#000000",
    "highlight": "#007acc"
}

DARK_THEME = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "button_bg": "#333333",
    "button_fg": "#ffffff",
    "highlight": "#ff9800"
}

def apply_theme(widget, theme: dict):
    """
    Recursively apply theme colors to a Tkinter widget and its children.
    """
    if "bg" in theme:
        try:
            widget.configure(bg=theme["bg"])
        except:
            pass
    if "fg" in theme:
        try:
            widget.configure(fg=theme["fg"])
        except:
            pass

    for child in widget.winfo_children():
        apply_theme(child, theme)
