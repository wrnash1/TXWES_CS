# Lab Activity: Module 09 — Graph Representations

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Overview

This lab has three parts:

- **Part 1** — Build adjacency lists from edge lists (undirected, directed, weighted)
- **Part 2** — Build adjacency matrices and compare with adjacency lists
- **Part 3** — Degree functions, connectivity check, and cycle detection

**Lab environment:** Python 3 (VS Code terminal or any Python REPL).

---

## Part 1 — Adjacency List Representations

**File:** `lab09_graph.py`

### 1.1 — Undirected Graph

```python
from collections import defaultdict

def build_undirected(edges):
    """
    Build an undirected adjacency list from a list of (u, v) edge tuples.
    Each edge is added in both directions.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
```

Test:

```python
edges = [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')]
g = build_undirected(edges)

print(dict(g))
# Expected (order within lists may vary):
# {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}

print(g['A'])    # ['B', 'C']
print(g['D'])    # ['B', 'C', 'E']
print(g['E'])    # ['D']
```

**Checkpoint:** Every edge appears in both directions. `g['A']` contains `'B'` and `'C'`; `g['B']` contains `'A'` and `'D'`.

---

### 1.2 — Directed Graph

```python
def build_directed(edges):
    """
    Build a directed adjacency list.
    Each edge (u, v) adds only u → v.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph
```

Test:

```python
# Directed edges: 0→1, 0→2, 1→3, 2→3, 3→4
directed_edges = [(0,1),(0,2),(1,3),(2,3),(3,4)]
dg = build_directed(directed_edges)

print(dict(dg))
# {0: [1, 2], 1: [3], 2: [3], 3: [4]}
# Note: node 4 has no outgoing edges — not in dict (defaultdict returns [] on access)

print(dg[4])    # [] — no outgoing edges, but no KeyError with defaultdict
```

**Checkpoint:** Node 4 has no entry in the dict (no outgoing edges), but `dg[4]` returns `[]` rather than raising `KeyError`.

---

### 1.3 — Weighted Graph

```python
def build_weighted(edges):
    """
    Build an undirected weighted adjacency list.
    Each entry in the list is a (neighbor, weight) tuple.
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph
```

Test:

```python
weighted_edges = [('A','B',4), ('A','C',2), ('B','C',1), ('C','D',7)]
wg = build_weighted(weighted_edges)

print(wg['A'])    # [('B', 4), ('C', 2)]
print(wg['C'])    # [('A', 2), ('B', 1), ('D', 7)]

# Iterate over neighbors and weights:
for neighbor, weight in wg['A']:
    print(f'  A → {neighbor} (weight {weight})')
# A → B (weight 4)
# A → C (weight 2)
```

**Checkpoint:** Each edge appears with its weight. Accessing `wg['A']` gives a list of `(neighbor, weight)` tuples.

---

## Part 2 — Adjacency Matrix

**File:** (add to `lab09_graph.py`)

### 2.1 — Build and Inspect

```python
def build_matrix(n, edges, directed=False):
    """
    Build an adjacency matrix for a graph with n vertices (0-indexed).
    """
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)
```

Test — undirected:

```python
# 4-vertex undirected graph: 0-1, 0-2, 1-3, 2-3
m_undirected = build_matrix(4, [(0,1),(0,2),(1,3),(2,3)])
print_matrix(m_undirected)
# [0, 1, 1, 0]
# [1, 0, 0, 1]
# [1, 0, 0, 1]
# [0, 1, 1, 0]
```

Test — directed:

```python
# Same edges but directed
m_directed = build_matrix(4, [(0,1),(0,2),(1,3),(2,3)], directed=True)
print_matrix(m_directed)
# [0, 1, 1, 0]
# [0, 0, 0, 1]
# [0, 0, 0, 1]
# [0, 0, 0, 0]
```

**Checkpoint:** The undirected matrix is symmetric (row i = column i transposed). The directed matrix is not symmetric.

---

### 2.2 — Edge Check Comparison

```python
# Build the same graph as both an adjacency list and a matrix
adj_edges = [(0,1),(0,2),(1,3),(2,3)]
adj_list = build_directed(adj_edges)
adj_mat  = build_matrix(4, adj_edges, directed=True)

# Check if edge 1→3 exists
print(3 in adj_list[1])        # True — O(degree) scan
print(adj_mat[1][3] == 1)      # True — O(1) direct access

# Check if edge 3→0 exists
print(0 in adj_list[3])        # False
print(adj_mat[3][0] == 1)      # False
```

**Checkpoint:** Both representations agree on edge existence. Note that the matrix check is O(1) while the list check is O(degree).

---

## Part 3 — Graph Properties

**File:** (add to `lab09_graph.py`)

### 3.1 — Degree Functions

```python
def degree(graph, vertex):
    """Degree of a vertex in an undirected graph."""
    return len(graph[vertex])

def out_degree(graph, vertex):
    """Out-degree of a vertex in a directed graph."""
    return len(graph[vertex])

def in_degree(graph, vertex):
    """In-degree of a vertex in a directed graph — O(V + E)."""
    return sum(1 for neighbors in graph.values() for n in neighbors if n == vertex)
```

Test:

```python
dg2 = build_directed([(0,1),(0,2),(1,3),(2,3),(3,4)])

print(out_degree(dg2, 0))    # 2 — edges to 1 and 2
print(out_degree(dg2, 4))    # 0 — no outgoing edges
print(in_degree(dg2, 3))     # 2 — edges from 1 and 2
print(in_degree(dg2, 0))     # 0 — nothing points to 0
```

**Checkpoint:** Out-degree of 0 = 2; in-degree of 3 = 2.

---

### 3.2 — Connectivity Check

```python
def is_connected(graph):
    """
    Return True if the undirected graph is connected.
    Uses iterative DFS from an arbitrary start node.
    """
    if not graph:
        return True
    start = next(iter(graph))
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return len(visited) == len(graph)
```

Test:

```python
# Connected graph
g_connected = build_undirected([('A','B'),('B','C'),('C','D')])
print(is_connected(g_connected))    # True

# Disconnected graph — two separate components: {A,B} and {C,D}
g_disconnected = defaultdict(list)
g_disconnected['A'].append('B')
g_disconnected['B'].append('A')
g_disconnected['C'].append('D')
g_disconnected['D'].append('C')
print(is_connected(g_disconnected))    # False
```

**Checkpoint:** Connected graph returns `True`; disconnected returns `False`.

---

### 3.3 — Cycle Detection (Undirected)

```python
def has_cycle_undirected(graph):
    """
    Return True if the undirected graph contains a cycle.
    Back edge = edge to a visited node that is not the direct parent.
    """
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:    # back edge → cycle
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

Test:

```python
# Graph with cycle: A-B-C-A
g_cycle = build_undirected([('A','B'),('B','C'),('C','A')])
print(has_cycle_undirected(g_cycle))     # True

# Tree (no cycle): A-B-C (path)
g_tree = build_undirected([('A','B'),('B','C')])
print(has_cycle_undirected(g_tree))      # False

# More complex: star graph (no cycle)
g_star = build_undirected([('X','A'),('X','B'),('X','C'),('X','D')])
print(has_cycle_undirected(g_star))      # False
```

**Checkpoint:** Cycle graph returns `True`; path and star graphs return `False`.

---

### 3.4 — Integration Test

```python
def test_all():
    # Undirected adjacency list
    g = build_undirected([('A','B'),('A','C'),('B','D')])
    assert 'B' in g['A']
    assert 'A' in g['B']
    assert len(g['B']) == 2    # connected to A and D

    # Directed graph
    dg = build_directed([(0,1),(1,2),(2,3)])
    assert 1 in dg[0]
    assert 0 not in dg[1]    # directed — no back edge

    # Matrix
    m = build_matrix(3, [(0,1),(1,2)])
    assert m[0][1] == 1
    assert m[1][0] == 1    # undirected — symmetric
    assert m[0][2] == 0    # no direct edge

    # Connectivity
    assert is_connected(build_undirected([('A','B'),('B','C')])) == True
    disc = defaultdict(list)
    disc['A']; disc['B']   # two isolated vertices
    assert is_connected(disc) == False

    # Cycle detection
    assert has_cycle_undirected(build_undirected([('A','B'),('B','C'),('C','A')])) == True
    assert has_cycle_undirected(build_undirected([('A','B'),('B','C')])) == False

    print('All assertions passed.')

test_all()
```

**Checkpoint:** All assertions pass.

---

## Deliverables

Submit to Canvas:

1. `lab09_graph.py` — all build functions, matrix, degree, connectivity, cycle detection, integration test
2. Short written answer (3–5 sentences): For the graph `[(0,1),(0,2),(1,3),(2,3),(3,4)]`, which representation would you choose if the algorithm needs to check edge existence for every pair of vertices? Why?

---

## Summary

| Concept | Key Point |
|---|---|
| Adjacency list | `defaultdict(list)`; O(V+E) space; default for interviews |
| Adjacency matrix | V×V array; O(V²) space; O(1) edge check |
| Undirected graph | Add both u→v and v→u |
| Weighted graph | Store `(neighbor, weight)` tuples |
| Degree | `len(graph[vertex])` |
| In-degree | Scan all neighbor lists — O(V+E) |
| Connectivity | BFS/DFS from start; visited count == vertex count |
| Cycle (undirected) | Back edge to visited node that is not parent |
| `defaultdict` advantage | No `KeyError` for nodes with no outgoing edges |
