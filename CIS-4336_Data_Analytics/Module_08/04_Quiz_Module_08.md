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

---

## Question 11 (5 points)

Given TP = 80, TN = 750, FP = 20, FN = 50, what is the model's recall?

A. 80%

B. 61.5%

C. 97.4%

D. 91.1%

**Correct Answer:** B — `recall = TP / (TP + FN) = 80 / (80 + 50) = 80 / 130 ≈ 61.5%`. Option A is the raw TP count, not a computed rate. Option C is precision: 80/(80+20)=80%. Option D is accuracy: (80+750)/(80+750+20+50)=830/900≈92.2%, which does not match any option exactly; closest is 91.1%.

---

## Question 12 (5 points)

What is the purpose of the elbow method in k-means clustering?

A. To determine the optimal learning rate for gradient descent

B. To select the number of clusters k where adding more clusters yields diminishing reduction in WCSS

C. To identify the maximum depth parameter for a decision tree

D. To choose the threshold probability for converting predicted probabilities to class labels

**Correct Answer:** B — The elbow method plots WCSS (within-cluster sum of squares) against k. The optimal k is at the "elbow" — the point beyond which additional clusters provide little improvement in WCSS reduction. Options A, C, and D describe hyperparameter selection for other algorithms, not k-means cluster count selection.

---

## Question 13 (5 points)

In a confusion matrix, False Negatives (FN) represent which outcome?

A. The model correctly predicts a positive case

B. The model incorrectly predicts a negative case when the actual label is positive

C. The model incorrectly predicts a positive case when the actual label is negative

D. The model correctly predicts a negative case

**Correct Answer:** B — A False Negative occurs when the model predicts negative (no event) but the actual label is positive (event exists). This is the "missed detection" error. Option A describes True Positive. Option C describes False Positive. Option D describes True Negative.

---

## Question 14 (5 points)

A bank's credit scoring model has R-squared = 0.91. What does this mean?

A. The model correctly classifies 91% of customers as low or high risk

B. 91% of the variance in loan default rates is explained by the predictors in the regression model

C. The model produces 91% precision on test data

D. The model's coefficients are statistically significant at the 9% level

**Correct Answer:** B — R-squared measures the proportion of variance in the dependent variable explained by the model's predictors. R-squared = 0.91 means 91% of the variability in the outcome is accounted for by the input features. It does not measure classification accuracy (A), precision (C), or statistical significance of coefficients (D).

---

## Question 15 (5 points)

Why does Adjusted R-squared decrease when an irrelevant predictor is added to a regression model?

A. Because adding variables always reduces model accuracy

B. Because Adjusted R-squared penalizes for the number of predictors, so adding an unhelpful variable reduces the adjusted score even if raw R-squared increases slightly

C. Because the OLS algorithm removes irrelevant variables from the model

D. Because more predictors reduce the degrees of freedom to zero

**Correct Answer:** B — Raw R-squared can only increase (or stay the same) when predictors are added, even useless ones. Adjusted R-squared applies a penalty proportional to the number of predictors (k) relative to sample size (n), so adding a variable that does not improve fit decreases the adjusted score. Options A and C are incorrect; OLS does not remove variables automatically. Option D overstates the effect.

---

## Question 16 (5 points)

An association rule has support = 0.05, confidence = 0.60, and lift = 2.4. What is the most accurate business interpretation?

A. 5% of all transactions contain both items; when item A is purchased, item B is purchased 60% of the time; this co-occurrence is 2.4 times more likely than if the items were independent

B. The rule applies to 60% of transactions with a 5% confidence

C. The model is 5% accurate and needs improvement

D. Lift of 2.4 means item B causes 2.4 times more revenue when purchased with item A

**Correct Answer:** A — Support (0.05) = the proportion of all transactions containing both items. Confidence (0.60) = the probability B is purchased given A is purchased. Lift (2.4 > 1) = the co-occurrence is 2.4 times more likely than by chance, indicating a meaningful positive association. Options B, C, and D misinterpret the metrics.

---

## Question 17 (5 points)

Which technique is used to prevent a single decision tree from overfitting when building a random forest?

A. Increasing the tree depth to fit every training sample perfectly

B. Training each tree on a bootstrap sample of the data and considering only a random subset of features at each split

C. Using the full feature set for every tree to ensure maximum information

D. Running the same tree multiple times and selecting the best result by validation accuracy

**Correct Answer:** B — Random forests prevent overfitting through two mechanisms: (1) bootstrap sampling — each tree sees a random subset of training rows, and (2) random feature selection — each split considers only a subset of features. Together, these ensure trees are diverse and uncorrelated, so their averaged predictions generalize better. Options A and C describe approaches that would increase overfitting. Option D describes model selection, not ensemble construction.

---

## Question 18 (5 points)

A model produces TP = 10, TN = 980, FP = 5, FN = 5. What is the accuracy, and why might this metric be misleading?

A. Accuracy = 99%; it is misleading because the dataset is heavily imbalanced — a model that always predicts "negative" would achieve 98.5% accuracy without detecting a single positive case

B. Accuracy = 95%; it is misleading because precision is higher than recall

C. Accuracy = 50%; the model is performing at chance level

D. Accuracy = 99%; it is not misleading because high accuracy always indicates a good model

**Correct Answer:** A — `accuracy = (10 + 980) / (10 + 980 + 5 + 5) = 990/1000 = 99%`. With only 15 actual positives out of 1,000 cases, a naive model predicting "no" always would achieve 98.5% accuracy. The high accuracy masks poor recall (10 of 15 positives detected = 66.7%), which matters in applications like disease detection. Option D is wrong because accuracy is misleading for imbalanced classes.

---

## Question 19 (5 points)

Which of the following statements correctly distinguishes classification from regression in supervised learning?

A. Classification predicts a continuous numeric output; regression assigns observations to discrete categories

B. Classification assigns observations to discrete class labels; regression predicts a continuous numeric output

C. Classification uses decision trees only; regression uses neural networks only

D. There is no meaningful difference — both tasks use identical loss functions and output formats

**Correct Answer:** B — Classification outputs a discrete class label (e.g., spam/not spam, yes/no, category A/B/C). Regression outputs a continuous numeric value (e.g., price, temperature, sales revenue). Option A reverses the definitions. Options C and D are factually incorrect — both tasks support many algorithm types.

---

## Question 20 (5 points)

In the Apriori algorithm, the anti-monotonicity property means:

A. Itemsets with higher support are always more useful than those with lower support

B. If an itemset is infrequent (below minimum support), all supersets containing it are also infrequent and can be pruned

C. Association rules must be listed in descending order of lift to be valid

D. Support for itemsets decreases as transaction volume increases

**Correct Answer:** B — Anti-monotonicity is the key efficiency property of the Apriori algorithm. If {milk} is below the minimum support threshold, then {milk, cereal}, {milk, bread}, and all larger itemsets containing milk are also below threshold. This allows the algorithm to prune the search space exponentially rather than evaluating all possible item combinations. Options A, C, and D do not describe the anti-monotonicity property.

---

End of Module 08 Quiz
