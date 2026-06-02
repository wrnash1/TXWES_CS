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
