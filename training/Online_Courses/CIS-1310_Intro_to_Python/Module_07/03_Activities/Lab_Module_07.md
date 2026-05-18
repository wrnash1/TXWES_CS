# Lab 7: For Loops and range()

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 7 assignment
**Due:** See Canvas for the deadline

---

## Objectives

1. Use `for` loops with `range()` (one, two, and three arguments)
2. Count down using a negative step
3. Iterate over strings character-by-character
4. Apply `enumerate()` and `zip()` for indexed and parallel iteration
5. Write and trace nested `for` loops
6. Use the `for...else` pattern for search loops

---

## Before You Begin

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 7 — For Loops and range()
```

---

## Part 1: range() Exploration (10 points)

### Step 1.1 — Predict, Then Verify

For each `range()` call below, write your prediction as a comment **before** running it. Then run the code and check.

```python
# Prediction 1: What does range(6) produce?
# Your prediction: ___
print(list(range(6)))

# Prediction 2: What does range(1, 8) produce?
# Your prediction: ___
print(list(range(1, 8)))

# Prediction 3: What does range(0, 20, 4) produce?
# Your prediction: ___
print(list(range(0, 20, 4)))

# Prediction 4: What does range(10, 0, -2) produce?
# Your prediction: ___
print(list(range(10, 0, -2)))

# Prediction 5: What does range(5, 5) produce?
# Your prediction: ___
print(list(range(5, 5)))
```

### Step 1.2 — Countdown Timer

Write a `for` loop that counts down from 10 to 1, then prints "Blast off!":

```python
# Your code here:
for i in range(___):
    print(i)
print("Blast off!")
```

Expected output:
```
10
9
8
7
6
5
4
3
2
1
Blast off!
```

### Step 1.3 — Even Numbers

Write a `for` loop that prints all even numbers from 2 to 20 inclusive:

```python
# Use range() with a step — fill in the blanks:
for i in range(___, ___, ___):
    print(i)
```

---

## Part 2: Iterating Over Strings (10 points)

### Step 2.1 — Character-by-Character

Write a `for` loop that prints each character in your name on its own line, preceded by its position number (starting at 1):

```python
name = "Python"   # Replace with your actual name

for i, char in enumerate(name, start=1):
    print(f"Position {i}: {char}")
```

### Step 2.2 — Vowel Counter

Write a program that counts how many vowels are in a word entered by the user:

```python
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1

print(f"'{word}' contains {count} vowel(s).")
```

Test with: `"Python"`, `"Mississippi"`, `"rhythm"`, and your own name.

### Step 2.3 — Caesar Cipher (Simple Shift)

Write a program that shifts each letter in a string by 1 position in the alphabet (A→B, B→C, ..., Z→A). Use `ord()` and `chr()` to convert:

```python
message = input("Enter a message (letters only, lowercase): ")
encrypted = ""

for char in message:
    if char.isalpha():
        shifted = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        encrypted += shifted
    else:
        encrypted += char

print(f"Encrypted: {encrypted}")
```

Test with: `"hello"` → should produce `"ifmmp"`.

---

## Part 3: enumerate() and zip() (10 points)

### Step 3.1 — Numbered List

Given this list of courses, print a numbered menu using `enumerate()`:

```python
courses = ["CIS-1310 Python", "CIS-1320 Java", "CIS-2340 Web Dev", "CIS-3350 Database"]

print("Available Courses:")
for number, course in enumerate(courses, start=1):
    print(f"  {number}. {course}")
```

Expected output:
```
Available Courses:
  1. CIS-1310 Python
  2. CIS-1320 Java
  3. CIS-2340 Web Dev
  4. CIS-3350 Database
```

### Step 3.2 — Grade Report with zip()

Use `zip()` to print a grade report pairing student names with their scores:

```python
students = ["Alice", "Bob", "Carol", "David", "Eva"]
scores = [92, 78, 85, 91, 67]

print(f"{'Name':<10} {'Score':>6} {'Grade':>6}")
print("-" * 24)

for student, score in zip(students, scores):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{student:<10} {score:>6} {grade:>6}")
```

### Step 3.3 — zip() Length Experiment

Predict the output before running:

```python
# What happens when lists have different lengths?
a = [1, 2, 3, 4, 5]
b = ["one", "two", "three"]

for x, y in zip(a, b):
    print(x, y)

# Prediction: How many lines print? ___
# Why? ___
```

---

## Part 4: Nested for Loops (10 points)

### Step 4.1 — Multiplication Table

Write a program that prints a 5×5 multiplication table using nested `for` loops:

```python
print("Multiplication Table (5×5)")
print()

# Header row
print(f"{'':>4}", end="")
for col in range(1, 6):
    print(f"{col:>4}", end="")
print()
print("-" * 24)

# Data rows
for row in range(1, 6):
    print(f"{row:>4}", end="")
    for col in range(1, 6):
        print(f"{row * col:>4}", end="")
    print()
```

### Step 4.2 — Star Patterns

Write code to produce each of these patterns using nested `for` loops:

**Pattern A — Right triangle:**
```
*
**
***
****
*****
```

```python
# Pattern A:
for row in range(1, 6):
    print("*" * row)
```

**Pattern B — Inverted triangle:**
```
*****
****
***
**
*
```

```python
# Pattern B — fill in the range():
for row in range(___, ___, ___):
    print("*" * row)
```

**Pattern C — Square (5×5):**
```
*****
*****
*****
*****
*****
```

```python
# Pattern C — uses nested loops:
for row in range(5):
    for col in range(5):
        print("*", end="")
    print()
```

### Step 4.3 — Iteration Counter

Before running, predict how many times the innermost `print` executes:

```python
# How many times does this print execute?
count = 0
for i in range(4):
    for j in range(3):
        for k in range(2):
            count += 1

print(count)
# Your prediction: ___
# Formula: ___ × ___ × ___ = ___
```

---

## Part 5: for...else and Search Loops (10 points)

### Step 5.1 — Prime Checker

Use `for...else` to check if a number is prime. A prime number has no divisors other than 1 and itself:

```python
n = int(input("Enter a positive integer: "))

if n < 2:
    print(f"{n} is not prime.")
else:
    for divisor in range(2, n):
        if n % divisor == 0:
            print(f"{n} is NOT prime. ({divisor} divides {n})")
            break
    else:
        print(f"{n} IS prime.")
```

Test with: 2, 7, 12, 17, 49, 97.

Note: The `else` clause belongs to the `for` loop, not the `if`. It only runs if no `break` occurred (no divisor was found).

### Step 5.2 — Linear Search

Write a linear search that looks for a target value in a list and reports whether it was found and at which position:

```python
numbers = [15, 42, 8, 99, 23, 7, 56]
target = int(input("Enter a number to search for: "))

for index, value in enumerate(numbers):
    if value == target:
        print(f"Found {target} at position {index}.")
        break
else:
    print(f"{target} was not found in the list.")
```

Test with values that are in the list (42, 99) and values that are not (10, 100).

### Step 5.3 — FizzBuzz with for

Classic FizzBuzz using a `for` loop — a common programming interview question:

```python
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Verify: 3 → "Fizz", 5 → "Buzz", 15 → "FizzBuzz", 7 → 7.

**Challenge:** Modify the loop to only print FizzBuzz lines (skip numbers that are just numbers):

```python
for i in range(1, 31):
    if i % 3 == 0 or i % 5 == 0:
        # Your code here
        ___
```

---

## Submission Checklist

- [ ] Student header at the top
- [ ] Part 1 predictions written as comments before running
- [ ] Countdown prints 10 down to 1, then "Blast off!" (Part 1.2)
- [ ] Vowel counter tested with 4 words (Part 2.2)
- [ ] Caesar cipher tested with "hello" → "ifmmp" (Part 2.3)
- [ ] Grade report uses zip() (Part 3.2)
- [ ] Multiplication table displays correctly (Part 4.1)
- [ ] All 3 star patterns correct (Part 4.2)
- [ ] Iteration counter prediction verified (Part 4.3)
- [ ] Prime checker tested with 2, 7, 12, 17, 49, 97 (Part 5.1)
- [ ] File saved as `lab07_yourLastName.ipynb` or `.py`

**Submit** to the **Lab 7** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | range() predictions and loops | 10 |
| Part 2 | String iteration | 10 |
| Part 3 | enumerate() and zip() | 10 |
| Part 4 | Nested loops and patterns | 10 |
| Part 5 | for...else search loops | 10 |
| **Total** | | **50** |

---

*Next: Module 8 Lab — Loop Control: break, continue, pass*
