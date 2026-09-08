"""
Day 04 - Loops (for and while)
Examples file: run this to see Day 4 concepts in action.
"""

# for loop - sum of numbers 1 to 10
total = 0
for num in range(1, 11):
    total += num
print(f"Sum of 1 to 10: {total}")

# while loop - countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# for loop with break - find first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break
