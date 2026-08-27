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

---

### Question 11

**Each question is worth 5 points.**

What is the load factor of a hash table, and why is a high load factor detrimental to performance?

- A) Load factor = number of collisions / table size; high values mean more keys per bucket on average
- B) Load factor = number of entries / table size; a high load factor increases the average collision probability, degrading O(1) average lookups toward O(n)
- C) Load factor = table size / number of entries; high values mean the table is mostly empty
- D) Load factor = maximum bucket size; a high value means one bucket holds all entries

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Load factor is defined as the ratio of entries to table size, not collisions to table size. The number of collisions is a consequence of load factor but not its definition.
- *Why B is correct:* Load factor α = n/m where n = number of entries and m = table size (number of buckets). When α is close to 1 (or exceeds 1 for separate chaining), the average bucket length grows, making lookups degrade from O(1) toward O(n). For example, with α = 1, the expected number of comparisons per lookup approaches 2 (for chaining). Dynamic resize (typically at α = 0.75) keeps α bounded and preserves O(1) average.
- *Why C is incorrect:* This is the reciprocal of the load factor. A high value of m/n would mean many empty buckets — low collisions. The actual load factor n/m is what's typically discussed.
- *Why D is incorrect:* Maximum bucket size is not the load factor. Maximum bucket size is a separate concern related to worst-case hash collision clusters.

---

### Question 12

In the Longest Consecutive Sequence problem (LeetCode #128), why must you only start counting from elements where `x - 1` is NOT in the set?

- A) To avoid counting duplicate values multiple times
- B) To ensure each sequence is counted only from its smallest element, preventing O(n²) redundant counting
- C) To skip even numbers in the sequence
- D) Because the set does not support membership tests for negative numbers

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Duplicates are handled by building a set (which removes duplicates automatically). The `x - 1` check is not about deduplication.
- *Why B is correct:* If you start counting from every element, you repeatedly count the same sequences from each element within them. For example, sequence `[1, 2, 3, 4, 5]` would be counted 5 times — starting from 1, 2, 3, 4, and 5. The `x - 1 not in set` check ensures you only start counting from the minimum element of each sequence (the one with no predecessor). Each sequence is then counted exactly once, making the total work O(n) across all sequences.
- *Why C is incorrect:* The check `x - 1 not in set` applies to all elements regardless of parity. There is no filtering by even or odd.
- *Why D is incorrect:* Python's `set` supports membership tests for any hashable value including negative integers. `(-1) in {-1, 0, 1}` returns `True` without issue.

---

### Question 13

What Python expression converts a string `s` into a canonical hashable key such that all anagrams of `s` produce the same key?

- A) `hash(s)`
- B) `frozenset(s)`
- C) `tuple(sorted(s))`
- D) `s.lower()`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `hash(s)` returns a single integer. Different strings with different character orderings (including anagrams) generally have different hash values. `hash("abc")` ≠ `hash("bca")`.
- *Why B is incorrect:* `frozenset(s)` creates a set of unique characters, discarding duplicate counts. `frozenset("aab")` = `frozenset("ab")` = `{'a','b'}`. This loses count information, causing non-anagrams with the same character set to be grouped together (e.g., "a" and "aa" would incorrectly share a key).
- *Why C is correct:* `tuple(sorted(s))` sorts the characters alphabetically and creates a tuple. Any anagram of `s` has the same characters in the same sorted order, producing identical tuples. Tuples are hashable and can be used as dictionary keys. For example: `tuple(sorted("eat"))` = `('a','e','t')` = `tuple(sorted("ate"))` = `tuple(sorted("tea"))`.
- *Why D is incorrect:* `s.lower()` only changes case; it does not sort characters or group anagrams. "eat" and "tea" both become "eat" and "tea" (lowercased), which are still different strings.

---

### Question 14

Given `d = {"a": 1, "b": 2, "c": 3}`, what does `d.get("x", 0)` return?

- A) Raises `KeyError` because "x" is not in `d`
- B) Returns `None` because "x" is not in `d`
- C) Returns `0` — the default value specified as the second argument
- D) Returns `"x"` — the key that was queried

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `d["x"]` raises `KeyError` for a missing key, but `d.get("x", 0)` is specifically designed to avoid `KeyError`. It returns the default value instead.
- *Why B is incorrect:* `d.get("x")` with no default argument returns `None` for a missing key. But `d.get("x", 0)` specifies `0` as the default, so `None` is not returned.
- *Why C is correct:* `dict.get(key, default)` returns `dict[key]` if `key` exists, otherwise returns `default`. Since "x" is not in `d`, `d.get("x", 0)` returns `0`. This is the standard idiom for safe dictionary lookups in Python.
- *Why D is incorrect:* `dict.get` returns the value associated with the key (or the default), never the key itself.

---

### Question 15

In Python's `Counter`, what does `Counter("aab") - Counter("ab")` return?

- A) `Counter({'a': 0, 'b': 0})` — all counts subtracted to zero
- B) `Counter({'a': 1})` — only positive result counts are kept
- C) `Counter({'a': -1, 'b': -1})` — negative counts allowed
- D) `Counter({'b': -1})` — 'a' cancels out, 'b' goes negative

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Counter subtraction drops keys with zero counts. `Counter("aab") - Counter("ab")` would give `Counter({'a': 2-1=1, 'b': 1-1=0})`. The zero count for 'b' is dropped, leaving only `Counter({'a': 1})`.
- *Why B is correct:* `Counter("aab")` = `{'a':2, 'b':1}`. `Counter("ab")` = `{'a':1, 'b':1}`. Subtraction: 'a': 2−1=1 (kept), 'b': 1−1=0 (dropped because non-positive). Result: `Counter({'a': 1})`. Counter subtraction drops all elements with zero or negative counts.
- *Why C is incorrect:* Counter subtraction does not produce negative counts. Results with zero or negative counts are dropped entirely. For `Counter("a") - Counter("aab")`, 'a' would give 1-2=-1 which is dropped, resulting in `Counter()`.
- *Why D is incorrect:* The calculation gives 'a': 2−1=1 (positive, kept) and 'b': 1−1=0 (non-positive, dropped). 'b' is dropped, not kept with value -1.

---

### Question 16

Which collision resolution strategy guarantees that no element is stored outside the original hash table array?

- A) Separate chaining — each bucket holds a linked list
- B) Open addressing (linear probing) — all elements are stored in the array itself
- C) Double hashing — uses two hash functions but still uses a secondary array
- D) Cuckoo hashing — moves elements between multiple separate arrays

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Separate chaining stores overflow elements in linked list nodes that are allocated outside the array. The array holds pointers to lists, but the list nodes themselves live on the heap — outside the original array.
- *Why B is correct:* Open addressing (including linear probing, quadratic probing, and double hashing) stores all elements directly in the hash table array itself. When a collision occurs, the algorithm probes successive slots in the same array until an empty slot is found. No auxiliary linked lists or secondary arrays are used.
- *Why C is incorrect:* Double hashing is a form of open addressing, so it does store all elements in the original array. But calling a "secondary array" is incorrect — double hashing uses a secondary hash function, not a secondary array.
- *Why D is incorrect:* Cuckoo hashing uses two separate hash tables (two arrays). Elements may be "kicked" between the tables. This does not store all elements in a single original array.

---

### Question 17

What happens when you attempt to use a Python `list` as a dictionary key?

- A) The list is automatically converted to a tuple and used as a key
- B) Python raises `TypeError: unhashable type: 'list'`
- C) Python uses the list's memory address as the hash value
- D) Python converts the list to a string representation and uses that as the key

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Python does not automatically convert unhashable types for use as keys. An explicit conversion (`tuple(my_list)`) is required.
- *Why B is correct:* Python dictionary keys must be hashable — they must implement `__hash__` and `__eq__` with consistent behavior. Python's `list` is mutable, and mutable objects are intentionally not hashable (because their hash value would change if the list were modified, breaking the hash table). Attempting to use a list as a key raises `TypeError: unhashable type: 'list'`.
- *Why C is incorrect:* Using the memory address (id) as a hash would make list equality by identity rather than by value, breaking expected behavior. Python's design choice is to make mutable containers non-hashable rather than hash by identity.
- *Why D is incorrect:* Python does not implicitly stringify objects for use as keys. The `str(my_list)` conversion must be done explicitly by the programmer.

---

### Question 18

The `is_anagram` function (LeetCode #242) using `Counter` has what time and space complexity?

- A) Time O(n log n), Space O(1)
- B) Time O(n), Space O(1)
- C) Time O(n), Space O(k) where k is the size of the character alphabet
- D) Time O(n²), Space O(n)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(n log n) is the complexity of the sort-based anagram check (`sorted(s) == sorted(t)`). The `Counter` approach iterates each string once — O(n).
- *Why B is incorrect:* O(1) space would require a fixed-size array (e.g., a 26-element array for lowercase English letters). `Counter` allocates space proportional to the number of distinct characters.
- *Why C is correct:* `Counter(s)` and `Counter(t)` each iterate n characters — O(n) time. The Counter objects store at most k distinct characters, where k is the alphabet size (e.g., k=26 for lowercase English, k=128 for ASCII). Space is O(k). Since k is a fixed constant for most problems (k ≤ 26), this is often stated as O(1) space in practice, but the technically correct answer acknowledges k.
- *Why D is incorrect:* O(n²) would require nested loops. `Counter` construction is a single linear pass — O(n) with no nesting.

---

### Question 19

What is the key insight that makes the Two Sum hash map solution O(n) instead of O(n²)?

- A) The hash map sorts the array, enabling binary search
- B) Each element is processed once; the complement is found in O(1) via hash map lookup instead of O(n) linear scan
- C) The hash map removes duplicates, reducing the effective input size
- D) The hash map enables parallel processing of array elements

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Hash maps do not sort data — they provide O(1) key-value lookup. Binary search would require sorting first (O(n log n)), which is a different approach entirely.
- *Why B is correct:* The brute-force O(n²) solution uses a nested loop: for each element at index i, scan all other elements to find `target - nums[i]`. The O(n) solution replaces the inner scan with a hash map lookup: store `nums[i] → i` in the map, then check if `target - nums[i]` is already in the map. The lookup is O(1) amortized. One pass, O(1) per element, O(n) total.
- *Why C is incorrect:* The Two Sum problem may have duplicate values, and duplicates are valid parts of the solution (e.g., [3, 3], target=6). The hash map does not remove duplicates.
- *Why D is incorrect:* Python is single-threaded. Hash maps provide O(1) lookup per element, not parallelism. The improvement is algorithmic — O(n) vs O(n²) — not due to parallel execution.

---

### Question 20

In separate chaining, what is the worst-case time complexity for a hash table lookup, and when does it occur?

- A) O(1) — hash tables are always constant time
- B) O(log n) — chains are kept sorted for binary search
- C) O(n) — when all n keys hash to the same bucket, forming a single chain of length n
- D) O(n log n) — when multiple buckets each hold a sorted sub-list

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(1) is the average case with a good hash function and bounded load factor. The worst case occurs when the hash function is poor or adversarial inputs cause all keys to collide.
- *Why B is incorrect:* Standard separate chaining uses unsorted linked lists per bucket. Sorted chains would enable O(log n) binary search, but standard hash table implementations do not sort chains — the overhead is not justified for expected O(1) performance.
- *Why C is correct:* If every key hashes to the same bucket index, all n entries are stored in a single chain. A lookup for any key requires scanning the entire chain — O(n) in the worst case. This is why a good hash function and bounded load factor are critical: they spread entries across buckets and bound the average chain length.
- *Why D is incorrect:* O(n log n) is not a standard hash table lookup complexity. The combination of multiple sorted sub-lists would add up to O(n log n) total construction cost, but individual lookups are O(log k) per bucket where k is the bucket size.
