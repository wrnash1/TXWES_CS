# Reading Guide: Module 15 — String Algorithms & Trie

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

Strings are the most common data type in technical interviews. Most string problems can be solved with a small set of patterns: the sliding window, two pointers, hash maps, and the Trie data structure. This module covers four core topics: the Trie (for prefix-based operations), the sliding window (for contiguous substring problems), expand-around-center (for palindromes), and the Minimum Window Substring. Mastering these patterns gives you the tools to approach the majority of string interview questions.

---

## 1. Trie (Prefix Tree)

### Structure

A Trie stores strings by sharing common prefixes. Each node represents a single character. The path from the root to any `is_end = True` node spells a complete stored word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char → TrieNode
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Exact match — requires is_end = True at the last character."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        """Prefix match — path must exist, is_end not required."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### Complexity

| Operation | Time | Space |
|---|---|---|
| Insert | O(L) | O(L) per new word |
| Search (exact) | O(L) | O(1) |
| Starts_with | O(L) | O(1) |
| Total space | — | O(N × L × A) |

L = word length, N = number of words, A = alphabet size (26 for lowercase English).

### Why Trie over Hash Set?

A hash set supports O(1) exact lookup but cannot efficiently answer prefix queries. The Trie answers "does any stored word start with 'pre'?" in O(L) without scanning all words. This matters for autocomplete, spell-check, and IP routing.

---

## 2. Sliding Window

### Pattern

Two pointers: `left` and `right` delimit a window (contiguous substring). Expand `right` to grow the window; advance `left` when the window violates a constraint.

```python
# Template: find the longest window satisfying a condition
left = 0
state = {}    # window state (character counts, etc.)

for right, char in enumerate(s):
    # add char to state
    while state_is_invalid():
        # remove s[left] from state
        left += 1
    # update answer using current window [left..right]
```

### Longest Substring Without Repeating Characters (LeetCode #3)

```python
def length_of_longest_substring(s):
    """Time: O(n), Space: O(A)"""
    char_index = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Key insight:** `char_index[char] >= left` — only move `left` if the duplicate is inside the current window. A duplicate seen before the window started is harmless.

**Alternative:** maintain a `seen` set; remove characters from the set as `left` advances.

### Minimum Window Substring (LeetCode #76)

```python
from collections import Counter

def min_window(s, t):
    """
    Shortest window in s containing all characters of t.
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

**Two counters pattern:** `required` = number of distinct characters needed. `formed` = number satisfied. When `formed == required`, shrink from the left. This avoids O(A) comparison of `have` and `need` on every step.

---

## 3. Longest Palindromic Substring (LeetCode #5)

### Expand-Around-Center

Every palindrome has a center. For n characters, there are n odd-length centers (each character) and n-1 even-length centers (each gap between adjacent characters). Expand outward while the characters match.

```python
def longest_palindrome(s):
    """Time: O(n²), Space: O(1)"""
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]    # left and right overshot by one

    result = ''
    for i in range(len(s)):
        odd  = expand(i, i)
        even = expand(i, i+1)
        if len(odd)  > len(result): result = odd
        if len(even) > len(result): result = even
    return result
```

**Slice explanation:** After the while loop, `left` is one position to the left of the palindrome boundary, and `right` is one position to the right. `s[left+1 : right]` extracts exactly the palindrome (Python slice: inclusive start, exclusive end).

### Valid Palindrome (LeetCode #125)

```python
def is_palindrome(s):
    """Check if s (alphanumeric only, case-insensitive) is a palindrome."""
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]
```

Two-pointer approach (O(1) space): `left=0`, `right=len-1`; skip non-alphanumeric; compare `s[left].lower()` and `s[right].lower()`.

---

## 4. Additional String Patterns

### Anagram Check

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

def find_anagrams(s, p):
    """LeetCode #438: indices where p's anagram starts in s."""
    need = Counter(p)
    have = Counter(s[:len(p)])
    result = [0] if have == need else []
    for i in range(1, len(s) - len(p) + 1):
        have[s[i-1]] -= 1
        if have[s[i-1]] == 0:
            del have[s[i-1]]
        have[s[i + len(p) - 1]] += 1
        if have == need:
            result.append(i)
    return result
```

### Valid Parentheses

```python
def is_valid(s):
    """LeetCode #20: check balanced brackets."""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif not stack or stack[-1] != pairs[char]:
            return False
        else:
            stack.pop()
    return len(stack) == 0
```

---

## 5. Trie vs. Hash Set vs. Sorted List

| Use case | Best structure |
|---|---|
| Exact string lookup | Hash set — O(1) |
| Prefix queries | Trie — O(L) |
| Alphabetical order | Sorted list / BST — O(log n) |
| Autocomplete | Trie — O(L + output) |
| Anagram grouping | Hash map with sorted key — O(L log L) |

---

## 6. Interview Exam Tips

1. **Sliding window = expand right, contract left** — the two operations are always this way. Expanding left or contracting right would move in the wrong direction.

2. **`char_index[char] >= left` is essential** — without this guard, you might move `left` backward (to before the current window start), which would be wrong. The duplicate only matters if it's inside the current window.

3. **Trie `search` vs. `starts_with`** — `search` requires `is_end = True`; `starts_with` does not. A common interview mistake: returning `True` from `search` when only the path exists but the word is not complete (e.g., stored 'apple', searching 'app' without inserting 'app').

4. **Even-length palindromes** — a common off-by-one: only calling `expand(i, i)` misses all even-length palindromes. Always call `expand(i, i+1)` as well.

5. **`formed == required` pattern** — for Minimum Window Substring, counting distinct satisfied characters with `formed` is cleaner and faster than comparing full dictionaries at every step.

6. **Trie space is O(N × L × A) in the worst case** — mention this in interviews. For large alphabets or very long words, a hash-map-based Trie is standard. For fixed alphabets (26 lowercase letters), a 26-element array per node is an optimization.

7. **Palindrome check with two pointers** — for LeetCode #125 (valid palindrome with non-alphanumeric filtering), cleaning the string first is cleaner in Python. For space-constrained languages, use two pointers that skip non-alphanumeric characters.

8. **Minimum Window Substring is hard** — it is a sliding window problem with two counters, but the shrinking logic is subtle. In interviews, draw the window on the string before coding.

---

## 7. Complexity Summary

| Problem | Pattern | Time | Space |
|---|---|---|---|
| Implement Trie (insert/search) | Trie | O(L) per op | O(N×L×A) |
| Longest substring no repeat | Sliding window | O(n) | O(A) |
| Minimum Window Substring | Sliding window | O(n+m) | O(n+m) |
| Longest Palindromic Substring | Expand center | O(n²) | O(1) |
| Valid Palindrome | Two pointers | O(n) | O(1) |
| Find Anagrams | Sliding window + Counter | O(n) | O(A) |

---

## 8. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Trie Visualization** — [https://visualgo.net/en/suffixtree](https://visualgo.net/en/suffixtree)
   VisuAlgo's trie and suffix tree visualizer shows the character-by-character construction of a Trie. Step through insertions to see node creation, `is_end` marking, and shared prefix paths. Useful for verifying that `search` and `starts_with` traverse the same path with different terminal conditions.

2. **NeetCode — Sliding Window & Trie Playlists (YouTube)** — [https://www.youtube.com/c/NeetCode](https://www.youtube.com/c/NeetCode)
   Free video walkthroughs for LeetCode #3 (Longest Substring Without Repeating Characters), #76 (Minimum Window Substring), #5 (Longest Palindromic Substring), and #208 (Implement Trie). Each video includes a whiteboard trace of the algorithm before coding.

3. **OpenDSA — String Matching and Tries** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Trie.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Trie.html)
   Free interactive OER textbook coverage of Trie structure, insertion, and search with embedded exercises. Includes a discussion of Trie space complexity and comparison with hash maps for prefix queries.

4. **Python `collections.Counter` Documentation** — [https://docs.python.org/3/library/collections.html#collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
   Official Python documentation for `Counter` — the hash map used in Minimum Window Substring and Find Anagrams. Covers `Counter` arithmetic, `most_common()`, set operations, and the `==` comparison used in the fixed-window anagram check.

5. **CP-Algorithms — String Hashing and Z-Function** — [https://cp-algorithms.com/string/string-hashing.html](https://cp-algorithms.com/string/string-hashing.html)
   Free competitive programming reference covering polynomial rolling hash for O(n) string comparison — the technique behind Rabin-Karp substring search. Also covers the Z-function (linear-time prefix match) as an alternative to the Trie for pattern matching. Both are interview-adjacent topics that appear in advanced string problems.

---

## 9. Study Checklist

- [ ] Watch the Module 15 video lecture by Professor Nash.
- [ ] Implement `Trie` with `insert`, `search`, `starts_with` from scratch.
- [ ] Implement `length_of_longest_substring` and trace `'abcabcbb'`.
- [ ] Implement `min_window` and trace `min_window('ADOBECODEBANC', 'ABC')`.
- [ ] Implement `longest_palindrome` and verify both odd and even center cases.
- [ ] Complete the Module 15 Lab.
- [ ] Complete the Module 15 Quiz.
- [ ] Solve LeetCode #208, #3, #76, #5.
