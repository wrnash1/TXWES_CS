# Quiz: Module 11 — Transfer Learning and Fine-Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points (100 points total).

---

## Question 1

When loading a pretrained VGG16 model for transfer learning in Keras, what does the `include_top=False` argument do?

A. It removes only the final softmax activation layer while keeping the dense layers.
B. It excludes the fully connected classification layers at the top of the network, returning only the convolutional feature extraction base.
C. It prevents the model from downloading ImageNet weights and initializes all layers randomly.
D. It limits the model to processing images smaller than 224x224 pixels.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. `include_top=False` removes the entire classification head — all Dense layers and the final softmax — not just the activation function. The retained base ends at the last convolutional block.
- B — Correct. Setting `include_top=False` returns only the convolutional base, which outputs a spatial feature map rather than class probabilities. This base is used as a feature extractor, and you attach your own classification head appropriate for your specific number of classes.
- C — Incorrect. The `weights` parameter controls whether pretrained weights are loaded. `include_top=False` with `weights='imagenet'` loads the pretrained convolutional weights but omits the classification head weights.
- D — Incorrect. `include_top=False` has no effect on accepted input size. You specify the input size with the `input_shape` parameter independently.

---

## Question 2

Why must you pass `training=False` when calling the frozen base model during transfer learning, as in `x = base_model(inputs, training=False)`?

A. It prevents the base model from computing gradients, which speeds up the forward pass.
B. It forces BatchNormalization layers inside the base model to use their stored running statistics rather than computing new statistics from the current batch, preserving the pretrained normalization behavior.
C. It disables Dropout layers in the base model so that all neurons are active during feature extraction.
D. It switches the base model from float32 to float16 precision to reduce memory usage.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Gradient computation is controlled by `layer.trainable = False` and `tf.GradientTape`, not by the `training` argument. Passing `training=False` does not disable gradient computation in Keras.
- B — Correct. BatchNormalization has two modes: training mode (computes mean/variance from the current batch and updates running statistics) and inference mode (uses stored running mean/variance). When the base model is frozen, you want inference mode so the pretrained BN statistics are used unchanged. Without `training=False`, BN layers may update their running statistics during your training, degrading performance.
- C — Incorrect. Dropout behavior is also affected by the `training` flag — `training=False` does disable Dropout, which is correct for inference. However, the primary and critical reason stated in the module is the BatchNormalization behavior, which is the cause of actual performance degradation when omitted.
- D — Incorrect. The `training` argument is a Boolean flag for layer behavior modes. It has no effect on numerical precision.

---

## Question 3

In the two-phase transfer learning workflow, what is the recommended learning rate strategy when transitioning from feature extraction (Phase 1) to fine-tuning (Phase 2)?

A. Keep the same learning rate to ensure training stability and continuity.
B. Increase the learning rate by 10x to accelerate adaptation of the pretrained weights to the new domain.
C. Use a learning rate approximately 10–100 times smaller than Phase 1 to gently adjust pretrained weights without catastrophic forgetting.
D. Reset the optimizer state and use the highest learning rate that does not cause NaN loss.

Correct Answer: C

Distractor Analysis:

- A — Incorrect. Using the same Phase 1 learning rate (typically `1e-3`) for fine-tuning causes large gradient updates that overwrite the pretrained weights within a few epochs — a phenomenon called catastrophic forgetting. The model loses the generalizable features it gained from ImageNet training.
- B — Incorrect. Increasing the learning rate makes catastrophic forgetting worse. Higher learning rates produce larger parameter updates, which more aggressively overwrite pretrained representations.
- C — Correct. Fine-tuning requires a very small learning rate — typically `1e-5` when Phase 1 used `1e-3`. Small updates nudge pretrained weights toward the new task without destroying the learned feature structure. This allows the model to adapt its deep representations while retaining the generic visual vocabulary.
- D — Incorrect. Resetting the optimizer and searching for a maximum stable learning rate is not a standard fine-tuning procedure. It would also discard the optimizer momentum accumulated during Phase 1, which can destabilize training.

---

## Question 4

Which pooling operation is preferred over `Flatten` when building a classification head on top of a pretrained convolutional base, and why?

A. `MaxPooling2D`, because it selects the strongest feature activation in each spatial region, which is more informative than averaging.
B. `GlobalAveragePooling2D`, because it reduces each feature map to a single average value, producing a compact representation that reduces overfitting and is translation-invariant.
C. `AveragePooling2D` with a fixed pool size of 7x7, because it matches the spatial output size of most pretrained models.
D. `Flatten`, because it preserves all spatial information and gives the Dense layers maximum input detail.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Standard `MaxPooling2D` reduces spatial dimensions by a factor but does not reduce the spatial maps to a single vector. It cannot serve as the bridge between the convolutional base and a Dense classification head without additional flattening.
- B — Correct. `GlobalAveragePooling2D` computes the spatial average of each feature map, reducing a tensor of shape `(batch, H, W, C)` to `(batch, C)`. This is compact (avoids the large flat vector that Flatten produces), acts as a regularizer (harder to overfit a C-dimensional vector than an `H * W * C`-dimensional one), and is consistent with how models like MobileNetV2 were originally designed.
- C — Incorrect. `AveragePooling2D` with a fixed pool size would only work if the spatial output of the base model is exactly 7x7. The spatial size varies with input image size and architecture, making a fixed pool size fragile.
- D — Incorrect. While Flatten preserves spatial detail, for large base models like VGG16 the flattened vector is enormous (e.g., 25,088 for VGG16 on 224x224 input). This creates a massive, overfit-prone Dense layer and dramatically increases parameter count.

---

## Question 5

MobileNetV2 is preferred over VGG16 for mobile deployment primarily because:

A. MobileNetV2 achieves significantly higher ImageNet accuracy than VGG16.
B. MobileNetV2 uses depthwise separable convolutions that reduce the parameter count to approximately 3.4 million — about 40 times fewer than VGG16's 138 million — while maintaining competitive accuracy.
C. MobileNetV2 does not require preprocessing and accepts raw pixel values in the [0, 255] range.
D. MobileNetV2 supports variable-length input sequences, making it suitable for both image and time series data.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. MobileNetV2 (Top-1: 71.8%) does not outperform VGG16 (Top-1: 71.3%) by a significant margin, and on some benchmarks VGG16 scores comparably. The advantage of MobileNetV2 is size and speed, not superior accuracy.
- B — Correct. MobileNetV2's depthwise separable convolutions factorize each standard convolution into a depthwise step (filtering each input channel independently) and a pointwise 1x1 step (combining channels). This reduces computation by approximately 8–9 times compared to standard convolutions, yielding a model that is 40 times smaller than VGG16 with similar accuracy — making it practical for mobile apps and edge devices.
- C — Incorrect. MobileNetV2 requires its own `preprocess_input` function, which scales pixel values to the range `[-1, 1]`. Using raw `[0, 255]` inputs would produce incorrect feature activations in all layers.
- D — Incorrect. MobileNetV2 is a CNN designed exclusively for fixed-size 2-D image inputs. It has no recurrent components and cannot process sequential data of variable length.

---

## Question 6

Which of the following correctly loads a pretrained feature extractor from TensorFlow Hub and integrates it into a Keras model?

A. `hub.load(url)` returns a TensorFlow SavedModel that must be converted to Keras format before use in `model.fit`.
B. `hub.KerasLayer(url, trainable=False)` wraps the Hub module as a standard Keras layer that can be used directly in a Sequential or Functional model.
C. TensorFlow Hub modules must be downloaded manually and loaded with `keras.models.load_model()`.
D. `hub.KerasLayer` only supports text embedding models; image models must use `hub.load` instead.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. While `hub.load` does return a SavedModel, this is not the recommended Keras integration path. `hub.KerasLayer` provides a direct, first-class Keras layer wrapper that works seamlessly with `model.fit`, `model.save`, and all Keras APIs.
- B — Correct. `hub.KerasLayer(url, input_shape=(...), trainable=False)` is the standard pattern for integrating TF Hub modules into Keras models. The `trainable=False` argument freezes the module for feature extraction. Setting `trainable=True` enables fine-tuning. The resulting layer behaves identically to any other Keras layer.
- C — Incorrect. TensorFlow Hub modules are downloaded automatically on first use and cached locally. No manual download is needed, and `keras.models.load_model` is for loading previously saved Keras models, not Hub modules.
- D — Incorrect. `hub.KerasLayer` supports all types of TF Hub modules: image classifiers, image feature vectors, text embeddings, video modules, and more. The TF Hub catalog explicitly lists image feature vector modules as a primary use case.

---

## Question 7

A researcher fine-tunes ResNet50 on a medical imaging dataset of 500 chest X-rays across 2 classes. After fine-tuning all 50 layers with a learning rate of `1e-3`, validation accuracy is worse than before fine-tuning began. What is the most likely cause?

A. ResNet50 is incompatible with binary classification tasks and requires a minimum of 10 output classes.
B. The learning rate of `1e-3` is too large for fine-tuning and caused catastrophic forgetting, overwriting the pretrained ImageNet features before they could be adapted.
C. The batch size must equal the number of training examples for fine-tuning to work correctly.
D. The dataset is too large — ResNet50 fine-tuning requires fewer than 100 training examples.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. ResNet50 works with any number of output classes. Binary classification simply requires 2 output neurons (or 1 with sigmoid). Architecture compatibility is not the issue here.
- B — Correct. Using `1e-3` for fine-tuning a fully unfrozen ResNet50 produces large gradient updates that overwrite the pretrained weights within a few epochs. The model loses the generalizable ImageNet features and essentially restarts learning from near-random weights — but with only 500 examples, it cannot relearn effectively, resulting in worse validation accuracy than the frozen Phase 1 baseline.
- C — Incorrect. Batch size equal to dataset size (gradient descent with no mini-batching) is not a requirement for fine-tuning and is computationally impractical. Standard batch sizes of 16–64 are typical.
- D — Incorrect. 500 examples is small but not incompatible with fine-tuning. The actual problem is the learning rate, not the dataset size. With only 500 examples, fine-tuning should be done with very few unfrozen layers and an especially low learning rate.

---

## Question 8

When using `MobileNetV2` from `tensorflow.keras.applications`, which preprocessing function must be applied to input images?

A. `tf.keras.applications.vgg16.preprocess_input`, which subtracts ImageNet channel means.
B. A manual division by 255 using `tf.cast(image, tf.float32) / 255.0`.
C. `tf.keras.applications.mobilenet_v2.preprocess_input`, which scales pixel values from `[0, 255]` to `[-1, 1]`.
D. No preprocessing is needed — MobileNetV2 includes an internal normalization layer that handles raw `[0, 255]` inputs automatically.

Correct Answer: C

Distractor Analysis:

- A — Incorrect. VGG16's `preprocess_input` subtracts fixed channel-wise ImageNet means and converts from RGB to BGR. Applying this to MobileNetV2 inputs would shift all values into a range the model was not trained on, degrading all feature activations.
- B — Incorrect. Dividing by 255 produces values in `[0, 1]`, not `[-1, 1]`. MobileNetV2 was trained with inputs in `[-1, 1]`. Using `[0, 1]` inputs with a frozen MobileNetV2 model will degrade feature quality because the activation ranges expected by the trained weights are mismatched.
- C — Correct. `mobilenet_v2.preprocess_input` applies the transformation `(pixel / 127.5) - 1`, which maps `[0, 255]` to `[-1, 1]`. This matches the normalization used during MobileNetV2's original ImageNet training and ensures correct behavior of all pretrained weights.
- D — Incorrect. `tensorflow.keras.applications.MobileNetV2` does not include an internal preprocessing layer. The caller is responsible for applying the correct `preprocess_input` function before passing images to the model.

---

## Question 9

In a transfer learning setup, what is the purpose of setting `layer.trainable = False` on individual layers of the base model before the final `model.compile` call?

A. It permanently deletes the weights of those layers to reduce the model's memory footprint.
B. It marks those layers so that their weights are not updated during `model.fit`, effectively freezing them while allowing other layers to train.
C. It converts those layers from float32 to float16 precision to speed up training.
D. It applies L2 regularization to those layers to prevent their weights from changing too rapidly.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Setting `trainable = False` does not modify or delete the weight tensors. The weights remain in memory at their current values. They are simply excluded from the gradient update step.
- B — Correct. The `trainable` attribute controls whether a layer's weights are included in the list of variables passed to the optimizer. When `trainable=False`, the layer's weights are not in `model.trainable_weights`, so the optimizer computes no gradient updates for them. The weights are preserved unchanged throughout training.
- C — Incorrect. Numerical precision (float32 vs. float16) is controlled through `tf.keras.mixed_precision` policies or explicit casting, not through the `trainable` attribute.
- D — Incorrect. Regularization is a separate mechanism added via `kernel_regularizer`, `bias_regularizer`, or `activity_regularizer` parameters. The `trainable` attribute has no regularization effect.

---

## Question 10

A team is building a custom image classifier for 20 classes of industrial defects. They have 200 labeled images per class (4,000 total). The target deployment is a Raspberry Pi 4 with no GPU. Which pretrained model and strategy is most appropriate?

A. VGG16, fine-tune all layers with learning rate `1e-3` — the large model capacity is needed for industrial images.
B. MobileNetV2, feature extraction only (frozen base), with a small dense head — the compact architecture suits edge deployment and the dataset is too small for aggressive fine-tuning.
C. ResNet50, full fine-tuning with learning rate `1e-3` — the residual connections prevent overfitting on small datasets.
D. Train a custom CNN from scratch — pretrained models were trained on natural images and will not transfer to industrial defect images.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. VGG16 at 528 MB is impractical for Raspberry Pi deployment. Its inference speed on CPU is also significantly slower than MobileNetV2. Fine-tuning all layers with `1e-3` on 4,000 images would cause catastrophic forgetting and severe overfitting.
- B — Correct. MobileNetV2's 14 MB model size and efficient depthwise separable convolutions make it suitable for Raspberry Pi inference. With only 200 images per class, feature extraction (frozen base) is safer than fine-tuning — the small dataset cannot adequately train a large number of parameters. If fine-tuning is attempted later, it should involve only the last few layers with a very small learning rate.
- C — Incorrect. ResNet50 at 98 MB is manageable but heavier than needed for edge deployment. Residual connections help with training stability in deep networks, not specifically with overfitting on small datasets. Full fine-tuning with `1e-3` on 4,000 images would overwrite pretrained features.
- D — Incorrect. Transfer learning from ImageNet to industrial images has been repeatedly demonstrated to work well in practice, even when the domains appear dissimilar. Low-level features (edges, textures, gradients) transfer broadly. Training from scratch on 4,000 images would almost certainly produce a weaker model than transfer learning.

---

*End of Quiz — Module 11*

---

### Question 11 (5 points)

When fine-tuning, a developer unfreezes the last 20 layers of a MobileNetV2 base model. Which code correctly unfreezes only those layers while keeping the rest frozen?

- A) `base_model.trainable = True` followed by `for layer in base_model.layers[:20]: layer.trainable = False`
- B) `base_model.trainable = True` followed by `for layer in base_model.layers[:-20]: layer.trainable = False`
- C) `for layer in base_model.layers[-20:]: layer.trainable = True`
- D) `base_model.layers[-20:].trainable = True`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* First, `base_model.trainable = True` enables gradient computation for the entire base model. Then, looping over `base_model.layers[:-20]` (all layers except the last 20) and setting `trainable = False` re-freezes the early layers. The last 20 layers (index -20 to end) remain trainable. This is the standard fine-tuning pattern: unfreeze the whole base, then re-freeze everything except the desired tail.
  - *Why A is incorrect:* `base_model.layers[:20]` refers to the first 20 layers (indices 0–19), not the last 20. Freezing the first 20 layers and training the rest means the early (most generic) features are frozen and the later (more specific) features are trained, which is correct for a different scenario — but the code selects the wrong group given the intent.
  - *Why C is incorrect:* While setting `trainable=True` on `layers[-20:]` enables those layers, if `base_model.trainable` is still `False` from the Phase 1 setup, the top-level flag overrides individual layer flags in some Keras versions. The safe pattern is to set `base_model.trainable = True` first, then freeze what you want frozen.
  - *Why D is incorrect:* `base_model.layers[-20:]` returns a Python list, not a Keras layer object. Lists do not have a `trainable` attribute. Setting `.trainable` on a list raises an `AttributeError`.

---

### Question 12 (5 points)

EfficientNetB0 uses a technique called "compound scaling." What does this mean?

- A) The model scales only the width (number of filters) of each layer while keeping depth and resolution fixed.
- B) The model simultaneously scales depth (number of layers), width (filter counts), and input resolution using a fixed ratio derived from a neural architecture search, optimizing accuracy under a compute budget.
- C) The model scales the learning rate, batch size, and number of epochs together proportionally to the dataset size.
- D) The model applies progressive resizing during training, starting with small images and scaling up the resolution each epoch.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* EfficientNet's key contribution (Tan & Le, 2019) is compound scaling: given a compute multiplier φ, width scales by `α^φ`, depth by `β^φ`, and resolution by `γ^φ`, where `α`, `β`, `γ` are determined by grid search on EfficientNetB0. This principled co-scaling achieves better accuracy-efficiency tradeoffs than scaling any single dimension alone.
  - *Why A is incorrect:* Scaling only width while fixing depth and resolution is the approach taken by some older architectures. EfficientNet explicitly scales all three dimensions simultaneously according to the compound coefficient.
  - *Why C is incorrect:* Compound scaling in EfficientNet refers to the network architecture dimensions (layers, filters, image resolution), not training hyperparameters. Hyperparameter scaling is a separate concept not part of the EfficientNet paper.
  - *Why D is incorrect:* Progressive resizing during training is a training curriculum technique used in fast.ai's image training approach. It is a data augmentation / training strategy, not an architectural design principle. EfficientNet's compound scaling is a property of the architecture, not the training procedure.

---

### Question 13 (5 points)

Which preprocessing function should be used for images fed into an `InceptionV3` model loaded from `tf.keras.applications`?

- A) `tf.keras.applications.vgg16.preprocess_input` — all Keras applications share the same preprocessing.
- B) `tf.keras.applications.inception_v3.preprocess_input` — which scales pixel values to `[-1, 1]`.
- C) `tf.image.per_image_standardization` — which subtracts the mean and divides by the standard deviation of each individual image.
- D) No preprocessing is needed; `InceptionV3` accepts raw `uint8` images in `[0, 255]` directly.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `tf.keras.applications.inception_v3.preprocess_input` applies the same `(x / 127.5) - 1` transformation used during InceptionV3's original ImageNet training, mapping pixel values to `[-1, 1]`. Each Keras applications model has its own `preprocess_input` function that must be used to match the model's training distribution.
  - *Why A is incorrect:* VGG16's preprocessing subtracts fixed per-channel ImageNet means (103.939, 116.779, 123.68) and converts RGB to BGR — a completely different transformation. Applying VGG16 preprocessing to InceptionV3 inputs would produce incorrect feature activations.
  - *Why C is incorrect:* Per-image standardization normalizes each image individually using its own mean and standard deviation. This is not the correct preprocessing for InceptionV3, which was trained with a fixed global normalization scheme, not per-image standardization.
  - *Why D is incorrect:* No Keras applications model accepts raw `uint8` inputs without preprocessing. Passing values in `[0, 255]` to InceptionV3 would produce severely out-of-distribution activations in all layers because the model was trained on `[-1, 1]` scaled inputs.

---

### Question 14 (5 points)

A developer uses the Keras Functional API to build a transfer learning model. Which code snippet is correct for the feature extraction phase?

- A) `base = MobileNetV2(include_top=False, weights='imagenet'); base.trainable = True; x = base.output; x = GlobalAveragePooling2D()(x); output = Dense(5, activation='softmax')(x)`
- B) `base = MobileNetV2(include_top=False, weights='imagenet', input_shape=(224,224,3)); base.trainable = False; x = base.output; x = GlobalAveragePooling2D()(x); output = Dense(5, activation='softmax')(x); model = Model(inputs=base.input, outputs=output)`
- C) `base = MobileNetV2(include_top=True, weights='imagenet'); base.trainable = False; output = Dense(5, activation='softmax')(base.output)`
- D) `base = MobileNetV2(include_top=False, weights=None); base.trainable = False; x = Flatten()(base.output); output = Dense(5)(x)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* This is the complete, correct Keras Functional API transfer learning pattern. `include_top=False` removes the classification head. `weights='imagenet'` loads pretrained weights. `input_shape=(224,224,3)` specifies the expected input. `base.trainable = False` freezes the base. `GlobalAveragePooling2D` provides an efficient transition. `Model(inputs=base.input, outputs=output)` creates the full model. `Dense(5, softmax)` adds a 5-class head.
  - *Why A is incorrect:* `base.trainable = True` enables training of all base model weights from the start, which is fine-tuning — not feature extraction. With a new head initialized with random weights, training from a high learning rate would corrupt the pretrained features immediately.
  - *Why C is incorrect:* `include_top=True` retains the original ImageNet Dense head including `Dense(1000, softmax)`. Adding another `Dense(5)` layer on top of that 1000-class output is architecturally incorrect and would not learn meaningful representations for 5 classes.
  - *Why D is incorrect:* `weights=None` initializes all MobileNetV2 weights randomly, providing no benefit from ImageNet pretraining. Feature extraction requires pretrained weights to be loaded. Additionally, `Flatten` instead of `GlobalAveragePooling2D` produces a much larger and more overfit-prone classification head.

---

### Question 15 (5 points)

After Phase 1 (feature extraction) training for 10 epochs, a developer begins Phase 2 (fine-tuning). What must be done before calling `model.fit` again in Phase 2?

- A) Call `model.reset_states()` to clear the optimizer's momentum and start fresh.
- B) Unfreeze the desired layers, then call `model.compile()` again with the lower learning rate — recompilation is required after changing layer trainability.
- C) Save and reload the model with `model.save()` and `tf.keras.models.load_model()` to commit the trainability changes.
- D) No additional steps are needed — changing `layer.trainable` is automatically detected by the optimizer between calls to `model.fit`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In Keras, after modifying `layer.trainable`, you must call `model.compile()` again before training. This recompilation updates the list of `model.trainable_weights` that the optimizer tracks. Without recompilation, the optimizer may continue updating the pre-Phase-2 set of variables, ignoring the newly unfrozen layers. The new `model.compile()` call should use the reduced learning rate (e.g., `1e-5`).
  - *Why A is incorrect:* Resetting optimizer state (momentum, velocity buffers) between phases is not required and can hurt convergence. Some practitioners intentionally preserve optimizer momentum for a smoother transition. The critical step is recompilation to update the trainable variable list.
  - *Why C is incorrect:* Saving and reloading the model is not required to commit trainability changes. The `layer.trainable` attribute is in memory and takes effect after `model.compile()`. A save-and-reload cycle would be unnecessary overhead.
  - *Why D is incorrect:* Keras does not automatically detect trainability changes between `fit` calls. The `trainable_weights` list is computed at compile time and cached. The model will continue training the same set of variables until `model.compile()` is called again.

---

### Question 16 (5 points)

Which statement correctly describes "catastrophic forgetting" in the context of neural network fine-tuning?

- A) The model forgets the class labels it learned during Phase 1 and must be retrained from scratch on the original dataset.
- B) The model's pretrained weights are overwritten by large gradient updates during fine-tuning, destroying the generalizable feature representations learned from the source domain.
- C) The GPU forgets the model's computation graph after each epoch and retraces it from scratch, causing slow training.
- D) The optimizer forgets which layers are frozen and accidentally updates all layers uniformly, regardless of the `trainable` flag.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Catastrophic forgetting occurs when a neural network trained on a new task with a high learning rate overwrites the weights that encoded useful knowledge from the previous task (ImageNet features). After catastrophic forgetting, the model is essentially randomly initialized with respect to general visual features and must relearn them from the small target dataset — a task it typically cannot do effectively with limited labeled data.
  - *Why A is incorrect:* The "forgetting" in catastrophic forgetting refers to the overwriting of general feature representations in the convolutional weights, not the class label assignments. The model does not "remember" class labels in any specific way — it learns class-discriminative weights throughout the network.
  - *Why C is incorrect:* TensorFlow's computation graph tracing is an internal framework mechanism unrelated to catastrophic forgetting. Graph retracing affects compilation speed, not weight values or generalization.
  - *Why D is incorrect:* The `trainable` flag is enforced by Keras's compilation step, not by the optimizer at runtime. When a model is correctly compiled after setting `trainable` flags, the optimizer only receives and updates the trainable variable list.

---

### Question 17 (5 points)

How does a TF Hub image feature vector module differ from a TF Hub image classifier module?

- A) Feature vector modules output a flat embedding vector (e.g., `(batch, 1280)`) used as input to a custom classification head; classifier modules output full class probabilities over a fixed label set.
- B) Feature vector modules require GPU acceleration; classifier modules run on CPU only.
- C) Feature vector modules use larger input images (448×448) while classifier modules use standard 224×224 inputs.
- D) Feature vector modules are fine-tunable; classifier modules are permanently frozen and cannot be fine-tuned.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* TF Hub provides two types of image modules. Feature vector modules (e.g., `imagenet/mobilenet_v2_100_224/feature_vector`) output a fixed-length embedding vector stripped of the classification head — these are used for transfer learning with a custom Dense head for any number of classes. Classifier modules (e.g., `imagenet/mobilenet_v2_100_224/classification`) output 1,001 ImageNet class probabilities — useful for direct inference on ImageNet classes but not for custom tasks.
  - *Why B is incorrect:* Both module types run on either GPU or CPU. TF Hub does not restrict execution hardware based on module type.
  - *Why C is incorrect:* Input image size is specified by the module URL and is a property of the specific module variant (e.g., `_224_` in the URL), not a categorical difference between feature vector and classifier modules.
  - *Why D is incorrect:* Both feature vector and classifier modules can be set to `trainable=True` or `trainable=False` via the `hub.KerasLayer` wrapper. Fine-tunability is not a categorical distinction between module types.

---

### Question 18 (5 points)

When should a developer choose fine-tuning over feature extraction for a transfer learning project?

- A) When the target dataset is large enough (typically thousands of labeled examples) and sufficiently different from the source domain that the pretrained high-level features may not transfer perfectly.
- B) When the target dataset has fewer than 100 examples per class, making fine-tuning safer because it involves fewer weight updates.
- C) Fine-tuning should always be used over feature extraction because it produces strictly higher accuracy in all scenarios.
- D) When the deployment target is a mobile device — fine-tuning makes the model smaller and faster for edge inference.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Fine-tuning is most beneficial when the target domain differs meaningfully from the source domain (e.g., ImageNet → medical imaging or satellite imagery) and sufficient labeled data exists to re-optimize the deeper feature representations without overfitting. With large labeled datasets (10,000+ examples), fine-tuning the last few blocks typically improves accuracy over frozen feature extraction.
  - *Why B is incorrect:* Very small datasets (fewer than 100 examples per class) are precisely when fine-tuning is most dangerous. With so few examples, fine-tuning leads to severe overfitting. Feature extraction (frozen base + small Dense head) is the recommended strategy for small datasets.
  - *Why C is incorrect:* Fine-tuning does not always outperform feature extraction. When the source and target domains are similar (e.g., both natural images) and the dataset is small, feature extraction often matches or exceeds fine-tuning accuracy while requiring less careful tuning.
  - *Why D is incorrect:* Fine-tuning does not change the model's size or inference speed. Model size is determined by architecture (MobileNetV2 vs. VGG16 etc.), and fine-tuning only adjusts weight values without removing parameters.

---

### Question 19 (5 points)

A developer loads VGG16 with `include_top=False` and passes an image of shape `(1, 224, 224, 3)`. What is the output shape of the VGG16 base model?

- A) `(1, 7, 7, 512)`
- B) `(1, 224, 224, 3)`
- C) `(1, 25088)`
- D) `(1, 1000)`

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* VGG16 with `include_top=False` terminates at the last MaxPooling layer. Starting from a `(224, 224, 3)` input, 5 max pooling operations each halve the spatial dimensions: 224 → 112 → 56 → 28 → 14 → 7. The depth at the final convolutional block is 512. The output is therefore `(batch, 7, 7, 512)`.
  - *Why B is incorrect:* The original input shape is `(224, 224, 3)`. The convolutional and pooling layers progressively reduce the spatial dimensions. The output is much smaller than the input when `include_top=False`.
  - *Why C is incorrect:* `(1, 25088)` is the shape of the flattened output: `7 * 7 * 512 = 25,088`. This flattening occurs inside VGG16's classification head, which is excluded when `include_top=False`. The raw base output is the unflattened 3D spatial tensor.
  - *Why D is incorrect:* `(1, 1000)` is the shape of VGG16's final softmax output over 1,000 ImageNet classes. This is the output when `include_top=True`. With `include_top=False`, the classification head is removed.

---

### Question 20 (5 points)

What is the effect of passing `input_shape=(160, 160, 3)` instead of the default `(224, 224, 3)` when loading a MobileNetV2 base model with `include_top=False`?

- A) The model raises an error because MobileNetV2 only accepts exactly `(224, 224, 3)` input.
- B) The model accepts `160×160` inputs and produces a proportionally smaller spatial feature map at the output, allowing faster inference with a slight accuracy tradeoff.
- C) The model automatically upsamples all input images to `(224, 224, 3)` internally to match the pretrained architecture.
- D) Using a non-standard input size invalidates the pretrained ImageNet weights, so random initialization is used automatically.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `include_top=False` makes MobileNetV2 flexible to different input sizes. With `(160, 160, 3)` input, the spatial output of the convolutional base is proportionally smaller (e.g., `5 × 5 × 1280` instead of `7 × 7 × 1280`). The pretrained weights are still valid because convolutional weights are spatial-size independent — only the spatial dimensions of intermediate activations change. `GlobalAveragePooling2D` aggregates these into the same-length vector regardless of spatial size.
  - *Why A is incorrect:* MobileNetV2 loaded with `include_top=False` explicitly accepts variable input sizes. The `include_top=True` version requires `(224, 224, 3)` because the Dense classification head expects a fixed input size. Without the Dense head, any spatial resolution is valid.
  - *Why C is incorrect:* Keras does not automatically resize inputs inside the model. If the developer passes `(160, 160, 3)` images, they are processed at that resolution. Resizing would need to be done explicitly in the data pipeline.
  - *Why D is incorrect:* The pretrained convolutional weights are fully valid for any input resolution because convolutional layers are spatially translation-invariant and parameter sharing means the same filter is applied at any spatial position. Only the Dense layers (excluded by `include_top=False`) require a specific spatial input size.
