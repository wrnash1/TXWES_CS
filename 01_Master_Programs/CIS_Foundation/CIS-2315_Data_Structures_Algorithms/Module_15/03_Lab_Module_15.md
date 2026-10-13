# Lab Activity: Module 15 — String Algorithms & Trie

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement Trie (LeetCode #208)
- **Part 2** — Sliding window: Longest Substring Without Repeating Characters and Find Anagrams
- **Part 3** — Minimum Window Substring and Longest Palindromic Substring

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Trie

**File:** `lab15_strings.py`

### 1.1 — TrieNode and Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char → TrieNode
        self.is_end = False   # True if a complete word ends here

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert word. Time: O(L)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """
        Return True if word was inserted (exact match). Time: O(L)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        """
        Return True if any inserted word starts with prefix. Time: O(L)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

Test:

```python
trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.insert('apply')
trie.insert('ape')

print(trie.search('apple'))       # True
print(trie.search('app'))         # True — 'app' was explicitly inserted
print(trie.search('ap'))          # False — 'ap' not inserted
print(trie.starts_with('ap'))     # True — 'app', 'apple', 'apply', 'ape' all start with 'ap'
print(trie.starts_with('apl'))    # True — 'apply' starts with 'apl'
print(trie.starts_with('b'))      # False
print(trie.search('appl'))        # False — path exists but is_end=False at 'l'
```

**Checkpoint:** All seven outputs correct. The critical distinction: `search('ap')` is False (path exists but no word ends there), while `starts_with('ap')` is True.

---

### 1.2 — Trie with Count Words by Prefix

```python
class TrieWithCount:
    """Trie that counts how many inserted words start with each prefix."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def count_starts_with(self, prefix):
        """Return number of inserted words that start with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self._count_words(node)

    def _count_words(self, node):
        count = 1 if node.is_end else 0
        for child in node.children.values():
            count += self._count_words(child)
        return count
```

Test:

```python
tc = TrieWithCount()
for word in ['apple', 'app', 'apply', 'ape', 'banana']:
    tc.insert(word)

print(tc.count_starts_with('ap'))       # 4 — apple, app, apply, ape
print(tc.count_starts_with('app'))      # 3 — apple, app, apply
print(tc.count_starts_with('appl'))     # 2 — apple, apply
print(tc.count_starts_with('b'))        # 1 — banana
print(tc.count_starts_with('c'))        # 0
```

**Checkpoint:** All five counts correct.

---

## Part 2 — Sliding Window

### 2.1 — Longest Substring Without Repeating Characters (LeetCode #3)

```python
def length_of_longest_substring(s):
    """
    Longest substring with no repeated characters.
    Time: O(n), Space: O(A) where A is alphabet size
    """
    char_index = {}    # char → most recent index seen
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1    # skip past the duplicate
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

Test:

```python
print(length_of_longest_substring('abcabcbb'))    # 3 — 'abc'
print(length_of_longest_substring('bbbbb'))       # 1 — 'b'
print(length_of_longest_substring('pwwkew'))      # 3 — 'wke'
print(length_of_longest_substring(''))            # 0
print(length_of_longest_substring('abcdef'))      # 6 — no repeats
```

**Trace `'abcabcbb'`:**

```text
right=0 'a': no dup. window=[0,0], len=1
right=1 'b': no dup. window=[0,1], len=2
right=2 'c': no dup. window=[0,2], len=3
right=3 'a': dup at 0 >= left(0). left=1. window=[1,3], len=3
right=4 'b': dup at 1 >= left(1). left=2. window=[2,4], len=3
right=5 'c': dup at 2 >= left(2). left=3. window=[3,5], len=3
right=6 'b': dup at 4 >= left(3). left=5. window=[5,6], len=2
right=7 'b': dup at 6 >= left(5). left=7. window=[7,7], len=1
Return 3 ✓
```

**Checkpoint:** All five tests correct. Submit to LeetCode #3.

---

### 2.2 — Find All Anagrams in a String (LeetCode #438)

```python
from collections import Counter

def find_anagrams(s, p):
    """
    Return list of starting indices of p's anagrams in s.
    Sliding window of fixed size len(p).
    Time: O(n), Space: O(A)
    """
    if len(p) > len(s):
        return []

    need = Counter(p)
    have = Counter(s[:len(p)])
    result = [0] if have == need else []

    for i in range(1, len(s) - len(p) + 1):
        # slide window: remove leftmost char, add new rightmost char
        left_char = s[i - 1]
        have[left_char] -= 1
        if have[left_char] == 0:
            del have[left_char]

        new_char = s[i + len(p) - 1]
        have[new_char] += 1

        if have == need:
            result.append(i)

    return result
```

Test:

```python
print(find_anagrams('cbaebabacd', 'abc'))    # [0, 6]
print(find_anagrams('abab', 'ab'))           # [0, 1, 2]
print(find_anagrams('aa', 'bb'))             # []
```

**Checkpoint:** All three tests correct.

---

## Part 3 — Minimum Window Substring and Palindromes

### 3.1 — Minimum Window Substring (LeetCode #76)

```python
def min_window(s, t):
    """
    Minimum window in s containing all characters of t.
    Time: O(|s| + |t|), Space: O(|s| + |t|)
    """
    if not t or not s:
        return ''

    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0
    left = 0
    min_len = float('inf')
    min_start = 0

    for right, char in enumerate(s):
        have[char] = have.get(char, 0) + 1
        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            lc = s[left]
            have[lc] -= 1
            if lc in need and have[lc] < need[lc]:
                formed -= 1
            left += 1

    return s[min_start : min_start + min_len] if min_len != float('inf') else ''
```

Test:

```python
print(min_window('ADOBECODEBANC', 'ABC'))    # 'BANC'
print(min_window('a', 'a'))                  # 'a'
print(min_window('a', 'aa'))                 # '' — impossible
print(min_window('ab', 'b'))                 # 'b'
```

**Trace key steps for `min_window('ADOBECODEBANC', 'ABC')`:**

```text
need={'A':1,'B':1,'C':1}, required=3

Expand right until formed=3:
  A(0): formed=1. B(3): formed=2. C(5): formed=3.
  Window 'ADOBEC' (len=6). Shrink: remove A → formed=2.
  Record: min_len=6, min_start=0.

Continue expanding... reach A again at index 9:
  formed=3 again. Window contains 'DOBECODEBA...': shrink aggressively.
  Eventually window='BANC' (indices 9-12, len=4).
  Shrink: remove B → formed=2. Record: min_len=4, min_start=9.

Return s[9:13] = 'BANC' ✓
```

**Checkpoint:** All four tests correct. Submit to LeetCode #76.

---

### 3.2 — Longest Palindromic Substring (LeetCode #5)

```python
def longest_palindrome(s):
    """
    Expand around each center (odd and even length).
    Time: O(n²), Space: O(1)
    """
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]    # slice: left overshot left, right overshot right

    result = ''
    for i in range(len(s)):
        odd  = expand(i, i)
        even = expand(i, i+1)
        if len(odd)  > len(result): result = odd
        if len(even) > len(result): result = even
    return result
```

Test:

```python
print(longest_palindrome('babad'))      # 'bab' or 'aba' (both valid)
print(longest_palindrome('cbbd'))       # 'bb'
print(longest_palindrome('a'))          # 'a'
print(longest_palindrome('racecar'))    # 'racecar'
print(longest_palindrome('abacaba'))    # 'abacaba'
```

**Checkpoint:** All five tests correct (for 'babad', either 'bab' or 'aba' is accepted). Submit to LeetCode #5.

---

### 3.3 — Valid Palindrome (LeetCode #125)

```python
def is_palindrome(s):
    """
    Check if s is a palindrome considering only alphanumeric characters, case-insensitive.
    Time: O(n), Space: O(1) with two-pointer approach
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

Test:

```python
print(is_palindrome('A man, a plan, a canal: Panama'))    # True
print(is_palindrome('race a car'))                         # False
print(is_palindrome(' '))                                   # True — empty after filtering
```

**Checkpoint:** All three tests correct.

---

### 3.4 — Integration Test

```python
def test_all():
    # Trie
    trie = Trie()
    trie.insert('apple')
    trie.insert('app')
    assert trie.search('apple') == True
    assert trie.search('app')   == True
    assert trie.search('ap')    == False
    assert trie.starts_with('ap') == True
    assert trie.starts_with('b')  == False

    # Longest substring
    assert length_of_longest_substring('abcabcbb') == 3
    assert length_of_longest_substring('bbbbb') == 1

    # Find anagrams
    assert find_anagrams('cbaebabacd', 'abc') == [0, 6]

    # Min window
    assert min_window('ADOBECODEBANC', 'ABC') == 'BANC'
    assert min_window('a', 'aa') == ''

    # Longest palindrome
    result = longest_palindrome('babad')
    assert result in ('bab', 'aba')
    assert longest_palindrome('cbbd') == 'bb'

    # Valid palindrome
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('race a car') == False

    print('All assertions passed.')

test_all()
```

---

## Deliverables

Submit to Canvas:

1. `lab15_strings.py` — all implementations and integration test
2. LeetCode submission screenshots for #208, #3, #76, #5
3. Short written answer (3–5 sentences): Explain the `char_index[char] >= left` guard in `length_of_longest_substring`. What happens if you remove it? Give a concrete example where removing it produces the wrong answer.

---

## Summary

| Concept | Key Point |
|---|---|
| Trie insert | O(L) — create node for each new char |
| Trie search vs starts_with | search requires `is_end=True`; starts_with only needs path |
| Sliding window | Expand right, contract left on violation |
| Longest substring no repeat | `char_index[char] >= left` guard prevents backward jump |
| Minimum window substring | `formed == required` triggers shrink phase |
| Expand-around-center | Both `expand(i,i)` and `expand(i,i+1)` required |
| Valid palindrome | Two pointers skip non-alphanumeric, compare case-insensitive |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Word Search II (LeetCode #212)

Given an m×n board of characters and a list of words, find all words in the board. The naive approach — calling `exist()` (LeetCode #79) for each word — is O(words × m × n × 4^L) and too slow for large inputs. The optimal solution builds a Trie from all words, then runs a single DFS over the board — at each cell, follow the Trie branch for the current character. When `is_end = True` is reached, record the word and mark it found. Implement this solution, verify it finds `['eat', 'oath']` in the standard test board, and explain why using a Trie reduces the time complexity compared to calling `exist()` once per word.

### 9.2 — Rabin-Karp Rolling Hash for Substring Search

The naive substring search (check every position) is O(n×m) where n=text length, m=pattern length. Rabin-Karp uses a rolling hash: compute the hash of the pattern and the first window; then slide the window by removing the leftmost character and adding the new rightmost — each slide is O(1) arithmetic. Implement `rabin_karp(text, pattern)` using polynomial hashing with a prime base and modulus. Verify it finds the correct starting index for `rabin_karp('abcxabcdabcdabcy', 'abcdabcy')`. Handle hash collisions by doing a character-by-character confirmation when hashes match. State the average case O(n+m) complexity and the worst case O(n×m) (many hash collisions).

### 9.3 — Trie Delete and Prefix Count

Extend your `Trie` class with two new methods: `delete(word)` removes a word from the Trie, cleaning up nodes that are no longer needed (a node can be deleted if it has no children and `is_end = False` after removing the word). Implement deletion recursively. Then add `count_words_with_prefix(prefix)` — which counts how many stored words begin with the given prefix using a DFS from the prefix node. Verify: insert ['app','apple','apply','ape','banana'], delete 'app', then `search('app')=False`, `starts_with('app')=True` (because 'apple' and 'apply' still exist), and `count_words_with_prefix('app')=2`. Explain why deleting 'app' does not remove the 'a'→'p'→'p' path.
