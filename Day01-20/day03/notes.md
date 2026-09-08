# Day 03 — Branching / Conditional Statements

## 1. Topic Explanation

So far, the code we've written ran top to bottom in a straight line. Real applications need **decision points**: "if this is true, do this, otherwise do that." That's what `if`, `elif`, and `else` are for.

```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if the first condition was False and this one is True
else:
    # runs if none of the above were True
```

Key points:

- **Indentation matters.** Python doesn't use `{}` curly braces like many other languages — indentation (usually 4 spaces) is what defines a block. Code under an `if` must be consistently indented, or you get an `IndentationError`.
- **`elif`** means "else if." You can chain as many as you need; Python checks them top to bottom and runs the block for the **first** condition that's `True`, skipping the rest.
- **`else`** is optional and takes no condition — it means "if nothing above matched, run this."
- A colon `:` is required at the end of every `if`/`elif`/`else` line. Forgetting it is a `SyntaxError`.

**Note:** Once a condition matches in an `if`/`elif` chain, Python does **not** re-check the earlier conditions — it just runs that one block and moves on, even if a later condition would also technically be true.

## 2. Real-World Analogy

A traffic signal:

```python
if signal_color == "red":
    print("Stop")
elif signal_color == "yellow":
    print("Slow down")
else:
    print("Go")
```

Only one of these applies at a time — a driver reacts to whichever color is currently showing, not all of them at once. That's exactly how `if/elif/else` works.

## 3. Code Walkthrough

See `examples.py` — an age classifier using chained `if/elif/else`.

## 4. Key Takeaways

- `if` / `elif` / `else` are checked top to bottom; the first matching condition runs, the rest are skipped
- Indentation defines a block in Python — it's mandatory, not just style
- Every `if`/`elif`/`else` line needs a trailing colon `:`
- `else` takes no condition — it's the catch-all

## 5. Practice Workout

See `workout.py` — Simple Grading System: takes marks (0-100) and prints a letter grade using `if/elif/else`.
