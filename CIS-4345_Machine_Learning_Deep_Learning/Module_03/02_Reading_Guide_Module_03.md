# Reading Guide: Module 03 - Linear and Logistic Regression
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 03 - Linear and Logistic Regression**! These two algorithms are the mathematical backbone of neural network output layers. Linear regression predicts continuous values using a weighted sum of inputs; logistic regression extends that to binary classification by passing the weighted sum through a sigmoid activation. Every dense output layer in Keras is doing exactly these operations — understanding regression first makes deep learning architecture choices intuitive.

As a student, you will learn how gradient descent minimizes the cost function for both algorithms, what the sigmoid function produces, and how to choose the right loss function and output activation for regression vs. classification tasks. These are foundational exam concepts.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Linear regression**: A supervised learning algorithm that models the relationship between input features and a continuous output variable as a weighted linear combination: y = w·x + b. The model is trained by minimizing Mean Squared Error (MSE) using gradient descent. In Keras, a single Dense(1) output layer with no activation function implements linear regression.

*   **Logistic regression**: A supervised classification algorithm that applies the sigmoid function to a linear combination of inputs to produce a probability between 0 and 1. The decision boundary is a threshold (typically 0.5) applied to that probability. In Keras, a Dense(1, activation='sigmoid') output layer with binary_crossentropy loss implements logistic regression.

*   **Sigmoid function**: The mathematical function σ(x) = 1 / (1 + e^−x) that maps any real number to the range (0, 1). It is used as the output activation for binary classification tasks. Its gradient approaches zero for very large or very small inputs — the vanishing gradient problem — which is why ReLU is preferred for hidden layers.

*   **Cost function (loss function)**: A function that measures how far the model's predictions are from the true labels. For regression, Mean Squared Error (MSE) = mean((y_pred − y_true)²) is standard. For binary classification, Binary Crossentropy = −[y·log(p) + (1−y)·log(1−p)] is standard. Choosing the wrong loss for the task is a common exam pitfall.

*   **Gradient descent**: An iterative optimization algorithm that adjusts model weights in the direction that reduces the cost function. At each step, the gradient (partial derivative of the loss with respect to each weight) is computed and the weights are updated: w = w − learning_rate × gradient. In Keras this is handled by the optimizer passed to `model.compile()`.

---

### 2. Certification Exam Tips
*   **Output Activation Selection:** The TF exam frequently tests whether you choose the correct output activation and loss. Use `sigmoid` + `binary_crossentropy` for binary classification (2 classes), `softmax` + `categorical_crossentropy` (or `sparse_categorical_crossentropy`) for multi-class, and no activation + `mse` for regression.
*   **Dense Layer as Logistic Regression:** A single `Dense(1, activation='sigmoid')` layer trained with `binary_crossentropy` is logistic regression. Recognizing this equivalence helps you understand why Keras's API is designed the way it is.
*   **Metrics vs. Loss:** The `loss` argument to `model.compile()` is what gradient descent minimizes. The `metrics` argument (e.g., `metrics=['accuracy']`) is only for human reporting — it does not affect training. Students often confuse these.
*   **Study Resource:** The [fast.ai Practical Deep Learning for Coders](https://course.fast.ai/) course (free) covers regression and classification with neural networks from a hands-on perspective. Lesson 1 directly addresses the connection between logistic regression and neural network output layers tested on the TF Developer Certificate exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the [Keras Dense layer documentation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense) at tensorflow.org, focusing on the `activation` parameter and how it maps to regression vs. classification. Also review the [loss functions guide](https://www.tensorflow.org/api_docs/python/tf/keras/losses) to understand when each loss applies.
*   **Required Video:** Watch the Linear and Logistic Regression section of the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers gradient descent, MSE, and binary crossentropy with scikit-learn and TensorFlow implementations.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Train a linear regression model**: Build `model = tf.keras.Sequential([tf.keras.layers.Dense(1)])`, compile with `loss='mse'`, and fit on a continuous-output dataset. Inspect predicted vs. actual values.
*   **Train a logistic regression model**: Build `model = tf.keras.Sequential([tf.keras.layers.Dense(1, activation='sigmoid')])`, compile with `loss='binary_crossentropy', metrics=['accuracy']`, and fit on a binary classification dataset.
*   **Compare probability outputs**: Call `model.predict(X_test)` on the logistic model and examine the raw probability values before and after applying a 0.5 threshold to produce class labels.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and write the Keras code equivalent for each concept.
*   [ ] Review the [Keras losses guide](https://www.tensorflow.org/api_docs/python/tf/keras/losses) and [Dense layer docs](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense).
*   [ ] Watch the regression module in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 03 lab: linear and logistic regression with Keras.
*   [ ] Proceed to the Module 03 quiz.
