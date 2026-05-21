# Quiz: Module 15 – Advanced Topics: Tries and Segment Trees
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of searching for a word of length L in a Trie containing n words?
*   A) O(n) — every stored word must be checked.
*   B) O(n · L) — each of the n words is compared character by character.
*   C) O(L) — the search follows at most L edges from root to leaf, one per character.
*   D) O(log n) — the Trie is a balanced binary tree, so search follows a binary-search path.
*   **Correct Answer:** C) O(L) — the search follows at most L edges from root to leaf, one per character.
*   **Distractor Analysis:**
    *   *Why correct:* In a Trie, each character in the query word selects the next child node. The search visits exactly L nodes regardless of how many words are stored, making it independent of n.
    *   A is incorrect: O(n) describes linear scan over all words (brute force), not Trie search.
    *   B is incorrect: O(n·L) is the cost of comparing the query string against all n stored strings character by character — exactly what the Trie avoids.
    *   D is incorrect: A Trie is not a binary search tree. It branches on characters (up to 26 children), and its search depth is bounded by word length L, not log n.

---

**Question 2**
Which of the following is the most accurate definition of a **segment tree** in the context of data structures?
*   A) A balanced BST whose in-order traversal visits array elements in sorted order, enabling O(log n) range queries by locating left and right boundary nodes.
*   B) A binary tree built over an array where each internal node stores the aggregate result (sum, min, max) of the subarray corresponding to its subtree, enabling O(log n) range queries and O(log n) point updates.
*   C) A tree structure for string prefix matching where each node represents one character and paths from root to leaf spell out complete words stored in the dataset.
*   D) A 2D tree structure that partitions a plane into quadrants recursively, used for spatial range queries over (x, y) coordinate data.
*   **Correct Answer:** B) A binary tree built over an array where each internal node stores the aggregate result (sum, min, max) of the subarray corresponding to its subtree, enabling O(log n) range queries and O(log n) point updates.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes a BST used for range queries by tree traversal, not a segment tree. Segment trees are indexed by array positions, not by value ordering.
    *   *Why B is correct:* A segment tree builds a complete binary tree where the root covers [0, n-1], each internal node covers a half-subarray, and leaves cover individual elements. Aggregate values propagate bottom-up, enabling log n-depth query traversal.
    *   *Why C is incorrect:* That describes a Trie (prefix tree), which is also covered in this module but is a completely different structure.
    *   *Why D is incorrect:* That describes a Quadtree, a spatial data structure for 2D point queries — unrelated to segment trees.

---

**Question 3**
In a Trie implementation using Python dictionaries for children, what does the `is_end` flag on a TrieNode represent?
*   A) Whether the node has any children — nodes with `is_end = True` are leaf nodes with no further characters.
*   B) Whether the path from the root to this node spells out a complete word that was explicitly inserted into the Trie.
*   C) Whether the character at this node is a vowel, used to optimize prefix search for natural language words.
*   D) Whether this node is the root of the Trie — only the root has `is_end = True` to mark the starting point of all searches.
*   **Correct Answer:** B) Whether the path from the root to this node spells out a complete word that was explicitly inserted into the Trie.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Leaf nodes (no children) are not always word ends — a word may be a prefix of a longer stored word, so its end node has children but still has `is_end = True`. A node can be both a leaf and `is_end = True`, or an internal node with `is_end = True`.
    *   *Why B is correct:* `is_end` marks the end of an inserted word. Without it, "app" and "apple" would be indistinguishable in a Trie since "app" is a prefix of "apple". Setting `is_end = True` at the 'p' node distinguishes inserted words from mere prefixes.
    *   *Why C is incorrect:* `is_end` has nothing to do with vowels or language-specific optimization. It is a structural marker for word boundaries.
    *   *Why D is incorrect:* The root is the starting point of all insertions and searches but represents no character and has `is_end = False` (unless the empty string was explicitly inserted).

---

**Question 4**
A segment tree over an array of size n = 8 is stored in an array. At what indices are the children of the node at index i stored?
*   A) Indices i–1 and i+1
*   B) Indices 2i and 2i+1
*   C) Indices i/2 and i·2
*   D) Indices i+n and i+n+1
*   **Correct Answer:** B) Indices 2i and 2i+1
*   **Distractor Analysis:**
    *   *Why A is incorrect:* i–1 and i+1 describe adjacent elements in a flat array, not a parent-child tree relationship.
    *   *Why B is correct:* The standard heap/segment tree array indexing (1-based) uses 2i for the left child and 2i+1 for the right child. This formula is derived from the complete binary tree level structure and is used in both heap and segment tree implementations.
    *   *Why C is incorrect:* i/2 is the parent of i (the parent formula), not the child. Swapping and mixing multiplication and division here produces incorrect indices.
    *   *Why D is incorrect:* i+n and i+n+1 are used in an alternative bottom-up segment tree layout where leaves start at index n, but this is not the standard formula for finding children of node i.

---

**Question 5**
A Trie stores the words: "apple", "app", "apt". Which result does `startsWith("ap")` return, and which does `search("app")` return?
*   A) `startsWith("ap")` returns False because "ap" is not a complete word; `search("app")` returns True.
*   B) `startsWith("ap")` returns True because "ap" is a prefix of stored words; `search("app")` returns True because "app" was explicitly inserted.
*   C) `startsWith("ap")` returns True; `search("app")` returns False because "app" is only a prefix of "apple", not a standalone word.
*   D) Both return False because neither "ap" nor "app" equals the full words stored in the Trie.
*   **Correct Answer:** B) `startsWith("ap")` returns True because "ap" is a prefix of stored words; `search("app")` returns True because "app" was explicitly inserted.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `startsWith("ap")` returning False would mean no stored word starts with "ap" — but "apple", "app", and "apt" all do. The method returns True for any valid prefix.
    *   *Why B is correct:* `startsWith("ap")` checks prefix existence — True since "ap" is a prefix of all three words. `search("app")` checks whether "app" was explicitly inserted as a complete word — True because "app" is in the Trie with `is_end = True` at the final 'p' node.
    *   *Why C is incorrect:* "app" was explicitly inserted, so its terminal 'p' node has `is_end = True`. Without this, C would be correct, illustrating exactly why the `is_end` flag is essential.
    *   *Why D is incorrect:* `startsWith` does not require a full word match; it returns True for any stored prefix. `search` does require a full word match, but "app" was inserted, so it is True.
