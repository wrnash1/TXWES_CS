# Lab Activity: Module 10 — Breadth-First Search & Depth-First Search

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Implement BFS with traversal order and shortest-path distances
- **Part 2** — Implement DFS (iterative and recursive), connected components, topological sort
- **Part 3** — LeetCode problems: Number of Islands and Course Schedule

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Breadth-First Search

**File:** `lab10_bfs_dfs.py`

### Setup: Graph Builder

```python
from collections import defaultdict, deque

def build_undirected(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def build_directed(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph
```

### 1.1 — BFS Traversal Order

```python
def bfs(graph, start):
    """
    BFS traversal from start.
    Returns nodes in order visited.
    Time: O(V + E), Space: O(V)
    """
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)    # mark on enqueue
                queue.append(neighbor)

    return order
```

Test:

```python
# Tree-shaped graph
edges = [('A','B'), ('A','C'), ('B','D'), ('B','E'), ('C','F')]
g = build_undirected(edges)

print(bfs(g, 'A'))
# ['A', 'B', 'C', 'D', 'E', 'F'] — level by level
```

**Checkpoint:** BFS visits A first, then its neighbors B and C (level 1), then D, E, F (level 2).

---

### 1.2 — BFS Shortest Distances

```python
def bfs_distances(graph, start):
    """
    BFS shortest distances from start to all reachable nodes.
    Returns dict of {node: distance}.
    Time: O(V + E)
    """
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

Test:

```python
g2 = build_undirected([('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')])
print(bfs_distances(g2, 'A'))
# {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 3}
```

Trace:

```text
Start: dist={'A':0}, queue=['A']
Pop A: neighbors B, C → dist={'A':0,'B':1,'C':1}, queue=['B','C']
Pop B: neighbor D (A already visited) → dist[...,'D':2], queue=['C','D']
Pop C: neighbor D (already visited)
Pop D: neighbor E → dist[...,'E':3]
Pop E: no new neighbors
```

**Checkpoint:** `dist['E']` = 3 (A→B→D→E or A→C→D→E, both length 3).

---

## Part 2 — Depth-First Search

### 2.1 — Iterative DFS

```python
def dfs_iterative(graph, start):
    """
    Iterative DFS using an explicit stack.
    Time: O(V + E), Space: O(V)
    """
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

Test:

```python
g3 = build_undirected([('A','B'), ('A','C'), ('B','D'), ('B','E'), ('C','F')])
print(dfs_iterative(g3, 'A'))
# One valid DFS order: ['A', 'C', 'F', 'B', 'E', 'D']
# (exact order depends on neighbor list order and stack behavior)
```

**Checkpoint:** All 6 nodes appear in the output. Node A appears first. The order is depth-first (deeper nodes before wide neighbors).

---

### 2.2 — Recursive DFS

```python
def dfs_recursive(graph, node, visited=None):
    """
    Recursive DFS.
    Time: O(V + E), Space: O(V) call stack
    """
    if visited is None:
        visited = set()
    visited.add(node)
    order = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order
```

Test:

```python
g4 = build_undirected([('A','B'), ('A','C'), ('B','D'), ('B','E'), ('C','F')])
print(dfs_recursive(g4, 'A'))
# ['A', 'B', 'D', 'E', 'C', 'F'] — follows neighbors in list order
```

**Checkpoint:** Both `dfs_iterative` and `dfs_recursive` visit all 6 nodes. Recursive DFS follows the first neighbor in each list before backtracking.

---

### 2.3 — Connected Components

```python
def count_components(graph):
    """
    Count the number of connected components in an undirected graph.
    Time: O(V + E)
    """
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

Test:

```python
# One connected graph
g5 = build_undirected([('A','B'), ('B','C'), ('C','D')])
print(count_components(g5))    # 1

# Two disconnected components: {A,B,C} and {D,E}
g6 = defaultdict(list)
for u, v in [('A','B'), ('B','C')]:
    g6[u].append(v); g6[v].append(u)
for u, v in [('D','E')]:
    g6[u].append(v); g6[v].append(u)
print(count_components(g6))    # 2

# Three isolated nodes
g7 = defaultdict(list)
g7['X']; g7['Y']; g7['Z']    # create keys with empty lists
print(count_components(g7))    # 3
```

**Checkpoint:** Connected graph = 1; two components = 2; three isolated = 3.

---

### 2.4 — Topological Sort

```python
def topological_sort(graph, all_nodes):
    """
    DFS-based topological sort for a DAG.
    all_nodes: list of all vertex labels (some may have no outgoing edges).
    Returns a list in topological order.
    Time: O(V + E)
    """
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)    # post-order

    for node in all_nodes:
        if node not in visited:
            dfs(node)

    return result[::-1]
```

Test:

```python
# Course prerequisites: Math→CS101, CS101→CS201, Science→CS101
prereq_edges = [('Math','CS101'), ('CS101','CS201'), ('Science','CS101')]
pg = build_directed(prereq_edges)
all_courses = ['Math', 'Science', 'CS101', 'CS201']

order = topological_sort(pg, all_courses)
print(order)
# Valid outputs include: ['Math', 'Science', 'CS101', 'CS201']
#                     or ['Science', 'Math', 'CS101', 'CS201']

# Verify: CS101 comes after both Math and Science; CS201 comes last
assert order.index('CS101') > order.index('Math')
assert order.index('CS101') > order.index('Science')
assert order.index('CS201') > order.index('CS101')
print('Topological order verified.')
```

**Checkpoint:** Assertions pass. CS101 appears after both prerequisites; CS201 appears last.

---

## Part 3 — LeetCode Patterns

**File:** (add to `lab10_bfs_dfs.py`)

### 3.1 — Number of Islands (LeetCode #200)

```python
def num_islands(grid):
    """
    Count connected components of '1' cells in a 2D grid.
    Uses in-place DFS marking (sinks visited cells to '0').
    Time: O(m * n), Space: O(m * n) recursion depth worst case
    """
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'    # sink visited cell
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

Test:

```python
grid1 = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]
print(num_islands(grid1))    # 1

grid2 = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
print(num_islands(grid2))    # 3
```

**Checkpoint:** `grid1` = 1 island; `grid2` = 3 islands. Submit to LeetCode #200.

---

### 3.2 — Course Schedule (LeetCode #207)

```python
def can_finish(num_courses, prerequisites):
    """
    Return True if all courses can be finished (no cycle in prerequisite graph).
    Uses three-color DFS: 0=unvisited, 1=in current path, 2=done.
    Time: O(V + E)
    """
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)    # b must be taken before a

    state = [0] * num_courses

    def dfs(node):
        if state[node] == 1:    # back edge — cycle detected
            return False
        if state[node] == 2:    # already fully processed — safe
            return True
        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = 2
        return True

    return all(dfs(i) for i in range(num_courses))
```

Test:

```python
print(can_finish(2, [[1,0]]))           # True — take 0 then 1
print(can_finish(2, [[1,0],[0,1]]))     # False — circular dependency
print(can_finish(4, [[1,0],[2,1],[3,2]]))  # True — linear chain
```

**Checkpoint:** All three tests pass. Submit to LeetCode #207.

---

### 3.3 — Integration Test

```python
def test_all():
    g = build_undirected([('A','B'),('A','C'),('B','D'),('B','E'),('C','F')])

    # BFS order starts at A, visits level by level
    bfs_order = bfs(g, 'A')
    assert bfs_order[0] == 'A'
    assert set(bfs_order) == {'A','B','C','D','E','F'}

    # BFS distances
    dist = bfs_distances(g, 'A')
    assert dist['A'] == 0
    assert dist['B'] == 1
    assert dist['D'] == 2

    # DFS visits all nodes
    assert set(dfs_iterative(g, 'A')) == {'A','B','C','D','E','F'}
    assert set(dfs_recursive(g, 'A')) == {'A','B','C','D','E','F'}

    # Connected components
    assert count_components(g) == 1

    # Number of Islands
    grid = [['1','1','0'],['0','0','0'],['1','0','1']]
    assert num_islands(grid) == 3

    # Course Schedule
    assert can_finish(2, [[1,0]]) == True
    assert can_finish(2, [[1,0],[0,1]]) == False

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass. LeetCode #200 and #207 submitted.

---

## Deliverables

Submit to Canvas:

1. `lab10_bfs_dfs.py` — BFS, DFS iterative and recursive, components, topological sort, num_islands, can_finish, integration test
2. LeetCode submission screenshots for #200 and #207

---

## Summary

| Concept | Key Point |
|---|---|
| BFS | Queue (deque); mark visited on enqueue; O(V+E) |
| BFS shortest path | First time a node is reached = shortest distance |
| DFS iterative | Explicit stack; mark visited on pop |
| DFS recursive | Call stack; beware Python recursion limit (1000) |
| Connected components | One DFS/BFS per unvisited node = one component |
| Topological sort | DFS post-order reversed; only valid on DAGs |
| Kahn's algorithm | BFS from in-degree-0 nodes; detects cycles implicitly |
| Grid traversal | 4-directional neighbors; bounds check first |
| In-place marking | `grid[r][c] = '0'` avoids separate visited set |
| Three-color DFS | 0=unvisited, 1=active, 2=done; detects directed cycles |

---

## Part 9 — Challenge Exercise

These steps are **optional** and ungraded. They are designed for students who want to deepen their understanding beyond the core lab.

### 9.1 — Word Ladder (LeetCode #127)

Given a `beginWord`, `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, changing one letter at a time (each intermediate word must be in `wordList`). This is a classic BFS shortest-path problem: treat each word as a graph node and add an edge between words that differ by exactly one letter. The BFS level counts give the minimum transformation steps. Implement the solution using BFS with a set-based `wordList` for O(1) membership checks. Verify on the standard test case (`beginWord="hit"`, `endWord="cog"`, `wordList=["hot","dot","dog","lot","log","cog"]`, expected output: 5) and state why DFS cannot guarantee the minimum path length.

### 9.2 — Kahn's Topological Sort with Cycle Detection

Implement Kahn's BFS-based topological sort: compute in-degrees for all vertices, enqueue all vertices with in-degree 0, then repeatedly dequeue a vertex, add it to the result, and decrement the in-degree of all its successors (enqueuing those that reach 0). If the result contains fewer than V vertices at the end, a cycle exists. Verify on Course Schedule II (LeetCode #210) which asks for the actual topological order. Compare Kahn's algorithm with the DFS post-order approach: implement both, verify they produce valid topological orderings for the same graph, and explain in a comment why they may produce different (but equally valid) orderings.

### 9.3 — Bipartite Graph Check (LeetCode #785)

A graph is bipartite if its vertices can be split into two independent sets such that every edge connects a vertex in one set to a vertex in the other. Implement a BFS-based 2-coloring algorithm: color the source vertex with color 0, then color all unvisited neighbors with color 1, then their neighbors with color 0, etc. If any neighbor already has the same color as the current vertex, the graph is not bipartite. Verify on a cycle of even length (bipartite) and a cycle of odd length (not bipartite). State the time complexity and explain why BFS naturally implements 2-coloring level by level.
