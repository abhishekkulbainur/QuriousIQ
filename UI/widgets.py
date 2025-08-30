import tkinter as tk

def title_label(parent, text, theme):
    return tk.Label(
        parent,
        text=text,
        font=("Arial", 22, "bold"),
        fg=theme.fg,
        bg=theme.bg,
        wraplength=700,
        justify="center"
    )

def subtitle_label(parent, text, theme):
    return tk.Label(
        parent,
        text=text,
        font=("Arial", 16, "bold"),
        fg=theme.fg,
        bg=theme.bg,
        wraplength=700,
        justify="center"
    )

def note_label(parent, text, theme):
    return tk.Label(
        parent,
        text=text,
        font=("Arial", 12),
        fg=theme.accent,
        bg=theme.bg,
        wraplength=700,
        justify="center"
    )

def entry_widget(parent, theme):
    return tk.Entry(
        parent,
        font=("Arial", 14),
        fg=theme.fg,
        bg=theme.input_bg,
        insertbackground=theme.fg,
        relief="flat",
        justify="center"
    )

def primary_button(parent, text, theme, command):
    return tk.Button(
        parent,
        text=text,
        font=("Arial", 14, "bold"),
        fg="white",
        bg=theme.accent,
        activebackground=theme.accent_dark,
        activeforeground="white",
        relief="flat",
        padx=10,
        pady=5,
        width=20,
        command=command,
        cursor="hand2"
    )

def secondary_button(parent, text, theme, command):
    return tk.Button(
        parent,
        text=text,
        font=("Arial", 12),
        fg=theme.fg,
        bg=theme.bg,
        activebackground=theme.card_bg,
        activeforeground=theme.accent,
        relief="groove",
        padx=8,
        pady=4,
        width=18,
        command=command,
        cursor="hand2"
    )
