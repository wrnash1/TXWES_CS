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

---

### Question 11

**Each question is worth 5 points.**

Why must visited nodes be marked on enqueue during BFS, rather than on dequeue?

- A) Marking on dequeue is faster because fewer operations are performed
- B) Marking on enqueue prevents the same node from being added to the queue multiple times, avoiding redundant processing and potential infinite loops
- C) Marking on dequeue ensures all neighbors are discovered before marking
- D) BFS has no requirement about when to mark visited nodes — either approach is equivalent

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Marking on dequeue is incorrect for BFS, not merely slower. If you wait until dequeue to mark, multiple neighbors may enqueue the same unvisited node simultaneously before any of them is dequeued. This causes redundant processing and can multiply the queue size by the degree of each node.
- *Why B is correct:* BFS explores nodes level by level. When node u is dequeued and its neighbor v is discovered, v is enqueued immediately and marked as visited. If v has other neighbors that are also currently being processed, they will see v as visited and skip it. Marking on enqueue prevents v from being added to the queue multiple times — even when multiple currently-processed nodes all have v as a neighbor.
- *Why C is incorrect:* Marking after discovering all neighbors (i.e., after the neighbor loop completes) is equivalent to marking before the loop — the node is already being processed. Marking on dequeue is the problematic pattern, not a late-marking within the current node's processing.
- *Why D is incorrect:* The two approaches are NOT equivalent. Marking on enqueue is correct and efficient; marking on dequeue causes the same node to be enqueued multiple times, leading to incorrect BFS behavior (especially for shortest-path distance calculations).

---

### Question 12

Given this graph and BFS starting from node A, what is the BFS order? `A-B, A-C, B-D, B-E, C-F`

- A) `A, B, D, E, C, F`
- B) `A, B, C, D, E, F`
- C) `A, C, B, F, E, D`
- D) The order depends on which neighbor is listed first in the adjacency list

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* A, B, D, E, C, F would mean B's children (D, E) are processed before C — this is DFS order, not BFS. BFS processes all level-1 nodes (B, C) before any level-2 nodes (D, E, F).
- *Why B is incorrect:* A, B, C, D, E, F is one valid BFS order — but only if B is enqueued before C (i.e., B appears before C in A's adjacency list). BFS order depends on adjacency list ordering.
- *Why C is incorrect:* This would require C to be enqueued before B (C first in A's neighbor list). This is a valid BFS order only for a specific adjacency list ordering.
- *Why D is correct:* BFS guarantees that all level-1 nodes are processed before level-2 nodes (etc.), but the order within each level depends on which neighbors appear first in the adjacency list. Both "A, B, C, D, E, F" and "A, C, B, F, D, E" are valid BFS orderings depending on the adjacency list. When stating BFS order in an interview, specify the neighbor ordering assumption.

---

### Question 13

In iterative DFS using an explicit stack (instead of recursion), nodes are pushed in reverse order of desired visit order. Why?

- A) Stacks are LIFO — the last pushed node is the first explored, so pushing in reverse order ensures correct traversal direction
- B) Reversing the order ensures the stack never overflows
- C) Iterative DFS always visits nodes in the same order as recursive DFS
- D) Reversing is not required — the iterative DFS produces the same order regardless of push order

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* For a node u with neighbors [A, B, C] in adjacency list order, if you want to explore A first (leftmost child), you must push C then B then A (reversed) so that A is on top of the stack and popped first. LIFO behavior means the last pushed is the first popped — reversing the push order makes the first desired neighbor be the first explored.
- *Why B is incorrect:* Stack overflow in iterative DFS would require pushing more nodes than available memory — unrelated to push order. Reversing order does not affect memory usage.
- *Why C is incorrect:* Iterative DFS and recursive DFS do not always produce the same order. Recursive DFS naturally follows the adjacency list order; iterative DFS requires the reverse-push trick to match recursive DFS order. Without reversing, iterative DFS explores in the reverse of the adjacency list order.
- *Why D is incorrect:* The push order directly determines the traversal order. Pushing neighbors in adjacency list order causes the last neighbor to be explored first (rightmost child first), which is a valid DFS but in a different order than typical recursive DFS.

---

### Question 14

In Kahn's topological sort, what does it indicate if the result list has fewer elements than the total number of vertices?

- A) Some vertices have no outgoing edges
- B) The graph is disconnected
- C) The graph contains at least one cycle — no valid topological order exists
- D) Some vertices were never enqueued because they had no in-degree

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Vertices with no outgoing edges (sinks) are correctly processed in Kahn's algorithm — they may be enqueued early if their in-degree was also 0, or eventually after all their predecessors are processed. Sinks do not prevent completion.
- *Why B is incorrect:* Kahn's algorithm handles disconnected graphs correctly. Each connected component has its own set of in-degree-0 nodes. All components will be fully processed if no cycles exist.
- *Why C is correct:* Kahn's algorithm processes a vertex by reducing the in-degrees of its successors. In a cyclic subgraph, no vertex in the cycle ever reaches in-degree 0 (because each vertex has a predecessor within the cycle that hasn't been processed). These vertices are never enqueued, so the result contains fewer than V vertices. This is the cycle detection property of Kahn's algorithm.
- *Why D is incorrect:* Option C correctly identifies the cause. Vertices with initial in-degree 0 are the starting point; all other vertices are enqueued when their in-degree reaches 0 as predecessors are processed. If in-degree never reaches 0, it is because of a cycle.

---

### Question 15

What is the space complexity of BFS on a graph with V vertices and E edges?

- A) O(E) — the queue grows proportional to the number of edges
- B) O(V) — the visited set and queue together hold at most V nodes
- C) O(V²) — BFS explores all pairs of vertices
- D) O(V + E) — the same as the time complexity

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The BFS queue holds vertices, not edges. At any moment, the queue contains the frontier nodes — at most V total across all levels. The number of edges doesn't directly determine queue size.
- *Why B is correct:* BFS maintains a queue and a visited set. The visited set grows to at most V (each vertex is marked exactly once). The queue at any moment holds the current frontier — at most V vertices simultaneously. Total auxiliary space: O(V).
- *Why C is incorrect:* O(V²) would be the space of an adjacency matrix. BFS space complexity is independent of the graph representation. The visited set and queue are the main memory costs — both O(V).
- *Why D is incorrect:* O(V + E) is the time complexity of BFS (visiting all V vertices and all E edge endpoints). Space complexity is O(V) — the queue/visited set do not store edges.

---

### Question 16

The Number of Islands problem (LeetCode #200) counts connected components in a 2D grid. What does each BFS/DFS call initiated from an unvisited '1' cell accomplish?

- A) It finds the shortest path across the island
- B) It marks all cells belonging to one island as visited, so subsequent iterations skip them
- C) It counts the number of '1' cells in the entire grid
- D) It validates that all island cells are surrounded by water

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Shortest path is irrelevant in this problem — there is no path to find, only connected regions to count. BFS/DFS is not finding a path; it is sinking (marking) an entire connected component.
- *Why B is correct:* When an unvisited '1' cell is found, one BFS/DFS call "sinks" the entire connected island — marking every connected '1' cell as visited (by changing it to '0' or adding to a visited set). After the call returns, the outer loop continues scanning the grid. Each subsequent '1' that is still unvisited starts a new BFS/DFS (= a new island). The island count equals the number of BFS/DFS initiations.
- *Why C is incorrect:* Counting all '1' cells would be a simple linear scan without any graph traversal. The traversal is needed to count connected groups, not total cells.
- *Why D is incorrect:* The problem does not ask about the surrounding water structure. Islands can be interior regions, coastal, or anything — the traversal simply counts connected components of '1' cells.

---

### Question 17

Which algorithm guarantees the shortest path in an unweighted graph: BFS or DFS? Why?

- A) DFS — it explores paths exhaustively and finds the shortest by comparison
- B) BFS — it explores nodes level by level, so the first time a node is reached is always via the shortest path
- C) Both guarantee shortest path — they visit every node
- D) Neither — shortest path requires a weighted algorithm like Dijkstra's

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DFS follows one path as deep as possible before backtracking. It may find a very long path to the target before finding the short one. DFS finds some path, not necessarily the shortest.
- *Why B is correct:* BFS explores all nodes at distance k from the source before exploring any nodes at distance k+1. The first time BFS reaches any node, it has taken the minimum number of hops to get there. This is the fundamental property that makes BFS the correct algorithm for shortest path in unweighted graphs. The distance recorded on first enqueue is always the shortest.
- *Why C is incorrect:* Visiting every node does not guarantee shortest path. DFS visits every node but follows single paths to their end before backtracking, potentially recording longer paths before shorter ones.
- *Why D is incorrect:* Dijkstra's algorithm is needed for weighted graphs (where edge weights differ). In unweighted graphs (or graphs where all weights = 1), BFS solves the shortest path problem exactly and more efficiently than Dijkstra's (O(V+E) vs O((V+E) log V)).

---

### Question 18

In recursive DFS on a graph with many connected components, why must the top-level loop call DFS on every unvisited vertex?

- A) To reset the visited set between components
- B) Because DFS started from one vertex only visits nodes reachable from it — disconnected vertices are never reached without an additional outer loop
- C) To ensure the time complexity remains O(V + E) rather than O(V²)
- D) To handle directed graphs where some vertices have no outgoing edges

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The visited set is shared across all DFS calls — it is not reset between components. The shared visited set ensures no vertex is processed twice.
- *Why B is correct:* DFS from a source vertex only reaches nodes in the same connected component (for undirected graphs) or the same reachable subgraph (for directed graphs). Isolated vertices or vertices in other components are never reached by a single DFS call. The outer loop `for v in vertices: if v not in visited: dfs(v)` ensures every unvisited vertex starts a new DFS, covering all components.
- *Why C is incorrect:* The time complexity is O(V + E) regardless of whether there is an outer loop or not. A single DFS from one node already visits all reachable vertices in O(V + E) time for that component. The outer loop adds negligible overhead.
- *Why D is incorrect:* This is a valid observation about directed graphs, but the primary reason for the outer loop is disconnectedness, not edge direction. The outer loop is equally important for undirected graphs with multiple components.

---

### Question 19

What is the key difference between topological sort and a regular DFS traversal?

- A) Topological sort visits nodes in alphabetical order; DFS visits in insertion order
- B) Topological sort only works on undirected graphs; DFS works on both
- C) Topological sort appends each node to the result AFTER all its successors are fully processed (post-order), then reverses; DFS may append in any order
- D) Topological sort uses a queue; DFS uses a stack

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Neither algorithm specifies alphabetical or insertion ordering. The adjacency list ordering determines the traversal order in both cases.
- *Why B is incorrect:* Topological sort requires a DAG (directed acyclic graph). Regular DFS works on both directed and undirected graphs. The restriction is on topological sort (DAG only), not on DFS.
- *Why C is correct:* In topological sort via DFS, a node is added to the result list only after all nodes reachable from it are fully processed (post-order DFS). This ensures every node appears after all its prerequisites. Reversing the post-order list gives the topological order. Regular DFS may record nodes in pre-order (on first visit) — the timing of result recording is the key difference.
- *Why D is incorrect:* Topological sort via DFS uses the call stack (recursion) just like regular DFS. Kahn's topological sort algorithm uses a queue, but DFS-based topological sort does not.

---

### Question 20

What is the time complexity of finding all connected components in an undirected graph with V vertices and E edges using DFS?

- A) O(V) — one DFS call per component, each O(1)
- B) O(V²) — DFS is called V times, each taking O(V)
- C) O(V + E) — each vertex is visited once and each edge is examined once
- D) O(E log V) — edges are processed in sorted order

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Each DFS call visits all vertices and edges in its component — not O(1) per call. The total work across all DFS calls is proportional to the graph size.
- *Why B is incorrect:* Although DFS is potentially called V times (once per unvisited vertex), each call only processes vertices not yet visited. A vertex visited in one call is never revisited in another. Total work = O(V) vertex visits + O(E) edge examinations across all calls = O(V + E), not O(V²).
- *Why C is correct:* The outer loop runs V times (checking every vertex), and DFS from each unvisited vertex processes the vertices and edges of that component. The visited set ensures each vertex is processed exactly once (O(V) total) and each edge is examined from both endpoints (O(2E) = O(E) total). Overall: O(V + E).
- *Why D is incorrect:* Standard DFS does not sort edges. O(E log V) is the time complexity for algorithms involving sorted edge processing, like Kruskal's minimum spanning tree algorithm. DFS does no sorting.
