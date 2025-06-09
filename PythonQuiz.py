import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Quiz questions
questions = [
    {
        "question": "What does a red traffic light mean?",
        "options": ["Stop", "Go"],
        "answer": "Stop"
    },
    {
        "question": "What should you do at a stop sign?",
        "options": ["Slow down", "Stop completely"],
        "answer": "Stop completely"
    },
    {
        "question": "When is it legal to use a mobile phone while driving?",
        "options": ["When using hands-free equipment", "When you're driving slowly"],
        "answer": "When using hands-free equipment"
    },
    {
        "question": "What does a yellow traffic light mean?",
        "options": ["Speed up to beat the red", "Prepare to stop"],
        "answer": "Prepare to stop"
    },
    {
        "question": "What must you do when you hear a siren from an emergency vehicle?",
        "options": ["Continue driving normally", "Pull over and stop"],
        "answer": "Pull over and stop"
    }
]

# Main App Class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Driver Safety Quiz")
        self.root.geometry("400x300")
        self.score = 0
        self.question_index = 0

        self.create_dob_screen()

    def create_dob_screen(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Enter your date of birth (YYYY-MM-DD):")
        self.label.pack(pady=10)

        self.dob_entry = tk.Entry(self.root)
        self.dob_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_age)
        self.submit_button.pack(pady=10)

    def check_age(self):
        dob_str = self.dob_entry.get()
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age >= 16:
                self.start_quiz()
            else:
                messagebox.showinfo("Age Check", "You must be at least 16 years old to take the quiz.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format.")

    def start_quiz(self):
        self.score = 0
        self.question_index = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()
        if self.question_index < len(questions):
            q = questions[self.question_index]
            self.q_label = tk.Label(self.root, text=q["question"], wraplength=380, justify="left")
            self.q_label.pack(pady=10)

            self.selected_option = tk.StringVar()

            for option in q["options"]:
                rb = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option)
                rb.pack(anchor="w")

            self.next_button = tk.Button(self.root, text="Next", command=self.check_answer)
            self.next_button.pack(pady=10)
        else:
            self.show_result()

    def check_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Selection Required", "Please select an answer before continuing.")
            return

        correct_answer = questions[self.question_index]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.question_index += 1
        self.show_question()

    def show_result(self):
        self.clear_screen()
        result = f"You scored {self.score} out of {len(questions)}"
        result_label = tk.Label(self.root, text=result, font=("Helvetica", 14))
        result_label.pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()