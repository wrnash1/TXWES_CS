# Quiz: Module 09 – Graphs: Representation and BFS/DFS
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
Which graph traversal algorithm guarantees finding the shortest path in an unweighted graph?
*   A) DFS using a stack
*   B) BFS using a queue
*   C) Topological sort
*   D) In-order traversal
*   **Correct Answer:** B) BFS using a queue
*   **Distractor Analysis:**
    *   *Why correct:* BFS explores all nodes at distance d before any node at distance d+1. The first time it reaches the destination, the path used is guaranteed to be the shortest in terms of edge count.
    *   A is incorrect: DFS follows one path as deep as possible and may reach the destination via a longer route before exploring shorter ones.
    *   C is incorrect: Topological sort orders nodes by dependency; it does not find shortest paths.
    *   D is incorrect: In-order traversal is a tree concept and does not apply to general graphs.

---

**Question 2**
Which of the following is the most accurate definition of an **adjacency list** graph representation?
*   A) A V×V 2D array where entry [u][v] equals 1 if an edge exists from vertex u to vertex v and 0 otherwise, enabling O(1) edge existence queries.
*   B) A data structure where each vertex maintains a list of its directly connected neighbors, using O(V + E) total space and making iteration over a vertex's neighbors O(degree) time.
*   C) A sorted list of all edges in the graph stored as (u, v, weight) tuples, enabling binary search for edge existence in O(log E) time.
*   D) A hash map from each vertex to its distance from the source, updated during BFS or Dijkstra's algorithm to track shortest path lengths.
*   **Correct Answer:** B) A data structure where each vertex maintains a list of its directly connected neighbors, using O(V + E) total space and making iteration over a vertex's neighbors O(degree) time.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes an adjacency matrix, not an adjacency list.
    *   *Why B is correct:* An adjacency list stores, for each vertex, only its actual neighbors. Total space is proportional to the number of vertices plus edges — efficient for sparse graphs.
    *   *Why C is incorrect:* That describes an edge list, a third representation distinct from both adjacency list and matrix.
    *   *Why D is incorrect:* That describes the `dist` array in BFS/Dijkstra, which is an output of an algorithm, not a graph representation.

---

**Question 3**
In the Number of Islands problem (LeetCode #200), you encounter a grid of '1's and '0's and must count connected land regions. After finding an unvisited '1', what should your DFS or BFS do?
*   A) Count all '1' cells in the entire grid and divide by the average island size.
*   B) Mark the current cell as visited (e.g., change '1' to '0' or add to visited set), then recursively/iteratively process all four adjacent '1' cells.
*   C) Sort all '1' cells by row and column, then use a two-pointer technique to group adjacent cells.
*   D) Push all grid cells into a priority queue ordered by value, then pop and connect cells greedily.
*   **Correct Answer:** B) Mark the current cell as visited (e.g., change '1' to '0' or add to visited set), then recursively/iteratively process all four adjacent '1' cells.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Islands vary in size; dividing a total count by an average is neither correct nor efficient.
    *   *Why B is correct:* Marking visited prevents revisiting cells in cycles. Expanding to all four neighbors floods the entire island, so incrementing the count once per DFS/BFS launch counts each connected component exactly once.
    *   *Why C is incorrect:* Sorting and two-pointers are array techniques; they do not correctly identify spatially connected components in a 2D grid.
    *   *Why D is incorrect:* A priority queue adds unnecessary O(log n) overhead and does not model island connectivity.

---

**Question 4**
What data structure is used to detect cycles in a directed graph using DFS?
*   A) A single `visited` set containing all nodes seen so far in any DFS call.
*   B) Two sets: a `visited` set for nodes fully processed, and a `in_stack` (or `grey`) set for nodes in the current DFS path; a cycle exists if you reach a node already in `in_stack`.
*   C) A queue containing the nodes at the current BFS frontier, which detects back-edges when a neighbor is already in the queue.
*   D) A min-heap sorted by discovery time; a cycle is detected when the minimum discovery time equals the current depth.
*   **Correct Answer:** B) Two sets: a `visited` set for nodes fully processed, and a `in_stack` (or `grey`) set for nodes in the current DFS path; a cycle exists if you reach a node already in `in_stack`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single visited set is sufficient for undirected graphs, but in directed graphs, reaching a previously visited node does not imply a cycle — the earlier visit may have been from a different path.
    *   *Why B is correct:* In directed graphs, a back edge (edge to a node already on the current DFS stack) indicates a cycle. The `in_stack` set tracks which nodes are on the active recursion path.
    *   *Why C is incorrect:* BFS frontier queues do not naturally detect directed cycles; a node leaving the queue does not mean its DFS path is finished.
    *   *Why D is incorrect:* Min-heaps are used in Dijkstra's algorithm; discovery time ordering does not detect directed cycles.

---

**Question 5**
You have a sparse graph with V = 1,000 vertices and E = 2,000 edges. Which representation is most space-efficient?
*   A) Adjacency matrix — O(V²) = 1,000,000 entries
*   B) Adjacency list — O(V + E) = 3,000 entries total
*   C) Both use the same space because the graph is stored in memory either way.
*   D) Adjacency matrix — because 2D arrays have better cache performance than linked lists.
*   **Correct Answer:** B) Adjacency list — O(V + E) = 3,000 entries total
*   **Distractor Analysis:**
    *   *Why A is incorrect:* With V = 1,000, an adjacency matrix requires 1,000,000 cells regardless of how many edges actually exist — wasteful when only 2,000 edges are present.
    *   *Why B is correct:* An adjacency list allocates space proportional to actual vertices plus actual edges: 1,000 + 2,000 = 3,000 — 333× more space-efficient than the matrix for this sparse graph.
    *   *Why C is incorrect:* The two representations have dramatically different space requirements; they are not equivalent.
    *   *Why D is incorrect:* Cache performance may favor matrices in dense graphs, but space efficiency is the primary concern here and the question asks about space, not cache behavior.
