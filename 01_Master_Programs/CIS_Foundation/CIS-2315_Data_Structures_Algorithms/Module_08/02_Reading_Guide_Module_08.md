# Reading Guide: Module 08 — Hash Tables & Hash Collisions

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

A hash table maps keys to values in O(1) average time for insert, lookup, and delete. It achieves this by using a hash function to compute an array index from the key, then storing the value at that index. Python's `dict` and `set` are both hash tables. Understanding the hash function, collision resolution strategies, and load factor makes you a more effective programmer and prepares you to answer interview questions about how dictionaries work under the hood.

---

## 1. Hash Table Structure

### Hash Function

A hash function takes a key and returns an integer index:

```python
index = hash(key) % table_size
```

Python's built-in `hash()` returns a large integer. The modulo operation maps it to a valid array index. A good hash function is:

- **Deterministic:** the same key always produces the same index.
- **Uniform:** keys spread evenly across buckets to minimize collisions.

### Load Factor

The load factor measures how full the hash table is:

```text
load_factor = number_of_keys / table_size
```

When the load factor exceeds a threshold (Python's `dict` uses 2/3), the table is **resized** — typically doubled — and all existing keys are **rehashed** into the new table. Resize is O(n), but it happens rarely enough that n insertions cost O(n) amortized — O(1) each.

---

## 2. Collision Resolution

A **collision** occurs when two different keys hash to the same index. Two main strategies handle this.

### Chaining

Each bucket holds a list of all key-value pairs that hash to that index:

```python
class HashTableChaining:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, val):
        idx = self._index(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                pair[1] = val
                return
        self.buckets[idx].append([key, val])

    def get(self, key):
        idx = self._index(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return pair[1]
        return None
```

Average case with load factor ≤ 0.7: O(1). Worst case (all keys in one bucket): O(n).

### Open Addressing (Linear Probing)

All key-value pairs are stored directly in the array. On a collision, probe the next slot: `(h + 1) % size`, `(h + 2) % size`, etc.

```python
class HashTableLinearProbe:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size

    def put(self, key, val):
        idx = hash(key) % self.size
        while self.table[idx] is not None and self.table[idx][0] != key:
            idx = (idx + 1) % self.size
        self.table[idx] = (key, val)

    def get(self, key):
        idx = hash(key) % self.size
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
        return None
```

**Clustering:** consecutive occupied slots form clusters that slow future probes. Quadratic probing `(h + i²) % size` reduces clustering. Python's `dict` uses a perturbation-based probing sequence.

---

## 3. Python `dict` and `set`

Python's built-in `dict` is a hash table. All of the following operations are O(1) average:

```python
d = {}
d['key'] = 'value'      # insert or update
val = d['key']          # lookup — KeyError if absent
val = d.get('key', 0)   # lookup with default — never raises
del d['key']            # delete
'key' in d              # membership test
```

Python's `set` is a hash table of keys with no values:

```python
s = set()
s.add(3)         # O(1)
3 in s           # O(1) — much faster than list's O(n)
s.remove(3)      # O(1) — KeyError if absent
s.discard(99)    # O(1) — no error if absent
```

---

## 4. Key Interview Patterns

### Two Sum (LeetCode #1)

Return indices of two numbers that sum to a target. Hash map solution: O(n) time, O(n) space.

```python
def two_sum(nums, target):
    seen = {}         # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Why O(n)?** Each element is processed once. The `in seen` check is O(1). Total: one pass = O(n).

### Contains Duplicate (LeetCode #217)

Return True if any value appears at least twice.

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Group Anagrams (LeetCode #49)

Group strings that are anagrams of each other. Two strings are anagrams iff their sorted forms are equal.

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

Time: O(n · k log k) where k is max string length (sort cost dominates). Space: O(n · k).

### Valid Anagram (LeetCode #242)

Return True if `t` is an anagram of `s`.

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

### Longest Consecutive Sequence (LeetCode #128)

Find the length of the longest consecutive integer sequence. Convert to a set, then for each number that is a sequence start (no `n-1` in set), count the run.

```python
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 not in num_set:    # start of a sequence
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)
    return best
```

Time: O(n) — each number is visited at most twice (once as a start check, once as a sequence element).

---

## 5. `collections` Utilities

### `defaultdict`

Avoids `KeyError` by providing a default factory for missing keys:

```python
from collections import defaultdict

# defaultdict(list): missing keys → empty list
graph = defaultdict(list)
graph['A'].append('B')    # works even if 'A' was not in graph

# defaultdict(int): missing keys → 0
freq = defaultdict(int)
for ch in 'aabbccc':
    freq[ch] += 1
```

### `Counter`

Specialized hash map for counting. Missing keys return 0, not KeyError:

```python
from collections import Counter

freq = Counter('aabbccca')
print(freq['a'])          # 3
print(freq['z'])          # 0 — no KeyError
print(freq.most_common(2))  # [('a', 3), ('c', 3)]

# Arithmetic on Counters:
c1 = Counter('aab')
c2 = Counter('abb')
print(c1 + c2)    # Counter({'b': 3, 'a': 3})
print(c1 - c2)    # Counter({'a': 1})
```

---

## 6. Complexity Summary

| Operation | Average | Worst Case | Notes |
|---|---|---|---|
| `dict` get / set / del | O(1) | O(n) | n = all keys in one bucket |
| `set` add / in / remove | O(1) | O(n) | same as dict |
| `dict` construction | O(n) | O(n) | |
| `Counter(s)` | O(n) | O(n) | n = len(s) |
| Sorted key hash | O(k log k) | O(k log k) | k = key length |
| Resize (rehash) | O(n) amortized | O(n) | doubles table, rare |

---

## 7. Interview Exam Tips

1. **`dict` lookup is O(1) average, not guaranteed O(1)** — the worst case is O(n), but mention this only if the interviewer probes it. For practical purposes, treat dict operations as O(1).

2. **Use `d.get(key, default)` instead of `d[key]`** — avoids KeyError when a key might be absent. This is the idiomatic Python pattern for optional lookups.

3. **Use `set` for O(1) membership tests** — `x in some_list` is O(n); `x in some_set` is O(1). Converting a list to a set before repeated lookups is a common O(n²) → O(n) optimization.

4. **Two Sum is the template for complement lookup** — any problem of the form "find two elements with property X" likely benefits from a hash map storing one element while searching for its complement.

5. **Anagram key = sorted string** — `tuple(sorted(s))` is a hashable, canonical form for any string. This key equals the key of any anagram of `s`.

6. **`Counter` subtraction drops zero and negative counts** — `Counter('ab') - Counter('aab')` gives `Counter({'b': ... no 'a'})`. Understand this for difference problems.

7. **`defaultdict` vs `dict.setdefault`** — both avoid KeyError, but `defaultdict` is cleaner for multi-value grouping. `d.setdefault(key, []).append(val)` is equivalent to `defaultdict(list); d[key].append(val)`.

8. **Hash table keys must be hashable** — Python requires dict/set keys to be immutable: `int`, `str`, `tuple` are hashable; `list`, `dict`, `set` are not. Use `tuple(sorted(s))` as a list-based key.

---

## 9. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — Hash Table Visualizations** — [https://visualgo.net/en/hashtable](https://visualgo.net/en/hashtable)
   Step-by-step animations of hash table insertion with both separate chaining and open addressing (linear probing). Visualizes collisions, bucket growth, and table resize operations.

2. **OpenDSA — Hash Tables Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/HashIntro.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/HashIntro.html)
   Free interactive OER textbook covering hash functions, collision resolution (chaining, probing), load factor analysis, and the mathematical proof of O(1) average performance.

3. **Python `collections` Module Documentation** — [https://docs.python.org/3/library/collections.html](https://docs.python.org/3/library/collections.html)
   Official Python documentation for `Counter`, `defaultdict`, `OrderedDict`, and `namedtuple`. Includes code examples for all common usage patterns relevant to hash map interview problems.

4. **NeetCode — Arrays & Hashing Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)
   Free video solutions for the most common hash table interview problems including Two Sum, Group Anagrams, Valid Anagram, Contains Duplicate, and Longest Consecutive Sequence — each with clear time and space complexity discussion.

5. **CS50 — Hash Tables Short (Harvard)** — [https://cs50.harvard.edu/x/2024/shorts/hash_tables/](https://cs50.harvard.edu/x/2024/shorts/hash_tables/)
   5-minute Harvard CS50 video introducing hash tables, hash functions, and separate chaining with clear visual diagrams. An excellent supplement for students wanting a second explanation before the lab.

---

## 8. Study Checklist

- [ ] Watch the Module 08 video lecture by Professor Nash.
- [ ] Implement `HashTableChaining` from scratch with `put` and `get`.
- [ ] Implement `HashTableLinearProbe` from scratch with `put` and `get`.
- [ ] Solve LeetCode #1 (Two Sum) using a hash map — O(n).
- [ ] Solve LeetCode #217 (Contains Duplicate) using a set.
- [ ] Solve LeetCode #49 (Group Anagrams) using sorted key.
- [ ] Solve LeetCode #128 (Longest Consecutive Sequence) using a set.
- [ ] Practice `Counter` and `defaultdict` from `collections`.
- [ ] Complete the Module 08 Lab.
- [ ] Complete the Module 08 Quiz.
