# Stage 4: Loops and Repetition
# Learning: for loops, while loops, range(), patterns

print("🔄 Welcome to the Loop Zone!")

# Simple counting with for loop
print("\nCounting to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# Creating patterns
print("\nLet's make a pattern:")
for i in range(1, 6):
    print("⭐" * i)

# Working with lists
fruits = ["apple", "banana", "orange", "grape"]
print("\nMy favorite fruits:")
for fruit in fruits:
    print(f"I love {fruit}! 🍎")

# Interactive loop
print("\nGuess the magic number!")
magic_number = 7
guess = 0

while guess != magic_number:
    guess = int(input("Guess a number (1-10): "))
    
    if guess < magic_number:
        print("Too low! Try again.")
    elif guess > magic_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You found the magic number!")

# Times table
number = int(input("\nWhich times table do you want to see? "))
print(f"\nTimes table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
