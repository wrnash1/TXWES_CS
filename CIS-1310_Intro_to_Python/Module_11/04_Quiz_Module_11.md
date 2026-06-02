# Quiz: Module 11 — String Methods and Operations

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

**Instructions:** Choose the single best answer for each question. All questions are specific to Module 11 topics.

---

### Question 1

What is the value of `s` after this code executes?

```python
s = 'hello'
s.upper()
print(s)
```

- A) `'HELLO'`
- B) `'hello'`
- C) `None`
- D) `TypeError` — strings cannot be uppercased

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `s.upper()` returns `'HELLO'`, but the return value is not captured — it is discarded. `s` still points to the original string `'hello'`.
- *Why B is correct:* Strings are immutable. `.upper()` does not modify `s` in place — it returns a new string. Since the return value was not assigned (`s = s.upper()`), `s` remains `'hello'`.
- *Why C is incorrect:* `None` is not the value of `s`. `None` would be stored if you wrote `s = s.sort()` on a list (since `.sort()` returns `None`), but string methods return new strings.
- *Why D is incorrect:* `.upper()` is a valid method on all strings. No `TypeError` occurs.

---

### Question 2

What does `'Python programming'.find('java')` return?

- A) `0`
- B) `None`
- C) `ValueError`
- D) `-1`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `0` is returned when the substring is found at index `0` (the very beginning of the string). `'java'` is not in this string at all.
- *Why B is incorrect:* String methods never return `None` as a "not found" signal. `None` would come from calling `d.get(key)` on a missing dictionary key.
- *Why C is incorrect:* `.find()` never raises `ValueError`. That is the key difference between `.find()` and `.index()` — `.find()` returns `-1` for missing substrings so the caller can handle it without a `try/except`.
- *Why D is correct:* `.find()` always returns `-1` when the substring is not present. This is the safe search method — it never raises an exception for missing substrings.

---

### Question 3

What is the output of this code?

```python
text = 'a  b'
print(text.split())
print(text.split(' '))
```

- A) `['a', 'b']` then `['a', 'b']`
- B) `['a', '', 'b']` then `['a', 'b']`
- C) `['a', 'b']` then `['a', '', 'b']`
- D) `['a', 'b']` then `['a', ' ', 'b']`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `.split(' ')` with an explicit space delimiter treats every single space as a boundary. With two consecutive spaces, there is an empty string between them — the output is not `['a', 'b']`.
- *Why B is incorrect:* This reverses the order. `.split()` (no argument) is forgiving — multiple spaces count as one. `.split(' ')` (explicit space) is strict — each space is a separate delimiter.
- *Why C is correct:* `.split()` with no argument collapses multiple whitespace characters into one split and produces `['a', 'b']`. `.split(' ')` with an explicit space splits at every space, so two consecutive spaces produce an empty string between them: `['a', '', 'b']`.
- *Why D is incorrect:* `.split(' ')` does not include the space character as a list element — it uses it as a separator and produces empty strings for consecutive occurrences, not the space itself.

---

### Question 4

Which of the following correctly joins a list of words into a hyphen-separated string?

- A) `words.join('-')`
- B) `join(words, '-')`
- C) `'-'.join(words)`
- D) `str.join(words, '-')`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `join` is a string method, not a list method. Lists have no `.join()` attribute. This raises `AttributeError: 'list' object has no attribute 'join'`.
- *Why B is incorrect:* There is no built-in function called `join()` in Python. `join` is exclusively a string method.
- *Why C is correct:* `.join()` is called on the separator string. `'-'.join(words)` inserts `'-'` between every element of `words` and returns the combined string.
- *Why D is incorrect:* `str.join()` is valid syntax as an unbound method call, but the signature is `str.join(iterable)` — not `str.join(iterable, separator)`. The separator is the string object you call the method on, not a second argument.

---

### Question 5

What is the output of `'banana'.count('an')`?

- A) `1`
- B) `2`
- C) `3`
- D) `4`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `'an'` appears at positions 1 (`an`ana) and 3 (ban`an`a). There are two non-overlapping occurrences.
- *Why B is correct:* `.count()` counts non-overlapping occurrences. `'banana'` contains `'an'` at index 1 (`b[an]ana`) and index 3 (`ban[an]a`). Count: 2.
- *Why C is incorrect:* `3` is the count of the letter `'a'` in `'banana'`, not the substring `'an'`.
- *Why D is incorrect:* There are only 2 non-overlapping `'an'` substrings — not 4. Overlapping matches are not counted.

---

### Question 6

What is the output of this code?

```python
s = '  Python  '
print(repr(s.strip()))
print(repr(s.lstrip()))
```

- A) `'Python'` then `'Python'`
- B) `'Python'` then `'Python  '`
- C) `'  Python'` then `'Python'`
- D) `'Python  '` then `'  Python'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.lstrip()` only removes leading (left-side) whitespace. The trailing spaces on the right are preserved. The output is `'Python  '`, not `'Python'`.
- *Why B is correct:* `.strip()` removes whitespace from both ends → `'Python'`. `.lstrip()` removes only from the left end → the leading spaces are gone but the trailing spaces remain → `'Python  '`.
- *Why C is incorrect:* This reverses the two results. `.strip()` removes both ends (produces `'Python'`), not just the right.
- *Why D is incorrect:* `.strip()` removes both leading and trailing spaces — the result is `'Python'`, not `'Python  '` with trailing spaces.

---

### Question 7

What is the output of `'Hello World'.lower().startswith('hello')`?

- A) `False` — `.startswith()` is case-sensitive
- B) `True`
- C) `None`
- D) `TypeError` — cannot chain methods this way

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.startswith()` is indeed case-sensitive — but in this expression, `.lower()` is called first, converting the string to `'hello world'` before `.startswith('hello')` is tested. The result is `True`.
- *Why B is correct:* Method chaining works left to right. `'Hello World'.lower()` returns `'hello world'`. Then `'hello world'.startswith('hello')` returns `True`.
- *Why C is incorrect:* Boolean testing methods return `True` or `False`, not `None`.
- *Why D is incorrect:* Method chaining is valid Python. `s.lower().startswith('x')` is equivalent to `temp = s.lower(); temp.startswith('x')`.

---

### Question 8

What is the value of `s` after this code?

```python
s = 'aabbaabb'
print(s.replace('aa', 'X', 1))
print(s)
```

- A) `'Xbbaabb'` then `'Xbbaabb'`
- B) `'Xbbaabb'` then `'aabbaabb'`
- C) `'XbbXbb'` then `'aabbaabb'`
- D) `'XbbXbb'` then `'XbbXbb'`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.replace()` returns a new string and never modifies the original. `s` remains `'aabbaabb'` after the call.
- *Why B is correct:* `s.replace('aa', 'X', 1)` replaces only the first occurrence of `'aa'` → `'Xbbaabb'`. The return value is printed. Then `print(s)` prints the original unchanged string `'aabbaabb'`.
- *Why C is incorrect:* The third argument `1` limits replacements to one occurrence. Only the first `'aa'` is replaced. `'XbbXbb'` would result from replacing all occurrences (no count limit).
- *Why D is incorrect:* The original `s` is never reassigned. `.replace()` returns a new string — `s` always holds `'aabbaabb'`.

---

### Question 9

What does `'nohtyP'[::-1]` evaluate to?

- A) `'nohtyP'`
- B) `'Python'`
- C) `''`
- D) `IndexError`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `[::-1]` is the reversal slice — it reads the string backwards. The original string is not returned.
- *Why B is correct:* `'nohtyP'[::-1]` reverses the string character by character. `'nohtyP'` reversed is `'Python'`.
- *Why C is incorrect:* An empty string results only when slicing produces no characters (e.g., `s[5:3]`). Reversing a 6-character string produces a 6-character string.
- *Why D is incorrect:* Slicing never raises `IndexError`. Even completely out-of-range slice bounds return an empty string rather than raising an error.

---

### Question 10

What is the output of this code?

```python
print(ord('B') - ord('A'))
print(chr(ord('a') + 3))
```

- A) `1` then `'c'`
- B) `2` then `'d'`
- C) `1` then `'d'`
- D) `2` then `'c'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `ord('a') + 3` = `97 + 3` = `100`. `chr(100)` is `'d'`, not `'c'`. The second output is wrong.
- *Why B is incorrect:* `ord('B')` = 66, `ord('A')` = 65. `66 - 65 = 1`, not `2`. The first output is wrong.
- *Why C is correct:* `ord('B') - ord('A')` = `66 - 65` = `1`. `ord('a') + 3` = `97 + 3` = `100`. `chr(100)` = `'d'`. Output: `1` then `'d'`.
- *Why D is incorrect:* Both values are wrong. `ord('B') - ord('A')` = 1 (not 2), and `chr(ord('a') + 3)` = `'d'` (not `'c'`).
