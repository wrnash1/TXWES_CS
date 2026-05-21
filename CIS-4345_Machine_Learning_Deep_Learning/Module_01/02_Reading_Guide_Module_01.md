# Reading Guide: Module 01 - ML Fundamentals
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 01 - ML Fundamentals**! This week you will build the foundational vocabulary and conceptual framework needed for the entire course. Understanding the three core learning paradigms — supervised, unsupervised, and reinforcement learning — is essential context for every TensorFlow model you will build throughout this course and on the TensorFlow Developer Certificate exam.

As a student, you will learn how machine learning differs from traditional rule-based programming, how data flows through an ML pipeline from raw collection to trained model, and how to reason about when each learning paradigm applies. These concepts underpin every Keras model architecture you will encounter.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Supervised learning**: A machine learning paradigm in which a model is trained on labeled input-output pairs. The model learns a mapping function from features (X) to target labels (y), and is evaluated on how well it predicts labels for unseen examples. Classification and regression are both supervised tasks.

*   **Unsupervised learning**: A machine learning paradigm in which the model receives only input features with no corresponding labels. The algorithm discovers hidden structure in the data on its own, such as natural groupings (clustering) or reduced representations (dimensionality reduction).

*   **Reinforcement learning**: A learning paradigm in which an agent takes actions in an environment to maximize a cumulative reward signal. Unlike supervised learning, there is no fixed dataset of correct answers — the agent learns from trial and error feedback.

*   **Train-test split**: The practice of dividing a labeled dataset into a training partition (used to fit the model) and a held-out test partition (used only for final evaluation). A common ratio is 80% train / 20% test. This prevents the model from simply memorizing training data, and gives an unbiased performance estimate on genuinely unseen examples.

*   **Feature engineering**: The process of transforming raw input variables into a representation more suitable for a machine learning model. Examples include normalizing numerical values, one-hot encoding categorical variables, and creating polynomial interaction terms. High-quality features often matter more than the choice of algorithm.

*   **Overfitting**: When a model learns the training data too precisely — including its noise — and loses the ability to generalize to new examples. Overfitting is diagnosed by a large gap between training accuracy and validation accuracy.

---

### 2. Certification Exam Tips
*   **TF Exam Scope:** The TensorFlow Developer Certificate exam requires you to build, train, and evaluate Keras models in a timed Google Colab or local environment. The exam tests practical coding ability, not multiple-choice recall — expect to write real `tf.keras` model definitions, compile steps, and `model.fit()` calls.
*   **Key Exam Tasks:** The four main task categories on the exam are (1) image classification with CNNs, (2) NLP/text classification, (3) time-series regression, and (4) basic dense networks. Knowing which learning paradigm applies to each task is foundational.
*   **Keras API Pattern:** The exam consistently uses the Sequential API: `model = tf.keras.Sequential([...])`, followed by `model.compile(optimizer=, loss=, metrics=)`, then `model.fit(X_train, y_train, epochs=, validation_data=)`. Memorize this three-step pattern.
*   **Study Resource:** The official TensorFlow Developer Certificate candidate handbook describes the exam format in detail. The free [TensorFlow tutorials at tensorflow.org](https://www.tensorflow.org/tutorials) cover all four task categories tested on the exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Review the [TensorFlow Core Concepts overview](https://www.tensorflow.org/guide) at tensorflow.org/guide — specifically the sections on tensors, variables, and the overall computation model. This free official documentation is one of the primary study materials for the certification exam.
*   **Required Video:** Watch the introductory video lecture on ML Fundamentals in the official course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This playlist from freeCodeCamp covers the full ML pipeline from data loading through model evaluation using scikit-learn and TensorFlow.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Set up the ML project environment**: Install TensorFlow, scikit-learn, NumPy, and Pandas in a Google Colab notebook. Verify installations with `import tensorflow as tf; print(tf.__version__)`.
*   **Load and inspect a dataset**: Use `sklearn.datasets.load_iris()` or a CSV file loaded with `pd.read_csv()` to examine feature shapes, data types, and class distributions.
*   **Perform a train-test split**: Apply `sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)` and verify the resulting partition sizes.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence explanation of each.
- [ ] Review the [TensorFlow Guide](https://www.tensorflow.org/guide) introduction and [Keras overview](https://www.tensorflow.org/guide/keras).
- [ ] Watch the ML Fundamentals lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
- [ ] Complete the Module 01 lab: environment setup and train-test split exercise.
- [ ] Proceed to the Module 01 quiz.
