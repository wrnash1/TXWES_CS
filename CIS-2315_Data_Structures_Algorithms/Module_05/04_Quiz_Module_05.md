# Quiz: Module 05 – Hash Tables and Hash Maps
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the average-case time complexity of lookup in a well-implemented hash table?
*   A) O(n)
*   B) O(log n)
*   C) O(n log n)
*   D) O(1)
*   **Correct Answer:** D) O(1)
*   **Distractor Analysis:**
    *   *Why correct:* A hash function maps the key directly to an index in one step; with a low load factor and good distribution, the chain or probe sequence at that index is near-constant length, giving O(1) average lookup.
    *   A is incorrect: O(n) is the worst case (all keys collide into one chain), not the average case.
    *   B is incorrect: O(log n) describes binary search trees, not hash tables.
    *   C is incorrect: O(n log n) is a sorting complexity, entirely unrelated to hash table lookup.

---

**Question 2**
Which of the following is the most accurate definition of **separate chaining** as a hash table collision resolution strategy?
*   A) When a collision occurs, the algorithm scans forward through the array one slot at a time until it finds an empty position, keeping all data in the main array for better cache locality.
*   B) When a collision occurs, the table is immediately doubled in size and all existing keys are rehashed into the new larger array to restore a low load factor.
*   C) When a collision occurs, both keys are stored at the same index by appending them to a linked list (or other collection) at that slot, so lookup scans the list at the target index.
*   D) When a collision occurs, the second key is assigned to a secondary hash table computed using a different hash function, and lookups check both tables.
*   **Correct Answer:** C) When a collision occurs, both keys are stored at the same index by appending them to a linked list (or other collection) at that slot, so lookup scans the list at the target index.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes open addressing with linear probing, not separate chaining.
    *   *Why B is incorrect:* That describes rehashing/resizing, which is a load factor management strategy, not a collision resolution method.
    *   *Why C is correct:* Separate chaining keeps a list at each bucket; all keys with the same hash go into the same list. Average lookup is O(1) when chains are short.
    *   *Why D is incorrect:* That describes cuckoo hashing or a two-table scheme — a more advanced variant, not the standard definition of separate chaining.

---

**Question 3**
You are given an array of integers and a target sum. You need to find whether any two elements add up to the target. Which approach gives O(n) time and O(n) space?
*   A) Sort the array and use binary search to find the complement of each element.
*   B) Use nested loops to check every pair of elements.
*   C) Store each element in a hash set as you iterate; for each element, check whether its complement (target – element) already exists in the set.
*   D) Use a stack to push elements and pop pairs that sum to the target.
*   **Correct Answer:** C) Store each element in a hash set as you iterate; for each element, check whether its complement (target – element) already exists in the set.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Sorting is O(n log n); binary search per element adds another O(n log n). This gives O(n log n) time, not O(n).
    *   *Why B is incorrect:* Nested loops check all O(n²) pairs — correct but does not meet the O(n) time requirement.
    *   *Why C is correct:* Each element is inserted and looked up once in O(1) average time, giving O(n) total. The hash set stores seen values, so the complement check is O(1).
    *   *Why D is incorrect:* A stack's LIFO order does not help identify complement pairs; this approach would not work correctly for the general case.

---

**Question 4**
What happens to hash table performance when the load factor becomes very high (approaching 1.0)?
*   A) Performance improves because fewer memory allocations are needed.
*   B) Performance degrades because chains become longer (chaining) or probe sequences grow (open addressing), increasing average lookup time toward O(n).
*   C) Performance remains O(1) regardless of load factor because the hash function is deterministic.
*   D) The hash table automatically switches to a binary search tree to maintain O(log n) performance.
*   **Correct Answer:** B) Performance degrades because chains become longer (chaining) or probe sequences grow (open addressing), increasing average lookup time toward O(n).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* High load factor means more collisions, which hurts performance; fewer allocations do not compensate.
    *   *Why B is correct:* With load factor near 1, the expected chain length (chaining) or probe length (open addressing) grows, degrading O(1) average toward O(n) worst case. This is why tables resize at ~0.75 load.
    *   *Why C is incorrect:* A deterministic hash function distributes keys uniformly but cannot prevent long chains when the table is nearly full.
    *   *Why D is incorrect:* Hash tables do not automatically convert to BSTs; they rehash into a larger array.

---

**Question 5**
In Python, which of the following can be used as a dictionary key?
*   A) A list such as `[1, 2, 3]`
*   B) A tuple such as `(1, 2, 3)`
*   C) A set such as `{1, 2, 3}`
*   D) A dictionary such as `{"a": 1}`
*   **Correct Answer:** B) A tuple such as `(1, 2, 3)`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Lists are mutable and unhashable in Python; using one as a dict key raises a `TypeError`. Mutability makes hashing unreliable since the hash could change.
    *   *Why B is correct:* Tuples are immutable and therefore hashable. `hash((1, 2, 3))` returns a consistent integer, making tuples valid dict keys — a common pattern in DSA solutions (e.g., grouping anagrams by `tuple(sorted(word))`).
    *   *Why C is incorrect:* Python sets are mutable and unhashable. `frozenset` is the immutable, hashable alternative.
    *   *Why D is incorrect:* Dicts are mutable and unhashable; they cannot be used as keys in another dict.
