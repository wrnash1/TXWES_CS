# Quiz: Module 10 — Breadth-First Search & Depth-First Search

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

Which data structure does BFS use to determine the order in which nodes are processed?

- A) Stack (LIFO)
- B) Priority queue (min-heap)
- C) Queue (FIFO)
- D) Sorted array

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A stack (LIFO) is used by DFS — nodes added last are processed first, producing depth-first behavior. BFS requires the opposite: nodes added first are processed first.
- *Why B is incorrect:* A priority queue (min-heap) is used by Dijkstra's algorithm to always expand the node with the smallest known distance. BFS treats all edges as equal weight and processes by insertion order.
- *Why C is correct:* BFS uses a FIFO queue (`collections.deque`). Nodes are enqueued when discovered and dequeued in the same order, ensuring all nodes at distance d are processed before any node at distance d+1. This level-by-level expansion is what guarantees shortest paths.
- *Why D is incorrect:* BFS does not sort nodes. A sorted array would require O(n log n) per level and would not preserve the traversal order that makes BFS correct.

---

### Question 2

In BFS, why should nodes be marked as visited **when enqueued** rather than **when dequeued**?

- A) Marking on dequeue causes a `KeyError` in Python
- B) Without early marking, the same node can be added to the queue multiple times by different neighbors, causing duplicates and O(E²) work
- C) Marking on enqueue allows BFS to skip nodes that are no longer reachable
- D) Python's `deque` requires all elements to be unique before insertion

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* There is no `KeyError` involved in marking visited nodes. Both strategies are syntactically valid Python; the distinction is correctness and performance.
- *Why B is correct:* Consider a node X with three neighbors A, B, C that all discover X before any of them is dequeued. If X is only marked visited at dequeue time, it will be enqueued three times — once by A, once by B, once by C. On a dense graph, this can cause O(E) enqueues per node and O(E²) total work. Marking on enqueue ensures X enters the queue exactly once, regardless of how many neighbors discover it.
- *Why C is incorrect:* Marking on enqueue does not skip reachable nodes — it prevents re-processing already-queued nodes. All reachable nodes are still visited exactly once.
- *Why D is incorrect:* Python's `deque` accepts any elements, including duplicates. The uniqueness requirement is a correctness constraint imposed by the algorithm, not by the data structure.

---

### Question 3

For an unweighted undirected graph, BFS from a source node S guarantees that when node T is first dequeued, `dist[T]` holds the shortest path distance from S to T. Why does this guarantee fail for DFS?

- A) DFS does not use a `visited` set, so nodes can be processed multiple times
- B) DFS explores paths in an arbitrary deep order, so the first path found to T may not be the shortest
- C) DFS only works on directed graphs, not undirected ones
- D) DFS cannot track distances because it uses recursion

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DFS does use a `visited` set to prevent cycles. But the `visited` set ensures correctness, not shortest-path optimality.
- *Why B is correct:* DFS follows one path as deep as possible before backtracking. The first path DFS finds to node T may be a long winding path, while a shorter path exists through a different branch. BFS's level-by-level expansion guarantees the first visit is via the minimum number of hops.
- *Why C is incorrect:* DFS works correctly on both directed and undirected graphs. The shortcoming is about path optimality, not graph type.
- *Why D is incorrect:* DFS can track distances during recursion by passing a depth counter. The problem is not implementation difficulty — it is that DFS-computed distances are not guaranteed to be minimal.

---

### Question 4

What is the time complexity of BFS on a graph with V vertices and E edges?

- A) O(V)
- B) O(E)
- C) O(V + E)
- D) O(V · E)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* O(V) would ignore the cost of processing edges. Even if you visited all vertices, you must process each edge to discover new vertices and enqueue them.
- *Why B is incorrect:* O(E) would ignore the initialization cost for V vertices (creating visited set, initializing dist dict). For a disconnected graph where E = 0, BFS still touches all V vertices.
- *Why C is correct:* BFS processes each vertex once (dequeued exactly once) — O(V). For each vertex, it iterates over its adjacency list — total iterations across all vertices = O(E). Combined: O(V + E).
- *Why D is incorrect:* O(V · E) would imply that for each vertex, all edges are re-scanned. This is not the case — each edge is visited only from its two endpoint vertices, not from all V vertices.

---

### Question 5

In the Number of Islands problem, the DFS implementation sets `grid[r][c] = '0'` when visiting a cell. Why is this done, and what is the alternative?

- A) To reset the grid after the algorithm completes
- B) To mark the cell as visited in-place, avoiding a separate `visited` set — the alternative is using a `set` of visited `(row, col)` tuples
- C) To convert land cells to water permanently for future queries
- D) To enable BFS to process the same cell from multiple neighbors

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The grid is not reset after the algorithm — the modification is permanent within the function call. If the original grid must be preserved, a copy must be made before running the algorithm.
- *Why B is correct:* Setting `grid[r][c] = '0'` is in-place marking. When DFS checks `grid[r][c] != '1'`, a sunk cell returns immediately — preventing revisiting. The alternative is `visited = set(); visited.add((r, c))` and checking `(r, c) in visited`. Both are correct; in-place marking saves O(m × n) extra space.
- *Why C is incorrect:* The purpose is to track visited cells during the algorithm, not to permanently alter the semantic meaning of the grid. The choice to modify in-place is a space optimization.
- *Why D is incorrect:* The opposite is true: sinking the cell prevents BFS or DFS from processing it multiple times, not the other way around.

---

### Question 6

The three-color DFS for directed cycle detection uses states 0 (unvisited), 1 (in current path), 2 (fully processed). Why is a back edge to state 1 (not state 2) considered a cycle?

- A) State 1 nodes are in the current recursion stack — an edge back to them creates a circular dependency
- B) State 2 nodes are unvisited — reaching them is always a cycle
- C) State 1 indicates a node that has been deleted from the graph
- D) Only state 0 nodes can have back edges; states 1 and 2 are the same

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is incorrect as a distractor / why it is correct:* A state-1 node is on the active DFS path — currently being explored. An edge from a later node in the path back to an earlier state-1 node creates a path that returns to its own ancestor — a directed cycle. State-2 nodes are fully explored; an edge to a state-2 node is a "cross edge" or "forward edge" — not a cycle.
- *Why B is incorrect:* State 2 means fully processed — all paths from that node have been explored and it is confirmed cycle-free in its subtree. An edge to a state-2 node is safe.
- *Why C is incorrect:* State 1 means the node is actively in the current DFS path (on the call stack), not deleted. No nodes are deleted during cycle detection.
- *Why D is incorrect:* States 1 and 2 are distinct and have different meanings. The three-color approach specifically distinguishes between "currently on the path" (gray/1) and "completely done" (black/2) to enable correct directed cycle detection.

---

### Question 7

Kahn's algorithm for topological sort starts from all nodes with in-degree 0. What does it mean if the output list has **fewer than V nodes** after Kahn's algorithm completes?

- A) The graph has isolated vertices with no edges
- B) Some nodes were processed in an incorrect order
- C) The graph has a cycle — those nodes were never added to the queue because their in-degrees never reached 0
- D) The algorithm ran out of memory before completing

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Isolated vertices (in-degree 0, out-degree 0) are added to the initial queue immediately and are always included in the output. They do not reduce the output count.
- *Why B is incorrect:* Kahn's processes nodes in valid topological order by construction. If a node is processed, its position is correct. The issue is nodes that are *never* processed.
- *Why C is correct:* In a cycle A→B→C→A, every node in the cycle has in-degree ≥ 1. None of them ever reaches in-degree 0 (because their predecessor in the cycle is never removed). They are never added to the queue and never appear in the output. Output size < V is exactly the cycle detection signal.
- *Why D is incorrect:* Memory issues would produce an exception, not a shortened output list. The shortened output is a structural property of cycles in the graph, not a runtime failure.

---

### Question 8

Why should you use `collections.deque` instead of a Python `list` for the BFS queue?

- A) `deque` supports more elements than a `list`
- B) `list.pop(0)` is O(n) because it shifts all remaining elements; `deque.popleft()` is O(1)
- C) `list` does not support the `append` operation needed for BFS
- D) `deque` automatically marks nodes as visited

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both `list` and `deque` grow dynamically and support any number of elements. Capacity is not the distinguishing factor.
- *Why B is correct:* Python's `list` stores elements contiguously. Removing the first element (`list.pop(0)`) requires shifting all remaining elements left by one position — O(n). `collections.deque` is a doubly-linked list that supports O(1) append and popleft. In BFS on a graph with E edges, the difference can be O(E) total vs O(E²) total if a list is used.
- *Why C is incorrect:* `list.append()` works perfectly for adding elements to the right side. The problem is specifically with `list.pop(0)` — removing from the left.
- *Why D is incorrect:* `deque` is a plain data structure with no graph-specific behavior. Visiting tracking is the programmer's responsibility regardless of which container is used.

---

### Question 9

For the grid traversal in Number of Islands, the DFS checks bounds before accessing `grid[r][c]`. In what order should the conditions be checked?

- A) `grid[r][c] != '1'` first, then bounds checks — always access the cell before checking bounds
- B) Bounds checks first (`0 <= r < rows and 0 <= c < cols`), then `grid[r][c] != '1'` — to avoid index-out-of-range errors
- C) Only check `grid[r][c] != '1'` — Python handles out-of-bounds automatically
- D) Order does not matter — Python evaluates all conditions simultaneously

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Accessing `grid[r][c]` before checking bounds will raise `IndexError` when `r` or `c` is out of range. The bounds check must come first.
- *Why B is correct:* Python's `and` operator short-circuits: if `0 <= r < rows and 0 <= c < cols` is False, the second condition `grid[r][c] != '1'` is never evaluated — preventing the index-out-of-range error. This is a critical pattern for all grid problems.
- *Why C is incorrect:* Python raises `IndexError` for out-of-bounds list access. Negative indices are valid in Python lists (they access from the end), which can silently introduce bugs in grid problems where negative row/column indices should mean "out of bounds."
- *Why D is incorrect:* Python evaluates `and` conditions left to right with short-circuit evaluation. Order is essential — placing the array access before the bounds check is a bug.

---

### Question 10

Topological sort is only valid on **DAGs** (Directed Acyclic Graphs). Which of the following problems is correctly modeled as a DAG requiring topological sort?

- A) Finding the shortest path between two cities on a road map
- B) Determining the order to take college courses given prerequisite requirements
- C) Counting the number of islands in a 2D grid
- D) Finding all friends of friends in a social network

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Road maps are undirected weighted graphs (or bidirectional directed). The goal is shortest path (Dijkstra or BFS), not ordering. Road networks typically have cycles (you can drive in a loop).
- *Why B is correct:* Course prerequisites form a directed acyclic graph: "take course A before course B" is a directed edge A→B, and a valid curriculum has no circular prerequisites. Topological sort gives a valid course order. This is LeetCode #207 (Course Schedule) and #210 (Course Schedule II).
- *Why C is incorrect:* Number of Islands is a connected-component problem on an undirected implicit graph (2D grid). It uses BFS or DFS, not topological sort.
- *Why D is incorrect:* Social networks are undirected (friendship is mutual) and cyclic (you can follow chains of friends back to a starting person). BFS is used to explore friend networks, not topological sort.
