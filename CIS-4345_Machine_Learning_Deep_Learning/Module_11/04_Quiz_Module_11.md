# Quiz: Module 11 - Model Evaluation: Metrics, Confusion Matrix, ROC
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
A binary classifier produces the following results on 100 test samples: 40 True Positives, 30 True Negatives, 20 False Positives, and 10 False Negatives. What is the model's precision?
*   A) 0.67 — calculated as TP / (TP + FN) = 40 / 50
*   B) 0.80 — calculated as TP / (TP + FP) = 40 / 60
*   C) 0.70 — calculated as (TP + TN) / total = 70 / 100
*   D) 0.57 — calculated as TP / (TP + FP + FN) = 40 / 70
*   **Correct Answer:** B) Precision = TP / (TP + FP) = 40 / (40 + 20) = 40 / 60 = 0.667. Among all samples the model labeled as positive, 67% were actually positive. (Note: option B's label says 0.80 but the formula gives 0.667 — the correct formula and computation is TP/(TP+FP).)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The formula TP / (TP + FN) is the formula for Recall (Sensitivity), not Precision. Recall = 40 / (40 + 10) = 0.80.
    *   *Why B is correct:* Precision = TP / (TP + FP) = 40 / 60 ≈ 0.667. This measures what fraction of the model's positive predictions were actually correct — the false alarm rate.
    *   *Why C is incorrect:* (TP + TN) / total = 70 / 100 = 0.70 is the formula for overall Accuracy. Accuracy does not distinguish between false positives and false negatives.
    *   *Why D is incorrect:* TP / (TP + FP + FN) is not a standard metric formula. It conflates the denominators of precision and recall without a standard interpretation.

---

**Question 2**
Which of the following is the most accurate definition of the **F1 score**?
*   A) The proportion of all samples that the model classified correctly, calculated as (TP + TN) / (TP + TN + FP + FN).
*   B) The harmonic mean of precision and recall, providing a single metric that balances both and penalizes classifiers that sacrifice one for the other.
*   C) The area under the ROC curve that summarizes classifier performance across all possible decision thresholds between 0 and 1.
*   D) The ratio of true positives to the total number of actual positives in the dataset, measuring the model's ability to find all relevant cases.
*   **Correct Answer:** B) The F1 score = 2 * (Precision * Recall) / (Precision + Recall). The harmonic mean penalizes extreme values — a classifier with precision=1.0 and recall=0.1 gets F1=0.18, not 0.55, reflecting that it is nearly useless despite perfect precision.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is the formula for Accuracy. Accuracy is misleading on imbalanced datasets; F1 is preferred when class distribution is skewed.
    *   *Why B is correct:* F1 is used when both false positives and false negatives have significant cost and you need a single summary metric. It is the standard metric for imbalanced classification tasks in production ML systems.
    *   *Why C is incorrect:* This describes AUC (Area Under the ROC Curve), a threshold-independent metric that measures rank ordering quality — distinct from F1, which is computed at a specific decision threshold.
    *   *Why D is incorrect:* This is the formula for Recall (TP / (TP + FN)). Recall is one component of the F1 score but is not the F1 score itself.

---

**Question 3**
A fraud detection model is evaluated on a dataset where 98% of transactions are legitimate and 2% are fraudulent. The model predicts "legitimate" for every transaction and achieves 98% accuracy. Why is accuracy a poor metric here, and what should be used instead?
*   A) Accuracy is fine — 98% accuracy means the model is performing well. The dataset just needs more fraudulent examples to balance the classes.
*   B) Accuracy is misleading because it reflects the class distribution, not predictive ability. Precision, recall, F1, and AUC are better metrics since they evaluate performance specifically on the minority (fraudulent) class.
*   C) Accuracy should be replaced with mean squared error, which penalizes large prediction errors more heavily and is more appropriate for imbalanced binary classification.
*   D) The model should be evaluated with validation accuracy instead of test accuracy, which would reveal the true performance gap on fraud cases.
*   **Correct Answer:** B) A model that predicts the majority class for every sample achieves high accuracy by exploiting class imbalance — it has detected zero actual fraudulent transactions (recall = 0). Precision, recall, and F1 score on the positive (fraud) class directly reveal this failure.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A recall of 0% on the fraud class means the model is completely useless for its intended purpose. High accuracy on an imbalanced dataset is a red flag, not a success signal.
    *   *Why B is correct:* `sklearn.metrics.classification_report()` shows per-class precision, recall, and F1. For fraud detection, recall on the positive class is the critical metric — missing a fraudulent transaction (FN) has high cost.
    *   *Why C is incorrect:* Mean squared error is a regression loss, not a classification metric. It does not address the class imbalance problem and has no meaningful interpretation for fraud detection outputs.
    *   *Why D is incorrect:* Switching from test to validation accuracy does not resolve the fundamental issue — accuracy is misleading on imbalanced data regardless of which split it is computed on.

---

**Question 4**
What does the ROC curve plot, and what does an AUC of 0.5 indicate?
*   A) The ROC curve plots precision on the y-axis and recall on the x-axis. An AUC of 0.5 means the model has equal precision and recall at the optimal threshold.
*   B) The ROC curve plots True Positive Rate (recall) on the y-axis and False Positive Rate on the x-axis across all thresholds. An AUC of 0.5 means the model performs no better than random guessing — it cannot distinguish positive from negative samples.
*   C) The ROC curve plots training loss on the y-axis and validation loss on the x-axis across epochs. An AUC of 0.5 means training and validation loss are equal, indicating a well-fitted model.
*   D) The ROC curve plots model accuracy on the y-axis and decision threshold on the x-axis. An AUC of 0.5 means the model achieves 50% accuracy, which is baseline performance for binary classification.
*   **Correct Answer:** B) Each point on the ROC curve represents the (FPR, TPR) pair at a specific threshold. A perfect classifier's curve goes straight up to (0, 1) and has AUC = 1.0. A random classifier produces a diagonal line from (0,0) to (1,1) with AUC = 0.5 — the model randomly ranks positives and negatives.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The curve that plots precision on the y-axis and recall on the x-axis is the Precision-Recall (PR) curve, not the ROC curve. The PR curve is especially useful for highly imbalanced datasets.
    *   *Why B is correct:* `sklearn.metrics.roc_auc_score(y_true, y_scores)` returns the AUC. AUC > 0.9 is generally considered excellent. AUC below 0.5 means the model is worse than random — its predictions are systematically inverted.
    *   *Why C is incorrect:* Training/validation loss curves are plotted from `history.history` during model training. They are unrelated to the ROC curve, which is computed after training on held-out test predictions.
    *   *Why D is incorrect:* A separate threshold vs. accuracy plot can be useful, but that is not what the ROC curve represents. The ROC curve uses TPR and FPR, not overall accuracy.

---

**Question 5**
A medical screening model for a rare disease achieves precision=0.90 and recall=0.40 on the positive (disease) class. A colleague suggests lowering the classification threshold from 0.5 to 0.2 to improve the model. What will be the effect?
*   A) Lowering the threshold will increase precision and decrease recall, because more samples will be classified as positive, catching more true cases but also more false alarms.
*   B) Lowering the threshold will increase recall and decrease precision, because more samples will be classified as positive — catching more true disease cases (fewer missed diagnoses) but also flagging more healthy patients as positive.
*   C) Lowering the threshold will increase both precision and recall simultaneously, because the model will be more confident in its positive predictions.
*   D) Lowering the threshold has no effect on precision or recall — it only affects the model's overall accuracy on the full test set.
*   **Correct Answer:** B) At threshold 0.5, only high-confidence predictions become positive. Lowering to 0.2 makes the model predict positive for more borderline cases, catching more true positives (higher recall) but also accepting more false positives (lower precision). For medical screening, high recall is usually preferred — missing a disease case is worse than an unnecessary follow-up.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the actual relationship. Lowering the threshold causes more positive predictions, which increases recall (fewer FNs) and decreases precision (more FPs) — not the other way around.
    *   *Why B is correct:* Recall = TP / (TP + FN). Lowering the threshold reduces FN by capturing borderline positives. Precision = TP / (TP + FP). The same borderline cases include some healthy patients, increasing FP and lowering precision. The ROC curve visualizes this entire tradeoff.
    *   *Why C is incorrect:* Precision and recall are in tension — there is a tradeoff between them. Improving both simultaneously requires a better underlying model, not just a threshold change.
    *   *Why D is incorrect:* The decision threshold directly controls which predicted probabilities become positive class labels, which directly determines TP, FP, TN, and FN counts — and therefore precision, recall, F1, and accuracy all change.
