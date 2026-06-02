# Quiz: Module 07 — Tuples, Sets, and Advanced Sorting

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 07 topics.

---

### Question 1

What is the type of `t = (42)`?

- A) `tuple`
- B) `int`
- C) `list`
- D) `SyntaxError` — parentheses cannot be used around a literal

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `(42)` is NOT a tuple. Python treats parentheses around a single value as a grouping operator (like in arithmetic), not a tuple constructor.
- *Why B is correct:* `(42)` evaluates to the integer `42`. To create a single-element tuple, you must include a trailing comma: `(42,)`.
- *Why C is incorrect:* List syntax requires square brackets: `[42]`. Parentheses alone do not create a list.
- *Why D is incorrect:* `(42)` is valid Python — it is simply a parenthesized integer expression, not a `SyntaxError`.

---

### Question 2

What happens when you attempt `t[0] = 99` on a tuple `t = (1, 2, 3)`?

- A) The tuple is modified — tuples support item assignment
- B) Python silently ignores the assignment
- C) `TypeError: 'tuple' object does not support item assignment`
- D) `ValueError: invalid assignment to immutable type`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Tuples are immutable. They do not support item assignment, insertion, deletion, or any other modification.
- *Why B is incorrect:* Python does not silently ignore invalid operations — it raises an exception.
- *Why C is correct:* Attempting to assign to a tuple index raises `TypeError: 'tuple' object does not support item assignment`. This error message is specific and frequently tested on the PCAP exam.
- *Why D is incorrect:* The error is `TypeError`, not `ValueError`. `ValueError` typically means a value is inappropriate for a function, not that an immutable object was modified.

---

### Question 3

What does `set([1, 2, 2, 3, 3, 3, 4])` produce?

- A) `[1, 2, 3, 4]`
- B) `{1, 2, 3, 4}`
- C) `{1, 2, 2, 3, 3, 3, 4}`
- D) `ValueError` — duplicate values are not allowed

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `set()` returns a set object, not a list. Although the content is similar, the type is `set`.
- *Why B is correct:* `set()` removes all duplicate values. `{1, 2, 3, 4}` is the result — a set containing the four unique values. No error is raised.
- *Why C is incorrect:* Duplicates are silently dropped when creating a set. The duplicates `2`, `3`, and `3` are not preserved.
- *Why D is incorrect:* `set()` handles duplicates by discarding them, not by raising an error. The constructor is designed to deduplicate.

---

### Question 4

What does `{1, 2, 3} & {2, 3, 4, 5}` return?

- A) `{1, 2, 3, 4, 5}`
- B) `{1}`
- C) `{2, 3}`
- D) `{1, 4, 5}`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `{1, 2, 3, 4, 5}` is the union (`|`), not the intersection. Union includes all elements in either set.
- *Why B is incorrect:* `{1}` is the difference `{1, 2, 3} - {2, 3, 4, 5}` — elements in the first set but not the second.
- *Why C is correct:* `&` is the intersection operator — it returns elements present in both sets. The elements `2` and `3` appear in both `{1, 2, 3}` and `{2, 3, 4, 5}`.
- *Why D is incorrect:* `{1, 4, 5}` is the symmetric difference (`^`) — elements in one set but not both.

---

### Question 5

What type does `{}` create in Python?

- A) An empty `set`
- B) An empty `tuple`
- C) An empty `dict`
- D) `SyntaxError` — empty braces are not valid

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An empty set requires `set()` — the empty-brace literal `{}` is already taken by the empty dict syntax.
- *Why B is incorrect:* An empty tuple is `()`, not `{}`.
- *Why C is correct:* `{}` creates an empty `dict` (dictionary). This is because the dict literal syntax `{key: value, ...}` was established before set literals were added to Python. To create an empty set, you must use `set()`.
- *Why D is incorrect:* `{}` is perfectly valid Python — it simply creates an empty dictionary, not a set.

---

### Question 6

What does `sorted(['banana', 'fig', 'apple'], key=len)` return?

- A) `['apple', 'banana', 'fig']`
- B) `['fig', 'apple', 'banana']`
- C) `['banana', 'fig', 'apple']`
- D) `[6, 3, 5]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* This is alphabetical order — the default `sorted()` behavior without a `key`.
- *Why B is correct:* `key=len` sorts elements by their length. `'fig'` has length 3, `'apple'` has length 5, `'banana'` has length 6. Sorted ascending by length: `['fig', 'apple', 'banana']`.
- *Why C is incorrect:* This is the original unsorted order — no sorting was applied.
- *Why D is incorrect:* `sorted()` returns the original elements sorted by their keys — not the key values themselves. The strings appear in the output, sorted by length.

---

### Question 7

What does the lambda `lambda x: x * 2` return when called with argument `7`?

- A) `7`
- B) `14`
- C) `SyntaxError` — lambda requires a `return` statement
- D) `None`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `x * 2` with `x = 7` evaluates to `14`, not `7`.
- *Why B is correct:* A lambda evaluates and returns its expression. `lambda x: x * 2` called with `7` returns `7 * 2 = 14`.
- *Why C is incorrect:* Lambda functions do NOT use `return`. The expression after the colon is implicitly returned. Writing `return` inside a lambda is a `SyntaxError` — but a lambda without `return` is valid and correct.
- *Why D is incorrect:* A lambda returns the value of its expression, not `None`. `None` would result only if the expression evaluated to `None`.

---

### Question 8

What does the following code print?

```python
x, y, z = (10, 20, 30)
print(y)
```

- A) `(10, 20, 30)`
- B) `10`
- C) `20`
- D) `TypeError` — cannot unpack a tuple

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `print(y)` prints only `y`, not the entire tuple.
- *Why B is incorrect:* `x` is `10`. The question asks for `y`.
- *Why C is correct:* Tuple unpacking assigns the first value to `x`, second to `y`, third to `z`. `y` receives the value at position 1, which is `20`.
- *Why D is incorrect:* Tuple unpacking is a core Python feature. `x, y, z = (10, 20, 30)` is valid Python that assigns each element to the corresponding variable.

---

### Question 9

Which statement about sets is correct?

- A) Sets are ordered — elements are stored in insertion order
- B) Sets can contain duplicate elements
- C) Sets can be indexed with `s[0]`
- D) Sets support the `in` operator for membership testing

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Sets are unordered. Elements have no guaranteed position or insertion-order preservation. (Python 3.7+ dicts preserve insertion order, but sets never do.)
- *Why B is incorrect:* Sets enforce uniqueness — duplicates are silently dropped. A set can never contain two equal elements.
- *Why C is incorrect:* Sets cannot be indexed. `s[0]` raises `TypeError: 'set' object is not subscriptable`. To access elements, iterate over the set or convert it to a sorted list.
- *Why D is correct:* `in` works with sets and is very efficient (average O(1) time). `5 in {1, 3, 5, 7}` returns `True`.

---

### Question 10

What does `a - b` produce if `a = {1, 2, 3, 4}` and `b = {3, 4, 5}`?

- A) `{5}`
- B) `{1, 2}`
- C) `{1, 2, 5}`
- D) `{3, 4}`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `{5}` is what `b - a` (difference in the other direction) would produce — elements in `b` that are not in `a`.
- *Why B is correct:* The set difference `a - b` gives elements that are in `a` but not in `b`. From `a = {1, 2, 3, 4}`, the elements `3` and `4` are also in `b`, so they are excluded. The result is `{1, 2}`.
- *Why C is incorrect:* `{1, 2, 5}` is the symmetric difference (`a ^ b`) — elements in either set but not both.
- *Why D is incorrect:* `{3, 4}` is the intersection (`a & b`) — elements in both sets.
