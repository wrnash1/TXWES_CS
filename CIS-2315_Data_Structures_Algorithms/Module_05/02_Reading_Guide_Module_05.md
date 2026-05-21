# Reading Guide: Module 05 – Hash Tables and Hash Maps
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 05 – Hash Tables and Hash Maps**! Hash tables are arguably the single most important data structure in coding interviews. They underpin solutions to Two Sum, Group Anagrams, Longest Consecutive Sequence, and hundreds of other problems by providing O(1) average-case lookup, insertion, and deletion. Understanding how hash functions, collision resolution, and load factors work — not just how to use a dict — is what separates strong candidates from average ones.

This module covers hash function design, collision handling strategies, hash map vs. hash set use cases, and the interview patterns that rely on hashing.

---

### 1. High-Yield Glossary

*   **Hash function**: A function that maps a key of arbitrary type to an integer index within a fixed-size array (the hash table). A good hash function distributes keys uniformly to minimize collisions. In Python, `hash(key) % capacity` is the simplified model.

*   **Hash table**: An array-based data structure that stores key-value pairs at positions determined by a hash function, achieving O(1) average-case insertion, deletion, and lookup. Python's `dict` and Java's `HashMap` are hash table implementations.

*   **Collision**: An event where two different keys produce the same hash index. All hash tables must handle collisions because the number of possible keys exceeds table capacity.

*   **Separate chaining**: A collision resolution strategy where each table slot holds a linked list (or another collection) of all key-value pairs that hash to that index. Lookup scans the chain at the target index. O(1) average, O(n) worst case if all keys collide.

*   **Open addressing (linear probing)**: A collision resolution strategy where, on a collision, the algorithm probes sequential slots (index+1, index+2, …) until an empty slot is found. Keeps all data in the primary array — better cache performance than chaining but requires careful deletion handling.

*   **Load factor**: The ratio of stored entries to total table capacity (n/m). When the load factor exceeds a threshold (commonly 0.75), the table is resized (rehashed) to maintain O(1) average performance. High load factors increase collision probability.

*   **Hash set**: A hash table that stores only keys (no associated values), providing O(1) average membership testing. Python's `set` is a hash set. Used in interviews to answer "have I seen this before?" in O(1).

---

### 2. Certification Exam Tips
*   **Two Sum in O(n) always uses a hash map:** For each element, check if its complement (target – current) already exists in the map. If not, store the current element. One pass, O(n) time, O(n) space.
*   **Frequency counting = hash map:** Counting characters, words, or elements (Group Anagrams, Top K Frequent Elements, Ransom Note) always starts with a `Counter` or `defaultdict(int)`.
*   **Hash set for O(1) "seen" checks:** Cycle detection in arrays, finding duplicates, and checking set membership are all solved with a hash set. Avoids the O(n) linear scan trap.
*   **Worst case is O(n) — know when it matters:** Hash table worst case (all keys collide) is O(n) per operation. Interviewers may ask about this; mention that good hash functions and rehashing keep the average at O(1).
*   **Tuple/frozenset as dict keys:** In Python, only hashable (immutable) objects can be dict keys. Tuples are hashable; lists are not. When grouping anagrams, use `tuple(sorted(word))` as the key.
*   **Study Resource:** Read [Hash Tables – Visualgo](https://visualgo.net/en/hashtable) for an animated visualization of separate chaining and linear probing that makes collision resolution concrete and memorable.

---

### Required Readings & Videos
*   **Required Reading:** [Hash Tables – Open Data Structures (Pat Morin), Chapter 5](https://opendatastructures.org/ods-python/5_Hash_Tables.html) — covers chaining and linear probing implementations with full Python code and amortized analysis.
*   **Required Video:** [Hash Map / Set – NeetCode on YouTube](https://www.youtube.com/watch?v=shs0KM3wKv8) — a 25-minute interview-focused walkthrough covering hash map internals, collision resolution, and the Two Sum / Group Anagrams patterns.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a hash map from scratch** using separate chaining with a fixed-size array and a linked list per bucket.
*   **Solve LeetCode #1 (Two Sum)** using a hash map for O(n) time and explain why the brute-force nested loop is O(n²).
*   **Solve LeetCode #49 (Group Anagrams)** using a `defaultdict(list)` with sorted-tuple keys.
*   **Solve LeetCode #128 (Longest Consecutive Sequence)** using a hash set to achieve O(n) instead of O(n log n).

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 5 of Open Data Structures.
- [ ] Watch the NeetCode Hash Map / Set video.
- [ ] Implement a hash map from scratch with separate chaining.
- [ ] Solve LeetCode #1, #49, and #128.
- [ ] Proceed to the Module 05 Quiz.
