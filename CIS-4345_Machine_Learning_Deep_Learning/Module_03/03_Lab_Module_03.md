# Lab Activity: Module 03 - Logistic Regression
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

## Objective
Configure and verify systems matching the operational parameters of **Logistic Regression**.

---

## Prerequisites
*   Ensure you have access to a terminal or a runtime environment matching the course requirements (e.g., Linux, macOS, Windows, or a cloud/web terminal).
*   Ensure you have administrative privileges if required to install packages or configure system services.

---

## Step-by-Step Instructions
1. **Train logistic regression model**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
2. **Predict binary class output labels**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
3. **Analyze probability arrays using predict_proba()**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.

---

## Troubleshooting Guide
*   *Error:* `Permission Denied`
    * *Fix:* Remember to run administrative command sequences using `sudo` or execute with administrative privileges (e.g., Run as Administrator on Windows).
*   *Error:* `Command Not Found`
    * *Fix:* Verify your environmental path settings, or double-check if the utility package is installed.

---

## Deliverables
1. Document your completed steps with screenshots or terminal output logs showing successful execution.
2. Submit your completion report to your Canvas LMS assignment portal for grading.

---

## Part 9 — Challenge Exercise

### Challenge 1: Training Both Regression and Classification Models Side-by-Side

Use the Breast Cancer dataset to train a logistic regression model in Keras, then adapt it to a linear regression model predicting the mean radius feature as a continuous target. Compare training curves for both.

```python
import tensorflow as tf
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
X, y_cls = cancer.data, cancer.target

scaler = StandardScaler()
X_train, X_test, y_train_cls, y_test_cls = train_test_split(
    X, y_cls, test_size=0.2, random_state=42, stratify=y_cls
)
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

# Logistic regression model (binary classification)
clf = tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(X_train_s.shape[1],))
])
clf.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
hist_clf = clf.fit(X_train_s, y_train_cls, epochs=50, validation_split=0.15, verbose=0)

# Linear regression model (predict mean radius — feature index 0)
y_train_reg = X_train[:, 0]  # raw unscaled mean radius as target
y_test_reg  = X_test[:, 0]
reg = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(X_train_s.shape[1],))  # no activation = linear
])
reg.compile(optimizer='adam', loss='mse', metrics=['mae'])
hist_reg = reg.fit(X_train_s, y_train_reg, epochs=50, validation_split=0.15, verbose=0)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(hist_clf.history['loss'], label='Train Loss')
axes[0].plot(hist_clf.history['val_loss'], label='Val Loss', linestyle='--')
axes[0].set_title('Logistic Regression — Binary Crossentropy')
axes[0].set_xlabel('Epoch'); axes[0].legend()

axes[1].plot(hist_reg.history['loss'], label='Train MSE')
axes[1].plot(hist_reg.history['val_loss'], label='Val MSE', linestyle='--')
axes[1].set_title('Linear Regression — MSE Loss')
axes[1].set_xlabel('Epoch'); axes[1].legend()

plt.tight_layout()
plt.savefig('regression_comparison.png', dpi=100)
plt.show()

_, test_acc = clf.evaluate(X_test_s, y_test_cls, verbose=0)
_, test_mae = reg.evaluate(X_test_s, y_test_reg, verbose=0)
print(f'Classification test accuracy: {test_acc:.4f}')
print(f'Regression test MAE: {test_mae:.4f}')
```

1. Observe the scale difference between binary crossentropy loss values and MSE loss values — note that loss magnitude alone is not comparable across different loss functions.
2. Apply a 0.5 threshold to `clf.predict(X_test_s)` to produce class labels and compute accuracy manually using `np.mean(predictions == y_test_cls)`.

### Challenge 2: Effect of L2 Regularization on Overfitting

Train two logistic regression models — one without regularization and one with L2 regularization — and compare their training vs. validation accuracy curves.

```python
def build_logreg(l2_strength=0.0):
    reg_arg = tf.keras.regularizers.l2(l2_strength) if l2_strength > 0 else None
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(
            1, activation='sigmoid',
            input_shape=(X_train_s.shape[1],),
            kernel_regularizer=reg_arg
        )
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

hist_no_reg = build_logreg(0.0).fit(X_train_s, y_train_cls, epochs=100,
                                     validation_split=0.15, verbose=0)
hist_l2     = build_logreg(0.1).fit(X_train_s, y_train_cls, epochs=100,
                                     validation_split=0.15, verbose=0)

plt.figure(figsize=(10, 4))
plt.plot(hist_no_reg.history['accuracy'],     label='No Reg — Train', color='blue')
plt.plot(hist_no_reg.history['val_accuracy'], label='No Reg — Val',   color='blue',   linestyle='--')
plt.plot(hist_l2.history['accuracy'],         label='L2=0.1 — Train', color='orange')
plt.plot(hist_l2.history['val_accuracy'],     label='L2=0.1 — Val',   color='orange', linestyle='--')
plt.title('Logistic Regression: No Regularization vs L2=0.1')
plt.xlabel('Epoch'); plt.ylabel('Accuracy'); plt.legend()
plt.tight_layout(); plt.savefig('l2_comparison.png', dpi=100); plt.show()
```

1. At epoch 100, record the train-val accuracy gap for each model. Does L2 reduce overfitting?
2. Try `l2_strength=0.01` and `l2_strength=1.0` and observe how very strong regularization can cause underfitting.

### Reflection Questions

1. The logistic regression model in Keras is mathematically identical to a single-neuron neural network with sigmoid output. What does this imply about the expressive power of logistic regression compared to a multi-layer neural network?
2. In a medical diagnosis application where false negatives (missed disease cases) are far more dangerous than false positives, how would you adjust the decision threshold and which metrics would you report to hospital administrators?
