# Quiz: Module 08 — Hash Tables & Hash Collisions

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the average-case time complexity of a lookup (`get`) operation in a well-implemented hash table?

- A) O(log n)
- B) O(n)
- C) O(1)
- D) O(n log n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(log n) is the lookup complexity for a balanced BST (e.g., Python's `sortedcontainers.SortedList`, Java's `TreeMap`). Hash tables achieve faster average lookups by computing the index directly rather than traversing a tree.
- *Why B is incorrect:* O(n) is the worst case for a hash table — it occurs when all keys hash to the same bucket (a pathological collision scenario). With a good hash function and load factor below the resize threshold, this almost never happens.
- *Why C is correct:* With a good hash function and bounded load factor, the average chain length (for chaining) or probe sequence length (for open addressing) is a small constant. Computing the hash and accessing the bucket is O(1), making lookup O(1) on average.
- *Why D is incorrect:* O(n log n) is typical of sorting algorithms and has no connection to hash table lookups. It would be a catastrophically slow lookup structure.

---

### Question 2

A hash table of size 8 receives a key whose `hash(key) % 8` equals 3. Another key also hashes to index 3. What is this situation called, and how does **chaining** handle it?

- A) Overflow — the table is resized immediately
- B) Collision — both keys are stored in a list at bucket 3
- C) Collision — the second key is discarded
- D) Overflow — the second key is hashed with a different function

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A collision at one bucket does not trigger a resize. Resize is triggered by load factor exceeding a threshold (typically 0.7). A single collision is expected and handled without resizing.
- *Why B is correct:* Chaining stores all key-value pairs that hash to the same bucket in a linked list (or Python list) at that index. Both keys coexist in bucket 3's list. Lookup scans the list at the bucket and compares keys until a match is found.
- *Why C is incorrect:* Discarding a key would break the hash table entirely — it would fail to store data. No valid collision strategy discards keys.
- *Why D is incorrect:* Double hashing (using a second hash function) is a form of open addressing, not chaining. Chaining keeps the secondary structure at the bucket, not a secondary hash.

---

### Question 3

In the linear probing implementation, deleted entries are marked with a `_DELETED` sentinel rather than simply setting the slot to `None`. Why is this necessary?

- A) `None` cannot be stored in a Python list
- B) Without the sentinel, a `None` slot during a probe would incorrectly terminate the search, causing lookups to miss keys that were inserted after the deleted slot
- C) The sentinel prevents the hash function from reusing the index
- D) Resizing requires sentinel values to count deleted slots accurately

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python lists can store `None` without any issue. The problem is not a storage limitation.
- *Why B is correct:* During a `get` probe, the algorithm stops when it finds a `None` slot, interpreting it as "this key was never inserted." If a previously occupied slot is simply set to `None` on deletion, a probe for a key inserted after the now-deleted slot will stop early at that `None` and return the wrong result. The `_DELETED` sentinel says "something was here, keep probing."
- *Why C is incorrect:* The hash function is deterministic and does not consult the table contents. The sentinel has no effect on hash computation.
- *Why D is incorrect:* While the count of deleted slots could be tracked for load-factor accounting, that is not the reason for the sentinel. The sentinel's purpose is correctness of probe chains during lookups.

---

### Question 4

What is the **load factor** of a hash table, and what happens when it exceeds the resize threshold?

- A) The ratio of collisions to insertions; the table is cleared and rebuilt from scratch
- B) The ratio of occupied buckets to total buckets; the table is sorted for faster lookups
- C) The ratio of stored keys to table size; the table is resized (typically doubled) and all keys are rehashed
- D) The ratio of chained entries to single entries; the table switches to open addressing

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Load factor measures fullness, not collisions specifically. And the table is not cleared — all existing data is preserved during a resize by rehashing each key into the new larger table.
- *Why B is incorrect:* Load factor is about the number of stored keys versus total capacity, not occupied-versus-total buckets (which would ignore chains). Sorting has no role — hash tables are not sorted structures.
- *Why C is correct:* `load_factor = n / table_size`. When this exceeds the threshold (Python uses 2/3), the table is doubled in size and every key is rehashed into a new position — because `hash(key) % new_size` produces a different index. This resize is O(n) but happens rarely enough that n total insertions cost O(n) amortized.
- *Why D is incorrect:* Load factor does not distinguish between chained and single entries. Python's dict uses open addressing throughout its lifetime — it does not switch strategies.

---

### Question 5

Which of the following correctly implements the Two Sum pattern for `nums = [2, 7, 11, 15]` and `target = 9`?

- A) Sort the array; use binary search for each complement — O(n log n)
- B) For every pair (i, j) with i ≠ j, check if `nums[i] + nums[j] == target` — O(n²)
- C) Store each number in a dict as you scan; for each `num`, check if `target - num` is already in the dict — O(n)
- D) Use a min-heap to always process the smallest element first — O(n log n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Sorting + binary search gives O(n log n), which is correct but not optimal. It also does not directly return the original indices, requiring index tracking. The hash map approach is O(n) and naturally preserves indices.
- *Why B is incorrect:* The nested loop approach is O(n²) — correct but brute force. For an array of 10,000 elements, this is 100,000,000 comparisons. The hash map reduces this to 10,000.
- *Why C is correct:* A single pass stores `{num: index}` in a dict. For each new number, `target - num` is the complement. Looking it up in the dict is O(1). Total time: O(n). This is the canonical interview answer.
- *Why D is incorrect:* A heap processes elements by value order, not by complement relationship. This approach does not leverage the problem's structure and requires O(n log n) just to build the heap.

---

### Question 6

Python's `collections.Counter` is used to count character frequencies. What does `Counter('aabbc')['z']` return?

- A) `None`
- B) `KeyError: 'z'`
- C) `0`
- D) `-1`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `None` is what `dict.get(key)` returns for a missing key with no default. `Counter` uses a different default — it returns `0` for any missing key, which is the natural identity element for counting.
- *Why B is incorrect:* A plain `dict['missing_key']` raises `KeyError`. `Counter` specifically overrides `__missing__` to return `0` instead of raising, making it safe to access any character without prior existence checks.
- *Why C is correct:* `Counter` is designed for counting, where a missing element has a count of 0. `Counter('aabbc')['z']` returns `0` because `'z'` never appeared in the input. This behavior makes frequency comparisons safe without needing `in` checks.
- *Why D is incorrect:* `-1` would suggest negative frequency, which has no meaning in counting. `Counter` subtraction (`c1 - c2`) drops results ≤ 0 from the output, but direct access to a missing key returns `0`.

---

### Question 7

Why does the Group Anagrams solution use `tuple(sorted(s))` as the dictionary key rather than `sorted(s)` directly?

- A) `sorted(s)` returns a string, which is not hashable
- B) `sorted(s)` returns a list, which is not hashable; `tuple(sorted(s))` creates a hashable key
- C) `tuple(sorted(s))` is faster to compute than `sorted(s)`
- D) Tuples preserve insertion order but lists do not

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `sorted(s)` does not return a string — it returns a list of characters. `''.join(sorted(s))` would return a string, which is hashable and would also work as a key.
- *Why B is correct:* Python dict keys must be hashable (immutable). `sorted(s)` returns a list, which is mutable and therefore not hashable — using it as a dict key would raise `TypeError: unhashable type: 'list'`. Converting to a tuple via `tuple(sorted(s))` creates an immutable, hashable object that can serve as a dict key.
- *Why C is incorrect:* `tuple(sorted(s))` has the same O(k log k) cost as `sorted(s)` plus a small O(k) tuple construction. It is not faster.
- *Why D is incorrect:* Both lists and tuples preserve insertion order in Python. The distinction is mutability and hashability, not ordering behavior.

---

### Question 8

The Longest Consecutive Sequence algorithm (LeetCode #128) only starts counting from numbers where `n - 1` is not in the set. Why is this check necessary for achieving O(n) time complexity?

- A) Numbers without a predecessor are always larger than numbers with one
- B) Without this check, the inner `while` loop would re-count the same sequences multiple times, degrading to O(n²)
- C) The check filters out duplicate values before building the set
- D) This check is not necessary — the algorithm works correctly without it, just slightly slower

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Whether a number has a predecessor has no relationship to its magnitude. The check is about avoiding redundant work, not about value ordering.
- *Why B is correct:* Without the `n - 1 not in num_set` guard, every number in every sequence would trigger a full `while` loop. For a sequence `[1, 2, 3, 4]`, each of 1, 2, 3, 4 would start counting, and the loops would collectively examine O(n) elements per starting point — O(n²) total. The guard ensures each sequence is counted exactly once from its true start.
- *Why C is incorrect:* Duplicates are already handled by converting `nums` to a `set` before the loop. The `n - 1` check serves a different purpose — preventing re-counting of sequences.
- *Why D is incorrect:* Without the guard, the algorithm is functionally correct but degrades to O(n²) time, which would time out on large inputs in LeetCode. The guard is essential for meeting the O(n) requirement.

---

### Question 9

Which of the following types can serve as a Python `dict` key?

- A) `list`
- B) `dict`
- C) `set`
- D) `tuple`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Lists are mutable. Python requires dict keys to be hashable (and therefore immutable). `hash([1, 2, 3])` raises `TypeError: unhashable type: 'list'`.
- *Why B is incorrect:* Dicts are mutable and not hashable. A dict cannot contain another dict as a key (though it can contain one as a value).
- *Why C is incorrect:* Sets are mutable and not hashable. `frozenset` is the immutable, hashable equivalent of `set` and can be used as a dict key.
- *Why D is correct:* Tuples are immutable. As long as all elements within the tuple are also hashable (e.g., `(1, 'a', (2, 3))`), the tuple is hashable and can serve as a dict key. This is why `tuple(sorted(s))` is used as the anagram key — it is hashable where a list is not.

---

### Question 10

`collections.defaultdict(list)` and a plain `dict` with `d.setdefault(key, [])` both avoid `KeyError` when accessing a new key. What is the primary practical advantage of `defaultdict(list)` for building a mapping of key → list of values?

- A) `defaultdict` is faster because it uses C extensions; plain `dict` is pure Python
- B) `defaultdict` automatically removes empty lists; `setdefault` does not
- C) `defaultdict` applies the default factory on every access; `d[key].append(val)` works cleanly without a prior existence check
- D) `setdefault` requires the key to already exist; `defaultdict` does not

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Both `defaultdict` and `dict` are implemented in C in CPython. The speed difference is negligible.
- *Why B is incorrect:* Neither `defaultdict` nor `setdefault` automatically removes empty lists. Empty-list cleanup would need to be done explicitly.
- *Why C is correct:* With `defaultdict(list)`, writing `d[key].append(val)` works for any key — the factory creates an empty list if the key is new. With a plain dict, you must write `d.setdefault(key, []).append(val)` or check `if key not in d: d[key] = []` before appending. `defaultdict` eliminates this boilerplate, making group-by patterns cleaner and less error-prone.
- *Why D is incorrect:* `d.setdefault(key, default)` works even if `key` is absent — it inserts `default` if the key is missing. The distinction is ergonomics and readability, not a correctness difference.
