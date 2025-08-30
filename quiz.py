import json, os, random, tkinter as tk
from tkinter import messagebox
from UI import styles, widgets

DATA_FOLDER = "data"
QUESTIONS_FILE = os.path.join(DATA_FOLDER, "questions.json")
HIGHSCORES_FILE = os.path.join(DATA_FOLDER, "highscores.json")

# Load questions
with open(QUESTIONS_FILE, "r") as f:
    QUESTIONS = json.load(f)

# Load highscores
if os.path.exists(HIGHSCORES_FILE):
    with open(HIGHSCORES_FILE, "r") as f:
        HIGHSCORES = json.load(f)
else:
    HIGHSCORES = []

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Quiz Game")
        self.root.geometry("700x500")
        self.root.configure(bg=styles.BG_COLOR)

        self.player_name = ""
        self.difficulty = "easy"
        self.score = 0
        self.current_q = 0
        self.quiz = []
        self.time_left = 15
        self.timer_id = None

        self.build_start_screen()

    # ---------- Start Screen ---------- #
    def build_start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        widgets.styled_label(self.root, "Welcome to the Quiz Game 🎉", styles.FONT_TITLE).pack(pady=20)

        widgets.styled_label(self.root, "Enter your name:").pack()
        self.name_entry = tk.Entry(self.root, font=styles.FONT_SUBTITLE, width=25)
        self.name_entry.pack(pady=10)

        widgets.styled_label(self.root, "Choose Difficulty:").pack()
        self.difficulty_var = tk.StringVar(value="easy")
        tk.OptionMenu(self.root, self.difficulty_var, "easy", "medium", "hard").pack(pady=10)

        widgets.styled_button(self.root, "Start Quiz", self.start_quiz, styles.PRIMARY_COLOR).pack(pady=20)

    # ---------- Start Quiz ---------- #
    def start_quiz(self):
        self.player_name = self.name_entry.get()
        self.difficulty = self.difficulty_var.get()

        if not self.player_name.strip():
            messagebox.showerror("Error", "Please enter your name!")
            return

        self.quiz = QUESTIONS[self.difficulty]
        random.shuffle(self.quiz)
        self.score = 0
        self.current_q = 0
        self.show_question()

    # ---------- Show Question ---------- #
    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_q >= len(self.quiz):
            self.end_quiz()
            return

        q = self.quiz[self.current_q]

        widgets.styled_label(self.root, f"Question {self.current_q+1}/{len(self.quiz)}", styles.FONT_SUBTITLE).pack(pady=10)
        widgets.styled_label(self.root, q["question"], styles.FONT_TITLE).pack(pady=20)

        for option in q["options"]:
            widgets.styled_button(self.root, option, lambda opt=option[0]: self.check_answer(opt), styles.SECONDARY_COLOR).pack(pady=5)

        self.timer_label = widgets.styled_label(self.root, f"⏳ Time Left: {self.time_left}s", styles.FONT_SUBTITLE, "red")
        self.timer_label.pack(pady=10)

        widgets.styled_label(self.root, f"Score: {self.score}", styles.FONT_SUBTITLE).pack(side="bottom", pady=10)

        self.start_timer()

    # ---------- Timer ---------- #
    def start_timer(self):
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"⏳ Time Left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up!", "You ran out of time!")
            self.current_q += 1
            self.show_question()

    # ---------- Check Answer ---------- #
    def check_answer(self, chosen):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        correct = self.quiz[self.current_q]["answer"]
        if chosen == correct:
            self.score += 1

        self.current_q += 1
        self.show_question()

    # ---------- End Quiz ---------- #
    def end_quiz(self):
        global HIGHSCORES
        HIGHSCORES.append({"name": self.player_name, "score": self.score, "difficulty": self.difficulty})
        HIGHSCORES = sorted(HIGHSCORES, key=lambda x: x["score"], reverse=True)[:5]

        with open(HIGHSCORES_FILE, "w") as f:
            json.dump(HIGHSCORES, f, indent=2)

        for widget in self.root.winfo_children():
            widget.destroy()

        widgets.styled_label(self.root, f"🎉 Well done {self.player_name}!", styles.FONT_TITLE).pack(pady=20)
        widgets.styled_label(self.root, f"Your Final Score: {self.score}", styles.FONT_SUBTITLE).pack(pady=10)

        widgets.styled_label(self.root, "🏆 Leaderboard:", styles.FONT_TITLE).pack(pady=10)
        for i, entry in enumerate(HIGHSCORES, start=1):
            widgets.styled_label(self.root, f"{i}. {entry['name']} - {entry['score']} ({entry['difficulty']})", styles.FONT_SUBTITLE).pack()

        widgets.styled_button(self.root, "Play Again", self.build_start_screen, styles.SECONDARY_COLOR).pack(pady=15)
        widgets.styled_button(self.root, "Exit", self.root.quit, styles.ERROR_COLOR).pack()
