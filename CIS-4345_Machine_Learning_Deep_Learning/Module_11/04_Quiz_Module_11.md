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
