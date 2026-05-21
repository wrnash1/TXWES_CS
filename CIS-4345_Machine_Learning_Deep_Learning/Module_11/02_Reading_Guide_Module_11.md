# Reading Guide: Module 11 - Model Evaluation: Metrics, Confusion Matrix, ROC
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 11 - Model Evaluation: Metrics, Confusion Matrix, ROC**! Accuracy alone is not sufficient to evaluate a model — especially on imbalanced datasets where one class dominates. This module covers the full evaluation toolkit: the confusion matrix to understand where errors occur, precision and recall to balance false positive and false negative costs, the F1 score to combine them, and the ROC curve / AUC to assess classifier performance across all decision thresholds.

Understanding these metrics is essential for both the TensorFlow Developer Certificate exam and real-world ML deployments, where the cost of a false negative (e.g., missing a cancer diagnosis) may be very different from the cost of a false positive.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Confusion matrix**: A 2×2 table (for binary classification) that breaks down model predictions into four categories: True Positives (TP — correct positive predictions), True Negatives (TN — correct negative predictions), False Positives (FP — negative samples predicted as positive), and False Negatives (FN — positive samples predicted as negative). The matrix reveals which types of errors the model is making, which accuracy alone cannot show.

*   **Precision**: The fraction of positive predictions that are actually correct: `Precision = TP / (TP + FP)`. A high-precision model rarely raises a false alarm. Use precision when the cost of a false positive is high (e.g., spam detection — you don't want real email classified as spam).

*   **Recall (Sensitivity)**: The fraction of actual positives that the model correctly identified: `Recall = TP / (TP + FN)`. A high-recall model catches most of the true positives. Use recall when the cost of a false negative is high (e.g., disease screening — missing a case is dangerous).

*   **F1 score**: The harmonic mean of precision and recall: `F1 = 2 * (Precision * Recall) / (Precision + Recall)`. The F1 score is the preferred single metric when precision and recall are both important and the dataset is imbalanced. It penalizes extreme imbalances between precision and recall more than the arithmetic mean would.

*   **ROC curve and AUC**: The Receiver Operating Characteristic (ROC) curve plots True Positive Rate (Recall) on the y-axis against False Positive Rate on the x-axis across all possible classification thresholds. The Area Under the Curve (AUC) summarizes the entire ROC curve as a single number between 0 and 1 — an AUC of 1.0 is a perfect classifier; AUC of 0.5 is no better than random guessing. A higher AUC means the model ranks positive samples above negative samples more reliably.

*   **Class imbalance**: A dataset condition where one class has significantly more samples than the other (e.g., 95% negative, 5% positive). A naive model that predicts the majority class for every sample achieves 95% accuracy but is completely useless. In imbalanced settings, precision, recall, F1, and AUC are more meaningful metrics than accuracy alone.

---

### 2. Certification Exam Tips
*   **Metrics in Keras:** `model.compile(metrics=['accuracy'])` tracks accuracy. For precision and recall in Keras: `tf.keras.metrics.Precision()` and `tf.keras.metrics.Recall()`. These can be passed as a list to `metrics=` in `model.compile()`.
*   **Classification Report:** The scikit-learn `classification_report(y_true, y_pred)` function prints precision, recall, F1 score, and support for every class — the most efficient way to get a full evaluation summary. Know how to read its output.
*   **Threshold Tuning:** The default classification threshold for sigmoid output is 0.5. Lowering the threshold (e.g., to 0.3) increases recall but decreases precision. Raising it does the opposite. The ROC curve visualizes this tradeoff across all thresholds.
*   **Study Resource:** The [scikit-learn metrics documentation](https://scikit-learn.org/stable/modules/model_evaluation.html) at scikit-learn.org provides the definitive reference for all classification metrics including confusion matrices, precision/recall curves, and ROC/AUC — it is free and includes runnable code examples. The [TensorFlow classification tutorial](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data) at tensorflow.org covers handling class imbalance with metrics beyond accuracy.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the [scikit-learn metrics guide](https://scikit-learn.org/stable/modules/model_evaluation.html) covering classification metrics, and work through the [TensorFlow imbalanced data tutorial](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data). These free resources cover the confusion matrix, precision/recall, F1, ROC/AUC, and class weighting.
*   **Required Video:** Watch the model evaluation lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers confusion matrix interpretation, the precision-recall tradeoff, and how to compute ROC/AUC in Python.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Generate a confusion matrix**: After training a binary classifier, call `sklearn.metrics.confusion_matrix(y_true, y_pred)` and visualize it with `sklearn.metrics.ConfusionMatrixDisplay`. Identify TP, TN, FP, and FN counts.
*   **Compute classification metrics**: Use `sklearn.metrics.classification_report(y_true, y_pred)` to print precision, recall, and F1 score per class. Compare against the accuracy reported by `model.evaluate()`.
*   **Plot a ROC curve**: Use `sklearn.metrics.roc_curve(y_true, y_scores)` with predicted probabilities (not class labels) and `sklearn.metrics.roc_auc_score()`. Plot the curve with matplotlib and annotate the AUC value.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and calculate precision, recall, and F1 by hand from a sample confusion matrix.
*   [ ] Review the [scikit-learn classification metrics guide](https://scikit-learn.org/stable/modules/model_evaluation.html) and work through the [TensorFlow imbalanced data tutorial](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data).
*   [ ] Watch the model evaluation lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 11 lab: confusion matrix, classification report, and ROC curve for a binary classifier.
*   [ ] Proceed to the Module 11 quiz.
