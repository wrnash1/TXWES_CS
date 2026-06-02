# Video Script: CIS-2315 — Data Structures & Algorithms

## Module 09 — Graph Representations

**Estimated Duration:** 22–26 minutes
**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

> **PRODUCTION NOTES FOR INSTRUCTOR:**
>
> - Use VS Code + Python terminal for all [DEMO] sections.
> - [PAUSE] = 2 seconds of silence.
> - Draw the graph as a diagram first (nodes as circles, edges as lines or arrows), then show how it maps to an adjacency list and adjacency matrix.
> - Always show both directed and undirected versions side-by-side for the same example graph.
> - Weighted vs. unweighted: introduce weights in the adjacency list as tuples `(neighbor, weight)`.
> - The adjacency list is the dominant representation in interview problems. Emphasize that Python's `defaultdict(list)` is the standard way to build one.
> - Common mistakes: forgetting to add both directions for undirected graphs, confusing directed and undirected degrees, using an adjacency matrix for sparse graphs (O(V²) space waste).
> - Vocabulary matters: vertex/node, edge/arc, directed/undirected, weighted/unweighted, degree, path, cycle, connected component.

---

## [00:00 – 01:30] Opening

**[INSTRUCTOR ON CAMERA — Title card: "Module 09 | Graph Representations | CIS-2315"]**

"Graphs are the most general data structure in computer science. A linked list is a special graph. A tree is a special graph. A grid is a special graph. Social networks, road maps, airline routes, dependency systems, the internet — all of these are graphs. This module covers the two primary ways to represent a graph in code — adjacency lists and adjacency matrices — and the vocabulary you need to describe and reason about graphs. The next two modules will add BFS, DFS, and shortest-path algorithms. Everything starts with representation."

---

## [01:30 – 07:00] Part 1 — Graph Vocabulary and Types

**[SHOW SLIDE: "Graph Terminology"]**

"A **graph** G = (V, E) consists of a set of **vertices** (also called nodes) and a set of **edges** (also called arcs) connecting pairs of vertices.

**[SHOW DIAGRAM: 5-node undirected graph with edges A-B, A-C, B-D, C-D, D-E]**

```text
    A --- B
    |     |
    C --- D --- E
```

Vocabulary you must know:

- **Directed graph (digraph):** edges have direction. An edge from A to B does not imply an edge from B to A.
- **Undirected graph:** edges have no direction. A-B and B-A are the same edge.
- **Weighted graph:** each edge has a numerical weight (distance, cost, time).
- **Degree:** the number of edges touching a vertex. In a directed graph, distinguish in-degree (edges arriving) from out-degree (edges leaving).
- **Path:** a sequence of vertices connected by edges.
- **Cycle:** a path that starts and ends at the same vertex.
- **Connected graph:** every vertex can reach every other vertex (undirected). Strongly connected (directed): every vertex can reach every other vertex in both directions.
- **Connected component:** a maximal subgraph in which every vertex is reachable from every other.
- **Tree:** a connected, acyclic undirected graph with V-1 edges.
- **DAG (Directed Acyclic Graph):** a directed graph with no cycles. Used in dependency resolution and topological sort.

[PAUSE]

For interview problems, you will almost always receive a graph as either:

1. An **edge list**: a list of `(u, v)` or `(u, v, weight)` tuples.
2. An **adjacency list**: a dict or list mapping each vertex to its neighbors.
3. A **2D grid**: an implicit graph where adjacent cells are connected."

---

## [07:00 – 14:00] Part 2 — Adjacency List Representation

**[SHOW SLIDE: "Adjacency List — The Standard Interview Representation"]**

"The **adjacency list** represents a graph as a mapping from each vertex to the list of its neighbors.

For the undirected graph A-B, A-C, B-D, C-D, D-E:

```python
from collections import defaultdict

graph = defaultdict(list)

# Add undirected edges — both directions
edges = [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(dict(graph))
# {'A': ['B','C'], 'B': ['A','D'], 'C': ['A','D'], 'D': ['B','C','E'], 'E': ['D']}
```

For a **directed** graph, add only the forward edge:

```python
def build_directed(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)    # only u → v, not v → u
    return graph
```

For a **weighted** graph, store tuples `(neighbor, weight)`:

```python
def build_weighted(edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))    # omit for directed
    return graph
```

**[DEMO: build weighted graph from `[('A','B',4), ('A','C',2), ('B','C',1)]`]**

[PAUSE]

**Space complexity:** O(V + E) — one entry per vertex plus one entry per edge endpoint. For sparse graphs (few edges), this is much more memory-efficient than a matrix.

**Time complexity of common operations:**

- Add edge: O(1) amortized
- Check edge (u, v): O(degree(u)) — must scan u's neighbor list
- Get all neighbors of u: O(1) — direct list access, iterate in O(degree(u))

**When to use adjacency list:**

- Most interview problems
- Sparse graphs (E << V²)
- When you need to iterate over neighbors frequently"

---

## [14:00 – 19:00] Part 3 — Adjacency Matrix Representation

**[SHOW SLIDE: "Adjacency Matrix — V×V Grid"]**

"The **adjacency matrix** represents a graph as a V×V boolean (or weight) matrix. `matrix[i][j] = 1` if there is an edge from vertex i to vertex j; 0 otherwise.

For the same 5-node graph with vertices indexed A=0, B=1, C=2, D=3, E=4:

```python
def build_matrix(n_vertices, edges, directed=False):
    matrix = [[0] * n_vertices for _ in range(n_vertices)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix

# Example: 4-vertex directed graph
# Edges: 0→1, 0→2, 1→3, 2→3
matrix = build_matrix(4, [(0,1),(0,2),(1,3),(2,3)], directed=True)
for row in matrix:
    print(row)
# [0, 1, 1, 0]
# [0, 0, 0, 1]
# [0, 0, 0, 1]
# [0, 0, 0, 0]
```

**[DEMO: show the matrix for the 4-vertex example above]**

[PAUSE]

**Properties of the adjacency matrix:**

- **Undirected graph:** matrix is symmetric (`matrix[i][j] == matrix[j][i]`)
- **Weighted graph:** store weight instead of 1; use `float('inf')` for no edge
- **Check edge (u, v):** O(1) — direct array access
- **All neighbors of u:** O(V) — must scan entire row even if degree is small
- **Space:** O(V²) — always, regardless of number of edges

**When to use adjacency matrix:**

- Dense graphs (E close to V²)
- When O(1) edge existence check is critical
- Floyd-Warshall all-pairs shortest path uses a matrix by design

[PAUSE]

**Comparison table:**

```text
                    Adjacency List    Adjacency Matrix
Space               O(V + E)          O(V²)
Add edge            O(1)              O(1)
Check edge (u,v)    O(deg(u))         O(1)
Neighbors of u      O(deg(u))         O(V)
Best for            Sparse graphs     Dense graphs
```"

---

## [19:00 – 23:00] Part 4 — Graph Properties and Helper Functions

**[SHOW SLIDE: "Degree, Connected Components, and Cycle Detection"]**

"Several graph properties come up often in interviews. Here are the key helper operations.

**Degree of a vertex:**

```python
def degree(graph, vertex):
    return len(graph[vertex])

# In-degree for a directed graph requires scanning all adjacency lists:
def in_degree(graph, vertex):
    return sum(1 for neighbors in graph.values() for n in neighbors if n == vertex)
```

**Check if a graph is connected (undirected):**

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

[PAUSE]

**Detecting a cycle in an undirected graph (DFS):**

```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:    # back edge — cycle found
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

The key insight: in an undirected graph, a back edge to any node other than the direct parent indicates a cycle.

**[DEMO: run has_cycle_undirected on a graph with cycle A-B-C-A and confirm True; run on a tree and confirm False]**

The Module 09 lab walks through building adjacency lists from edge lists, implementing degree functions, and testing connectivity and cycle detection on several example graphs."

---

**[END CARD: Texas Wesleyan University | CIS-2315 Data Structures & Algorithms | Module 09 — Graph Representations]**

---

## Additional Resources

- [VisuAlgo — Graph Visualization](https://visualgo.net/en/graphds)
- [NeetCode — Graphs](https://www.youtube.com/watch?v=tWVWeAqZ0WU)
- [LeetCode #200 — Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [LeetCode #207 — Course Schedule](https://leetcode.com/problems/course-schedule/)
- [LeetCode #133 — Clone Graph](https://leetcode.com/problems/clone-graph/)
