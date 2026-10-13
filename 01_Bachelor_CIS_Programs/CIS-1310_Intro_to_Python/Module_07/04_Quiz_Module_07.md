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

---

### Question 11

What is the output of this code?

```python
t = (1, 2, 3, 2, 1)
print(t.count(2), t.index(3))
```

- A) `2 3`
- B) `2 2`
- C) `1 2`
- D) `TypeError: tuples have no count or index methods`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `t.count(2)` is `2` (correct), but `t.index(3)` returns the index of the first occurrence of `3`, which is `2` (index 2), not `3`.
- *Why B is correct:* `t.count(2)` counts occurrences of `2` in the tuple: positions 1 and 3 → count is `2`. `t.index(3)` returns the index of the first `3`, which is at index `2`. Output: `2 2`.
- *Why C is incorrect:* `t.count(2) = 2`, not `1`. The value `2` appears at indices 1 and 3.
- *Why D is incorrect:* Tuples do support `count()` and `index()` — they are read-only sequence methods that do not modify the tuple.

---

### Question 12

What is the result of `{1, 2, 3} | {3, 4, 5}`?

- A) `{3}`
- B) `{1, 2, 4, 5}`
- C) `{1, 2, 3, 4, 5}`
- D) `{1, 2, 3, 3, 4, 5}`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `{3}` is the intersection (`&`) — the only element in both sets.
- *Why B is incorrect:* `{1, 2, 4, 5}` is the symmetric difference (`^`) — elements in one set but not both.
- *Why C is correct:* `|` is the union operator — it returns all elements present in either set. Duplicates are automatically eliminated: `3` appears in both but only once in the result.
- *Why D is incorrect:* Sets never contain duplicate values. Even though `3` is in both sets, it appears only once in the union result.

---

### Question 13

What does `sorted([(2, 'b'), (1, 'c'), (1, 'a')])` produce?

- A) `[(1, 'a'), (1, 'c'), (2, 'b')]`
- B) `[(1, 'c'), (1, 'a'), (2, 'b')]`
- C) `[(2, 'b'), (1, 'c'), (1, 'a')]`
- D) `TypeError: tuples cannot be compared`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Python sorts tuples lexicographically — first by the first element, then by the second as a tiebreaker. Both `(1, 'a')` and `(1, 'c')` have first element `1`. Since `'a' < 'c'`, `(1, 'a')` comes first. Then `(2, 'b')` follows.
- *Why B is incorrect:* Python's sort is stable — but when comparing tuples with equal first elements, it compares second elements. `'a' < 'c'`, so `(1, 'a')` sorts before `(1, 'c')`.
- *Why C is incorrect:* That is the original unsorted order.
- *Why D is incorrect:* Tuples are fully comparable in Python. Comparison proceeds element by element, left to right.

---

### Question 14

Which of the following is a valid way to create an empty set?

- A) `s = {}`
- B) `s = set()`
- C) `s = set{}`
- D) `s = ()`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `{}` creates an empty **dict**, not a set. This is a critical distinction tested directly on the PCAP exam.
- *Why B is correct:* `set()` with no arguments creates an empty set. This is the only way to create an empty set in Python.
- *Why C is incorrect:* `set{}` is not valid Python syntax. `set()` is a function call, not a literal syntax like `{}`.
- *Why D is incorrect:* `()` creates an empty **tuple**, not a set.

---

### Question 15

What does `lambda x, y: x if x > y else y` return when called as `f(3, 7)`?

- A) `3`
- B) `7`
- C) `True`
- D) `SyntaxError` — lambda cannot contain if/else expressions

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The lambda returns the larger value. Since `3 > 7` is `False`, the expression returns `y = 7`, not `x = 3`.
- *Why B is correct:* The lambda uses a ternary expression: return `x` if `x > y`, else return `y`. With `x=3, y=7`: `3 > 7` is `False`, so `y = 7` is returned.
- *Why C is incorrect:* The lambda returns the value of `x` or `y`, not a boolean comparison result.
- *Why D is incorrect:* Lambda expressions fully support ternary (`if`/`else`) expressions within their body. The ternary is a single expression, which is all a lambda may contain.

---

### Question 16

What is the output of this code?

```python
coords = (3, 7)
x, y = coords
print(f'x={x}, y={y}')
```

- A) `x=(3, 7), y=(3, 7)`
- B) `x=3, y=7`
- C) `TypeError: cannot unpack non-sequence tuple`
- D) `x=7, y=3`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Tuple unpacking assigns individual elements, not the entire tuple to each variable.
- *Why B is correct:* `x, y = coords` unpacks the two-element tuple, assigning `3` to `x` and `7` to `y`. The f-string produces `x=3, y=7`.
- *Why C is incorrect:* Tuples are sequences and fully support unpacking. The error message is fabricated — no such `TypeError` occurs.
- *Why D is incorrect:* Unpacking assigns in order: first element to the first variable. `x` gets `3`, `y` gets `7` — not reversed.

---

### Question 17

What does `discard()` do that `remove()` does not?

- A) `discard()` removes an element and returns it; `remove()` returns `None`
- B) `discard()` removes all occurrences; `remove()` removes only the first
- C) `discard()` does not raise an error if the element is not found; `remove()` raises `KeyError`
- D) `discard()` works on lists; `remove()` works only on sets

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Neither `discard()` nor `remove()` returns the element. Both return `None`. `pop()` is the method that removes and returns an element.
- *Why B is incorrect:* Sets cannot contain duplicates, so "all occurrences" vs "first occurrence" is irrelevant. Both methods remove a single element (since duplicates don't exist in sets).
- *Why C is correct:* `s.remove(x)` raises `KeyError` if `x` is not in the set. `s.discard(x)` does the same thing if `x` is present, but silently does nothing if `x` is absent. Use `discard()` when you want to remove-if-present without the need for a guard check.
- *Why D is incorrect:* Both `discard()` and `remove()` are set methods, not list methods. Lists have their own `remove()` method that raises `ValueError` (not `KeyError`) for missing values.

---

### Question 18

What is the output of this code?

```python
students = [('Alice', 90), ('Bob', 85), ('Carol', 90), ('Dave', 85)]
result = sorted(students, key=lambda s: (-s[1], s[0]))
print(result[0])
```

- A) `('Alice', 90)`
- B) `('Carol', 90)`
- C) `('Bob', 85)`
- D) `('Dave', 85)`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The key `(-s[1], s[0])` sorts by score descending (negated) then name ascending. Score 90 students come first (negative: -90 < -85). Among `'Alice'` and `'Carol'` (both 90), `'Alice' < 'Carol'` alphabetically, so Alice is first.
- *Why B is incorrect:* Carol also has score 90 but `'Alice' < 'Carol'` alphabetically, so Alice sorts before Carol.
- *Why C is incorrect:* Bob has score 85, which sorts after both 90-point students.
- *Why D is incorrect:* Dave has score 85 and comes last among the 85-point students alphabetically.

---

### Question 19

A tuple `t = (1, [2, 3], 4)` contains a list. What happens when you run `t[1].append(5)`?

- A) `TypeError: tuple object does not support item assignment`
- B) The tuple becomes `(1, [2, 3, 5], 4)` — the list inside is mutable
- C) The tuple becomes `(1, [2, 3], 4, 5)` — the value is appended to the tuple
- D) `AttributeError: tuples have no append method`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `t[1].append(5)` does not assign to `t[1]` — it calls a method on the object that `t[1]` references. Tuple immutability means the reference inside the tuple cannot be changed, but the object being referenced (the list) can still be mutated.
- *Why B is correct:* The tuple's immutability means `t[1]` will always refer to the same list object. But the list itself is mutable — `append()` modifies the list object in place. The tuple's reference is unchanged; the referenced list now has an extra element.
- *Why C is incorrect:* `append()` is a list method, not a tuple method. And tuples themselves cannot be extended.
- *Why D is incorrect:* `t[1]` is a list, not a tuple. Lists have `append()`. The `AttributeError` would only occur if you tried `t.append(5)` on the tuple itself.

---

### Question 20

What does `{x**2 for x in range(5)}` produce?

- A) `[0, 1, 4, 9, 16]` — a list comprehension
- B) `{0, 1, 4, 9, 16}` — a set comprehension
- C) `(0, 1, 4, 9, 16)` — a generator expression
- D) `SyntaxError` — comprehensions cannot use the `**` operator inside curly braces

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Square brackets `[...]` create a list comprehension. Curly braces `{...}` with an expression (not a key-value pair) create a set comprehension.
- *Why B is correct:* `{expression for var in iterable}` is a set comprehension — it produces a set. `{x**2 for x in range(5)}` = `{0, 1, 4, 9, 16}`. Note: since sets are unordered, the display order may vary, but the content is the five unique squared values.
- *Why C is incorrect:* A generator expression uses parentheses: `(x**2 for x in range(5))`. This creates a lazy iterator, not a set.
- *Why D is incorrect:* `**` is a valid Python operator and works inside any comprehension. No SyntaxError occurs.
