"""
Day 02 - Practice Workout

Task: Movie Ticket Eligibility Checker

Ask the user for their age and whether they already have a ticket
(input "yes"/"no"). A person is allowed entry only if they are 18 or
older AND they already have a ticket. Print True/False for entry allowed,
using comparison and logical operators (no if-statements yet - that's Day 3).
"""

age = int(input("Enter your age: "))
has_ticket_input = input("Do you have a ticket? (yes/no): ")

has_ticket = has_ticket_input.lower() == "yes"
entry_allowed = age >= 18 and has_ticket

print(f"Entry allowed: {entry_allowed}")
