# Reading Guide: Module 14 – Greedy Algorithms
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 14 – Greedy Algorithms**! A greedy algorithm makes the locally optimal choice at each step with the hope that this leads to a globally optimal solution. Greedy algorithms are elegant and efficient when they work — but they fail silently when they do not, and the critical skill is proving (or disproving) that a greedy strategy is correct for a specific problem. Interviews test your ability to propose a greedy solution and justify it, not just code it.

This module covers the conditions that make greedy algorithms correct (exchange argument, matroid structure), the most common greedy interview problems, and the key contrast between greedy and DP.

---

### 1. High-Yield Glossary

*   **Greedy algorithm**: An algorithm that builds a solution by making the choice that looks best at the current step, never reconsidering past decisions. Runs in a single forward pass, typically O(n log n) after an initial sort or O(n) without sorting.

*   **Greedy choice property**: A problem has this property if a globally optimal solution can always be constructed by making locally optimal (greedy) choices. Proving this property is what justifies using a greedy algorithm over DP.

*   **Exchange argument**: A common proof technique for greedy correctness: assume a non-greedy optimal solution exists, then show that swapping its choice for the greedy choice does not make it worse — eventually converting it to the greedy solution while maintaining optimality.

*   **Activity selection problem**: A classic greedy problem: given intervals with start and end times, find the maximum number of non-overlapping intervals. The greedy strategy — always select the interval with the earliest end time — is provably optimal.

*   **Interval scheduling / merging**: Problems involving intervals often have greedy solutions. Key pattern: sort by start time (for merging) or end time (for maximizing non-overlapping count), then make one-pass decisions.

*   **Fractional knapsack**: A variant of the knapsack problem where items can be divided into fractions. The greedy strategy (sort by value-to-weight ratio, take as much as possible of the highest-ratio item) gives the optimal solution. The 0/1 knapsack (no fractions) requires DP.

*   **Greedy vs. DP**: Greedy makes one irrevocable choice per step; DP explores all possibilities by storing subproblem solutions. Use greedy when the greedy choice property holds; use DP when it does not.

---

### 2. Certification Exam Tips
*   **Always justify your greedy:** In an interview, state which greedy property you're using and why. "I sort by X because taking the smallest/earliest/cheapest first is always optimal because..." — an unjustified greedy answer looks like guessing.
*   **Sorting first is the most common greedy setup:** Jump Game, Merge Intervals, Meeting Rooms, Task Scheduler — nearly all interval and scheduling greedy problems start with sorting.
*   **The classic trap: Greedy fails for 0/1 knapsack:** If you cannot break items, greedy by value/weight ratio does not work. This is a common interview trap — mention DP is required when items are indivisible.
*   **Jump Game (LeetCode #55) is the canonical greedy problem:** Track the maximum reachable index as you iterate. O(n) time, O(1) space — much simpler than a DP solution and provably equivalent.
*   **Huffman coding = greedy on a priority queue:** Build an optimal prefix-free code by always merging the two lowest-frequency symbols first using a min-heap. The correctness proof is an exchange argument.
*   **Study Resource:** [Greedy Algorithms – Algorithms by Jeff Erickson, Chapter 4](https://jeffe.cs.illinois.edu/teaching/algorithms/book/04-greedy.pdf) — a free open-access chapter with formal greedy proofs for interval scheduling, Huffman coding, and MST algorithms.

---

### Required Readings & Videos
*   **Required Reading:** [Greedy Algorithms – Algorithms (Jeff Erickson), Chapter 4](https://jeffe.cs.illinois.edu/teaching/algorithms/book/04-greedy.pdf) — covers the exchange argument proof technique, activity selection, fractional knapsack, and Huffman coding with rigorous analysis.
*   **Required Video:** [Greedy – NeetCode on YouTube](https://www.youtube.com/watch?v=lfQvPHGtu6Q) — a 20-minute interview-focused video covering Jump Game, Merge Intervals, and Gas Station with greedy justification and LeetCode solutions.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Solve LeetCode #55 (Jump Game)** using the greedy max-reach approach — track the farthest reachable index in O(n).
*   **Solve LeetCode #56 (Merge Intervals)** — sort by start time, then make greedy merge decisions in one pass.
*   **Solve LeetCode #435 (Non-overlapping Intervals)** — minimum removals to eliminate overlaps (greedy: sort by end time, keep intervals with earliest end).
*   **Compare LeetCode #322 (Coin Change)** using greedy vs. DP: demonstrate with a counterexample (coins = [1, 3, 4], amount = 6) that greedy fails and DP is required.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read Chapter 4 of Algorithms by Jeff Erickson.
- [ ] Watch the NeetCode Greedy video.
- [ ] Solve LeetCode #55, #56, and #435.
- [ ] Construct and document a counterexample showing greedy fails for 0/1 knapsack.
- [ ] Proceed to the Module 14 Quiz.
