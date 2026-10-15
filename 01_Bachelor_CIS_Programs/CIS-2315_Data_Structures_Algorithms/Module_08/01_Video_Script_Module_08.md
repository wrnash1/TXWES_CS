# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 08 — Hash Tables & Hash Collisions

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course &bull; Module 08</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=8hly31xKli0" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/8hly31xKli0" title="freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

This module covers hash tables — the most important data structure for interview problems. A hash table maps keys to values in O(1) average time for insert, lookup, and delete. Python's built-in `dict` and `set` are both hash tables. Understanding how they work under the hood — the hash function, collision resolution, and load factor — separates you from candidates who can use a dict but cannot explain it. This module also covers the top interview patterns that use hash tables: Two Sum, anagram grouping, and frequency counting.

---

## Part 1 — Hash Table Structure and Hash Functions

A hash table is an array of fixed size. To store a key-value pair, we apply a **hash function** to the key, which produces an integer index. We store the value at that index in the array.

For a table of size 8 and a key `'apple'`:

```python
index = hash('apple') % 8
```

The `hash()` built-in returns a large integer; the modulo operation maps it to a valid array index.

A good hash function has two properties:

1. **Deterministic:** the same key always produces the same index.
2. **Uniform:** keys distribute evenly across buckets to minimize collisions.

For integer keys: `hash(k) = k % table_size` is simple and often sufficient.

For string keys: Python uses a polynomial rolling hash — each character contributes to the hash value based on its position.

```python
# Simple polynomial hash (conceptual — not Python's actual implementation):
def simple_hash(s, size):
    h = 0
    for ch in s:
        h = (h * 31 + ord(ch)) % size
    return h
```

The constant 31 is a small prime chosen to spread character values across the output range.

**Why does the table need to be resized?**

If we insert too many keys into a fixed-size table, many buckets will have multiple entries — **collisions**. The ratio of stored keys to table size is the **load factor**:

```text
load_factor = n / table_size
```

When load factor exceeds a threshold (typically 0.7 for Python dicts), the table is resized — usually doubled — and all keys are **rehashed** into the new table. This resize is O(n), but it happens rarely enough that the amortized cost of n inserts remains O(n) total — O(1) per insert.

---

## Part 2 — Collision Resolution

**What is a collision?**

A collision occurs when two different keys hash to the same index. For example:

```python
hash('apple') % 8 == 3
hash('grape') % 8 == 3   # same bucket!
```

There are two main strategies to handle collisions.

### Strategy 1: Chaining

Each bucket holds a linked list (or Python list) of all key-value pairs that hash to that index.

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
                pair[1] = val    # update existing key
                return
        self.buckets[idx].append([key, val])

    def get(self, key):
        idx = self._index(key)
        for pair in self.buckets[idx]:
            if pair[0] == key:
                return pair[1]
        return None
```

**,['grape',2]]`]**

With chaining, the worst case is O(n) — if all n keys hash to the same bucket. But with a good hash function and load factor ≤ 0.7, the average chain length is a small constant, giving O(1) average.

### Strategy 2: Open Addressing (Linear Probing)

Instead of chaining, all key-value pairs are stored directly in the array. On a collision, we probe the next bucket: index `(h + 1) % size`, then `(h + 2) % size`, and so on, until we find an empty slot.

```python
class HashTableLinearProbe:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size

    def _probe(self, key):
        idx = hash(key) % self.size
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return idx     # found existing key
            idx = (idx + 1) % self.size
        return idx             # empty slot

    def put(self, key, val):
        idx = self._probe(key)
        self.table[idx] = (key, val)

    def get(self, key):
        idx = hash(key) % self.size
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
        return None
```

**Clustering problem:** consecutive occupied slots form clusters, making probes longer. Quadratic probing `(h + i²) % size` reduces clustering. Python's dict uses a more sophisticated pseudorandom probing scheme.

**Which does Python use?**

CPython's `dict` uses open addressing with a perturbation-based probing sequence (not simple linear probing). The load factor threshold is 2/3. When it exceeds this, the table is doubled and all keys are rehashed.

---

## Part 3 — Key Interview Patterns

**Pattern 1: Two Sum (LeetCode #1)**

Given a list of integers and a target, return the indices of two numbers that add to the target.

Brute force: O(n²) — for every pair.

Hash map approach: O(n) — as we scan, store each number and its index. For each `num`, check if `target - num` is already in the map.

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

**, 9)` — trace: seen={}, num=2, comp=7 not seen → seen={2:0}; num=7, comp=2 in seen → return [0,1]]**

The key insight: `complement in seen` is O(1) for a dict. This reduces the problem from O(n²) to O(n).

### Pattern 2: Contains Duplicate (LeetCode #217)

Return True if any value appears at least twice.

```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```

Or equivalently:

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

The set membership test `num in seen` is O(1) average.

### Pattern 3: Group Anagrams (LeetCode #49)

Given a list of strings, group all anagrams together. Two words are anagrams if they contain the same characters with the same frequencies.

Key insight: two strings are anagrams if and only if their sorted versions are equal. Use the sorted string as the hash key.

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))     # sorted string as dict key
        groups[key].append(s)
    return list(groups.values())
```

**` → `{('a','e','t'): ['eat','tea','ate'], ('a','n','t'): ['tan','nat'], ('a','b','t'): ['bat']}`]**

Time: O(n · k log k) where n is the number of strings and k is the maximum string length. The sort dominates.

### Pattern 4: Frequency Counting with `Counter`

Python's `collections.Counter` is a specialized hash map for counting.

```python
from collections import Counter

# Count character frequencies
freq = Counter('aabbccca')
print(freq)     # Counter({'a': 3, 'c': 3, 'b': 2})
print(freq['a'])  # 3
print(freq['z'])  # 0 — missing keys return 0, not KeyError

# Top-k elements
print(freq.most_common(2))  # [('a', 3), ('c', 3)]
```

**Anagram check using Counter:**

```python
def is_anagram(s, t):
    return Counter(s) == Counter(t)
```"

---

## Part 4 — `defaultdict`, `set`, and Complexity

`collections.defaultdict` avoids KeyError by providing a default factory for missing keys:

```python
from collections import defaultdict

graph = defaultdict(list)
graph['A'].append('B')    # no KeyError even though 'A' was not in graph
graph['A'].append('C')
print(graph['A'])         # ['B', 'C']
print(graph['X'])         # [] — empty list, not KeyError
```

`defaultdict(int)` initializes missing keys to 0 — perfect for frequency counting:

```python
freq = defaultdict(int)
for ch in 'aabbccc':
    freq[ch] += 1
print(freq)   # defaultdict(<class 'int'>, {'a': 2, 'b': 2, 'c': 3})
```

**`set` operations — all O(1) average:**

```python
s = {1, 2, 3, 4}
print(3 in s)        # True — O(1)
s.add(5)             # O(1)
s.remove(2)          # O(1)
s.discard(99)        # O(1) — no error if absent
```

Set intersection, union, difference: O(min(len(s1), len(s2))), O(len(s1) + len(s2)), O(len(s1)).

**Complexity Summary:**

```text
Operation          Average    Worst Case
─────────────────────────────────────────
dict get/set/del   O(1)       O(n)
set add/in/remove  O(1)       O(n)
dict construction  O(n)       O(n)
Counter(s)         O(n)       O(n)
sorted key hash    O(k log k) —
```

The worst case O(n) occurs with a pathological hash function that puts all keys in one bucket. With Python's built-in hash, this is rare enough to ignore for interviews. When someone asks for average complexity, say O(1) for individual hash map operations.

The Module 08 lab has you implement chaining and linear probing from scratch, practice Two Sum, Group Anagrams, and frequency counting with Counter and defaultdict. Good luck.

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 08 — Hash Tables & Hash Collisions]**

---

## Additional Resources

- [Python dict internals (Brandon Rhodes)](https://www.youtube.com/watch?v=C4gxoTaI71U)
- [LeetCode #1 — Two Sum](https://leetcode.com/problems/two-sum/)
- [LeetCode #49 — Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [LeetCode #217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [Python collections.Counter documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
