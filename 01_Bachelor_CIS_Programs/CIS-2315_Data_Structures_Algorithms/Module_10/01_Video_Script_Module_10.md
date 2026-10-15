# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 10 — Breadth-First Search & Depth-First Search

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / MIT &bull; Data Structures and Algorithms Full Course &bull; Module 10</strong>
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

**Estimated Duration:** 23–27 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Opening

This module covers the two fundamental graph traversal algorithms: Breadth-First Search and Depth-First Search. BFS explores a graph level by level using a queue and finds shortest paths in unweighted graphs. DFS explores as far as possible before backtracking using a stack or recursion, and powers topological sort, cycle detection, and connected component counting. Together, BFS and DFS solve the majority of graph interview problems. Every graph algorithm you will learn — Dijkstra, topological sort, Kosaraju's SCC — is built on one of these two traversals.

---

## Part 1 — Breadth-First Search

"

```text
      A
     / \
    B   C
   / \   \
  D   E   F
```

BFS starts at node A and visits all nodes at distance 1 before visiting any at distance 2. The order is A, B, C, D, E, F.

**BFS uses a queue (FIFO):**

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()    # FIFO — process oldest first
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # mark BEFORE enqueue
                queue.append(neighbor)

    return order
```

```text
Start:   queue=['A'], visited={'A'}
Step 1:  pop A → order=['A'], enqueue B,C → queue=['B','C'], visited={'A','B','C'}
Step 2:  pop B → order=['A','B'], enqueue D,E → queue=['C','D','E']
Step 3:  pop C → order=['A','B','C'], enqueue F → queue=['D','E','F']
Step 4:  pop D → order=['A','B','C','D'] (no unvisited neighbors)
Step 5:  pop E → order=['A','B','C','D','E']
Step 6:  pop F → order=['A','B','C','D','E','F']
```

**Critical detail:** Mark nodes as visited when you enqueue them, not when you dequeue them. If you wait until dequeue, the same node can be enqueued multiple times — causing duplicates and O(E²) behavior on dense graphs.

**Time complexity:** O(V + E) — every vertex and every edge is processed once.
**Space complexity:** O(V) — the queue and visited set together hold at most V nodes.

**BFS finds shortest paths in unweighted graphs.** Because BFS expands nodes level by level, the first time BFS reaches a node is the shortest path from the source. Track distances:

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

"

---

## Part 2 — Depth-First Search

DFS explores as far as possible down one path before backtracking and trying another. For the same graph:

BFS order: A, B, C, D, E, F (level by level)
DFS order: A, B, D, E, C, F (deep first)

**Iterative DFS (explicit stack — LIFO):**

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()    # LIFO — most recently added
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order
```

**Recursive DFS:**

```python
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order
```

**Connected components using DFS:**

Count disconnected subgraphs — each time we start a fresh DFS from an unvisited node, we have found a new component.

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

**Topological Sort (DFS-based, for DAGs):**

In a DAG, a topological ordering lists every vertex before all vertices it points to. DFS computes this by appending each node to a result list after all its descendants are visited (post-order), then reversing.

```python
def topological_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)    # post-order: append after processing all neighbors

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]    # reverse gives topological order
```

"

---

## Part 3 — Number of Islands (LeetCode #200)

The Number of Islands problem is the most common graph interview problem. Given a 2D grid of `'1'` (land) and `'0'` (water), count the number of islands (connected groups of land cells).

**Model:** each `'1'` cell is a vertex; edges connect horizontally and vertically adjacent `'1'` cells. The problem asks for the number of connected components.

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '0'    # mark visited by sinking the cell
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

**[DEMO: trace on grid:**

```text
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```

Expected: 3 islands]

The `grid[r][c] = '0'` trick sinks visited cells in-place, replacing the `visited` set. When we find a `'1'`, we start a DFS that sinks the entire island — each DFS call corresponds to one island, so `count` increments exactly once per island.

**Time:** O(m × n) — every cell is visited at most once.
**Space:** O(m × n) in the worst case (recursion depth for a grid of all 1s).

---

## Part 4 — BFS vs. DFS Decision Guide

Choosing between BFS and DFS depends on what you need from the traversal:

| Goal | Algorithm | Why |
|---|---|---|
| Shortest path (unweighted) | BFS | Level-by-level guarantees minimum hops |
| Connected components | Either | Both visit all nodes in a component |
| Cycle detection | DFS | Recursion stack tracks the active path |
| Topological sort | DFS | Post-order finish times give reverse topological order |
| Grid traversal (islands) | Either | DFS is simpler to implement recursively |
| Detect if path exists | Either | Stop as soon as destination is reached |

**BFS pitfall:** Using a `list` instead of `deque` for the queue. `list.pop(0)` is O(n) — it shifts all remaining elements. Always use `deque.popleft()` which is O(1).

**DFS pitfall:** Python's default recursion limit is 1000. For deep graphs (e.g., a chain of 10,000 nodes), recursive DFS will raise `RecursionError`. Use iterative DFS with an explicit stack for large inputs.

The Module 10 lab has you implement BFS with distance tracking, DFS (both recursive and iterative), connected component counting, topological sort, and the Number of Islands problem. Good luck.

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 10 — BFS & DFS]**

---

## Additional Resources

- [VisuAlgo — BFS/DFS Visualization](https://visualgo.net/en/dfsbfs)
- [NeetCode — BFS/DFS Playlist](https://www.youtube.com/watch?v=tWVWeAqZ0WU)
- [LeetCode #200 — Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [LeetCode #207 — Course Schedule (Topological Sort / Cycle Detection)](https://leetcode.com/problems/course-schedule/)
- [LeetCode #133 — Clone Graph](https://leetcode.com/problems/clone-graph/)
