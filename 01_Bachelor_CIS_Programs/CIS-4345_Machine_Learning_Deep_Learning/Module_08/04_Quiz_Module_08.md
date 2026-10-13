# Quiz: Module 08 — Data Augmentation and Image Preprocessing

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

### Question 1

A developer creates two `ImageDataGenerator` instances — one for training and one for validation. Which configuration is correct?

- A) Both generators should include all augmentation parameters (rotation, flip, zoom) to ensure the model sees augmented images during validation.
- B) The training generator uses augmentation and rescaling; the validation generator uses only rescaling.
- C) The validation generator uses augmentation to produce harder test cases; the training generator uses only rescaling.
- D) Both generators should use the same identical configuration so that the evaluation is not biased toward simpler images.

**Correct Answer:** B) Augmentation is a regularization technique applied only during training to increase sample diversity. Validation measures model performance on real, unmodified images, so augmentation would introduce artificial variance and make the validation metric unreliable.

**Distractor Analysis:**

- *Why A is incorrect:* Augmenting validation data corrupts the metric. Validation accuracy should reflect how well the model handles real images, not transformed variants. This is one of the most common mistakes on the TF Developer Certificate exam.
- *Why B is correct:* The training generator uses augmentation to combat overfitting. The validation generator uses `rescale=1.0/255` only. This ensures a fair, repeatable validation score.
- *Why C is incorrect:* Making validation harder defeats the purpose of the evaluation. Validation should mimic the distribution of real-world inference data.
- *Why D is incorrect:* Identical generators would either augment both (bad for validation) or augment neither (wastes the benefit of augmentation for training).

---

### Question 2

What is the correct order of operations in a `tf.data` pipeline for image training?

- A) shuffle → batch → map(normalize) → cache → map(augment) → prefetch
- B) map(load) → map(augment) → batch → cache → shuffle → prefetch
- C) map(load+normalize) → map(augment) → cache → shuffle → batch → prefetch
- D) cache → map(load) → shuffle → map(augment) → batch → prefetch

**Correct Answer:** C) This order ensures images are decoded and normalized first (expensive, deterministic), then augmented (random, cheap), then cached (so decoding is not repeated), then shuffled and batched for each epoch.

**Distractor Analysis:**

- *Why A is incorrect:* Shuffling before batching is correct, but normalizing after batching is unusual and placing cache before normalization would cache raw undecoded bytes, eliminating the benefit.
- *Why B is incorrect:* Caching after batching means fewer, larger items are cached — this works but placing cache before shuffle means shuffling is also cached, which prevents different orderings each epoch.
- *Why C is correct:* Load and normalize are deterministic and expensive — cache them. Augmentation is random — do not cache its output, as that would freeze the random transformations. Shuffle before batching ensures random mini-batches.
- *Why D is incorrect:* Caching before loading means you cache nothing useful. The pipeline order is completely inverted.

---

### Question 3

Which code snippet correctly builds a `tf.data` pipeline that normalizes pixels to [0, 1] and applies random horizontal flipping?

- A)

```python
ds = dataset.map(lambda x, y: (x / 255.0, y))
ds = ds.map(lambda x, y: (tf.image.random_flip_left_right(x), y))
```

- B)

```python
ds = dataset.map(lambda x, y: (x * 255.0, y))
ds = ds.map(lambda x, y: (tf.image.flip_left_right(x), y))
```

- C)

```python
ds = dataset.map(lambda x, y: (x / 255.0, y))
ds = ds.map(lambda x, y: (tf.image.flip_left_right(x), y))
```

- D)

```python
ds = dataset.map(lambda x, y: (x / 127.5 - 1.0, y))
ds = ds.map(lambda x, y: (tf.image.random_flip_up_down(x), y))
```

**Correct Answer:** A) Dividing by 255.0 scales pixels to [0, 1]. `tf.image.random_flip_left_right` applies the flip randomly (only to some images), which is the correct augmentation behavior.

**Distractor Analysis:**

- *Why A is correct:* `x / 255.0` maps uint8 [0, 255] to float32 [0, 1]. `tf.image.random_flip_left_right` randomly mirrors the image 50% of the time — this is the standard augmentation call.
- *Why B is incorrect:* Multiplying by 255.0 scales values up, which is the wrong direction. `tf.image.flip_left_right` (without "random_") always flips every image, which is not augmentation — it simply transforms all images identically.
- *Why C is incorrect:* The normalization is correct but `tf.image.flip_left_right` (non-random) flips every image deterministically, not randomly. This does not add diversity.
- *Why D is incorrect:* `x / 127.5 - 1.0` maps to [-1, 1], which is correct for MobileNetV2 but not general [0, 1] normalization. `random_flip_up_down` is rarely appropriate for natural images (cats and dogs do not appear upside-down in practice).

---

### Question 4

A dataset has 2,000 images of class 0 (cats) and 200 images of class 1 (dogs). A developer wants to address this 10:1 imbalance using `class_weight`. Which dictionary is correct?

- A) `{0: 1.0, 1: 1.0}` — equal weights; the model handles imbalance internally.
- B) `{0: 0.1, 1: 0.9}` — weights proportional to the inverse of class frequency.
- C) `{0: 0.0909, 1: 0.909}` — computed as `count / total` for each class.
- D) `{0: 1.0, 1: 10.0}` — the minority class receives 10 times the loss penalty.

**Correct Answer:** D) With a 10:1 ratio, errors on class 1 (dogs) should be penalized 10 times more heavily than errors on class 0 (cats). The formula `total / (n_classes * count)` gives `2200 / (2 * 200) = 5.5` for dogs and `2200 / (2 * 2000) = 0.55` for cats, which scales proportionally to 1:10.

**Distractor Analysis:**

- *Why A is incorrect:* Equal weights do not address imbalance. The model will still learn to favor the majority class because the majority class contributes more loss samples per batch.
- *Why B is incorrect:* These weights are proportional to class frequency (not inverse frequency). Setting the minority class weight to 0.9 and the majority to 0.1 would further bias the model toward the minority, which overcorrects in the wrong direction.
- *Why C is incorrect:* These are the class probabilities, not corrective weights. Class weights should be inversely proportional to frequency — the minority class needs a higher weight, not a lower one.
- *Why D is correct:* The relative ratio is correct. The minority class (dogs, 10%) receives 10 times the weight of the majority class (cats, 90%). This balances the gradient contribution from each class regardless of their raw counts.

---

### Question 5

What happens to `RandomFlip`, `RandomRotation`, and `RandomZoom` Keras preprocessing layers when `model.predict()` is called?

- A) They apply the same random transformations used during training to ensure consistency between training and inference distributions.
- B) They are automatically disabled and pass images through unchanged, because random augmentation layers are only active when `training=True`.
- C) They raise an error because preprocessing layers cannot be included in a saved model used for inference.
- D) They apply a fixed (non-random) transformation equivalent to the mean of their configured range to standardize inference behavior.

**Correct Answer:** B) Keras `Random*` preprocessing layers check the `training` flag internally. During inference (`model.predict()`, `model.evaluate()`), the flag is `False` by default and all random operations are bypassed — images pass through unchanged.

**Distractor Analysis:**

- *Why A is incorrect:* Applying random augmentation during inference would introduce non-determinism — the same input image would produce different predictions on different calls. This would make the model unreliable in production.
- *Why B is correct:* This is a key TF Developer Certificate exam fact. The layers are part of the model graph and travel with a saved model, but augmentation is only active when `training=True`. Rescaling layers (like `Rescaling`) always apply regardless of training mode.
- *Why C is incorrect:* Keras preprocessing layers are fully saveable and exportable. They are designed to be embedded in the model for deployment. This is one of their primary advantages over external preprocessing scripts.
- *Why D is incorrect:* Keras preprocessing layers do not apply a mean transformation during inference. They simply pass the data through unchanged (identity function) for all `Random*` layers.

---

### Question 6

Which `tf.data` method prepares the next batch on the CPU while the GPU is processing the current batch?

- A) `.cache()`
- B) `.shuffle()`
- C) `.prefetch(tf.data.AUTOTUNE)`
- D) `.repeat()`

**Correct Answer:** C) `.prefetch()` enables the CPU and GPU to work in parallel. While the GPU trains on batch N, the CPU prepares batch N+1. `AUTOTUNE` lets TensorFlow determine the optimal buffer size automatically.

**Distractor Analysis:**

- *Why A is incorrect:* `.cache()` stores the dataset in memory after the first epoch to avoid repeated file I/O and decoding. It does not pipeline CPU and GPU work.
- *Why B is incorrect:* `.shuffle()` randomizes the order of elements in the dataset. It has no effect on CPU/GPU parallelism.
- *Why C is correct:* Prefetching is the single most impactful pipeline optimization for GPU utilization. Without it, the GPU sits idle while the CPU decodes and preprocesses the next batch. `tf.data.AUTOTUNE` is the recommended value.
- *Why D is incorrect:* `.repeat()` makes the dataset loop indefinitely (or for a specified number of times). It does not affect preprocessing pipeline parallelism.

---

### Question 7

A developer embeds a `Rescaling(1.0/255)` layer inside a Keras model. What is the primary advantage over rescaling in the `tf.data` pipeline?

- A) Rescaling inside the model is faster because it runs on the GPU rather than the CPU.
- B) The rescaling logic is saved with the model, so raw pixel images can be passed directly to the deployed model without any external preprocessing.
- C) Rescaling inside the model allows different rescaling factors to be applied to different batches during training.
- D) Internal rescaling layers automatically adjust their scale factor based on the dataset statistics each epoch.

**Correct Answer:** B) When preprocessing layers are part of the model, the saved `.keras` or `SavedModel` file contains the full preprocessing graph. Any application can call `model.predict(raw_images)` without needing to know the normalization details.

**Distractor Analysis:**

- *Why A is incorrect:* Rescaling is a trivially cheap operation. Whether it runs on CPU or GPU makes no measurable difference in practice. The benefit is portability, not speed.
- *Why B is correct:* This is the production advantage of in-model preprocessing. The model is self-contained. Teams that consume the model do not need a preprocessing specification document — the model handles it internally.
- *Why C is incorrect:* A `Rescaling` layer applies the same scale factor to every batch. It does not vary by batch. Dynamic batch-wise scaling would require a custom layer.
- *Why D is incorrect:* `Rescaling` uses a fixed, user-specified scale factor set at construction time. It does not adapt to dataset statistics. The `Normalization` layer (with `adapt()`) does adapt to statistics, but `Rescaling` does not.

---

### Question 8

What does `tf.data.AUTOTUNE` do when passed as the `num_parallel_calls` argument to `.map()`?

- A) It disables parallelism and processes map operations sequentially to avoid race conditions.
- B) It tells TensorFlow to automatically determine the optimal number of parallel CPU threads at runtime.
- C) It doubles the number of CPU cores used compared to specifying a fixed integer.
- D) It applies the map function asynchronously on the GPU rather than the CPU.

**Correct Answer:** B) `AUTOTUNE` (equal to `-1`) instructs TensorFlow's runtime to dynamically choose the number of threads based on available CPU resources and pipeline throughput. This is almost always faster than specifying a fixed integer.

**Distractor Analysis:**

- *Why A is incorrect:* Sequential processing (no parallelism) is the default when `num_parallel_calls` is not specified or set to `1`. `AUTOTUNE` does the opposite — it maximizes parallelism.
- *Why B is correct:* Using `num_parallel_calls=tf.data.AUTOTUNE` is the recommended pattern in TensorFlow documentation for all `.map()` calls on large datasets. It adapts to the runtime environment automatically.
- *Why C is incorrect:* `AUTOTUNE` does not guarantee double the cores — it selects whatever is optimal for the pipeline, which could be more or fewer than doubling.
- *Why D is incorrect:* `.map()` operations run on the CPU. GPU operations in TensorFlow are performed inside the model's forward pass, not in the data pipeline.

---

### Question 9

A developer uses `tf.keras.layers.RandomRotation(factor=0.1)` inside a model. What is the maximum rotation angle applied?

- A) 0.1 degrees
- B) 10 degrees
- C) Approximately 36 degrees (10% of a full 360-degree rotation, i.e., `0.1 * 2 * pi` radians)
- D) 90 degrees (the nearest 90-degree multiple of 0.1)

**Correct Answer:** C) The `factor` parameter in `RandomRotation` is a fraction of a full rotation (2π radians = 360 degrees). A factor of `0.1` means the rotation range is `[-0.1 * 2π, 0.1 * 2π]`, which corresponds to approximately ±36 degrees.

**Distractor Analysis:**

- *Why A is incorrect:* `factor` is not a degree value. Treating it as degrees would make the rotation imperceptibly small and useless for augmentation.
- *Why B is incorrect:* This confuses `factor` with `rotation_range` from `ImageDataGenerator`, where the parameter is specified in degrees. `RandomRotation` uses a fraction of a full 360-degree rotation.
- *Why C is correct:* `0.1 * 360 = 36 degrees`. This is a meaningful augmentation range for natural images. Larger values (e.g., 0.25) would produce 90-degree rotations, which are appropriate for some domains but not for most natural image tasks.
- *Why D is incorrect:* `RandomRotation` applies a continuous random angle within the specified range, not a discrete 90-degree snap. The value 90 degrees would correspond to `factor=0.25`, not 0.1.

---

### Question 10

Which of the following correctly uses `tf.keras.utils.image_dataset_from_directory` and adds a `.prefetch()` stage?

- A)

```python
ds = tf.keras.utils.image_dataset_from_directory('data/train', image_size=(224,224))
ds = ds.prefetch(buffer_size=tf.data.AUTOTUNE)
```

- B)

```python
ds = tf.keras.utils.image_dataset_from_directory('data/train', image_size=(224,224))
ds = ds.prefetch(buffer_size=0)
```

- C)

```python
ds = tf.data.Dataset.from_tensor_slices('data/train')
ds = ds.prefetch(buffer_size=tf.data.AUTOTUNE)
```

- D)

```python
ds = tf.keras.utils.image_dataset_from_directory('data/train', image_size=(224,224))
ds = ds.cache().prefetch(buffer_size=-255)
```

**Correct Answer:** A) `image_dataset_from_directory` returns a `tf.data.Dataset`. Chaining `.prefetch(tf.data.AUTOTUNE)` enables CPU/GPU pipelining. This is the complete, correct pattern.

**Distractor Analysis:**

- *Why A is correct:* This is the canonical usage. `tf.data.AUTOTUNE` is the recommended buffer size. The resulting `ds` can be passed directly to `model.fit()`.
- *Why B is incorrect:* `buffer_size=0` disables prefetching (no elements are prefetched). You need at least `buffer_size=1` for any overlap, and `AUTOTUNE` for optimal overlap.
- *Why C is incorrect:* `tf.data.Dataset.from_tensor_slices` expects a tensor or list, not a directory path string. This would create a dataset of individual characters from the path string, not images.
- *Why D is incorrect:* `-255` is not a valid buffer size for `.prefetch()`. Only non-negative integers and `tf.data.AUTOTUNE` (which equals `-1`) are valid. `-255` would raise a runtime error.

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.

---

### Question 11 (5 points)

A developer applies `RandomZoom(height_factor=(-0.2, 0.2))` as a Keras preprocessing layer. What range of zoom behavior does this produce?

- A) The image is zoomed in by exactly 20% on every training step.
- B) The image is randomly zoomed in or out by up to 20% of its height on each training step.
- C) The image height is randomly cropped to between 80% and 120% of the original, then padded back to the original size.
- D) The image is always zoomed out (made smaller) with a 20% black border added to fill the remaining space.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `height_factor=(-0.2, 0.2)` specifies a range: negative values zoom out (the image appears smaller with padding) and positive values zoom in (crop). A random value in `[-0.2, 0.2]` is drawn each time, producing variety in the apparent scale of the subject across training samples.
  - *Why A is incorrect:* The layer applies a random value within the specified range, not a fixed value. Using a tuple `(-0.2, 0.2)` explicitly defines a range. If a fixed zoom were desired, a scalar would be used, and it would still be random with magnitude up to that scalar.
  - *Why C is incorrect:* `RandomZoom` does not crop and pad independently for height and width in the manner described. It scales the image in the spatial domain and uses `fill_mode` (e.g., `'reflect'`, `'nearest'`) to handle the border, not explicit padding.
  - *Why D is incorrect:* The `(-0.2, 0.2)` range includes positive values (zoom in) as well as negative values (zoom out). It is not restricted to zoom-out only. The layer randomly draws from the full specified range.

---

### Question 12 (5 points)

Which of the following is NOT a valid use case for `tf.data.Dataset.cache()`?

- A) Caching a dataset loaded from disk so that images are only decoded once across all epochs.
- B) Caching after augmentation to ensure the same augmented images are reused across all epochs without re-randomizing.
- C) Caching in memory when the full dataset fits in RAM to eliminate repeated I/O overhead.
- D) Caching to a file (`.cache('/tmp/cache')`) when the dataset is too large to fit in memory.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct (i.e., NOT a valid use case):* Caching after augmentation defeats the purpose of augmentation. If augmented images are cached on the first epoch and reused unchanged, the model sees the same transformed version of each image every epoch — eliminating the diversity that makes augmentation effective. Augmentation must run after the cache to produce fresh random transforms each epoch.
  - *Why A is incorrect (it IS valid):* Caching after decoding/normalization but before augmentation is the recommended pattern. Expensive operations like JPEG decoding are only performed once, while augmentation (placed after cache) remains random.
  - *Why C is incorrect (it IS valid):* In-memory caching is ideal when the dataset fits in RAM. It completely eliminates disk I/O after the first epoch, often providing significant training speedups.
  - *Why D is incorrect (it IS valid):* File-based caching writes the dataset to disk after the first epoch. Subsequent epochs read from the cache file rather than the original source, which is faster if the source involves network I/O or complex decoding.

---

### Question 13 (5 points)

A developer has a training directory with 8,000 cat images and 2,000 dog images. Using `sklearn.utils.class_weight.compute_class_weight`, what approximate values are returned?

- A) `{0: 0.625, 1: 2.5}` — inversely proportional to class frequency.
- B) `{0: 0.8, 1: 0.2}` — proportional to class frequency.
- C) `{0: 1.0, 1: 1.0}` — equal weights regardless of imbalance.
- D) `{0: 4.0, 1: 1.0}` — the majority class receives a higher weight.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* The formula is `total / (n_classes * count)`. Total = 10,000, n_classes = 2. For cats: `10000 / (2 * 8000) = 0.625`. For dogs: `10000 / (2 * 2000) = 2.5`. The minority class (dogs) receives a weight 4x higher than the majority class, balancing their gradient contributions.
  - *Why B is incorrect:* These values are proportional to class frequency, not inverse frequency. Using them as class weights would amplify the imbalance rather than correct it, making the model even more biased toward the majority class.
  - *Why C is incorrect:* Equal weights ignore the imbalance entirely. The model still effectively sees 4 cat examples for every 1 dog example in expectation, with no correction. This is the behavior without any class weighting.
  - *Why D is incorrect:* Class weights should favor the minority class (dogs), not the majority. Giving the majority class a higher weight would make the imbalance catastrophically worse, causing the model to almost entirely ignore dog predictions.

---

### Question 14 (5 points)

What does the `shuffle_buffer_size` parameter control in `tf.data.Dataset.shuffle(buffer_size=1000)`, and what happens if `buffer_size=1`?

- A) It controls the number of epochs over which shuffling is distributed; `buffer_size=1` shuffles after every single batch.
- B) It controls the size of the in-memory buffer from which elements are randomly drawn; `buffer_size=1` produces no shuffling.
- C) It controls the random seed used for shuffling; `buffer_size=1` uses the default system random seed.
- D) It controls the number of CPU threads used for shuffling; `buffer_size=1` uses a single thread.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Shuffling in `tf.data` works by maintaining an in-memory buffer. At each step, one element is randomly drawn from the buffer and emitted, then the next element from the dataset fills the vacated slot. With `buffer_size=1`, the buffer holds only one element at a time — there is no randomness, and the dataset is returned in its original order. For perfect shuffling, `buffer_size` should equal the full dataset size.
  - *Why A is incorrect:* `buffer_size` is a spatial parameter (how many elements to hold in memory), not a temporal parameter (how many epochs). Shuffling operates element-by-element as data flows through the pipeline.
  - *Why C is incorrect:* The random seed is controlled by the `seed` parameter (e.g., `.shuffle(1000, seed=42)`), not `buffer_size`. Setting a seed makes shuffling reproducible; the buffer size controls randomization quality.
  - *Why D is incorrect:* CPU threading is controlled by `num_parallel_calls` in `.map()` and `.interleave()`, not by `.shuffle()`. The shuffle operation is single-threaded and does not support parallel execution.

---

### Question 15 (5 points)

A developer wants to apply MixUp augmentation — blending two training images and their labels. Which `tf.data` method enables this operation on pairs of examples?

- A) `.map(mixup_fn)` applied before batching, processing one example at a time.
- B) `.batch(batch_size).map(mixup_fn)` applied after batching, where `mixup_fn` operates on tensors of shape `(batch, H, W, C)`.
- C) `.interleave(mixup_fn)` applied as a flat-map operation that interleaves multiple datasets.
- D) `.filter(mixup_fn)` applied to select only pairs of images that are visually similar.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* MixUp requires two images: `x_new = lambda * x1 + (1 - lambda) * x2`. To access pairs of images, you must first batch the dataset so that each call to the map function receives a full batch tensor. The `mixup_fn` can then randomly pair examples within the batch: `x_mixed = lam * x[i] + (1 - lam) * x[j]` for random indices i, j within the batch.
  - *Why A is incorrect:* Applying a map function before batching processes one example at a time. MixUp requires access to at least two examples simultaneously to create the blend. A single-example map cannot perform MixUp.
  - *Why C is incorrect:* `.interleave()` is used to read from multiple data sources in parallel (e.g., multiple sharded files) and merge them into a single stream. It is not a mechanism for combining pairs of individual examples from the same dataset.
  - *Why D is incorrect:* `.filter()` selects or rejects individual examples based on a predicate. It cannot create new blended examples — it only keeps or discards existing ones. MixUp creates new synthetic training examples, which is an operation for `.map()`, not `.filter()`.

---

### Question 16 (5 points)

Why is it important to set `seed` in both `ImageDataGenerator` and `flow_from_directory` when creating paired training and validation generators?

- A) The seed ensures that augmentation parameters are identical for training and validation, making the comparison fair.
- B) The seed ensures that corresponding training and validation generators sample images in the same shuffled order, preventing label/image mismatches when using a single source directory split.
- C) The seed controls the learning rate schedule of the model trained with the generator, making training deterministic.
- D) The seed ensures the generator applies the same random crop to all images in a batch, producing uniform batch dimensions.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When splitting a dataset directory into training and validation using two generators from the same source, both generators must use the same seed so they shuffle images in the same order. This ensures that the files assigned to training and validation are consistent. If seeds differ, the same image could appear in both training and validation sets.
  - *Why A is incorrect:* Validation generators should NOT apply augmentation at all — only `rescale` is used. Having identical seeds for augmentation parameters would only matter if both generators applied augmentation, which is incorrect practice.
  - *Why C is incorrect:* Generator seeds have no connection to learning rate schedules. Learning rate is controlled by the optimizer configuration and callbacks like `ReduceLROnPlateau`. Seeds affect random number generation for data ordering.
  - *Why D is incorrect:* Keras image generators apply independent random crops per image within a batch, not a single shared crop. The seed ensures shuffling order consistency, not crop uniformity.

---

### Question 17 (5 points)

A developer uses `tf.keras.layers.Normalization` (not `Rescaling`) as an in-model preprocessing layer. What additional step is required before training that is NOT needed for `Rescaling`?

- A) Calling `layer.compile()` to register the normalization layer with the optimizer.
- B) Calling `layer.adapt(training_data)` to compute the mean and variance of the training set before training begins.
- C) Passing `normalize=True` to `model.compile()` so the loss function knows to expect normalized inputs.
- D) Adding a corresponding `Denormalization` layer at the model output to recover the original value range.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `tf.keras.layers.Normalization` computes mean and variance per feature to standardize inputs to zero mean and unit variance (z-score normalization). Unlike `Rescaling` (which uses a fixed user-specified factor), `Normalization` must learn the statistics of the training data by calling `.adapt(x_train)` before training. This is conceptually similar to `StandardScaler.fit()` in scikit-learn.
  - *Why A is incorrect:* Keras layers do not have individual `compile()` methods. Only `tf.keras.Model` objects are compiled. The `Normalization` layer does not require compilation; it requires `adapt()`.
  - *Why C is incorrect:* `model.compile()` has no `normalize` argument. The loss function has no awareness of whether inputs are normalized — it only sees model outputs and target labels. Normalization is entirely handled at the input layer.
  - *Why D is incorrect:* A `Normalization` layer at the input standardizes the model's input distribution. There is no corresponding inverse layer required at the output unless the model is predicting values in the original space (a regression task), and even then the inverse transform would be applied manually, not via a Keras layer.

---

### Question 18 (5 points)

Which code snippet correctly applies random brightness and contrast augmentation using the `tf.image` API inside a `tf.data` pipeline map function?

- A) `tf.image.random_brightness(image, max_delta=0.2); tf.image.random_contrast(image, lower=0.8, upper=1.2)`
- B) `tf.image.adjust_brightness(image, delta=0.2); tf.image.adjust_contrast(image, contrast_factor=1.2)`
- C) `image = tf.image.random_brightness(image, max_delta=0.2); image = tf.image.random_contrast(image, lower=0.8, upper=1.2)`
- D) `tf.augment.brightness(image, 0.2); tf.augment.contrast(image, 0.8, 1.2)`

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Both `tf.image.random_brightness` and `tf.image.random_contrast` return new tensors — they do not modify tensors in-place. The result must be assigned back to `image` (or a new variable). Both functions apply random transformations within the specified range on each call, which is the correct augmentation behavior.
  - *Why A is incorrect:* The function calls are correct but the results are discarded — they are not assigned to any variable. In TensorFlow's functional (eager or graph) execution, operations that return new tensors must be captured in a variable; otherwise, the original image tensor is used unchanged.
  - *Why B is incorrect:* `tf.image.adjust_brightness` and `tf.image.adjust_contrast` apply a fixed (non-random) adjustment. These are deterministic functions used for testing specific transformations, not for augmentation. Augmentation requires the `random_` prefix versions.
  - *Why D is incorrect:* `tf.augment` is not a valid TensorFlow submodule. The correct namespace for image operations is `tf.image`. Using an invalid namespace raises an `AttributeError` at runtime.

---

### Question 19 (5 points)

After applying data augmentation and achieving 82% validation accuracy on a Cats vs. Dogs classifier, a developer wants to further improve accuracy. Which technique is most appropriate as the next step?

- A) Apply test-time augmentation (TTA) — average predictions across multiple augmented versions of each test image.
- B) Increase `rotation_range` from 20 to 90 degrees in `ImageDataGenerator` to expose the model to more extreme rotations.
- C) Remove the `Dropout` layer to allow the model to learn more complex representations without regularization interference.
- D) Reduce the batch size from 32 to 1 to ensure the model updates weights on every single example.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Test-time augmentation applies multiple augmented versions of each test image (e.g., flips, slight crops) and averages the model's predictions. This reduces prediction variance and consistently improves accuracy by 1–3 percentage points with no retraining required. TTA is a powerful, low-cost technique for squeezing additional accuracy from a trained model.
  - *Why B is incorrect:* Cats and dogs in real photos are rarely rotated more than 30–45 degrees. Increasing `rotation_range` to 90 degrees would expose the model to unrealistic training examples that don't match the test distribution, potentially hurting accuracy rather than helping.
  - *Why C is incorrect:* At 82% validation accuracy with augmentation, the model is likely still slightly overfitting. Removing Dropout would increase overfitting and reduce generalization. Regularization should be maintained or tuned, not removed.
  - *Why D is incorrect:* Reducing batch size to 1 (pure SGD) makes training noisier and slower. For small-to-medium CNNs, batch sizes of 16–128 are optimal. Batch size 1 often produces worse final accuracy due to noisy gradient estimates.

---

### Question 20 (5 points)

When using `image_dataset_from_directory` with `label_mode='binary'`, what shape do the label tensors have per batch, and which loss function should be used?

- A) Shape `(batch_size, 2)` — use `categorical_crossentropy`.
- B) Shape `(batch_size, 1)` — use `binary_crossentropy`.
- C) Shape `(batch_size,)` — use `sparse_categorical_crossentropy`.
- D) Shape `(batch_size, num_classes)` — use `categorical_crossentropy`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `label_mode='binary'` generates float32 labels with shape `(batch_size, 1)` — a single value of 0.0 or 1.0 per image. This is compatible with a model output of `Dense(1, activation='sigmoid')` and `loss='binary_crossentropy'`. This is the standard configuration for two-class image classification.
  - *Why A is incorrect:* Shape `(batch_size, 2)` with one-hot encoding corresponds to `label_mode='categorical'`, not `'binary'`. The loss function would be `categorical_crossentropy`, and the output layer would need `Dense(2, activation='softmax')`.
  - *Why C is incorrect:* Shape `(batch_size,)` with integer labels corresponds to `label_mode='int'`. The loss function for integer labels in multi-class classification is `sparse_categorical_crossentropy`. For binary classification, `label_mode='binary'` is more appropriate.
  - *Why D is incorrect:* Shape `(batch_size, num_classes)` with one-hot vectors corresponds to `label_mode='categorical'`. This is for multi-class problems. `label_mode='binary'` only produces a single scalar label per image.
