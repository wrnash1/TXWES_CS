# Quiz: Module 09 — Graph Representations

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

What is the space complexity of an adjacency list for a graph with V vertices and E edges?

- A) O(V²)
- B) O(V + E)
- C) O(E²)
- D) O(V · E)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(V²) is the space complexity of an adjacency matrix — a fixed V×V grid regardless of how many edges exist. An adjacency list only stores what is actually present.
- *Why B is correct:* An adjacency list allocates one entry per vertex (O(V) total) and one entry per edge endpoint (O(E) for directed, O(2E) for undirected — still O(E)). Total: O(V + E). For sparse graphs where E << V², this is far more efficient than a matrix.
- *Why C is incorrect:* O(E²) has no basis in graph representation. No standard structure requires squaring the edge count.
- *Why D is incorrect:* O(V · E) would imply storing each vertex's information for every edge, which no standard representation does. This is an overcount with no structural basis.

---

### Question 2

In a directed graph, what is the difference between **in-degree** and **out-degree** of a vertex?

- A) In-degree counts all adjacent vertices; out-degree counts only reachable vertices
- B) In-degree is the number of edges arriving at the vertex; out-degree is the number of edges leaving it
- C) In-degree applies to source nodes; out-degree applies to sink nodes
- D) In-degree and out-degree are the same in a directed graph

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* "All adjacent vertices" and "reachable vertices" are different concepts, and neither correctly defines in-degree. In-degree specifically counts edges that terminate at the vertex.
- *Why B is correct:* In-degree = number of edges whose head is at this vertex (edges arriving). Out-degree = number of edges whose tail is at this vertex (edges leaving). In the adjacency list, out-degree is `len(graph[v])`; in-degree requires scanning all neighbor lists.
- *Why C is incorrect:* Source nodes (in-degree = 0) and sink nodes (out-degree = 0) are special cases, but in-degree and out-degree are defined for every vertex, not restricted to sources and sinks.
- *Why D is incorrect:* In an undirected graph, in-degree and out-degree are equal (both = degree). In a directed graph, they can differ. For example, a vertex with three incoming edges and one outgoing edge has in-degree 3 and out-degree 1.

---

### Question 3

For the undirected graph built from edges `[('A','B'), ('B','C'), ('C','A')]`, which of the following correctly describes the adjacency list entry for vertex `'B'`?

- A) `['A']` — B points only to A (the first edge added)
- B) `['B']` — a vertex points to itself
- C) `['A', 'C']` — B is connected to both A and C
- D) `['A', 'C', 'B']` — includes a self-loop

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Edge `('A','B')` adds B to A's list and A to B's list. Edge `('B','C')` then adds C to B's list and B to C's list. B ends up with both A and C as neighbors.
- *Why B is incorrect:* There are no self-loops in this graph. Self-loops (`('B','B')`) would add B to its own list, but none of the three edges involve the same vertex twice.
- *Why C is correct:* From edge `('A','B')`: `graph['B'].append('A')` → B's list is `['A']`. From edge `('B','C')`: `graph['B'].append('C')` → B's list is `['A', 'C']`. The edge `('C','A')` does not involve B.
- *Why D is incorrect:* B does not appear in its own neighbor list unless there is a self-loop. The graph `A-B-C-A` is a triangle with no self-loops.

---

### Question 4

An adjacency matrix for an undirected graph is always **symmetric**. What does this mean, and why is it true?

- A) The matrix has equal numbers of 0s and 1s
- B) `matrix[i][j] == matrix[j][i]` for all i and j — because an undirected edge between i and j exists in both directions
- C) The matrix is square with equal row and column sums
- D) The diagonal entries are all 1, representing self-connections

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Having equal numbers of 0s and 1s is not a property of undirected graph matrices. A sparse graph has far more 0s than 1s, yet is still symmetric.
- *Why B is correct:* An undirected edge between vertex i and vertex j means "i is connected to j" and "j is connected to i." When building the matrix, both `matrix[i][j] = 1` and `matrix[j][i] = 1` are set. Therefore `matrix[i][j] == matrix[j][i]` for every pair — the matrix mirrors itself across the main diagonal.
- *Why C is incorrect:* Equal row and column sums would mean every vertex has the same degree — a regular graph. Symmetry is a stronger statement about the mirror relationship of individual entries, not row/column totals.
- *Why D is incorrect:* Diagonal entries `matrix[i][i]` represent self-loops. Most graphs have no self-loops, so diagonal entries are typically 0. Symmetry refers to off-diagonal mirroring, not the diagonal itself.

---

### Question 5

Which of the following graph representations allows checking whether a specific edge (u, v) exists in **O(1)** time?

- A) Adjacency list
- B) Adjacency matrix
- C) Edge list (unsorted)
- D) Linked list of vertices

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* In an adjacency list, checking whether v is a neighbor of u requires scanning u's neighbor list — O(degree(u)). In the worst case, this is O(V).
- *Why B is correct:* An adjacency matrix stores edge existence at a fixed index: `matrix[u][v]` is a direct array access — O(1). This is the primary advantage of the matrix representation.
- *Why C is incorrect:* An unsorted edge list requires scanning all edges to find (u, v) — O(E). A sorted edge list with binary search would be O(log E), still not O(1).
- *Why D is incorrect:* A linked list of vertices has no direct index addressing. Finding vertex u requires O(V) traversal, and then finding its neighbor v requires additional scanning.

---

### Question 6

In the cycle detection algorithm for **undirected** graphs, a cycle is identified when DFS encounters a neighbor that is already visited and is **not the direct parent**. Why is the "not the direct parent" condition necessary?

- A) To avoid counting the starting vertex as a cycle
- B) Because undirected edges appear in both directions — without this check, every edge would appear to be a back edge
- C) To prevent infinite recursion when the graph has no cycle
- D) Because directed edges only go one way, so parent tracking is unnecessary

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The starting vertex is not an issue — DFS begins there and moves to unvisited nodes. The parent condition is about the immediate predecessor, not the starting vertex.
- *Why B is correct:* In an undirected graph, edge A-B is stored as both `graph['A']` containing `'B'` and `graph['B']` containing `'A'`. When DFS visits B from A, A is already visited — but that is just the edge we came from, not a cycle. Without the `neighbor != parent` check, every undirected edge would incorrectly trigger the "back edge = cycle" condition.
- *Why C is incorrect:* Infinite recursion is prevented by the `visited` set, not by parent tracking. Marking nodes as visited ensures each node is processed only once.
- *Why D is incorrect:* This is cycle detection for undirected graphs, not directed. The parent condition is necessary precisely because undirected edges appear in both directions.

---

### Question 7

A graph has V = 1000 vertices and E = 1500 edges (sparse). What is the memory difference between storing it as an adjacency list versus an adjacency matrix?

- A) The adjacency list uses more memory because it stores neighbor pointers
- B) Both use the same memory — O(V + E) in both cases
- C) The adjacency matrix uses roughly 665 times more memory than the adjacency list
- D) The adjacency list uses O(V²) memory; the matrix uses O(V + E)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* For sparse graphs, the adjacency list uses dramatically less memory. The claim that pointer storage makes it larger is false — the list stores exactly the edges that exist.
- *Why B is incorrect:* The matrix always uses O(V²) regardless of edge count. For sparse graphs, O(V + E) << O(V²).
- *Why C is correct:* Adjacency list: O(V + E) = O(1000 + 1500) = O(2500) entries. Adjacency matrix: O(V²) = O(1,000,000) entries. Ratio ≈ 1,000,000 / 2,500 = 400. More precisely, the matrix uses about 400× more memory than the list for this graph. Option C ("roughly 665 times") reflects the ratio V² / (V + E) = 1,000,000 / 1,500 for E-only count ≈ 667. The point is: the matrix is dramatically larger for sparse graphs.
- *Why D is incorrect:* The descriptions are swapped. The adjacency list uses O(V + E); the matrix uses O(V²).

---

### Question 8

Python's `collections.defaultdict(list)` is commonly used to build adjacency lists. What happens when you access `graph[node]` for a node that has no outgoing edges and was never explicitly added?

- A) A `KeyError` is raised
- B) `None` is returned
- C) An empty list `[]` is returned and the key is added to the dict
- D) `0` is returned (default integer value)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `KeyError` is what a plain `dict` raises for missing keys. `defaultdict` suppresses this by calling the factory function instead.
- *Why B is incorrect:* `None` is the default for `dict.get(key)` when no default is specified, or for `defaultdict(lambda: None)`. `defaultdict(list)` uses `list` as the factory, which returns `[]`.
- *Why C is correct:* `defaultdict(list)` calls `list()` (which returns `[]`) whenever a missing key is accessed. The empty list is inserted into the dict and returned. For graph traversal, this means `for neighbor in graph[isolated_node]` iterates zero times without raising an error — clean and correct.
- *Why D is incorrect:* `0` is the default for `defaultdict(int)`. `defaultdict(list)` uses `list` as the factory, not `int`.

---

### Question 9

Which type of graph is a prerequisite (dependency) system — where task A must be completed before task B — most accurately modeled as?

- A) Undirected weighted graph
- B) Directed Acyclic Graph (DAG)
- C) Undirected connected graph
- D) Complete graph

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A dependency is directional (A before B is not the same as B before A), so the graph must be directed. Undirected edges imply mutual relationships, not ordering.
- *Why B is correct:* A dependency system is directed (A → B means "A before B") and must be acyclic (a cycle would mean A depends on B depends on A — an impossible circular dependency). DAGs are the canonical model for build systems (Make, Gradle), course prerequisites, task schedulers, and package managers.
- *Why C is incorrect:* Undirected removes the "before/after" directionality. Connected means every task is reachable from every other — which is not required (independent tasks may exist in different components).
- *Why D is incorrect:* A complete graph has edges between every pair of vertices — implying every task depends on every other, which makes the system impossible to complete.

---

### Question 10

In the adjacency list for the directed graph built from `[(0,1),(0,2),(1,3),(2,3)]`, what is the in-degree of vertex `3`?

- A) 0
- B) 1
- C) 2
- D) 4

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Vertex 3 appears as a destination in two edges: `1→3` and `2→3`. In-degree 0 would mean no edges point to vertex 3.
- *Why B is incorrect:* In-degree 1 would mean exactly one edge points to vertex 3. Both vertex 1 and vertex 2 have edges directed toward 3.
- *Why C is correct:* Counting all edges whose destination is 3: edge `(1,3)` and edge `(2,3)` — exactly 2 edges arrive at vertex 3. In-degree = 2. To compute this from an adjacency list, scan every neighbor list for occurrences of 3: `dg[0]=[1,2]` (no 3), `dg[1]=[3]` (one 3), `dg[2]=[3]` (one 3) — total 2.
- *Why D is incorrect:* The graph has only 4 edges total. In-degree 4 would require all 4 edges to point to vertex 3, which is not the case.

---

### Question 11

**Each question is worth 5 points.**

For a graph with V vertices and E edges stored as an adjacency matrix, what is the space complexity?

- A) O(E)
- B) O(V)
- C) O(V + E)
- D) O(V²)

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* O(E) is the space of an edge list representation. An adjacency matrix allocates a V×V array regardless of how many edges exist. For a sparse graph (E << V²), an adjacency matrix wastes enormous space.
- *Why B is incorrect:* O(V) would be the space of a vertex list only. The adjacency matrix stores a relationship for every pair of vertices — V rows times V columns.
- *Why C is incorrect:* O(V + E) is the space of an adjacency list. Adjacency lists store exactly E edge references plus V vertex entries, making them space-efficient for sparse graphs.
- *Why D is correct:* An adjacency matrix is a V×V boolean (or weight) array. Regardless of the number of edges, every cell `matrix[i][j]` exists for all pairs (i, j). Total cells = V × V = V². For large sparse graphs, this is highly inefficient — a social network with 1 billion users would require a 10¹⁸-cell matrix.

---

### Question 12

In an undirected graph represented as an adjacency list, what property must hold for each edge (u, v)?

- A) `v` appears in `graph[u]` only
- B) Both `v` appears in `graph[u]` AND `u` appears in `graph[v]`
- C) `u` appears in `graph[v]` only, not `graph[u]`
- D) The edge is stored once in a separate edge set, not in the adjacency list

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Storing only `v` in `graph[u]` would make the graph directed (from u to v only). An undirected edge means you can traverse from u to v and from v to u — both directions must be represented.
- *Why B is correct:* An undirected edge (u, v) is stored twice: `graph[u].append(v)` and `graph[v].append(u)`. This allows traversal in both directions. As a consequence, an undirected graph with E edges stores 2E entries in the adjacency list.
- *Why C is incorrect:* Storing `u` in `graph[v]` only without `v` in `graph[u]` would make the edge directed from v to u. Undirected requires symmetry.
- *Why D is incorrect:* A separate edge set is the edge list representation, not the adjacency list representation. In an adjacency list, edges are embedded in each vertex's neighbor list.

---

### Question 13

Which graph representation is most efficient for the operation "list all neighbors of vertex v"?

- A) Adjacency matrix — scan row v for non-zero entries
- B) Edge list — scan all edges for those containing v
- C) Adjacency list — directly iterate over `graph[v]`
- D) Both adjacency matrix and adjacency list are equivalent for this operation

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* To find all neighbors in an adjacency matrix, you must scan the entire row v — O(V) time even if v has only one neighbor. For sparse graphs, most of these checks return 0 (no edge), wasting time.
- *Why B is incorrect:* To find all neighbors of v in an edge list, you must scan every edge looking for those containing v — O(E) time. For dense graphs, E = O(V²), making this very slow.
- *Why C is correct:* An adjacency list stores exactly the neighbors of v at `graph[v]`. Iterating over them costs O(degree(v)) — proportional to the number of actual neighbors. This is optimal — you must visit every neighbor at least once.
- *Why D is incorrect:* Adjacency matrix is O(V) per neighbor query; adjacency list is O(degree(v)). For sparse graphs, degree(v) << V, making the adjacency list dramatically faster.

---

### Question 14

What is the maximum number of edges in a simple directed graph with V vertices (no self-loops, at most one directed edge per pair)?

- A) V
- B) V(V-1)/2
- C) V(V-1)
- D) V²

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* V edges would be a very sparse graph (a ring or a chain). The maximum number of edges in a directed graph is much larger.
- *Why B is incorrect:* V(V-1)/2 is the maximum number of edges in a simple undirected graph. In an undirected graph, edge (u,v) and edge (v,u) are the same. In a directed graph, they are different.
- *Why C is correct:* In a simple directed graph, for each ordered pair (u, v) where u ≠ v, there can be at most one directed edge u→v. The number of ordered pairs is V × (V-1) (V choices for source, V-1 choices for destination excluding self-loops). Maximum edges = V(V-1).
- *Why D is incorrect:* V² includes self-loops (V edges of the form u→u). For simple graphs (no self-loops), the maximum is V(V-1) = V² − V.

---

### Question 15

A graph has V vertices and E edges. What is the time complexity of building its adjacency list from a list of edge pairs?

- A) O(V)
- B) O(E)
- C) O(V + E)
- D) O(V × E)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(V) would be sufficient only if you initialize empty vertex entries. But processing all E edges requires at least O(E) additional work.
- *Why B is incorrect:* O(E) covers processing all edges but doesn't account for initializing the adjacency list structure with V vertex entries. For a graph with isolated vertices (no edges), initialization is O(V) even with E = 0.
- *Why C is correct:* Building an adjacency list requires two phases: initialize V vertex entries (O(V)) and process E edge pairs by appending to the appropriate neighbor lists (O(E)). Total: O(V + E). This is also the standard time complexity stated for most graph algorithms — "O(V + E)" is shorthand for this initialization + traversal cost.
- *Why D is incorrect:* O(V × E) would imply checking every vertex for every edge — a nested loop structure. Building an adjacency list does not require this — each edge is appended in O(1) to the appropriate vertex's list.

---

### Question 16

In a directed graph, a vertex with out-degree 0 is called a:

- A) Source vertex
- B) Sink vertex
- C) Isolated vertex
- D) Leaf vertex

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A source vertex has in-degree 0 (no incoming edges) — it is where traversal "originates." A vertex with out-degree 0 has no outgoing edges.
- *Why B is correct:* A sink vertex has out-degree 0 — no edges leave it. Information flows into a sink but never out. In a topological sort, sinks have no dependencies after them.
- *Why C is incorrect:* An isolated vertex has both in-degree 0 AND out-degree 0 — no edges of any kind. A vertex with only out-degree 0 may still have incoming edges.
- *Why D is incorrect:* "Leaf vertex" is a tree term (a node with no children in a rooted tree). In graph theory, it is not the standard term for a vertex with out-degree 0.

---

### Question 17

Which of the following Python code snippets correctly builds an undirected adjacency list from an edge list?

- A)
```python
graph = {}
for u, v in edges:
    graph[u] = v
```

- B)
```python
from collections import defaultdict
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

- C)
```python
graph = defaultdict(list)
for u, v in edges:
    graph[u] = [v]
```

- D)
```python
graph = {}
for u, v in edges:
    graph[(u, v)] = True
```

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `graph[u] = v` overwrites the previous value for key `u` instead of appending. If vertex u has multiple neighbors, only the last one is stored. Also, the reverse direction `graph[v].append(u)` is missing.
- *Why B is correct:* `defaultdict(list)` initializes missing keys with empty lists. `graph[u].append(v)` adds v to u's neighbor list. `graph[v].append(u)` adds u to v's neighbor list, making the edge undirected. This is the canonical Python adjacency list construction.
- *Why C is incorrect:* `graph[u] = [v]` replaces the entire neighbor list with `[v]` on each iteration. If u has multiple neighbors, only the last-processed one is retained.
- *Why D is incorrect:* This builds an edge-set (a set of directed pairs), not an adjacency list. It stores each edge as a tuple key — useful for quick edge existence checks, but not for "list all neighbors of v" queries.

---

### Question 18

What is a "sparse" graph, and which representation is preferred for it?

- A) A graph where every pair of vertices is connected; adjacency matrix preferred
- B) A graph where E << V² (much fewer edges than the maximum possible); adjacency list preferred
- C) A graph with no cycles; edge list preferred
- D) A graph where all vertices have the same degree; adjacency matrix preferred

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A graph where every pair is connected is a complete graph — this is a dense graph, the opposite of sparse. Complete graphs have E = V(V-1)/2 ≈ V² edges.
- *Why B is correct:* A sparse graph has many fewer edges than the theoretical maximum. Real-world networks (social graphs, road networks, internet topology) are almost always sparse. For sparse graphs, an adjacency list uses O(V + E) space — much less than the O(V²) of a matrix. Additionally, traversal algorithms like BFS/DFS run in O(V + E) time on adjacency lists versus O(V²) on matrices for sparse graphs.
- *Why C is incorrect:* A graph with no cycles is an acyclic graph (a DAG if directed, or a forest if undirected). Acyclicity is a cycle property, not a density property. Acyclic graphs can be sparse or dense.
- *Why D is incorrect:* A regular graph (all vertices same degree) can still be dense or sparse depending on the degree value. Regularity does not determine sparsity.

---

### Question 19

Cycle detection in an undirected graph using DFS requires tracking the parent of each node. Why?

- A) To reconstruct the cycle path when one is found
- B) To avoid marking the edge back to the parent as a cycle — traversing a tree edge backwards along the same undirected edge is not a cycle
- C) To count the number of cycles in the graph
- D) To ensure that only nodes in the current component are visited

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* While tracking the parent can help reconstruct a cycle path, that is not the reason it is required. The primary reason is to avoid false positives.
- *Why B is correct:* In an undirected graph, every edge (u, v) is represented as both `u→v` and `v→u`. When DFS is at node u (having arrived from parent v), it sees v in u's neighbor list. Without parent tracking, the algorithm would incorrectly conclude that the back edge to v forms a cycle. Tracking the parent `visited[u] = v` allows the algorithm to skip v when checking u's neighbors, distinguishing a legitimate back edge from the edge back to the tree parent.
- *Why C is incorrect:* Standard DFS cycle detection for undirected graphs returns True/False (cycle exists or not), not a count. Counting cycles is a harder problem and requires different algorithms.
- *Why D is incorrect:* Component isolation is enforced by the `visited` set, not the parent tracking. Nodes in other components are simply not visited when starting DFS from a given source.

---

### Question 20

A graph G has 6 vertices and 5 edges forming a tree (connected, acyclic). What can you conclude?

- A) G is a directed graph
- B) G is a complete graph
- C) G is a connected acyclic graph where exactly V-1 = 5 edges exist, confirming the tree property
- D) G has exactly one vertex with degree 5

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A tree can be either directed (rooted tree) or undirected. The problem states "tree" without specifying direction — the standard definition of a tree as a data structure is undirected. No conclusion about direction can be drawn from V=6, E=5 alone.
- *Why B is incorrect:* A complete graph with 6 vertices has V(V-1)/2 = 15 edges. 5 edges with 6 vertices is far from complete.
- *Why C is correct:* A tree with V vertices has exactly V-1 edges. For V=6: V-1 = 5, which matches. A tree is by definition connected and acyclic. The fact that E = V-1 and the graph is connected is both necessary and sufficient to conclude it is a tree (for undirected graphs).
- *Why D is incorrect:* A star graph (one central vertex connected to all others) would have one vertex with degree V-1 = 5, but this is just one possible tree structure. Many trees with 6 vertices and 5 edges have no vertex of degree 5 — for example, a path graph (each vertex has degree at most 2).
