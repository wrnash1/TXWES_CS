# Reading Guide: Module 10 — Breadth-First Search & Depth-First Search

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

BFS and DFS are the two fundamental graph traversal algorithms. Every graph problem reduces to one of them. BFS expands outward level by level using a queue, guaranteeing shortest paths in unweighted graphs. DFS goes as deep as possible before backtracking using a stack or recursion, powering cycle detection, connected components, and topological sort. Both run in O(V + E) time.

---

## 1. Breadth-First Search (BFS)

### Algorithm

BFS uses a FIFO queue. Nodes are marked visited when enqueued to prevent duplicates.

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)    # mark on enqueue, not dequeue
                queue.append(neighbor)

    return order
```

### BFS Shortest Path

BFS guarantees that the first time a node is reached is via the shortest path (fewest hops). Track distances explicitly:

```python
def bfs_distances(graph, start):
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist
```

### BFS Complexity

- Time: O(V + E) — each vertex and edge processed once
- Space: O(V) — queue and visited set

### Why Mark on Enqueue?

If a node is marked visited only when dequeued, the same node can be added to the queue multiple times (once by each neighbor that discovers it). This causes duplicate processing and degrades performance on dense graphs. Marking on enqueue ensures each node enters the queue exactly once.

---

## 2. Depth-First Search (DFS)

### Iterative DFS (Explicit Stack)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order
```

### Recursive DFS

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    order = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order
```

### DFS Complexity

- Time: O(V + E)
- Space: O(V) for the recursion stack or explicit stack

### Recursion Depth Warning

Python's default recursion limit is 1000 (`sys.getrecursionlimit()`). For large graphs, use iterative DFS to avoid `RecursionError`. Increase the limit only as a last resort: `sys.setrecursionlimit(10000)`.

---

## 3. Connected Components

Each DFS or BFS call from an unvisited node explores exactly one connected component. Count components by counting how many times a fresh traversal is started.

```python
def count_components(graph):
    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            components += 1

    return components
```

---

## 4. Topological Sort (DFS Post-Order)

Topological sort orders vertices in a DAG such that every edge u→v has u before v. The DFS-based approach appends each node after visiting all its descendants (post-order), then reverses the list.

```python
def topological_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)    # post-order append

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]    # reverse = topological order
```

**Why reversal?** A node is appended after all its dependencies are processed. Reversing the post-order list puts the most independent nodes (those with no outgoing edges) last — which, after reversal, become last in the topological order.

**Kahn's Algorithm (BFS-based topological sort):** Start from all nodes with in-degree 0 and repeatedly remove them. If the final list has fewer than V nodes, the graph has a cycle.

```python
from collections import deque

def kahns_topological_sort(graph, n):
    in_deg = [0] * n
    for u in graph:
        for v in graph[u]:
            in_deg[v] += 1

    queue = deque([i for i in range(n) if in_deg[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []    # empty = cycle detected
```

---

## 5. Grid BFS/DFS — Number of Islands (LeetCode #200)

Grids are implicit graphs. Model each cell as a node and cardinal neighbors (up/down/left/right) as edges.

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'    # mark visited by sinking
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

**In-place marking:** setting `grid[r][c] = '0'` avoids a separate `visited` set. Valid when modifying the input is acceptable; copy the grid first if the original must be preserved.

---

## 6. Course Schedule — Cycle Detection (LeetCode #207)

Given `numCourses` and a list of prerequisites, return True if all courses can be finished (no cycle in the directed dependency graph).

```python
def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        graph[b].append(a)    # b must be taken before a

    # 0 = unvisited, 1 = in current path, 2 = done
    state = [0] * num_courses

    def dfs(node):
        if state[node] == 1:    # back edge — cycle
            return False
        if state[node] == 2:    # already fully processed
            return True
        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = 2
        return True

    return all(dfs(i) for i in range(num_courses))
```

Three-color DFS (0=white, 1=gray, 2=black) is the canonical directed cycle detection for interview problems.

---

## 7. BFS vs. DFS Decision Table

| Goal | Algorithm | Key Reason |
|---|---|---|
| Shortest path (unweighted) | BFS | Level-by-level guarantees minimum hops |
| All nodes in a component | Either | Both visit every reachable node |
| Cycle detection (directed) | DFS | Recursion stack tracks active path |
| Topological sort | DFS or Kahn's BFS | Post-order DFS or in-degree reduction |
| Grid traversal (islands) | DFS (recursive) | Natural 4-directional recursion |
| Detect if path exists | Either | Stop at destination |

---

## 8. Complexity Summary

| Algorithm | Time | Space | Notes |
|---|---|---|---|
| BFS | O(V + E) | O(V) | Use deque for O(1) popleft |
| DFS iterative | O(V + E) | O(V) | Explicit stack |
| DFS recursive | O(V + E) | O(V) | Call stack — beware depth limit |
| Topological sort | O(V + E) | O(V) | DFS post-order or Kahn's |
| Grid BFS/DFS | O(m × n) | O(m × n) | m rows, n columns |

---

## 9. Interview Exam Tips

1. **BFS for shortest path, DFS for everything else (roughly)** — BFS level-by-level expansion is the key property. If the problem asks for minimum distance or steps, BFS is the right choice.

2. **Mark visited on enqueue in BFS** — not on dequeue. This prevents adding the same node to the queue multiple times from different neighbors.

3. **Use `deque` not `list` for BFS** — `list.pop(0)` is O(n); `deque.popleft()` is O(1). This is a common interview mistake.

4. **Iterative DFS for large inputs** — Python's recursion limit is 1000. Explicit stack-based DFS has no depth limit.

5. **Three-color DFS for directed cycle detection** — white (unvisited), gray (in current path), black (done). Gray-to-gray back edge = cycle.

6. **Grid problems: 4-directional neighbors** — `(r±1, c)` and `(r, c±1)`. Always check bounds first: `0 <= r < rows and 0 <= c < cols`.

7. **Topological sort only works on DAGs** — if the graph has a cycle, there is no valid topological order. Kahn's algorithm detects cycles implicitly: if result length < V, a cycle exists.

8. **In-place grid marking** — setting visited cells to a sentinel value (`'0'`, `-1`) avoids extra space. Only do this if modifying input is acceptable.

---

## 11. Supplemental Resources

The following free, openly licensed resources reinforce the concepts in this module. All are zero-cost and require no account to access.

1. **VisuAlgo — BFS and DFS Visualizations** — [https://visualgo.net/en/dfsbfs](https://visualgo.net/en/dfsbfs)
   Step-by-step animations of BFS and DFS on directed and undirected graphs, with the queue/stack state shown alongside the graph traversal. An excellent tool for confirming your mental model before coding.

2. **OpenDSA — Graph Traversal Chapter** — [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/GraphTraversal.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/GraphTraversal.html)
   Free interactive OER textbook covering BFS, DFS, topological sort, and cycle detection with embedded exercises and complexity proofs.

3. **NeetCode — Graphs BFS/DFS Playlist (YouTube)** — [https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI](https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI)
   Free video solutions for Number of Islands, Course Schedule, and other BFS/DFS interview problems. Each video explains the algorithm choice (BFS vs DFS) and the complexity analysis.

4. **Khan Academy — BFS and DFS** — [https://www.khanacademy.org/computing/computer-science/algorithms/graph-search/a/breadth-first-search-and-its-uses](https://www.khanacademy.org/computing/computer-science/algorithms/graph-search/a/breadth-first-search-and-its-uses)
   Free article covering BFS with the level-by-level distance guarantee and common applications including shortest path in unweighted graphs.

5. **MIT OCW 6.006 — BFS/DFS Lecture 13** — [https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)
   MIT lecture notes and video on BFS, DFS, topological sort, and DAG cycle detection. The proof that BFS computes shortest distances in unweighted graphs is covered rigorously here.

---

## 10. Study Checklist

- [ ] Watch the Module 10 video lecture by Professor Nash.
- [ ] Implement BFS with distance tracking from scratch.
- [ ] Implement iterative DFS and recursive DFS.
- [ ] Implement connected component counting using DFS.
- [ ] Implement topological sort (DFS post-order) and Kahn's algorithm.
- [ ] Solve LeetCode #200 (Number of Islands).
- [ ] Solve LeetCode #207 (Course Schedule).
- [ ] Complete the Module 10 Lab.
- [ ] Complete the Module 10 Quiz.
