import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("System")        # light / dark / system
ctk.set_default_color_theme("dark-blue")  # theme pack

questions = [
    {
        "question": "Does the driver of the blue car have to give way?",
        "options": ["Yes", "No"],
        "answer": "No",
        "image": "question1.png"
    },
    {
        "question": "What does this sign mean?",
        "options": ["Keep Left", "Turn Left","U-Turn"],
        "answer": "Keep Left",
        "image": "question2.png"
        
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


class QuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Driver Safety Quiz")
        self.geometry("600x700")
        self.score = 0
        self.qi = 0
        self.img_ref = None
        self.create_dob()

    def create_dob(self):
        self.clear()
        self.dob = ctk.CTkEntry(self, placeholder_text="YYYY-MM-DD", width=200)
        self.dob.pack(pady=40)
        ctk.CTkButton(self, text="Start Quiz", command=self.check_age).pack(pady=20)

    def check_age(self):
        try:
            dob = datetime.strptime(self.dob.get(), "%Y-%m-%d")
            age = (datetime.today().year - dob.year) - ((datetime.today().month, datetime.today().day) < (dob.month, dob.day))
            if age >= 16:
                self.score = 0
                self.qi = 0
                self.show_q()
            else:
                messagebox.showinfo("Oops", "You must be 16+")
        except:
            messagebox.showerror("Invalid", "Use YYYY-MM-DD")

    def show_q(self):
        self.clear()
        q = questions[self.qi]
        ctk.CTkLabel(self, text=f"Question {self.qi+1}/{len(questions)}", font=("sans", 14)).pack(pady=10)
        bar = ctk.CTkProgressBar(self, width=500)
        bar.set(self.qi / len(questions))
        bar.pack(pady=(0,15))

        ctk.CTkLabel(self, text=q["question"], font=("sans", 16, "bold"), wraplength=550).pack(pady=10)

        if "image" in q:
            p = os.path.join("images", q["image"])
            try:
                im = Image.open(p).resize((500,300), Image.LANCZOS)
                self.img_ref = ImageTk.PhotoImage(im)
                ctk.CTkLabel(self, image=self.img_ref).pack(pady=10)
            except:
                ctk.CTkLabel(self, text="Image load failed", text_color="red").pack()

        self.var = ctk.StringVar(value="")  # initialize empty value
        for opt in q["options"]:
            ctk.CTkRadioButton(self, text=opt, variable=self.var, value=opt).pack(anchor="w", padx=50, pady=5)

        ctk.CTkButton(self, text="Next", command=self.process).pack(pady=20)

    def process(self):
        if self.var.get() == "":
            messagebox.showwarning("Pick one", "Select an option")
            return
        if self.var.get() == questions[self.qi]["answer"]:
            self.score += 1
        self.qi += 1
        if self.qi < len(questions):
            self.show_q()
        else:
            self.show_res()

    def show_res(self):
        self.clear()
        ctk.CTkLabel(self, text="Quiz Complete!", font=("sans", 20, "bold")).pack(pady=30)
        ctk.CTkLabel(self, text=f"Score: {self.score}/{len(questions)}", font=("sans", 18)).pack(pady=10)

        # Restart quiz by resetting the state and showing the DOB screen again
        ctk.CTkButton(self, text="Restart", command=self.restart_quiz).pack(pady=10)
        ctk.CTkButton(self, text="Exit", command=self.destroy).pack(pady=5)

    def restart_quiz(self):
        self.score = 0
        self.qi = 0
        self.create_dob()

    def clear(self):
        for w in self.winfo_children():
            w.destroy()

if __name__=="__main__":
    os.makedirs("images", exist_ok=True)
    app = QuizApp()
    app.mainloop()
