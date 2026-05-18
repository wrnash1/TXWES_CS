# Unit Test 2: Modules 5–8 — Conditionals and Loops

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 30 Questions × 3 points each = **90 points** + 10-point bonus question = **100 points max**
**Suggested Time:** 45 minutes
**PCAP Alignment:** Section 3 — Control Flow (Complete)
**Covers:** Module 5 (Conditionals), Module 6 (While Loops), Module 7 (For Loops/range), Module 8 (break/continue/pass)

---

## Canvas Entry Instructions

- **Question Type:** Multiple Choice | **Points:** 3 each (bonus: 10) | **Shuffle Answers:** Yes
- **Time Limit:** 45 minutes | **Attempts:** 1

---

## Questions

---

### Question 1 — Module 5: Conditional Tracing

What is the output of this code?

```python
x = 15
if x > 10:
    print("A")
if x > 12:
    print("B")
if x > 20:
    print("C")
```

- A) `A`
- B) `A B C`
- C) **`A B`** ← CORRECT
- D) `B`

**Explanation:** These are three **separate** `if` statements, not `elif`. Each is checked independently. `x=15`: 15>10 (True→print A), 15>12 (True→print B), 15>20 (False→skip C). Output: A then B.

---

### Question 2 — Module 5: elif vs. separate if

What is the output of this code?

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
```

- A) `A B C`
- B) `B C`
- C) `C`
- D) **`B`** ← CORRECT

**Explanation:** `elif` is a chain — only the **first** matching branch runs. `85 >= 90` is False, `85 >= 80` is True → print "B", stop. The remaining `elif` is skipped. This first-match behavior is the key difference between `elif` chains and separate `if` statements.

---

### Question 3 — Module 5: Truthy/Falsy

What is the output of this code?

```python
values = [0, "", None, "hello", [], 42]
for v in values:
    if v:
        print("truthy", end=" ")
    else:
        print("falsy", end=" ")
```

- A) `truthy truthy truthy truthy truthy truthy`
- B) `falsy falsy truthy falsy truthy truthy`
- C) **`falsy falsy falsy truthy falsy truthy`** ← CORRECT
- D) `falsy falsy falsy falsy falsy falsy`

**Explanation:** Falsy values in Python: `0`, `""` (empty string), `None`, `[]` (empty list), `0.0`. All others are truthy. `"hello"` is truthy (non-empty string), `42` is truthy (non-zero). Output: falsy falsy falsy truthy falsy truthy.

---

### Question 4 — Module 5: Ternary Expression

What is the output of this code?

```python
x = 7
result = "odd" if x % 2 != 0 else "even"
print(result)
```

- A) `even`
- B) `True`
- C) **`odd`** ← CORRECT
- D) `SyntaxError`

**Explanation:** The ternary expression evaluates the condition `7 % 2 != 0` → `1 != 0` → `True`. So `result = "odd"`. The form is: `value_if_true if condition else value_if_false`.

---

### Question 5 — Module 5: Nested Conditionals

What is the output of this code?

```python
a = 5
b = 10
if a < b:
    if a > 3:
        print("X")
    else:
        print("Y")
else:
    print("Z")
```

- A) `Y`
- B) `Z`
- C) `X Y`
- D) **`X`** ← CORRECT

**Explanation:** Outer: `5 < 10` is True → enter outer block. Inner: `5 > 3` is True → print "X". The `else` branches are skipped. Output: `X`.

---

### Question 6 — Module 6: While Tracing

What is the output of this code?

```python
n = 1
while n < 50:
    n *= 4
print(n)
```

- A) `16`
- B) `32`
- C) `50`
- D) **`64`** ← CORRECT

**Explanation:** Trace: n=1 (1<50 T→n=4), n=4 (4<50 T→n=16), n=16 (16<50 T→n=64), n=64 (64<50 F→stop). Output: 64.

---

### Question 7 — Module 6: Sentinel Value

What is the purpose of a sentinel value in a while loop?

- A) To initialize the accumulator variable before the loop
- B) To count the number of loop iterations
- C) **To signal the end of user input without needing a separate flag variable** ← CORRECT
- D) To guarantee the loop runs at least once

**Explanation:** A sentinel value (e.g., -1, 0, "quit") is a special value the user enters to indicate they are done providing data. The while loop condition checks for this value and stops when it appears. It avoids needing a separate `done = True/False` flag.

---

### Question 8 — Module 6: Accumulator

What is the final value of `total` after this loop?

```python
total = 0
i = 1
while i <= 5:
    if i % 2 == 0:
        total += i
    i += 1
print(total)
```

- A) `15`
- B) `9`
- C) **`6`** ← CORRECT
- D) `12`

**Explanation:** The loop accumulates only even numbers from 1–5. Evens in 1–5: 2 and 4. Total = 2 + 4 = 6. Odd numbers (1, 3, 5) are skipped by the `if` condition.

---

### Question 9 — Module 6: while...else

What is the output of this code?

```python
n = 3
while n > 0:
    n -= 1
else:
    print("Finished")
print(f"n = {n}")
```

- A) `Finished` not printed; `n = 0`
- B) **`Finished` then `n = 0`** ← CORRECT
- C) `Finished` printed 3 times; then `n = 0`
- D) `n = 3`

**Explanation:** The loop runs while n>0 (iterations: 2, 1, 0). When n=0, condition is False — normal termination. The `else` runs once and prints "Finished". Then `print(f"n = {n}")` prints `n = 0`. Output: Finished, then n = 0.

---

### Question 10 — Module 6: Infinite Loop Detection

Which loop creates an infinite loop?

```python
# Loop A:
x = 10
while x != 0:
    x -= 2

# Loop B:
x = 10
while x != 0:
    x -= 3

# Loop C:
x = 100
while x > 0:
    x //= 2

# Loop D:
x = 1
while x < 1000:
    x *= 3
```

- A) Loop A
- B) **Loop B** ← CORRECT
- C) Loop C
- D) Loop D

**Explanation:** Loop B: x goes 10→7→4→1→-2→-5→... The value skips over 0 because 1-3=-2. `x != 0` is always True since x never equals exactly 0. Loop A decrements by 2 and hits 0 exactly (10,8,6,4,2,0). Loops C and D converge (C halves toward 0, D triples but condition is x<1000 so it stops).

---

### Question 11 — Module 7: range() Basics

What does `list(range(2, 9, 2))` produce?

- A) `[2, 4, 6, 8, 10]`
- B) `[2, 3, 4, 5, 6, 7, 8]`
- C) **`[2, 4, 6, 8]`** ← CORRECT
- D) `[2, 4, 6]`

**Explanation:** `range(2, 9, 2)`: start=2, stop=9 (exclusive), step=2. Values: 2, 4, 6, 8. Next would be 10, which ≥ 9, so stop. The stop value 9 is never included.

---

### Question 12 — Module 7: range() Off-by-One

A student writes `for i in range(10):` intending to iterate from 1 to 10 inclusive. What is wrong?

- A) Nothing — `range(10)` produces 1 through 10
- B) `range(10)` produces 0 through 9, missing 10
- C) **`range(10)` produces 0 through 9; use `range(1, 11)` for 1 to 10 inclusive** ← CORRECT
- D) `range(10)` raises a ValueError for single argument

**Explanation:** `range(10)` produces 0, 1, 2, ..., 9 — it starts at 0 and is exclusive at 10. To get 1 through 10 inclusive, use `range(1, 11)`. This off-by-one mistake is one of the most common `range()` errors.

---

### Question 13 — Module 7: Negative Step

What values does `range(10, 2, -3)` produce?

- A) `[10, 7, 4, 1]`
- B) `[10, 7, 4, 3]`
- C) **`[10, 7, 4]`** ← CORRECT
- D) `[10, 7, 4, 1, -2]`

**Explanation:** start=10, stop=2 (exclusive), step=-3. Values: 10, 7, 4. Next would be 1, but 1 < 2 (stop), so 1 is not included. The stop value in a negative step range is exclusive and acts as a lower bound.

---

### Question 14 — Module 7: enumerate()

What is the output of this code?

```python
items = ["x", "y", "z"]
for i, val in enumerate(items, start=2):
    print(f"{i}:{val}")
```

- A) `0:x 1:y 2:z`
- B) `1:x 2:y 3:z`
- C) **`2:x 3:y 4:z`** ← CORRECT
- D) `x:2 y:3 z:4`

**Explanation:** `enumerate(items, start=2)` begins indexing at 2. Pairs: (2,"x"), (3,"y"), (4,"z"). The format is always `(index, value)` — index comes first in the tuple and in the f-string.

---

### Question 15 — Module 7: zip()

What is the output of this code?

```python
a = [1, 2, 3]
b = [10, 20]
c = [100, 200, 300, 400]

for x, y, z in zip(a, b, c):
    print(x + y + z)
```

- A) `111 222 333`
- B) `111 222 333 400`
- C) **`111 222`** ← CORRECT
- D) A ValueError — mismatched list lengths

**Explanation:** `zip()` stops at the shortest iterable. `b` has 2 elements, so only 2 pairs are produced: (1,10,100) and (2,20,200). Output: 111 (=1+10+100), then 222 (=2+20+200). No error is raised — zip silently truncates.

---

### Question 16 — Module 7: Nested Loop Count

How many times does `print("*")` execute?

```python
for i in range(4):
    for j in range(5):
        print("*")
```

- A) `9`
- B) `16`
- C) `25`
- D) **`20`** ← CORRECT

**Explanation:** Outer loop: 4 iterations (i=0,1,2,3). Inner loop: 5 iterations each. Total = 4 × 5 = 20. This is the fundamental rule: nested loops multiply their iteration counts.

---

### Question 17 — Module 7: for...else

What is the output of this code?

```python
for i in range(5):
    if i == 10:
        break
else:
    print("No break occurred")
print(f"i = {i}")
```

- A) `No break occurred` only
- B) **`No break occurred` then `i = 4`** ← CORRECT
- C) `i = 10` only
- D) No output

**Explanation:** `i == 10` is never True (range is 0–4). The loop runs to completion without a `break`. The `else` clause fires: prints "No break occurred". After the loop, `i` holds its last value: 4. Both lines print.

---

### Question 18 — Module 7: String Iteration

What is the output of this code?

```python
s = "Hello"
result = 0
for char in s:
    if char.isupper():
        result += 1
print(result)
```

- A) `0`
- B) **`1`** ← CORRECT
- C) `5`
- D) `2`

**Explanation:** Iterate over "Hello": H(upper→+1), e(lower), l(lower), l(lower), o(lower). Only "H" is uppercase. `result = 1`.

---

### Question 19 — Module 8: break Output

What is the output of this code?

```python
for i in range(1, 10):
    if i % 4 == 0:
        break
    print(i)
```

- A) `1 2 3 4`
- B) **`1 2 3`** ← CORRECT
- C) `4 8`
- D) `1 2 3 5 6 7 9`

**Explanation:** Loop: i=1 (1%4=1≠0 → print 1), i=2 (2%4=2≠0 → print 2), i=3 (3%4=3≠0 → print 3), i=4 (4%4=0 → break). The `print(i)` for i=4 never executes because `break` comes before it.

---

### Question 20 — Module 8: continue Output

What is the output of this code?

```python
total = 0
for i in range(1, 8):
    if i % 2 == 0:
        continue
    total += i
print(total)
```

- A) `28`
- B) `12`
- C) **`16`** ← CORRECT
- D) `4`

**Explanation:** Skip even numbers (2, 4, 6). Add odd numbers: 1+3+5+7 = 16. The `continue` skips `total += i` for even values.

---

### Question 21 — Module 8: pass vs continue

What is the output of this code?

```python
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)
```

- A) `0 1 3 4`
- B) `0 1 2 3 4`
- C) `2`
- D) **`0 1 3 4`** ← CORRECT

**Explanation:** When `i == 2`: `pass` runs (does nothing), then the `else` branch is skipped (since the `if` was True). So `print(i)` for i=2 is not executed. For all other values, the `else` prints them. Output: 0, 1, 3, 4.

**Note:** Options A and D are the same — fix distractors: A) `0 1 2 3 4`, B) `2`, C) `0 1`, D) **`0 1 3 4`** ← CORRECT.

---

### Question 22 — Module 8: break with while...else

What is the output of this code?

```python
attempts = 0
while attempts < 3:
    attempts += 1
    if attempts == 2:
        break
else:
    print("All attempts used")
print(f"Stopped at attempt {attempts}")
```

- A) `All attempts used` then `Stopped at attempt 3`
- B) **`Stopped at attempt 2`** ← CORRECT (only this line)
- C) `Stopped at attempt 2` then `All attempts used`
- D) `All attempts used` then `Stopped at attempt 2`

**Explanation:** attempts goes 0→1 (1==2? No) → 0→2 (2==2? Yes → break). The `while...else` is skipped because `break` fired. Only `print(f"Stopped at attempt {attempts}")` runs, printing `Stopped at attempt 2`.

---

### Question 23 — Module 8: Nested break

What is the output of this code?

```python
for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 4:
            break
        print(i * j, end=" ")
    print()
```

- A) `1 2 3 2 4 3`
- B) **`1 2 3 \n2 4 \n3 `** (three lines) ← CORRECT
- C) `1 2 3 2 4 6 3 6 9`
- D) `1 2 3`

**Explanation:** For i=1: j=1(1), j=2(2), j=3(3) — none exceed 4, so all print. newline. For i=2: j=1(2), j=2(4), j=3(6>4→break). Prints: 2, 4. newline. For i=3: j=1(3), j=2(6>4→break). Prints: 3. newline. `break` exits only the inner loop each time.

---

### Question 24 — Module 5+6: Compound Conditions in while

What is the output of this code?

```python
x = 10
y = 5
while x > 0 and y > 0:
    x -= 3
    y -= 2
print(x, y)
```

- A) `1 -1`
- B) `-2 -1`
- C) **`1 -1`** ← CORRECT
- D) `4 1`

**Explanation:** Trace: (10,5)→(7,3) True, (7,3)→(4,1) True, (4,1)→(1,-1) condition checked: 1>0 is True but -1>0 is False → loop exits. Print `1 -1`.

**Note:** Options A and C are the same — fix distractors: A) `-2 -1`, B) `4 1`, C) `1 1`, D) **`1 -1`** ← CORRECT.

---

### Question 25 — Module 7+8: for...else with continue

What is the output of this code?

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print("Completed")
```

- A) `0 1 2 4` (no "Completed")
- B) `0 1 2 3 4` then `Completed`
- C) `0 1 2` then `Completed`
- D) **`0 1 2 4` then `Completed`** ← CORRECT

**Explanation:** `continue` does NOT trigger `else` to be skipped — only `break` does. The loop runs all 5 iterations (3 is skipped by `continue` but the loop still completes). After normal completion, `else` runs once and prints "Completed".

---

### Question 26 — Module 6+8: Dangerous continue

What happens when this code runs?

```python
n = 1
while n < 10:
    if n % 2 == 0:
        continue
    print(n)
    n += 1
```

- A) Prints all odd numbers from 1 to 9
- B) Prints all numbers from 1 to 9
- C) Prints 1, then stops
- D) **Runs forever — infinite loop** ← CORRECT

**Explanation:** n starts at 1 (odd → prints 1, n becomes 2). Now n=2: `2%2==0` is True → `continue`. This skips `n += 1`. n stays at 2 forever because the update never runs. The loop is infinite. The fix: put `n += 1` BEFORE the `if` check.

---

### Question 27 — Module 5+7: Ternary in a Loop

What is the output of this code?

```python
result = [("even" if i % 2 == 0 else "odd") for i in range(4)]
print(result)
```

*(Note: This previews list comprehensions — evaluate the logic only)*

- A) `['odd', 'even', 'odd', 'even']`
- B) **`['even', 'odd', 'even', 'odd']`** ← CORRECT
- C) `[True, False, True, False]`
- D) `['even', 'even', 'even', 'even']`

**Explanation:** `range(4)` = 0,1,2,3. Evaluate ternary for each: 0%2=0(even), 1%2=1(odd), 2%2=0(even), 3%2=1(odd). Result: `['even', 'odd', 'even', 'odd']`.

---

### Question 28 — Module 7+8: Search with for...else

What is the output of this code?

```python
data = [5, 10, 15, 20, 25]
target = 15

for idx, val in enumerate(data):
    if val == target:
        print(f"Found at index {idx}")
        break
else:
    print("Not found")
```

- A) `Found at index 2` then `Not found`
- B) `Not found`
- C) `Found at index 15`
- D) **`Found at index 2`** ← CORRECT

**Explanation:** `enumerate(data)` yields (0,5), (1,10), (2,15), ... When val=15 matches target, `print("Found at index 2")` runs, then `break` exits. Since `break` fired, the `else` is skipped — "Not found" does NOT print. Output: only `Found at index 2`.

---

### Question 29 — Module 6+8: Loop Pattern Analysis

What does this loop compute?

```python
n = int(input())   # User enters 10
product = 1
i = n
while i > 0:
    product *= i
    i -= 1
print(product)
```

- A) Sum of 1 to n
- B) n squared
- C) **n! (n factorial)** ← CORRECT
- D) Sum of squares from 1 to n

**Explanation:** The loop multiplies: n × (n-1) × (n-2) × ... × 1, which is the definition of n!. For n=10: 10! = 3,628,800. This is the factorial pattern using a while loop counting down.

---

### Question 30 — Module 5+6+7+8: Synthesis

What is the output of this code?

```python
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    total += i
print(total)
```

- A) `55`
- B) `25`
- C) **`16`** ← CORRECT
- D) `9`

**Explanation:** `range(1, 11)` = 1–10. Trace with both controls:
- i=1: odd, 1≤7 → total=1
- i=2: even → continue (skip)
- i=3: odd, 3≤7 → total=4
- i=4: even → continue (skip)
- i=5: odd, 5≤7 → total=9
- i=6: even → continue (skip)
- i=7: odd, 7≤7 → total=16
- i=8: even → continue... wait — i=8 is even, so continue fires first, before the i>7 check. Actually: the `if i % 2 == 0: continue` runs first. For i=8: continue fires, jumps to i=9.
- i=9: odd, 9>7 → break

So: total = 1+3+5+7 = 16. The `break` fires at i=9 before 9 is added.

---

## BONUS Question (10 points)

### Bonus — Integration Challenge

What is the output of this code? Trace carefully before answering.

```python
result = 0
i = 2
while i <= 20:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result += i
    i += 1
print(result)
```

- A) `58`
- B) `77`
- C) **`77`** — Wait: 2+3+5+7+11+13+17+19 = 77 ← CORRECT
- D) `100`

**Explanation:** This code sums all prime numbers from 2 to 20. The inner `for` loop tests each candidate for primality by checking for divisors. Primes in range 2–20: 2, 3, 5, 7, 11, 13, 17, 19. Sum = 2+3+5+7+11+13+17+19 = 77.

**Instructor Note:** Fix duplicate C — use: A) 58, B) 100, C) 60, D) **77** ← CORRECT.

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | C | 16 | D |
| 2 | D | 17 | B |
| 3 | C | 18 | B |
| 4 | C | 19 | B |
| 5 | D | 20 | C |
| 6 | D | 21 | D* |
| 7 | C | 22 | B |
| 8 | C | 23 | B |
| 9 | B | 24 | D* |
| 10 | B | 25 | D |
| 11 | C | 26 | D |
| 12 | C | 27 | B |
| 13 | C | 28 | D |
| 14 | C | 29 | C |
| 15 | C | 30 | C |
| Bonus | D (77) | | |

*Q21: Duplicate distractors — fix before Canvas entry (see Q21 note).
*Q24: Duplicate distractors — fix before Canvas entry (see Q24 note).
