# Lab 6: While Loops

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 6 assignment
**Due:** See Canvas for the deadline

---

## Objectives

1. Write `while` loops with proper initialization, condition, and update
2. Use sentinel values to control loop termination from user input
3. Implement accumulator patterns inside while loops
4. Trace while loop execution by hand before running
5. Identify infinite loops and fix them
6. Use `while...else` correctly

---

## Before You Begin

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 6 — While Loops
```

---

## Part 1: Basic While Loop Tracing (10 points)

### Step 1.1 — Trace Before Running

For each loop, trace the execution by hand in a comment table, then verify by running:

**Loop A:**
```python
x = 1
while x <= 32:
    x *= 2
print(x)
# Trace: x starts at 1, doubles each iteration. What is x when the loop exits?
# Your trace table (add as comment):
# Iter | x (start) | Condition | x (end)
# 1    | 1         | True      | 2
# ...  (complete the trace)
```

**Loop B:**
```python
n = 100
count = 0
while n > 1:
    n //= 2
    count += 1
print(count)
# What does count represent? Explain in a comment.
```

**Loop C:**
```python
total = 0
i = 10
while i > 0:
    total += i
    i -= 3
print(total, i)
# Note: i goes below 0. What are the final values of total and i?
```

---

## Part 2: Accumulator Loops (10 points)

### Step 2.1 — Sum and Count with User Input

Write a `while` loop that:
1. Asks the user to enter positive numbers one at a time
2. Stops when the user enters `0` (sentinel value)
3. Prints the count, sum, and average of all entered numbers

```python
print("Enter positive numbers. Enter 0 to stop.")
count = 0
total = 0.0

number = float(input("Number: "))
while number != 0:
    # accumulate total and count
    ___
    ___
    number = float(input("Number: "))

if count > 0:
    print(f"Count: {count}")
    print(f"Sum: {total:.2f}")
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered.")
```

Test with at least 5 numbers before entering 0.

### Step 2.2 — Factorial Calculator

Write a `while` loop to calculate `n!` (n factorial) for a user-supplied `n`:

```python
n = int(input("Enter a non-negative integer for factorial: "))

# Handle edge cases: 0! = 1, 1! = 1
result = 1
i = ___         # What should i start at?
while i <= n:
    result *= i
    i += 1

print(f"{n}! = {result}")
```

Test with n = 0, 1, 5, 10.

---

## Part 3: Input Validation Loops (10 points)

### Step 3.1 — Validated Age Input

Write a loop that keeps asking for age until the user enters a value between 0 and 120:

```python
while True:
    try:
        age = int(input("Enter your age (0-120): "))
        if 0 <= age <= 120:
            break
        else:
            print("Age must be between 0 and 120.")
    except ValueError:
        print("Please enter a whole number.")

print(f"Valid age entered: {age}")
```

Note: `while True:` with `break` is a valid and common pattern for input validation — Module 8 explains `break` formally. Run this and test with: negative numbers, numbers over 120, non-numeric input, and a valid age.

### Step 3.2 — Password Checker (3 Attempts)

Build a password checker that gives the user exactly 3 attempts:

```python
CORRECT_PASSWORD = "txwes2024"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1
    if password == CORRECT_PASSWORD:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect. {remaining} attempt(s) remaining.")
else:
    print("Account locked. Maximum attempts exceeded.")
```

The `while...else` here is intentional — the `else` executes if the loop completes without `break`. Test all paths: correct password on attempt 1, attempt 2, attempt 3, and all 3 wrong.

---

## Part 4: Classic Algorithms (15 points)

### Step 4.1 — Number Guessing Game

Build a complete guessing game:

```python
import random

secret_number = random.randint(1, 100)
max_guesses = 7
guesses_used = 0

print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_guesses} guesses.")

while guesses_used < max_guesses:
    guess = int(input(f"\nGuess {guesses_used + 1}: "))
    guesses_used += 1
    
    if guess == secret_number:
        print(f"Correct! You got it in {guesses_used} guess(es)!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"\nGame over! The number was {secret_number}.")
```

Play the game at least twice (you can hardcode `secret_number = 42` during testing to verify all hints work). Then restore `random.randint`.

### Step 4.2 — Collatz Sequence

The Collatz conjecture: starting with any positive integer `n`:
- If `n` is even: divide by 2
- If `n` is odd: multiply by 3 and add 1
- Repeat until `n` equals 1

Write a `while` loop that prints the Collatz sequence and counts the steps:

```python
n = int(input("Enter a positive integer: "))
original = n
steps = 0

while n != 1:
    print(n, end=" → ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1

print(1)
print(f"\nStarted at {original}, reached 1 in {steps} steps.")
```

Test with n = 6, 27, and one of your own. Note which starting value takes the most steps.

---

## Part 5: Infinite Loop Detection (5 points)

### Step 5.1 — Find and Fix the Bugs

Each loop below contains a bug that would cause an infinite loop. Do NOT run them — identify the bug and write a corrected version as a comment.

**Buggy Loop 1:**
```python
count = 0
while count < 5:
    print(count)
# Bug: What is missing? Write the fix as a comment.
```

**Buggy Loop 2:**
```python
x = 10
while x != 0:
    x -= 3
    print(x)
# Bug: When does this loop exit? Does x ever equal exactly 0? Write the fix.
```

**Buggy Loop 3:**
```python
total = 0
while total < 100:
    number = int(input("Enter number: "))
    total = number    # Bug: what should this line be?
print(total)
```

---

## Submission Checklist

- [ ] Student header at the top
- [ ] Part 1 trace tables written as comments before running
- [ ] Accumulator loop tested with 5+ numbers (Part 2.1)
- [ ] Factorial tested with 0, 1, 5, 10 (Part 2.2)
- [ ] Password checker tested for all 4 paths (Part 3.2)
- [ ] Collatz tested for n=6 and n=27 (Part 4.2)
- [ ] All 3 infinite loop bugs identified and fixed (Part 5)
- [ ] File saved as `lab06_yourLastName.ipynb` or `.py`

**Submit** to the **Lab 6** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | Loop tracing (3 loops) | 10 |
| Part 2 | Accumulator and factorial loops | 10 |
| Part 3 | Input validation and password checker | 10 |
| Part 4 | Guessing game and Collatz sequence | 15 |
| Part 5 | Infinite loop bug detection | 5 |
| **Total** | | **50** |

---

*Next: Module 7 Lab — For Loops*
