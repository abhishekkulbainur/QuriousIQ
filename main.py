import tkinter as tk
import json
from UI.styles import LIGHT_THEME, DARK_THEME, apply_theme


def load_config():
    with open("data/config.json", "r") as f:
        return json.load(f)


def main():
    config = load_config()
    theme_choice = config.get("theme", "light").lower()

    root = tk.Tk()
    root.title("Python Quiz Game")
    root.geometry("600x400")

    # Apply theme
    if theme_choice == "dark":
        apply_theme(root, DARK_THEME)
    else:
        apply_theme(root, LIGHT_THEME)

    label = tk.Label(root, text="Hello! Tkinter is working 🚀", font=("Arial", 18))
    label.pack(pady=50)

    root.mainloop()


if __name__ == "__main__":
    main()
