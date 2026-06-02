# Quiz: Module 15 — String Algorithms & Trie

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the time complexity of `insert`, `search`, and `starts_with` in a Trie, and what variable does it depend on?

- A) O(n) where n is the number of stored words
- B) O(L) where L is the length of the word or prefix being processed
- C) O(n log n) where n is the total number of characters stored
- D) O(1) — Tries support constant-time operations like hash tables

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n) depending on number of words would mean operations slow down as the Trie grows. A Trie's insert and search only traverse the path for the specific word — exactly L nodes — regardless of how many other words are stored.
- *Why B is correct:* Each operation processes one character at a time down a single path from the root. For a word of length L, exactly L nodes are visited. The number of other stored words has no effect on the path length.
- *Why C is incorrect:* O(n log n) is associated with sorting algorithms. The Trie's path traversal is strictly proportional to the word length, not the total stored characters.
- *Why D is incorrect:* Tries do not support O(1) operations. The O(L) cost is unavoidable — you must process each character to traverse or build the path. Hash tables achieve approximate O(L) by hashing the full string, not O(1).

---

### Question 2

A Trie stores the words: 'car', 'card', 'care', 'cat'. What does `search('car')` return, and what does `starts_with('car')` return?

- A) `search('car') = True`, `starts_with('car') = True`
- B) `search('car') = False`, `starts_with('car') = True`
- C) `search('car') = True`, `starts_with('car') = False`
- D) Both return `False` — 'car' is a prefix of other words, not a complete word

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* 'car' is in the word list — it was inserted, so `is_end = True` at the node after 'r'. Therefore `search('car')` returns True. The path 'c'→'a'→'r' also exists, so `starts_with('car')` returns True. Both are True because 'car' is both a complete stored word and a prefix of 'card' and 'care'.
- *Why B is incorrect:* `search('car')` returns False only if 'car' was not explicitly inserted. Since 'car' is in the word list, it was inserted and `is_end` is set at 'r'.
- *Why C is incorrect:* If `search` returns True, the path must exist — so `starts_with` must also return True. These two cannot have opposite answers for an exact match.
- *Why D is incorrect:* Both functions can return True independently. A word being a prefix of longer words does not prevent it from being a complete stored word itself.

---

### Question 3

In `length_of_longest_substring`, why is the condition `char_index[char] >= left` necessary when deciding to move `left`?

```python
if char in char_index and char_index[char] >= left:
    left = char_index[char] + 1
```

- A) To prevent `left` from exceeding `right`, which would cause an empty window
- B) To ensure we only move `left` when the duplicate is inside the current window — a duplicate seen before the window started is irrelevant
- C) To handle the case where `char_index` has not been initialized for the character
- D) To skip non-alphabetic characters in the string

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The condition does not prevent `left > right`. It prevents `left` from moving backward to a position before the current window. The guard checks whether the duplicate is within bounds of the current window.
- *Why B is correct:* Suppose the string is 'abba' and we are at right=3 (second 'a'). `char_index['a'] = 0`. If `left = 2` (we already moved past the first 'a'), then `char_index['a'] = 0 < left = 2` — the duplicate is before the current window and irrelevant. Without the guard, we would incorrectly move `left` to 1 (backward from 2), breaking the window.
- *Why C is incorrect:* The `char in char_index` check handles uninitialized characters — if the character is not in the dict, the condition short-circuits. The `>= left` guard is about position, not initialization.
- *Why D is incorrect:* `length_of_longest_substring` handles all characters. There is no alphabetic filtering in the algorithm.

---

### Question 4

In the Minimum Window Substring algorithm, what do `required` and `formed` track, and when does the inner `while` loop execute?

- A) `required` counts total characters in t; `formed` counts characters seen so far; inner loop runs when `formed > required`
- B) `required` counts distinct character types needed from t; `formed` counts how many are currently satisfied in the window; inner loop runs when the window is valid (`formed == required`)
- C) `required` and `formed` both count window size; inner loop runs when the window is too large
- D) `required` is fixed at 1; `formed` increments by character frequency; inner loop runs to count anagrams

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `required` is not the total character count in t — it is the number of distinct character types. `formed` tracks satisfied types (those whose count in the window meets the requirement), not raw character count.
- *Why B is correct:* `required = len(Counter(t))` — the number of distinct characters needed. `formed` increments when a character's count in the window first reaches the required count. When `formed == required`, every required character is sufficiently covered — the window is valid and can be shrunk.
- *Why C is incorrect:* Neither variable tracks window size. Window size is `right - left + 1`, computed only to compare with `min_len` when recording the best window.
- *Why D is incorrect:* `required` is never 1 unless t has only one distinct character. The algorithm is for Minimum Window Substring, not anagram finding.

---

### Question 5

In `longest_palindrome`, why must `expand` be called twice per center — once as `expand(i, i)` and once as `expand(i, i+1)`?

- A) `expand(i, i)` finds even-length palindromes; `expand(i, i+1)` finds odd-length palindromes
- B) `expand(i, i)` finds odd-length palindromes centered at character i; `expand(i, i+1)` finds even-length palindromes centered between i and i+1
- C) Both calls find the same palindromes — one is a performance optimization
- D) `expand(i, i+1)` is only needed when `s[i] == s[i+1]`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The descriptions are swapped. A single character as center gives odd-length palindromes; a gap between two characters gives even-length palindromes. `expand(i, i)` is odd; `expand(i, i+1)` is even.
- *Why B is correct:* `expand(i, i)` starts with both pointers at the same character — a valid one-character palindrome — and expands outward to find all odd-length palindromes centered at `i`. `expand(i, i+1)` starts with adjacent characters and expands if they match, finding all even-length palindromes. For 'cbbd', only `expand(1, 2)` finds 'bb'. Missing the even case would return 'c' (length 1) instead.
- *Why C is incorrect:* They find entirely different palindromes. Calling only `expand(i, i)` misses all even-length palindromes like 'bb', 'abba', 'aabbaa'.
- *Why D is incorrect:* `expand(i, i+1)` should always be called. If `s[i] != s[i+1]`, the expand function immediately returns an empty string — that is correct behavior, not an error to guard against.

---

### Question 6

After the `expand` while loop in `longest_palindrome`, why is the result `s[left+1 : right]` rather than `s[left : right+1]`?

- A) Because Python slicing is inclusive on both ends, so adjustments are needed
- B) Because the while loop exits when characters don't match or a bound is exceeded — `left` has moved one too far left and `right` one too far right, so the actual palindrome is `s[left+1 : right]`
- C) Because `left+1` and `right` are the inclusive center of the palindrome
- D) Because the function returns the second half only

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python slicing `s[a:b]` is inclusive on the start, exclusive on the end. No adjustment is needed for this — the `left+1` adjustment is about correcting the overshoot, not slice semantics.
- *Why B is correct:* The while loop continues while `s[left] == s[right]`. When it exits, `left` is one position before the palindrome's left edge and `right` is one position after the palindrome's right edge. The palindrome occupies `s[left+1 : right]` — add 1 to left to step back in, use right as the exclusive end.
- *Why C is incorrect:* `left+1` is the left edge of the palindrome, not its center. The center is at the original starting position `i`.
- *Why D is incorrect:* The function returns the entire palindrome, not half of it.

---

### Question 7

Which data structure is most appropriate for autocomplete — completing a partially typed word from a stored dictionary?

- A) Hash set — O(1) lookup for any word
- B) Sorted array with binary search — O(log n) to find the prefix position
- C) Trie — O(L) to navigate to the prefix node, then enumerate all words in that subtree
- D) Max-heap — O(log n) to retrieve the most common word

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A hash set supports exact membership testing in O(1), but cannot answer prefix queries efficiently. Finding all words with prefix 'pre' requires scanning all stored words — O(n) — making it impractical for autocomplete.
- *Why B is incorrect:* Binary search on a sorted array locates a prefix in O(log n) and can scan forward for matches. This works but is less elegant than a Trie and does not improve on O(k) enumeration of results.
- *Why C is correct:* The Trie is the canonical autocomplete structure. Navigate to the prefix node in O(L), then enumerate all words in the subtree by DFS. Purpose-built for this query pattern and used in production autocomplete systems.
- *Why D is incorrect:* A max-heap supports finding the largest element in O(1). It has no concept of prefix matching — it orders by value, not by character structure.

---

### Question 8

Trace `length_of_longest_substring('dvdf')`. What is `left` when `right = 3`?

- A) `left = 0` — no duplicates encountered yet
- B) `left = 1` — moved past the duplicate 'd' at index 0, so left = char_index['d'] + 1 = 1
- C) `left = 2` — moved past both 'd' and 'v'
- D) `left = 3` — left and right converge on the last character

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* At right=2, char='d' is a duplicate of the 'd' at index 0. Since `char_index['d']=0 >= left(0)`, left moves to 1. So left is not 0 at right=3.
- *Why B is correct:* Full trace: right=0,'d': left=0, char_index={'d':0}, len=1. right=1,'v': left=0, char_index adds 'v', len=2. right=2,'d': duplicate at index 0 >= left(0) → left=1, char_index['d']=2, len=2. right=3,'f': no duplicate, char_index['f']=3, len=max(2, 3-1+1)=3. At right=3, left=1. Return 3 (substring 'vdf').
- *Why C is incorrect:* 'v' at index 1 is not a duplicate — 'v' appears only once in 'dvdf'. Left only moves when a duplicate of the current character is found within the window; moving past 'v' is unnecessary.
- *Why D is incorrect:* left=3 would mean the window is a single character at right=3. But the window is 'vdf' (indices 1 through 3, length 3), so left=1, not 3.

---

### Question 9

A student implements `starts_with` by checking `node.is_end` at the end of prefix traversal. What bug does this introduce?

- A) No bug — checking `is_end` at the prefix end is correct for `starts_with`
- B) `starts_with` would return False for any prefix that is not itself a complete stored word, even if longer words with that prefix exist
- C) `starts_with` would return True even when no words are stored in the Trie
- D) The traversal would skip characters that appear more than once in the prefix

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Checking `is_end` is correct for `search`, not `starts_with`. `is_end` marks whether a full word ends at that node — it is False for nodes that are only intermediate prefixes of longer words.
- *Why B is correct:* If the Trie stores 'apple' but not 'app', then at the end of prefix 'app', `is_end = False` (no word ends at that 'p' node). A buggy `starts_with` checking `is_end` would return False — even though 'apple' starts with 'app'. The correct `starts_with` returns True whenever the prefix path exists, regardless of `is_end`.
- *Why C is incorrect:* If no words are stored, the children dictionary is empty, and prefix traversal would fail at the first character — returning False before reaching any `is_end` check.
- *Why D is incorrect:* Repeated characters in the prefix are handled correctly by the traversal loop — each character maps to a child node independently of repetition.

---

### Question 10

`min_window('a', 'aa')` should return `''`. Why can't the algorithm find a valid window?

- A) Because the string 'a' has length 1 and the algorithm requires length ≥ 2
- B) Because t='aa' requires two 'a' characters, but s='a' contains only one — the window can never satisfy `have['a'] == need['a']` (which is 2), so `formed` never reaches `required`
- C) Because the algorithm only works when t is a subset of the alphabet of s
- D) Because the `Counter` of 'aa' produces `{'a': 1}`, which matches `have['a'] = 1` after seeing one 'a'

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* There is no minimum length requirement in the algorithm. A one-character string is valid input. `min_window('a', 'a')` correctly returns 'a'.
- *Why B is correct:* `need = Counter('aa') = {'a': 2}`. The algorithm increments `formed` only when `have[char] == need[char]`. Since s='a' has only one 'a', `have['a']` reaches 1 but never 2. `formed` never reaches `required = 1` (there is 1 distinct character needed with count 2). The inner while loop never executes, and `min_len` remains infinity — the function returns ''.
- *Why C is incorrect:* The algorithm does not require t to be a subset of the alphabet. It handles the impossibility case by returning '' when `min_len` is still infinity at the end.
- *Why D is incorrect:* `Counter('aa') = {'a': 2}`, not `{'a': 1}`. The Counter correctly reflects the frequency of each character in t.
