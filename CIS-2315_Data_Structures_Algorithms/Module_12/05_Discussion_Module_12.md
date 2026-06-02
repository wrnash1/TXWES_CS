# Discussion Forum: Module 12 — Divide & Conquer

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Background

Divide and conquer is the strategy behind some of the most elegant algorithms in computer science. The insight that splitting a problem into independent halves and combining results can be asymptotically faster than solving the whole at once is non-obvious. Merge sort demonstrates this for sorting. Binary search demonstrates it for searching. The Master Theorem makes the analysis of such algorithms systematic. Understanding why the combination step in merge sort is O(n) per level — not O(n log n) — and why binary search converges in O(log n) steps are the conceptual foundations for recognizing divide-and-conquer opportunities in new problems.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Merge Sort, Stability, and the Recursion Tree

Merge sort's O(n log n) complexity comes from a specific structure: log n levels of recursion, each performing O(n) total work. The stability property — that equal elements maintain their relative order — comes directly from the `left[i] <= right[j]` tie-breaking rule in the merge step.

In 175–225 words, respond to the following:

- From the Module 12 lab (Part 1, Section 1.1), you ran `merge_sort([5,3,8,1,9,2,7,4])`. Draw the first two levels of the recursion tree: what are the subproblems at level 1 (the first split), and what are the subproblems at level 2 (the second split)? At which level does the base case first occur?
- The reading guide explains why merge sort is stable: the `merge` function uses `left[i] <= right[j]` (taking from left when equal) rather than `left[i] < right[j]`. Walk through the stability test from lab Section 1.2: for the pair `(3,'a')` and `(3,'c')`, trace the merge step that places these two elements and explain exactly how the `<=` condition ensures `(3,'a')` precedes `(3,'c')` in the output.
- Quicksort averages O(n log n) but degrades to O(n²) on sorted input with a naive first-element pivot. Describe a real-world scenario where input is likely to be nearly sorted and explain why merge sort would be a better choice than quicksort in that context.

Reference the lab or reading guide in your response.

---

### Scenario B — Binary Search Variants and the Invariant

Binary search seems simple — halve the search space, compare at the middle, narrow down. The difficulty is in the details: `<=` vs `<` in the loop condition, `mid + 1` vs `mid` in the update, what `left` represents at termination. Getting these details right requires understanding the loop invariant: what property is always maintained about the remaining search space.

In 175–225 words, respond to the following:

- From the Module 12 lab (Part 2, Section 2.1), you traced `binary_search([1,3,5,7,9,11,13,15], 7)`. List the state of `left`, `right`, and `mid` at each iteration until the answer is found. At each step, state the invariant: what range are you guaranteed the target is in?
- The lab's `search_leftmost` uses `while left < right` and `right = mid` (not `right = mid - 1`) when `arr[mid] >= target`. Explain why `right = mid` is correct here rather than `right = mid - 1`. What would go wrong if you used `right = mid - 1` when searching for the leftmost occurrence of a duplicate?
- The binary search on answer template (Section 3.1) applies to the ship packages problem because `feasible(capacity)` is a monotone function. Describe another real-world or LeetCode problem (not ship packages) where the answer lies in a numeric range and the feasibility function is monotone. State what `left`, `right`, and `feasible(x)` represent in your example.

Reference the lab or reading guide in your response.

---

### Scenario C — The Master Theorem and Divide-and-Conquer Analysis

The Master Theorem gives asymptotic complexity for recurrences of the form T(n) = a·T(n/b) + f(n). Applying it correctly requires identifying a (number of subproblems), b (reduction factor), and f(n) (combination cost), then comparing f(n) to n^(log_b(a)).

In 175–225 words, respond to the following:

- The reading guide's comparison table lists merge sort as T(n)=2T(n/2)+O(n) → O(n log n) and binary search as T(n)=T(n/2)+O(1) → O(log n). Apply the Master Theorem explicitly to both: for each, state a, b, c=log_b(a), which case applies, and the resulting complexity. Explain in one sentence why Case 2 applies to both despite having different a values.
- Naïve matrix multiplication has recurrence T(n)=8T(n/2)+O(n²). Strassen's algorithm reduces subproblems from 8 to 7: T(n)=7T(n/2)+O(n²). Apply the Master Theorem to both. For which case does the recurrence fall, and what complexity does Strassen achieve? Why is this practically significant?
- The reading guide defines the inversion count modification to merge sort. The counting inversions algorithm from lab Section 1.3 has the same recurrence as merge sort: T(n)=2T(n/2)+O(n). Explain why this is the correct recurrence — specifically, where does the O(n) combination cost come from in the inversion count version?

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 12 lab or reading guide at least once

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

Divide and conquer is where algorithm analysis becomes interesting. The Master Theorem makes it mechanical once you identify the recurrence, but recognizing that a problem has divide-and-conquer structure in the first place is the harder skill. The binary search on answer pattern is the best example: students who see "minimum capacity" or "minimum speed" problems and immediately write a `feasible` function and binary search the range are demonstrating genuine algorithmic thinking. Your posts should show that reasoning — not just "I used binary search" but "I recognized the feasibility function was monotone, so the answer could be found by binary search on the range." That's the level of explanation that earns full credit on algorithm design questions.
