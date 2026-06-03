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
