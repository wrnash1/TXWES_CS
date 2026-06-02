# Discussion Forum: Module 13 — Greedy Algorithms

## Course: CIS-2315 Data Structures & Algorithms

**Certification Alignment:** Technical Interview Readiness (LeetCode / HackerRank)

---

## Background

Greedy algorithms are deceptively simple in structure but require careful justification. The algorithm itself — sort, iterate, pick the locally best option — often fits in ten lines of code. The hard part is knowing when that local optimality translates into a globally optimal result. Activity selection works. 0/1 knapsack doesn't. Jump Game works. Coin change only works for certain denominations. The difference is always in the mathematical structure of the problem, not the code. The exchange argument is the tool that distinguishes the two: if you can show that swapping the greedy choice into any optimal solution leaves it no worse, the greedy algorithm is correct.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Activity Selection and the Exchange Argument

Activity selection is the canonical example of a provably correct greedy algorithm. The proof relies entirely on the exchange argument: any optimal solution that does not start with the earliest-finishing activity can be modified to do so without reducing the total count.

In 175–225 words, respond to the following:

- From the Module 13 lab (Part 1, Section 1.1), you tested `activity_selection([(1,2),(3,4),(0,6),(5,7),(3,5),(5,9)])`. Write out the sorted order and trace the greedy selection step by step: for each activity after the first, state whether it is selected or skipped and why. What is the final selected set?
- The reading guide's exchange argument explains why the greedy choice (earliest-finishing activity) is safe. State the exchange argument in your own words — not a quote, but your own explanation. Why does swapping in the earliest-finishing activity guarantee the result is "no worse"?
- Describe a real-world scheduling scenario (not the one from the video or reading guide) where you would apply the earliest-finish greedy. Be specific: what are the activities, what is the resource being shared, and what problem would earliest-start greedy cause in your scenario?

Reference the lab or reading guide in your response.

---

### Scenario B — Jump Game I and II: Greedy Reachability

Jump Game I and II look similar but ask different questions: can you reach the end, and what is the minimum number of jumps? Both have O(n) greedy solutions, but the variables tracked and the invariants maintained are different.

In 175–225 words, respond to the following:

- From the Module 13 lab (Part 2, Section 2.1), trace `can_jump([3,2,1,0,4])` step by step. List the value of `i`, `jump`, and `max_reach` at each iteration, and identify the exact step where the function returns False.
- Jump Game II uses `current_end` and `farthest` in a way the reading guide describes as a "BFS-level metaphor." Explain this metaphor: what does a "level" represent, when does the level change, and why does each level change correspond to exactly one jump increment?
- In `jump([2,3,0,1,4])`, trace the algorithm through its iterations. Your trace should show `i`, `farthest`, and `current_end` at each step, and identify when `jumps` increments. Confirm that your result (2) is the minimum using a written explanation of why 1 jump is insufficient.

Reference the lab or reading guide in your response.

---

### Scenario C — When Greedy Fails: Knapsack and Coin Change

The most important skill related to greedy algorithms is knowing when not to use them. The 0/1 knapsack and certain coin change problems are standard examples where a seemingly reasonable greedy strategy produces a suboptimal result.

In 175–225 words, respond to the following:

- From the Module 13 lab (Part 3, Section 3.3), the counterexample has capacity=50 and items A(60,10), B(100,20), C(120,30). Trace the greedy algorithm (sort by ratio, take whole items) step by step: list the ratio for each item, which items are taken, what capacity remains, and why C cannot fit. Confirm that the optimal solution (B+C=220) is better.
- The reading guide states that greedy works for fractional knapsack but fails for 0/1 knapsack. Explain in structural terms (not just "you can't split items") why divisibility of items makes greedy correct for fractional but incorrect for 0/1. Your explanation should connect to the exchange argument — specifically, why the exchange argument holds for fractional but breaks for 0/1.
- The coin change problem (Module 13 Quiz, Question 10) shows greedy fails for denominations {1,3,4} with target 6. Construct your own example: choose a denomination set and a target amount where greedy fails. Show the greedy result, the optimal result, and explain specifically which greedy choice caused the failure.

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 13 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a second example, challenge a claim with a counter-case, extend the concept to a harder LeetCode problem, or explain how the concept from your classmate's scenario connects to one from a different module

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

Greedy algorithms are where students learn to distinguish between "this seems to work on examples" and "I can prove this is always correct." The exchange argument is the formal version of that distinction. When you are asked in an interview whether a greedy strategy is correct — and you will be — the interviewer is not looking for "I tested it on a few inputs." They are looking for the structural argument: why does choosing locally optimally here guarantee a globally optimal result? The activity selection exchange argument is the template. If you can explain that argument fluently, you can apply the same reasoning to new problems — interval scheduling, task assignment, bandwidth allocation. The 0/1 knapsack failure is just as important to internalize: recognizing when greedy is tempting but wrong is a sign of algorithmic maturity. If you see "cannot be split" or "must take all or nothing," that is your cue to reach for dynamic programming instead.
