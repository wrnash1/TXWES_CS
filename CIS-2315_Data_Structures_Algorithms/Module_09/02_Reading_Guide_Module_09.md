# Reading Guide: Module 09 — Graph Representations

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Introduction

A graph G = (V, E) is a set of vertices connected by edges. Graphs generalize trees (which are graphs with no cycles) and are the correct model for any problem involving connections, relationships, dependencies, or paths. This module covers how to represent graphs in code and the vocabulary required to reason about them. BFS and DFS algorithms follow in Module 10.

---

## 1. Graph Terminology

| Term | Definition |
|---|---|
| Vertex (node) | A point in the graph |
| Edge (arc) | A connection between two vertices |
| Directed graph | Edges have direction: u → v does not imply v → u |
| Undirected graph | Edges are bidirectional: u-v and v-u are the same edge |
| Weighted graph | Each edge has a numerical weight |
| Degree | Number of edges touching a vertex |
| In-degree | Number of edges arriving at a vertex (directed graphs) |
| Out-degree | Number of edges leaving a vertex (directed graphs) |
| Path | A sequence of vertices connected by edges |
| Cycle | A path that starts and ends at the same vertex |
| Connected | Every vertex reachable from every other (undirected) |
| Strongly connected | Every vertex reachable from every other in both directions (directed) |
| Connected component | A maximal connected subgraph |
| Tree | Connected acyclic undirected graph with exactly V-1 edges |
| DAG | Directed Acyclic Graph — no cycles; used for dependency ordering |

---

## 2. Adjacency List

The adjacency list maps each vertex to the list of its neighbors. It is the standard representation for interview problems.

### Undirected Graph

```python
from collections import defaultdict

def build_undirected(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    # both directions
    return graph

edges = [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')]
g = build_undirected(edges)
# g['A'] = ['B', 'C']
# g['D'] = ['B', 'C', 'E']
```

### Directed Graph

```python
def build_directed(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)    # only forward direction
    return graph
```

### Weighted Graph

Store `(neighbor, weight)` tuples:

```python
def build_weighted(edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))    # omit for directed
    return graph
```

### Complexity

- Space: O(V + E)
- Add edge: O(1) amortized
- Check edge (u, v): O(degree(u))
- Iterate neighbors of u: O(degree(u))

Best for: sparse graphs, most interview problems.

---

## 3. Adjacency Matrix

A V×V array where `matrix[i][j]` is 1 (or the edge weight) if edge i→j exists, else 0.

```python
def build_matrix(n, edges, directed=False):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix
```

For weighted graphs, store the weight value; use `float('inf')` for absent edges.

### Properties

- Undirected graph: matrix is symmetric (`matrix[i][j] == matrix[j][i]`)
- Check edge (u, v): O(1)
- Iterate all neighbors of u: O(V) — must scan entire row

### Matrix Complexity

- Space: O(V²) — always
- Check edge: O(1)
- Iterate neighbors: O(V)

Best for: dense graphs, algorithms that require O(1) edge existence checks (Floyd-Warshall).

---

## 4. Comparison: Adjacency List vs. Adjacency Matrix

| Property | Adjacency List | Adjacency Matrix |
|---|---|---|
| Space | O(V + E) | O(V²) |
| Add edge | O(1) | O(1) |
| Check edge (u, v) | O(deg(u)) | O(1) |
| Iterate neighbors | O(deg(u)) | O(V) |
| Best for | Sparse graphs | Dense graphs |
| Interview default | Yes | No (unless graph is dense) |

---

## 5. Degree and Graph Properties

### Degree (Undirected)

```python
def degree(graph, vertex):
    return len(graph[vertex])
```

### In-degree and Out-degree (Directed)

```python
def out_degree(graph, vertex):
    return len(graph[vertex])

def in_degree(graph, vertex):
    return sum(1 for neighbors in graph.values() for n in neighbors if n == vertex)
```

### Connectivity Check (Undirected)

```python
def is_connected(graph):
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

---

## 6. Cycle Detection

### Undirected Graph (DFS with Parent Tracking)

A back edge to any node other than the direct parent indicates a cycle:

```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:    # back edge
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

### Directed Graph (DFS with Recursion Stack)

A back edge to a node currently in the recursion stack (currently being processed) indicates a cycle:

```python
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:    # back edge in directed graph
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```

---

## 7. Interview Tips

1. **Always clarify directed vs. undirected** — in problems like "Number of Islands," the graph is implicit (grid) and undirected. In "Course Schedule," the graph is directed (prerequisites).

2. **Use `defaultdict(list)` for adjacency lists** — avoids `KeyError` when accessing nodes with no outgoing edges, which simplifies BFS/DFS code.

3. **For grid problems, the graph is implicit** — model cells as nodes and cardinal neighbors (up/down/left/right) as edges. Build the graph on the fly during traversal rather than constructing an explicit adjacency list.

4. **Adjacency matrix means O(1) edge check** — if an algorithm requires "does edge (u,v) exist?" repeatedly, the matrix is the right choice. Otherwise, default to adjacency list.

5. **V and E matter for complexity** — "O(V + E)" is not the same as "O(n)." For a dense graph, E can be O(V²), making O(V + E) = O(V²). Always state complexity in terms of V and E.

6. **Isolated vertices:** a vertex with no edges may not appear in an adjacency list built from edge lists alone. Add it explicitly if needed: `graph[vertex]` with `defaultdict(list)` creates an empty list without error.

7. **Trees are graphs** — a tree is a connected acyclic undirected graph with V-1 edges. Tree traversal algorithms are special cases of graph traversal with no `visited` set needed (trees have no cycles).

8. **DAGs power dependency resolution** — topological sort (Module 10) works only on DAGs. If the problem involves ordering with prerequisites, the graph is a DAG and cycle detection matters.

---

## 8. Study Checklist

- [ ] Watch the Module 09 video lecture by Professor Nash.
- [ ] Build an undirected adjacency list from an edge list.
- [ ] Build a directed adjacency list and compute in-degree for each vertex.
- [ ] Build an adjacency matrix and verify the symmetric property for undirected graphs.
- [ ] Implement the degree function for both directed and undirected graphs.
- [ ] Implement and test `is_connected` on a connected graph and a disconnected graph.
- [ ] Implement `has_cycle_undirected` and test on a graph with a cycle and a tree.
- [ ] Complete the Module 09 Lab.
- [ ] Complete the Module 09 Quiz.
