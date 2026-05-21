# Quiz: Module 01 – Big-O Notation and Complexity Analysis
## Course: CIS-2315 Data Structures & Algorithms (Technical Interview Readiness)

---

**Question 1**
What is the time complexity of the following code snippet?
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
*   A) O(n)
*   B) O(n log n)
*   C) O(n²)
*   D) O(2n)
*   **Correct Answer:** C) O(n²)
*   **Distractor Analysis:**
    *   *Why correct:* There are two nested loops each iterating n times, producing n × n = n² total operations.
    *   A is incorrect: O(n) would require only a single linear pass with no nesting.
    *   B is incorrect: O(n log n) is the complexity of efficient sorting algorithms, not nested linear loops.
    *   D is incorrect: O(2n) simplifies to O(n) and does not describe nested iteration.

---

**Question 2**
Which of the following is the most accurate definition of **amortized analysis** in the context of data structures and algorithms?
*   A) The process of analyzing the average-case cost of a single operation by assuming all inputs are equally likely.
*   B) A technique that calculates the total cost of a sequence of operations and distributes it evenly across each operation, giving the average cost per operation even when individual operations vary widely in cost.
*   C) A method of proving an algorithm is optimal by establishing a lower bound on any possible solution to the same problem.
*   D) An analysis that measures how much additional heap memory a recursive algorithm consumes beyond its input data.
*   **Correct Answer:** B) A technique that calculates the total cost of a sequence of operations and distributes it evenly across each operation, giving the average cost per operation even when individual operations vary widely in cost.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes average-case analysis, which considers probability distributions over inputs — distinct from amortized analysis.
    *   *Why B is correct:* Amortized analysis looks at total cost over a sequence (e.g., n appends to a dynamic array) and spreads the occasional expensive operation (resize) across all operations to get O(1) per operation.
    *   *Why C is incorrect:* That describes lower-bound or optimality proofs (e.g., Omega notation arguments), not amortized analysis.
    *   *Why D is incorrect:* That describes auxiliary space complexity for recursive calls, which is a separate concept.

---

**Question 3**
An algorithm's runtime doubles each time the input size increases by one element. What is its time complexity?
*   A) O(n²)
*   B) O(n log n)
*   C) O(2ⁿ)
*   D) O(log n)
*   **Correct Answer:** C) O(2ⁿ)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* O(n²) grows polynomially; doubling per element increase is exponential growth.
    *   *Why B is incorrect:* O(n log n) is sub-quadratic, far slower-growing than doubling per element.
    *   *Why C is correct:* If runtime = 2^n, then adding one element doubles the work — the defining characteristic of exponential complexity.
    *   *Why D is incorrect:* O(log n) shrinks per step (halving), the opposite growth pattern.

---

**Question 4**
You are solving a LeetCode problem and notice your recursive solution has the recurrence T(n) = 2T(n/2) + O(n). According to the Master Theorem, what is the time complexity?
*   A) O(n)
*   B) O(n log n)
*   C) O(n²)
*   D) O(log n)
*   **Correct Answer:** B) O(n log n)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* O(n) would require the divide step to do O(1) work, not O(n).
    *   *Why B is correct:* T(n) = 2T(n/2) + O(n) matches Master Theorem Case 2 (a=2, b=2, f(n)=n, log_b(a)=1 = degree of f(n)), yielding O(n log n). This is the complexity of merge sort.
    *   *Why C is incorrect:* O(n²) would arise from T(n) = n·T(n-1) or similar quadratic recurrences.
    *   *Why D is incorrect:* O(log n) applies when the problem is halved and only constant work is done at each level.

---

**Question 5**
Which of the following correctly orders these complexity classes from fastest (best) to slowest (worst) for large n?
*   A) O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
*   B) O(log n) < O(1) < O(n) < O(n²) < O(n log n) < O(2ⁿ)
*   C) O(1) < O(n) < O(log n) < O(n log n) < O(2ⁿ) < O(n²)
*   D) O(1) < O(log n) < O(n log n) < O(n) < O(n²) < O(2ⁿ)
*   **Correct Answer:** A) O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the standard ordering every interviewer expects you to know. Constant time is fastest; exponential is slowest for large n.
    *   *Why B is incorrect:* O(1) is always faster than O(log n); swapping them is wrong.
    *   *Why C is incorrect:* O(log n) grows more slowly than O(n); placing O(n) before O(log n) is incorrect.
    *   *Why D is incorrect:* O(n) grows more slowly than O(n log n); placing O(n log n) before O(n) is incorrect.
