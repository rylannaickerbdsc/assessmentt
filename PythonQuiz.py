from datetime import datetime

def is_age_16_or_older(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD."

    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    if age >= 16:
        return True, "You are 16 or older."
    else:
        return False, "You must be at least 16 years old to take the quiz."

def get_user_input(prompt, options):
    while True:
        answer = input(prompt).strip().upper()
        if answer in options:
            return answer
        print(f"Invalid input. Please enter one of {', '.join(options)}.")

def run_quiz():
    questions = [
        {
            "question": "1. What does a red traffic light mean?",
            "options": {"A": "Stop", "B": "Go"},
            "correct": "A"
        },
        {
            "question": "2. What should you do at a stop sign?",
            "options": {"A": "Slow down", "B": "Stop completely"},
            "correct": "B"
        },
        {
            "question": "3. When is it legal to use a mobile phone while driving?",
            "options": {"A": "When using hands-free equipment", "B": "When you're driving slowly"},
            "correct": "A"
        },
        {
            "question": "4. What does a yellow traffic light mean?",
            "options": {"A": "Speed up to beat the red", "B": "Prepare to stop"},
            "correct": "B"
        },
        {
            "question": "5. What must you do when you hear a siren coming from an emergency vehicle?",
            "options": {"A": "Continue driving normally", "B": "Pull over and stop"},
            "correct": "B"
        }
    ]

    score = 0
    for q in questions:
        print(f"\n{q['question']}")
        for key, value in q["options"].items():
            print(f"{key}. {value}")
        answer = get_user_input("Your answer: ", q["options"].keys())
        if answer == q["correct"]:
            score += 1