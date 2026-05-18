# Lab 8: Loop Control — break, continue, pass

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 8 assignment
**Due:** See Canvas for the deadline

---

## Objectives

1. Use `break` to exit a loop when a condition is met
2. Use `continue` to skip unwanted iterations
3. Understand how `break` interacts with `for...else` and `while...else`
4. Apply `pass` as a stub for unfinished code blocks
5. Build practical programs using loop control: search, filtering, input validation

---

## Before You Begin

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 8 — Loop Control: break, continue, pass
```

---

## Part 1: break Fundamentals (10 points)

### Step 1.1 — Predict, Then Verify

For each snippet, predict the output as a comment **before** running:

```python
# Snippet A:
for i in range(10):
    if i == 5:
        break
    print(i)
# Prediction: ___

# Snippet B:
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("Loop complete")
# Prediction (does "Loop complete" print?): ___

# Snippet C — nested:
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"{i},{j}")
# Prediction: How many lines print? ___
```

### Step 1.2 — First Match Search

Write a program that searches a list for the first number divisible by 7 and prints it, then stops:

```python
numbers = [4, 15, 22, 49, 63, 14, 77, 8]

for num in numbers:
    if num % 7 == 0:
        print(f"First multiple of 7: {num}")
        break
else:
    print("No multiple of 7 found.")
```

Then change the list to `[3, 8, 10, 25]` and verify the `else` branch prints.

### Step 1.3 — Menu System

Build a simple text menu that loops until the user chooses to quit:

```python
print("=== Simple Menu ===")
while True:
    print("\n1. Say Hello")
    print("2. Show Date")
    print("3. Quit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("Hello, World!")
    elif choice == "2":
        import datetime
        print(f"Today is: {datetime.date.today()}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
```

Test all four paths: choice 1, choice 2, choice 3 (quit), and an invalid choice.

---

## Part 2: continue Fundamentals (10 points)

### Step 2.1 — Predict, Then Verify

```python
# Snippet A:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Prediction: ___

# Snippet B:
n = 0
while n < 10:
    n += 1
    if n % 4 == 0:
        continue
    print(n)
# Prediction: Which numbers print? ___
```

### Step 2.2 — Filter Negatives

Given a list of numbers, print only the positive ones using `continue`:

```python
data = [5, -3, 0, 12, -7, 3, -1, 8]

print("Positive numbers:")
for val in data:
    if val <= 0:
        continue
    print(val)
```

Then modify the program to also keep a count of how many positive numbers were printed.

### Step 2.3 — Skip Multiples

Print all integers from 1 to 30, but skip any that are multiples of both 3 and 5:

```python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i, end=" ")
print()
```

Expected: 15 and 30 are skipped (they are the only multiples of both 3 and 5 in range 1–30).

---

## Part 3: break vs. continue — Head-to-Head (10 points)

### Step 3.1 — Same Data, Different Behavior

Run both loops on the same list and compare outputs:

```python
scores = [85, 92, -1, 78, 95, -1, 67]

print("With break (stop at first -1):")
for score in scores:
    if score == -1:
        break
    print(score)

print()

print("With continue (skip all -1s):")
for score in scores:
    if score == -1:
        continue
    print(score)
```

Before running, write your predictions as comments. Then verify.

### Step 3.2 — Identify the Correct Statement

For each task, choose `break` or `continue` and write the complete loop:

**Task A:** Print the first 5 even numbers from a list (stop after finding 5):
```python
evens = []
numbers = [1, 4, 7, 8, 2, 11, 6, 3, 10, 14, 9]

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
        if len(evens) == 5:
            ___    # break or continue?
            
print(evens)
```

**Task B:** From 1 to 100, sum all numbers EXCEPT multiples of 7:
```python
total = 0
for i in range(1, 101):
    if i % 7 == 0:
        ___    # break or continue?
    total += i

print(f"Sum (excluding multiples of 7): {total}")
```

---

## Part 4: pass and Code Stubs (5 points)

### Step 4.1 — Using pass as a Placeholder

The following program skeleton uses `pass` to mark sections not yet implemented. Fill in the actual code for 2 of the 3 stubs:

```python
numbers = [10, -5, 0, 23, -8, 7, 0, 15]

for num in numbers:
    if num > 0:
        pass    # TODO: accumulate positive numbers
    elif num < 0:
        pass    # TODO: accumulate negative numbers
    else:
        pass    # TODO: count zeros

# After replacing pass with real code, print:
# Total of positives: ___
# Total of negatives: ___
# Count of zeros: ___
```

### Step 4.2 — pass vs. continue

Explain in a comment the difference between these two versions:

```python
# Version 1:
for i in range(5):
    if i == 2:
        pass
    print(i)

# Version 2:
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Write the output of each as a comment, then explain: why does Version 1 still print `2` but Version 2 does not?

---

## Part 5: Classic Algorithms Using Loop Control (15 points)

### Step 5.1 — Prime Number Finder

Find and print all prime numbers between 2 and 50 using nested loops with `break` and `for...else`:

```python
print("Prime numbers from 2 to 50:")
primes = []

for n in range(2, 51):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)

print(primes)
print(f"Count: {len(primes)}")
```

Expected: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]` — 15 primes.

### Step 5.2 — Guessing Game with continue

Enhance the number guessing game from Module 6. Use `continue` to skip processing when the input is not a valid integer:

```python
import random

secret = random.randint(1, 100)
max_guesses = 7
guesses = 0

print("Guess the number (1-100). You have 7 tries.")

while guesses < max_guesses:
    raw = input(f"Guess {guesses + 1}: ")
    
    try:
        guess = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        continue    # don't count this as a guess attempt
    
    guesses += 1
    
    if guess == secret:
        print(f"Correct! You got it in {guesses} guess(es).")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game over! The number was {secret}.")
```

Note: `continue` skips the `guesses += 1` increment when the input was invalid, so invalid entries don't cost the player a guess.

### Step 5.3 — Running Statistics with Sentinel and break

Build a statistics calculator that accepts numbers until the user enters a sentinel, then reports:

```python
print("Enter numbers to analyze. Enter 'done' when finished.")

numbers = []
while True:
    raw = input("Number (or 'done'): ")
    
    if raw.lower() == "done":
        break
    
    try:
        num = float(raw)
        numbers.append(num)
    except ValueError:
        print(f"'{raw}' is not a number — skipped.")
        continue

if not numbers:
    print("No numbers entered.")
else:
    total = sum(numbers)
    count = len(numbers)
    minimum = numbers[0]
    maximum = numbers[0]
    
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    
    print(f"\nResults ({count} numbers):")
    print(f"  Sum:     {total:.2f}")
    print(f"  Average: {total / count:.2f}")
    print(f"  Min:     {minimum:.2f}")
    print(f"  Max:     {maximum:.2f}")
```

Test with: several valid numbers, a few invalid entries (like "abc"), then "done".

---

## Submission Checklist

- [ ] Student header at the top
- [ ] Part 1 predictions written as comments before running
- [ ] Menu system tested for all 4 paths (Part 1.3)
- [ ] continue predictions written before running (Part 2.1)
- [ ] break vs. continue comparison explained in comments (Part 3.1)
- [ ] Task A and Task B filled in correctly (Part 3.2)
- [ ] pass stubs replaced with working code (Part 4.1)
- [ ] pass vs. continue output difference explained (Part 4.2)
- [ ] Prime list shows all 15 primes from 2–50 (Part 5.1)
- [ ] Statistics calculator tested with mixed valid/invalid input (Part 5.3)
- [ ] File saved as `lab08_yourLastName.ipynb` or `.py`

**Submit** to the **Lab 8** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | break fundamentals | 10 |
| Part 2 | continue fundamentals | 10 |
| Part 3 | break vs. continue comparison | 10 |
| Part 4 | pass and code stubs | 5 |
| Part 5 | Classic algorithms | 15 |
| **Total** | | **50** |

---

*Next: Module 9 Lab — Lists*
