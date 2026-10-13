# Quiz: Module 05 — Loops: Iteration with while and for

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 05 topics.

---

### Question 1

How many values does `range(1, 10, 3)` produce, and what are they?

- A) 3 values: 1, 4, 7
- B) 4 values: 1, 4, 7, 10
- C) 3 values: 3, 6, 9
- D) 4 values: 1, 3, 6, 9

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `range(1, 10, 3)` starts at 1 and increments by 3: 1, 4, 7. The next value would be 10, but `stop=10` is excluded, so the sequence ends at 7. That is 3 values.
- *Why B is incorrect:* 10 is the `stop` value and is always excluded. `range(start, stop, step)` never includes the `stop` value itself.
- *Why C is incorrect:* The starting value is 1, not 3. `range(1, 10, 3)` starts at 1 and steps by 3 from there.
- *Why D is incorrect:* The step is 3, meaning each value is 3 more than the last: 1, 4, 7. The gaps between values are uniform at 3.

---

### Question 2

What does the following code output?

```python
for i in range(3):
    print(i, end=' ')
```

- A) `1 2 3`
- B) `0 1 2`
- C) `0 1 2 3`
- D) `1 2`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `range(stop)` starts at 0, not 1. To get `1 2 3`, you would use `range(1, 4)`.
- *Why B is correct:* `range(3)` is equivalent to `range(0, 3)` — it produces 0, 1, 2. The `stop` value 3 is excluded. `end=' '` puts spaces between values instead of newlines.
- *Why C is incorrect:* `range(3)` does not include 3. To include 3, you would need `range(4)` or `range(0, 4)`.
- *Why D is incorrect:* This would require `range(1, 3)` — starting at 1, stopping before 3.

---

### Question 3

When does the `else` clause of a `for` loop execute?

- A) When the loop body raises an exception
- B) When the loop condition becomes False on the first check
- C) When the loop finishes normally without a `break` statement being executed
- D) Every time the loop body completes an iteration

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An exception in the loop body propagates upward — it does not trigger `else`. The `else` clause is not an error handler.
- *Why B is incorrect:* There is no "condition" in a `for` loop the same way there is in `while`. For a `for` loop over an empty iterable, the body never runs — but the `else` clause still executes (since no `break` was hit).
- *Why C is correct:* The `else` clause runs when the loop exhausts its iterable without encountering a `break`. This is the "successful completion without early exit" signal.
- *Why D is incorrect:* `else` does not run on each iteration — it runs once, after the loop, and only if `break` was never executed.

---

### Question 4

What is the output of this code?

```python
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
else:
    print('done')
print('end')
```

- A) `done` then `end`
- B) `end` only
- C) `done` only
- D) Nothing — `break` prevents any output

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `break` fires when `n == 3`, which causes the loop to exit early. Because `break` was executed, the `else` clause is skipped. `done` is never printed.
- *Why B is correct:* The loop runs for n=1 and n=2 (no break), then n=3 triggers `break`. The `else` clause is skipped. Execution continues after the loop, reaching `print('end')`.
- *Why C is incorrect:* `done` is inside the `else` clause which is skipped when `break` fires.
- *Why D is incorrect:* `print('end')` is outside and after the loop. It always runs regardless of how the loop exits.

---

### Question 5

What does the `continue` statement do inside a loop?

- A) Exits the loop immediately
- B) Restarts the loop from the beginning, resetting all variables
- C) Skips the rest of the current iteration and moves to the next one
- D) Pauses execution until the user presses Enter

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* That is what `break` does. `continue` does not exit the loop.
- *Why B is incorrect:* `continue` does not restart the loop or reset variables. The loop variable advances to its next value (for `for`) or the condition is re-evaluated (for `while`).
- *Why C is correct:* `continue` ends the current iteration early — any code after `continue` in the loop body is skipped for this iteration — and immediately re-evaluates the condition (while) or moves to the next item (for).
- *Why D is incorrect:* `continue` has no input-waiting behavior. It is a flow control statement, not an I/O operation.

---

### Question 6

What does `enumerate(['a', 'b', 'c'])` return when used in a `for` loop?

- A) `('a', 'b', 'c')` — a single tuple of all values
- B) `(0, 'a')`, `(1, 'b')`, `(2, 'c')` — index-value pairs
- C) `(1, 'a')`, `(2, 'b')`, `(3, 'c')` — 1-based index-value pairs by default
- D) `0`, `1`, `2` — only the indices, not the values

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `enumerate()` does not bundle all items into one tuple — it yields one `(index, value)` pair per iteration.
- *Why B is correct:* `enumerate()` wraps each item with its 0-based index, yielding `(0, 'a')`, `(1, 'b')`, `(2, 'c')`. The index starts at 0 by default.
- *Why C is incorrect:* The default starting index is 0, not 1. Use `enumerate(lst, start=1)` to begin at 1.
- *Why D is incorrect:* `enumerate()` always includes both the index and the value. If you need only indices, use `range(len(lst))`.

---

### Question 7

What is the output of this code?

```python
total = 0
for i in range(1, 5):
    total += i
print(total)
```

- A) `10`
- B) `15`
- C) `6`
- D) `4`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `range(1, 5)` produces 1, 2, 3, 4. The accumulator adds each: 0+1=1, 1+2=3, 3+3=6, 6+4=10. Total is 10.
- *Why B is incorrect:* 15 is the sum of 1 through 5. But `range(1, 5)` excludes 5 — to get 15, you need `range(1, 6)`.
- *Why C is incorrect:* 6 is the sum of 1+2+3, which is only the first 3 values. The loop also adds 4.
- *Why D is incorrect:* 4 is just the last value added, not the cumulative total.

---

### Question 8

What is the output of the following nested loop code?

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

- A) 4 lines of output
- B) 5 lines of output
- C) 6 lines of output
- D) 2 lines of output

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* 4 = 2+2. The multiplication of 2 outer iterations × 3 inner iterations = 6 total, not 4.
- *Why B is incorrect:* 5 is neither the sum nor the product of 2 and 3.
- *Why C is correct:* The outer loop runs 2 times (i=0, i=1). For each outer iteration, the inner loop runs 3 times (j=0, j=1, j=2). Total iterations: 2 × 3 = 6. Six lines are printed.
- *Why D is incorrect:* 2 is only the number of outer iterations. Each outer iteration triggers a full inner loop of 3 iterations.

---

### Question 9

What does `zip([1, 2, 3], ['a', 'b'])` produce?

- A) `[(1, 'a'), (2, 'b'), (3, None)]`
- B) `[(1, 'a'), (2, 'b')]`
- C) `[(1, 2, 3), ('a', 'b')]`
- D) `ValueError` — the lists must be the same length

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `zip()` does not pad shorter iterables with `None`. That behavior requires `itertools.zip_longest()`, not the built-in `zip()`.
- *Why B is correct:* `zip()` stops at the shortest iterable. `['a', 'b']` has 2 items, so `zip()` produces only 2 pairs: `(1, 'a')` and `(2, 'b')`. The value `3` from the first list is discarded.
- *Why C is incorrect:* `zip()` pairs corresponding elements together across iterables — it does not group each iterable as its own tuple.
- *Why D is incorrect:* `zip()` does not raise an error when iterables have different lengths. It simply stops when the shortest is exhausted.

---

### Question 10

What kind of error is caused by the following code?

```python
count = 0
while count < 5:
    print(count)
```

- A) `SyntaxError` — `while` requires an `else` clause
- B) `NameError` — `count` is not defined inside the loop
- C) An infinite loop — the program never terminates
- D) `IndentationError` — the loop body must be on the same line

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `else` is optional for `while` loops. The code is syntactically valid.
- *Why B is incorrect:* `count` is defined before the loop and is visible inside the loop body. `NameError` is not raised.
- *Why C is correct:* `count` is never incremented inside the loop body. The condition `count < 5` remains `True` forever because `count` stays at 0. The program prints `0` infinitely until interrupted with `Ctrl+C`.
- *Why D is incorrect:* The loop body is correctly indented on a separate line. Python does not require the body on the same line as the `while` statement (though a single-statement body technically could be).

---

### Question 11

What is the output of this code?

```python
for i in range(5):
    if i % 2 == 0:
        continue
    print(i, end=' ')
```

- A) `0 2 4`
- B) `1 3`
- C) `0 1 2 3 4`
- D) `1 3 5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `0 2 4` are the even numbers (where `i % 2 == 0`). The `continue` statement skips those iterations — only odd numbers print.
- *Why B is correct:* `continue` skips to the next iteration when the condition is true (even numbers). So only the odd values 1 and 3 reach `print()`. `range(5)` produces 0,1,2,3,4 — odd values are 1 and 3.
- *Why C is incorrect:* All five values would print if `continue` were removed.
- *Why D is incorrect:* `5` is not in `range(5)` — the range stops before 5.

---

### Question 12

What does `range(10, 0, -2)` produce?

- A) `10, 8, 6, 4, 2`
- B) `10, 8, 6, 4, 2, 0`
- C) `0, 2, 4, 6, 8, 10`
- D) An empty sequence

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `range(10, 0, -2)` starts at 10, steps by -2 (counting down), and stops before reaching 0. Values: 10, 8, 6, 4, 2. The stop value 0 is excluded.
- *Why B is incorrect:* The stop value is always excluded. `range(10, 0, -2)` will not include 0.
- *Why C is incorrect:* That is ascending order. The step is -2, so the sequence counts down, not up.
- *Why D is incorrect:* The range is non-empty because the step (-2) moves from start (10) toward stop (0). An empty range would result from a step that moves away from the stop value (e.g., `range(0, 10, -1)`).

---

### Question 13

What is the output of the following code?

```python
for i in range(3):
    for j in range(3):
        if i == j:
            break
    print(i, j)
```

- A) Three lines showing `0 0`, `1 1`, `2 2`
- B) Three lines showing `0 2`, `1 2`, `2 2`
- C) One line: `2 2`
- D) Nine lines showing all combinations

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* For each value of `i`, the inner loop starts at `j=0`. When `i == j`, `break` exits the inner loop. So the inner loop stops as soon as `j` equals `i`. After the inner break, `print(i, j)` runs with the values at the time of break: `i=0,j=0`; `i=1,j=1`; `i=2,j=2`.
- *Why B is incorrect:* `j=2` after every inner loop would only occur if the inner loop always ran to completion. The `break` stops it early.
- *Why C is incorrect:* `break` only exits the inner loop, not the outer loop. The outer loop still iterates all three values of `i`.
- *Why D is incorrect:* Nine lines would result with no `break`. The `break` causes the inner loop to exit early on each outer iteration.

---

### Question 14

Which of the following correctly demonstrates the `for-else` pattern to search a list for a target value?

Consider these four approaches (pseudocode described in each option):

- A) Loop over `numbers`; when `x == target`, print `found`. After the loop (at zero indentation), always print `not found`.
- B) Loop over `numbers`; when `x == target`, print `found` then `break`. Attach an `else` clause to the `for` that prints `not found`.
- C) Loop over `numbers`; when `x == target`, print `found` (no `break`). Attach an `else` clause to the `for` that prints `not found`.
- D) Loop over `numbers`; when `x != target`, `continue`. Otherwise print `found`. After the loop (at zero indentation), always print `not found`.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `print('not found')` is outside the loop at zero indentation, so it runs unconditionally after every loop — even when the target was found. This always prints `not found`.
- *Why B is correct:* The `break` exits the loop when the target is found, which causes the `else` clause to be skipped. The `else` only runs when the loop exhausts the iterable without hitting `break` — meaning the target was not found. This is the canonical `for-else` search pattern.
- *Why C is incorrect:* Without `break`, the loop always runs to completion regardless of whether the target was found. Because `break` never fires, the `else` always executes, printing `not found` even after having printed `found`.
- *Why D is incorrect:* `print('not found')` is outside the loop at zero indentation and runs unconditionally after the loop completes, regardless of whether the target was found.

---

### Question 15

What is the output of `list(zip('AB', [1, 2, 3]))`?

- A) `[('A', 1), ('B', 2), ('', 3)]`
- B) `[('A', 1), ('B', 2)]`
- C) `[('A', 'B'), (1, 2, 3)]`
- D) `ValueError: iterables must be the same length`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `zip()` does not pad shorter iterables. When the shorter iterable is exhausted, `zip()` stops. No empty strings or `None` values are inserted.
- *Why B is correct:* The string `'AB'` has 2 characters; the list has 3 elements. `zip()` stops at the shorter one, producing `[('A', 1), ('B', 2)]`. The `3` from the list is silently dropped.
- *Why C is incorrect:* `zip()` pairs corresponding elements across iterables — it does not group each iterable as a whole. `('A', 'B')` and `(1, 2, 3)` would be the result of a different operation.
- *Why D is incorrect:* `zip()` does not raise `ValueError` for mismatched lengths. It silently stops at the shortest iterable.

---

### Question 16

How many times does the body of the following `while` loop execute?

```python
n = 1
while n < 100:
    n *= 2
```

- A) 6
- B) 7
- C) 99
- D) 100

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* After 6 iterations: 1→2→4→8→16→32→64. Since 64 < 100, the condition is still `True` and the loop runs again.
- *Why B is correct:* Trace: n=1→2→4→8→16→32→64→128. After 7 iterations, n=128. The condition `128 < 100` is `False`, so the loop exits. The body ran 7 times.
- *Why C is incorrect:* 99 iterations would occur with `n += 1`. Doubling reaches 100+ much faster.
- *Why D is incorrect:* Same reasoning as C — exponential growth means far fewer iterations than linear counting.

---

### Question 17

What is the output of this code?

```python
result = 1
for i in range(1, 6):
    result *= i
print(result)
```

- A) `15`
- B) `120`
- C) `5`
- D) `720`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* 15 is the sum of 1+2+3+4+5. This code uses `*=` (multiplication), not `+=` (addition).
- *Why B is correct:* `range(1, 6)` produces 1,2,3,4,5. The accumulator multiplies: 1×1=1, 1×2=2, 2×3=6, 6×4=24, 24×5=120. This is `5!` (5 factorial).
- *Why C is incorrect:* 5 is only the last value in the range, not the accumulated product.
- *Why D is incorrect:* 720 is `6!` (6 factorial). `range(1, 6)` stops before 6.

---

### Question 18

What does `enumerate(['x', 'y', 'z'], start=1)` yield?

- A) `(0, 'x')`, `(1, 'y')`, `(2, 'z')`
- B) `(1, 'x')`, `(2, 'y')`, `(3, 'z')`
- C) `('x', 1)`, `('y', 2)`, `('z', 3)`
- D) `(1, 2, 3)` — only the indices

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That is the default `start=0` behavior. The `start=1` argument shifts the index sequence to begin at 1.
- *Why B is correct:* `enumerate(iterable, start=N)` begins the counter at N. With `start=1`, the pairs are `(1, 'x')`, `(2, 'y')`, `(3, 'z')`. This is useful when you want 1-based numbering in output.
- *Why C is incorrect:* `enumerate()` always yields `(index, value)` with the index first, then the value. The order is not reversed.
- *Why D is incorrect:* `enumerate()` yields both the index and the value as a tuple. It never discards the values.

---

### Question 19

What is the minimum number of statements required in a valid Python `while` loop body?

- A) 0 — an empty body is valid
- B) 1 — at least one statement is required
- C) 2 — you need the loop logic plus a `break` or increment
- D) There is no minimum — a `while` with no body is a `SyntaxError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python requires at least one statement in any block. A completely empty `while` body causes an `IndentationError`. To intentionally do nothing, use `pass`.
- *Why B is correct:* Every block in Python needs at least one statement. For an intentionally empty loop, use `pass`: `while condition: pass`. This is the minimal valid `while` loop.
- *Why C is incorrect:* You only need one statement (even just `pass`). Having a meaningful update or `break` is good practice but not a language requirement.
- *Why D is incorrect:* A `while` with `pass` as its body IS valid — the `pass` statement is the required placeholder.

---

### Question 20

What is the output of this code?

```python
for i in range(4):
    pass
print(i)
```

- A) `NameError: name 'i' is not defined`
- B) `3`
- C) `4`
- D) Nothing — `pass` prevents `i` from being assigned

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* In Python, the loop variable `i` retains its last value after the loop ends. It is still accessible in the scope where the loop was defined.
- *Why B is correct:* `range(4)` produces 0, 1, 2, 3. After the loop completes, `i` holds its last value: `3`. `print(i)` outputs `3`.
- *Why C is incorrect:* `4` is the `stop` value of the range and is never assigned to `i`. The last value `i` holds is `3`.
- *Why D is incorrect:* `pass` is a no-op statement — it does nothing and does not prevent any assignments. The loop variable `i` is assigned on every iteration.
