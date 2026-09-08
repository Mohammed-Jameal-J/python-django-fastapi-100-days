"""
Day 03 - Branching / Conditional Statements
Examples file: run this to see Day 3 concepts in action.
"""

age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"You are classified as: {category}")
