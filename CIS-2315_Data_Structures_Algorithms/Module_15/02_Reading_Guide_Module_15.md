# Reading Guide: Module 15 – Advanced Topics: Tries and Segment Trees
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 15 – Advanced Topics: Tries and Segment Trees**! This module covers two specialized data structures that appear in harder interview problems and in-depth system design discussions. Tries are the essential structure behind autocomplete, spell checking, and word prefix problems. Segment trees power range query problems in competitive programming and sometimes appear in advanced interview rounds at top companies. Mastering both structures demonstrates the depth expected for senior and staff-level roles.

This module covers Trie construction and search, prefix/suffix operations, and segment tree range query and point update patterns.

---

### 1. High-Yield Glossary

*   **Trie (prefix tree)**: A tree data structure where each node represents a single character, and paths from the root to marked nodes represent complete words or prefixes. Insertion and search are O(L) where L is the word length, independent of the number of stored words.

*   **TrieNode**: The building block of a trie, typically containing an array or dictionary of 26 (or more) child pointers (one per possible character) and a boolean `is_end` flag marking whether the node represents the end of a valid word.

*   **Prefix search**: One of the primary use cases for a trie — determining whether any stored word starts with a given prefix in O(L) time, where L is the prefix length. This is O(n·L) with a linear scan over n strings.

*   **Segment tree**: A binary tree data structure built over an array, where each node stores the result of a range query (sum, min, max) for a contiguous subarray. Supports both range queries and point updates in O(log n) time.

*   **Range query**: A query that asks for an aggregated value (sum, minimum, maximum, GCD) over all elements in a specified index range [l, r]. Segment trees answer these in O(log n) versus O(n) for brute force.

*   **Point update**: Changing the value of a single element in an array and reflecting that change in all range query results. Segment trees propagate point updates in O(log n) by updating only the nodes on the root-to-leaf path.

*   **Lazy propagation**: An optimization for segment trees where range updates (update all elements in [l, r] simultaneously) are deferred using "lazy" markers, allowing both range updates and range queries in O(log n). Without lazy propagation, range updates cost O(n).

---

### 2. Certification Exam Tips
*   **Implement a Trie from scratch — it is a common interview question:** Build a `TrieNode` class with `children = {}` and `is_end = False`. Then build a `Trie` class with `insert`, `search`, and `startsWith` methods. LeetCode #208 is the canonical problem.
*   **Trie solves "word dictionary with wildcards":** LeetCode #211 (Design Add and Search Words Data Structure) uses a trie where `.` matches any character — implement DFS over children for the wildcard case.
*   **Segment tree is O(log n) for both update and query:** Brute force is O(1) update / O(n) query; prefix sum is O(n) update / O(1) query; segment tree achieves O(log n) for both simultaneously.
*   **Know the segment tree array indexing:** Store the tree in an array of size 4n. Left child of index i is at 2i; right child at 2i+1. Build recursively, query and update with range partitioning.
*   **Fenwick Tree (Binary Indexed Tree) is an O(log n) alternative:** Simpler to code than a segment tree for prefix-sum queries and point updates. Useful as an alternative to segment trees when only prefix operations are needed.
*   **Study Resource:** [Trie Data Structure — LeetCode Explore Card](https://leetcode.com/explore/learn/card/trie/) — a structured progression of trie problems with implementation guidance, from basic insert/search through word search II.

---

### Required Readings & Videos
*   **Required Reading:** [Tries – Open Data Structures (Pat Morin), Chapter 13](https://opendatastructures.org/ods-python/13_Data_Structures_for_Strings.html) — covers trie construction, prefix operations, and time complexity analysis with Python implementations.
*   **Required Video:** [Trie – NeetCode on YouTube](https://www.youtube.com/watch?v=oobqoCJlHA0) — a 15-minute video implementing a Trie from scratch with the LeetCode #208 and #211 problems, covering the `children` dict approach and `is_end` flag.
*   **Additional Video:** [Segment Tree – NeetCode on YouTube](https://www.youtube.com/watch?v=2bSS8rtFym4) — a 20-minute segment tree implementation video covering the array-based build, range sum query, and point update with LeetCode #307.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Implement a Trie class from scratch** with `insert`, `search`, and `startsWith` — verify on LeetCode #208.
*   **Solve LeetCode #211 (Design Add and Search Words)** — extend the Trie to handle `.` wildcard characters using DFS.
*   **Solve LeetCode #212 (Word Search II)** — combine a Trie with backtracking on a 2D grid.
*   **Implement a Segment Tree** supporting range sum query and point update — verify on LeetCode #307 (Range Sum Query — Mutable).

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 13 of Open Data Structures.
- [ ] Watch the NeetCode Trie and Segment Tree videos.
- [ ] Implement a Trie from scratch.
- [ ] Solve LeetCode #208, #211, and #307.
- [ ] Proceed to the Module 15 Quiz.
