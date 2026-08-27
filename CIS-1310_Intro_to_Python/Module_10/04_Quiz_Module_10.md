# Quiz: Module 10 — Dictionaries

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 10 topics.

---

### Question 1

What does `d['key']` do when `'key'` does not exist in dictionary `d`?

- A) Returns `None`
- B) Returns `0`
- C) Raises `KeyError`
- D) Creates a new entry with value `None`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `None` is what `d.get('key')` returns for a missing key — not what bracket notation returns. Bracket notation is strict.
- *Why B is incorrect:* `0` would only be returned if you called `d.get('key', 0)` with an explicit default.
- *Why C is correct:* Bracket notation `d[key]` raises `KeyError` when the key is not found. This is the fundamental difference between `d[key]` and `d.get(key)`.
- *Why D is incorrect:* Python does not auto-create dictionary entries on read. Auto-creation only happens on assignment: `d['key'] = value`.

---

### Question 2

What is the output of this code?

```python
scores = {'Alice': 90, 'Bob': 75}
print(scores.get('Carol', 'Not enrolled'))
print(scores.get('Alice', 'Not enrolled'))
```

- A) `KeyError: 'Carol'` then `90`
- B) `None` then `90`
- C) `Not enrolled` then `Not enrolled`
- D) `Not enrolled` then `90`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `.get()` never raises `KeyError`. That is its entire purpose — safe access without crashing on missing keys.
- *Why B is incorrect:* `None` is what `.get()` returns when there is no default argument. Here a default of `'Not enrolled'` was provided, so missing keys return `'Not enrolled'`, not `None`.
- *Why C is incorrect:* `'Alice'` is present in the dictionary. `.get('Alice', 'Not enrolled')` returns the actual value `90`, not the default.
- *Why D is correct:* `'Carol'` is not in the dictionary, so `.get('Carol', 'Not enrolled')` returns the default `'Not enrolled'`. `'Alice'` is in the dictionary with value `90`, so `.get('Alice', 'Not enrolled')` returns `90`.

---

### Question 3

What does `for item in d:` produce when `d` is a dictionary?

- A) Each `(key, value)` tuple
- B) Each key only
- C) Each value only
- D) Each key-value pair as a list

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `(key, value)` tuples are produced by `for item in d.items():`, not by iterating the dictionary directly.
- *Why B is correct:* Iterating a dictionary directly — `for item in d:` — yields each key. This is equivalent to `for item in d.keys():`.
- *Why C is incorrect:* Values are produced by `for item in d.values():`. Direct iteration skips values entirely.
- *Why D is incorrect:* Dictionary iteration never produces lists. `.items()` produces tuples, not lists.

---

### Question 4

What is the output of this code?

```python
d = {'a': 1, 'b': 2, 'c': 3}
print('b' in d)
print(2 in d)
```

- A) `True` then `True`
- B) `True` then `False`
- C) `False` then `True`
- D) `False` then `False`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `2 in d` tests for `2` among the dictionary's **keys** — not its values. The keys are `'a'`, `'b'`, `'c'` — all strings. `2` is not a key.
- *Why B is correct:* `'b' in d` is `True` because `'b'` is a key. `2 in d` is `False` because `2` is a value, not a key. `in` always tests keys.
- *Why C is incorrect:* `'b'` is definitely a key in this dictionary. `'b' in d` is `True`, not `False`.
- *Why D is incorrect:* `'b'` is a key — `'b' in d` is `True`. Both answers cannot be `False`.

---

### Question 5

Which code correctly counts the frequency of each word in a string?

- A)

```python
words = text.split()
freq = {}
for word in words:
    freq[word] += 1
```

- B)

```python
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
```

- C)

```python
words = text.split()
freq = []
for word in words:
    freq.append(word)
```

- D)

```python
words = text.split()
freq = {}
for word in words:
    freq[word] = 1
```

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `freq[word] += 1` raises `KeyError` the first time any word is encountered because the key does not exist yet. The dictionary has no default value for new keys.
- *Why B is correct:* `freq.get(word, 0)` returns `0` if the word is new, or the current count if it already exists. Adding `1` and assigning back correctly initializes new words and increments existing ones.
- *Why C is incorrect:* This builds a list of all words, not a frequency count. No counting takes place.
- *Why D is incorrect:* `freq[word] = 1` always resets the count to `1`, even if the word has already been seen. Every word will have a count of exactly `1` at the end.

---

### Question 6

What is the output of this code?

```python
data = {'x': 10, 'y': 20, 'z': 30}
result = {k: v * 2 for k, v in data.items() if v > 15}
print(result)
```

- A) `{'x': 20, 'y': 40, 'z': 60}`
- B) `{'y': 40, 'z': 60}`
- C) `{'y': 20, 'z': 30}`
- D) `{20: 'y', 30: 'z'}`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The comprehension includes an `if v > 15` filter. `'x': 10` fails this condition (10 is not > 15) and is excluded.
- *Why B is correct:* Only `'y': 20` (20 > 15) and `'z': 30` (30 > 15) pass the filter. Their values are doubled: `20 * 2 = 40`, `30 * 2 = 60`. Result: `{'y': 40, 'z': 60}`.
- *Why C is incorrect:* This shows the original values, not the doubled values. The expression `v * 2` must be applied.
- *Why D is incorrect:* The comprehension is `{k: v * 2 ...}`, meaning keys come first, then values. `{20: 'y', 30: 'z'}` would require the expression to swap key and value.

---

### Question 7

Which of the following can be used as a dictionary key?

- A) `[1, 2, 3]`
- B) `{'a': 1}`
- C) `(1, 2, 3)`
- D) `{1, 2, 3}`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Lists are mutable and therefore not hashable. `TypeError: unhashable type: 'list'` is raised if you try to use a list as a key.
- *Why B is incorrect:* Dictionaries are mutable and not hashable. `TypeError: unhashable type: 'dict'` is raised.
- *Why C is correct:* Tuples containing only hashable elements are themselves hashable and can be used as dictionary keys. `(1, 2, 3)` is an immutable tuple of integers — valid key.
- *Why D is incorrect:* Sets are mutable and not hashable. `TypeError: unhashable type: 'set'` is raised.

---

### Question 8

What does `.pop('key')` do when `'key'` exists in the dictionary?

- A) Returns `None` and removes the key
- B) Returns the value and removes the key
- C) Returns the value but leaves the key in the dictionary
- D) Returns the key and removes the key-value pair

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.pop()` returns the actual value associated with the key, not `None`. `None` is the return value only if the key is missing and a default of `None` was provided.
- *Why B is correct:* `.pop(key)` removes the key from the dictionary and returns the value that was associated with it. This is the dictionary equivalent of `list.pop(index)`.
- *Why C is incorrect:* `.pop()` modifies the dictionary by removing the key. To read a value without removing it, use `d[key]` or `d.get(key)`.
- *Why D is incorrect:* `.pop()` returns the **value**, not the key. The caller already knows the key — they passed it as the argument.

---

### Question 9

What is the output of this code?

```python
d = {'a': 1, 'b': 2}
d.update({'b': 99, 'c': 3})
print(d)
```

- A) `{'a': 1, 'b': 2, 'c': 3}`
- B) `{'a': 1, 'b': 99, 'c': 3}`
- C) `{'b': 99, 'c': 3}`
- D) `TypeError` — cannot update a dictionary with another dictionary

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'b'` exists in both dictionaries. `.update()` overwrites existing keys with the values from the argument. `'b'` becomes `99`, not stays as `2`.
- *Why B is correct:* `.update()` merges the argument into the dictionary. New keys (`'c'`) are added. Existing keys (`'b'`) are overwritten with the new value. Keys not in the argument (`'a'`) are unchanged.
- *Why C is incorrect:* `.update()` merges — it does not replace the entire dictionary. Keys from the original dictionary that are not in the argument (`'a'`) are preserved.
- *Why D is incorrect:* `.update()` accepts any dictionary (or any iterable of key-value pairs) as its argument. Passing another dict is the most common usage.

---

### Question 10

What is the output of this code?

```python
roster = {
    'Alice': {'grade': 92, 'year': 3},
    'Bob':   {'grade': 85, 'year': 2},
}

roster['Carol'] = {'grade': 78, 'year': 1}
print(roster['Alice']['grade'])
print(len(roster))
```

- A) `92` then `2`
- B) `{'grade': 92, 'year': 3}` then `3`
- C) `92` then `3`
- D) `3` then `92`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* After adding `'Carol'`, the roster has 3 entries, not 2. `len(roster)` is `3`.
- *Why B is incorrect:* `roster['Alice']['grade']` uses double bracket access — first `roster['Alice']` returns the nested dict `{'grade': 92, 'year': 3}`, then `['grade']` retrieves `92`. The full nested dict is not printed.
- *Why C is correct:* `roster['Alice']['grade']` correctly drills into the nested dictionary to get `92`. After adding `'Carol'`, there are 3 entries in `roster`, so `len(roster)` is `3`.
- *Why D is incorrect:* This reverses the two print statements. `roster['Alice']['grade']` prints first (`92`), then `len(roster)` prints second (`3`).

---

### Question 11

What is the output of this code?

```python
d = {'a': 1, 'b': 2, 'c': 3}
d.pop('b')
print(list(d.keys()))
```

- A) `['a', 'b', 'c']`
- B) `['a', 'c']`
- C) `['b']`
- D) `KeyError: 'b'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.pop('b')` removes the key `'b'` from the dictionary. The resulting dictionary has only `'a'` and `'c'` as keys.
- *Why B is correct:* `.pop('b')` removes `'b'` and returns its value (`2`). After the pop, `d` is `{'a': 1, 'c': 3}`. `list(d.keys())` produces `['a', 'c']`.
- *Why C is incorrect:* `.pop()` does not return a list of removed keys. It returns the value associated with the removed key. The resulting `d.keys()` reflects what remains, not what was removed.
- *Why D is incorrect:* `.pop('b')` raises `KeyError` only if `'b'` is **not** in the dictionary. `'b'` is present here, so no error is raised.

---

### Question 12

What is the output of this code?

```python
d = {'x': 5, 'y': 10}
d['x'] += 3
d['z'] = d.get('z', 0) + 1
print(d['x'], d.get('y'), d['z'])
```

- A) `5 10 1`
- B) `8 10 1`
- C) `8 None 1`
- D) `8 10 0`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `d['x'] += 3` modifies `d['x']` from `5` to `8`. The original value `5` is not preserved.
- *Why B is correct:* `d['x'] += 3` → `8`. `d.get('z', 0) + 1` → `0 + 1 = 1`, stored as `d['z'] = 1`. `d.get('y')` → `10` (key exists). Output: `8 10 1`.
- *Why C is incorrect:* `d.get('y')` does not return `None` — `'y'` exists in the dictionary with value `10`. `None` is only returned for missing keys when no default is provided.
- *Why D is incorrect:* `d['z']` is `1`, not `0`. The expression `d.get('z', 0) + 1` evaluates to `1` before assignment, so `d['z']` is stored as `1`.

---

### Question 13

Which code safely removes the key `'score'` from dictionary `d` and stores the value in `result`, without raising an error if `'score'` is not present?

- A) `result = del d['score']`
- B) `result = d.pop('score')`
- C) `result = d.pop('score', None)`
- D) `result = d.remove('score')`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `del` is a statement, not an expression — it cannot return a value. Writing `result = del d['score']` is a `SyntaxError`. Additionally, `del d['score']` raises `KeyError` if `'score'` is missing.
- *Why B is incorrect:* `d.pop('score')` with one argument does remove the key and return the value, but raises `KeyError` if `'score'` is not in the dictionary. It is not safe for missing keys.
- *Why C is correct:* `d.pop('score', None)` removes `'score'` and returns its value if present; returns `None` without raising an error if `'score'` is missing. This is the safe, idiomatic pattern.
- *Why D is incorrect:* Dictionaries have no `.remove()` method. `list.remove()` removes by value, but there is no equivalent for dict. Using `.remove()` raises `AttributeError`.

---

### Question 14

What is the output of this code?

```python
inventory = {'apples': 5, 'bananas': 3}
inventory.update({'bananas': 10, 'cherries': 7})
print(sorted(inventory.items()))
```

- A) `[('apples', 5), ('bananas', 3), ('cherries', 7)]`
- B) `[('apples', 5), ('bananas', 10), ('cherries', 7)]`
- C) `[('bananas', 10), ('cherries', 7)]`
- D) `[('apples', 5), ('bananas', 3, 10), ('cherries', 7)]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.update()` overwrites existing keys with the new values. `'bananas'` is in both dicts; the new value `10` replaces the old value `3`.
- *Why B is correct:* `.update()` overwrites `'bananas'` from `3` to `10` and adds `'cherries': 7`. `sorted()` on `.items()` sorts tuples lexicographically by key. Result: `[('apples', 5), ('bananas', 10), ('cherries', 7)]`.
- *Why C is incorrect:* `.update()` is a merge, not a replacement. Keys from the original dictionary that are not in the argument (`'apples'`) are preserved.
- *Why D is incorrect:* Dictionary values are not accumulated into tuples. Each key maps to exactly one value — the new value overwrites the old.

---

### Question 15

What does `d.setdefault('count', 0)` do if `'count'` is already in `d` with value `5`?

- A) Resets `d['count']` to `0`
- B) Returns `0` without changing `d`
- C) Returns `5` without changing `d`
- D) Raises `KeyError`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `setdefault` never overwrites an existing value. It only inserts if the key is absent. The existing `5` is preserved.
- *Why B is incorrect:* `setdefault` returns the **existing** value when the key is present, not the default. `0` is only returned (and inserted) when the key is missing.
- *Why C is correct:* When `'count'` already exists in `d`, `setdefault('count', 0)` simply returns the current value `5` and leaves the dictionary unchanged. It is a no-op for existing keys.
- *Why D is incorrect:* `setdefault` never raises `KeyError`. It is specifically designed as a safe operation — insert-if-absent, never error.

---

### Question 16

What is the output of this code?

```python
pairs = [('a', 1), ('b', 2), ('c', 3)]
d = dict(pairs)
print({v: k for k, v in d.items()})
```

- A) `{'a': 1, 'b': 2, 'c': 3}`
- B) `{1: 'a', 2: 'b', 3: 'c'}`
- C) `[('a', 1), ('b', 2), ('c', 3)]`
- D) `{('a', 1): 0, ('b', 2): 1, ('c', 3): 2}`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The comprehension is `{v: k for k, v in d.items()}` — note that `v` is the key and `k` is the value in the output. This inverts the dictionary.
- *Why B is correct:* `dict(pairs)` builds `{'a': 1, 'b': 2, 'c': 3}`. The comprehension iterates `.items()` unpacking as `k, v`, then produces `{v: k}` — swapping keys and values. Result: `{1: 'a', 2: 'b', 3: 'c'}`.
- *Why C is incorrect:* The comprehension produces a `dict`, not a list of tuples. The curly braces with a colon expression always produce a dict.
- *Why D is incorrect:* This would require using `enumerate()` and the pair as a key. The comprehension shown iterates `.items()` and swaps keys and values.

---

### Question 17

What is the output of this code?

```python
text = 'go go go stop go stop'
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq['go'], freq['stop'])
```

- A) `3 2`
- B) `4 2`
- C) `1 1`
- D) `go stop`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Count `'go'` in the string: `go go go stop go stop` → positions 1, 2, 3, 5. That is 4 occurrences, not 3.
- *Why B is correct:* `'go'` appears 4 times and `'stop'` appears 2 times. The accumulator pattern correctly counts each occurrence. `freq['go'] = 4`, `freq['stop'] = 2`.
- *Why C is incorrect:* `freq[word] = 1` would always reset to `1`. The pattern shown uses `freq.get(word, 0) + 1`, which increments correctly.
- *Why D is incorrect:* `freq['go']` and `freq['stop']` are integer counts, not the word strings themselves.

---

### Question 18

Which of the following correctly creates a dictionary mapping each number from 1 to 5 to its cube?

- A) `{n: n**3 for n in range(1, 6)}`
- B) `[n: n**3 for n in range(1, 6)]`
- C) `{n**3 for n in range(1, 6)}`
- D) `dict(n**3 for n in range(1, 6))`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `{key: value for item in iterable}` is the dictionary comprehension syntax. `{n: n**3 for n in range(1, 6)}` maps each `n` to `n**3`, producing `{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}`.
- *Why B is incorrect:* Square brackets `[...]` create a list comprehension. `n: n**3` is not valid syntax inside a list comprehension — it would raise `SyntaxError`.
- *Why C is incorrect:* `{expr for item in iterable}` with a single expression (no colon) is a **set** comprehension. This produces `{1, 8, 27, 64, 125}` — a set of cube values, not a dict mapping.
- *Why D is incorrect:* `dict()` accepts an iterable of key-value pairs. `n**3 for n in range(1, 6)` generates single integers, not pairs. `dict()` would raise `TypeError`.

---

### Question 19

What is the output of this code?

```python
d = {'one': 1, 'two': 2, 'three': 3}
total = sum(d.values())
largest_key = max(d, key=d.get)
print(total, largest_key)
```

- A) `6 three`
- B) `6 'three'`
- C) `3 three`
- D) `6 3`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `sum(d.values())` sums `1 + 2 + 3 = 6`. `max(d, key=d.get)` iterates over keys and uses each key's value as the sort key — `d.get('three') = 3` is the maximum. Result: `6 three`.
- *Why B is incorrect:* `print()` outputs the string `three` without quotes. Python's `print()` function does not add surrounding quotes to string values.
- *Why C is incorrect:* `sum(d.values())` is `6`, not `3`. `3` is just the maximum value, not the sum.
- *Why D is incorrect:* `max(d, key=d.get)` returns the **key** with the highest value — the string `'three'` — not the value `3` itself. To get the maximum value, you would use `max(d.values())`.

---

### Question 20

What is the output of this code?

```python
a = {'x': 1, 'y': 2}
b = a.copy()
b['x'] = 99
print(a['x'], b['x'])
```

- A) `99 99`
- B) `1 99`
- C) `99 1`
- D) `1 1`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `b = a.copy()` creates a separate dictionary. Modifying `b['x']` does not affect `a`. If `b` had been assigned as `b = a` (reference, not copy), both would show `99`.
- *Why B is correct:* `.copy()` creates a shallow copy — a new dictionary object with the same key-value pairs. `b['x'] = 99` modifies `b` only. `a['x']` remains `1`.
- *Why C is incorrect:* `a['x']` is `1` (unchanged) and `b['x']` is `99` (modified). This answer reverses the two values.
- *Why D is incorrect:* `b['x'] = 99` is an explicit assignment. `b['x']` is definitely `99` after this line — it cannot remain `1`.
