"""
Day 04 - Practice Workout

Task: Multiplication Table Generator

Ask the user for a number, then use a for loop to print its
multiplication table from 1 to 10:
  n x 1 = ...
  n x 2 = ...
  ...
  n x 10 = ...
"""

user = int(input("Enter the number: "))
for n in range(1, 11):
    print(f"{user} x {n} = {user * n}")
