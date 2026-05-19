# Quiz: Module 04 - Regularization Techniques
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Question 1
How does L1 regularization (Lasso) differ from L2 regularization (Ridge)?

*   A) L1 adds squared penalties, L2 adds absolute penalties
*   B) L1 can force feature weights exactly to zero, performing feature selection
*   C) L2 is only used in unsupervised learning
*   D) L1 increases model training time by 10x

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Lasso adds an absolute weight penalty to the cost, leading to sparse coefficients (forces unimportant features to 0).

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Ridge uses squared penalties (L2) and shrinks weights close to but not exactly to 0.
