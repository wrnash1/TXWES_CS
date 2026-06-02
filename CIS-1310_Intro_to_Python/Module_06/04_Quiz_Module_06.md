# Quiz: Module 06 — Lists: The Workhorse Data Structure

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 06 topics.

---

### Question 1

What does `grades[-2]` return if `grades = [88, 72, 95, 61, 83]`?

- A) `72`
- B) `61`
- C) `83`
- D) `IndexError` — negative indices are not valid in Python

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `grades[-2]` counts two positions from the end. The last item (`-1`) is `83`, and the second-to-last (`-2`) is `61`, not `72`.
- *Why B is correct:* Negative indices count from the end. For a 5-item list: `[-5]=88, [-4]=72, [-3]=95, [-2]=61, [-1]=83`. So `grades[-2]` is `61`.
- *Why C is incorrect:* `grades[-1]` is `83` — the last item. `grades[-2]` is one step earlier.
- *Why D is incorrect:* Python fully supports negative indices. They are equivalent to `len(list) + negative_index`. `grades[-2]` = `grades[5 - 2]` = `grades[3]` = `61`.

---

### Question 2

What does `lst[1:4]` return if `lst = [10, 20, 30, 40, 50]`?

- A) `[10, 20, 30, 40]`
- B) `[20, 30, 40, 50]`
- C) `[20, 30, 40]`
- D) `[10, 20, 30]`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* This would be `lst[0:4]` — starting at index 0.
- *Why B is incorrect:* This would be `lst[1:]` — from index 1 to the end.
- *Why C is correct:* `lst[1:4]` includes indices 1, 2, and 3 — values `20`, `30`, `40`. The `stop` value `4` is always excluded.
- *Why D is incorrect:* This would be `lst[:3]` or `lst[0:3]` — starting at index 0 and stopping before index 3.

---

### Question 3

What does `my_list.sort()` return?

- A) The sorted list
- B) A new sorted list, leaving the original unchanged
- C) `None`
- D) The length of the sorted list

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `sort()` modifies the list in place but returns `None`. Assigning `result = my_list.sort()` gives you `None`, not the sorted list.
- *Why B is incorrect:* That is the behavior of the built-in `sorted()` function, not the `list.sort()` method.
- *Why C is correct:* `list.sort()` is a mutating method — it sorts the list in place and returns `None`. This is a deliberate Python design choice to prevent accidental double-sorting.
- *Why D is incorrect:* `sort()` returns `None`, not an integer. Use `len(my_list)` to get the length.

---

### Question 4

What is the output of the following code?

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) `TypeError` — `b` cannot modify `a`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `b = a` creates an alias, not a copy. Both `a` and `b` reference the same list object. Modifying through `b` modifies the shared object that `a` also refers to.
- *Why B is correct:* `b = a` makes `b` point to the same list as `a`. When `b.append(4)` adds an item to that list, it is visible through both `a` and `b`. `a` now contains `[1, 2, 3, 4]`.
- *Why C is incorrect:* `append()` adds to the end of the existing list — it does not replace the list.
- *Why D is incorrect:* There is no `TypeError` here. The code is valid and runs without error.

---

### Question 5

Which of the following creates an independent copy of `original = [1, 2, 3]`?

- A) `copy = original`
- B) `copy = original.sort()`
- C) `copy = original[:]`
- D) `copy = original + 0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `copy = original` creates an alias — both names point to the same list. Modifying `copy` modifies `original`.
- *Why B is incorrect:* `original.sort()` returns `None` — `copy` would be `None`, not a list.
- *Why C is correct:* `original[:]` creates a new list containing all items from `original`. This is a shallow copy — an independent list object. Other valid copy methods: `original.copy()` and `list(original)`.
- *Why D is incorrect:* `[1, 2, 3] + 0` raises `TypeError` — you cannot add a list and an integer.

---

### Question 6

What does the following list comprehension produce?

```python
[x**2 for x in range(1, 5) if x % 2 != 0]
```

- A) `[1, 4, 9, 16]`
- B) `[1, 9]`
- C) `[4, 16]`
- D) `[2, 4]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This would be the result without the filter condition — `x**2` for all x in 1, 2, 3, 4.
- *Why B is correct:* `range(1, 5)` gives 1, 2, 3, 4. The filter `x % 2 != 0` keeps only odd numbers: 1 and 3. Squaring those gives 1 and 9. Result: `[1, 9]`.
- *Why C is incorrect:* `[4, 16]` would result from `[x**2 for x in range(1, 5) if x % 2 == 0]` — squaring only even numbers.
- *Why D is incorrect:* `[2, 4]` does not match any straightforward reading of the expression. There is no path from this comprehension to those values.

---

### Question 7

What does `[0] * 4` produce?

- A) `[0, 4]`
- B) `0`
- C) `[0, 0, 0, 0]`
- D) `TypeError` — `*` cannot be used with lists

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `*` does not merge values — it repeats the list structure.
- *Why B is incorrect:* The result is a list, not a scalar multiplication.
- *Why C is correct:* `list * int` repeats the list `int` times. `[0] * 4` = `[0, 0, 0, 0]`. This is commonly used to initialize a fixed-size list with default values.
- *Why D is incorrect:* `*` is a valid operator for lists. `list * int` (or `int * list`) repeats the list.

---

### Question 8

What does `'banana' in ['apple', 'banana', 'cherry']` return?

- A) `1` — the index where 'banana' is found
- B) `True`
- C) `'banana'` — the matching item
- D) `False` — `in` only works with strings, not lists

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `in` is a membership test, not an index lookup. It returns `True` or `False`. To get the index, use `list.index(value)`.
- *Why B is correct:* `in` tests whether a value is present in a sequence. `'banana'` is in the list, so the result is `True`.
- *Why C is incorrect:* `in` returns a Boolean, not the matching item.
- *Why D is incorrect:* `in` works with lists, strings, tuples, sets, dicts, and any other iterable. It is not restricted to strings.

---

### Question 9

What is the output of this code?

```python
lst = [3, 1, 4, 1, 5, 9]
lst.reverse()
print(lst)
```

- A) `[9, 5, 1, 4, 1, 3]`
- B) `[1, 1, 3, 4, 5, 9]`
- C) `None`
- D) `[3, 1, 4, 1, 5, 9]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `reverse()` reverses the list in place. The original `[3, 1, 4, 1, 5, 9]` becomes `[9, 5, 1, 4, 1, 3]`.
- *Why B is incorrect:* That would be the result of `sorted(lst)` — sorting, not reversing.
- *Why C is incorrect:* `reverse()` does return `None`, but `print(lst)` prints the list itself — `lst` was modified in place, not replaced with `None`.
- *Why D is incorrect:* `reverse()` modifies the list. The original order is no longer what `lst` contains.

---

### Question 10

What does `matrix[2][1]` return if `matrix = [[1, 2], [3, 4], [5, 6]]`?

- A) `3`
- B) `4`
- C) `5`
- D) `6`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `matrix[2][1]` is row index 2, column index 1. Row 2 is `[5, 6]`. Column 1 of that row is `6`, not `3`.
- *Why B is incorrect:* `4` is at `matrix[1][1]` — row 1 (`[3, 4]`), column 1.
- *Why C is incorrect:* `5` is at `matrix[2][0]` — row 2 (`[5, 6]`), column 0.
- *Why D is correct:* `matrix[2]` is `[5, 6]` (third row, index 2). `[5, 6][1]` is `6`. Answer: `6`.
