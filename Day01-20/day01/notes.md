# Day 01 — Intro to Python

## 1. Topic Explanation (Tanglish)

Python nu solra ஒரு **high-level, general-purpose programming language**. High-level nu sonna, machine-oda 0s and 1s language-la nee code eluthanum nu illa — nee almost English madhiri eluthina code-ah, Python andha machine-oda language-ku translate pannikkum.

Rendu vidhamana languages irukku:

- **Compiled languages** (C, C++): Nee full code-ah eluthi mudichathukku aprom, oru **compiler** andha muzhu code-ayum onnaa translate panni, oru `.exe` madhiri executable file create pannum. Apparam dhaan run pannuvom. Edhaavadhu mistake irundha, run pannradhukku munnadiye compile stage-la error varum.
- **Interpreted languages** (Python): Ivlo simple-a illa. Python-oda **interpreter** nee eluthina code-ah, **line by line** padichu, andha nerathulaye run pannikittu poidum. Adhunaala dhaan Python-la code eluthi udane run pannalaam — compile step thevai illa.

Idhu vachu dhaan Python:
- Padikka romba easy (English syntax-ah nerukkama iruku)
- Fast-a prototype pannalaam (web apps, data science, automation, AI — ellaathukkum use aagum)
- "Batteries included" — நிறைய built-in libraries already irukku

**Python install pannradhu எப்படி:**
1. python.org-ல irundhu latest version download pannunga
2. Terminal/CMD-la `python --version` nu type panni check pannunga
3. Rendu vidhama Python run pannalaam:
   - **REPL / Interactive mode**: Terminal-la `python` nu type panna, oru `>>>` prompt varum. Ange line by line command podalaam, udane result kaamikkum. Idhu quick testing-ku nallaadhu.
   - **Script mode**: `.py` extension-la oru file eluthi, `python filename.py` nu run pannuvom. Real projects ellaam idhu madhiri dhaan irukkum.

**Comments** — code-la nama pottukira notes, interpreter idha ignore pannidum:
- Single line: `# idhu comment`
- Multi-line / docstring: `""" ... """` moonu double-quotes-oda block

## 2. Real-World Analogy

Ithu oru **restaurant-la translator** irukkara scene madhiri nினைச்சுக்குங்க:

- **Compiled language** = Nee oru foreign country-ku poi, unnoda full menu order-ah munnadiyே ஒரு translator-kitta kudutha, avaru andha full order-ayum translate panni, waiter-kitta kudukkaraan. Apparam dhaan cooking start aagum. Full translation mudinja aprom dhaan process start.
- **Interpreted language (Python)** = Nee waiter-kitta pேசும்போதே, translator unnoda ஒவ்வொரு வாக்கியத்தையும் **real-time-ல** translate panni sollikittu irukkaru. Nee "I want water" sona udane, andha vaakiyam mattum translate aagi waiter-ku pogum. Adhukkulla unnoda next sentence-ah yosikkalaam.

Athanaala dhaan Python-la, oru line-la mistake irundha, andha line varaikkum run aagum, apparamdhaan error varum — full program-ah first translate pannala.

## 3. Code Walkthrough (`examples.py`)

```python
# hello.py — Day 1 first program

# 1. print() function — screen-la output kaamikka use pannuvom
print("Vanakkam, Python world!")

# 2. Variable — oru value-ah store panna oru "peru" (name) kudukkarom
name = input("Enter your name: ")

# 3. f-string — variable value-ah string-oda inject panna
print(f"Vanakkam, {name}! Welcome to Day 1 of Python 100 Days.")

# 4. Multiple variables, different data types
age = 21          # int
city = "Coimbatore"   # str
is_learning = True    # bool

print(f"{name} is {age} years old, lives in {city}. Learning Python: {is_learning}")
```

**Line by line:**

1. `# hello.py — Day 1 first program` — comment, interpreter ignore pannidum. Just readability-ku.
2. `print("Vanakkam, Python world!")` — `print()` oru **built-in function**. Adhoda arguments (`""`-la irukra string) screen-la output-a kaamikkum.
3. `name = input("Enter your name: ")` — `input()` function user-kitta irundhu keyboard-la irundhu text vaangum. `=` (assignment operator) andha vaangina value-ah `name` nu oru variable-la store pannudhu.
4. `print(f"Vanakkam, {name}! ...")` — `f` prefix vachi eludhina string-ah **f-string** nu solluvom. `{name}` place-la, `name` variable-oda current value automatic-a substitute aagum.
5. `age = 21`, `city = "Coimbatore"`, `is_learning = True` — moonu vera vera **data types**: `int` (whole number), `str` (text, quotes-la irukkum), `bool` (True/False).
6. Last `print()` — multiple variables-ah oru single f-string-la combine panniruken.

## 4. Key Takeaways
- Python **interpreted** language — line by line execute aagum
- `print()` → output kaamikka, `input()` → input vaangikka
- Variables-ku data type declare pannanum nu kட்டாயம் illa (dynamically typed)
- `#` single line comment, `""" """` multi-line
- f-strings (`f"..."`) — variables-ah string-la clean-a embed panna best way
