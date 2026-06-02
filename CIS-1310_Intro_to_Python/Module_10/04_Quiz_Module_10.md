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
