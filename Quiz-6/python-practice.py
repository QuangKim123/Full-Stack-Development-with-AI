# ===============================
# Python Fundamentals Practice
# ===============================

print("=== 1. Variables & Data Types ===")

# Declare variables
age = 20
height = 5.9
name = "Alice"
is_student = True
grades = [85, 90, 78]

# Manipulate variables
print(name, "is", age, "years old.")
print("Average grade:", sum(grades) / len(grades))
print("Is student?", is_student)

# Dynamic typing
age = "twenty"
print("Age is now:", age)   # Notice the type changed!


print("\n=== 2. Conditional Logic ===")

# Ask user input
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Even / Odd check
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


print("\n=== 3. Loops ===")

# For loop
print("Numbers from 1 to 5 (for loop):")
for i in range(1, 6):
    print(i, end=" ")
print()

# While loop
print("Countdown from 5 to 1 (while loop):")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()

# Iterate list
fruits = ["apple", "banana", "orange"]
print("List of fruits:")
for fruit in fruits:
    print("I like", fruit)


print("\n=== 4. Functions ===")

def add_numbers(a, b):
    """Return the sum of two numbers"""
    return a + b

def greet(name, age):
    """Print a greeting with a name and age"""
    print(f"Hello {name}, you are {age} years old.")

# Function calls
print("Sum of 5 and 10:", add_numbers(5, 10))
print("Sum of 2.5 and 3.5:", add_numbers(2.5, 3.5))

greet("Alice", 20)
greet("Bob", 25)


print("\n=== End of Practice Script ===")
