# Reading Guide: Module 09 – Graphs: Representation and BFS/DFS
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 09 – Graphs: Representation and BFS/DFS**! Graphs are the most general data structure in computer science — trees and linked lists are special cases of graphs. Graph problems appear constantly in interviews at top companies: number of islands, course schedule, word ladder, clone graph, and network delay time are all graph problems. Mastering BFS and DFS traversal on graphs, and knowing when to apply each, is a prerequisite for medium-to-hard interview success.

This module covers graph representations (adjacency list, adjacency matrix), directed vs. undirected graphs, BFS for shortest paths, and DFS for connectivity and cycle detection.

---

### 1. High-Yield Glossary

*   **Graph**: A data structure consisting of a set of vertices (nodes) and a set of edges connecting pairs of vertices. Graphs model networks, dependencies, maps, and relationships that trees cannot express due to their acyclic constraint.

*   **Adjacency list**: A graph representation where each vertex stores a list of its neighbors. Space complexity O(V + E). The standard representation for sparse graphs and the default choice in interview solutions.

*   **Adjacency matrix**: A V×V 2D array where `matrix[u][v] = 1` (or edge weight) if an edge exists from u to v. Space complexity O(V²). Efficient for dense graphs and O(1) edge existence checks, but wasteful for sparse graphs.

*   **Directed graph (digraph)**: A graph where each edge has a direction — an edge from u to v does not imply an edge from v to u. Used to model dependencies, one-way streets, and prerequisite chains.

*   **Undirected graph**: A graph where edges are bidirectional — if u connects to v, then v connects to u. Used to model symmetric relationships like friendship networks or road maps.

*   **Breadth-First Search (BFS)**: A graph traversal that explores all neighbors of a node before exploring their neighbors, using a queue. Visits nodes in increasing order of distance from the source. Finds shortest paths in unweighted graphs.

*   **Depth-First Search (DFS)**: A graph traversal that explores as far as possible along each branch before backtracking, using a stack (explicit or call stack). Used for cycle detection, topological sort, connected components, and path existence.

---

### 2. Certification Exam Tips
*   **"Shortest path in unweighted graph" = BFS:** BFS guarantees the shortest path because it explores nodes layer by layer. Never use DFS for shortest path in unweighted graphs — it does not guarantee shortest.
*   **Number of Islands template is essential:** Build it from memory. Iterate over the grid; when you find a '1', increment count and DFS/BFS to mark all connected '1's as visited. O(V + E) time. This pattern solves dozens of variants.
*   **Always track visited nodes in graphs:** Unlike trees, graphs can have cycles. Use a `visited` set (or mark nodes in-place) to prevent infinite loops.
*   **Topological sort = DFS with reverse postorder:** For scheduling/dependency problems (Course Schedule LeetCode #207/#210), use DFS with a `visited` set and a `cycle-detecting` set. Push to result stack on DFS return. Or use Kahn's algorithm (BFS with in-degree tracking).
*   **Bipartite check = 2-coloring with BFS:** Color each node alternately; if any edge connects two nodes of the same color, the graph is not bipartite.
*   **Study Resource:** [Visualgo Graph Traversal](https://visualgo.net/en/dfsbfs) — interactive BFS and DFS animations on custom graphs you can build, making the visited-node frontier concrete.

---

### Required Readings & Videos
*   **Required Reading:** [Graphs – Open Data Structures (Pat Morin), Chapter 12](https://opendatastructures.org/ods-python/12_Graphs.html) — covers adjacency list and matrix representations, BFS and DFS implementations, and connectivity analysis.
*   **Required Video:** [Graph Algorithms – NeetCode on YouTube](https://www.youtube.com/watch?v=EgI5nU9etnU) — a 30-minute interview-focused video covering BFS, DFS, adjacency list construction, and the Number of Islands / Course Schedule patterns.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Build a graph from an edge list** using a `defaultdict(list)` adjacency list and implement both BFS and DFS from a given source node.
*   **Solve LeetCode #200 (Number of Islands)** using DFS to count connected components in a 2D grid.
*   **Solve LeetCode #133 (Clone Graph)** using BFS with a hash map to map old nodes to new nodes.
*   **Solve LeetCode #207 (Course Schedule)** using DFS cycle detection to determine if the prerequisite graph contains a cycle.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 12 of Open Data Structures.
- [ ] Watch the NeetCode Graph Algorithms video.
- [ ] Implement BFS and DFS on an adjacency list graph from scratch.
- [ ] Solve LeetCode #200, #133, and #207.
- [ ] Proceed to the Module 09 Quiz.
