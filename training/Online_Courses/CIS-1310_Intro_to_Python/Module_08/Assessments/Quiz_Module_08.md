# Quiz: Module 8 — Loop Control: break, continue, pass

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

What is the output of this code?

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

- A) `0 1 2 3 4`
- B) **`0 1 2 3`** ← CORRECT
- C) `4 5 6 7 8 9`
- D) `0 1 2 3 4 5 6 7 8 9`

**Explanation:** When `i` reaches 4, `break` fires and the loop exits immediately. The `print(i)` line for `i == 4` is never reached because `break` comes first. Output: 0, 1, 2, 3.

---

### Question 2

What is the output of this code?

```python
for i in range(7):
    if i % 2 == 0:
        continue
    print(i)
```

- A) `0 2 4 6`
- B) `0 1 2 3 4 5 6`
- C) **`1 3 5`** ← CORRECT
- D) `1 2 3 4 5 6`

**Explanation:** `continue` skips the rest of the current iteration when the condition is True. Even numbers (0, 2, 4, 6) trigger `continue` and their `print` is skipped. Odd numbers (1, 3, 5) pass the check and print. Note: `range(7)` goes 0–6.

---

### Question 3

When a `for` loop has an `else` clause and a `break` statement fires, what happens?

- A) The `else` block executes, then the loop ends
- B) The `else` block executes before the `break`
- C) The `else` block executes after the break, once
- D) **The `else` block is skipped entirely** ← CORRECT

**Explanation:** The `else` clause on a loop runs only when the loop terminates **normally** (all items exhausted, or `while` condition becomes False). If `break` exits the loop, the `else` is skipped. This is the entire point of `for...else` / `while...else` — it lets you detect whether a search succeeded (`break` fired) or failed (`else` runs).

---

### Question 4

What is the output of this code?

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print("Done")
```

- A) `0 1 2 4` (no "Done")
- B) `0 1 2 3 4` then `Done`
- C) **`0 1 2 4` then `Done`** ← CORRECT
- D) `0 1 2` then `Done`

**Explanation:** `continue` skips `print(i)` for `i == 3`, so 3 is not printed. The loop still completes normally (not via `break`), so the `else` block runs and prints `"Done"`. Output: 0, 1, 2, 4, then Done.

---

### Question 5

What does the `pass` statement do?

- A) It pauses the loop for one iteration
- B) It skips to the next iteration like `continue`
- C) It exits the loop like `break`
- D) **It does nothing — it is a no-operation placeholder** ← CORRECT

**Explanation:** `pass` is a null statement. It satisfies Python's syntactic requirement for an indented block but performs no action. The loop (or function, class, etc.) continues executing as if the `pass` were not there. It is used as a placeholder for code not yet written.

---

### Question 6

What is the output of this code?

```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```

- A) `0 1 3 4`
- B) `0 1`
- C) `2`
- D) **`0 1 2 3 4`** ← CORRECT

**Explanation:** `pass` does nothing. When `i == 2`, `pass` executes and has no effect — execution falls through to `print(i)`, which prints `2`. All five values (0–4) are printed. This contrasts with `continue`, which would skip `print(i)` for `i == 2`.

---

### Question 7

What is the output of this code?

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"{i},{j}")
```

- A) `1,1 1,2 2,1 2,2 3,1 3,2`
- B) **`1,1 2,1 3,1`** ← CORRECT
- C) `1,1 1,2 1,3 2,1 2,2 2,3 3,1 3,2 3,3`
- D) `1,1`

**Explanation:** `break` exits only the **inner** loop. For each value of `i` (1, 2, 3): j starts at 1, prints `i,1`, then j reaches 2 and `break` exits the inner loop. The outer loop continues to the next `i`. Three lines print: `1,1`, `2,1`, `3,1`.

---

### Question 8

Which loop is DANGEROUS and likely causes an infinite loop?

```python
# Loop A:
n = 0
while n < 5:
    if n == 3:
        continue
    print(n)
    n += 1

# Loop B:
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
```

- A) **Loop A** ← CORRECT
- B) Loop B
- C) Both loops are infinite
- D) Neither loop is infinite

**Explanation:** In Loop A, when `n == 3`, `continue` skips `n += 1` — so `n` stays at 3 forever. In Loop B, `n += 1` runs BEFORE `continue`, so `n` still increments past 3. Always ensure the update statement in a `while` loop runs before `continue` if the loop variable is what `continue` is based on.

---

### Question 9

What is the output of this code?

```python
numbers = [2, 4, 6, 8, 10]
target = 5

for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not found.")
```

- A) `Found!`
- B) `Found!` then `Not found.`
- C) No output
- D) **`Not found.`** ← CORRECT

**Explanation:** `5` is not in `numbers`. The loop exhausts all items without `break` firing. When the loop ends normally (all items visited), the `else` block runs and prints `"Not found."`. If `5` had been in the list, `break` would have fired and `"Not found."` would NOT have printed.

---

### Question 10

What is the output of this code?

```python
total = 0
for i in range(1, 11):
    if i % 3 == 0:
        continue
    total += i
print(total)
```

- A) `55`
- B) `18`
- C) `37`
- D) **`37`** ← CORRECT

**Explanation:** `range(1, 11)` = 1–10. Skip multiples of 3: skip 3, 6, 9. Sum the rest: 1+2+4+5+7+8+10 = 37. Verification: total 1–10 = 55; subtract 3+6+9 = 18; 55–18 = 37.

**Instructor Note:** Options C and D are both 37 — fix distractors before Canvas entry. Suggested: A) 55, B) 45, C) 28, D) **37** ← CORRECT.

---

### Question 11

What is the output of this code?

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)
else:
    print("Done")
```

- A) `1 2 3` then `Done`
- B) `1 2` then `Done`
- C) **`1 2`** ← CORRECT (no "Done")
- D) `1 2 3 4 5`

**Explanation:** The loop runs: i=1 (print 1), i=2 (print 2), i=3 → `break` fires. Since `break` exits the loop, the `else` clause is skipped — `"Done"` is never printed. Output: just `1` and `2`.

---

### Question 12

What is the purpose of `while True:` combined with `break`?

- A) It creates a loop that runs exactly twice
- B) It is always a bug — infinite loops must be avoided
- C) It runs once regardless of any conditions
- D) **It is a valid pattern for loops that exit when an internal condition is met** ← CORRECT

**Explanation:** `while True:` is a deliberate infinite loop that relies on `break` inside the body to exit. This is the standard Python pattern for input validation loops, menu systems, and any situation where the exit condition can only be tested inside the loop body. It is perfectly valid and widely used in professional Python code.

---

### Question 13

What is the output of this code?

```python
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(f"{i}{j}", end=" ")
```

- A) `00 11 22`
- B) **`01 02 10 12 20 21`** ← CORRECT
- C) `01 02 10 12`
- D) `00 01 02 10 11 12 20 21 22`

**Explanation:** `continue` skips printing when `i == j` (the diagonal: 0,0 and 1,1 and 2,2). All other pairs print. The pairs that print: (0,1), (0,2), (1,0), (1,2), (2,0), (2,1). Output: `01 02 10 12 20 21`.

---

### Question 14

Which statement correctly describes `continue` in a `for` loop?

- A) It terminates the for loop and any enclosing loops
- B) It terminates only the innermost for loop
- C) It exits the current iteration and skips to the loop's `else` clause
- D) **It skips the remaining code in the current iteration and starts the next one** ← CORRECT

**Explanation:** `continue` causes the current iteration to end immediately. Execution jumps back to the loop header — the next item in the sequence (for) or condition check (while). The loop's `else` clause is not involved with `continue`. The loop continues running; `continue` does not terminate it.

---

### Question 15

What is the output of this code?

```python
found = False
for i in range(1, 20):
    if i * i > 150:
        found = True
        break

if found:
    print(f"First i where i² > 150: {i}")
else:
    print("None found")
```

- A) `First i where i² > 150: 12`
- B) **`First i where i² > 150: 13`** ← CORRECT
- C) `First i where i² > 150: 14`
- D) `None found`

**Explanation:** Check squares: 12² = 144 (≤150, continue), 13² = 169 (>150, break!). So `i = 13` when `break` fires. After the loop, `found = True` and `i = 13`, so `"First i where i² > 150: 13"` prints.

---

## Answer Key

| Q | A | Q | A |
|---|---|---|---|
| 1 | B | 9 | D |
| 2 | C | 10 | D* |
| 3 | D | 11 | C |
| 4 | C | 12 | D |
| 5 | D | 13 | B |
| 6 | D | 14 | D |
| 7 | B | 15 | B |
| 8 | A | | |

*Q10: Correct answer is D (37), but C and D are duplicates in the draft — fix distractors before Canvas entry.
