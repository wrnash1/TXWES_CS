# Discussion Forum: Module 11 — Dijkstra's Shortest Path Algorithm

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Background

Dijkstra's algorithm is the bridge between graph traversal and optimization. BFS finds the shortest path by hop count; Dijkstra finds the shortest path by total cost. The mechanism — always expanding the cheapest unvisited node — is a greedy strategy whose correctness depends entirely on one assumption: non-negative edge weights. Violate that assumption and the greedy proof collapses. Understanding why the algorithm works (not just the code) prepares you to adapt it to variants like Path With Minimum Effort, to recognize when Bellman-Ford is needed instead, and to explain your choices under interview pressure.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — The Greedy Property and Non-Negative Weights

Dijkstra's correctness proof hinges on a single invariant: when a node is popped from the min-heap, its recorded distance is the true shortest distance from the source. This invariant holds because all edge weights are non-negative — adding any edge can only increase or maintain the total path cost, never decrease it below what was already computed.

In 175–225 words, respond to the following:

- From the Module 11 lab (Part 1, Section 1.1), you traced Dijkstra on the graph with edges A→B(4), A→D(2), D→E(3), B→E(1), E→F(1), B→C(8). When node B is popped with distance 4, the algorithm checks edge B→E and computes 4+1=5. At that moment, E is already in the heap with distance 5 (via A→D→E). Explain why no update occurs, and why this is correct behavior — how does the invariant ensure that dist[E]=5 is already optimal at this point?
- The reading guide presents a graph where Dijkstra gives the wrong answer due to a negative edge (A→B(1), A→C(3), C→B(-3)). Trace Dijkstra's execution step by step and identify the exact moment the algorithm makes a wrong decision. What would Bellman-Ford do differently at that point?
- Describe a real-world application where negative edge weights could naturally arise in a shortest-path problem (not from the reading guide). What does the negative weight represent in that context, and which algorithm would you use?

Reference the lab or reading guide in your response.

---

### Scenario B — Stale Entries and the Lazy Deletion Pattern

Python's `heapq` does not support decrease-key operations. When Dijkstra finds a shorter path to a node already in the heap, it pushes a new `(better_dist, node)` entry without removing the old `(worse_dist, node)`. The old entry becomes stale and is detected and skipped when popped. This is the "lazy deletion" pattern — the standard interview implementation.

In 175–225 words, respond to the following:

- From the Module 11 lab (Part 1, Section 1.2), you ran `dijkstra_verbose` and observed stale entries being skipped. Describe one specific stale skip that occurred in your output: what was the popped distance `d`, what was `dist[node]` at that moment, and how did that gap arise? Which earlier event caused the stale entry to be in the heap?
- The reading guide explains that without the stale check (`if d > dist[node]: continue`), a stale entry would trigger incorrect relaxations of neighbors. Construct a concrete 3-node example where removing this check causes Dijkstra to compute a wrong shortest distance. Trace the execution with and without the check.
- Decrease-key is available in Fibonacci heaps (used in the theoretical O(E + V log V) Dijkstra). For the lazy deletion approach, the heap can hold up to O(E) entries instead of O(V). Explain why this does not change the overall time complexity from O((V + E) log V) — how does the O(E) heap size affect the log factor in each push/pop?

Reference the lab or reading guide in your response.

---

### Scenario C — Network Delay Time and Dijkstra Variants

LeetCode #743 (Network Delay Time) is the canonical Dijkstra interview problem. After solving it, many interview problems become recognizable variants: Path With Minimum Effort (minimize the maximum edge weight on the path), Cheapest Flights Within K Stops (constrained Dijkstra), and Swim in Rising Water (minimize the maximum value along the path).

In 175–225 words, respond to the following:

- From the Module 11 lab (Part 3, Section 3.1), you solved `network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2)` which returned 2. Walk through the Dijkstra execution from source 2: what is the `dist` dictionary at each step, and why is `max(dist.values()) = 2` the correct answer — what physical interpretation does the maximum distance represent?
- The reading guide notes that `network_delay_time` returns -1 if any node is unreachable. In the test case `network_delay_time([[1,2,1]], 2, 2)`, node 1 is unreachable from node 2. Without modifying the Dijkstra code, what value does `max(dist.values())` produce, and how does comparing it to `float('inf')` detect the unreachable case?
- LeetCode #1631 (Path With Minimum Effort) requires finding the path from the top-left to the bottom-right of a grid that minimizes the maximum absolute difference between adjacent cells — not the sum of differences. Describe how you would modify the Dijkstra implementation to solve this: what does the heap store, how is the distance updated differently, and why is Dijkstra still the right algorithm?

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 11 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a second example, challenge a claim with a counter-case, extend the concept to a harder problem, or describe a real-world application that illustrates the point

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | Scenario answered fully with specific, concrete examples. Reference to lab or reading guide. 175–225 words. Complete sentences. |
| 3–4 pts | Mostly addressed but vague or generic. Close to word count. |
| 1–2 pts | Significant parts missing or well below word count. |
| 0 pts | Not submitted. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 pts | Two responses to classmates with different scenarios. Each 60+ words and adds genuine value. |
| 2 pts | One peer response only, or responses lack substance. |
| 0 pts | No peer responses. |

---

## A Note from Professor Nash

Dijkstra is one of those algorithms that seems simple once you understand it, but has a surprising number of subtle failure modes: forgetting to skip stale entries, using the wrong initialization value, applying it to negative-weight graphs. Interviewers know this, and they will probe exactly these edges. The students who answer Dijkstra questions well are not the ones who wrote the most Dijkstra implementations — they are the ones who can explain why the stale check exists, why `float('inf')` is the right initialization, and why BFS is sufficient for unweighted graphs but not for weighted ones. Your posts should engage with those explanations, not just describe the steps.
