# Quiz: Module 11 — Dijkstra's Shortest Path Algorithm

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question.

---

### Question 1

Dijkstra's algorithm is best described as which of the following?

- A) DFS with a priority queue, guaranteeing the deepest path first
- B) BFS with a priority queue, always expanding the node with the smallest known distance
- C) A sorting algorithm that orders nodes by their degree
- D) A dynamic programming algorithm that builds a shortest-path table bottom-up

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DFS with a priority queue does not describe Dijkstra. DFS goes deep; Dijkstra always expands the closest unprocessed node, which is breadth-like behavior directed by distance rather than depth.
- *Why B is correct:* Dijkstra replaces BFS's FIFO queue with a min-heap (priority queue). Instead of processing nodes in the order they were discovered, it always processes the node with the smallest currently known distance. This greedy nearest-first expansion guarantees optimality for non-negative weights.
- *Why C is incorrect:* Node degree (number of connections) is irrelevant to shortest paths. Dijkstra orders by cumulative path distance, not structural properties of vertices.
- *Why D is incorrect:* While Dijkstra uses memoization-like dist tracking, it is classified as a greedy algorithm, not dynamic programming. It makes locally optimal choices (pop the minimum) that together produce a globally optimal result — the greedy property.

---

### Question 2

What initial value should be assigned to `dist[node]` for all nodes **except the source** before Dijkstra begins?

- A) `0`
- B) `-1`
- C) `float('inf')`
- D) `None`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Initializing to 0 would cause the algorithm to skip all relaxation steps (since any real distance ≥ 0 would never be less than 0). Every node would appear to already have a known shortest distance.
- *Why B is incorrect:* `-1` has no natural interpretation as "unknown distance." It would cause incorrect comparisons: `new_dist < -1` would be true for any negative path, and `-1` might be mistaken for "no path found" (which it actually signals in some APIs like `network_delay_time`).
- *Why C is correct:* `float('inf')` represents "no known path." Any actual distance computed during relaxation is finite and will be less than infinity, so every real path will update the initial value. After the algorithm, nodes that remain `float('inf')` are genuinely unreachable.
- *Why D is incorrect:* Using `None` would cause a `TypeError` when comparing `new_dist < None` in Python 3, since integers cannot be compared to `None` with `<`.

---

### Question 3

In the Dijkstra implementation, the line `if d > dist[node]: continue` is called the "stale entry check." Why is this check necessary?

- A) To prevent the algorithm from processing the source node more than once
- B) When a shorter path to a node is found after it is already in the heap, the old (larger distance) entry is not removed — it must be skipped when popped to avoid incorrect relaxations
- C) To skip nodes that have no outgoing edges
- D) To handle the case where `dist[node]` was initialized to `float('inf')`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The source node is pushed once with distance 0. If it were pushed again (it is not, in the standard implementation), the check would catch it — but source re-processing is not the primary motivation.
- *Why B is correct:* Python's `heapq` does not support decrease-key operations. When a better distance to node X is found, the new `(better_dist, X)` is pushed, but the old `(worse_dist, X)` remains in the heap. When the old entry is eventually popped, `d > dist[node]` catches it (because `dist[node]` was updated to the better distance), and `continue` skips it. Without this check, the stale entry would attempt to relax neighbors with a suboptimal distance.
- *Why C is incorrect:* Nodes with no outgoing edges are handled correctly without the stale check — the `for neighbor, weight in graph[node]` loop simply iterates zero times. No `continue` is needed for that case.
- *Why D is incorrect:* The initial `float('inf')` values are only in `dist`, not in the heap. The heap starts with only `(0, start)`. The stale check addresses heap entries added during execution, not the initialization state.

---

### Question 4

Given the directed weighted graph with edges A→B(4), A→C(2), C→B(1), what is `dist['B']` after Dijkstra from source A?

- A) 4 — via the direct edge A→B
- B) 3 — via A→C→B (2+1=3)
- C) 2 — via the cheapest outgoing edge from A
- D) 1 — the weight of the cheapest edge touching B

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The direct path A→B has cost 4. But the path A→C→B has cost 2+1=3, which is shorter. Dijkstra finds the shortest path, not the direct path.
- *Why B is correct:* Dijkstra from A: Pop (0,A), relax B→4 and C→2. Pop (2,C), relax B→2+1=3 < 4 → update dist[B]=3. Pop (3,B). Final dist[B]=3 via A→C→B.
- *Why C is incorrect:* 2 is the distance to C, not to B. The cheapest outgoing edge from A goes to C, but B is reached through C.
- *Why D is incorrect:* 1 is the weight of edge C→B in isolation. Shortest path distances consider the full path from the source, not single edge weights.

---

### Question 5

Why does Dijkstra's algorithm fail to find correct shortest paths when the graph contains **negative edge weights**?

- A) Python's `heapq` cannot store negative numbers
- B) Negative weights cause the `dist` array to overflow
- C) Once a node is popped from the heap, its distance is considered final — a later negative-weight path that would give a shorter distance is never explored
- D) Negative weights create cycles that cause infinite loops

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Python's `heapq` handles negative numbers correctly. Tuples with negative distances are valid heap entries.
- *Why B is incorrect:* Python floats do not overflow for realistic graph weights. The failure is algorithmic, not numerical.
- *Why C is correct:* Dijkstra's greedy correctness proof relies on the fact that adding any edge to a path can only increase (or maintain) the distance, never decrease it below the already-popped node's distance. With negative edges, this proof fails: a node popped with distance d might have a shorter path discovered later through a negative-weight edge from a higher-distance node.
- *Why D is incorrect:* Negative weights alone do not create cycles. Negative-weight cycles (cycles with total negative weight) are a separate issue handled by Bellman-Ford's cycle detection. A graph can have negative edges with no cycles and still produce incorrect results with Dijkstra.

---

### Question 6

In the Network Delay Time problem (LeetCode #743), after running Dijkstra from source k, what expression gives the correct answer?

- A) `min(dist.values())`
- B) `sum(dist.values())`
- C) `max(dist.values())` — or -1 if any value is `float('inf')`
- D) `dist[k]`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `min(dist.values())` returns the distance to the closest node (which is 0 for the source itself). The problem asks how long until all nodes have received the signal — the bottleneck is the farthest node.
- *Why B is incorrect:* Summing all distances has no meaningful interpretation for the "when does the last signal arrive" question. It would give an inflated value proportional to the number of nodes.
- *Why C is correct:* The signal reaches all nodes in parallel; the total time is limited by the last node to receive it — the one with the maximum shortest-path distance from k. If any node is unreachable (`dist[node] == float('inf')`), the maximum is `float('inf')`, which maps to -1 (the "unreachable" sentinel).
- *Why D is incorrect:* `dist[k]` = 0, since k is the source. This would always return 0 regardless of the graph structure.

---

### Question 7

In path reconstruction after Dijkstra, the `prev` dictionary tracks the predecessor of each node. After computing `prev`, how is the actual path from `start` to `end` recovered?

- A) Read `prev` from `start` to `end` — the values form a forward path
- B) Follow `prev` pointers from `end` back to `start`, collecting nodes, then reverse the resulting list
- C) Sort all nodes by their `dist` values to get the path order
- D) Follow `prev` pointers from `start` to `end` — `prev[start]` points to the next node on the path

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `prev[node]` stores the predecessor of `node`, not its successor. Reading forward from `start` using `prev` is not directly possible — `prev` maps destinations to their source, not the other way around.
- *Why B is correct:* `prev[end]` gives the node before `end` on the shortest path. Following `prev` repeatedly: `end → prev[end] → prev[prev[end]] → ... → start → None`. This backward chain, when reversed, gives the correct forward path from `start` to `end`.
- *Why C is incorrect:* Sorting by `dist` gives the order in which nodes were finalized, not the specific path from start to end. The sorted order would list all nodes, not just those on the shortest path to a particular destination.
- *Why D is incorrect:* `prev[start]` is `None` — the source has no predecessor. `prev` does not point forward; it points to the parent in the shortest-path tree.

---

### Question 8

The time complexity of Dijkstra with a binary min-heap is O((V + E) log V). What operation accounts for the `log V` factor?

- A) Initializing the distance array to `float('inf')`
- B) Each `heappush` and `heappop` operation on the heap, which costs O(log(heap size)) — bounded by O(log V) since at most V nodes are in the heap at any time
- C) Sorting the graph's edges before processing
- D) Scanning all edges to find the minimum-weight edge at each step

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Initializing V distances to `float('inf')` is O(V) — a one-time linear-cost setup. It contributes to the O(V) term, not the O(log V) factor.
- *Why B is correct:* Each `heappush` and `heappop` costs O(log k) where k is the current heap size. In the worst case, E edges are relaxed and each triggers a `heappush`, giving O(E log V) for all pushes. Plus O(V log V) for V pops. Combined: O((V + E) log V).
- *Why C is incorrect:* Dijkstra does not pre-sort edges. It processes edges lazily during BFS-style expansion. Pre-sorting would add O(E log E) = O(E log V) for a distinct reason, but it is not part of the standard implementation.
- *Why D is incorrect:* Finding the minimum at each step takes O(1) for a heap (`heap[0]`), not O(E). Scanning all edges for the minimum would give O(V · E) — that is closer to a naive Dijkstra without a heap.

---

### Question 9

For the Network Delay Time problem, the nodes are 1-indexed (1 to n). A student initializes `dist` as:

```python
dist = {i: float('inf') for i in range(n)}
```

What bug does this introduce?

- A) The `range(n)` generates indices 0 through n-1, missing node n — `dist[n]` raises `KeyError` during relaxation
- B) `float('inf')` is not a valid dictionary value in Python
- C) The dictionary should use a list, not a dict comprehension
- D) Using `range(n)` instead of `range(1, n+1)` means node 0 is included but node n is excluded, causing incorrect initialization for 1-indexed nodes

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* While "missing node n" is partially correct, the more complete answer includes both the off-by-one error and its consequence. Option D states it more precisely.
- *Why B is incorrect:* `float('inf')` is a perfectly valid Python dictionary value. The bug is in the key range, not the value type.
- *Why C is incorrect:* A dict comprehension is appropriate here and is more readable than a list. The bug is in the range arguments.
- *Why D is correct:* `range(n)` produces 0, 1, ..., n-1. For 1-indexed nodes (1 to n), the correct range is `range(1, n+1)`. Using `range(n)` creates a `dist` that covers node 0 (which does not exist) and misses node n (which does exist), causing `KeyError: n` when processing edges that touch node n.

---

### Question 10

Which of the following correctly explains why BFS finds shortest paths in an **unweighted** graph but Dijkstra is needed for **weighted** graphs?

- A) BFS uses more memory than Dijkstra, so it cannot handle weighted graphs
- B) In an unweighted graph, all edges have cost 1, so FIFO order (BFS) naturally processes nodes in order of increasing hop count. In a weighted graph, a node reached in two hops may be cheaper than one reached in one hop, requiring the min-heap to process by actual cost
- C) Dijkstra only works for directed graphs, while BFS works for both directed and undirected
- D) BFS is O(V + E) and Dijkstra is O((V + E) log V) — the log factor makes Dijkstra slower, so it handles more complex inputs

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Memory usage does not determine which problems an algorithm can solve correctly. BFS uses O(V) space; Dijkstra uses O(V + E) — comparable. The distinction is about correctness, not memory.
- *Why B is correct:* In an unweighted graph, every edge has implicit cost 1. BFS processes nodes in FIFO order, which is the same as distance order (nodes at distance d before d+1). In a weighted graph, a 2-hop path might cost 3 while a 1-hop path costs 10. BFS would incorrectly finalize the 1-hop node first. Dijkstra's min-heap ensures the node with the smallest total cost is always processed next, regardless of hop count.
- *Why C is incorrect:* Both BFS and Dijkstra work on both directed and undirected graphs. The distinction is weight handling, not direction.
- *Why D is incorrect:* The log factor describes complexity, not capability. An O(n²) algorithm can be "more powerful" than an O(n) one if it solves a harder problem. Dijkstra handles weighted graphs because of its priority-queue property, not because it is slower.
