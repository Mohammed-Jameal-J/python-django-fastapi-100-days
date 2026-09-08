"""
Day 03 - Practice Workout

Task: Simple Grading System

Ask the user for their marks (0-100), then use if/elif/else to decide
a letter grade:
  marks >= 90 -> "A"
  marks >= 75 -> "B"
  marks >= 50 -> "C"
  below that  -> "Fail"
Print the result as: Grade: <grade>
"""

mark = int(input("Enter your marks: "))

if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
elif mark >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")
