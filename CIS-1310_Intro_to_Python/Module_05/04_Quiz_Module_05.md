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
