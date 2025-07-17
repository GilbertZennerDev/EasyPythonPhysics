# Stage 3: Making Decisions
# Learning: if/elif/else statements, comparisons, boolean logic

# Get user information
name = input("What's your name? ")
age = int(input("How old are you? "))

# Age-based decisions
print(f"Hello, {name}!")

if age < 13:
    print("You're a kid! 🧒")
    activity = "play with toys"
elif age < 18:
    print("You're a teenager! 🧑")
    activity = "study hard"
elif age < 65:
    print("You're an adult! 🧑‍💼")
    activity = "work and enjoy life"
else:
    print("You're a senior! 👴")
    activity = "relax and share wisdom"

print(f"At your age, you might like to {activity}.")

# Simple grade calculator
score = float(input("What's your test score (0-100)? "))

if score >= 90:
    grade = "A"
    message = "Excellent work! 🌟"
elif score >= 80:
    grade = "B"
    message = "Great job! 👍"
elif score >= 70:
    grade = "C"
    message = "Good effort! 👌"
elif score >= 60:
    grade = "D"
    message = "You can do better! 💪"
else:
    grade = "F"
    message = "Let's study more! 📚"

print(f"Your grade is {grade}. {message}")
