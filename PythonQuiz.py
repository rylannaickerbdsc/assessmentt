from datetime import datetime

def is_age_16_or_older(dob_str):
    """Check if the user is at least 16 years old."""
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD."

    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    if age >= 16:
        return True, "You are 16 or older."
    else:
        return False, "You must be at least 16 years old to continue."

# Get date of birth
dob_input = input("Enter your date of birth (YYYY-MM-DD): ").strip()
allowed, message = is_age_16_or_older(dob_input)
print(message)

# Only run quiz if age is 16 or older
if allowed:
    score = 0
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
        }
    ]

    for q in questions:
        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"{key}. {value}")

        # Keep asking until a valid answer is entered
        while True:
            answer = input("Your answer (A or B): ").strip().upper()
            if answer in q["options"]:
                break
            else:
                print("Invalid option. Please enter A or B.")

        if answer == q["correct"]:
            score += 1

    print(f"\nYou got {score} out of {len(questions)} correct.")