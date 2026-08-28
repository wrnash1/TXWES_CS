# Reading Guide: Module 03 - Linear and Logistic Regression

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4345 &BULL; MACHINE LEARNING & DEEP LEARNING SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

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

---

## 9. Supplemental Resources

**1. fast.ai Practical Deep Learning for Coders — Lesson 1**
<https://course.fast.ai/Lessons/lesson1.html>
Free hands-on course that covers logistic regression, binary crossentropy, and the connection between classical regression and neural network output layers. Lesson 1 directly maps to the regression and classification tasks tested on the TF Developer Certificate exam.

**2. Keras Loss Functions API Reference**
<https://www.tensorflow.org/api_docs/python/tf/keras/losses>
Official TensorFlow documentation listing every built-in loss function with mathematical definitions and usage examples. Essential for correctly pairing output activations with loss functions across regression, binary classification, and multi-class classification tasks.

**3. StatQuest: Logistic Regression (YouTube)**
<https://www.youtube.com/watch?v=yIYKR4sgzI8>
Clear visual explanation of the sigmoid function, log-odds, and binary crossentropy from first principles. Covers why MSE is a poor choice for classification and how the logistic loss surface ensures convexity — the conceptual foundation behind Module 03's key exam tips.
