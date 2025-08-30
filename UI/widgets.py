import tkinter as tk
from . import styles

def styled_button(root, text, command, color=styles.PRIMARY_COLOR):
    return tk.Button(
        root, 
        text=text,
        command=command,
        font=styles.FONT_BUTTON,
        bg=color,
        fg="white",
        activebackground="#333",
        relief="flat",
        padx=10,
        pady=5,
        cursor="hand2"
    )

def styled_label(root, text, font=styles.FONT_SUBTITLE, color="black"):
    return tk.Label(
        root,
        text=text,
        font=font,
        bg=styles.BG_COLOR,
        fg=color,
        wraplength=500,
        justify="center"
    )
