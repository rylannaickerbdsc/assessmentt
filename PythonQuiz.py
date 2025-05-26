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
        return False, "You must be at least 16 years old."

# Get date of birth
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
allowed, message = is_age_16_or_older(dob_input)
print(message)

# Only run quiz if age is 16 or older
if allowed:
    score = 0

    print("\n1. What does a red traffic light mean?")
    print("A. Stop")
    print("B. Go")
    answer = input("Your answer: ").upper()
    if answer == "A":
        score += 1

    print("\n2. What should you do at a stop sign?")
    print("A. Slow down")
    print("B. Stop completely")
    answer = input("Your answer: ").upper()
    if answer == "B":
        score += 1

    print("\nYou got", score, "out of 2 correct.")