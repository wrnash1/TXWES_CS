# Quiz: Module 06 - Convolutional Neural Networks (CNNs) for Image Classification
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
In a Keras CNN, what is the role of the `MaxPooling2D(pool_size=(2,2))` layer?
*   A) It applies a learnable 2×2 filter to each input pixel to extract spatial features.
*   B) It downsamples the feature map by taking the maximum value within each 2×2 window, reducing spatial dimensions by half in both height and width.
*   C) It normalizes the pixel values in each 2×2 region to have zero mean and unit variance.
*   D) It reshapes the 3D feature map tensor into a 1D vector so it can be passed to Dense layers.
*   **Correct Answer:** B) MaxPooling2D selects the largest activation within each non-overlapping window, discarding the rest — this reduces the spatial size of feature maps, decreasing computation and providing some translation invariance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Applying a learnable filter is the job of `Conv2D`, not `MaxPooling2D`. MaxPooling has no trainable parameters.
    *   *Why B is correct:* `MaxPooling2D(pool_size=(2,2))` on a 28×28 feature map produces a 14×14 output. It is placed after Conv2D layers to progressively reduce spatial resolution.
    *   *Why C is incorrect:* Normalization to zero mean and unit variance describes Batch Normalization (`tf.keras.layers.BatchNormalization`), not pooling.
    *   *Why D is incorrect:* Reshaping a 3D tensor to a 1D vector is the job of the `Flatten` layer, which comes after all convolutional and pooling layers.

---

**Question 2**
Which of the following is the most accurate definition of a **convolutional filter (kernel)** in a CNN?
*   A) A lookup table that maps integer token IDs to dense vector representations for use in text processing pipelines.
*   B) A small matrix of learnable weights that slides across the input image, computing a dot product with each local patch of pixels to produce a feature map that highlights specific patterns such as edges or textures.
*   C) A regularization technique that randomly sets a fraction of neuron activations to zero during training to prevent co-adaptation.
*   D) A pooling operation that computes the average value within each spatial window to reduce the feature map size smoothly.
*   **Correct Answer:** B) A convolutional filter is a small learnable weight matrix (e.g., 3×3) that detects a specific spatial feature; stacking multiple filters in a Conv2D layer produces multiple feature maps, each detecting a different pattern.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes an Embedding layer used in NLP tasks, not a convolutional filter.
    *   *Why B is correct:* In Keras: `Conv2D(32, kernel_size=(3,3), activation='relu')` creates 32 independent 3×3 filters. Each filter produces one feature map. The filters are learned via backpropagation.
    *   *Why C is incorrect:* This describes a Dropout layer (`tf.keras.layers.Dropout`), which is a regularization technique unrelated to convolution.
    *   *Why D is incorrect:* This describes `AveragePooling2D`, a downsampling layer — not a convolutional filter. Convolutional filters learn spatial features; pooling layers reduce spatial dimensions.

---

**Question 3**
A developer builds a CNN for binary image classification. Which Keras code correctly implements the standard `[Conv2D → MaxPooling2D] × 2 → Flatten → Dense → output` pattern?
*   A) `model = tf.keras.Sequential([tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)), tf.keras.layers.MaxPooling2D(2,2), tf.keras.layers.Conv2D(64,(3,3),activation='relu'), tf.keras.layers.MaxPooling2D(2,2), tf.keras.layers.Flatten(), tf.keras.layers.Dense(64,activation='relu'), tf.keras.layers.Dense(1,activation='sigmoid')])`
*   B) `model = tf.keras.Sequential([tf.keras.layers.Dense(32,activation='relu',input_shape=(150,150,3)), tf.keras.layers.Dense(64,activation='relu'), tf.keras.layers.Dense(1,activation='sigmoid')])`
*   C) `model = tf.keras.Sequential([tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)), tf.keras.layers.Flatten(), tf.keras.layers.Dense(1,activation='sigmoid')])`
*   D) `model = tf.keras.Sequential([tf.keras.layers.Conv2D(32,(3,3),activation='softmax',input_shape=(150,150,3)), tf.keras.layers.MaxPooling2D(2,2), tf.keras.layers.Dense(1,activation='sigmoid')])`
*   **Correct Answer:** A) Two Conv2D+MaxPooling2D blocks, followed by Flatten, one hidden Dense(relu), and a sigmoid output unit — the canonical binary image classifier pattern for the TF Developer Certificate exam.
*   **Distractor Analysis:**
    *   *Why A is correct:* This matches the exam's expected pattern. Compile with `loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']`. The `input_shape=(150,150,3)` is the standard dog/cat exam shape.
    *   *Why B is incorrect:* Dense layers applied directly to a 3D input tensor `(150,150,3)` have no spatial feature extraction capability. CNNs use Conv2D layers, not Dense layers, for image feature learning.
    *   *Why C is incorrect:* This is missing both MaxPooling2D layers and a second Conv2D block. Without pooling, the spatial dimensions remain large, greatly increasing parameter count and risking overfitting.
    *   *Why D is incorrect:* `softmax` in a Conv2D layer is not appropriate for a hidden convolutional layer. Also, the Flatten layer is missing before Dense, which would cause a shape mismatch error.

---

**Question 4**
When using `ImageDataGenerator`, what does the `rescale=1./255` argument do?
*   A) It resizes every image to 255×255 pixels before feeding it into the model.
*   B) It divides each pixel value by 255, normalizing the pixel range from [0, 255] to [0, 1] so that input features have a consistent scale.
*   C) It limits the generator to loading a maximum of 255 images per batch from the directory.
*   D) It applies random horizontal flipping and rotation with a probability of 1/255 to each image.
*   **Correct Answer:** B) Neural networks train more efficiently when inputs are normalized. `rescale=1./255` is the standard preprocessing step for image pixels, converting integer values in [0, 255] to floats in [0, 1].
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Image resizing is controlled by the `target_size` argument in `flow_from_directory()`, not by `rescale`. `rescale` only modifies pixel values, not spatial dimensions.
    *   *Why B is correct:* Usage: `train_gen = ImageDataGenerator(rescale=1./255)`. Without this, input pixel values would range from 0 to 255, causing slow convergence and unstable gradients.
    *   *Why C is incorrect:* Batch size is controlled by the `batch_size` argument in `flow_from_directory()`, not by `rescale`.
    *   *Why D is incorrect:* Augmentation parameters like `horizontal_flip=True` and `rotation_range=40` are separate arguments to `ImageDataGenerator`, not determined by `rescale`.

---

**Question 5**
What is the difference between `padding='same'` and `padding='valid'` in a `Conv2D` layer?
*   A) `padding='same'` applies max-pooling before the convolution; `padding='valid'` skips pooling entirely.
*   B) `padding='same'` adds zero-padding around the input so the output feature map has the same height and width as the input; `padding='valid'` performs no padding, so the output is smaller than the input.
*   C) `padding='same'` repeats the convolution twice to double the number of feature maps; `padding='valid'` applies the convolution once.
*   D) `padding='same'` uses stride 2 to skip every other pixel; `padding='valid'` uses stride 1 to scan every pixel position.
*   **Correct Answer:** B) `padding='same'` preserves spatial dimensions by adding zeros at the border; `padding='valid'` (the Keras default) allows the output to shrink based on the filter size — a 3×3 filter on a 28×28 input yields a 26×26 output with valid padding.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The `padding` argument controls spatial dimension preservation only. MaxPooling is a separate layer and is not controlled by the padding argument of Conv2D.
    *   *Why B is correct:* With `padding='same'` and `kernel_size=(3,3)`, a 150×150 input produces a 150×150 feature map. With `padding='valid'`, it produces a 148×148 feature map. The TF exam commonly uses `padding='same'` to maintain dimensions across multiple Conv2D layers.
    *   *Why C is incorrect:* The number of feature maps is determined by the `filters` argument (e.g., `Conv2D(32, ...)`), not by the padding setting.
    *   *Why D is incorrect:* Stride is controlled by the separate `strides` argument in Conv2D. `padding` and `strides` are independent parameters with independent effects on output shape.

---

### Question 6 (5 points)

A CNN uses `MaxPooling2D(pool_size=(2,2))` after each Conv2D block. A developer considers replacing all MaxPooling layers with `AveragePooling2D(pool_size=(2,2))`. What is the key difference between the two pooling types, and when is each preferred?

* A) MaxPooling retains the average activation in each window; AveragePooling retains the maximum — they are functionally identical but differ in naming convention.
* B) MaxPooling selects the largest activation in each pooling window, preserving the strongest feature responses and providing sharp spatial feature detection; AveragePooling computes the mean of all values in the window, producing smoother feature maps. MaxPooling is preferred for object detection tasks; AveragePooling is often used in the final Global Average Pooling step before the Dense classifier in modern architectures.
* C) MaxPooling is used only during inference; AveragePooling is used only during training.
* D) AveragePooling increases spatial dimensions; MaxPooling decreases spatial dimensions.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* MaxPooling's `max()` operation preserves the most activated (highest response) feature in each local region, which is effective at retaining edge and texture detectors. AveragePooling's `mean()` operation smooths the feature map, which can dilute strong activations. In the TF Developer Certificate exam, MaxPooling is used in standard CNN classification architectures. Global Average Pooling (`GlobalAveragePooling2D`) is used in modern architectures (like MobileNet and InceptionV3) as a parameter-efficient alternative to Flatten before the final Dense layer.
  * *Why A is incorrect:* This reverses the definitions. MaxPooling uses the maximum, AveragePooling uses the average — they are functionally distinct operations with different effects on feature map preservation.
  * *Why C is incorrect:* Both pooling types are used during training and inference in the same way. Pooling is a feed-forward operation that behaves identically in both phases (unlike Dropout or BatchNormalization).
  * *Why D is incorrect:* Both MaxPooling and AveragePooling reduce (downsample) spatial dimensions by the pool size factor. Neither increases spatial dimensions. Upsampling is performed by `UpSampling2D` or transposed convolutions, used in decoder architectures.

---

### Question 7 (5 points)

A `Conv2D(64, kernel_size=(3,3), strides=(2,2), padding='valid')` layer receives a 32×32 input feature map. What is the spatial size (height × width) of the output feature map?

* A) 32×32 — stride does not affect spatial dimensions.
* B) 30×30 — only the kernel size reduces dimensions when padding='valid'.
* C) 15×15 — with stride=2 and valid padding, the spatial dimensions are halved (approximately).
* D) 64×64 — the number of filters determines the output spatial size.

* **Correct Answer:** C
* **Distractor Analysis:**
  * *Why C is correct:* The output spatial dimension formula is: `floor((input_size - kernel_size) / stride) + 1`. For height: `floor((32 - 3) / 2) + 1 = floor(29 / 2) + 1 = 14 + 1 = 15`. Same calculation for width. So the output is 15×15 with 64 feature maps (depth). Stride controls how many pixels the kernel moves between each application — stride=2 downsamples the spatial dimensions roughly by half, similar to MaxPooling, but within the convolution itself.
  * *Why A is incorrect:* Stride directly affects output spatial dimensions. A stride of 2 reduces the output size compared to stride=1 by skipping every other position.
  * *Why B is incorrect:* This calculation applies stride=1 with valid padding: `(32 - 3) + 1 = 30`. With stride=2, the kernel steps 2 pixels at a time, producing a smaller output.
  * *Why D is incorrect:* The number of filters (64 in this case) determines the depth of the output feature map (the number of channels), not the spatial height or width. Spatial dimensions are determined by input size, kernel size, stride, and padding.

---

### Question 8 (5 points)

A Conv2D layer with 32 filters of size 3×3 processes a grayscale input image of shape (28, 28, 1) with padding='same' and stride=1. How many trainable parameters does this Conv2D layer have?

* A) 32 — one parameter per filter.
* B) 288 — 32 filters × 3 × 3 kernel size, with no bias.
* C) 320 — 32 filters × (3 × 3 × 1 weights + 1 bias per filter).
* D) 9,408 — 28 × 28 × 3 × 3 × 32 convolution operations.

* **Correct Answer:** C
* **Distractor Analysis:**
  * *Why C is correct:* Each filter has `kernel_height × kernel_width × input_channels` weights: `3 × 3 × 1 = 9` weights per filter. Each filter also has 1 bias term. Total per filter: `9 + 1 = 10`. With 32 filters: `32 × 10 = 320 trainable parameters`. For an RGB input (3 channels), it would be `32 × (3 × 3 × 3 + 1) = 32 × 28 = 896`. This parameter count formula — `filters × (kernel_h × kernel_w × input_channels + 1)` — is a core TF Developer Certificate exam skill.
  * *Why A is incorrect:* Each filter has multiple weights (one per kernel position per input channel) plus a bias. A single parameter per filter would provide no spatial feature-learning capability.
  * *Why B is incorrect:* This counts only the kernel weights (9 × 32 = 288) and omits the bias term. Each filter has exactly 1 bias, adding 32 more parameters for a total of 320.
  * *Why D is incorrect:* 9,408 represents the total number of multiply-accumulate operations (FLOPs) performed during the convolution across all spatial positions, not the number of trainable parameters. Parameters are shared across all spatial positions — that is the key efficiency of convolutional layers.

---

### Question 9 (5 points)

A developer wants to build a CNN for classifying a custom medical image dataset with only 800 labeled training images. Training from scratch produces poor results due to insufficient data. Which approach is most appropriate, and how is it implemented in Keras?

* A) Increase the number of Conv2D filters to 1024 per layer to compensate for the small dataset.
* B) Use transfer learning — load a pretrained model (e.g., VGG16 or MobileNetV2) with weights pretrained on ImageNet, freeze the convolutional base, and train only a new classification head on the 800 medical images.
* C) Use 10-fold cross-validation to multiply the effective training set size by 10.
* D) Generate additional training images by querying an image search API and adding them to the dataset.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Transfer learning reuses feature representations learned from a large dataset (ImageNet, 1.2M images, 1000 classes) in a model trained for a different but related task. The frozen convolutional base already detects universal visual features (edges, textures, shapes) that are useful for medical images. In Keras: `base_model = tf.keras.applications.MobileNetV2(include_top=False, weights='imagenet')`, then `base_model.trainable = False`, then add a new `GlobalAveragePooling2D()` + `Dense(1, activation='sigmoid')` head. Only the head is trained on the 800 images. This is the canonical approach for small medical datasets on the TF Developer Certificate exam.
  * *Why A is incorrect:* Increasing filter count makes the model larger and more prone to overfitting on a small dataset. A larger model with 800 samples will overfit worse, not better.
  * *Why C is incorrect:* Cross-validation is a model evaluation technique for estimating generalization performance. It does not create new data or increase the actual training set — each fold still trains on a subset of the original 800 images.
  * *Why D is incorrect:* Downloading internet images without domain expertise and proper labeling introduces label noise and distribution shift. This approach does not constitute valid data augmentation and would likely degrade model quality.

---

### Question 10 (5 points)

A developer uses `ImageDataGenerator` for training a CNN on 1,000 cat and dog images. The generator is configured with `horizontal_flip=True`, `rotation_range=30`, `zoom_range=0.2`, and `width_shift_range=0.1`. What is the primary purpose of these settings, and what is a key constraint on how they should be applied?

* A) These settings permanently alter the images on disk to create a larger static dataset before training begins.
* B) These settings apply random geometric and color transformations to each training image on-the-fly during each epoch, artificially increasing the effective training set diversity and reducing overfitting — but they should only be applied to the training generator, NOT to the validation or test generator.
* C) These settings define the model's preprocessing pipeline for inference and must also be applied to the test generator to ensure consistent predictions.
* D) These settings are applied only once during the first epoch and have no effect on subsequent epochs.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Data augmentation via `ImageDataGenerator` applies random transformations to each image at load time during training, producing different variations of each image across epochs. This effectively increases training set diversity without requiring additional raw data, helping the model learn rotation- and flip-invariant features. Critically, augmentation must NOT be applied to the validation or test generator — those generators should use only `rescale=1./255` to ensure evaluation on unmodified images that reflect real inference conditions.
  * *Why A is incorrect:* `ImageDataGenerator` augmentation is applied in-memory at runtime during training — it does not modify files on disk. The original images remain unchanged.
  * *Why C is incorrect:* Applying augmentation (random flips, rotations, zooms) to the validation and test generators would introduce randomness into evaluation, causing different metric values on each run and making it impossible to reliably measure model performance.
  * *Why D is incorrect:* Augmentation is applied independently to each image on each epoch. Every time an image is loaded during training, a new random transformation is applied — so the model sees a different version of each image each epoch, which is precisely what provides the diversity benefit.

---

### Question 11 (5 points)

What does setting `restore_best_weights=True` in an `EarlyStopping` callback do?

*   A) It saves the model to disk every epoch and restores the last saved file when training ends.
*   B) It resets all model weights to their randomly initialized values when training stops.
*   C) It reverts the model weights to the values from the epoch with the best monitored metric when training stops early.
*   D) It continues training for an additional number of epochs equal to `patience` after the best epoch is found.

*   **Correct Answer:** C) Without `restore_best_weights=True`, the model retains the weights from the final epoch, which may be worse than the best epoch if overfitting occurred. This parameter ensures the model state at the best monitored epoch is kept.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Saving to disk on every epoch is `ModelCheckpoint` behavior, not `EarlyStopping`. `restore_best_weights` operates entirely in memory — it does not touch the filesystem.
    *   *Why B is incorrect:* Resetting to random initialization would destroy all training progress. `restore_best_weights` restores the best *trained* weights, not initial random weights.
    *   *Why C is correct:* Usage: `EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)`. When training stops at epoch 45 but the best val_loss was at epoch 32, the model's weights are rolled back to epoch 32.
    *   *Why D is incorrect:* `patience` controls how many non-improving epochs to tolerate before stopping. It does not extend training after the best epoch is found.

---

### Question 12 (5 points)

A `ReduceLROnPlateau` callback is configured as `ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-7)`. The current learning rate is `0.001`. After 5 consecutive epochs with no improvement in `val_loss`, what learning rate will the optimizer use next?

*   A) `0.0005`
*   B) `0.001`
*   C) `0.0000001`
*   D) `0.001 - 0.5 = -0.499`

*   **Correct Answer:** A) When the callback fires, the learning rate is multiplied by `factor`. `0.001 * 0.5 = 0.0005`. The `min_lr=1e-7` is the floor — the LR cannot be reduced below that value.
*   **Distractor Analysis:**
    *   *Why A is correct:* `new_lr = current_lr * factor = 0.001 * 0.5 = 0.0005`. Subsequent firings would give 0.00025, 0.000125, etc., down to the `min_lr` floor.
    *   *Why B is incorrect:* The LR stays at `0.001` only if the callback has not yet fired. After `patience=5` non-improving epochs, the callback fires and reduces the LR.
    *   *Why C is incorrect:* `min_lr=1e-7` is the lower bound — the LR cannot go below this value, but it does not jump directly to this value on the first firing.
    *   *Why D is incorrect:* `factor` is a multiplicative scalar, not a value to subtract. Subtracting `factor` from the LR is not how `ReduceLROnPlateau` works.

---

### Question 13 (5 points)

A `BatchNormalization()` layer is placed after a `Dense(64)` layer in a Keras model. How many total parameters does the `BatchNormalization` layer add, and how many of those are trainable?

*   A) 128 total, all 128 trainable
*   B) 256 total, 128 trainable and 128 non-trainable
*   C) 64 total, 64 trainable
*   D) 256 total, all 256 trainable

*   **Correct Answer:** B) BatchNormalization on a 64-feature layer adds gamma (64) + beta (64) as trainable parameters and running mean (64) + running variance (64) as non-trainable parameters, totaling 256 with 128 trainable.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Only gamma and beta are trainable (128 params). The moving mean and moving variance are non-trainable buffers used only during inference — they are updated via exponential moving average, not backpropagation.
    *   *Why B is correct:* Formula: `4 * features` total parameters, `2 * features` trainable. For 64 features: 256 total, 128 trainable. `model.summary()` shows these split under "Trainable params" and "Non-trainable params".
    *   *Why C is incorrect:* This counts only one component (either gamma or beta) but ignores the other three. All four parameter tensors (gamma, beta, mean, variance) are present.
    *   *Why D is incorrect:* Moving mean and moving variance are non-trainable — they are updated by the layer's internal logic, not by the optimizer. Marking them trainable would be incorrect.

---

### Question 14 (5 points)

What is the primary difference in behavior of a `Dropout(0.3)` layer between `model.fit()` and `model.predict()`?

*   A) During `model.fit()`, dropout zeros 30% of units; during `model.predict()`, dropout zeros 70% of units.
*   B) During `model.fit()`, dropout randomly zeros 30% of units; during `model.predict()`, dropout is disabled and all units are active with outputs scaled by 0.7.
*   C) During `model.fit()`, dropout is disabled; during `model.predict()`, dropout zeros 30% of units.
*   D) Dropout behaves identically during training and inference — the 30% zero rate applies in both cases.

*   **Correct Answer:** B) This is called inverted dropout. Keras scales active unit outputs by `1/(1-rate)` during training so no scaling is needed at inference time, where all units are active.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The complementary rate (70%) is not applied during inference. All units are active at inference — the 30% rate only applies during training.
    *   *Why B is correct:* Keras `Dropout` is automatically toggled by the `training` flag. `model.fit()` sets `training=True` (dropout active); `model.predict()` sets `training=False` (dropout disabled, all units active).
    *   *Why C is incorrect:* This has training and inference backwards. Dropout provides regularization *during training* to prevent co-adaptation. Applying it only at inference would give noisy, non-deterministic predictions.
    *   *Why D is incorrect:* If dropout behaved identically at both stages, inference predictions would be non-deterministic (random), making the model unusable in production.

---

### Question 15 (5 points)

A model is compiled and evaluated as follows:

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', 'AUC'])
results = model.evaluate(X_test, y_test, verbose=0)
```

What does `results` contain?

*   A) A single float representing the test loss only
*   B) A list `[loss, accuracy, AUC]` in the order the metrics were specified during compile
*   C) A dictionary with keys `'loss'`, `'accuracy'`, and `'AUC'`
*   D) A list `[accuracy, AUC]` without the loss value

*   **Correct Answer:** B) `model.evaluate()` always returns the loss value first, followed by the compiled metrics in the order they were listed. `results[0]` is loss, `results[1]` is accuracy, `results[2]` is AUC.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* When metrics are compiled, `evaluate()` returns all of them, not just loss. The returned list length equals `1 + len(metrics)`.
    *   *Why B is correct:* Unpack cleanly with `loss, acc, auc = model.evaluate(X_test, y_test, verbose=0)`. The order matches: loss first, then metrics in compile order.
    *   *Why C is incorrect:* `evaluate()` returns a Python list, not a dictionary. Use `model.metrics_names` (a separate attribute) to get the corresponding string names if needed.
    *   *Why D is incorrect:* The loss value is always included as the first element, even if it was not listed in `metrics=`. The loss is always position 0.

---

### Question 16 (5 points)

A developer trains a model and observes that training loss decreases smoothly to near 0.05 while validation loss decreases for 10 epochs then rises steadily to 0.45. What is the correct diagnosis and recommended fix?

*   A) Underfitting — the model needs more layers or neurons to capture the training data patterns.
*   B) Learning rate too high — reduce the learning rate and retrain from scratch.
*   C) Overfitting — the model memorized training data but generalizes poorly; add dropout, L2 regularization, or more training data.
*   D) Class imbalance — compute class weights and pass them to `model.fit(class_weight={...})`.

*   **Correct Answer:** C) A large gap where training loss is very low and validation loss is much higher is the canonical overfitting signature. The model has memorized the training set and fails to generalize.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Underfitting means both training and validation losses remain high. A training loss near 0.05 demonstrates the model has sufficient capacity.
    *   *Why B is incorrect:* A high learning rate causes oscillating or diverging loss, not the smooth separation between train and val curves described here.
    *   *Why C is correct:* The three primary remedies: (1) regularization — `Dropout` or `kernel_regularizer=tf.keras.regularizers.l2(0.01)`; (2) reduce model capacity; (3) collect more training data to reduce the train-val distribution gap.
    *   *Why D is incorrect:* Class imbalance manifests as high overall accuracy but poor performance on the minority class — it does not produce the train/val loss divergence pattern described.

---

### Question 17 (5 points)

What keys are present in `history.history` after calling `model.fit(X_train, y_train, validation_data=(X_val, y_val))` with `metrics=['accuracy']`?

*   A) `['loss', 'accuracy']` — only training metrics are stored
*   B) `['loss', 'val_loss', 'accuracy', 'val_accuracy']` — both training and validation metrics for each epoch
*   C) `['loss', 'val_loss']` — accuracy is not stored unless explicitly requested from `model.evaluate()`
*   D) `['train_loss', 'train_accuracy', 'val_loss', 'val_accuracy']` — with `train_` prefix for training metrics

*   **Correct Answer:** B) When `validation_data` is provided, Keras automatically tracks validation versions of all compiled metrics. The naming convention adds `val_` prefix for validation metrics; training metrics have no prefix.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Providing `validation_data` causes Keras to evaluate on the validation set at the end of each epoch and add `val_loss` and `val_accuracy` to the history dictionary.
    *   *Why B is correct:* `history.history.keys()` returns `dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])`. Access training loss with `history.history['loss']`, validation accuracy with `history.history['val_accuracy']`.
    *   *Why C is incorrect:* All compiled metrics — including accuracy — are tracked in the history object during training. `model.evaluate()` is called separately for the test set and does not write to `history`.
    *   *Why D is incorrect:* Keras uses no prefix for training metrics and `val_` prefix for validation metrics. There is no `train_` prefix convention in the `History` object.

---

### Question 18 (5 points)

Which `tf.keras.callbacks.Callback` method fires at the **end of each training batch** (not epoch)?

*   A) `on_epoch_end(self, epoch, logs)`
*   B) `on_train_end(self, logs)`
*   C) `on_batch_end(self, batch, logs)`
*   D) `on_step_complete(self, step, logs)`

*   **Correct Answer:** C) `on_batch_end` fires after each gradient update step (one batch processed). `on_epoch_end` fires after all batches in an epoch are complete.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `on_epoch_end` fires once per epoch — after all mini-batches for that epoch have been processed. It is not a per-batch hook.
    *   *Why B is incorrect:* `on_train_end` fires exactly once — when `model.fit()` completes entirely. It is used for cleanup or final logging, not per-batch logic.
    *   *Why C is correct:* `on_batch_end(self, batch, logs)` receives the batch index and a `logs` dict containing the current training metrics. Useful for logging loss at sub-epoch granularity or for gradient clipping diagnostics.
    *   *Why D is incorrect:* `on_step_complete` is not a valid Keras Callback method name. The correct names are `on_batch_begin`, `on_batch_end`, `on_epoch_begin`, `on_epoch_end`, `on_train_begin`, and `on_train_end`.

---

### Question 19 (5 points)

An `ExponentialDecay` schedule is configured as follows. What is the learning rate at step 2000?

```python
schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=1000,
    decay_rate=0.96
)
```

*   A) `0.01 * 0.96 = 0.0096`
*   B) `0.01 * 0.96^2 = 0.009216`
*   C) `0.01 * 0.96^(2000) ≈ 0.0`
*   D) `0.01 - (2000 * 0.96) = -1910.99`

*   **Correct Answer:** B) Formula: `lr(t) = initial_lr * decay_rate ^ (t / decay_steps)`. At step 2000: `0.01 * 0.96 ^ (2000/1000) = 0.01 * 0.96^2 = 0.01 * 0.9216 = 0.009216`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This applies the decay only once (`0.96^1`), which corresponds to step 1000, not step 2000. At step 2000, `t/decay_steps = 2`, so the exponent is 2.
    *   *Why B is correct:* `0.96^2 = 0.9216`. Final LR = `0.01 * 0.9216 = 0.009216`. With `staircase=False` (the default), decay is continuous (smooth); with `staircase=True`, the exponent is floored to the nearest integer.
    *   *Why C is incorrect:* Using `decay_rate^t` directly (without dividing by `decay_steps`) would shrink the LR to near zero far too quickly — this is not the formula.
    *   *Why D is incorrect:* LR schedules never use subtraction. The rate is always computed multiplicatively via the exponential formula.

---

### Question 20 (5 points)

A developer adds `ModelCheckpoint(filepath='best.keras', monitor='val_loss', save_best_only=True)` to their training callbacks. Under what condition does Keras overwrite the `best.keras` file?

*   A) At the end of every epoch regardless of performance
*   B) Only when the current epoch's `val_loss` is lower than the best `val_loss` seen so far
*   C) Only when `val_accuracy` exceeds the best `val_accuracy` seen so far
*   D) When the training completes, saving the final epoch's weights

*   **Correct Answer:** B) `save_best_only=True` means the file is overwritten only when the monitored metric (`val_loss`) improves. This ensures `best.keras` always contains the weights from the epoch with the lowest validation loss.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Saving every epoch is the behavior of `save_best_only=False`. With `save_best_only=True`, only improvements trigger a save — this avoids overwriting a good checkpoint with a worse one from a later epoch.
    *   *Why B is correct:* Combine with `EarlyStopping(restore_best_weights=True)` for belt-and-suspenders: EarlyStopping restores best weights in memory; ModelCheckpoint saves them to disk as a backup in case the session crashes.
    *   *Why C is incorrect:* The `monitor='val_loss'` argument explicitly specifies which metric triggers saving. To save on `val_accuracy` improvement you would set `monitor='val_accuracy'` and `mode='max'`.
    *   *Why D is incorrect:* This describes `save_best_only=False` with training completion — that behavior saves once at the end. `save_best_only=True` saves mid-training whenever improvement occurs.
