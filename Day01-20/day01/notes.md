# Day 01 — Intro to Python

## 1. Topic Explanation

Python is a **high-level, general-purpose programming language**. "High-level" means you don't have to write in the machine's raw 0s and 1s — you write code that reads almost like plain English, and Python translates it into instructions the machine understands.

There are two broad categories of languages:

- **Compiled languages** (C, C++): You write the entire program first, then a **compiler** translates the whole thing at once into an executable file. Only after that do you run it. If there's a mistake anywhere, it's usually caught before the program ever runs.
- **Interpreted languages** (Python): Different story. The Python **interpreter** reads your code **line by line** and executes each line as it reads it. That's why you can write a Python script and run it immediately — there's no separate compile step.

This is what makes Python:
- Easy to learn (syntax stays close to English)
- Fast to prototype with
- "Batteries included" — a huge standard library ships with it out of the box

**How to run Python:**
1. Download the latest version from python.org
2. Check the install with `python --version` in your terminal
3. Two ways to run code:
   - **REPL / Interactive mode**: type `python` in a terminal and you get a `>>>` prompt. Great for quick one-off testing.
   - **Script mode**: write a `.py` file and run it with `python filename.py`. This is how real projects work.

**Comments** — notes in your code that the interpreter ignores:
- Single line: `# this is a comment`
- Multi-line / docstring: a block wrapped in `""" ... """`

## 2. Real-World Analogy

Think of a **translator standing next to you in a restaurant**:

- **Compiled language** = You write your entire order in advance, hand it to a translator, and they translate the whole thing before the waiter ever sees it. Cooking only starts once the full translation is done.
- **Interpreted language (Python)** = The translator is translating each sentence in real time as you speak to the waiter. You say "I want water," it gets translated and sent immediately. If your next sentence has a mistake, only that sentence causes a problem — everything before it already went through.

That's why in Python, a script can run fine up to a certain line and then fail — the interpreter never checked the whole file up front.

## 3. Code Walkthrough

```python
# hello.py — Day 1 first program

# 1. print() — displays output on the screen
print("Hello, Python world!")

# 2. Variable — a name that stores a value
name = input("Enter your name: ")

# 3. f-string — inject a variable's value into a string
print(f"Hello, {name}! Welcome to Day 1 of Python 100 Days.")

# 4. Multiple variables, different data types
age = 21          # int
city = "Coimbatore"   # str
is_learning = True    # bool

print(f"{name} is {age} years old, lives in {city}. Learning Python: {is_learning}")
```

**Line by line:**

1. `# hello.py — Day 1 first program` — a comment; the interpreter ignores it. Just for readability.
2. `print("Hello, Python world!")` — `print()` is a **built-in function**. Whatever you pass it gets shown on screen.
3. `name = input("Enter your name: ")` — `input()` reads text typed by the user. `=` (assignment) stores the value in a variable called `name`.
4. `print(f"Hello, {name}! ...")` — the `f` prefix marks an **f-string**. `{name}` gets replaced with the current value of the `name` variable automatically.
5. `age = 21`, `city = "Coimbatore"`, `is_learning = True` — three different **data types**: `int` (whole number), `str` (text), `bool` (True/False).
6. Final `print()` — combines multiple variables into one f-string.

## 4. Key Takeaways
- Python is an **interpreted** language — it executes line by line
- `print()` for output, `input()` for taking input
- Variables don't need an explicit type declaration (dynamically typed)
- `#` for single-line comments, `""" """` for multi-line
- f-strings (`f"..."`) are the cleanest way to embed variables in a string
