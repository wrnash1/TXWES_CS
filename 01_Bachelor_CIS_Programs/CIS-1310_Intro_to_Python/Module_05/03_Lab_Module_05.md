# Lab Activity: Module 05 — Loops: Iteration with while and for

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Estimated Time:** 70–85 minutes

---

## Overview

In this lab you will write `while` loops that count and validate input, use `break` and `continue` to control loop flow, trigger and interrupt an infinite loop, iterate over sequences with `for` loops, explore every form of `range()`, search with the loop `else` clause, apply the accumulator pattern to compute statistics, use `enumerate()` and `zip()`, and build a complete number guessing game.

---

## Prerequisites

- Ubuntu VM from Module 01 is running.
- Terminal open, Python 3.10+ installed.

---

## Setup

```bash
cd ~/cis1310
mkdir module05
cd module05
```

---

## Part 1 — while Loop Basics

```bash
python3
```

### Step 1.1 — Counting Loop

```python
>>> count = 1
>>> while count <= 5:
...     print(count)
...     count += 1
...
1
2
3
4
5
```

### Step 1.2 — Trace the Loop Manually

Before running, predict the output of each iteration:

```python
>>> n = 10
>>> while n > 0:
...     print(n)
...     n -= 3
...
10
7
4
1
```

Trace: n=10 (print 10, n becomes 7) → n=7 (print 7, n becomes 4) → n=4 (print 4, n becomes 1) → n=1 (print 1, n becomes -2) → n=-2, condition False, loop exits.

### Step 1.3 — Infinite Loop and Ctrl+C

Type this and let it run for a moment — then press `Ctrl+C`:

```python
>>> while True:
...     print('looping...')
...
looping...
looping...
looping...
^C
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

`KeyboardInterrupt` is how Python reports that you manually interrupted execution. This is not a program error — it is a deliberate interruption.

Exit and restart:

```python
>>> exit()
```

```bash
python3
```

### Step 1.4 — break and continue

```python
>>> # break — exit when sentinel value reached
>>> i = 0
>>> while True:
...     i += 1
...     if i == 4:
...         break
...     print(i)
...
1
2
3

>>> # continue — skip even numbers
>>> n = 0
>>> while n < 10:
...     n += 1
...     if n % 2 == 0:
...         continue
...     print(n)
...
1
3
5
7
9
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 1 REQUIRED:** Screenshot showing the `Ctrl+C` infinite loop interruption and the `break`/`continue` demos from Steps 1.3 and 1.4. Save as `lab05_screenshot_01_while_control.png`.

---

## Part 2 — range() in All Forms

```bash
python3
```

### Step 2.1 — range(stop)

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(0))
[]
>>> for i in range(5):
...     print(i, end=' ')
...
0 1 2 3 4
```

### Step 2.2 — range(start, stop)

```python
>>> list(range(1, 6))
[1, 2, 3, 4, 5]
>>> list(range(3, 8))
[3, 4, 5, 6, 7]
>>> list(range(5, 5))
[]
```

### Step 2.3 — range(start, stop, step)

```python
>>> list(range(0, 10, 2))
[0, 2, 4, 6, 8]
>>> list(range(1, 10, 3))
[1, 4, 7]
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list(range(10, 0, -2))
[10, 8, 6, 4, 2]
>>> list(range(5, 0))
[]
```

Note: `range(5, 0)` with no step defaults to step=+1. Since `5 >= 0` already, no values are produced — the range is empty.

### Step 2.4 — for with range

```python
>>> for i in range(1, 6):
...     print(f'{i} squared = {i**2}')
...
1 squared = 1
2 squared = 4
3 squared = 9
4 squared = 16
5 squared = 25
```

Exit the REPL:

```python
>>> exit()
```

> **SCREENSHOT 2 REQUIRED:** Screenshot showing range() examples from Steps 2.1–2.3 — particularly the countdown range and the empty range. Save as `lab05_screenshot_02_range.png`.

---

## Part 3 — for Over Sequences and Loop else

```bash
python3
```

### Step 3.1 — for Over a String

```python
>>> for char in 'Python':
...     print(char)
...
P
y
t
h
o
n
```

### Step 3.2 — Count Vowels

```python
>>> vowel_count = 0
>>> for char in 'Hello World':
...     if char.lower() in 'aeiou':
...         vowel_count += 1
...
>>> vowel_count
3
```

### Step 3.3 — Loop else (not found)

```python
>>> numbers = [1, 3, 5, 7, 9]
>>> target = 6
>>> for n in numbers:
...     if n == target:
...         print(f'Found {target}')
...         break
... else:
...     print(f'{target} not found in the list')
...
6 not found in the list
```

### Step 3.4 — Loop else (found — else does NOT run)

```python
>>> target = 5
>>> for n in numbers:
...     if n == target:
...         print(f'Found {target}')
...         break
... else:
...     print(f'{target} not found in the list')
...
Found 5
```

When `break` fires, Python skips the `else` entirely. Confirm the distinction — this is a key PCAP exam concept.

Exit the REPL:

```python
>>> exit()
```

---

## Part 4 — enumerate() and zip()

```bash
python3
```

### Step 4.1 — enumerate()

```python
>>> names = ['Alice', 'Bob', 'Carol', 'Dave']
>>> for i, name in enumerate(names):
...     print(f'{i}: {name}')
...
0: Alice
1: Bob
2: Carol
3: Dave

>>> for i, name in enumerate(names, start=1):
...     print(f'{i}. {name}')
...
1. Alice
2. Bob
3. Carol
4. Dave
```

### Step 4.2 — zip()

```python
>>> names = ['Alice', 'Bob', 'Carol']
>>> scores = [92, 85, 78]
>>> for name, score in zip(names, scores):
...     print(f'{name}: {score}')
...
Alice: 92
Bob: 85
Carol: 78
```

### Step 4.3 — zip stops at shortest

```python
>>> list(zip([1, 2, 3, 4], ['a', 'b']))
[(1, 'a'), (2, 'b')]
```

The value `3` and `4` are dropped because the second list has only 2 items.

Exit the REPL:

```python
>>> exit()
```

---

## Part 5 — Accumulator Pattern

```bash
nano accumulator.py
```

```python
# accumulator.py
# Demonstrates sum, average, min, max accumulators
# Module 05 Lab — CIS-1310

scores = [88, 72, 95, 61, 83, 90, 77]

total = 0
count = 0
maximum = scores[0]
minimum = scores[0]

for score in scores:
    total += score
    count += 1
    if score > maximum:
        maximum = score
    if score < minimum:
        minimum = score

average = total / count

print('=== Score Statistics ===')
print(f'  Scores:  {scores}')
print(f'  Count:   {count}')
print(f'  Total:   {total}')
print(f'  Average: {average:.2f}')
print(f'  Maximum: {maximum}')
print(f'  Minimum: {minimum}')
```

Save and run:

```bash
python3 accumulator.py
```

Expected output:

```text
=== Score Statistics ===
  Scores:  [88, 72, 95, 61, 83, 90, 77]
  Count:   7
  Total:   566
  Average: 80.86
  Maximum: 95
  Minimum: 61
```

---

## Part 6 — Write guessing_game.py

### Step 6.1 — Create the Script

```bash
nano guessing_game.py
```

```python
# guessing_game.py
# Number guessing game combining while, break, loop else, accumulator
# Module 05 Lab — CIS-1310

import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print('=== Number Guessing Game ===')
print(f'I am thinking of a number between 1 and 100.')
print(f'You have {max_attempts} attempts.')
print()

while attempts < max_attempts:
    try:
        guess = int(input(f'Attempt {attempts + 1}/{max_attempts}: '))
    except ValueError:
        print('Please enter a whole number.')
        continue

    attempts += 1

    if guess < 1 or guess > 100:
        print('Guess must be between 1 and 100.')
        attempts -= 1    # don't count invalid guess
        continue

    if guess < secret:
        print('Too low.')
    elif guess > secret:
        print('Too high.')
    else:
        print(f'\nCorrect! You guessed {secret} in {attempts} attempt(s).')
        break
else:
    print(f'\nOut of attempts! The number was {secret}.')

print('Thanks for playing!')
```

Save and run:

```bash
python3 guessing_game.py
```

Sample winning run:

```text
=== Number Guessing Game ===
I am thinking of a number between 1 and 100.
You have 7 attempts.

Attempt 1/7: 50
Too high.
Attempt 2/7: 25
Too low.
Attempt 3/7: 37
Too low.
Attempt 4/7: 43
Correct! You guessed 43 in 4 attempt(s).
Thanks for playing!
```

Play the game at least twice — once winning (to confirm the success path) and once losing (exhaust all 7 attempts to confirm the `else` branch fires).

> **SCREENSHOT 3 REQUIRED:** Screenshot of `guessing_game.py` running — at least one full game shown (winning or losing). Save as `lab05_screenshot_03_guessing_game.png`.

---

## Part 7 — Write input_validator.py

This program uses a `while` loop to enforce valid input — re-prompting until the user provides an acceptable value.

```bash
nano input_validator.py
```

```python
# input_validator.py
# Input validation loop — re-prompt until valid score received
# Module 05 Lab — CIS-1310

print('=== Score Entry System ===')
print()

# Keep prompting until a valid score is entered
while True:
    raw = input('Enter a score (0-100): ')

    # Check if input is numeric
    if not raw.isdigit():
        print(f'  Error: "{raw}" is not a whole number. Try again.')
        continue

    score = int(raw)

    # Check if in valid range
    if score < 0 or score > 100:
        print(f'  Error: {score} is out of range. Must be 0-100. Try again.')
        continue

    # If we reach here, input is valid
    break

print()
print(f'  Valid score entered: {score}')

# Assign grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'  Grade: {grade}')
```

Save and run:

```bash
python3 input_validator.py
```

Test by entering bad values first:

```text
=== Score Entry System ===

Enter a score (0-100): hello
  Error: "hello" is not a whole number. Try again.
Enter a score (0-100): 150
  Error: 150 is out of range. Must be 0-100. Try again.
Enter a score (0-100): 82

  Valid score entered: 82
  Grade: B
```

> **SCREENSHOT 4 REQUIRED:** Screenshot of `input_validator.py` running — showing at least one rejection before a successful entry. Save as `lab05_screenshot_04_input_validator.png`.

---

## Part 8 — Nested Loop: Multiplication Table

```bash
nano times_table.py
```

```python
# times_table.py
# Nested loops to print a multiplication table
# Module 05 Lab — CIS-1310

size = int(input('Enter table size (e.g., 5 for 5x5): '))

print()
print(f'=== {size}x{size} Multiplication Table ===')
print()

# Header row
print('    ', end='')
for col in range(1, size + 1):
    print(f'{col:4}', end='')
print()
print('    ' + '----' * size)

# Data rows
for row in range(1, size + 1):
    print(f'{row:3} |', end='')
    for col in range(1, size + 1):
        print(f'{row * col:4}', end='')
    print()
```

Save and run:

```bash
python3 times_table.py
```

Enter `5`:

```text
=== 5x5 Multiplication Table ===

       1   2   3   4   5
    --------------------
  1 |  1   2   3   4   5
  2 |  2   4   6   8  10
  3 |  3   6   9  12  15
  4 |  4   8  12  16  20
  5 |  5  10  15  20  25
```

> **SCREENSHOT 5 REQUIRED:** Screenshot of `times_table.py` running with size 5. Save as `lab05_screenshot_05_times_table.png`.

---

## Deliverables

Zip all 5 screenshots and upload to the Canvas Module 05 Lab Assignment.

| # | File Name | What It Shows |
|---|---|---|
| 1 | `lab05_screenshot_01_while_control.png` | Infinite loop interruption, break and continue demos |
| 2 | `lab05_screenshot_02_range.png` | range() examples including countdown and empty range |
| 3 | `lab05_screenshot_03_guessing_game.png` | `guessing_game.py` — at least one full game |
| 4 | `lab05_screenshot_04_input_validator.png` | `input_validator.py` — rejection then acceptance |
| 5 | `lab05_screenshot_05_times_table.png` | `times_table.py` — 5x5 table |

---

## Part 9 — Challenge Exercise

These steps are optional and ungraded. They extend loop concepts to more complex algorithmic patterns.

### Challenge 9.1 — FizzBuzz with Loop-Else

FizzBuzz is a classic programming interview problem. Write `~/cis1310/module05/fizzbuzz.py` that:

1. Uses a `for` loop over `range(1, 101)` to print numbers 1–100
2. Prints `FizzBuzz` for multiples of both 3 and 5
3. Prints `Fizz` for multiples of 3 only
4. Prints `Buzz` for multiples of 5 only
5. Prints the number itself otherwise
6. After the loop, uses the `else` clause to print `Complete — no break occurred`
7. Counts and prints the total number of `Fizz`, `Buzz`, and `FizzBuzz` outputs using three accumulator variables

The challenge: the `elif` order matters — test `FizzBuzz` (divisible by both) first before testing `Fizz` or `Buzz` individually. If you check `Fizz` first, multiples of 15 will match early and never reach `FizzBuzz`.

---

### Challenge 9.2 — Prime Number Sieve (Loop + For-Else)

Write `~/cis1310/module05/primes.py` that finds all prime numbers up to a user-specified limit using trial division and the `for-else` pattern:

For each candidate number `n` from 2 to the limit, use a `for` loop to test whether any number from 2 to `n-1` divides `n` evenly. If a divisor is found, `break`. If the inner loop completes without breaking (meaning no divisor was found), the `else` clause identifies `n` as prime and appends it to a list.

Print all discovered primes and their count. Then improve the algorithm: instead of testing up to `n-1`, only test up to `int(n**0.5) + 1` (the square root bound). Compare the execution speed hint — the optimized version tests far fewer candidates.

---

### Challenge 9.3 — Collatz Conjecture Visualizer

Write `~/cis1310/module05/collatz.py` that implements the Collatz sequence:

- Start with any positive integer `n`
- If `n` is even: `n = n // 2`
- If `n` is odd: `n = 3 * n + 1`
- Repeat until `n == 1`

Use a `while` loop to generate the sequence. Print each value, count the steps, and track the maximum value reached. Then run the sequence for starting values 1 through 20 using an outer `for` loop and print a summary table showing the starting value, number of steps to reach 1, and the maximum value encountered. The Collatz conjecture states this sequence always reaches 1 for any positive integer — it has never been proven or disproven for all integers.

---

## Troubleshooting Guide

**Infinite loop that won't stop.**
Press `Ctrl+C` to send `KeyboardInterrupt`. Check your `while` condition — something inside the loop must eventually make the condition `False` or hit a `break`.

**range() produces unexpected values.**
Remember: `stop` is always excluded. `range(1, 5)` gives 1, 2, 3, 4 — not 5. To include 5, use `range(1, 6)`.

**Loop else runs when it should not (or vice versa).**
The `else` only runs when no `break` was executed. If `break` fires even once, `else` is skipped entirely.

**`guessing_game.py` — same answer every time.**
The `random.randint(1, 100)` call at the top generates a new number each run. If you always get the same number, check that you are not accidentally setting `secret` to a fixed value.

**`times_table.py` — columns misaligned.**
The `:4` format spec right-aligns numbers in a 4-character field. If your numbers are wider than 4 digits, increase the field width in both the header and data rows.
