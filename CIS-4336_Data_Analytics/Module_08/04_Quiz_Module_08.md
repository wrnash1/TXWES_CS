# Quiz: Module 08 — Data Mining and Predictive Techniques

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 20 (2 points each)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Instructions

Select the single best answer for each question. Each question is worth 2 points. No partial credit.

---

## Question 1

Which of the following best describes unsupervised learning?

A. A model trained on labeled data to predict output values for new inputs

B. A model that discovers hidden structure in data without predefined output labels

C. A model that uses a training set and a test set to evaluate classification accuracy

D. A model that predicts a continuous numeric output using regression coefficients

**Correct Answer:** B — Unsupervised learning finds patterns in unlabeled data. Option A describes supervised learning. Option C describes model evaluation methodology, not learning type. Option D describes regression, which is a supervised technique.

---

## Question 2

In the k-means algorithm, what happens during each iteration after initial centroid placement?

A. Each centroid is moved to the farthest data point from the cluster center

B. Each data point is assigned to the nearest centroid, then centroids are recalculated as cluster means

C. A new centroid is added for each cluster that exceeds the WCSS threshold

D. The algorithm removes data points that fall outside two standard deviations of the mean

**Correct Answer:** B — K-means alternates between assignment (each point to nearest centroid) and update (centroid to mean of assigned points) until convergence. Options A, C, and D do not describe any step of the k-means algorithm.

---

## Question 3

A decision tree model achieves 100% accuracy on training data but only 62% on test data. What problem does this indicate?

A. Underfitting — the model is too simple to capture patterns

B. Data leakage — test data was included in training

C. Overfitting — the model memorized training data and does not generalize

D. Class imbalance — the model is biased toward the majority class

**Correct Answer:** C — A large gap between training accuracy (100%) and test accuracy (62%) is the classic signature of overfitting. The model learned training noise rather than generalizable patterns. Underfitting shows low accuracy on both sets (A). Data leakage typically inflates test performance, not reduces it (B). Class imbalance distorts metrics but does not cause this training/test gap pattern (D).

---

## Question 4

Which metric should be prioritized when building a model to screen patients for a rare but treatable disease where missing a positive case has serious consequences?

A. Accuracy

B. Precision

C. Recall

D. Specificity

**Correct Answer:** C — Recall measures the proportion of actual positives correctly identified. Missing a diseased patient (false negative) is the costly error, so maximizing recall is critical. Accuracy is misleading with rare conditions (A). Precision penalizes false positives, not false negatives (B). Specificity measures the true negative rate, not sensitivity to positive cases (D).

---

## Question 5

A fraud detection model produces: TP = 45, TN = 900, FP = 55, FN = 10. What is the model's precision?

A. 45%

B. 55%

C. 82%

D. 90%

**Correct Answer:** A — `precision = TP / (TP + FP) = 45 / (45 + 55) = 45 / 100 = 45%`. Option B is the raw FP count, not precision. Option C applies an incorrect formula. Option D is closer to the overall accuracy figure.

---

## Question 6

In association rule mining, what does a lift value of 1.0 indicate?

A. The two items are perfectly correlated and always appear together

B. The two items are negatively associated and rarely appear together

C. The two items appear together no more often than would be expected by chance

D. The confidence of the rule equals the support of the consequent itemset

**Correct Answer:** C — `lift = confidence(A → B) / support(B)`. When lift = 1, the conditional probability of B given A equals the unconditional probability of B — the items are statistically independent. Lift > 1 means positive association (not what lift=1 describes, so A is wrong). Lift < 1 means negative association (B). Option D restates the lift formula imprecisely without capturing the independence meaning.

---

## Question 7

What is the primary advantage of random forests over a single decision tree?

A. Random forests are faster to train and require less memory

B. Random forests are fully interpretable — you can trace every prediction path

C. Random forests reduce overfitting by averaging across many diverse trees

D. Random forests do not require a training dataset

**Correct Answer:** C — By combining hundreds of trees trained on different bootstrap samples and feature subsets, random forests average out individual tree errors and dramatically reduce variance and overfitting. They are slower than single trees (A is wrong). They sacrifice interpretability compared to single trees (B is wrong). All supervised models require training data (D is wrong).

---

## Question 8

Given TP = 60, TN = 200, FP = 20, FN = 10, what is the F1 score?

A. F1 = 2 × (0.75 × 0.857) / (0.75 + 0.857) ≈ 0.80

B. F1 = (60 + 200) / (60 + 200 + 20 + 10) = 0.90

C. F1 = 60 / (60 + 20) = 0.75

D. F1 = 60 / (60 + 10) = 0.857

**Correct Answer:** A — `precision = 60/(60+20) = 0.75`. `recall = 60/(60+10) = 0.857`. `F1 = 2*(0.75*0.857)/(0.75+0.857) ≈ 0.80`. Option B computes overall accuracy. Option C computes precision alone. Option D computes recall alone.

---

## Question 9

Which split criterion is used by the CART decision tree algorithm?

A. Information gain (entropy reduction)

B. Gini impurity

C. Chi-square statistic

D. Pearson correlation coefficient

**Correct Answer:** B — CART (Classification and Regression Trees) uses Gini impurity as its split criterion. Information gain via entropy is used by ID3 and C4.5 algorithms (A). Chi-square is used in the CHAID algorithm (C). Pearson correlation is not a tree-splitting criterion (D).

---

## Question 10

A retail analyst finds: `support(milk) = 0.40`, `support(cereal) = 0.30`, `support(milk and cereal) = 0.18`. What is the confidence of the rule `{milk} → {cereal}`?

A. 0.18

B. 0.45

C. 0.60

D. 1.50

**Correct Answer:** B — `confidence(milk → cereal) = support(milk and cereal) / support(milk) = 0.18 / 0.40 = 0.45`. Option A is the raw joint support. Option C results from dividing by support(cereal) rather than support(milk). Option D is the lift value, not confidence.

---

End of Module 08 Quiz
