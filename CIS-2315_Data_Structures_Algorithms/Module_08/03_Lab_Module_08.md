# Lab Activity: Module 08 — Hash Tables & Hash Collisions

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement a hash table from scratch using chaining and linear probing
- **Part 2** — Use Python's `dict` and `set` for the Two Sum and anagram patterns
- **Part 3** — LeetCode interview patterns: Contains Duplicate, Group Anagrams, Longest Consecutive Sequence

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Hash Table from Scratch

**File:** `lab08_hashtable.py`

### 1.1 — Chaining Implementation

```python
class HashTableChaining:
    """
    Hash table using separate chaining for collision resolution.
    Each bucket holds a list of [key, value] pairs.
    """
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _index(self, key):
        return hash(key) % self.size

    def put(self, key, val):
        """Insert or update key → val. Time: O(1) average."""
        idx = self._index(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                pair[1] = val    # update existing
                return
        self.buckets[idx].append([key, val])

    def get(self, key):
        """Return value for key, or None if absent. Time: O(1) average."""
        idx = self._index(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        """Remove key if present. Time: O(1) average."""
        idx = self._index(key)
        self.buckets[idx] = [p for p in self.buckets[idx] if p[0] != key]
```

Test:

```python
ht = HashTableChaining()
ht.put('apple', 1)
ht.put('banana', 2)
ht.put('cherry', 3)
ht.put('apple', 99)    # update existing key

print(ht.get('apple'))   # 99 — updated
print(ht.get('banana'))  # 2
print(ht.get('missing')) # None

ht.remove('banana')
print(ht.get('banana'))  # None — removed
```

**Checkpoint:** All outputs match expected values. `put` overwrites an existing key; `get` returns `None` for absent keys.

---

### 1.2 — Inspect Bucket Distribution

```python
def show_buckets(ht):
    """Print each bucket to visualize collisions."""
    for i, bucket in enumerate(ht.buckets):
        if bucket:
            print(f'  Bucket {i}: {bucket}')

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
ht2 = HashTableChaining()
for w in words:
    ht2.put(w, len(w))

show_buckets(ht2)
# Observe: some buckets have 0, 1, or 2 entries depending on hash collisions
```

**Checkpoint:** Most buckets have 0 or 1 entries. If two words land in the same bucket, that is a collision handled by chaining.

---

### 1.3 — Linear Probing Implementation

```python
_DELETED = object()   # sentinel for deleted slots

class HashTableLinearProbe:
    """
    Hash table using open addressing (linear probing).
    Deleted slots marked with _DELETED sentinel to maintain probe chains.
    """
    def __init__(self, size=16):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _probe(self, key):
        """Return index of key or first empty/deleted slot."""
        idx = hash(key) % self.size
        first_deleted = None
        for _ in range(self.size):
            entry = self.table[idx]
            if entry is None:
                return first_deleted if first_deleted is not None else idx
            if entry is _DELETED:
                if first_deleted is None:
                    first_deleted = idx
            elif entry[0] == key:
                return idx
            idx = (idx + 1) % self.size
        return first_deleted

    def put(self, key, val):
        idx = self._probe(key)
        if self.table[idx] is None or self.table[idx] is _DELETED:
            self.count += 1
        self.table[idx] = (key, val)

    def get(self, key):
        idx = hash(key) % self.size
        for _ in range(self.size):
            entry = self.table[idx]
            if entry is None:
                return None
            if entry is not _DELETED and entry[0] == key:
                return entry[1]
            idx = (idx + 1) % self.size
        return None

    def remove(self, key):
        idx = hash(key) % self.size
        for _ in range(self.size):
            entry = self.table[idx]
            if entry is None:
                return
            if entry is not _DELETED and entry[0] == key:
                self.table[idx] = _DELETED
                self.count -= 1
                return
            idx = (idx + 1) % self.size
```

Test:

```python
lp = HashTableLinearProbe()
lp.put('x', 10)
lp.put('y', 20)
lp.put('z', 30)

print(lp.get('x'))   # 10
print(lp.get('y'))   # 20

lp.remove('y')
print(lp.get('y'))   # None — removed
print(lp.get('z'))   # 30 — probe chain still works past _DELETED slot
```

**Checkpoint:** Values are retrieved correctly. After `remove('y')`, `get('z')` still works because the `_DELETED` sentinel preserves the probe chain.

---

## Part 2 — Python Dict and Set Patterns

**File:** `lab08_patterns.py`

### 2.1 — Two Sum (LeetCode #1)

```python
def two_sum(nums, target):
    """
    Return indices [i, j] such that nums[i] + nums[j] == target.
    Time: O(n), Space: O(n)
    """
    seen = {}    # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

Test:

```python
print(two_sum([2, 7, 11, 15], 9))          # [0, 1]
print(two_sum([3, 2, 4], 6))               # [1, 2]
print(two_sum([3, 3], 6))                  # [0, 1]
```

Trace `two_sum([2, 7, 11, 15], 9)`:

```text
i=0, num=2,  complement=7,  7 not in seen → seen={2:0}
i=1, num=7,  complement=2,  2 in seen → return [0, 1]  ✓
```

**Checkpoint:** All three tests pass. Submit to LeetCode #1.

---

### 2.2 — Contains Duplicate (LeetCode #217)

```python
def contains_duplicate(nums):
    """
    Return True if any value appears at least twice.
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

Test:

```python
print(contains_duplicate([1, 2, 3, 1]))    # True
print(contains_duplicate([1, 2, 3, 4]))    # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
```

**Checkpoint:** All three tests pass.

---

### 2.3 — Valid Anagram (LeetCode #242)

```python
from collections import Counter

def is_anagram(s, t):
    """
    Return True if t is an anagram of s.
    Time: O(n), Space: O(1) — at most 26 distinct characters
    """
    return Counter(s) == Counter(t)
```

Test:

```python
print(is_anagram('anagram', 'nagaram'))   # True
print(is_anagram('rat', 'car'))           # False
print(is_anagram('listen', 'silent'))     # True
```

**Checkpoint:** All three tests pass.

---

## Part 3 — Advanced Patterns

**File:** (add to `lab08_patterns.py`)

### 3.1 — Group Anagrams (LeetCode #49)

```python
from collections import defaultdict

def group_anagrams(strs):
    """
    Group strings that are anagrams of each other.
    Key: sorted tuple of characters (canonical anagram form).
    Time: O(n * k log k), Space: O(n * k)
    """
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

Test:

```python
result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
# Each inner list is a group — order within groups may vary
for group in sorted(result, key=lambda g: sorted(g)[0]):
    print(sorted(group))

# Expected (in some order):
# ['ate', 'eat', 'tea']
# ['bat']
# ['nat', 'tan']
```

**Checkpoint:** Three groups produced. `'eat'`, `'tea'`, `'ate'` are in the same group. Submit to LeetCode #49.

---

### 3.2 — Longest Consecutive Sequence (LeetCode #128)

```python
def longest_consecutive(nums):
    """
    Find the length of the longest sequence of consecutive integers.
    Time: O(n) — each number visited at most twice.
    Space: O(n)
    """
    num_set = set(nums)
    best = 0

    for n in num_set:
        if n - 1 not in num_set:    # only start sequences from their beginning
            length = 1
            while n + length in num_set:
                length += 1
            best = max(best, length)

    return best
```

Test:

```python
print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4 → [1, 2, 3, 4]
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 → [0..8]
```

**Why O(n)?** For each number `n` where `n-1 ∉ set`, we walk forward through the sequence. Each element in `num_set` is visited at most once as a sequence continuation, so the total work across all inner `while` loops is O(n).

**Checkpoint:** Both tests pass. Submit to LeetCode #128.

---

### 3.3 — Integration Test

```python
def test_all():
    # Chaining hash table
    ht = HashTableChaining()
    ht.put('a', 1)
    ht.put('b', 2)
    assert ht.get('a') == 1
    assert ht.get('b') == 2
    assert ht.get('c') is None
    ht.put('a', 99)
    assert ht.get('a') == 99

    # Two Sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Contains Duplicate
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([1, 2, 3, 4]) == False

    # Valid Anagram
    assert is_anagram('anagram', 'nagaram') == True
    assert is_anagram('rat', 'car') == False

    # Longest Consecutive
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass. LeetCode #1, #217, #242, #49, #128 submitted.

---

## Deliverables

Submit to Canvas:

1. `lab08_hashtable.py` — chaining and linear probing implementations with bucket inspection
2. `lab08_patterns.py` — Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams, Longest Consecutive, integration test
3. LeetCode submission screenshots for #1, #49, and #128

---

## Summary

| Concept | Key Point |
|---|---|
| Hash function | Maps key → array index using `hash(key) % size` |
| Collision | Two keys map to same index — resolved by chaining or probing |
| Chaining | Each bucket holds a list; O(1) average, O(n) worst |
| Linear probing | Probe next slot; `_DELETED` sentinel preserves chains |
| Load factor | n / size; resize when > threshold to keep O(1) average |
| Two Sum | Store complement in dict; one-pass O(n) |
| Group Anagrams | Sorted tuple as canonical key |
| Longest Consecutive | Set membership; only start from sequence beginning |
| `defaultdict` | Missing keys return default value, not KeyError |
| `Counter` | Frequency map; missing keys return 0 |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Design a Hash Map from Scratch (LeetCode #706)

Implement `MyHashMap` with `put(key, value)`, `get(key)`, and `remove(key)` without using Python's built-in `dict`. Use separate chaining with a fixed array of 1024 buckets and a simple hash function `key % 1024`. Handle collisions by storing `(key, value)` pairs in a list at each bucket. Verify it passes LeetCode #706. Then modify your implementation to support dynamic resizing: when `load_factor > 0.75`, double the bucket array and rehash all entries. Add a test that inserts 2,000 entries and confirms `get` still returns correct values after the resize.

### 9.2 — Subarray Sum Equals K (LeetCode #560)

Given an array of integers `nums` and a target `k`, return the number of contiguous subarrays that sum to `k`. The naive O(n²) approach tries all (i,j) pairs. The optimal O(n) approach uses a prefix-sum hash map: maintain a running prefix sum and count how many times `prefix_sum - k` has appeared (using `defaultdict(int)` initialized with `{0: 1}`). Implement both approaches, verify they produce the same answers on several test cases, and explain in a comment why the prefix-sum + hash map approach is O(n) rather than O(n²).

### 9.3 — LFU Cache (LeetCode #460)

Implement a Least Frequently Used (LFU) cache: `get(key)` and `put(key, value)` both O(1). The LFU cache evicts the least frequently accessed item; ties are broken by LRU order (evict the least recently used among those with minimum frequency). The solution requires three hash maps: `key_map` (key → value, frequency), `freq_map` (frequency → ordered dict of keys), and tracking the `min_freq`. This is one of the most difficult hash table problems on LeetCode. Implement it, verify correctness on the LeetCode test cases, and write a detailed comment explaining the role of each hash map and why ordered dicts (`collections.OrderedDict`) are used in `freq_map`.
