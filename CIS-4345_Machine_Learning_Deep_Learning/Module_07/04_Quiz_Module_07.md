# Quiz: Module 07 - Transfer Learning and Fine-Tuning
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
When loading a pre-trained Keras model for transfer learning, what does setting `include_top=False` do?
*   A) It prevents the model from loading pre-trained ImageNet weights, forcing random initialization.
*   B) It removes the final fully connected classification layers of the pre-trained model, so you can attach your own output head suited to your target task.
*   C) It freezes all layers in the model so that none of the pre-trained weights can be updated during training.
*   D) It limits the model to using only the top (deepest) convolutional layers and discards all earlier feature extraction layers.
*   **Correct Answer:** B) `include_top=False` strips the original 1,000-class ImageNet classification head from the pre-trained model, leaving only the convolutional base. You then attach your own `GlobalAveragePooling2D`, `Dense`, and output layers for your specific task.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Pre-trained weights are loaded independently via `weights='imagenet'`. Setting `include_top=False` only removes the classification head — the convolutional base still loads its ImageNet weights.
    *   *Why B is correct:* Usage: `base = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(160,160,3))`. The exam requires knowing this parameter to build a transfer learning pipeline.
    *   *Why C is incorrect:* Freezing layers is a separate step controlled by `base_model.trainable = False`. `include_top` and `trainable` are independent properties.
    *   *Why D is incorrect:* `include_top=False` removes the classification head at the end of the network (the "top"), not any convolutional layers. All feature extraction layers are preserved.

---

**Question 2**
Which of the following is the most accurate definition of **fine-tuning** in the context of transfer learning?
*   A) The process of loading a pre-trained model and immediately using it to make predictions on a new dataset without any additional training.
*   B) A data preprocessing step that scales input pixel values from [0, 255] to [0, 1] to improve training stability.
*   C) The second stage of transfer learning in which some or all of the pre-trained base model's frozen layers are unfrozen and the entire model is trained end-to-end at a very low learning rate to adapt the pre-trained features to the target task.
*   D) A regularization technique that randomly drops entire convolutional feature maps during training to prevent overfitting in deep networks.
*   **Correct Answer:** C) Fine-tuning builds on a feature extraction phase — once the new classification head has converged, you selectively unfreeze layers in the base model and retrain at a very low learning rate (e.g., 1e-5) so the pre-trained weights shift slightly toward the target domain without forgetting what they learned on ImageNet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using a model for direct inference without additional training is called inference or zero-shot transfer, not fine-tuning. Fine-tuning always involves additional training.
    *   *Why B is incorrect:* This describes pixel normalization using `rescale=1./255` in `ImageDataGenerator`, a preprocessing step independent of the fine-tuning concept.
    *   *Why C is correct:* After `model.compile()` with a low LR and `model.fit()` for additional epochs with unfrozen base layers, validation accuracy typically improves over feature extraction alone.
    *   *Why D is incorrect:* This describes Spatial Dropout or feature map dropout, a regularization technique — not fine-tuning.

---

**Question 3**
A developer wants to perform feature extraction with MobileNetV2. Which code correctly loads the pre-trained base, freezes it, and adds a classification head for 5-class classification?
*   A) `base = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(160,160,3)); base.trainable = False; model = tf.keras.Sequential([base, tf.keras.layers.GlobalAveragePooling2D(), tf.keras.layers.Dense(5, activation='softmax')])`
*   B) `base = tf.keras.applications.MobileNetV2(weights=None, include_top=True); model = tf.keras.Sequential([base, tf.keras.layers.Dense(5, activation='sigmoid')])`
*   C) `base = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False); base.trainable = True; model = tf.keras.Sequential([base, tf.keras.layers.Flatten(), tf.keras.layers.Dense(5, activation='softmax')])`
*   D) `model = tf.keras.Sequential([tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(160,160,3)), tf.keras.layers.GlobalAveragePooling2D(), tf.keras.layers.Dense(5, activation='softmax')])`
*   **Correct Answer:** A) This correctly loads MobileNetV2 with ImageNet weights, removes its top, freezes the base with `trainable = False`, and adds `GlobalAveragePooling2D` and a 5-unit softmax output for feature extraction.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the canonical feature extraction pattern. Compile with `loss='sparse_categorical_crossentropy', optimizer='adam'`. After initial training, you can unfreeze top layers and fine-tune at LR=1e-5.
    *   *Why B is incorrect:* `weights=None` initializes weights randomly — there is no transfer of knowledge. `include_top=True` keeps the 1,000-class ImageNet head, making the appended Dense(5) layer architecturally incorrect.
    *   *Why C is incorrect:* Setting `base.trainable = True` immediately unfreezes all base layers, meaning the pre-trained ImageNet weights will be overwritten from the start instead of being preserved for feature extraction.
    *   *Why D is incorrect:* This builds a CNN from scratch rather than using a pre-trained base. It has no transfer learning — all weights are randomly initialized and must be learned from your small dataset.

---

**Question 4**
After completing feature extraction training, a developer unfreezes the top 20 layers of the base model for fine-tuning. What additional step is required before calling `model.fit()` again?
*   A) Call `model.reset_weights()` to reinitialize the weights of the newly unfrozen layers to random values.
*   B) Call `model.compile()` again with a very low learning rate (e.g., `1e-5`) to rebuild the training graph with the updated `trainable` attributes.
*   C) Call `model.evaluate()` to measure current performance before fine-tuning begins, which automatically prepares the model for the next training run.
*   D) Call `base_model.trainable = False` a second time to confirm the freeze state before running the fine-tuning loop.
*   **Correct Answer:** B) Changing `trainable` attributes on layers does not take effect until `model.compile()` is called again. The very low learning rate (1e-5 vs the typical 1e-3 for Adam) prevents the fine-tuning pass from catastrophically overwriting the pre-trained weights.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The purpose of fine-tuning is to adapt the existing pre-trained weights — resetting them to random values would destroy the benefit of transfer learning entirely.
    *   *Why B is correct:* This is a critical exam pattern. The sequence is: (1) unfreeze layers, (2) `model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), ...)`, (3) `model.fit(...)` for fine-tuning epochs.
    *   *Why C is incorrect:* `model.evaluate()` runs inference to compute metrics — it does not modify the training configuration or prepare the model for subsequent training.
    *   *Why D is incorrect:* Calling `trainable = False` after unfreezing would re-freeze the layers, undoing the fine-tuning setup entirely.

---

**Question 5**
A developer trains a transfer learning model on a dataset of 500 images (5 classes). After feature extraction, validation accuracy is 82%. After fine-tuning all base layers with `learning_rate=0.01`, validation accuracy drops to 64%. What is the most likely cause?
*   A) The `include_top=False` argument caused the model to lose its classification head during fine-tuning.
*   B) The learning rate for fine-tuning was too high, causing catastrophic forgetting — the large weight updates overwrote the pre-trained ImageNet features.
*   C) The model requires more convolutional layers to extract sufficient features from a 500-image dataset.
*   D) Fine-tuning always reduces validation accuracy because unfreezing layers introduces additional noise into the model's predictions.
*   **Correct Answer:** B) Fine-tuning requires a very small learning rate (typically 1e-5 to 1e-4) so the pre-trained weights shift only slightly. Using `lr=0.01` (100x–1000x too large) causes the optimizer to take large gradient steps that destroy the useful low-level features learned on ImageNet — a problem called catastrophic forgetting.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `include_top=False` is set only at model load time and does not change during fine-tuning. The classification head you added remains attached throughout training.
    *   *Why B is correct:* The standard fine-tuning learning rate is `Adam(learning_rate=1e-5)`. At `lr=0.01`, weight updates are so large that the convolutional features that worked well during feature extraction are overwritten with noise-like values.
    *   *Why C is incorrect:* Transfer learning is specifically designed to work well with small datasets because the base model already knows low-level features. Adding more layers would not address the fine-tuning instability.
    *   *Why D is incorrect:* Fine-tuning with the correct low learning rate consistently improves accuracy over feature extraction alone. The problem here is the specific learning rate choice, not fine-tuning in general.
