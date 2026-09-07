"""
Day 02 - Variables, Operators & Expressions
Examples file: run this to see Day 2 concepts in action.
"""

# 1. Arithmetic operators - grocery bill calculation
price = 250
quantity = 3
total = price * quantity
print(f"Total bill: {total}")

# 2. Comparison + logical operators - free delivery eligibility
is_member = True
free_delivery_eligible = total >= 500 and is_member == True
print(f"Free delivery eligible: {free_delivery_eligible}")

# 3. Floor division and modulus - splitting items into boxes
items = 17
box_capacity = 5
full_boxes = items // box_capacity        # how many FULL boxes
leftover_items = items % box_capacity      # items left over
print(f"Full boxes: {full_boxes}, leftover items: {leftover_items}")

# 4. Operator precedence demo
result = 2 + 3 * 4 ** 2   # ** first (16), then * (48), then + (50)
print(f"2 + 3 * 4 ** 2 = {result}")
