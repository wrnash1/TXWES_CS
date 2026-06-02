# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 15 — String Algorithms & Trie

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - The key concept for Trie: it trades space for search speed. Insert and search are both O(L) where L is the word length — independent of how many words are stored.
> - Sliding window is the dominant string interview pattern. Emphasize: expand right pointer, contract left pointer when the window violates the constraint.
> - Walk `lengthOfLongestSubstring` carefully — the "move left to char_after_duplicate" shortcut is the key insight.
> - For Minimum Window Substring, two counters (required vs. formed) are essential — trace the window on "ADOBECODEBANC" explicitly.
> - Longest Palindromic Substring: expand-around-center is O(n²) and dead simple — preferred over Manacher's in interviews.
> - Common mistakes: off-by-one in sliding window (using `>` vs `>=`), forgetting to handle even-length palindromes in expand-around-center.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 15 | String Algorithms & Trie | CIS-2315"]**

"Strings are the single most common data type in technical interviews. String problems test your understanding of sliding windows, two pointers, hash maps, and tree data structures — all in the context of character sequences. This module covers four topics: the Trie (prefix tree), the sliding window pattern for string problems, palindrome expansion, and the Minimum Window Substring. These four techniques cover the majority of string-focused interview questions."

---

## [01:30 – 08:00] Part 1 — The Trie

**[SHOW SLIDE: "Trie — Prefix Tree"]**

"A Trie — short for retrieval tree — is a tree data structure where each node represents a single character, and paths from the root spell out words. It is optimized for prefix-based operations: insert a word in O(L) time, search for a word in O(L) time, and check if any stored word starts with a given prefix in O(L) time — all independent of how many words are stored.

[PAUSE]

**[SHOW DIAGRAM: Trie storing 'apple', 'app', 'apply', 'ape']**

Each node has a dictionary mapping characters to child nodes, plus a boolean flag `is_end` marking whether a complete word ends here.

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char → TrieNode
        self.is_end = False   # True if a word ends here

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        \"\"\"
        Insert word into the trie.
        Time: O(L) where L = len(word)
        \"\"\"
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        \"\"\"
        Return True if word is in the trie (exact match).
        Time: O(L)
        \"\"\"
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        \"\"\"
        Return True if any stored word starts with prefix.
        Time: O(L) where L = len(prefix)
        \"\"\"
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

**[DEMO: insert 'apple', 'app', 'apply'; search 'app' → True; search 'ap' → False; starts_with 'ap' → True]**

The difference between `search` and `starts_with`: search requires `is_end = True` at the last character. `starts_with` only requires that the path exists.

[PAUSE]

**Why Trie over a hash set?** A hash set can check exact membership in O(1). But a hash set cannot efficiently find all words with a given prefix — you'd have to scan all words. The Trie supports prefix queries in O(L) and can enumerate all words with a prefix in O(L + output size).

**Space:** O(N × L × A) where N = number of words, L = average length, A = alphabet size (26 for lowercase English). Each node can have up to A children."

---

## [08:00 – 14:00] Part 2 — Sliding Window: Longest Substring Without Repeating Characters

**[SHOW SLIDE: "Sliding Window for Strings"]**

"The sliding window pattern uses two pointers — left and right — to maintain a window (a contiguous substring) that satisfies some constraint. The right pointer expands the window; when the constraint is violated, the left pointer contracts it.

**[SHOW DIAGRAM: window sliding over string 'abcabcbb']**

**LeetCode #3 — Longest Substring Without Repeating Characters:**

```python
def length_of_longest_substring(s):
    \"\"\"
    Return length of longest substring with no repeated characters.
    Time: O(n), Space: O(min(n, A)) — A is alphabet size
    \"\"\"
    char_index = {}    # char → most recent index seen
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1    # move left past the duplicate
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

**[DEMO: `length_of_longest_substring('abcabcbb')` — trace:]**

```text
right=0, char='a': no dup. char_index={'a':0}. window=[0,0], len=1
right=1, char='b': no dup. char_index={'a':0,'b':1}. window=[0,1], len=2
right=2, char='c': no dup. window=[0,2], len=3
right=3, char='a': dup at 0 >= left(0). left=1. char_index['a']=3. window=[1,3], len=3
right=4, char='b': dup at 1 >= left(1). left=2. char_index['b']=4. window=[2,4], len=3
right=5, char='c': dup at 2 >= left(2). left=3. char_index['c']=5. window=[3,5], len=3
right=6, char='b': dup at 4 >= left(3). left=5. window=[5,6], len=2
right=7, char='b': dup at 6 >= left(5). left=7. window=[7,7], len=1

Return 3 ✓ (substring 'abc')
```

**Key implementation detail:** `char_index[char] >= left` — we only move left if the duplicate is inside the current window. A duplicate seen before the window started is irrelevant."

---

## [14:00 – 19:00] Part 3 — Minimum Window Substring

**[SHOW SLIDE: "Minimum Window Substring — LeetCode #76"]**

"Given strings `s` and `t`, return the shortest window of `s` that contains all characters of `t`. Return empty string if no such window exists.

Strategy: expand right until all required characters are in the window; contract left as much as possible while maintaining coverage; record the minimum window seen.

```python
from collections import Counter

def min_window(s, t):
    \"\"\"
    Minimum window in s containing all of t.
    Time: O(|s| + |t|), Space: O(|s| + |t|)
    \"\"\"
    if not t or not s:
        return ''

    need = Counter(t)       # required character counts
    have = {}               # character counts in current window
    required = len(need)    # distinct characters needed
    formed = 0              # distinct characters in window meeting their count

    left = 0
    min_len = float('inf')
    min_window_start = 0

    for right, char in enumerate(s):
        have[char] = have.get(char, 0) + 1
        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:    # valid window — try to shrink
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_start = left

            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return s[min_window_start : min_window_start + min_len] if min_len != float('inf') else ''
```

**[DEMO: `min_window('ADOBECODEBANC', 'ABC')` — trace key steps:]**

```text
t='ABC', need={'A':1,'B':1,'C':1}, required=3

Expand until formed=3:
  right=0(A): have={'A':1}, formed=1 (A satisfied)
  right=1(D): no change
  right=2(O): no change
  right=3(B): have={'B':1}, formed=2
  right=4(E): no change
  right=5(C): have={'C':1}, formed=3 → window 'ADOBEC', len=6

Shrink from left:
  left=0(A): have['A']=0 < need['A']=1 → formed=2, left=1 → stop
  Record minimum: 'ADOBEC', len=6

Continue expanding:
  right=9(A): have={'A':1}, formed=3 → window 'DOBECODEBA'...
  Shrink: left advances past D,O,B,E,C → eventually window='BANC', len=4

Final result: 'BANC' ✓
```

[PAUSE]

**Why `formed` and `required`?** They track how many distinct character requirements are currently satisfied. When `formed == required`, the window is valid. This avoids comparing `have` to `need` on every step."

---

## [19:00 – 23:00] Part 4 — Longest Palindromic Substring

**[SHOW SLIDE: "Longest Palindromic Substring — LeetCode #5"]**

"A palindrome reads the same forwards and backwards. To find the longest palindromic substring, expand around each possible center.

Every palindrome has a center: either a single character (odd-length) or a gap between two equal characters (even-length). Try all n + (n-1) centers.

```python
def longest_palindrome(s):
    \"\"\"
    Return the longest palindromic substring.
    Expand-around-center: O(n²) time, O(1) space.
    \"\"\"
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]    # slice after expanding past the palindrome

    result = ''
    for i in range(len(s)):
        odd  = expand(i, i)        # odd-length center
        even = expand(i, i+1)      # even-length center
        if len(odd)  > len(result): result = odd
        if len(even) > len(result): result = even
    return result
```

**[DEMO: `longest_palindrome('babad')` — trace centers:]**

```text
i=0: odd=expand(0,0): s[0]='b', expand left=0,right=0 → 'b'
         even=expand(0,1): s[0]='b'≠s[1]='a' → ''
i=1: odd=expand(1,1): s[1]='a', expand: s[0]='b'≠s[2]='b'? No: s[0]='b',s[2]='b' equal!
         left=-1,right=3 → exit. palindrome='bab', result='bab'
         even=expand(1,2): s[1]='a'≠s[2]='b' → ''
i=2: odd=expand(2,2): s[2]='b', expand: s[1]='a',s[3]='a' equal. left=0,right=4.
         s[0]='b',s[4]='d' — not equal. palindrome=s[1:4]='aba', len=3
i=3: odd='a', even: s[3]='a'≠s[4]='d' → ''
i=4: odd='d'

Result: 'bab' (length 3) ✓ — 'aba' is also valid
```

Note the slice `s[left+1 : right]` after the while loop: `left` and `right` overshot by one in each direction when the loop ended, so we add one to left and use right as-is (Python slicing is exclusive on the right).

The Module 15 lab covers Trie implementation, Longest Substring Without Repeating Characters, Minimum Window Substring, and Longest Palindromic Substring. Good luck."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 15 — String Algorithms & Trie]**

---

## Additional Resources

- [NeetCode — Sliding Window Playlist](https://www.youtube.com/watch?v=GcW4mgmgSbw)
- [LeetCode #208 — Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [LeetCode #3 — Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [LeetCode #76 — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [LeetCode #5 — Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
