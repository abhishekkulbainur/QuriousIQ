class Theme:
    def __init__(self, mode="light"):
        if mode.lower() == "dark":
            self.bg = "#1e1e1e"
            self.fg = "#ffffff"
            self.card_bg = "#2d2d2d"
            self.input_bg = "#3c3c3c"
            self.accent = "#4cafef"
            self.accent_dark = "#3793c9"
        else:  # light mode
            self.bg = "#f5f5f5"
            self.fg = "#222222"
            self.card_bg = "#ffffff"
            self.input_bg = "#eeeeee"
            self.accent = "#0078d7"
            self.accent_dark = "#005a9e"
