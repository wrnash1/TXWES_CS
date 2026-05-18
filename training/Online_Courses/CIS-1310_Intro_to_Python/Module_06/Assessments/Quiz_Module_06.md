# Quiz: Module 6 — While Loops

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 15 Questions | 2 points each = **30 points**
**Suggested Time:** 20 minutes
**PCAP Alignment:** Section 3 — Control Flow, Loops

---

## Canvas Entry Instructions

- **Question Type:** Multiple Choice | **Points:** 2 each | **Shuffle Answers:** Yes

---

## Questions

---

### Question 1

What is the output of the following code?

```python
x = 1
while x < 20:
    x *= 3
print(x)
```

- A) `9`
- B) `18`
- C) `20`
- D) **`27`** ← CORRECT

**Explanation:** Trace: x=1 (1<20 True → x=3), x=3 (3<20 True → x=9), x=9 (9<20 True → x=27), x=27 (27<20 False → stop). Output: `27`.

---

### Question 2

How many times does the following loop body execute?

```python
count = 10
while count > 0:
    count -= 3
```

- A) 3
- B) **4** ← CORRECT
- C) 10
- D) Infinite

**Explanation:** count goes: 10→7→4→1→-2. Condition checked: 10>0(T), 7>0(T), 4>0(T), 1>0(T), -2>0(F). Body executes 4 times.

---

### Question 3

Which component is MISSING from this while loop, causing an infinite loop?

```python
count = 0
while count < 5:
    print(count)
```

- A) The condition
- B) The initial value
- C) The colon
- D) **The update statement (count += 1)** ← CORRECT

**Explanation:** `count` is never incremented inside the loop body. It stays at `0` forever, and `0 < 5` is always `True`. Adding `count += 1` after `print(count)` fixes the infinite loop.

---

### Question 4

What is the output of this code?

```python
total = 0
i = 1
while i <= 4:
    total += i
    i += 1
print(total)
```

- A) `4`
- B) `5`
- C) `6`
- D) **`10`** ← CORRECT

**Explanation:** Accumulator pattern: total = 1+2+3+4 = 10. This is the classic sum of integers 1 to n.

---

### Question 5

What is the purpose of a sentinel value in a while loop?

- A) To initialize the loop counter variable
- B) To prevent the loop from running more than once
- C) **To provide a special input value that signals the loop to stop** ← CORRECT
- D) To store the loop result after it finishes

**Explanation:** A sentinel value (like -1 or "quit") is a value the user enters to indicate they are done entering data. The while loop checks for this value as its exit condition.

---

### Question 6

What is the output of this code?

```python
x = 2
while x < 100:
    x **= 2
print(x)
```

- A) `16`
- B) `64`
- C) `100`
- D) **`256`** ← CORRECT

**Explanation:** x=2 (2<100 T → x=4), x=4 (4<100 T → x=16), x=16 (16<100 T → x=256), x=256 (256<100 F → stop). Output: `256`.

---

### Question 7

When does the `else` clause of a `while...else` statement execute?

- A) Every time the loop body runs
- B) When the loop runs at least once
- C) Only when `break` is used
- D) **When the while condition becomes False (normal termination, not via break)** ← CORRECT

**Explanation:** The `else` block on a `while` loop runs after normal loop completion (when the condition becomes False). It does NOT run if the loop exits via a `break` statement. This allows detection of whether a search loop found what it was looking for.

---

### Question 8

What is the output of this while...else code (assuming user never types -1)?

```python
n = 5
while n > 0:
    n -= 1
else:
    print("Done")
```

- A) No output
- B) `Done` printed 5 times
- C) `Done` only if n reaches exactly 0
- D) **`Done` printed once after the loop** ← CORRECT

**Explanation:** The loop runs while n > 0 (iterations: 4, 3, 2, 1, 0). When n = 0, the condition `n > 0` is False — normal termination. The `else` block runs once: prints `"Done"`.

---

### Question 9

What is the final value of `result` after this loop?

```python
result = 1
n = 5
while n > 0:
    result *= n
    n -= 1
```

- A) `5`
- B) `15`
- C) `25`
- D) **`120`** ← CORRECT

**Explanation:** result = 1×5×4×3×2×1 = 120. This is the factorial of 5 (5!). The while loop counts down from 5 to 1, multiplying result by each value.

---

### Question 10

Which of the following while loop conditions creates an infinite loop?

- A) `while x != 0` (where x starts at 10 and decreases by 1 each iteration)
- B) `while count < 100` (where count starts at 0 and doubles each iteration)
- C) **`while x != 0` (where x starts at 10 and decreases by 3 each iteration)** ← CORRECT
- D) `while True:` (where a break statement is inside)

**Explanation:** Starting at 10 and subtracting 3 each time: 10→7→4→1→-2→-5→... The value skips over 0 and goes negative. `x != 0` is always True because x is never exactly 0. Option A decrements by 1, so it hits 0. Option B doubles, so it eventually exceeds 100. Option D has a break that exits it.

---

### Question 11

What is the output of this code?

```python
x = 10
while x > 0:
    x -= 4
print(x)
```

- A) `0`
- B) `2`
- C) `4`
- D) **`-2`** ← CORRECT

**Explanation:** x: 10→6→2→-2. When x=-2, condition `-2>0` is False, loop ends. `print(-2)`. The final value goes below 0 because 2-4=-2, and the condition isn't checked until after the subtraction.

---

### Question 12

Which statement about `while` loops is TRUE?

- A) The loop body always executes at least once
- B) The condition is checked after each iteration, not before
- C) **If the condition is False before the loop starts, the body never executes** ← CORRECT
- D) A `while` loop must have a numeric counter variable

**Explanation:** Python's `while` loop checks the condition BEFORE each iteration (including before the first). If the condition is False at the start, the body never runs. This is different from a do-while loop (which Python does not have natively). The body can execute 0 or more times.

---

### Question 13

What does this loop compute?

```python
n = int(input("Enter n: "))   # User enters 10
result = 0
i = 1
while i <= n:
    result += i * i
    i += 1
print(result)
```

- A) Sum of integers 1 to 10 = 55
- B) Sum of even squares from 1 to 10
- C) **Sum of squares from 1² to 10² = 385** ← CORRECT
- D) Product of integers 1 to 10

**Explanation:** The loop accumulates `i²` for i from 1 to 10: 1+4+9+16+25+36+49+64+81+100 = 385. `result += i * i` is "result = result + i-squared".

---

### Question 14

What is the purpose of `while True:` with a `break` inside?

- A) It always runs exactly once
- B) It creates an error — infinite loops are forbidden
- C) It runs until Python runs out of memory
- D) **It is a valid pattern for loops that exit when an internal condition is met** ← CORRECT

**Explanation:** `while True:` creates a nominally infinite loop. The loop exits via a `break` statement when some condition inside the body is met. This pattern is commonly used for input validation and menu-driven programs where the number of iterations is unknown in advance. It is perfectly valid Python.

---

### Question 15

A while loop runs exactly 0 times. Under what condition does this occur?

- A) When the loop body contains a `break` on the first line
- B) When the update variable is not modified in the loop
- C) Never — a while loop always runs at least once
- D) **When the while condition is False before the first iteration** ← CORRECT

**Explanation:** Python checks the `while` condition BEFORE the first iteration. If it is already False, the entire loop body is skipped. Example: `while 0 > 5:` — condition is always False, body never runs. This is unlike many learners expect (some confuse while with do-while).

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | D | 9 | D |
| 2 | B | 10 | C |
| 3 | D | 11 | D |
| 4 | D | 12 | C |
| 5 | C | 13 | C |
| 6 | D | 14 | D |
| 7 | D | 15 | D |
| 8 | D | | |
