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
