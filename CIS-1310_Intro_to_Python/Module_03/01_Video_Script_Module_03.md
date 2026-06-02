# Video Script: CIS-1310 — Introduction to Python

## Module 03 — Variables and Basic I/O

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
> - Use screen-share for all [DEMO] sections — run live in Ubuntu terminal/REPL.
> - [PAUSE] = hold 2 seconds of silence.
> - For naming rules, show both valid and invalid examples on screen side-by-side.

---

## [00:00 – 00:45] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 03 | Variables and Basic I/O | CIS-1310"]**

"Welcome back, everyone. We're in Module 03 now, and this is where Python starts to feel like an actual programming language rather than a calculator.

So far you've worked with literal values — you typed `42` or `'Hello'` directly into the REPL and Python gave you the result. But real programs don't work with fixed values — they work with data that changes: a user's name, a temperature reading, a bank balance, a product count. To work with changing data, we need **variables**.

This module covers three tightly connected topics: variables and naming rules, dynamic typing, and basic input and output. These are foundational skills that every single module from here forward depends on. Let's go."

---

## [00:45 – 02:30] What Is a Variable?

**[SHOW SLIDE: "Variables — Named Storage for Values"]**

"A **variable** is a named label that points to a value stored in memory. When you write:

```python
age = 25
```

You are telling Python: 'Create a place in memory to hold the value `25`, and give that place the name `age`.' Now whenever you use `age` in your code, Python looks up what value is stored under that name.

**[DEMO — REPL]**

```python
>>> age = 25
>>> age
25
>>> name = 'Alice'
>>> name
'Alice'
>>> price = 9.99
>>> price
9.99
```

The `=` symbol in Python is the **assignment operator** — it assigns the value on the right to the variable name on the left. This is NOT the same as the `==` equality comparison operator. `=` assigns. `==` compares. Keep that distinction sharp.

You can reassign a variable at any time:

```python
>>> age = 25
>>> age = 30
>>> age
30
```

The old value `25` is gone. `age` now points to `30`. Variables are not permanent — they hold whatever was most recently assigned to them."

---

## [02:30 – 05:00] Variable Naming Rules and PEP 8 Conventions

**[SHOW SLIDE: "Variable Naming — Rules and Conventions"]**

"Python has strict rules for what makes a valid variable name. The PCAP exam will show you names and ask you to identify which are valid. Know these rules cold.

### The Rules (enforced by Python)

**Rule 1:** Names must start with a **letter** (a–z, A–Z) or an **underscore** (`_`). They cannot start with a digit.

```python
>>> my_var = 10    # valid
>>> _hidden = 5    # valid
>>> 2fast = 3      # SyntaxError — starts with a digit
```

**Rule 2:** After the first character, names can contain letters, digits, and underscores. No hyphens, spaces, or special characters.

```python
>>> user_age = 25    # valid — underscore is fine
>>> user-age = 25    # SyntaxError — hyphen is not allowed
>>> user age = 25    # SyntaxError — space is not allowed
```

**Rule 3:** Python is **case-sensitive**. `age`, `Age`, and `AGE` are three completely different variables.

```python
>>> count = 1
>>> Count = 2
>>> COUNT = 3
>>> count
1
>>> Count
2
>>> COUNT
3
```

**Rule 4:** You cannot use Python **reserved keywords** as variable names. Keywords are words Python uses for its own syntax.

**[PAUSE]**

Here are all 35 Python 3 reserved keywords:

```text
False    None     True     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

Try to use `class` or `if` as a variable name and Python will raise a `SyntaxError`.

### PEP 8 Conventions (professional style)

These aren't enforced by Python — they're conventions that professional developers follow:

- Use **snake_case** for variable names: words separated by underscores, all lowercase. Example: `user_age`, `first_name`, `total_price`.
- Use **UPPER_SNAKE_CASE** for constants (values that should not change): `MAX_SIZE = 100`, `PI = 3.14159`.
- Variable names should be **descriptive** — `student_count` is better than `sc` or `n`.
- Avoid single-letter names except for loop counters (`i`, `j`, `k`) or coordinates (`x`, `y`).

The PCAP exam tests both the rules (what Python enforces) and the naming conventions (what PEP 8 recommends)."

---

## [05:00 – 06:30] Dynamic Typing

**[SHOW SLIDE: "Dynamic Typing — Python Determines Types at Runtime"]**

"Python is a **dynamically typed** language. This means you never declare a variable's type. Python determines the type automatically based on the value you assign.

**[DEMO]**

```python
>>> x = 42
>>> type(x)
<class 'int'>
>>> x = 'hello'
>>> type(x)
<class 'str'>
>>> x = 3.14
>>> type(x)
<class 'float'>
```

The same variable `x` holds an `int`, then a `str`, then a `float`. Python never complained. The type of `x` is whatever was most recently assigned to it.

This is different from statically typed languages like Java or C where you write `int x = 42;` — declaring the type at compile time. Once declared, a Java `int` variable cannot hold a string without an explicit cast.

Dynamic typing makes Python flexible and fast to write. But it also means Python won't stop you from accidentally mixing types until the operation actually fails at runtime:

```python
>>> x = '5'
>>> x + 1
TypeError: can only concatenate str (not 'int') to str
```

Python didn't know `x` would be used for arithmetic. It only caught the problem when you actually tried to add an `int` to a `str`. This is the trade-off of dynamic typing — flexibility comes with the responsibility to track your own types."

---

## [06:30 – 07:45] Multiple Assignment and Augmented Assignment

**[SHOW SLIDE: "Multiple Assignment and Augmented Operators"]**

"Python gives you convenient shorthand for several assignment patterns.

**Multiple assignment — assign multiple variables in one line:**

```python
>>> a, b, c = 1, 2, 3
>>> a
1
>>> b
2
>>> c
3
```

The right side is a tuple — Python unpacks it and assigns each value to the corresponding variable. The number of variables must match the number of values.

**Swap two variables without a temp variable:**

```python
>>> x, y = 10, 20
>>> x, y = y, x
>>> x
20
>>> y
10
```

This is a Python idiom — much cleaner than the three-step swap used in C or Java.

**Augmented assignment operators:**

These combine an arithmetic operation with assignment:

```python
>>> count = 0
>>> count += 1       # same as count = count + 1
>>> count
1
>>> count += 5
>>> count
6
>>> count -= 2
>>> count
4
>>> count *= 3
>>> count
12
>>> count //= 4
>>> count
3
```

All seven arithmetic operators have augmented forms: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`. These are used everywhere in Python — loops, accumulators, counters."

---

## [07:45 – 10:00] The print() Function — Full Control Over Output

**[SHOW SLIDE: "print() — Output to the Screen"]**

"You have been using `print()` since Module 01. Now let's cover its full capabilities.

**Multiple arguments:**

```python
>>> print('Name:', 'Alice', 'Age:', 30)
Name: Alice Age: 30
```

`print()` accepts any number of arguments. By default, it separates them with a space.

**The `sep` parameter — change the separator:**

```python
>>> print('Alice', 'Bob', 'Carol', sep=', ')
Alice, Bob, Carol
>>> print('2026', '06', '01', sep='-')
2026-06-01
>>> print('A', 'B', 'C', sep='')
ABC
```

`sep=''` means no separator at all — values run together.

**The `end` parameter — change what goes at the end:**

```python
>>> print('Loading', end='...')
>>> print('Done')
Loading...Done
```

By default, `print()` adds a newline `\n` at the end. Setting `end=''` or `end='...'` changes that behavior.

**[DEMO — show loop with end parameter]**

```python
>>> for i in range(5):
...     print(i, end=' ')
...
0 1 2 3 4
```

Without `end=' '`, each number would print on its own line. With `end=' '`, they print across one line.

**f-strings — formatted string literals:**

f-strings are the modern, clean way to embed variable values inside strings. Put `f` before the opening quote, and use `{}` to embed expressions:

```python
>>> name = 'Alice'
>>> age = 30
>>> print(f'Hello, {name}! You are {age} years old.')
Hello, Alice! You are 30 years old.
```

You can embed any expression inside `{}` — not just variable names:

```python
>>> price = 19.99
>>> qty = 3
>>> print(f'Total: ${price * qty:.2f}')
Total: $59.97
```

The `:2f` format spec rounds the float to 2 decimal places. f-strings are tested on the PCAP exam."

---

## [10:00 – 12:30] The input() Function — Getting Data from Users

**[SHOW SLIDE: "input() — Reading User Input"]**

"The `input()` function lets your programs interact with users. It pauses execution, shows a prompt, waits for the user to type something and press Enter, and returns what they typed.

**[DEMO — run in script mode, not REPL, to show interactive flow]**

```python
name = input('What is your name? ')
print(f'Hello, {name}!')
```

Run this: `python3 greet.py`

```text
What is your name? Alice
Hello, Alice!
```

The critical rule — **`input()` ALWAYS returns a string**. No exceptions. Even if the user types `42`, what you get back is the string `'42'`, not the integer `42`.

**[SHOW DEMO of the TypeError trap]**

```python
# This will crash
age = input('Enter your age: ')
print(age + 1)
```

Output:

```text
Enter your age: 25
TypeError: can only concatenate str (not 'int') to str
```

Python cannot add a `str` and an `int`. The fix: convert immediately after `input()`.

**[SHOW FIX]**

```python
age = int(input('Enter your age: '))
print(f'Next year you will be {age + 1}.')
```

Output:

```text
Enter your age: 25
Next year you will be 26.
```

The pattern `int(input(...))` is the standard idiom for reading an integer from the user. For floats: `float(input(...))`.

**What happens if the user types something non-numeric?**

```python
age = int(input('Enter your age: '))
```

If the user types `'twenty-five'`, Python raises `ValueError: invalid literal for int() with base 10: 'twenty-five'`. We handle this gracefully with exception handling in Module 12 — for now, assume valid input.

The PCAP exam tests `input()` behavior heavily. Three things to remember:

1. `input()` always returns `str`
2. `input('prompt')` displays the prompt text — no extra space is added automatically, so put a space before the closing quote: `input('Enter name: ')`
3. `int(input())` — conversion wraps the entire `input()` call"

---

## [12:30 – 14:00] Putting It Together — Interactive Program

**[SHOW SLIDE: "Putting It All Together"]**

**[DEMO — show final script]**

"Let me show you a complete interactive program that uses everything from this module:

```python
# profile.py

print('=== Student Profile Creator ===')
print()

name = input('Enter your name: ')
age = int(input('Enter your age: '))
major = input('Enter your major: ')
gpa = float(input('Enter your GPA: '))

years_left = max(0, 4 - (age - 18))

print()
print('=== Your Profile ===')
print(f'Name:       {name}')
print(f'Age:        {age}')
print(f'Major:      {major}')
print(f'GPA:        {gpa:.2f}')
print(f'Years left: {years_left}')
print()
print(f'Welcome to Texas Wesleyan, {name}!')
```

This script uses `input()` with type conversion, f-strings with format specs, and augmented assignment. It's a complete, working, useful program — about 15 lines."

---

## [14:00 – 15:00] PCAP Exam Tips & Wrap-Up

**[SHOW SLIDE: "Module 03 — PCAP Alignment"]**

"Key exam take-aways:

**1.** `input()` always returns `str` — even if the user types a number.

**2.** `age = input() + 1` raises `TypeError`. Fix: `age = int(input()) + 1`.

**3.** `int('3.14')` raises `ValueError`. Fix: `int(float('3.14'))`.

**4.** Variable names cannot start with a digit, cannot contain hyphens, cannot be keywords.

**5.** Python is dynamically typed — no type declarations needed, type is set by the assigned value.

**6.** f-strings use `f'...'` syntax with `{}` for embedded expressions.

In your Module 03 lab, you will write a greeting program, a unit converter, and trigger `TypeError` and `ValueError` intentionally to see the exact error messages.

Module 04 covers control flow — `if`, `elif`, `else` — where variables and input really start working together to make decisions. See you there."

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 03 — Variables and Basic I/O]**

---

## Additional Resources

- [Python for Everybody — Chapters 2–3](https://www.py4e.com/book) — Variables, Expressions, Statements
- [Official Python Docs — Built-in Functions: input()](https://docs.python.org/3/library/functions.html#input)
- [Official Python Docs — f-strings (PEP 498)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
- [Python Keywords List](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
- [PEP 8 — Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)
- [Python for Everybody Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episodes 5–6
