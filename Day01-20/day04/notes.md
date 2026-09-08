# Day 04 — Loops (for and while)

## 1. Topic Explanation

Everything we've written so far executed each line exactly once. Often you need to repeat the same task multiple times — that's what **loops** are for. Python has two main loop types.

**`for` loop** — use when you already know how many times you need to repeat, or you're iterating over a sequence (list, range, string):

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4
```

`range(5)` produces `0, 1, 2, 3, 4` — 5 numbers, starting at 0, stopping before 5 (the stop value is exclusive). `i` holds the current number on each iteration.

**`while` loop** — use when you don't know in advance how many times to repeat; it keeps running **while a condition stays true**, and stops the moment the condition becomes false:

```python
count = 0
while count < 5:
    print(count)
    count += 1   # IMPORTANT - without this, infinite loop
```

**Important warning:** in a `while` loop, something inside the loop body must eventually make the condition `False` (here, `count += 1`). Forget that, and you get an **infinite loop** — the program never stops, and it can pin the CPU at 100% or hang the whole process. This is a real production hazard: an accidental infinite loop can take down a server.

**`break` and `continue`:**
- `break` — stops the loop immediately, skipping any remaining iterations
- `continue` — skips the rest of the current iteration and jumps to the next one

**`range()` variants:** `range(start, stop)` and `range(start, stop, step)` are both valid — `range(1, 11)` gives 1 through 10, `range(0, 10, 2)` gives 0, 2, 4, 6, 8 (step of 2).

## 2. Real-World Analogy

**`for` loop** = an attendance register — you already know there are 30 students in the class, so `for student in class_list:` calls each name in turn. You know the count upfront.

**`while` loop** = entering a password at an ATM — "keep asking until the password is correct." You don't know in advance how many attempts it'll take; the loop continues until the condition (password correct?) is satisfied.

## 3. Code Walkthrough

See `examples.py` — sum of 1 to 10 with a `for` loop, a countdown with a `while` loop, and finding the first number divisible by 7 using `break`.

## 4. Key Takeaways

- `for` loop — when you already know how many times to repeat (iterating over a sequence/range)
- `while` loop — repeats while a condition stays true, useful when the repeat count isn't known in advance
- A `while` loop needs something in its body that eventually makes the condition `False`, or you get an infinite loop
- `break` stops the loop immediately; `continue` skips to the next iteration
- `range(start, stop, step)` — `stop` is exclusive; `start` and `step` are optional

## 5. Practice Workout

See `workout.py` — Multiplication Table Generator: takes a number and prints its multiplication table from 1 to 10 using a `for` loop.
