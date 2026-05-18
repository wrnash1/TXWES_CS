# Reading Guide: Module 6 — While Loops

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Certification Alignment:** PCAP — Certified Associate in Python Programming
**PCAP Exam Section:** Section 3 — Control Flow — Conditional Blocks and Loops
**Estimated Reading Time:** 40–50 minutes
**OER Resources:** [edube.org PE1 Module 3](https://edube.org/) | [Python while Loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a `while` loop with a correctly formed condition and loop body
2. Initialize and update a counter variable to control loop repetition
3. Identify and prevent infinite loops by ensuring the condition eventually becomes `False`
4. Use a sentinel value to control loop termination based on user input
5. Explain and use the `while...else` construct
6. Trace through a `while` loop to predict output

---

## Section 1: The `while` Loop

A `while` loop executes its body **repeatedly** as long as its condition remains `True`. When the condition becomes `False`, the loop ends and execution continues with the next statement.

### Syntax

```python
while condition:
    # loop body — indented
    statement1
    statement2
# code here runs after the loop ends
```

### Simple Counter Example

```python
count = 1
while count <= 5:
    print(count)
    count += 1   # CRITICAL: must change count or loop runs forever
print("Done")
```

**Output:**
```
1
2
3
4
5
Done
```

**Three essential components of a safe while loop:**
1. **Initialization** — set the loop variable before the loop (`count = 1`)
2. **Condition** — the test checked before each iteration (`count <= 5`)
3. **Update** — change the variable inside the loop (`count += 1`)

---

## Section 2: Infinite Loops

If the condition never becomes `False`, the loop runs forever — an **infinite loop**. This is usually a bug.

```python
# INFINITE LOOP — count never changes:
count = 1
while count <= 5:
    print(count)
    # Missing count += 1 — this runs forever!
```

**To stop an infinite loop:** Press `Ctrl + C` in the terminal or interrupt the kernel in Jupyter/Colab.

> **PCAP Exam Tip:** Questions about infinite loops test whether you can identify when the loop variable is never modified or when the condition can never become `False`. Always verify that the loop variable changes on every iteration.

---

## Section 3: User Input Loops

A common pattern: keep asking the user for input until they enter a valid response.

### Validation Loop

```python
age = -1
while age < 0 or age > 120:
    age = int(input("Enter a valid age (0-120): "))
    if age < 0 or age > 120:
        print("Invalid age. Try again.")
print(f"Your age is: {age}")
```

### Sentinel Value Loop

A **sentinel value** is a special input value that signals the loop to stop:

```python
total = 0
count = 0
print("Enter exam scores. Type -1 to finish.")

score = float(input("Score: "))
while score != -1:          # -1 is the sentinel value
    total += score
    count += 1
    score = float(input("Score: "))

if count > 0:
    print(f"Average: {total / count:.2f}")
else:
    print("No scores entered")
```

---

## Section 4: Accumulator Pattern

A common `while` loop use case is **accumulation** — building up a result across iterations:

```python
# Sum of integers 1 to n
n = 10
total = 0
i = 1
while i <= n:
    total += i   # accumulate
    i += 1
print(f"Sum of 1 to {n}: {total}")   # 55
```

```python
# Factorial using while
n = 5
result = 1
while n > 0:
    result *= n
    n -= 1
print(f"5! = {result}")   # 120
```

---

## Section 5: The `while...else` Construct

Python allows an `else` clause on a `while` loop. The `else` block executes when the loop condition becomes `False` (normal termination). It does **not** execute when the loop exits via `break`.

```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed normally")
```

**Output:**
```
Count: 0
Count: 1
Count: 2
Loop completed normally
```

> The `while...else` is covered more in Module 8 after learning `break`. Its main use: detect whether a search loop succeeded or exhausted all options.

---

## Section 6: Common While Loop Patterns

### Countdown

```python
countdown = 10
while countdown >= 0:
    if countdown > 0:
        print(countdown)
    else:
        print("Blast off!")
    countdown -= 1
```

### Number Guessing Game (Preview Pattern)

```python
import random
secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"Correct! You got it in {attempts} attempt(s).")
```

---

## Section 7: Tracing a While Loop

To predict `while` loop output without running it:
1. Note the initial value of all variables
2. Check the condition before each "iteration"
3. Trace each statement in the body
4. Note the update step
5. Repeat until condition is `False`

**Trace this loop:**
```python
x = 1
while x < 20:
    x *= 3
print(x)
```

| Iteration | Start of iteration: x | Condition: x < 20 | After body: x *= 3 |
|---|---|---|---|
| 1 | 1 | True | 3 |
| 2 | 3 | True | 9 |
| 3 | 9 | True | 27 |
| 4 | 27 | False — loop ends | — |

Output: `27` (the value of `x` when the loop exits)

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **`while` loop** | Repeats a block of code as long as a condition is `True` |
| **Infinite loop** | A loop whose condition never becomes `False` — runs forever |
| **Sentinel value** | A special input value used to signal the end of a data entry loop |
| **Accumulator** | A variable that collects a running total or result across loop iterations |
| **`while...else`** | Executes the `else` block when the `while` condition becomes `False` (not via `break`) |

---

## External Resources

| Resource | Link | What to Study |
|---|---|---|
| Python `while` Reference | [docs.python.org/3/reference/compound_stmts.html#the-while-statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) | Full syntax |
| edube.org PE1 Module 3 | [edube.org](https://edube.org/) | While loops section |

---

## Self-Check Review Questions

1. What are the three essential components of a properly controlled `while` loop?
2. What happens if the condition of a `while` loop never becomes `False`?
3. What is a sentinel value and why is it useful?
4. Trace this loop and give the output: `x = 2; while x < 100: x **= 2; print(x)`
5. When does the `else` clause of a `while...else` execute?

---

*Next Module → Module 7: For Loops and range()*
