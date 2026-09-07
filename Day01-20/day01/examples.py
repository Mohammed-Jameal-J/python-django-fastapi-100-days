"""
Day 01 - Intro to Python
Examples file: run this to see Day 1 concepts in action.
"""

# 1. print() function - screen-la output kaamikka use pannuvom
print("Vanakkam, Python world!")

# 2. Variable - oru value-ah store panna oru "peru" (name) kudukkarom
name = input("Enter your name: ")

# 3. f-string - variable value-ah string-oda inject panna
print(f"Vanakkam, {name}! Welcome to Day 1 of Python 100 Days.")

# 4. Multiple variables, different data types
age = 21                # int
city = "Coimbatore"      # str
is_learning = True       # bool

print(f"{name} is {age} years old, lives in {city}. Learning Python: {is_learning}")

# 5. type() function - oru variable-oda data type check panna
print(type(age), type(city), type(is_learning))

# 6. Comments demo
# Idhu single-line comment
"""
Idhu oru
multi-line comment / docstring
"""
