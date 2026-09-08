"""
Day 01 - Intro to Python
Examples file: run this to see Day 1 concepts in action.
"""

# 1. print() - displays output on the screen
print("Hello, Python world!")

# 2. Variable - a name that stores a value
name = input("Enter your name: ")

# 3. f-string - inject a variable's value into a string
print(f"Hello, {name}! Welcome to Day 1 of Python 100 Days.")

# 4. Multiple variables, different data types
age = 21                # int
city = "Coimbatore"      # str
is_learning = True       # bool

print(f"{name} is {age} years old, lives in {city}. Learning Python: {is_learning}")

# 5. type() - check a variable's data type
print(type(age), type(city), type(is_learning))

# 6. Comments demo
# This is a single-line comment
"""
This is a
multi-line comment / docstring
"""
