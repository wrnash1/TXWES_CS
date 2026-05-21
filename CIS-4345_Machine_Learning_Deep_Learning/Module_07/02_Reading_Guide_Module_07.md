# Reading Guide: Module 07 - Transfer Learning and Fine-Tuning
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 07 - Transfer Learning and Fine-Tuning**! Transfer learning is one of the most powerful and practical techniques in modern deep learning: instead of training a CNN from scratch, you load a model pre-trained on a large dataset (such as ImageNet) and adapt it for your specific task. This approach dramatically reduces training time and data requirements, and it is a high-priority topic on the TensorFlow Developer Certificate exam.

You will learn how to use `tf.keras.applications` to load pre-trained models such as MobileNetV2 and InceptionV3, how to freeze base model layers to perform feature extraction, and how to unfreeze layers for fine-tuning to achieve higher accuracy on your target dataset.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Transfer learning**: A technique where a model trained on one large dataset (the source task, e.g., ImageNet with 1.2 million images and 1,000 classes) is reused as the starting point for a model on a different but related task (the target task). The pre-trained model has already learned low-level features like edges, textures, and shapes that are useful across many vision tasks.

*   **Pre-trained model**: A CNN whose weights have already been optimized through training on a large benchmark dataset. In Keras, pre-trained models are available via `tf.keras.applications`, e.g., `tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(160,160,3))`. Setting `include_top=False` removes the original classification head so you can attach your own output layers.

*   **Feature extraction**: The first stage of transfer learning — the base model's convolutional layers are frozen (weights are not updated during training) and used only to extract feature representations from images. A new classification head (`GlobalAveragePooling2D → Dense → output`) is trained on top of the frozen features.

*   **Fine-tuning**: The second stage of transfer learning — after the classification head has converged, some or all of the base model's layers are unfrozen and the entire model is trained end-to-end at a very low learning rate (e.g., `1e-5`). Fine-tuning adjusts the pre-trained weights to better match the target dataset's specific features.

*   **`layer.trainable = False`**: The Keras attribute that freezes a layer, preventing its weights from being updated during backpropagation. Setting `base_model.trainable = False` freezes the entire pre-trained base. Individual layers can be selectively unfrozen for fine-tuning by setting `base_model.layers[-20:]` layers to `trainable = True`.

*   **GlobalAveragePooling2D**: A pooling layer that averages each feature map across all spatial positions, producing a single value per feature map. It replaces the Flatten layer in transfer learning architectures, producing a compact representation regardless of the base model's output spatial size and significantly reducing the number of parameters in the classification head.

---

### 2. Certification Exam Tips
*   **Two-Stage Training Pattern:** The TF exam transfer learning pattern is: (1) load pre-trained base with `include_top=False`, freeze it, add `GlobalAveragePooling2D → Dense → output`, compile and train at normal LR; (2) unfreeze top layers of base, recompile at very low LR (1e-5), and fine-tune for additional epochs.
*   **`include_top=False` is required:** Always set `include_top=False` when loading a pre-trained model for transfer learning. This removes the 1,000-class ImageNet output head so you can attach your own output layer with the correct number of classes.
*   **Recompile after unfreezing:** After setting `base_model.trainable = True` for fine-tuning, you MUST call `model.compile()` again. Changing `trainable` attributes without recompiling has no effect on the training graph.
*   **Study Resource:** The [TensorFlow Transfer Learning and Fine-Tuning tutorial](https://www.tensorflow.org/tutorials/images/transfer_learning) at tensorflow.org walks through the complete two-stage process with MobileNetV2 and is one of the most directly exam-representative tutorials available. The [fast.ai Practical Deep Learning course](https://course.fast.ai/) covers transfer learning in Lesson 1 using a real-world image classification task similar to the exam format.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow Transfer Learning tutorial](https://www.tensorflow.org/tutorials/images/transfer_learning) at tensorflow.org. This free official tutorial covers loading MobileNetV2, freezing/unfreezing layers, GlobalAveragePooling2D, and the complete two-stage training pipeline tested on the exam.
*   **Required Video:** Watch the Transfer Learning lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers `tf.keras.applications`, feature extraction vs fine-tuning, and the `trainable` attribute with runnable code examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Load a pre-trained base model**: Use `tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(160,160,3))` and set `base_model.trainable = False` to freeze all convolutional layers.
*   **Build and train a feature extraction model**: Add `GlobalAveragePooling2D()`, `Dense(128, activation='relu')`, and `Dense(num_classes, activation='softmax')` on top of the frozen base, compile with Adam and `sparse_categorical_crossentropy`, and train for 10 epochs.
*   **Fine-tune the model**: Unfreeze the last 20 layers of the base model, recompile with `learning_rate=1e-5`, and train for 5 more epochs. Compare validation accuracy before and after fine-tuning.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and describe the difference between feature extraction and fine-tuning in your own words.
*   [ ] Work through the [TensorFlow Transfer Learning tutorial](https://www.tensorflow.org/tutorials/images/transfer_learning).
*   [ ] Watch the transfer learning lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 07 lab: feature extraction and fine-tuning with MobileNetV2.
*   [ ] Proceed to the Module 07 quiz.
