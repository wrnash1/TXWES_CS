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

---

### Question 11

A Trie stores ['apple', 'app', 'apply']. What does `trie.search('appl')` return?

- A) True — 'appl' is a prefix of stored words so the path exists
- B) False — 'appl' was not inserted, so `is_end = False` at the node after the second 'p'
- C) True — any path that exists returns True for search
- D) An error — 'appl' is neither a full word nor a full prefix

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `search` requires `is_end = True` at the terminal node, not just that the path exists. The node for the second 'p' in 'appl' was created when 'apple' and 'apply' were inserted, but `is_end` was never set there. Path existence is `starts_with`'s criterion, not `search`'s.
- *Why B is correct:* Traversing 'a'→'p'→'p'→'l' succeeds (all nodes exist from 'apple'/'apply' insertions). At the 'l' node, `is_end = False` because no word 'appl' was inserted. `search` returns `node.is_end`, which is False.
- *Why C is incorrect:* Returning True for any existing path would make `search` equivalent to `starts_with`. The two methods have different semantics: `search` requires a complete word; `starts_with` only requires the path.
- *Why D is incorrect:* The Trie handles partial paths without errors. Traversing 'appl' succeeds silently — it simply reaches a node where `is_end = False`.

---

### Question 12

`length_of_longest_substring('pwwkew')` returns 3 ('wke'). What is `left` when `right = 4` (character 'e')?

- A) `left = 0`
- B) `left = 1`
- C) `left = 2`
- D) `left = 3`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* At right=2, 'w' is a duplicate of 'w' at index 1. Since `char_index['w']=1 >= left(0)`, left advances to 2. left is no longer 0 after right=2.
- *Why B is incorrect:* After the 'w' duplicate at right=2, left becomes 2. At right=3 ('k'), no duplicate, left stays 2. At right=4 ('e'), no duplicate, left stays 2.
- *Why C is correct:* Trace: right=0,'p': no dup, left=0. right=1,'w': no dup, left=0. right=2,'w': dup at index 1 >= left(0) → left=2, char_index['w']=2. right=3,'k': no dup, left=2. right=4,'e': no dup, left=2. At right=4, left=2.
- *Why D is incorrect:* Left reaches 3 only if a duplicate is found inside the window at right=3 or right=4. 'k' and 'e' have not appeared before in the string — no jump occurs.

---

### Question 13

In `find_anagrams('abab', 'ab')`, the function returns `[0, 1, 2]`. Why is index 1 included — isn't 'ba' at index 1 not an anagram of 'ab'?

- A) 'ba' is not an anagram of 'ab' — the function has a bug
- B) 'ba' is an anagram of 'ab' — anagrams are unordered character sets; both contain exactly one 'a' and one 'b'
- C) Index 1 is included because 'a' and 'b' are adjacent characters in the alphabet
- D) The function counts all substrings of equal length, not just anagrams

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The function is correct. By definition, two strings are anagrams if and only if they have the same character counts (regardless of order). 'ba' has one 'a' and one 'b' — identical to 'ab'. The Counter comparison `{'a':1,'b':1} == {'a':1,'b':1}` is True.
- *Why B is correct:* An anagram is a rearrangement of characters. 'ba' and 'ab' are anagrams because they contain the same characters in possibly different order. The `Counter` comparison captures this: `Counter('ba') == Counter('ab')` is True.
- *Why C is incorrect:* Adjacency in the alphabet has no bearing on anagram detection. 'ab' and 'ba' are anagrams of each other because of character frequency equality, not alphabet position.
- *Why D is incorrect:* The function specifically checks `have == need` (Counter equality), which only matches when character frequencies are identical. Substrings with different characters would fail this check.

---

### Question 14

`longest_palindrome('racecar')` returns 'racecar'. When `expand(3, 3)` is called (center = 'e' at index 3), what is the sequence of `(left, right)` values during the while loop?

- A) (3,3) → exits immediately because 'e' has no matching character
- B) (3,3) → (2,4) → (1,5) → (0,6) → (-1,7) — exits when left=-1
- C) (3,3) → (2,4) → exits because 'c' ≠ 'a' at positions 2 and 4
- D) (3,3) → (2,4) → (1,5) → exits because index 1 is out of bounds

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The while loop starts with `left=right=3`, which means `s[3]==s[3]` ('e'=='e') — always True. The loop does not exit immediately; it expands outward.
- *Why B is correct:* Starting at (3,3): s[3]='e'==s[3]='e' → left=2,right=4. s[2]='c'==s[4]='c' → left=1,right=5. s[1]='a'==s[5]='a' → left=0,right=6. s[0]='r'==s[6]='r' → left=-1,right=7. Now left=-1 < 0 → loop exits. Return `s[-1+1:7] = s[0:7] = 'racecar'`. Correct.
- *Why C is incorrect:* s[2]='c' and s[4]='c' — these ARE equal (they match). The loop does not exit at this step.
- *Why D is incorrect:* There is no index 1 out-of-bounds issue. The bounds check is `left >= 0 and right < len(s)`. Index 1 is well within bounds for 'racecar' (length 7).

---

### Question 15

In `min_window`, when does `formed` decrement? What triggers it?

- A) When `left` advances past any character
- B) When the count of a character in `have` drops below its required count in `need` while shrinking the window
- C) When `right` reaches the end of the string
- D) When `formed == required` and the window is recorded

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `formed` does not decrement for every character removal. It only decrements when removing a required character causes the window to no longer satisfy that character's count requirement.
- *Why B is correct:* Inside the inner while loop: after decrementing `have[lc]`, if `lc in need and have[lc] < need[lc]`, it means we no longer have enough of character `lc` — this required character is no longer satisfied. `formed -= 1` exits the inner loop and continues expanding the outer window.
- *Why C is incorrect:* `formed` is a counter of satisfied character types — it is not related to the position of `right`. The outer loop advances `right`, but that increments `formed`, not decrements it.
- *Why D is incorrect:* Recording the minimum window and decrementing `formed` are separate operations. The window is recorded first (`min_len` update), then the left side is shrunk. `formed` decrements only if the shrink violates a character requirement.

---

### Question 16

What is the total number of `expand` calls made by `longest_palindrome` on a string of length n?

- A) n — one call per character
- B) 2n − 1 — one odd-center call per character and one even-center call per adjacent pair
- C) 2n — n odd-center calls and n even-center calls
- D) n² — each character is compared with every other

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The outer loop makes two `expand` calls per index: `expand(i, i)` for odd and `expand(i, i+1)` for even. One call per character underestimates by half.
- *Why B is incorrect:* There are n−1 adjacent pairs (even centers) but n single characters (odd centers), giving n + (n−1) = 2n−1 total if we count distinct centers. However, the code calls `expand(i, i+1)` for all i in `range(n)`, including i=n-1 where `expand(n-1, n)` immediately exits (out of bounds) — so the loop makes exactly n odd calls and n even calls = 2n total calls.
- *Why C is correct:* The `for i in range(len(s))` loop runs n times. Each iteration calls `expand(i, i)` once and `expand(i, i+1)` once. Total: 2n calls. (The last even call `expand(n-1, n)` exits immediately since `right=n >= len(s)`.)
- *Why D is incorrect:* O(n²) describes the worst-case total work inside expand (e.g., for 'aaaa...a', every expansion goes to the full length). But the number of expand calls is 2n — fixed. The total character comparisons can be O(n²), but that is different from the number of calls.

---

### Question 17

Which of the following correctly distinguishes when to use a Trie versus a hash set for string problems?

- A) Use a Trie when the string keys are integers; use a hash set when keys are alphabetic
- B) Use a Trie for prefix queries and autocomplete; use a hash set for exact membership tests where prefix queries are not needed
- C) Use a Trie for small alphabets only (≤ 26 characters); use a hash set for Unicode strings
- D) Use a Trie when strings are sorted; use a hash set when strings are unsorted

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both data structures handle string keys regardless of character type. Integer vs. alphabetic is not the relevant distinction.
- *Why B is correct:* The core trade-off: a hash set gives O(L) average case for exact lookup (hashing the full string) but cannot answer "does any stored word start with 'pre'?" without scanning all words. A Trie answers prefix queries in O(prefix_length) — it is structurally built for prefix traversal. When exact lookup is all that is needed, the hash set's simplicity and constant-time hash wins.
- *Why C is incorrect:* Tries work for any alphabet. A hash-map-based Trie (using Python dicts for children) handles arbitrary Unicode characters without any alphabet-size restriction.
- *Why D is incorrect:* Neither structure requires sorted input. The Trie's ordering is implicit in the character-level tree structure. A hash set has no ordering at all. Sorting is irrelevant to the choice between them.

---

### Question 18

`is_palindrome('A man, a plan, a canal: Panama')` returns True. What do the two inner while loops in the two-pointer implementation accomplish?

- A) They reverse the string before comparison
- B) They skip non-alphanumeric characters so that only letters and digits are compared
- C) They advance both pointers to the center of the string
- D) They count the number of spaces and punctuation characters

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The string is never reversed. Two-pointer palindrome check compares characters from both ends toward the center — no reversal is performed.
- *Why B is correct:* The inner while loops advance `left` rightward and `right` leftward while `not s[left].isalnum()` and `not s[right].isalnum()` respectively. This skips commas, spaces, colons, and other non-alphanumeric characters so only letters/digits are compared. 'A man...' becomes effectively 'amanaplanacanalpanama' for comparison purposes.
- *Why C is incorrect:* The inner loops skip non-alphanumeric characters — they do not advance to the center. The center is reached gradually as `left` and `right` converge through the outer while loop.
- *Why D is incorrect:* The algorithm does not count non-alphanumeric characters. It simply skips over them without accumulating a count.

---

### Question 19

In `find_anagrams`, why is `del have[left_char]` called when `have[left_char] == 0` rather than leaving zero in the dict?

- A) Deleting zeros is required to prevent integer overflow in the Counter
- B) The comparison `have == need` would fail if `have` contains keys with value 0 that are absent from `need` — deleting zeros keeps the Counter clean for equality comparison
- C) Leaving zeros in the dict causes a KeyError on the next access
- D) Deleting zeros reduces memory usage, which is critical for correctness

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python integers do not overflow. Memory is not a correctness concern here. The reason for deletion is about `Counter` equality, not arithmetic overflow.
- *Why B is correct:* `Counter({'a': 0}) != Counter({})` in Python. If `have` contains `{'a': 0, 'b': 1}` and `need` contains `{'b': 1}`, they are not equal — even though 'a' with count 0 means "no 'a' present." Deleting zero-count keys ensures `have` only contains characters with a positive count, making `have == need` a correct equality check.
- *Why C is incorrect:* Python dicts do not raise KeyError for zero values. The code later accesses `have[new_char]` with `have[new_char] += 1` (via `get` pattern in some implementations), which handles missing keys correctly. The deletion is not about KeyError prevention.
- *Why D is incorrect:* Memory reduction from deleting a few zero entries is negligible and is not relevant to correctness. The correctness reason is the Counter equality check as described in B.

---

### Question 20

What is the space complexity of a Trie storing N words each of length L over an alphabet of size A?

- A) O(N) — one node per word
- B) O(N × L) — one node per character across all words
- C) O(N × L × A) — in the worst case (no shared prefixes), each node has space for A children pointers
- D) O(L) — depth is L and only one path is needed

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(N) would require each word to be stored in a single node — like a hash set. A Trie stores individual characters at each node, so a word of length L requires L nodes (in the worst case of no prefix sharing).
- *Why B is incorrect:* O(N × L) accounts for the number of nodes but ignores the per-node storage for children pointers. If each node stores an array of A pointers (common in fixed-alphabet implementations), the space per node is O(A), not O(1).
- *Why C is correct:* Worst case: N words with no shared prefixes, each of length L. This creates N × L nodes. Each node stores up to A children pointers (e.g., a 26-element array for lowercase English). Total space: O(N × L × A). In practice, prefix sharing reduces this significantly, but O(N × L × A) is the theoretical upper bound.
- *Why D is incorrect:* O(L) would describe the depth of one path, not the total storage for N words. With N words, there are up to N × L nodes and the space grows with both N and L.
