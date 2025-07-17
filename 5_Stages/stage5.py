# Stage 5: Functions and Lists
# Learning: function definition, parameters, return values, list operations

# Function definitions
def greet_user(name):
    """A friendly greeting function"""
    return f"Hello, {name}! Welcome to Python! 🐍"

def calculate_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    return area

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def find_largest(numbers):
    """Find the largest number in a list"""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Using functions
print("🎯 Function Practice!")

# Greeting example
user_name = input("What's your name? ")
greeting = greet_user(user_name)
print(greeting)

# Area calculator
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = calculate_area(length, width)
print(f"The area is {area} square units.")

# Even/odd checker
number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")

# List operations
print("\n📝 Working with Lists:")
my_scores = []

# Adding scores
for i in range(3):
    score = float(input(f"Enter score {i+1}: "))
    my_scores.append(score)

# List analysis
print(f"Your scores: {my_scores}")
print(f"Highest score: {find_largest(my_scores)}")
print(f"Average score: {sum(my_scores) / len(my_scores):.2f}")

# Shopping list manager
shopping_list = ["milk", "bread", "eggs"]
print(f"\nCurrent shopping list: {shopping_list}")

while True:
    action = input("Add item (a), remove item (r), or quit (q)? ").lower()
    
    if action == 'a':
        item = input("What item to add? ")
        shopping_list.append(item)
        print(f"Added {item}. List: {shopping_list}")
    elif action == 'r':
        item = input("What item to remove? ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed {item}. List: {shopping_list}")
        else:
            print(f"{item} not found in list.")
    elif action == 'q':
        print("Final shopping list:", shopping_list)
        break
    else:
        print("Invalid option. Try again.")
