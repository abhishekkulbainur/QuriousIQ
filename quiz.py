import json
import random
import tkinter as tk
from UI.widgets import primary_button, secondary_button, title_label
from UI.styles import apply_theme, LIGHT_THEME, DARK_THEME
from UI.themes import Theme
from UI.sounds import SoundManager
import json

def load_config():
    with open("data/config.json", "r") as f:
        return json.load(f)


# Load data functions
def load_questions():
    with open("data/questions.json", "r") as f:
        return json.load(f)

def load_highscores():
    with open("data/highscores.json", "r") as f:
        return json.load(f)

def save_highscores(scores):
    with open("data/highscores.json", "w") as f:
        json.dump(scores, f, indent=4)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuriousIQ Quiz Game")

        # Load config + theme
        self.config = load_config()
        self.theme = Theme(self.config.get("theme", "light"))
        apply_theme(self.root, LIGHT_THEME if self.config.get("theme") == "light" else DARK_THEME)

        # Sound manager
        self.sound_manager = SoundManager()

        # Load and shuffle questions
        self.questions = load_questions()
        if self.config.get("shuffle_questions", True):
            random.shuffle(self.questions)
        self.current_q_index = 0
        self.score = 0
        self.timer = self.config.get("time_per_question", 15)
        self.timer_id = None

        # UI setup
        self.setup_ui()
        self.show_question()

    def setup_ui(self):
        self.question_label = title_label(self.root, "Question will appear here", self.theme)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = primary_button(self.root, f"Option {i+1}", self.theme, lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5, fill="x", padx=100)
            self.option_buttons.append(btn)

        self.timer_label = title_label(self.root, f"Time left: {self.timer}s", self.theme)
        self.timer_label.pack(pady=10)

        self.next_button = secondary_button(self.root, "Next Question", self.theme, self.next_question)
        self.next_button.pack(pady=20)

    def show_question(self):
        if self.current_q_index < len(self.questions):
            self.timer = self.config.get("time_per_question", 15)
            self.update_timer()

            q = self.questions[self.current_q_index]
            self.question_label.config(text=q["question"])

            options = q["options"][:]
            if self.config.get("shuffle_options", True):
                random.shuffle(options)

            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option, state="normal")

        else:
            self.end_game()

    def check_answer(self, idx):
        q = self.questions[self.current_q_index]
        if self.option_buttons[idx].cget("text") == q["answer"]:
            self.score += 1
            self.sound_manager.play("Assets/correct.mp3")
        else:
            self.sound_manager.play("Assets/wrong.mp3")

        for btn in self.option_buttons:
            btn.config(state="disabled")

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def next_question(self):
        self.current_q_index += 1
        self.show_question()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer}s")
        if self.timer > 0:
            self.timer -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def end_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label(self.root, f"Game Over! Your Score: {self.score}/{len(self.questions)}", self.theme).pack(pady=20)

        highscores = load_highscores()
        highscores.append({"score": self.score})
        highscores = sorted(highscores, key=lambda x: x["score"], reverse=True)[:self.config.get("max_highscores", 10)]
        save_highscores(highscores)

        primary_button(self.root, "Show Highscores", self.theme, self.show_highscores).pack(pady=10)
        primary_button(self.root, "Quit", self.theme, self.root.quit).pack(pady=10)

    def show_highscores(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label(self.root, "🏆 Highscores", self.theme).pack(pady=20)
        highscores = load_highscores()
        highscores = sorted(highscores, key=lambda x: x["score"], reverse=True)[:5]

        for i, entry in enumerate(highscores, 1):
            title_label(self.root, f"{i}. Score: {entry['score']}", self.theme).pack()

        primary_button(self.root, "Back", self.theme, self.root.quit).pack(pady=20)

def start_quiz():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
