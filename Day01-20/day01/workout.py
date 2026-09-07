"""
Day 01 - Practice Workout
Exercises 1-3 + Mini Project. Try each one yourself FIRST (write your own
version above the solution), then compare with the solution given.
"""

# ---------------------------------------------------------------------------
# Exercise 1: Print your name, age, and city using variables
# ---------------------------------------------------------------------------
# TODO: create variables my_name, my_age, my_city and print them in one
# sentence using an f-string.

# Solution:
my_name = "Jameal"
my_age = 21
my_city = "Coimbatore"
print(f"My name is {my_name}, I am {my_age} years old, and I live in {my_city}.")


# ---------------------------------------------------------------------------
# Exercise 2: Take two numbers as input and print their sum
# ---------------------------------------------------------------------------
# TODO: use input() to take two numbers (remember input() returns a string,
# so convert with int() or float()), then print the sum.

# Solution:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum of {num1} and {num2} is {num1 + num2}")


# ---------------------------------------------------------------------------
# Exercise 3: Take the user's name and print it in reverse
# ---------------------------------------------------------------------------
# TODO: use input() to get a name, then reverse it using string slicing
# ([::-1]) and print it.

# Solution:
user_name = input("Enter your name: ")
reversed_name = user_name[::-1]
print(f"Reversed: {reversed_name}")


# ---------------------------------------------------------------------------
# Mini Project: Greeting Card Generator
# ---------------------------------------------------------------------------
# Ask the user for their name and an occasion (birthday, farewell, etc.),
# then print a nicely formatted greeting card using those values.

def generate_greeting_card():
    name = input("Enter the person's name: ")
    occasion = input("Enter the occasion (e.g. Birthday, Farewell): ")

    card = f"""
    *********************************
    *   Happy {occasion}, {name}!
    *   Wishing you all the best today
    *   and always. - From Python 100 Days
    *********************************
    """
    print(card)


if __name__ == "__main__":
    generate_greeting_card()
