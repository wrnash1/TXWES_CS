# Quiz: Module 02 - Python for ML

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Instructions:** Select the single best answer for each question. Each question is worth 10 points (100 points total). Align your study to the TensorFlow Developer Certificate objectives at tensorflow.org/certificate.

---

## Question 1

A developer writes the following code to normalize features before training. What is the critical error in this approach?

```python
scaler = StandardScaler()
X_all_scaled = scaler.fit_transform(X)   # fit on entire dataset
X_train = X_all_scaled[:800]
X_test  = X_all_scaled[800:]
```

- A) `StandardScaler` is not compatible with NumPy arrays and requires a DataFrame input.
- B) The scaler was fitted on the full dataset including test samples, causing data leakage.
- C) `fit_transform` cannot be called on a 2D array and must be called on a 1D array.
- D) The split should use indices 0:900 and 900: rather than 0:800 and 800:.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Calling `fit_transform` on the full dataset before splitting means the scaler learned the mean and standard deviation from test samples. The test set should represent unseen data, but here the scaler has already "seen" it and incorporated its statistics. This is data leakage — it produces falsely optimistic test metrics because the test features were inadvertently included in the preprocessing fit.
- *Why A is incorrect:* `StandardScaler` accepts NumPy arrays natively. It does not require a DataFrame; `fit_transform(X)` where X is a 2D NumPy array is the standard usage.
- *Why C is incorrect:* `fit_transform` operates correctly on 2D arrays. The shape requirement for `StandardScaler` is that the input is at least 2D — a 1D array would actually need to be reshaped.
- *Why D is incorrect:* The choice of split index is a separate concern and not the error highlighted here. The data leakage issue exists regardless of where the split falls.

---

## Question 2

What does the `axis` parameter control in `X.mean(axis=0)` when `X` has shape `(1000, 20)`?

- A) It computes the mean across all 20,000 elements and returns a single scalar.
- B) It computes the mean of each row, returning a 1D array of shape `(1000,)`.
- C) It computes the mean of each column across all 1000 rows, returning a 1D array of shape `(20,)`.
- D) It sorts the array along the first dimension before computing the mean.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* `axis=0` tells NumPy to reduce along dimension 0 — which is the rows. For each of the 20 columns, the operation collapses all 1000 row values into a single mean. The result is shape `(20,)` — one mean per feature. This is the standard way to compute feature-wise statistics for preprocessing.
- *Why A is incorrect:* A global mean with no axis argument returns a scalar. Specifying `axis=0` restricts the reduction to one dimension only.
- *Why B is incorrect:* `axis=1` computes a mean per row (reducing across columns), producing shape `(1000,)`. The question asks about `axis=0`, which is the opposite.
- *Why D is incorrect:* `np.sort()` handles sorting; `mean()` does not sort. The `axis` parameter only specifies the dimension along which the aggregation occurs.

---

## Question 3

A developer builds a `tf.data.Dataset` pipeline with the following code. What is wrong with the order of operations?

```python
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
dataset = dataset.batch(32).shuffle(1000).prefetch(1)
```

- A) `prefetch` must come before `batch` to avoid idle GPU time.
- B) `shuffle` is called after `batch`, which only randomizes the batch order rather than the individual sample order within the dataset.
- C) `from_tensor_slices` does not accept tuple inputs and requires X and y to be passed separately.
- D) A buffer size of 1000 is invalid; only `tf.data.AUTOTUNE` is accepted as a buffer size argument.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* When `shuffle` is called after `batch`, TensorFlow shuffles the order of batches, not the order of individual samples. Samples within each batch remain in their original sequential order, introducing ordering bias. The correct sequence is `.shuffle()` then `.batch()` then `.prefetch()`.
- *Why A is incorrect:* `prefetch` does belong after `batch`, as shown. Its purpose is to overlap computation and data loading — it should always be the last step in the pipeline chain.
- *Why C is incorrect:* `from_tensor_slices` accepts a tuple `(X, y)` as its standard pattern for supervised datasets. This is the most common usage and is explicitly supported.
- *Why D is incorrect:* An integer buffer size is a valid argument to `shuffle()`. `tf.data.AUTOTUNE` is an option for `prefetch()`, not a requirement for `shuffle()`.

---

## Question 4

What does `pd.get_dummies(df["city"], prefix="city")` produce when the "city" column contains the values "Austin", "Dallas", and "Houston"?

- A) A single column with integer codes 0, 1, and 2 representing each city.
- B) Three new boolean/integer columns named "city_Austin", "city_Dallas", and "city_Houston", one for each category.
- C) A frequency table showing the count of each city in the dataset.
- D) A column containing the sorted alphabetical rank of each city name.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* `pd.get_dummies()` performs one-hot encoding: for each unique category it creates a new binary column. The `prefix="city"` argument prepends "city_" to each column name. The result has one column per unique value, with a 1 in the row corresponding to that category and 0 elsewhere.
- *Why A is incorrect:* Integer encoding (label encoding) is produced by `.astype("category").cat.codes`, not `get_dummies`. One-hot encoding deliberately avoids integer codes because they imply an ordinal relationship that does not exist for nominal categories like city names.
- *Why C is incorrect:* `df["city"].value_counts()` produces frequency counts. `get_dummies` creates encoded columns, not summary statistics.
- *Why D is incorrect:* No ranking or sorting occurs. `get_dummies` is purely an encoding transformation that produces binary indicator columns.

---

## Question 5

A model is trained for 40 epochs. The training loss decreases from 0.95 to 0.12. The validation loss decreases from 0.97 to 0.18 for the first 20 epochs and then gradually climbs back to 0.35 by epoch 40. What does this training curve indicate?

- A) The model is underfitting because both losses are below 1.0.
- B) The model is overfitting — it memorized training patterns that do not generalize, as shown by the increasing validation loss.
- C) The model needs a larger learning rate because the training loss is still not zero.
- D) The model is performing optimally and should continue training for another 40 epochs.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The divergence between training loss and validation loss is the signature of overfitting. Training loss continues to fall (the model keeps improving on training data) while validation loss rises (performance on held-out data degrades). The model is memorizing training examples rather than learning generalizable patterns. The best model weights exist at epoch 20 — before the validation loss begins climbing.
- *Why A is incorrect:* Underfitting is characterized by both losses remaining high and failing to decrease, not by losses below 1.0. The absolute scale of loss depends on the problem and loss function.
- *Why C is incorrect:* Increasing the learning rate would likely make the training loss bounce more erratically. The rising validation loss is an overfitting problem, not a speed-of-convergence problem.
- *Why D is incorrect:* Continuing to train beyond the point where validation loss starts rising will deepen the overfitting. The recommended action is to use `EarlyStopping(monitor="val_loss", restore_best_weights=True)` to stop at epoch 20.

---

## Question 6

Which NumPy operation correctly reshapes a 1D array of 784 elements into a format suitable for passing a single grayscale image to a Keras model expecting input shape `(None, 28, 28, 1)`?

- A) `x.reshape(28, 28)`
- B) `x.reshape(784, 1)`
- C) `x.reshape(1, 28, 28, 1)`
- D) `x.reshape(-1, 784)`

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Keras models expect batched input. The shape `(None, 28, 28, 1)` means (batch_size, height, width, channels). For a single image, batch_size is 1. Reshaping to `(1, 28, 28, 1)` adds both the batch dimension and the channel dimension required by convolutional layers.
- *Why A is incorrect:* `(28, 28)` produces a 2D array with no batch dimension and no channel dimension. Passing this directly to a model expecting `(None, 28, 28, 1)` raises a shape mismatch error.
- *Why B is incorrect:* `(784, 1)` is a 2D column vector, not an image tensor. It has the wrong number of dimensions and the wrong spatial structure.
- *Why D is incorrect:* `(-1, 784)` produces shape `(1, 784)` — a 2D array with a single row of 784 features, which is appropriate for a fully connected layer expecting flat input, not for a CNN expecting spatial input.

---

## Question 7

What is the purpose of calling `.prefetch(tf.data.AUTOTUNE)` at the end of a `tf.data.Dataset` pipeline?

- A) It shuffles the dataset in the background before each epoch begins.
- B) It overlaps the loading and preprocessing of the next batch with the GPU's computation on the current batch, reducing idle time.
- C) It caches the entire dataset in GPU memory to avoid repeated loading from disk.
- D) It automatically determines the optimal batch size for the dataset.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* `prefetch` instructs the pipeline to prepare the next batch while the model is still training on the current batch. This overlaps CPU data preparation with GPU computation, eliminating the CPU-to-GPU handoff bottleneck. `tf.data.AUTOTUNE` lets TensorFlow determine the optimal prefetch buffer size at runtime.
- *Why A is incorrect:* Shuffling is handled by `.shuffle()`. `prefetch` has no effect on the order of samples.
- *Why C is incorrect:* `.cache()` stores the dataset in memory or on disk. `prefetch` is about timing — it prepares batches in advance, not about caching all data simultaneously.
- *Why D is incorrect:* Batch size is set by `.batch(n)`. `prefetch` has no influence over batch size; it only controls how many batches are prepared ahead of time.

---

## Question 8

A developer calls `df.describe()` on a DataFrame and notices that the "income" column has a mean of 55,000 and a max of 9,800,000. What does this suggest about the preprocessing step needed before training?

- A) The income column should be dropped because it contains an error.
- B) The income column likely has extreme outliers, and a RobustScaler or log transform should be considered before training.
- C) The income column is already normalized and requires no preprocessing.
- D) The mean being much lower than the max means the column has missing values that must be imputed.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A max value of 9,800,000 against a mean of 55,000 indicates a severe positive skew with extreme outliers. Standard normalization (StandardScaler) is sensitive to outliers because it divides by the standard deviation, which is inflated by extreme values. RobustScaler uses the median and IQR instead. A log transform `np.log1p(income)` compresses the scale and is a common preprocessing step for income-like distributions.
- *Why A is incorrect:* A high-income outlier may be a legitimate data point (a billionaire in the dataset). Dropping it requires domain knowledge, not an automatic rule. Preprocessing is the appropriate first response.
- *Why C is incorrect:* A feature with values ranging from thousands to millions is far from normalized. Unscaled features with large absolute values cause gradient instability during training.
- *Why D is incorrect:* `describe()` shows count, mean, and percentiles. If count equals the expected number of rows, there are no missing values. Outlier detection requires inspecting the spread between mean and max, not the count.

---

## Question 9

Which of the following correctly converts a Pandas DataFrame column to a NumPy array suitable for TensorFlow model input?

- A) `X = df[["sqft", "bedrooms"]].to_numpy().astype(np.float32)`
- B) `X = df[["sqft", "bedrooms"]].float32()`
- C) `X = tf.cast(df[["sqft", "bedrooms"]], tf.float32)`
- D) `X = np.float32(df.columns[["sqft", "bedrooms"]])`

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* `.to_numpy()` (equivalent to `.values`) extracts the underlying NumPy array from a DataFrame selection. Chaining `.astype(np.float32)` casts to float32, which is the standard dtype for TensorFlow operations. This two-step pattern is the standard, idiomatic way to prepare tabular data for a TF model.
- *Why B is incorrect:* `.float32()` is not a valid Pandas method. There is no such method on DataFrame objects.
- *Why C is incorrect:* `tf.cast()` operates on TensorFlow tensors, not Pandas DataFrames. Passing a DataFrame directly to `tf.cast` raises a TypeError.
- *Why D is incorrect:* `df.columns` returns column names (strings), not column data. Indexing `df.columns` with a list of strings does not select column data — it would raise an error or return unexpected results.

---

## Question 10

A developer needs to normalize pixel values of images stored in a NumPy array `X` with shape `(60000, 28, 28)` and dtype `uint8` (values 0–255). Which code correctly prepares the array for TensorFlow?

- A) `X_norm = X / 255`
- B) `X_norm = X.astype(np.float32) / 255.0`
- C) `X_norm = StandardScaler().fit_transform(X.reshape(60000, -1))`
- D) `X_norm = (X - 128) / 128`

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Converting to float32 before dividing is the correct pattern for two reasons. First, dividing uint8 by 255 in NumPy keeps integer dtype and produces all zeros (integer division). Casting to float32 first ensures floating-point division. Second, float32 is the standard TensorFlow dtype — float64 wastes memory and can cause slow TF operations.
- *Why A is incorrect:* Dividing a uint8 array by the integer 255 performs integer division in NumPy, producing 0 for all values less than 255. You must cast to float32 first.
- *Why C is incorrect:* StandardScaler on flattened images can work, but it learns per-pixel statistics across all 60,000 images, which is computationally wasteful and not the standard approach. Division by 255 is preferred for images because all pixels share the same natural scale.
- *Why D is incorrect:* `(X - 128) / 128` centers around 128 and scales to roughly [-1, 1], which is a valid normalization choice for some architectures. However, it still has the uint8 integer division problem without the float cast, and the standard TF/Keras pattern for image normalization is division by 255.0.
