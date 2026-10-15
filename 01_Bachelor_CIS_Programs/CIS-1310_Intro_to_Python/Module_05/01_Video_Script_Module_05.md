# Video Script: CIS-1310 — Introduction to Python

## Module 05 — Loops: Iteration with while and for

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Python Institute &bull; Python Programming Full Course &bull; Module 05</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=rfscVS0vtbw" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/rfscVS0vtbw" title="freeCodeCamp / Python Institute &bull; Python Programming Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Python Institute &bull; Python Programming Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 14–16 minutes
**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

Welcome back. Module 04 gave programs the ability to make decisions. Module 05 gives programs the ability to repeat — and repetition is where the real power of programming comes in.

Think about what it would mean to print every number from 1 to 1,000 without loops. You would write a thousand `print` statements. With a loop, that is three lines of code. A payroll system processes hundreds of employees with the same logic. A search engine scans billions of pages. A game engine redraws the screen 60 times per second. None of that is possible without loops.

Python has two loop types. The `while` loop repeats while a condition is True — it is condition-driven. The `for` loop iterates over a sequence — it is data-driven. Both are tested heavily on the PCAP exam. Let's cover both in depth.

---

## The while Loop

The `while` loop is the simpler of the two to understand conceptually. It repeats its body for as long as its condition remains `True`.

```python
while condition:
    body
```

The structure is identical to `if` — a condition, a colon, and an indented body. The difference is that `if` runs its body once; `while` runs its body repeatedly, re-checking the condition before each repetition.

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

Trace through the execution:

- Before iteration 1: `count = 1`, `1 <= 5` is True → print `1`, increment to 2
- Before iteration 2: `count = 2`, `2 <= 5` is True → print `2`, increment to 3
- Before iteration 5: `count = 5`, `5 <= 5` is True → print `5`, increment to 6
- Before iteration 6: `count = 6`, `6 <= 5` is False → loop exits

The critical requirement: **something in the loop body must eventually make the condition False**. If nothing changes, the condition stays True forever — you have an **infinite loop**.

### Infinite Loop

```python
>>> while True:
...     print('looping...')
...
looping...
looping...
looping...
```

Press `Ctrl+C` to interrupt. Python raises `KeyboardInterrupt` — that is how you stop a runaway loop in the terminal.

`while True:` is actually useful in some patterns — a menu that keeps running until the user chooses to quit. The key is that the loop body must eventually `break` or call `exit()`.

### Input Validation Loop

The most common real-world use of `while` is re-prompting until valid input is received:

```python
score = int(input('Enter score (0-100): '))
while score < 0 or score > 100:
    print('Invalid. Try again.')
    score = int(input('Enter score (0-100): '))
print(f'Score accepted: {score}')
```

This is the enhanced guardian from Module 04 — instead of just rejecting invalid input once, the loop re-prompts until it gets something valid.

---

## break and continue

Two keywords give you extra control over loop execution:

`break` — immediately exits the loop entirely, regardless of the condition.

`continue` — skips the rest of the current iteration and jumps back to the condition check.

```python
>>> number = 0
>>> while True:
...     number = int(input('Enter a positive number (0 to quit): '))
...     if number == 0:
...         break
...     print(f'You entered: {number}')
...
Enter a positive number (0 to quit): 5
You entered: 5
Enter a positive number (0 to quit): 12
You entered: 12
Enter a positive number (0 to quit): 0
>>>
```

The `while True:` runs indefinitely, but `break` exits the loop when the user enters 0.

```python
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

When `n` is even, `continue` skips the `print(n)` and returns to the top of the loop. Only odd numbers are printed.

---

## The for Loop

The `for` loop is Python's most-used loop. Instead of repeating while a condition is true, it iterates over each item in a **sequence** — a string, a list, a range, or any other iterable object.

```python
for variable in sequence:
    body
```

On each iteration, `variable` is automatically assigned the next item from `sequence`. When there are no more items, the loop ends.

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

```python
>>> grades = [88, 72, 95, 61, 83]
>>> for g in grades:
...     print(g)
...
88
72
95
61
83
```

### The range() Function

For loops that count a specific number of times, use `range()`.

`range(stop)` — produces integers from `0` up to but NOT including `stop`.
`range(start, stop)` — produces integers from `start` up to but NOT including `stop`.
`range(start, stop, step)` — produces integers from `start` to `stop` with a step increment.

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4

>>> for i in range(1, 6):
...     print(i)
...
1
2
3
4
5

>>> for i in range(0, 20, 5):
...     print(i)
...
0
5
10
15

>>> for i in range(10, 0, -1):
...     print(i)
...
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
```

The `stop` value is always excluded — `range(5)` gives 0 through 4, not 0 through 5. This is a very common PCAP exam trap.

---

## for with else, and the else Clause

Python has a feature that surprises most new programmers: both `while` and `for` loops can have an `else` clause. The `else` runs after the loop finishes **normally** — meaning it was not interrupted by a `break`.

```python
# Search for a value
numbers = [1, 3, 5, 7, 9]
target = 6

for n in numbers:
    if n == target:
        print(f'Found {target}')
        break
else:
    print(f'{target} not found in list')
```

Output:

```text
6 not found in list
```

Change `target = 5`:

```text
Found 5
```

The `else` only runs when the `for` loop exhausted the entire sequence without hitting `break`. This is used for search patterns — 'did we find what we were looking for?'

The PCAP exam will test your understanding of when the loop `else` runs and when it does not.

---

## Nested Loops

Just as you can nest `if` statements, you can nest loops. The inner loop runs to completion for every single iteration of the outer loop.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f'{row} x {col} = {row * col}')
    print()
```

Output:

```text
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

For each value of `row` (1, 2, 3), the inner `col` loop runs completely (1, 2, 3). That is `3 × 3 = 9` iterations total.

**Performance note:** Every level of nesting multiplies the iteration count. A triple-nested loop over lists of size N runs N³ iterations. Keeping loops shallow is important for performance.

---

## enumerate() and zip()

Two built-in functions make `for` loops significantly more powerful.

### enumerate()

`enumerate()` adds an automatic counter to each item in an iterable, returning `(index, value)` pairs:

```python
>>> names = ['Alice', 'Bob', 'Carol']
>>> for i, name in enumerate(names):
...     print(f'{i}: {name}')
...
0: Alice
1: Bob
2: Carol
```

By default the counter starts at 0. Use `enumerate(names, start=1)` to start at 1.

### zip()

`zip()` combines two or more iterables, pairing their items by position:

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

`zip()` stops at the shortest iterable. Both `enumerate()` and `zip()` are tested on the PCAP exam.

---

## Accumulator Pattern

One of the most important programming patterns enabled by loops is the **accumulator pattern**: initialize a variable before the loop, then update it on each iteration.

```python
scores = [88, 72, 95, 61, 83]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f'Total: {total}')
print(f'Average: {average:.1f}')
```

Output:

```text
Total: 399
Average: 79.8
```

```python
words = ['Python', 'is', 'fun']
result = ''

for word in words:
    result += word + ' '

print(result.strip())
```

Output:

```text
Python is fun
```

Accumulators can be integers (sum, count), floats (average), strings (building output), or lists (collecting filtered results). This pattern underlies nearly every data-processing algorithm.

---

## Putting It Together — Number Guessing Game

Let me build a complete interactive program that combines everything from this module:

```python
# guessing_game.py
# Module 05 Lab — CIS-1310

import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print('=== Number Guessing Game ===')
print(f'Guess a number between 1 and 100. You have {max_attempts} tries.')
print()

while attempts < max_attempts:
    guess = int(input(f'Attempt {attempts + 1}/{max_attempts}: '))
    attempts += 1

    if guess < secret:
        print('Too low.')
    elif guess > secret:
        print('Too high.')
    else:
        print(f'Correct! You got it in {attempts} attempt(s).')
        break
else:
    print(f'Out of attempts. The number was {secret}.')
```

This combines: `while` loop with a counter, `break` on success, loop `else` on exhaustion, `if-elif-else` for feedback, and an accumulator (`attempts`). It is a real, playable game in about 20 lines.

---

## PCAP Exam Tips and Wrap-Up

Key exam take-aways:

**1.** `range(stop)` starts at 0 and excludes `stop`. `range(5)` = 0,1,2,3,4.

**2.** `range(start, stop, step)` — negative step counts down: `range(10, 0, -1)`.

**3.** Loop `else` runs when the loop finishes normally (no `break`). It does NOT run if `break` exits the loop.

**4.** `break` exits the loop entirely. `continue` skips the rest of the current iteration.

**5.** `enumerate(iterable)` returns `(index, value)` pairs. `zip(a, b)` pairs items by position.

**6.** An infinite loop has no termination condition — `while True:` with no `break` runs forever.

**7.** Nested loops — inner loop completes all iterations for each iteration of the outer loop.

Module 06 covers lists in depth — and lists work hand-in-hand with `for` loops. See you there.

---

**[END CARD: Texas Wesleyan University | CIS-1310 Introduction to Python | Module 05 — Loops: Iteration with while and for]**

---

## Additional Resources

- [Python for Everybody — Chapter 5](https://www.py4e.com/book) — Iteration
- [Official Python Docs — for statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
- [Official Python Docs — while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [Official Python Docs — range()](https://docs.python.org/3/library/stdtypes.html#range)
- [Python for Everybody Playlist](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGPQAfUMERODyTGp) — Episodes 8–9 (Loops)
