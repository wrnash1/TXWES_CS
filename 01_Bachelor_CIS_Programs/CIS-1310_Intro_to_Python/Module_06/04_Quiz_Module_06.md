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

---

### Question 11

What is the output of this code?

```python
lst = [10, 20, 30, 40, 50]
print(lst[::2])
```

- A) `[10, 30, 50]`
- B) `[20, 40]`
- C) `[50, 40, 30, 20, 10]`
- D) `[10, 20]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `lst[::2]` uses the slice form `[start:stop:step]` with both start and stop omitted (defaulting to the whole list) and a step of 2. Every second element starting from index 0: indices 0, 2, 4 → values 10, 30, 50.
- *Why B is incorrect:* `[20, 40]` would be indices 1 and 3 — the odd-indexed elements. You'd need `lst[1::2]` for that.
- *Why C is incorrect:* That is the reversed list, produced by `lst[::-1]`.
- *Why D is incorrect:* `[10, 20]` would be `lst[:2]` — the first two elements.

---

### Question 12

What does `lst.pop(1)` do to `lst = ['a', 'b', 'c', 'd']`?

- A) Removes the last element and returns it
- B) Removes and returns the element at index 1, modifying the list
- C) Returns the element at index 1 without removing it
- D) Raises `IndexError` because `pop()` only works without arguments

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `lst.pop()` (no argument) removes and returns the last element. `lst.pop(1)` specifies index 1, which is `'b'`.
- *Why B is correct:* `lst.pop(index)` removes the element at the specified index and returns it. `lst.pop(1)` removes `'b'` and returns it. After the call, `lst = ['a', 'c', 'd']`.
- *Why C is incorrect:* `pop()` always removes the element. To read without removing, use `lst[1]` (indexing).
- *Why D is incorrect:* `pop()` accepts an optional index argument. Without an argument, it pops the last element. With an index, it pops that specific element.

---

### Question 13

What is the result of `sorted([3, 1, 4, 1, 5], reverse=True)`?

- A) `[1, 1, 3, 4, 5]`
- B) `[5, 4, 3, 1, 1]`
- C) `None`
- D) `[5, 4, 3, 2, 1]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* That is the ascending sort (`reverse=False`, which is the default). `reverse=True` sorts in descending order.
- *Why B is correct:* `sorted(iterable, reverse=True)` returns a new list sorted in descending order. `[5, 4, 3, 1, 1]` is the correct descending sort.
- *Why C is incorrect:* `sorted()` is the built-in function that returns a new sorted list. Only `list.sort()` (the in-place method) returns `None`.
- *Why D is incorrect:* `[5, 4, 3, 2, 1]` would require the original list to contain a `2`. The input list is `[3, 1, 4, 1, 5]` — no `2` is present.

---

### Question 14

What is the output of this code?

```python
nums = [1, 2, 3, 4, 5]
nums.insert(2, 99)
print(nums)
```

- A) `[1, 2, 99, 3, 4, 5]`
- B) `[1, 2, 3, 99, 4, 5]`
- C) `[99, 1, 2, 3, 4, 5]`
- D) `[1, 2, 3, 4, 99, 5]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `insert(index, value)` inserts `value` before the element currently at `index`. `insert(2, 99)` inserts `99` before index 2 (the value `3`). Result: `[1, 2, 99, 3, 4, 5]`.
- *Why B is incorrect:* That would be inserting before index 3 (the value `4`): `insert(3, 99)`.
- *Why C is incorrect:* That would be `insert(0, 99)` — inserting at the beginning.
- *Why D is incorrect:* That would be inserting before index 4 (the value `5`): `insert(4, 99)`.

---

### Question 15

What does the following list comprehension produce?

```python
[len(word) for word in ['cat', 'python', 'go']]
```

- A) `['cat', 'python', 'go']`
- B) `[3, 6, 2]`
- C) `[3]`
- D) `TypeError: len() requires a string argument`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The expression is `len(word)`, not `word`. The comprehension applies `len()` to each word, producing the character count, not the word itself.
- *Why B is correct:* `len('cat')=3`, `len('python')=6`, `len('go')=2`. The comprehension collects these into `[3, 6, 2]`.
- *Why C is incorrect:* `[3]` would result if only one word were in the list. All three words are processed.
- *Why D is incorrect:* `len()` works on strings — this is one of its primary use cases. No TypeError is raised.

---

### Question 16

What is the difference between `list.remove(x)` and `list.pop(i)`?

- A) `remove(x)` deletes by value; `pop(i)` deletes by index and returns the removed item
- B) `remove(x)` deletes by index; `pop(i)` deletes by value
- C) Both delete by value; `pop()` also prints the item
- D) `remove(x)` returns the removed item; `pop(i)` returns `None`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `remove(x)` searches the list for the first occurrence of value `x` and removes it — no return value (returns `None`). `pop(i)` removes the item at index `i` and returns it. These are complementary operations for different use cases.
- *Why B is incorrect:* The descriptions are reversed. `remove()` works by value; `pop()` works by index.
- *Why C is incorrect:* `pop()` does not print anything — it returns the removed item. `remove()` returns `None`.
- *Why D is incorrect:* The return values are backwards. `remove()` returns `None`; `pop()` returns the removed item.

---

### Question 17

What does `[x for x in range(10) if x % 3 == 0]` produce?

- A) `[0, 3, 6, 9]`
- B) `[3, 6, 9]`
- C) `[1, 4, 7]`
- D) `[0, 3, 6]`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `range(10)` gives 0–9. Values where `x % 3 == 0` (divisible by 3): 0, 3, 6, 9. Note that 0 is included because `0 % 3 == 0`.
- *Why B is incorrect:* `0` is excluded from this option but `0 % 3 == 0` is `True`, so `0` must be included.
- *Why C is incorrect:* `[1, 4, 7]` are values where `x % 3 == 1`, not `0`.
- *Why D is incorrect:* `9` is missing. `9 % 3 == 0` is `True` and 9 is within `range(10)` (which includes 9).

---

### Question 18

What is the output of this code?

```python
a = [1, 2, 3]
b = a.copy()
a.append(4)
print(b)
```

- A) `[1, 2, 3, 4]`
- B) `[1, 2, 3]`
- C) `[4]`
- D) `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `b = a.copy()` creates an independent shallow copy. Modifying `a` after the copy does not affect `b`.
- *Why B is correct:* `.copy()` creates a new list with the same elements. After `a.append(4)`, `a` has four elements but `b` still has only three — they are separate objects.
- *Why C is incorrect:* `b` contains all three elements from the original list, not just the appended value.
- *Why D is incorrect:* `b` is a list, not `None`. `a.copy()` returns the new list, not `None`.

---

### Question 19

What happens when you try to access `lst[5]` on `lst = [1, 2, 3]`?

- A) Python returns `None` as a default value
- B) Python returns the last element (`3`) as a fallback
- C) Python raises `IndexError: list index out of range`
- D) Python returns `0` as the default for out-of-range numeric lists

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python does not silently return `None` for out-of-bounds access. Returning `None` would hide bugs. Python raises an explicit error.
- *Why B is incorrect:* Python never silently falls back to the last element. That behavior must be coded explicitly with clamping.
- *Why C is correct:* Accessing an index outside the valid range raises `IndexError: list index out of range`. Valid indices for a 3-element list are 0, 1, 2 (and -3, -2, -1 for negative indexing).
- *Why D is incorrect:* Python has no concept of a "default value" for list access. Out-of-range access always raises `IndexError`.

---

### Question 20

What is the output of this code?

```python
words = ['delta', 'alpha', 'gamma', 'beta']
words.sort()
print(words[0], words[-1])
```

- A) `delta gamma`
- B) `alpha gamma`
- C) `alpha delta`
- D) `beta gamma`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* After sorting, `words[0]` is the first alphabetically. `delta` is not first alphabetically — `alpha` is.
- *Why B is correct:* After `.sort()`, `words = ['alpha', 'beta', 'delta', 'gamma']`. `words[0]` is `'alpha'` and `words[-1]` (last) is `'gamma'`.
- *Why C is incorrect:* `delta` is not the last alphabetically — `gamma` comes after `delta`.
- *Why D is incorrect:* `beta` is the second element after sorting, not the first (`words[0]`).
