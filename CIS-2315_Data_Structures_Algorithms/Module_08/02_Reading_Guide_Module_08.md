# Reading Guide: Module 08 — Hash Tables & Hash Collisions

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
