
age = input("Please enter your age: ")

try:
    age = int(age)
    if age >= 16:
        print("Welcome.")
    else:
        print("You must be at least 16 years old.")
except ValueError:
    print("Please enter a valid number.")