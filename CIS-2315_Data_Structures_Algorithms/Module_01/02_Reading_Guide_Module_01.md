# Reading Guide: Module 01 – Big-O Notation and Complexity Analysis
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 01 – Big-O Notation and Complexity Analysis**! This module establishes the language every technical interview uses to evaluate algorithm quality. Before you can discuss whether your solution is "good enough," you must be able to precisely describe how its runtime and memory usage scale with input size. Interviewers at every level — from new grad roles to senior engineering positions — expect fluency with Big-O reasoning.

This module covers the mathematical framework behind complexity analysis, the most important complexity classes you will encounter on LeetCode and HackerRank, and the mental habits you need to instantly estimate the cost of code you write or read in an interview.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. Technical interviewers expect you to use these terms precisely:

*   **Big-O notation (O)**: A mathematical notation describing the *upper bound* of an algorithm's growth rate as input size n approaches infinity. It expresses the worst-case scenario, ignoring constant factors and lower-order terms — so O(2n + 5) simplifies to O(n).

*   **Time complexity**: A measure of how the number of operations an algorithm performs grows relative to its input size n. For example, a single loop over n elements is O(n); two nested loops over the same n elements is typically O(n²).

*   **Space complexity**: A measure of how much additional memory an algorithm requires relative to input size. Iterative solutions often achieve O(1) auxiliary space, while recursive solutions may use O(n) stack space even if no extra data structures are allocated.

*   **Omega notation (Ω)**: The *lower bound* counterpart to Big-O; Ω(n log n) for comparison-based sorting means no such algorithm can do better in the worst case. Less commonly tested in interviews but useful for proving algorithm optimality.

*   **Theta notation (Θ)**: A tight bound describing an algorithm whose best and worst case growth rates are the same. If an algorithm is both O(n) and Ω(n), it is Θ(n) — meaning it always runs in linear time.

*   **Amortized analysis**: A technique for analyzing the *average* cost per operation over a sequence of operations, rather than the worst-case cost of any single one. Dynamic array appending is O(1) amortized even though occasional resizes cost O(n).

*   **Logarithmic complexity (O(log n))**: Growth rate where each step eliminates half the remaining work, as in binary search. Recognizing this pattern (repeatedly halving the problem) is a key interview skill.

---

### 2. Certification Exam Tips
*   **Identify the dominant term:** When calculating complexity, find the term that grows fastest and drop everything else. A function that does an O(n²) nested loop plus an O(n) scan is O(n²) overall.
*   **Count loops, not lines:** Interviewers care about loops and recursive calls. A single `for` loop is O(n); a `for` inside a `for` is O(n²); a loop that halves its range each iteration is O(log n).
*   **Recursive complexity — use the recurrence:** For recursive functions, write the recurrence (e.g., T(n) = 2T(n/2) + O(n) for merge sort) and apply the Master Theorem to get O(n log n).
*   **Space vs. auxiliary space:** Interviewers often ask for *auxiliary* space (extra memory beyond the input). An in-place sort uses O(1) auxiliary space even though the input itself takes O(n).
*   **Know the complexity class table cold:** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!). Any solution worse than O(n²) for large inputs will likely fail.
*   **Study Resource:** Visualize how complexity classes diverge with input size at [Big-O Cheat Sheet](https://www.bigocheatsheet.com) — an authoritative reference listing complexities for all major data structures and sorting algorithms.

---

### Required Readings & Videos
*   **Required Reading:** [Big-O Notation – Open Data Structures (Pat Morin)](https://opendatastructures.org/ods-python/1_3_Mathematical_Background.html) — free open-access textbook chapter covering the formal definition and worked examples.
*   **Required Video:** [Big O Notation – NeetCode on YouTube](https://www.youtube.com/watch?v=BgLTDT03QtU) — a focused 20-minute walkthrough tailored specifically to coding interview preparation, covering time and space complexity with code examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will:
*   **Write and benchmark two solutions to the same problem (e.g., linear vs. binary search)** and compare actual runtimes to predicted complexity classes.
*   **Use Python's `time` module** (`import time; start = time.perf_counter()`) to measure execution time for inputs of size 100, 1000, and 10000.
*   **Annotate each function** with its O(n) time and space complexity as a docstring comment before submitting.
*   **Submit at least one LeetCode Easy problem** (e.g., Two Sum #1) with a written complexity analysis in your solution comments.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the Big-O chapter in Open Data Structures.
- [ ] Watch the NeetCode Big-O video.
- [ ] Practice identifying the complexity of at least 5 code snippets (provided in lab).
- [ ] Complete the lab benchmarking activity and complexity annotation exercise.
- [ ] Proceed to the Module 01 Quiz.
