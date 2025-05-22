from datetime import datetime

def is_age_16_or_older(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    if age >= 16:
        return "You are 16 or older."
    else:
        return "You must be at least 16 years old."

# Example usage:
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
result = is_age_16_or_older(dob_input)
print(result)