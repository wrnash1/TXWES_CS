# Reading Guide: Module 16 — Final Exam Prep & Coding Interview Practice

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-2315 &BULL; DATA STRUCTURES & ALGORITHM ANALYSIS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

This reading guide consolidates the entire CIS-2315 curriculum into a single reference document. It is organized by algorithm family, with the canonical LeetCode problem for each family, the key implementation insight, and the complexity. Use this guide as a study checklist before the certification exam.

---

## 1. Sorting and Searching

### Sorting Complexity Reference

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Python Timsort | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

Choose merge sort when stability or worst-case guarantee matters. Use Python's built-in `sorted()` in interviews unless asked to implement.

### Binary Search (Module 12)

Three variants — memorize all three:

```python
# Standard: find index or -1
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    ...

# Leftmost occurrence
left, right = 0, len(arr)
while left < right:
    mid = left + (right - left) // 2
    if arr[mid] < target: left = mid + 1
    else: right = mid

# Binary search on answer (monotone feasible)
while left < right:
    mid = left + (right - left) // 2
    if feasible(mid): right = mid
    else: left = mid + 1
```

---

## 2. Heaps and Priority Queues (Module 7)

- `heapq` is a min-heap. For max-heap: push `-val`, pop and negate.
- K-th largest: maintain a size-K min-heap. If `val > heap[0]`, replace.
- K-way merge: push `(val, list_index, element_index)` tuples.
- Heapify: O(n). Push/pop: O(log n). Peek: O(1).

```python
import heapq
heap = []
heapq.heappush(heap, val)
smallest = heapq.heappop(heap)
heapq.heapify(arr)        # O(n) in-place
```

---

## 3. Hash Tables (Module 8)

- Python `dict`: O(1) average insert/lookup/delete. Load factor ~2/3, rehash when exceeded.
- `collections.Counter(iterable)` — frequency map; missing keys return 0.
- `collections.defaultdict(list)` — missing keys create default value.
- Canonical patterns:

| Pattern | Technique |
|---|---|
| Two Sum | Store complement in dict |
| Group Anagrams | `tuple(sorted(word))` as key |
| Longest Consecutive Sequence | Set membership; start only at sequence head |
| Contains Duplicate | `len(set(nums)) < len(nums)` |

---

## 4. Graph Representations (Module 9)

- **Adjacency list:** `defaultdict(list)`. O(V+E) space. Standard for interviews.
- **Adjacency matrix:** V×V array. O(V²) space. O(1) edge check. Good for dense graphs.
- For directed graphs: `graph[u].append(v)` only. For undirected: both directions.
- Weighted graph: `graph[u].append((v, weight))`.

---

## 5. BFS and DFS (Module 10)

### BFS

Use `deque`. Mark visited on **enqueue** (not dequeue). BFS gives shortest path in unweighted graphs.

```python
from collections import deque
visited = {start}
queue = deque([start])
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### DFS

Recursive (uses call stack) or iterative (explicit stack). Three-color DFS for directed cycle detection:

```python
color = {node: 0 for node in graph}    # 0=unvisited, 1=active, 2=done
def dfs(node):
    color[node] = 1
    for neighbor in graph[node]:
        if color[neighbor] == 1: return False    # cycle
        if color[neighbor] == 0:
            if not dfs(neighbor): return False
    color[node] = 2
    return True
```

### Topological Sort

Kahn's algorithm: find zero-in-degree nodes, BFS, reduce neighbors' in-degrees.
DFS post-order: append node to result after all neighbors finish; reverse at end.

### Grid Problems

Mark visited in-place. 4-directional neighbors: `[(0,1),(0,-1),(1,0),(-1,0)]`.

---

## 6. Dijkstra's Algorithm (Module 11)

Shortest path in weighted non-negative graphs. Lazy deletion with stale-entry check.

```python
dist = {node: float('inf') for node in graph}
dist[start] = 0
heap = [(0, start)]
while heap:
    d, node = heapq.heappop(heap)
    if d > dist[node]: continue    # stale — skip
    for neighbor, weight in graph[node]:
        if dist[node] + weight < dist[neighbor]:
            dist[neighbor] = dist[node] + weight
            heapq.heappush(heap, (dist[neighbor], neighbor))
```

Time: O((V+E) log V). Negative weights: Bellman-Ford O(V·E).

Path reconstruction: `prev` dict; trace back from destination, reverse.

---

## 7. Divide & Conquer (Module 12)

**Master Theorem:** T(n) = aT(n/b) + f(n), c = log_b(a).

- Case 1: f(n) = O(n^(c-ε)) → T(n) = Θ(n^c)
- Case 2: f(n) = Θ(n^c) → T(n) = Θ(n^c log n)
- Case 3: f(n) = Ω(n^(c+ε)) → T(n) = Θ(f(n))

Merge sort and binary search both fall under Case 2.

**Counting inversions:** modified merge sort; when right-half element placed before remaining left elements, `inversions += len(left) - i`.

---

## 8. Greedy Algorithms (Module 13)

Correctness requires the exchange argument: any optimal solution can be modified to agree with the greedy choice without reducing quality.

| Problem | Greedy Criterion | Complexity |
|---|---|---|
| Activity Selection | Earliest finish time | O(n log n) |
| Jump Game I | Track max_reach | O(n) |
| Jump Game II | BFS-level: current_end, farthest | O(n) |
| Gas Station | Reset start on negative tank | O(n) |
| Fractional Knapsack | Value/weight ratio | O(n log n) |

Greedy fails for 0/1 Knapsack — requires DP.

---

## 9. Dynamic Programming (Module 14)

**Three-step setup:** define subproblem → write recurrence → establish base cases.

### 1D DP Reference

| Problem | dp[i] means | Recurrence | Base |
|---|---|---|---|
| Fibonacci | ith Fibonacci | dp[i] = dp[i-1] + dp[i-2] | dp[0]=0, dp[1]=1 |
| Coin Change | min coins for amount i | dp[i] = min(dp[i-c]+1) | dp[0]=0 |
| Climbing Stairs | ways to reach step i | dp[i] = dp[i-1] + dp[i-2] | dp[1]=1, dp[2]=2 |
| House Robber | max robbery first i houses | dp[i] = max(dp[i-1], dp[i-2]+nums[i]) | dp[0]=0, dp[1]=nums[0] |

### 2D DP Reference

**LCS:** `dp[i][j]` = LCS of text1[0..i-1] and text2[0..j-1].
Match: `dp[i][j] = dp[i-1][j-1] + 1`. No match: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**0/1 Knapsack:** `dp[i][w]` = max value, first i items, capacity w.
`dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)` if weight ≤ w, else `dp[i-1][w]`.

---

## 10. String Algorithms (Module 15)

### Trie

O(L) insert/search. `is_end` flag distinguishes `search` from `starts_with`. Space: O(N×L×A).

### Sliding Window

Expand right pointer; contract left when constraint violated. Key guard: `char_index[char] >= left`.

### Minimum Window Substring

`formed` / `required` pattern. Expand until `formed == required`; shrink while valid.

### Palindromes

Expand-around-center: `expand(i,i)` for odd, `expand(i,i+1)` for even. Slice: `s[left+1:right]` after loop exits (overshoot correction).

---

## 11. Complexity Quick Reference

| Operation / Problem | Time | Space |
|---|---|---|
| Hash table lookup | O(1) avg | O(n) |
| Binary search | O(log n) | O(1) |
| Heap push/pop | O(log n) | — |
| BFS / DFS | O(V+E) | O(V) |
| Dijkstra | O((V+E) log V) | O(V) |
| Merge sort | O(n log n) | O(n) |
| Coin Change | O(amount × coins) | O(amount) |
| LCS | O(m×n) | O(m×n) |
| 0/1 Knapsack | O(n×W) | O(n×W) |
| Trie insert/search | O(L) | O(N×L×A) |
| Sliding window | O(n) | O(A) |

---

## 12. Pattern Recognition Guide

| Problem hint | Pattern / Algorithm |
|---|---|
| "Shortest path", unweighted | BFS |
| "Shortest path", weighted non-negative | Dijkstra |
| "Shortest path", negative weights | Bellman-Ford |
| "Minimum/maximum satisfying condition" in a range | Binary search on answer |
| "Contiguous subarray/substring" | Sliding window |
| "All combinations/subsets" | Backtracking (recursion) |
| "Count ways / minimum cost / maximum value" | Dynamic programming |
| "Locally optimal → globally optimal" | Greedy |
| "Prefix query / autocomplete" | Trie |
| "Cycle detection, connectivity, ordering" | DFS (three-color for directed) |

---

## 13. Supplemental Resources

The following free, openly licensed resources support final exam preparation and certification readiness. All are zero-cost and require no account to access.

1. **LeetCode — Top Interview Questions (Free Tier)** — [https://leetcode.com/problemset/all/?listId=wpwgkgt](https://leetcode.com/problemset/all/?listId=wpwgkgt)
   LeetCode's curated "Top Interview Questions" list contains 145 problems across all difficulty levels covering the exact algorithm families taught in CIS-2315: arrays, strings, trees, graphs, DP, and sorting. Solving 10–15 of these before the certification exam provides direct practice under interview-style problem statements.

2. **NeetCode 150 — Complete Roadmap (YouTube + Website)** — [https://neetcode.io/roadmap](https://neetcode.io/roadmap)
   A free structured study roadmap organizing 150 LeetCode problems by pattern (Arrays, Two Pointers, Sliding Window, Heaps, Graphs, DP, etc.). Each problem links to a free video solution. The roadmap directly maps to the CIS-2315 module sequence and is the most widely used free self-study resource for technical interview preparation.

3. **Big-O Cheat Sheet** — [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)
   A single-page reference for time and space complexities of all major data structures (array, linked list, BST, AVL, heap, hash table) and algorithms (sorting, searching, graph traversal). Use this as a quick-review reference before the certification exam.

4. **MIT OCW 6.006 — Introduction to Algorithms (Full Course)** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   The complete free MIT undergraduate algorithms course — lecture notes, problem sets, and exams. Covers every major topic in CIS-2315 at a rigorous level. Particularly useful for reviewing Master Theorem applications, DP recurrences, and graph algorithm correctness proofs.

5. **HackerRank — Interview Preparation Kit** — [https://www.hackerrank.com/interview/interview-preparation-kit](https://www.hackerrank.com/interview/interview-preparation-kit)
   HackerRank's free Interview Preparation Kit with timed practice problems organized by topic (Arrays, Dictionaries, Trees, Graphs, DP, Greedy). Completing this kit provides targeted practice across the full CIS-2315 curriculum and directly builds certification exam readiness.

---

## 14. Study Checklist

- [ ] Watch the Module 16 video lecture by Professor Nash.
- [ ] Complete the Module 16 Final Practice Quiz (10 cross-module questions).
- [ ] Solve one LeetCode problem from each module's canonical list (Modules 7–15).
- [ ] Implement binary search, BFS, Dijkstra, and Coin Change from scratch without reference.
- [ ] Practice explaining the exchange argument for activity selection aloud.
- [ ] Practice explaining the DP subproblem definition for Coin Change and LCS aloud.
- [ ] Register for the Technical Interview Readiness certification exam.
- [ ] Submit certification score report to Canvas (Module 16 Lab assignment).
