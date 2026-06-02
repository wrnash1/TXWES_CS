# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 16 — Final Exam Prep & Coding Interview Practice

**Estimated Duration:** 28–32 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - This is a review lecture — no new algorithms. Emphasize patterns and connections across modules.
> - Use VS Code to show quick implementations from memory, demonstrating interview-style coding.
> - [PAUSE] = 2 seconds of silence.
> - Structure: walk through the six major algorithm families covered in this course, stating the canonical LeetCode problem for each, the key implementation detail, and the complexity.
> - Emphasize the "pattern recognition" skill: given a new problem, which family does it belong to?
> - End with 5 interview strategies: think aloud, start with brute force, optimize, test on examples, ask clarifying questions.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 16 | Final Exam Prep | CIS-2315"]**

"This is the final module of CIS-2315. We have covered sixteen weeks of data structures and algorithms — arrays, linked lists, trees, graphs, hash tables, heaps, divide-and-conquer, greedy algorithms, dynamic programming, and string algorithms. Today we review the six major algorithm families, connect them to the LeetCode problems you have practiced, and discuss how to approach a coding interview problem you have never seen before. The goal is not just to remember algorithms — it is to recognize which algorithm applies when."

---

## [01:30 – 07:00] Review — Sorting, Searching, and Tree Operations

**[SHOW SLIDE: "Foundational Algorithms: Sort, Search, Tree"]**

"Let's start with the foundation. Every interview assumes you know these cold.

**Sorting:** Know three algorithms and their trade-offs.

| Algorithm | Time | Space | Stable |
|---|---|---|---|
| Merge sort | O(n log n) | O(n) | Yes |
| Quicksort | O(n log n) avg / O(n²) worst | O(log n) | No |
| Heap sort | O(n log n) | O(1) | No |

In Python, `sorted()` and `list.sort()` use Timsort — O(n log n), stable, O(n) space. Use it. Do not implement sorting unless asked.

**Binary Search:** Three variants.

```python
# Standard — find if target exists
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

# Leftmost — first occurrence
def search_leftmost(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target: left = mid + 1
        else: right = mid
    return left if left < len(arr) and arr[left] == target else -1

# Binary search on answer (monotone feasible function)
# Template: while left < right; feasible(mid) → right=mid; else left=mid+1
```

**Binary Search Trees:** Inorder traversal gives sorted order. Search, insert, delete: O(h) where h = height. Balanced BST: O(log n). Python: use `sortedcontainers.SortedList` or `heapq`.

**Heaps:** Min-heap via `heapq`. Push: O(log n). Pop: O(log n). Heapify: O(n). Use for K-th largest (size-K min-heap), K-way merge, and priority queues.

[PAUSE]"

---

## [07:00 – 13:00] Review — Graph Algorithms

**[SHOW SLIDE: "Graph Algorithms: BFS, DFS, Dijkstra"]**

"Graphs are the most common non-trivial data structure in interviews. Know three algorithms.

**BFS — shortest path in unweighted graphs, level-by-level traversal:**

```python
from collections import deque
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

Mark on enqueue, not dequeue. Use `deque` not `list` (O(1) popleft vs. O(n)).

**DFS — connected components, cycle detection, topological sort:**

Three-color DFS for directed cycle detection (Course Schedule):
- 0 = unvisited, 1 = in current path, 2 = fully processed
- Back edge to a 1-colored node = cycle

Kahn's algorithm for topological sort: reduce in-degrees, BFS from zero-in-degree nodes.

**Dijkstra — shortest path in weighted non-negative graphs:**

```python
import heapq
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]: continue    # stale entry
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist
```

Time: O((V+E) log V). Negative weights: use Bellman-Ford — O(V·E).

[PAUSE]"

---

## [13:00 – 18:00] Review — Divide & Conquer and Greedy

**[SHOW SLIDE: "Divide & Conquer and Greedy"]**

"**Divide & Conquer — Master Theorem:**

T(n) = a·T(n/b) + f(n). Let c = log_b(a).
- Case 2: f(n) = Θ(n^c) → T(n) = Θ(n^c log n)
- Merge sort: T(n)=2T(n/2)+O(n) → O(n log n). Binary search: T(n)=T(n/2)+O(1) → O(log n). Both Case 2.

Binary search on answer: when the answer is in a range and feasibility is monotone. Canonical: Ship Packages (LeetCode #1011).

**Greedy — exchange argument proves correctness:**

Three canonical problems:
- Activity Selection: sort by finish time → O(n log n). Exchange argument: earliest-finish leaves the most room.
- Jump Game I (LeetCode #55): track `max_reach` → O(n).
- Gas Station (LeetCode #134): reset `start = i+1` when `current_tank < 0` → O(n).

When greedy fails — 0/1 knapsack. Items cannot be split → use DP.

[PAUSE]"

---

## [18:00 – 23:00] Review — Dynamic Programming

**[SHOW SLIDE: "Dynamic Programming: Subproblem, Recurrence, Base Case"]**

"DP requires two properties: optimal substructure and overlapping subproblems.

The three-step DP setup:
1. Define the subproblem: what does `dp[i]` (or `dp[i][j]`) mean?
2. Write the recurrence.
3. Establish base cases.

**1D DP:**

| Problem | Subproblem | Recurrence |
|---|---|---|
| Fibonacci | dp[i] = ith Fibonacci number | dp[i] = dp[i-1] + dp[i-2] |
| Coin Change | dp[i] = min coins for amount i | dp[i] = min(dp[i-c]+1) over coins c |
| Climbing Stairs | dp[i] = ways to reach step i | dp[i] = dp[i-1] + dp[i-2] |
| House Robber | dp[i] = max robbery up to house i | dp[i] = max(dp[i-1], dp[i-2]+nums[i]) |

**2D DP:**

LCS: dp[i][j] = LCS length of text1[0..i-1] and text2[0..j-1].
- Match: dp[i][j] = dp[i-1][j-1] + 1
- No match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

0/1 Knapsack: dp[i][w] = max value using first i items with capacity w.
- dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)

[PAUSE]"

---

## [23:00 – 27:00] Review — Hash Tables and String Algorithms

**[SHOW SLIDE: "Hash Tables, Trie, Sliding Window"]**

"**Hash Tables:**

Python `dict` and `set` — O(1) average for insert, lookup, delete. `collections.Counter` for frequency counts. `collections.defaultdict` to avoid KeyError on missing keys.

Two Sum: store complement → O(n). Group Anagrams: `tuple(sorted(word))` as canonical key. Longest Consecutive: use set, start sequence only when `n-1` not in set.

**Trie:**

Node: `children = {}`, `is_end = False`. Insert and search: O(L). `search` requires `is_end=True`; `starts_with` only needs the path to exist.

**Sliding Window:**

Longest Substring Without Repeating Characters:
```python
char_index = {}; left = 0
for right, char in enumerate(s):
    if char in char_index and char_index[char] >= left:
        left = char_index[char] + 1
    char_index[char] = right
    max_len = max(max_len, right - left + 1)
```

Minimum Window Substring: expand right until formed==required; shrink left while valid.

Expand-Around-Center for palindromes: call `expand(i,i)` and `expand(i,i+1)` for every center."

---

## [27:00 – 31:00] Five Interview Strategies

**[SHOW SLIDE: "Five Strategies for Unseen Problems"]**

"When you see a new problem in an interview:

**1. Restate the problem.** Repeat it back in your own words and confirm constraints (sorted? unique? positive? what to return?). This shows you understand it and buys thinking time.

**2. Brute force first.** Say 'the brute force is O(n²) — nested loops checking all pairs.' This gives you a baseline and shows you can solve the problem, even if slowly.

**3. Identify the pattern.** Ask: Is there sorted structure? → Binary search. Is there a contiguous window? → Sliding window. Is there a graph? → BFS/DFS. Is there overlapping subproblems? → DP. Is there a locally optimal choice that's globally valid? → Greedy.

**4. Code with variable names that match your explanation.** `max_reach`, `current_end`, `farthest` are better than `a`, `b`, `c`. The interviewer is reading your code as you type.

**5. Test on the examples, then on edge cases.** Edge cases: empty input, single element, all same elements, already sorted, reverse sorted. Run them mentally before saying 'I'm done.'

[PAUSE]

**The pattern map:**

- Any contiguous range problem → Sliding window or prefix sum
- Any 'find minimum/maximum satisfying condition' over a range → Binary search on answer
- Any graph problem → BFS (shortest path / level) or DFS (connectivity / cycles / topo sort)
- Any problem with 'at most K' or overlapping subsets → DP
- Any prefix lookup or word suggestion → Trie

Good luck on your certification exam. You have the tools. Now practice until the patterns are automatic."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 16 — Final Exam Prep]**

---

## Additional Resources

- [NeetCode Roadmap — Comprehensive LeetCode Study Guide](https://neetcode.io/roadmap)
- [LeetCode Top 100 Liked Problems](https://leetcode.com/studyplan/top-100-liked/)
- [Tech Interview Handbook — Algorithm Cheat Sheet](https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/)
