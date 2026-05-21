# Reading Guide: Module 02 - Python for ML
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 02 - Python for ML**! This week focuses on the three Python libraries that form the data layer beneath every TensorFlow model: NumPy for numerical arrays, Pandas for tabular data, and Matplotlib for visualization. Mastery of these tools is assumed on the TensorFlow Developer Certificate exam — you will need to preprocess datasets quickly and correctly before building any model.

As a student, you will learn how to manipulate multi-dimensional arrays with NumPy, load and clean structured data with Pandas, and visualize distributions and training curves with Matplotlib. These skills directly support every lab and exam task in this course.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **NumPy ndarray**: The fundamental N-dimensional array object in NumPy. All TensorFlow tensors interoperate with NumPy arrays, and most scikit-learn data pipelines pass data as ndarrays. Key attributes include `.shape`, `.dtype`, and `.reshape()`. Understanding array broadcasting — how NumPy applies operations across arrays of different shapes — is essential for writing efficient preprocessing code.

*   **Pandas DataFrame**: A two-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table. DataFrames are the standard way to load CSV files (`pd.read_csv()`), inspect data (`df.head()`, `df.describe()`), handle missing values (`df.fillna()`, `df.dropna()`), and encode categorical features before feeding data to a model.

*   **Matplotlib figure/axes**: The two-level hierarchy in Matplotlib where a `Figure` is the overall container and `Axes` is an individual plot within it. In ML workflows, Matplotlib is used to plot training/validation loss curves, feature distributions, and confusion matrices. The `plt.plot(history.history['loss'])` pattern appears on the TF exam.

*   **Feature scaling (normalization vs. standardization)**: Normalization rescales features to [0, 1] using min-max scaling; standardization (z-score) rescales to mean=0, std=1 using `(x - mean) / std`. Neural networks trained with gradient descent are highly sensitive to feature scale — unscaled inputs cause slow or failed convergence. Always fit scalers on training data only, then apply to test data.

*   **One-hot encoding**: Converting a categorical variable with K classes into K binary columns. For example, a color column with values {red, green, blue} becomes three columns. In Keras, `tf.keras.utils.to_categorical()` converts integer class labels to one-hot vectors for multi-class classification with `categorical_crossentropy` loss.

---

### 2. Certification Exam Tips
*   **TF Exam Data Prep:** The exam provides datasets as CSV files or built-in Keras datasets (e.g., `tf.keras.datasets.mnist.load_data()`). You must normalize pixel values to [0, 1] by dividing by 255.0 and reshape inputs to match the model's expected input shape.
*   **Common Pitfall:** A very frequent exam error is fitting a scaler or encoder on the full dataset before splitting, causing data leakage. Always use `scaler.fit(X_train)` then `scaler.transform(X_test)` — never `fit_transform` on the combined data.
*   **Keras History Object:** After `model.fit()`, the returned `history` object contains `history.history['loss']`, `history.history['val_loss']`, etc. Plotting these curves is a standard way to diagnose overfitting or underfitting on the exam.
*   **Study Resource:** The [Kaggle Python course](https://www.kaggle.com/learn/python) and [Kaggle Pandas course](https://www.kaggle.com/learn/pandas) are free, hands-on micro-courses that cover all the Python data manipulation skills expected on the TF Developer Certificate exam. Kaggle also provides free GPU-enabled notebooks for running TensorFlow code.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html) at numpy.org and the [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) guide at pandas.pydata.org. Both are free official documentation resources that cover the exact array and DataFrame operations used in ML preprocessing pipelines.
*   **Required Video:** Watch the Python for ML section of the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This freeCodeCamp video covers NumPy arrays, Pandas DataFrames, and Matplotlib visualization in the context of ML data preparation.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Load and inspect a CSV dataset**: Use `df = pd.read_csv('data.csv')` and examine `df.shape`, `df.dtypes`, and `df.isnull().sum()` to understand the data before preprocessing.
*   **Normalize numeric features**: Extract the feature matrix with `X = df[feature_cols].values`, then apply `X = (X - X.mean(axis=0)) / X.std(axis=0)` or use `sklearn.preprocessing.StandardScaler`.
*   **Visualize training history**: After training a model, plot `plt.plot(history.history['loss'], label='train')` and `plt.plot(history.history['val_loss'], label='val')` to assess convergence.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and explain each in your own words.
*   [ ] Complete the [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) and [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) tutorials.
*   [ ] Watch the Python for ML lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 02 lab: data loading, normalization, and visualization exercise.
*   [ ] Proceed to the Module 02 quiz.
