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

---

### Question 11

What is the output of this code?

```python
s = 'Mississippi'
print(s.count('ss'))
print(s.find('ss'))
print(s.rfind('ss'))
```

- A) `2` then `2` then `5`
- B) `2` then `3` then `6`
- C) `3` then `2` then `5`
- D) `2` then `2` then `2`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `'ss'` appears at index 2 (`Mi[ss]issippi`) and index 5 (`Missi[ss]ippi`) — count is 2. `.find('ss')` returns the first occurrence index: 2. `.rfind('ss')` returns the last occurrence index: 5.
- *Why B is incorrect:* `.find('ss')` returns `2`, not `3`. Index 3 is the character `'i'`, not the start of `'ss'`.
- *Why C is incorrect:* The count of non-overlapping `'ss'` is `2`, not `3`. There are only two `'ss'` substrings in `'Mississippi'`.
- *Why D is incorrect:* `.rfind()` searches from the right and returns the index of the last occurrence. The last `'ss'` starts at index 5, not index 2.

---

### Question 12

What is the output of this code?

```python
words = ['one', 'two', 'three']
print(', '.join(words))
print(' '.join(reversed(words)))
```

- A) `'one, two, three'` then `'three two one'`
- B) `one, two, three` then `three two one`
- C) `one two three` then `three, two, one`
- D) `['one', 'two', 'three']` then `['three', 'two', 'one']`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `print()` does not add surrounding quotes to strings. The output is the string content without quotes.
- *Why B is correct:* `', '.join(words)` → `'one, two, three'`. `reversed(words)` reverses the list; `' '.join(reversed(words))` → `'three two one'`. `print()` outputs both without quotes.
- *Why C is incorrect:* This swaps the separators. The first join uses `', '` (comma-space), the second uses `' '` (space only).
- *Why D is incorrect:* `.join()` returns a single string, not a list representation. Lists are only displayed with brackets when using `repr()` or printing the list object directly.

---

### Question 13

What does `'  hello world  '.strip().split()` return?

- A) `['hello', 'world']`
- B) `['  hello', 'world  ']`
- C) `['hello world']`
- D) `['', 'hello', 'world', '']`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `.strip()` removes the leading and trailing whitespace → `'hello world'`. Then `.split()` (no argument) splits on any whitespace and ignores multiple spaces → `['hello', 'world']`.
- *Why B is incorrect:* `.strip()` is applied before `.split()`, removing the surrounding spaces. The split receives a clean string with no leading/trailing whitespace.
- *Why C is incorrect:* `.split()` with no argument splits on all whitespace. The result is a list of words, not a single-element list containing the whole phrase.
- *Why D is incorrect:* Empty strings at the ends are produced by `.split(' ')` with an explicit space delimiter. `.strip()` followed by `.split()` produces no empty strings.

---

### Question 14

What is the output of this code?

```python
s = 'Hello, World!'
print(s.lower().replace('world', 'python').title())
```

- A) `Hello, Python!`
- B) `hello, python!`
- C) `Hello, World!`
- D) `HELLO, PYTHON!`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Method chains execute left to right. `s.lower()` → `'hello, world!'`. `.replace('world', 'python')` → `'hello, python!'`. `.title()` capitalizes the first letter of each "word" (sequence of letters/digits) → `'Hello, Python!'`.
- *Why B is incorrect:* `.title()` is applied last, capitalizing the first letter of each word. The final result is title case, not all lowercase.
- *Why C is incorrect:* `.lower()` converts to lowercase first, then `.replace('world', 'python')` substitutes successfully (case-insensitive match only works because `.lower()` was called first).
- *Why D is incorrect:* No `.upper()` is called in the chain. `.title()` capitalizes only the first letter of each word, not the entire string.

---

### Question 15

What does `'Python'.zfill(10)` return?

- A) `'Python    '`
- B) `'    Python'`
- C) `'0000Python'`
- D) `'Python0000'`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `.zfill()` pads with zeros, not spaces. Space-padding on the right is done with `.ljust()`.
- *Why B is incorrect:* `.zfill()` pads with zeros, not spaces. Space-padding on the left is done with `.rjust()`.
- *Why C is correct:* `.zfill(width)` pads the string on the left with `'0'` characters until the total width is reached. `'Python'` has 6 characters; `10 - 6 = 4` zeros are prepended → `'0000Python'`.
- *Why D is incorrect:* `.zfill()` adds zeros to the left (leading zeros), not the right. Right-padding with zeros would require `.ljust(10, '0')`.

---

### Question 16

What is the output of this code?

```python
text = 'first:second:third:fourth'
parts = text.split(':', 2)
print(len(parts), parts[-1])
```

- A) `4 fourth`
- B) `3 third:fourth`
- C) `2 third`
- D) `3 fourth`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.split(':', 2)` performs at most 2 splits, producing at most 3 parts — not 4. A split with no limit would produce 4 parts.
- *Why B is correct:* `.split(':', 2)` splits at the first two `':'` characters only. Result: `['first', 'second', 'third:fourth']`. `len(parts) = 3`. `parts[-1] = 'third:fourth'`.
- *Why C is incorrect:* `len(parts) = 3`, not 2. Two splits produce three parts. And `parts[-1]` is `'third:fourth'` — the unsplit remainder.
- *Why D is incorrect:* `parts[-1]` is `'third:fourth'` (the entire unsplit remainder after 2 splits), not just `'fourth'`.

---

### Question 17

What is the output of this code?

```python
s = 'abcABC123'
print(s.isalpha())
print(s.isalnum())
print('abc123'.isalpha())
```

- A) `True` then `True` then `True`
- B) `True` then `True` then `False`
- C) `False` then `True` then `False`
- D) `False` then `False` then `False`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `s.isalpha()` returns `False` because `s` contains digits (`'1'`, `'2'`, `'3'`), which are not alphabetic characters.
- *Why B is incorrect:* `s.isalpha()` is `False` (digits are present). The first value cannot be `True`.
- *Why C is correct:* `'abcABC123'.isalpha()` → `False` (digits present). `'abcABC123'.isalnum()` → `True` (all letters or digits, no other characters). `'abc123'.isalpha()` → `False` (digits are not alphabetic).
- *Why D is incorrect:* `'abcABC123'.isalnum()` returns `True` — every character is either a letter or a digit, which satisfies `.isalnum()`.

---

### Question 18

What is the output of `'hello world'.startswith(('hi', 'hell', 'hey'))`?

- A) `False` — `.startswith()` only accepts a single string
- B) `True`
- C) `TypeError: expected str, not tuple`
- D) `['hi', 'hell', 'hey']`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.startswith()` accepts either a string or a **tuple of strings**. It returns `True` if the string starts with any of the given prefixes.
- *Why B is correct:* `.startswith(('hi', 'hell', 'hey'))` checks all three prefixes. `'hello world'` starts with `'hell'`, so the result is `True`.
- *Why C is incorrect:* Passing a tuple to `.startswith()` is explicitly supported. `TypeError` would only occur if you passed a list (`list` is not accepted — only `tuple` or `str`).
- *Why D is incorrect:* `.startswith()` always returns a `bool` (`True` or `False`), never a list.

---

### Question 19

What is the output of this code?

```python
name = '  Alice  '
formatted = f'Hello, {name.strip().upper()}!'
print(formatted)
print(len(name.strip()))
```

- A) `Hello,   ALICE  !` then `9`
- B) `Hello, ALICE!` then `5`
- C) `Hello, ALICE!` then `9`
- D) `Hello, alice!` then `5`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `.strip()` removes the surrounding spaces before `.upper()` is applied. The f-string uses the stripped-and-uppercased result, not the original padded value.
- *Why B is correct:* `name.strip()` → `'Alice'`. `.upper()` → `'ALICE'`. f-string → `'Hello, ALICE!'`. `name.strip()` is `'Alice'` (5 characters). `len('Alice') = 5`.
- *Why C is incorrect:* `len(name.strip())` measures the stripped string (`'Alice'`), which has 5 characters — not 9 (which is the length of the original `'  Alice  '`).
- *Why D is incorrect:* `.upper()` is called after `.strip()`. The result is uppercase `'ALICE'`, not lowercase.

---

### Question 20

What is the output of this code?

```python
s = 'racecar'
print(s == s[::-1])
print(s[0] == s[-1])
```

- A) `True` then `False`
- B) `False` then `True`
- C) `True` then `True`
- D) `False` then `False`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `s[0]` is `'r'` and `s[-1]` is `'r'` — they are equal. The second expression is `True`, not `False`.
- *Why B is incorrect:* `'racecar'[::-1]` is `'racecar'` (a palindrome). `s == s[::-1]` is `True`, not `False`.
- *Why C is correct:* `'racecar'` is a palindrome — it reads the same forwards and backwards. `s[::-1]` = `'racecar'` = `s`, so `s == s[::-1]` is `True`. `s[0]` = `'r'` and `s[-1]` = `'r'`, so `s[0] == s[-1]` is also `True`.
- *Why D is incorrect:* Both expressions evaluate to `True`. `'racecar'` is a classic palindrome example used in many Python courses and exams.
