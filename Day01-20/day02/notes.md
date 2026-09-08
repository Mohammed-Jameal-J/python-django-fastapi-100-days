# Day 02 — Variables, Operators & Expressions

## 1. Topic Explanation

Day 1 covered creating variables and using print/input. Now let's look at how to perform operations on those variables.

**Arithmetic operators** — for calculations:

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division (always returns a float) | `5 / 2 = 2.5` |
| `//` | Floor division (whole number, decimal dropped) | `5 // 2 = 2` |
| `%` | Modulus (remainder) | `5 % 2 = 1` |
| `**` | Exponent (power) | `5 ** 2 = 25` |

The difference between `/` and `//` trips up a lot of beginners: `5 / 2` **always** returns a float (`2.5`), while `5 // 2` drops the decimal part and returns a whole number (`2`). `%` (modulus) is very useful for checking whether a number is odd or even — an even number always gives `0` when you do `% 2`.

**Comparison operators** — compare two values, the result is always `True` or `False` (a `bool`): `==`, `!=`, `>`, `<`, `>=`, `<=`.

**Important:** `=` and `==` are completely different. `=` is **assignment** (storing a value), `==` is **comparison** (checking equality). This is a very common beginner mistake — `if age = 18` throws an error in Python, `if age == 18` is correct.

**Logical operators** — combine multiple conditions: `and`, `or`, `not`.

- `age >= 18 and has_id == True` — only overall `True` if **both** are true
- `is_weekend or is_holiday` — overall `True` if **either** is true

**Operator precedence** — similar to the BODMAS/PEMDAS rules from school: `**` first, then `* / // %`, then `+ -`, then comparison operators, and `and`/`or` last. When in doubt, use `()` to make the order explicit — it's the safest option.

## 2. Real-World Analogy

Think of a **grocery bill calculator**:
- `price * quantity` → an arithmetic operator used to calculate the total
- `total >= 500` → a comparison operator, checking "is this eligible for free delivery?"
- `total >= 500 and is_member == True` → a logical operator, checking "does it need free delivery eligibility **AND** membership status?"

Or a club bouncer: `age >= 18 and has_valid_id == True` — both conditions need to be satisfied before entry is allowed.

## 3. Code Walkthrough

See `examples.py` in this folder — bill calculation with arithmetic operators, free-delivery eligibility with comparison + logical operators, and floor division/modulus for splitting items into boxes.

## 4. Key Takeaways

- Arithmetic: `+ - * / // % **` — know the difference between `/` and `//`
- Comparison: `== != > < >= <=` — the result is always a `bool`
- Logical: `and`, `or`, `not` — combine multiple conditions
- `=` is assignment, `==` is comparison — never confuse them
- Use `()` to make operator precedence explicit when in doubt

## 5. Practice Workout

See `workout.py` — Movie Ticket Eligibility Checker (comparison + logical operators).
