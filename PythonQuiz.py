import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
import os

# Quiz questions
questions = [
    {
        "question": "Does the driver of the blue car have to give way?",
        "options": ["Yes", "No"],
        "answer": "No",
        "image": "bluecargiveway1.png"
    },
    {
        "question": "What does this sign mean?",
        "options": ["Keep Left", "Turn Left","U-Turn"],
        "answer": "Keep Left",
        "image": "keepleftsign.png"
        
    },
    {
        "question": "How many standard drinks can you have before driving if you are under 20 years old?",
        "options": ["One", "Two","Three","None"],
        "answer": "None"
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

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Driver Safety Quiz")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.score = 0
        self.question_index = 0
        self.tk_image = None  # Keep reference to prevent garbage collection

        self.create_dob_screen()

    def create_dob_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Enter your date of birth", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.root, text="(YYYY-MM-DD)", font=("Helvetica", 10)).pack()

        self.dob_entry = tk.Entry(self.root, font=("Helvetica", 12), width=20)
        self.dob_entry.pack(pady=10)

        tk.Button(self.root, text="Submit", command=self.check_age, font=("Helvetica", 12)).pack(pady=10)

    def check_age(self):
        dob_str = self.dob_entry.get().strip()
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age >= 16:
                self.start_quiz()
            else:
                messagebox.showinfo("Age Restriction", "You must be at least 16 years old to take the quiz.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date in YYYY-MM-DD format.")

    def start_quiz(self):
        self.score = 0
        self.question_index = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()

        # Progress bar
        progress_value = int((self.question_index / len(questions)) * 100)
        self.progress = ttk.Progressbar(self.root, length=400, mode='determinate', maximum=100)
        self.progress['value'] = progress_value
        self.progress.pack(pady=(10, 5))

        if self.question_index < len(questions):
            q = questions[self.question_index]

            tk.Label(self.root, text=f"Question {self.question_index + 1} of {len(questions)}",
                     font=("Helvetica", 12, "italic")).pack(pady=(5, 0))
            tk.Label(self.root, text=q["question"], font=("Helvetica", 13, "bold"),
                     wraplength=400, justify="left").pack(pady=10)

            # Display image if present
            if "image" in q:
                image_path = os.path.join("images", q["image"])
                try:
                    img = Image.open(image_path)
                    img = img.resize((400, 300))
                    self.tk_image = ImageTk.PhotoImage(img)
                    tk.Label(self.root, image=self.tk_image).pack(pady=5)
                except Exception as e:
                    tk.Label(self.root, text="Image could not be loaded.", fg="red").pack()

            self.selected_option = tk.StringVar(value="")

            for option in q["options"]:
                tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option,
                               font=("Helvetica", 12)).pack(anchor="w", padx=20)

            tk.Button(self.root, text="Next", command=self.check_answer, font=("Helvetica", 12)).pack(pady=20)
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
        tk.Label(self.root, text="Quiz Completed!", font=("Helvetica", 16, "bold")).pack(pady=20)
        result_text = f"You scored {self.score} out of {len(questions)}"
        tk.Label(self.root, text=result_text, font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="Retake Quiz", command=self.create_dob_screen, font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 12)).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
