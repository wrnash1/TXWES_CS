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

---

### Question 11 (5 points)

A developer writes `X_train_scaled = scaler.fit_transform(X_train)` but forgets to scale `X_test`. They then call `model.evaluate(X_test, y_test)`. What is the most likely consequence?

- A) TensorFlow raises a shape mismatch error because the dtypes differ.
- B) The model's test performance degrades significantly because the test features are on a different scale than the training features.
- C) The model automatically rescales X_test internally using the stored scaler statistics.
- D) No consequence — neural networks are scale-invariant and normalize inputs automatically.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The model's weights were optimized for scaled (zero-mean, unit-variance) inputs. Feeding raw unscaled test features produces input values in entirely different numerical ranges than the model expects, causing its decision boundaries to misfire and evaluation metrics to drop substantially.
  - *Why A is incorrect:* Both X_train_scaled and X_test would typically have dtype float32 after `fit_transform`. No dtype mismatch occurs — the issue is numerical magnitude, not data type.
  - *Why C is incorrect:* Keras models do not store or apply scikit-learn scalers internally. The scaler is a separate object and `model.evaluate` has no knowledge of it.
  - *Why D is incorrect:* Neural networks are not scale-invariant. Unscaled features with large magnitudes produce large pre-activations that push neurons into saturation or cause exploding gradients.

---

### Question 12 (5 points)

What is the correct way to select multiple columns from a Pandas DataFrame and convert them to a float32 NumPy array?

- A) `X = df[["col1", "col2"]].to_numpy().astype(np.float32)`
- B) `X = df.loc["col1", "col2"].values`
- C) `X = np.array(df.columns[["col1", "col2"]])`
- D) `X = df[["col1", "col2"]].float32()`

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* `df[["col1", "col2"]]` selects multiple columns using a list, producing a DataFrame. `.to_numpy()` converts it to a NumPy array. `.astype(np.float32)` ensures the dtype is float32, which is required for TensorFlow models.
  - *Why B is incorrect:* `df.loc` with two string arguments interprets them as row label and column label, not two column names. This syntax would attempt to select a single cell at row "col1", column "col2".
  - *Why C is incorrect:* `df.columns` returns an Index of column name strings. Indexing it with a list returns string names, not column data. `np.array(...)` of column names produces an array of strings, not feature values.
  - *Why D is incorrect:* `.float32()` is not a valid Pandas DataFrame method. There is no such method in the Pandas API.

---

### Question 13 (5 points)

In a `tf.data.Dataset` pipeline, what is the effect of setting `buffer_size=1` in `.shuffle(buffer_size=1)`?

- A) Only 1 element is loaded into the shuffle buffer at a time, effectively disabling random shuffling.
- B) The dataset is shuffled perfectly across all elements simultaneously.
- C) TensorFlow automatically increases the buffer to match the dataset size.
- D) The dataset is divided into 1 equal partition and shuffled within that partition.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* The shuffle buffer in `tf.data` works by maintaining a pool of `buffer_size` elements and randomly drawing from that pool. With `buffer_size=1`, the pool always contains exactly one element, so the "random" draw always picks the only element in the buffer — no randomization occurs. Effective shuffling requires `buffer_size` equal to (or larger than) the full dataset size.
  - *Why B is incorrect:* Perfect full-dataset shuffling requires `buffer_size >= dataset_size`. A buffer of 1 is the worst possible choice for randomness.
  - *Why C is incorrect:* TensorFlow does not override the buffer size you specify. If you set `buffer_size=1`, the pipeline uses a buffer of exactly 1 element.
  - *Why D is incorrect:* `buffer_size` is not a partition count. It is the number of elements held in memory simultaneously for random selection. Partitioning is not a concept associated with the shuffle buffer.

---

### Question 14 (5 points)

A developer has a target column `y` containing the strings "cat", "dog", and "bird". Which Pandas/NumPy pattern correctly converts these to integer labels (0, 1, 2) for use in a classification model?

- A) `y_int = pd.get_dummies(y).values`
- B) `y_int = pd.Categorical(y).codes`
- C) `y_int = y.astype(np.float32)`
- D) `y_int = np.log(y)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `pd.Categorical(series).codes` assigns each unique string value a unique integer code based on alphabetical order, producing 0 for "bird", 1 for "cat", 2 for "dog". This is label encoding — the standard approach for converting string class labels to integer indices for use with `sparse_categorical_crossentropy`.
  - *Why A is incorrect:* `pd.get_dummies` performs one-hot encoding, producing a 2D matrix of shape (n_samples, n_classes) rather than a 1D array of integer codes. This is appropriate for `categorical_crossentropy` but not for `sparse_categorical_crossentropy`.
  - *Why C is incorrect:* `y.astype(np.float32)` on a string Series raises a ValueError — NumPy cannot cast string values to float directly. This would fail at runtime.
  - *Why D is incorrect:* `np.log` computes logarithm and requires numeric input. Applying it to string values raises a TypeError.

---

### Question 15 (5 points)

What does `np.random.seed(42)` guarantee when placed at the beginning of a script?

- A) All TensorFlow operations in the script will produce identical results on GPU and CPU.
- B) NumPy random functions called after this line will produce the same sequence of numbers on every run.
- C) scikit-learn and TensorFlow random operations are also seeded by this single call.
- D) The script will run 42 times faster due to cached random number generation.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `np.random.seed(42)` seeds NumPy's global random state. All subsequent calls to NumPy random functions (e.g., `np.random.randn()`, `np.random.choice()`) will produce the same sequence of pseudo-random numbers every run, ensuring reproducible data generation and sampling.
  - *Why A is incorrect:* TensorFlow uses its own separate random number generator. `np.random.seed()` does not affect TF operations. Use `tf.random.set_seed(42)` for TensorFlow reproducibility.
  - *Why C is incorrect:* scikit-learn uses its own RNG separate from NumPy's global seed for most operations when `random_state` is not explicitly set. To seed sklearn, pass `random_state=42` to individual functions.
  - *Why D is incorrect:* Setting a seed has no effect on execution speed. It only determines the sequence of pseudo-random values, not how fast they are generated.

---

### Question 16 (5 points)

A developer wants to apply a custom preprocessing function to each element of a `tf.data.Dataset`. Which method achieves this?

- A) `.apply(fn)` — applies fn to the entire dataset as a transformation
- B) `.map(fn)` — applies fn to each individual element
- C) `.filter(fn)` — applies fn and keeps elements where fn returns True
- D) `.zip(fn)` — pairs dataset elements with fn output

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `.map(fn)` applies a function element-wise to every sample (or batch) in the dataset. The function receives a single element's features (and label if the dataset is a tuple) and returns the transformed result. This is the standard way to apply augmentation, normalization, or parsing logic inside a `tf.data` pipeline.
  - *Why A is incorrect:* `.apply(fn)` applies a function to the entire dataset object (not element-wise), used for dataset-level transformations like `.apply(tf.data.experimental.unbatch())`. It is not for per-element preprocessing.
  - *Why C is incorrect:* `.filter(fn)` keeps elements for which fn returns True and discards the rest. It is for selecting a subset of data, not for transforming elements.
  - *Why D is incorrect:* `.zip(other_dataset)` combines two datasets element-wise into tuples, analogous to Python's `zip()`. It does not apply a transformation function to dataset elements.

---

### Question 17 (5 points)

What is the output of `np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)`?

- A) A 3×2 matrix with rows [1,2], [3,4], [5,6]
- B) A 2×3 matrix with rows [1,2,3] and [4,5,6]
- C) A 1D array of 6 elements with no change
- D) A 6×1 column vector

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `reshape(2, 3)` interprets the 6 elements in row-major (C) order and fills a 2-row, 3-column matrix. The first row gets elements 1,2,3 and the second row gets elements 4,5,6. NumPy fills rows left-to-right, top-to-bottom.
  - *Why A is incorrect:* `reshape(3, 2)` would produce a 3×2 matrix with rows [1,2], [3,4], [5,6]. The arguments to reshape specify (rows, columns), so `reshape(2, 3)` creates 2 rows and 3 columns, not the reverse.
  - *Why C is incorrect:* `reshape` with different dimensions always changes the shape. The array's view changes from 1D shape (6,) to 2D shape (2, 3).
  - *Why D is incorrect:* A 6×1 column vector is produced by `reshape(6, 1)` or `reshape(-1, 1)`, which creates 6 rows and 1 column. `reshape(2, 3)` creates 2 rows and 3 columns.

---

### Question 18 (5 points)

Which of the following is the correct pattern for applying `MinMaxScaler` to training data and using the same scale for test data?

- A) `scaler.fit(X_train); X_tr = scaler.transform(X_train); X_te = scaler.transform(X_test)`
- B) `X_tr = scaler.fit_transform(X_train); X_te = scaler.fit_transform(X_test)`
- C) `scaler.fit(X_test); X_tr = scaler.transform(X_train); X_te = scaler.transform(X_test)`
- D) `X_tr = MinMaxScaler().fit_transform(X_train); X_te = MinMaxScaler().fit_transform(X_test)`

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* `scaler.fit(X_train)` learns the min and max from the training set only. `scaler.transform(X_train)` and `scaler.transform(X_test)` then apply those same training statistics to both sets — no data leakage occurs.
  - *Why B is incorrect:* Calling `fit_transform` on both sets fits separate scalers to each partition. This is equivalent to fitting the scaler on test data, which constitutes data leakage.
  - *Why C is incorrect:* Fitting on `X_test` and transforming `X_train` using test statistics inverts the correct relationship — training data would be scaled using test distribution parameters, which is backwards and wrong.
  - *Why D is incorrect:* Creating two separate `MinMaxScaler()` instances means each is fitted independently on its respective partition. This is the same data leakage problem as option B, with the additional issue of having two incompatible scale objects.

---

### Question 19 (5 points)

A Pandas DataFrame `df` has 1,000 rows. After calling `df.dropna(subset=["price"])`, the DataFrame has 985 rows. What does this tell you?

- A) 985 rows have missing values in columns other than "price".
- B) 15 rows had a missing value in the "price" column and were removed.
- C) The DataFrame was sorted by price and the bottom 15 values were dropped.
- D) 15 duplicate rows were detected and removed based on the "price" column.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `dropna(subset=["price"])` removes any row where the "price" column contains NaN. Starting from 1,000 rows and ending with 985 rows means exactly 15 rows had a missing "price" value and were dropped. The `subset` parameter restricts the check to only the specified column(s).
  - *Why A is incorrect:* `subset=["price"]` restricts removal to rows with NaN only in the "price" column. Missing values in other columns are not considered by this call.
  - *Why C is incorrect:* `dropna` removes rows with missing values (NaN), not rows with low values. Sorting and value-based dropping are separate operations.
  - *Why D is incorrect:* Duplicate detection uses `df.drop_duplicates()`, not `dropna`. The `subset` parameter in `dropna` specifies which columns to check for NaN, not which columns to use for deduplication.

---

### Question 20 (5 points)

A developer has a feature matrix `X` of shape `(1000, 10)` and computes `X.std(axis=0)`. One of the resulting values is `0.0`. What does this indicate and what should the developer do?

- A) The feature has perfect variance; no action is needed.
- B) The feature is constant (all values are identical) and should be removed before scaling to avoid division by zero.
- C) The feature has negative values that must be made positive before computing the standard deviation.
- D) The standard deviation of 0.0 is expected and StandardScaler will handle it automatically without any issues.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A standard deviation of 0.0 means every value in that feature column is identical — the feature carries no information and cannot discriminate between samples. `StandardScaler` divides by the standard deviation; if std=0, this produces division by zero (NaN or inf). The feature should be identified and removed before scaling using `VarianceThreshold(threshold=0)` from scikit-learn.
  - *Why A is incorrect:* A std of 0.0 means zero variance, not perfect variance. High variance would show a large standard deviation value, not zero.
  - *Why C is incorrect:* Standard deviation is always non-negative regardless of whether the values are positive or negative. A std of 0.0 is caused by all values being the same, not by negative values.
  - *Why D is incorrect:* StandardScaler in scikit-learn sets the scale to 1 for zero-variance features to avoid division by zero, but the resulting scaled feature is all zeros — it contributes no information to the model. Relying on this silent behavior is poor practice; explicitly removing constant features is correct.
