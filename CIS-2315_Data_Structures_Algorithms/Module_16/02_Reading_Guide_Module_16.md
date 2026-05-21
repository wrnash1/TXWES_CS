# Reading Guide: Module 16 – Final Exam Prep & Coding Interview Practice
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

### Introduction
Welcome to **Module 16 – Final Exam Prep & Coding Interview Practice**! This module does not introduce new data structures or algorithms — it consolidates everything from Modules 1–15 and applies it to the full technical interview experience. A coding interview tests not just correctness but communication, problem decomposition, edge case handling, and time/space complexity analysis. This module is your structured preparation for the final coding interview assessment and for real technical screens.

By the end of this module, you should be able to receive an unfamiliar problem, work through it methodically in front of an interviewer, produce a working solution, and discuss its complexity — all within 30–45 minutes.

---

### 1. High-Yield Glossary

*   **FAANG-style technical interview**: A structured coding interview format used by major technology companies (Meta, Amazon, Apple, Netflix, Google and others) consisting of one or more 30–60 minute sessions where a candidate solves algorithmic problems while communicating their reasoning aloud.

*   **Problem decomposition**: The process of breaking a novel interview problem into sub-problems you recognize from prior study. Steps: understand the input/output, identify the data structure, recognize the algorithmic pattern, write a brute-force, then optimize.

*   **Edge case analysis**: Explicitly identifying and testing inputs that could cause incorrect or unexpected behavior: empty arrays, single-element inputs, negative numbers, very large values, sorted/reverse-sorted inputs, and inputs at constraint boundaries.

*   **Time-space tradeoff**: The engineering decision to use additional memory (e.g., a hash map or memo table) to reduce computation time. Common in interviews: use O(n) space to reduce O(n²) time to O(n).

*   **Behavioral interview (STAR format)**: A structured response format for non-technical interview questions: Situation → Task → Action → Result. Used to answer questions like "Tell me about a time you dealt with a technical challenge."

*   **Mock interview**: A simulated coding interview conducted with a partner or through a platform (LeetCode Mock Interview, Pramp, interviewing.io) to practice the full experience including time pressure and verbal communication.

*   **Blind 75 / NeetCode 150**: Curated lists of the most important LeetCode problems for interview preparation, organized by topic. Completing these lists covers the majority of patterns seen in real technical screens at top companies.

---

### 2. Certification Exam Tips
*   **Verbalize your thought process from the start:** Interviewers care as much about how you think as what you produce. Say "I'm going to try a brute force first" before coding, then "I can optimize this with a hash map because..." Silence is the biggest red flag.
*   **Write brute force, then optimize:** For any unfamiliar problem, write the O(n²) or O(2ⁿ) brute force first. This proves you understand the problem. Then optimize iteratively — it is better to have a slow correct solution than to stall searching for the optimal approach.
*   **State complexity after every solution:** Always follow your solution with "This is O(n) time and O(1) space because..." before being asked. This signals senior-level thinking.
*   **Use the 7-step interview framework:** (1) Clarify constraints and edge cases. (2) State and walk through an example. (3) Propose a brute force. (4) Optimize. (5) Write the code. (6) Trace through your code with the example. (7) State time and space complexity.
*   **Review the NeetCode 150 by pattern, not randomly:** Work through arrays, two-pointer, sliding window, stack, binary search, trees, graphs, DP in that order. Solving by pattern builds transferable templates.
*   **Study Resource:** [NeetCode 150 Practice List](https://neetcode.io/practice) — the 150-problem curated list organized by topic with video solutions for every problem. This is the primary preparation resource for the final assessment.

---

### Required Readings & Videos
*   **Required Reading:** Review your notes and completed labs from all previous modules. Focus on the Certification Exam Tips sections for the 3 topics you feel least confident about.
*   **Required Video:** [How to: Work at Google — Example Coding Interview](https://www.youtube.com/watch?v=XKu_SEDAykw) — a 30-minute mock interview by a Google engineer demonstrating exactly how to think aloud, handle hints, and communicate during a live coding interview.
*   **Additional Reading:** [LeetCode Patterns – Sean Prashad's Curated Problem List](https://seanprashad.com/leetcode-patterns/) — a free resource organizing 200+ LeetCode problems by pattern (sliding window, two pointer, tree DFS, etc.) so you study templates rather than individual problems.

---

### Lab & Command Integration
In this week's final assessment lab, you will:
*   **Complete two timed mock interviews (45 minutes each)** on LeetCode's Interview Simulation mode or with a classmate — one easy + one medium problem per session.
*   **Solve at least 5 LeetCode problems you have not seen before**, one from each of: arrays/hashing, trees, graphs, DP, and your weakest topic from this course.
*   **Write a 1-page complexity analysis** for any two problems you solved this semester: state the brute force, the optimized approach, and the time/space complexity of each with justification.
*   **Complete the Final Coding Interview Assessment** — a timed, proctored session with unseen problems drawn from the full course curriculum.

---

### 3. Study Checklist
- [ ] Review Certification Exam Tips from Modules 1–15.
- [ ] Complete at least two timed mock interview sessions.
- [ ] Solve 5 new unseen LeetCode problems across 5 different topics.
- [ ] Write a complexity analysis document for two course problems.
- [ ] Review the NeetCode 150 list and mark problems you have not yet attempted.
- [ ] Complete the Final Coding Interview Assessment.
