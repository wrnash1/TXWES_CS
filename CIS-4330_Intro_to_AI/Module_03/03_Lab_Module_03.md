# Lab Activity: Module 03 - Unsupervised Learning: Clustering and Dimensionality Reduction

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure
**Points:** 100
**Submission:** Canvas LMS — Module 03 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Trace the K-means algorithm step by step through two full iterations on a small dataset.
- Apply the elbow method to select an appropriate value of K.
- Interpret clustering evaluation metrics including WCSS and silhouette score.
- Explain the purpose and output of PCA.
- Match clustering and dimensionality reduction techniques to appropriate business scenarios.

---

## Prerequisites

No Azure subscription is required. All exercises are analytical and computational tasks performed by hand or with a basic calculator. You will need:

- Module 03 video lecture (completed).
- Module 03 reading guide (completed), including the K-means and PCA sections.
- A calculator or spreadsheet application for the distance calculations in Part A.

---

## Part A: K-means Manual Trace (40 points)

This exercise walks you through two complete iterations of the K-means algorithm on a two-dimensional dataset. This is the same process Azure ML performs internally at scale.

### Dataset

You have six data points in two-dimensional space. Each point has an x-coordinate and a y-coordinate.

| Point | x | y |
|---|---|---|
| P1 | 1 | 1 |
| P2 | 1 | 3 |
| P3 | 2 | 2 |
| P4 | 7 | 7 |
| P5 | 8 | 6 |
| P6 | 8 | 8 |

You will use K = 2 clusters. The initial centroids are:

- Centroid A: (1, 1) — same position as P1
- Centroid B: (8, 8) — same position as P6

### Step 1 — Compute Distances (Round to Two Decimal Places)

For each data point, compute the Euclidean distance to Centroid A (1,1) and to Centroid B (8,8).

Recall: Euclidean distance between (x1, y1) and (x2, y2) = square root of ((x2-x1) squared + (y2-y1) squared).

Complete the table:

| Point | Distance to A (1,1) | Distance to B (8,8) | Assigned Cluster |
|---|---|---|---|
| P1 (1,1) | ___ | ___ | ___ |
| P2 (1,3) | ___ | ___ | ___ |
| P3 (2,2) | ___ | ___ | ___ |
| P4 (7,7) | ___ | ___ | ___ |
| P5 (8,6) | ___ | ___ | ___ |
| P6 (8,8) | ___ | ___ | ___ |

### Step 2 — Update Centroids After Iteration 1

Based on the cluster assignments in Step 1, calculate the new position of each centroid as the mean of all points assigned to it.

**New Centroid A:** x-coordinate: ________ y-coordinate: ________
**New Centroid B:** x-coordinate: ________ y-coordinate: ________

Show your calculation:

**Centroid A calculation:** _______________
**Centroid B calculation:** _______________

### Step 3 — Compute Distances Using Updated Centroids

Using your new centroids from Step 2, compute the Euclidean distance from each point to each new centroid.

| Point | Distance to New A | Distance to New B | Assigned Cluster |
|---|---|---|---|
| P1 (1,1) | ___ | ___ | ___ |
| P2 (1,3) | ___ | ___ | ___ |
| P3 (2,2) | ___ | ___ | ___ |
| P4 (7,7) | ___ | ___ | ___ |
| P5 (8,6) | ___ | ___ | ___ |
| P6 (8,8) | ___ | ___ | ___ |

### Step 4 — Check for Convergence

Did any points change cluster assignment between Iteration 1 and Iteration 2?

**Your answer:** _______________

If no points changed assignment, the algorithm has converged. If points changed, another iteration would begin.

### Step 5 — Compute WCSS After Iteration 2

Calculate the WCSS (Within-Cluster Sum of Squares) for your final clustering. WCSS is the sum of squared distances between each point and its assigned centroid.

WCSS = sum of (each point's squared distance to its centroid)

**Show your calculation:**

**WCSS Cluster A:** _______________
**WCSS Cluster B:** _______________
**Total WCSS:** _______________

### Step 6 — Interpretation Questions (10 points)

Answer these questions in complete sentences.

**Question A:** Looking at the original data points, do the final clusters make intuitive sense? Describe what you would call each cluster if this were a real customer dataset.

**Question B:** If you ran K-means with K = 3 on this same dataset, would the WCSS be higher or lower than with K = 2? Explain why.

**Question C:** You run K-means five times on this dataset with different random initializations and get slightly different WCSS values: 2.33, 2.33, 2.33, 3.17, 2.33. Which result would you select and why?

---

## Part B: Elbow Method Application (20 points)

A data scientist runs K-means on a customer dataset with K = 1 through 8. The resulting WCSS values are:

| K | WCSS |
|---|---|
| 1 | 4800 |
| 2 | 2100 |
| 3 | 1050 |
| 4 | 950 |
| 5 | 870 |
| 6 | 820 |
| 7 | 790 |
| 8 | 775 |

### Question 7

Based on the WCSS values above, at which value of K does the elbow appear? Explain your reasoning using the rate of change between consecutive K values.

**Your answer:** _______________

### Question 8

Sketch (or describe in words) what the elbow plot would look like. Where is the curve steep, and where does it flatten?

**Your answer:** _______________

### Question 9

After selecting K based on the elbow method, a colleague suggests using a silhouette score to validate the choice. The silhouette scores for your K candidates are: K=2: 0.61, K=3: 0.74, K=4: 0.68, K=5: 0.55. Does the silhouette score agree with the elbow method? Which K would you select and why?

**Your answer:** _______________

### Question 10

The data scientist plans to present the clustering results to non-technical business leaders. Which K value would they argue is "correct"? Is there a single objectively correct answer? Explain.

**Your answer:** _______________

---

## Part C: PCA and Dimensionality Reduction (20 points)

Answer each question in complete sentences.

### Question 11

A dataset has 200 features per patient collected from electronic health records. A data scientist runs PCA and finds that the first 10 principal components explain 88% of the total variance. They decide to keep only these 10 components before training a logistic regression model.

Explain what "explains 88% of the total variance" means in plain language. What information is lost when the remaining 190 features are discarded?

**Your answer:** _______________

### Question 12

Why must features be standardized (scaled to mean 0, standard deviation 1) before applying PCA? What would happen if you applied PCA to a dataset where one feature is measured in dollars (range: 10,000-500,000) and another is measured as a binary flag (0 or 1)?

**Your answer:** _______________

### Question 13

A colleague suggests using t-SNE to preprocess a 300-feature dataset before training a random forest classifier. Evaluate this suggestion. Is t-SNE appropriate for this purpose? What technique should be used instead?

**Your answer:** _______________

---

## Part D: Scenario Matching (20 points)

For each scenario, recommend one technique from the following list: K-means Clustering, Hierarchical Clustering, DBSCAN, PCA, t-SNE, Isolation Forest.

Each technique may be used at most once. Provide a one-sentence justification for each choice.

### Scenario 14

A cybersecurity team has 10 million network connection records per day from normal operations. No labeled examples of attacks exist. The team wants to flag individual connections that are statistically unusual.

**Recommended technique:** _______________
**Justification:** _______________

### Scenario 15

A bioinformatics researcher has gene expression data with 15,000 genes (features) per patient. They want to visualize the structure of 500 patient samples in a 2D plot to identify whether cancer subtypes form natural visual groups.

**Recommended technique:** _______________
**Justification:** _______________

### Scenario 16

A retail company wants to segment 2 million customers into a small number of distinct groups for a targeted marketing campaign. The clusters should be interpretable and the number of segments is expected to be between 3 and 7.

**Recommended technique:** _______________
**Justification:** _______________

### Scenario 17

An urban planning department has GPS coordinate data on traffic incidents in a city. The incident locations form irregular clusters — some neighborhoods have dense clusters of incidents, others have scattered single events. The team wants an algorithm that does not require specifying the number of clusters and will automatically identify noise points.

**Recommended technique:** _______________
**Justification:** _______________

---

## Answer Key and Grading Rubric

### Part A (30 points for Steps 1-5, 10 points for Step 6 questions)

**Step 1 distances (rounded to 2 decimal places):**

- P1: Dist to A = 0.00, Dist to B = 9.90, Assigned to A
- P2: Dist to A = 2.00, Dist to B = 7.62, Assigned to A
- P3: Dist to A = 1.41, Dist to B = 8.49, Assigned to A
- P4: Dist to A = 8.49, Dist to B = 1.41, Assigned to B
- P5: Dist to A = 9.22, Dist to B = 2.00, Assigned to B
- P6: Dist to A = 9.90, Dist to B = 0.00, Assigned to B

**Step 2 updated centroids:**

- New Centroid A: mean of P1(1,1), P2(1,3), P3(2,2) = x=(1+1+2)/3=1.33, y=(1+3+2)/3=2.00. New A = (1.33, 2.00)
- New Centroid B: mean of P4(7,7), P5(8,6), P6(8,8) = x=(7+8+8)/3=7.67, y=(7+6+8)/3=7.00. New B = (7.67, 7.00)

**Step 3:** All points maintain same cluster assignments as in Step 1. Convergence is reached.

**Step 4:** No points changed assignment. Algorithm converged after Iteration 2.

**Step 5 WCSS:** Full credit requires showing squared distances for each point to its centroid and summing. Approximate correct answer: WCSS cluster A ~ 2.89, cluster B ~ 2.89, total ~ 5.78. Accept values within rounding tolerance.

Scoring Part A steps 1-5: 4 points each step = 20 points. Step 6 questions: Q A 3 pts + Q B 4 pts + Q C 3 pts = 10 pts.

**Step 6 answers:** Q A: Cluster A = lower-left points (small values) — could be "budget/entry-level customers." Cluster B = upper-right points (large values) — "premium customers." Q B: WCSS would be lower because adding clusters always decreases WCSS. Q C: Select the result with WCSS = 2.33 (the most common and lowest value). It represents the global optimum; the 3.17 result was a poor local optimum from a bad initialization.

### Part B (5 points per question = 20 points)

**Q7:** K=3. The WCSS drops 2700 from K=1 to K=2, then 1050 to K=2, then only 100 from K=3 to K=4. The elbow is at K=3.

**Q8:** Steep descent from K=1 to K=3; then nearly flat from K=4 onward.

**Q9:** Silhouette agrees: K=3 has the highest silhouette score (0.74). Select K=3, supported by both methods.

**Q10:** No single objectively correct answer. Business context determines the most useful K. The data scientist would recommend K=3 but acknowledge the business team may prefer K=5 for operational reasons.

### Part C (6-7 points per question, total 20 points)

**Q11:** 88% variance explained means the 10 components capture 88% of the information content (variability) in the original 200 features. The lost 12% represents information not captured — potentially subtle feature interactions or rare patterns. For most tasks, retaining 88% is sufficient.

**Q12:** Without standardization, PCA would be dominated by the high-variance dollar feature and would effectively ignore the binary flag. Features must be on the same scale to contribute equally to the variance calculation.

**Q13:** t-SNE is inappropriate for preprocessing before model training. It is computationally expensive, non-deterministic, and its output distances are not meaningful for distance-based learning. Use PCA for dimensionality reduction as a preprocessing step before the random forest.

### Part D (5 points per scenario = 20 points)

**Scenario 14:** Isolation Forest. Unsupervised anomaly detection on large unlabeled datasets without labeled attack examples.

**Scenario 15:** t-SNE. 2D visualization of high-dimensional data to reveal cluster structure.

**Scenario 16:** K-means. Large dataset, small expected number of interpretable clusters, standard business segmentation use case.

**Scenario 17:** DBSCAN. Irregular cluster shapes, does not require specifying K, automatically identifies noise points.

---

## Deliverable

Submit a single document (PDF or Word) containing all calculations, answers, and justifications. Show your work for all distance calculations in Part A. Include your name, course section, and date at the top. Upload to the Module 03 Lab Assignment in Canvas by the posted due date.
