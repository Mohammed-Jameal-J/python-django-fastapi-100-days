# Day 02 — Variables, Operators & Expressions

## 1. Topic Explanation (Tanglish)

Day 1-la variables create panradhu, print/input use panradhu paathom. Ippo andha variables-ah vachi operations eppadi pannuradhu nu paakalaam.

**Arithmetic operators** — calculation panna:

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division (always float result) | `5 / 2 = 2.5` |
| `//` | Floor division (whole number, decimal cut) | `5 // 2 = 2` |
| `%` | Modulus (remainder) | `5 % 2 = 1` |
| `**` | Exponent (power) | `5 ** 2 = 25` |

`/` and `//`-ku difference romba per confuse aaguvanga: `5 / 2` always float kudukkum (`2.5`), `5 // 2` decimal part cut panni whole number kudukkum (`2`). `%` (modulus) oru number odd-a even-a check panna romba use aagum.

**Comparison operators** — rendu values compare panna, result eppovume `True`/`False` (`bool`): `==`, `!=`, `>`, `<`, `>=`, `<=`.

**Important:** `=` (assignment) vs `==` (comparison) — vera vera. `if age = 18` error kudukkum, `if age == 18` dhaan correct.

**Logical operators** — multiple conditions combine panna: `and` (rendும் true), `or` (edhavadhu ondru true), `not` (reverse).

**Operator precedence** — BODMAS madhiri: `**` first, apparam `* / // %`, apparam `+ -`, apparam comparisons, last `and/or`. Confusion irundha `()` vachi group pannikonga.

## 2. Real-World Analogy

Grocery bill calculator: `price * quantity` (arithmetic) → total calculate panna. `total >= 500` (comparison) → free delivery eligible-a check panna. `total >= 500 and is_member == True` (logical) → rendும் satisfy aaganum-a check panna.

Club bouncer: `age >= 18 and has_valid_id == True` — rendும் true-va irundhaal mattum entry.

## 3. Code Walkthrough (`examples.py`)

See `examples.py` in this folder — bill calculation with arithmetic operators, free-delivery eligibility with comparison + logical operators, and floor division/modulus for splitting items into boxes.

## 4. Key Takeaways

- Arithmetic: `+ - * / // % **` — know the difference between `/` and `//`
- Comparison: `== != > < >= <=` — result is always a `bool`
- Logical: `and`, `or`, `not` — combine multiple conditions
- `=` is assignment, `==` is comparison — never confuse them
- Use `()` to make operator precedence explicit when in doubt

## 5. Practice Workout

See `workout.py` — Movie Ticket Eligibility Checker (comparison + logical operators).
