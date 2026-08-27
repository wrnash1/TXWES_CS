# Quiz: Module 16 — Final Exam Prep (Comprehensive Review)

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

**Instructions:** Choose the single best answer for each question. This quiz draws from all modules in CIS-2315.

---

### Question 1

You need to find the shortest path between two nodes in a graph with equal edge weights. Which algorithm should you use?

- A) Dijkstra's algorithm — it finds shortest paths in weighted graphs
- B) BFS — it finds the shortest path (fewest edges) in unweighted or equal-weight graphs in O(V+E)
- C) DFS — it explores all paths and returns the shortest one
- D) Topological sort — it orders nodes by distance from the source

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Dijkstra works for weighted graphs and would produce the correct answer here, but it is slower than BFS for equal-weight graphs — O((V+E) log V) versus O(V+E). When all edges have equal weight (or weight 1), BFS is the optimal choice.
- *Why B is correct:* BFS explores nodes level by level. In an equal-weight graph, levels correspond to distances (number of edges). The first time BFS reaches a node is guaranteed to be the shortest path — this is BFS's core property. Time complexity is O(V+E).
- *Why C is incorrect:* DFS does not guarantee shortest paths. It follows one branch to its conclusion before backtracking — the first path found may be the longest, not the shortest.
- *Why D is incorrect:* Topological sort orders nodes in a DAG such that all edges go from earlier to later in the ordering. It does not compute distances and is not applicable to general shortest path problems.

---

### Question 2

You need to group a list of strings by their anagram equivalence class. What is the most efficient approach?

- A) Sort the entire list of strings, then use binary search to find groups
- B) Use a Trie — insert all strings and group those that share a common prefix
- C) Use a hash map with `tuple(sorted(word))` as the key — all anagrams produce the same canonical key
- D) Compare every pair of strings with `sorted(a) == sorted(b)` — O(n²) pairs, O(L log L) each

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Sorting the string list places anagrams near each other alphabetically only if they happen to sort the same way — but different anagrams of the same set sort identically only if each string's sorted form is identical. This is essentially the same as C but less directly.
- *Why B is incorrect:* A Trie groups words by shared prefix, not by anagram equivalence. 'eat', 'ate', and 'tea' share no common prefix and would be scattered across the Trie.
- *Why C is correct:* Sorting each string's characters produces a canonical form: 'eat', 'ate', 'tea' all produce `('a','e','t')`. Using this as a hash map key groups all anagrams together in O(n × L log L) total time — one pass through all strings.
- *Why D is incorrect:* This is the brute-force O(n² × L log L) approach. It works but is much slower than the hash map approach for large n.

---

### Question 3

The recurrence T(n) = 4T(n/2) + O(n²) describes an algorithm. What does the Master Theorem give for its complexity?

- A) O(n²) — the combination step dominates (Case 3)
- B) O(n² log n) — the combination step equals the critical exponent (Case 2)
- C) O(n²) — the recursion dominates (Case 1)
- D) O(n^log₂4) = O(n²) — same answer as A but by Case 1

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Case 3 applies when f(n) grows faster than n^c by a polynomial factor (Ω(n^(c+ε))). Here, c = log₂(4) = 2 and f(n) = O(n²) = Θ(n^c) — they are equal, not f growing faster. Case 3 does not apply.
- *Why B is correct:* a=4, b=2, c=log₂(4)=2. f(n)=O(n²)=Θ(n^c). This is exactly Case 2: f(n)=Θ(n^c) → T(n)=Θ(n^c log n)=Θ(n² log n). This is the same pattern as merge sort (Case 2 with c=1) but with c=2.
- *Why C is incorrect:* Case 1 applies when f(n) = O(n^(c-ε)) for some ε > 0 — when the recursion dominates. Here f(n)=Θ(n^c), so neither side dominates. Case 1 does not apply.
- *Why D is incorrect:* n^log₂4 = n² is the Case 1 result if Case 1 applied. But as noted, Case 2 applies, giving n² log n, not n².

---

### Question 4

Which of the following correctly describes the difference between memoization and tabulation in dynamic programming?

- A) Memoization fills the DP table from left to right; tabulation fills it from right to left
- B) Memoization is top-down (recursive with cache); tabulation is bottom-up (iterative table fill)
- C) Memoization computes all subproblems; tabulation computes only needed subproblems
- D) Memoization uses an array; tabulation uses a dictionary

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both memoization and tabulation can fill tables in various orders depending on the problem. Fill direction is a detail of implementation, not the defining distinction.
- *Why B is correct:* Memoization starts from the original problem, recurses down to subproblems, and caches results in a dictionary (top-down). Tabulation starts from the base cases and fills the table iteratively toward the answer (bottom-up). Both produce identical results; the difference is execution order and recursion vs. iteration.
- *Why C is incorrect:* This is backwards. Memoization only computes subproblems that are actually needed (lazy evaluation). Tabulation computes all subproblems in order, even those not needed for the final answer.
- *Why D is incorrect:* Memoization typically uses a dictionary (or `functools.lru_cache`), and tabulation typically uses an array. This is the reverse of what the answer states.

---

### Question 5

Given `nums = [2,7,9,3,1]`, `rob(nums)` should return 12. Which houses are robbed in the optimal solution?

- A) Houses 1 and 3 (values 7 and 3) — total 10
- B) Houses 0, 2, and 4 (values 2, 9, 1) — total 12
- C) Houses 0 and 2 (values 2 and 9) — total 11
- D) House 2 alone (value 9) — can't rob non-adjacent neighbors

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Houses 1 and 3 (7+3=10) are not adjacent, so this is a valid selection — but it is not optimal. House 2 (value 9) was skipped despite not being adjacent to either chosen house.
- *Why B is correct:* Houses 0, 2, 4 are pairwise non-adjacent. Values: 2+9+1=12. The House Robber DP confirms this: prev2=0,prev1=0; num=2: curr=2; num=7: curr=7; num=9: curr=max(7,0+9... wait: curr=max(7,2+9)=11; num=3: curr=max(11,7+3)=11; num=1: curr=max(11,11+1)=12. Return 12.
- *Why C is incorrect:* Houses 0 and 2 give 2+9=11. Adding house 4 (not adjacent to house 2) gives 12 — so skipping house 4 is suboptimal.
- *Why D is incorrect:* House 2 at value 9 is available to rob. The constraint is only that adjacent houses cannot both be robbed. House 2's neighbors are houses 1 and 3; if we also rob house 0 and house 4 (not adjacent to 2), all constraints are satisfied.

---

### Question 6

You are implementing a word search feature: given a dictionary of 50,000 words and user-typed prefixes, return all words that start with the prefix in under 1 millisecond. Which data structure is most appropriate?

- A) Sorted array — binary search finds the prefix start in O(log n), then scan forward
- B) Hash set — O(1) lookup for exact matches
- C) Trie — O(L) to reach the prefix node; enumerate matching words from that subtree
- D) Max-heap — maintain a heap of words sorted by frequency for fast retrieval

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Sorted array with binary search finds the insertion point in O(log n) but then requires scanning forward through potentially many words. For 50,000 words and a short prefix, this scan could be slow. The Trie navigates directly to the prefix node without scanning.
- *Why B is incorrect:* A hash set answers "is this exact word stored?" in O(1), but cannot find words sharing a prefix without scanning all 50,000 entries.
- *Why C is correct:* The Trie is purpose-built for prefix queries. Navigating to the prefix node takes O(L) (L = prefix length, typically 1–5 characters). All matching words are in the subtree rooted at that node and can be enumerated by DFS. No scanning of unrelated words.
- *Why D is incorrect:* A max-heap orders by a numeric priority (frequency). It has no concept of string prefix structure and cannot answer prefix queries without scanning all elements.

---

### Question 7

In the sliding window algorithm for Longest Substring Without Repeating Characters, the key invariant is that `s[left..right]` contains no repeated characters. What enforces this invariant?

- A) Checking `char in seen_set` and removing the duplicate from the set before proceeding
- B) Checking `char_index[char] >= left` and moving `left` to `char_index[char] + 1` to skip past the duplicate
- C) Sorting the current window at each step to detect duplicates
- D) Using a Counter to count character frequencies and removing any character with count > 1

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Removing from a `seen` set by scanning is O(window size) per step — the algorithm still works but uses a different state representation. The `char_index` approach avoids scanning by jumping `left` directly to the position after the duplicate.
- *Why B is correct:* `char_index` stores the most recent index of each character. When a duplicate is found inside the current window (`char_index[char] >= left`), `left` jumps to `char_index[char] + 1` — one position past the old occurrence. This maintains the invariant without scanning. The `>= left` guard prevents `left` from jumping backward (to a position before the window started).
- *Why C is incorrect:* Sorting the window at each step would be O(window size × log(window size)) per character — O(n² log n) total. Far slower than O(n), and sorting does not maintain the window's position structure.
- *Why D is incorrect:* Using a Counter and removing characters with count > 1 requires removing them one at a time from the left — this works but is equivalent to a set-based sliding window and does not jump `left` directly, making it slower in the worst case.

---

### Question 8

You need to detect whether a directed graph has a cycle. Which algorithm and approach is correct?

- A) BFS from every node; if any node is visited twice in any BFS traversal, a cycle exists
- B) DFS with three-color marking: unvisited (0), active/in-current-path (1), done (2). A cycle exists if DFS reaches a node marked 1
- C) Topological sort; if the sorted order includes all V nodes, a cycle exists
- D) Run Dijkstra; if any distance is infinity, a cycle exists

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* BFS does not detect cycles in directed graphs by revisiting nodes. A node can be reachable from multiple sources without forming a cycle. Cycle detection in directed graphs requires tracking the current path — which BFS does not maintain.
- *Why B is correct:* The three-color DFS maintains which nodes are on the current recursion path (color 1). A back edge — reaching a node that is still on the active path — indicates a cycle. This is the standard algorithm for directed cycle detection (used in LeetCode #207 Course Schedule). Color 2 marks fully processed nodes — revisiting them is safe.
- *Why C is incorrect:* This is backwards. Topological sort (via Kahn's) is valid only for DAGs. If the sort produces fewer than V nodes, it means some nodes have unresolvable in-degrees — indicating a cycle exists. The sort cannot complete if a cycle is present, not "includes all V nodes."
- *Why D is incorrect:* Dijkstra finds shortest paths in weighted graphs. Distances of infinity mean nodes are unreachable, not that cycles exist. Cycles can exist even when all nodes are reachable.

---

### Question 9

`coin_change([2], 3)` returns -1. Trace the DP table and explain why.

- A) Because `dp[3]` is never updated — no coin divides 3, so all `dp[i]` for odd i remain infinity
- B) Because `dp[0] = 1` instead of 0 — the base case is wrong
- C) Because coin 2 is larger than target 3, so the inner loop never executes
- D) Because the algorithm tries to use fractional coins, which is not allowed

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* coins=[2], amount=3. dp=[0,inf,inf,inf]. dp[1]: coin=2 > 1, skip. dp[2]: coin=2 ≤ 2, dp[2]=min(inf,dp[0]+1)=1. dp[3]: coin=2 ≤ 3, dp[3]=min(inf,dp[1]+1)=min(inf,inf+1)=inf. dp[1] is infinity because 1 is not reachable with coin 2. So dp[3] remains infinity → return -1. It is not that coin 2 > 3 (it is smaller), but that there is no combination of 2s that sums to 3.
- *Why B is incorrect:* The correct base case is `dp[0] = 0`. If `dp[0] = 1`, the count would be off by one for all reachable amounts, but the -1 result for amount=3 would still occur (dp[3] would still be infinity since 3 is not reachable with coin 2).
- *Why C is incorrect:* coin 2 is smaller than target 3 — the inner loop does execute for i=2 and i=3. The problem is not that the loop is skipped, but that dp[1] is infinity and dp[3] depends on dp[1].
- *Why D is incorrect:* The DP algorithm only uses whole coins — there are no fractional operations. The -1 result is purely because 3 cannot be expressed as a sum of 2s (3 is odd; all sums of 2s are even).

---

### Question 10

A problem asks: "Given weights and values of n items and a knapsack capacity W, find the maximum value you can carry. Each item must be taken whole or not at all." Which algorithm is correct?

- A) Greedy by value/weight ratio — take the most valuable items first
- B) BFS — explore all combinations of items level by level
- C) Dynamic programming — `dp[i][w]` = max value using first i items with capacity w
- D) Greedy by total value — take the highest-value items regardless of weight

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Greedy by value/weight ratio fails for 0/1 knapsack. The Module 13 counterexample: items A(60,10), B(100,20), C(120,30), capacity 50. Greedy takes A (ratio 6/kg) + B (ratio 5/kg) = 160, but optimal is B+C = 220. Since items cannot be split, greedy's locally optimal choice can block a globally better combination.
- *Why B is incorrect:* BFS could enumerate all 2^n subsets level by level, but this is exponential time. BFS has no mechanism for the "optimal substructure" needed to prune the search. It would work for tiny n but is not the correct algorithm.
- *Why C is correct:* The 0/1 Knapsack DP runs in O(n×W). The subproblem `dp[i][w]` captures the essential structure: using a subset of the first i items with capacity w. The recurrence `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight_i]+value_i)` considers both options (take or skip item i) and picks the best — correctly handling the interaction between items that greedy misses.
- *Why D is incorrect:* Greedy by total value ignores weight. Taking the highest-value item might consume all capacity with a single heavy item, missing a better combination of lighter items with higher combined value.

---

### Question 11

A graph has 5 nodes and 4 undirected edges. The graph is connected. What type of graph structure must this be?

- A) A cycle — connected graphs with equal nodes and edges always contain a cycle
- B) A tree — a connected graph with n nodes and n−1 edges is always a tree
- C) A complete graph — all nodes are connected to all others
- D) A bipartite graph — equal nodes and edges imply two-colorability

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* A connected graph with n nodes and n−1 edges cannot have a cycle. Adding any edge to a tree creates exactly one cycle — so a tree has no cycles. The structure described is a tree.
- *Why B is correct:* A tree is defined as a connected acyclic graph. It has exactly n−1 edges for n nodes. This is a fundamental theorem: a connected graph with n nodes and n−1 edges is always a tree (and vice versa). With 5 nodes and 4 edges, connectivity confirms it is a tree.
- *Why C is incorrect:* A complete graph K₅ has 5×4/2 = 10 edges, not 4. The graph described has far fewer edges than a complete graph.
- *Why D is incorrect:* Bipartiteness is about graph colorability (two-colorable = no odd cycles), not about edge count. A graph with n nodes and n−1 edges can be bipartite or not — for a tree (which is always acyclic), it is always bipartite. But the primary classification is "tree," not "bipartite graph."

---

### Question 12

You must find the K-th largest element in an unsorted array of n numbers without sorting the full array. What is the optimal time complexity and approach?

- A) O(n log n) — full sort, then index at position n-K
- B) O(n log K) — maintain a min-heap of size K; final heap top is the K-th largest
- C) O(K log n) — pop from a max-heap K times
- D) O(n) — linear scan comparing each element to the current K-th candidate

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* O(n log n) full sort works and is correct, but it is not optimal for finding just the K-th largest. When K << n, there are faster approaches.
- *Why B is correct:* Maintain a min-heap of size K. For each element: if the heap has fewer than K elements, push it. If the new element is larger than the heap minimum (top), pop the minimum and push the new element. After processing all n elements, the heap top is the K-th largest. Time: O(n log K) — n elements, each heap operation O(log K). Space: O(K).
- *Why C is incorrect:* Converting the array to a max-heap (`heapify`) takes O(n), and popping K times takes O(K log n). Total: O(n + K log n). For large K, this is worse than the min-heap approach. For K=1 (maximum), it is just O(n) — efficient but only for small K.
- *Why D is incorrect:* A single linear scan can find the maximum in O(n), but finding the K-th largest with a single pass requires maintaining a sorted structure of size K — which brings us back to the heap approach. Pure linear O(n) is achievable only with QuickSelect (average case), not a simple scan.

---

### Question 13

Which recurrence and Master Theorem case applies to merge sort, and what is the resulting complexity?

- A) T(n) = T(n/2) + O(1); Case 2; O(log n)
- B) T(n) = 2T(n/2) + O(n); Case 2; O(n log n)
- C) T(n) = 2T(n/2) + O(n²); Case 3; O(n²)
- D) T(n) = 4T(n/2) + O(n); Case 1; O(n²)

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* T(n) = T(n/2) + O(1) is the recurrence for binary search (one subproblem of half size, O(1) combination). c = log₂(1) = 0; f(n)=O(1)=Θ(n⁰); Case 2 gives O(log n). This is binary search, not merge sort.
- *Why B is correct:* Merge sort splits into 2 subproblems of size n/2 and merges in O(n). So a=2, b=2, c=log₂(2)=1. f(n)=O(n)=Θ(n^1)=Θ(n^c) — Case 2 applies. T(n)=Θ(n log n). This is the definitive merge sort analysis.
- *Why C is incorrect:* T(n)=2T(n/2)+O(n²): c=log₂(2)=1; f(n)=O(n²)=Ω(n^(1+1)) — Case 3 applies (combine dominates), giving T(n)=Θ(n²). This describes an algorithm that splits in two but does O(n²) combination work — not merge sort.
- *Why D is incorrect:* T(n)=4T(n/2)+O(n): a=4, b=2, c=log₂(4)=2; f(n)=O(n)=O(n^(2-1)) — Case 1 applies (recursion dominates), giving T(n)=Θ(n²). This describes naive matrix multiplication, not merge sort.

---

### Question 14

A problem says: "Given a string, find the length of the longest contiguous substring containing at most 2 distinct characters." Which algorithm pattern solves this optimally?

- A) Dynamic programming — define dp[i] as the longest such substring ending at index i
- B) Sliding window — maintain a window [left, right] with a character count map; shrink from the left when distinct count exceeds 2
- C) Divide and conquer — split the string at the midpoint and combine palindromic halves
- D) Greedy — always extend the window by the character with the highest frequency

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* DP is not the optimal pattern here. Defining dp[i] as the longest valid substring ending at i would require looking back at all previous positions — O(n²). The sliding window solves this in O(n) by maintaining the current valid window without restarting.
- *Why B is correct:* Sliding window is the canonical pattern for "longest/shortest contiguous substring satisfying a constraint." Maintain a window `[left, right]` and a character count map. Expand `right` always; when `len(count) > 2`, shrink from `left` until the count drops to ≤ 2. Current window length `right - left + 1` is a candidate for the answer. O(n) time.
- *Why C is incorrect:* Divide and conquer splits the problem into halves and combines results — suited for problems where the answer can span the midpoint (like merge sort's inversion count or "longest palindromic substring" with Manacher's). A contiguous substring with a character count constraint does not naturally split this way.
- *Why D is incorrect:* Greedy by highest frequency would not maintain the "at most 2 distinct characters" constraint correctly. The sliding window's shrink-from-left mechanism is what enforces the constraint — not a frequency-based selection criterion.

---

### Question 15

`lcs('AGGTAB', 'GXTXAYB')` returns 4. Which of the following is a valid LCS of these two strings?

- A) 'GTAB'
- B) 'AGAB'
- C) 'GXTB'
- D) 'AGTB'

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* 'GTAB' is a valid LCS of length 4. Verify it is a subsequence of 'AGGTAB': A**G**G**T**A**B** — G at index 1 (or 2), T at index 3, A at index 4, B at index 5. Check 'GXTXAYB': **G**XT**X**A**Y**... wait — 'GTAB' in 'GXTXAYB': G(0), T(3), A(4), B(6). In order — valid. Length 4.
- *Why B is incorrect:* 'AGAB' — check in 'AGGTAB': A(0),G(1 or 2),A(4),B(5) — valid subsequence. Check in 'GXTXAYB': A(4),G(?)... G does not appear after index 0. So A must come after G in 'GXTXAYB'. G is at index 0; A is at index 4. A(4) then G(?) — G at 0 is before 4. 'AGAB' is not a subsequence of 'GXTXAYB' in order (need A before G, but A=4 > G=0). Invalid.
- *Why C is incorrect:* 'GXTB' — check in 'AGGTAB': G(1),X(?)... 'X' does not appear in 'AGGTAB'. Invalid subsequence of 'AGGTAB'.
- *Why D is incorrect:* 'AGTB' — check in 'GXTXAYB': A(4),G(?)... G appears at index 0, which is before A at index 4. Need G after A. No G appears after index 4 in 'GXTXAYB'. Invalid subsequence.

---

### Question 16

What is the key difference between BFS cycle detection in an undirected graph (track parent) and directed graph cycle detection (three-color DFS)?

- A) BFS works for both directed and undirected cycle detection; three-color is only needed for weighted graphs
- B) In undirected graphs, revisiting the immediate parent is not a cycle (it is the same edge traversed backward); in directed graphs, any back edge to an ancestor on the current path is a cycle regardless of parent
- C) Three-color DFS uses more memory than BFS and is therefore avoided for undirected graphs
- D) Undirected cycle detection requires sorting edges by weight first; directed cycle detection does not

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* BFS is not the standard approach for directed cycle detection. For directed graphs, three-color DFS (or Kahn's topological sort) is the standard. BFS with parent tracking works for undirected graphs, but not directly for directed ones.
- *Why B is correct:* In an undirected graph, when DFS visits node B from A and then sees A from B, that is just the bidirectional edge — not a cycle. The parent check (`neighbor != parent`) excludes this. A true cycle requires a visited node that is not the immediate parent. In a directed graph, every edge is one-directional, so a back edge (reaching an ancestor on the current recursion stack, color=1) is always a genuine cycle — no parent exception is needed.
- *Why C is incorrect:* Memory usage is O(V) for both approaches. Three-color DFS is not avoided for memory reasons — it is simply unnecessary for undirected graphs where parent tracking is sufficient.
- *Why D is incorrect:* Neither approach requires edge sorting. Cycle detection is purely structural — edge weights are irrelevant.

---

### Question 17

Which of the following statements about hash tables is correct?

- A) Hash tables guarantee O(1) worst-case lookup
- B) Hash tables support prefix queries in O(L) where L is the key length
- C) Hash tables have O(1) average-case lookup but O(n) worst-case (all keys hash to the same bucket)
- D) Hash tables maintain keys in sorted order for efficient range queries

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Hash tables guarantee O(1) average-case, not worst-case. In the worst case (all keys collide to the same bucket), lookup degrades to O(n) — traversing a chain of n elements.
- *Why B is incorrect:* Hash tables do not support prefix queries. Checking whether any stored key starts with 'pre' requires scanning all keys — O(n). The Trie is the data structure purpose-built for O(L) prefix queries.
- *Why C is correct:* The expected/average case for a hash table with a good hash function and low load factor is O(1) for insert, lookup, and delete. The worst case is O(n) when all keys collide. Python's dict uses a very good hash function that makes worst-case collisions extremely rare in practice.
- *Why D is incorrect:* Hash tables have no ordering guarantee — keys are stored by hash value, not alphabetically or numerically. Sorted order and range queries are provided by BSTs, sorted arrays, or balanced BSTs (like Python's `sortedcontainers.SortedList`).

---

### Question 18

You need to implement `can_complete_circuit` (LeetCode #134). After running the greedy loop, `total_tank = 0` and `start = 3`. What does this mean?

- A) The circuit is impossible — total_tank must be positive for a valid start
- B) The circuit is exactly feasible and station 3 is the valid starting point
- C) Station 3 cannot be the start — total_tank = 0 means the circuit barely completes and the answer is always 0
- D) The function should return -1 because total_tank = 0 is treated as negative

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The feasibility condition is `total_tank >= 0`, not `total_tank > 0`. A total_tank of 0 means the total fuel exactly equals the total cost — the circuit is completable with no surplus. This is valid.
- *Why B is correct:* `total_tank >= 0` confirms the circuit is feasible. The greedy reset logic identified station 3 as the candidate starting point — all stations 0–2 were eliminated because starting there led to a negative running tank. Station 3 is the answer. `return start if total_tank >= 0 else -1` returns 3.
- *Why C is incorrect:* There is no rule that forces the answer to be 0 when total_tank=0. The greedy reset dynamically identifies the start based on where the running tank went negative — the result can be any station index.
- *Why D is incorrect:* The code explicitly checks `total_tank >= 0`. A total of 0 satisfies `>= 0` and returns `start`. Only negative total_tank returns -1.

---

### Question 19

For LeetCode #207 (Course Schedule), you are given `numCourses=2` and `prerequisites=[[1,0],[0,1]]`. What does the three-color DFS algorithm return, and why?

- A) True — both courses are reachable from each other, so all courses can be finished
- B) False — there is a cycle: course 0 requires course 1, and course 1 requires course 0
- C) True — cycles in prerequisites are allowed as long as not all courses are in the cycle
- D) False — two-course cycles always prevent completion regardless of structure

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Mutual reachability means a cycle exists, not that courses can be completed. A cycle in prerequisites means you cannot start either course — each requires the other first. This is a deadlock.
- *Why B is correct:* `prerequisites=[[1,0],[0,1]]` means: to take course 1, you need course 0; and to take course 0, you need course 1. This is a direct cycle of length 2. The three-color DFS detects this: from node 0, mark color=1; go to node 1, mark color=1; follow edge back to node 0 which is still color=1 — cycle detected. Return False. The answer to "can you finish all courses?" is False.
- *Why C is incorrect:* Any cycle in the prerequisite graph makes it impossible to start the courses in that cycle. If courses 0 and 1 are in a cycle, neither can be taken — at least one course cannot be finished. Return False.
- *Why D is incorrect:* Two-course cycles always form a deadlock (answer False), but the claim "regardless of structure" is too general. If the two courses are isolated from all others, only those two fail. The question states only 2 courses total, so all courses fail.

---

### Question 20

What is the correct order of data structure choices from most space-efficient to least for storing n integers?

- A) Hash set → sorted array → binary heap → doubly linked list
- B) Sorted array → binary heap → doubly linked list → hash set
- C) Binary heap ≈ sorted array ≈ doubly linked list < hash set
- D) Sorted array < binary heap < doubly linked list < hash set

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A hash set typically uses more space than a sorted array or heap because it requires extra space for the hash table's load factor and collision handling. A sorted array, heap, and linked list all store exactly n elements with constant overhead per element.
- *Why B is incorrect:* This ordering misidentifies the space costs. A sorted array and binary heap both store exactly n elements as a contiguous array — they have identical space footprints. Neither is inherently smaller than the other.
- *Why C is correct:* A sorted array, binary heap, and array-based doubly linked list all store n elements with O(n) space and minimal constant overhead (one pointer/value per element). A hash set stores the same n elements but requires extra space: the hash table is sized larger than n (load factor typically ~2/3 in Python's dict), and collision handling adds overhead. In Python specifically, sets use approximately 4× the memory of a bare list for the same number of elements.
- *Why D is incorrect:* A sorted array and binary heap have essentially identical space usage (both are n-element arrays). Ranking them as `sorted array < binary heap` with strict inequality misrepresents their actual space cost, which is the same.
