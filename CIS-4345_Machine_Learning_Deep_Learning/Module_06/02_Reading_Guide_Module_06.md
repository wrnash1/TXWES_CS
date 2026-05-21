# Reading Guide: Module 06 - Convolutional Neural Networks (CNNs) for Image Classification
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 06 - Convolutional Neural Networks (CNNs) for Image Classification**! CNNs are the dominant architecture for image tasks and are one of the four core task categories on the TensorFlow Developer Certificate exam. Unlike fully connected networks that flatten images and lose spatial relationships, CNNs use convolutional filters that slide across the image and detect local features like edges, textures, and shapes — regardless of where they appear in the image.

You will learn to build CNN architectures with `tf.keras.layers.Conv2D`, `MaxPooling2D`, `Flatten`, and `Dense` layers, and how to use `ImageDataGenerator` to load and preprocess image datasets.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Convolutional layer (Conv2D)**: Applies a set of learnable filters to the input image. Each filter slides across the spatial dimensions and computes a dot product with the local patch of pixels, producing a feature map. In Keras: `tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', padding='same')`. The number of filters determines how many feature maps are produced.

*   **MaxPooling2D**: A downsampling layer that reduces the spatial dimensions of feature maps by taking the maximum value in each pooling window. `tf.keras.layers.MaxPooling2D(pool_size=(2,2))` halves both the height and width. Pooling reduces computation, controls overfitting, and introduces some translation invariance.

*   **Flatten layer**: Converts the 3D feature map tensor (height × width × channels) output from the last convolutional/pooling layer into a 1D vector so it can be fed into Dense layers. `tf.keras.layers.Flatten()` has no trainable parameters — it only reshapes the tensor.

*   **Feature map**: The output of a convolutional filter applied to an input. Each filter learns to detect a specific low-level feature (e.g., horizontal edges, diagonal textures). Deeper layers combine these into higher-level features (e.g., eyes, wheels). The shape of a feature map is (batch, height, width, filters).

*   **ImageDataGenerator**: A Keras utility for loading images from directories and optionally applying real-time data augmentation (rotation, zoom, horizontal flip). `ImageDataGenerator(rescale=1./255)` normalizes pixel values from [0, 255] to [0, 1]. `flow_from_directory()` creates batches from a folder structure where each subfolder is a class.

*   **Padding**: Controls whether the filter extends beyond the edges of the input. `padding='same'` adds zeros around the border so the output feature map has the same spatial dimensions as the input. `padding='valid'` (default) does not pad, so the output is smaller than the input.

---

### 2. Certification Exam Tips
*   **CNN Architecture Pattern:** The standard TF exam CNN pattern is: `[Conv2D → MaxPooling2D] × N → Flatten → Dense(relu) → Dense(output)`. Typically 2–3 Conv/Pool blocks, then one or two Dense layers.
*   **Input Shape:** Always specify `input_shape=(height, width, channels)` in the first layer. For grayscale: `(28, 28, 1)`. For color: `(150, 150, 3)`. The exam commonly uses `(150, 150, 3)` for dog/cat image tasks.
*   **ImageDataGenerator Pattern:** `train_gen = ImageDataGenerator(rescale=1./255, rotation_range=40, horizontal_flip=True)` then `train_gen.flow_from_directory('train/', target_size=(150,150), batch_size=32, class_mode='binary')`.
*   **Study Resource:** The [TensorFlow image classification tutorial](https://www.tensorflow.org/tutorials/images/classification) at tensorflow.org walks through a complete CNN training pipeline with `ImageDataGenerator` and is directly representative of exam tasks. The [fast.ai Lesson 1](https://course.fast.ai/) also covers CNN image classification using a dataset very similar to the exam format.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow CNN tutorial](https://www.tensorflow.org/tutorials/images/cnn) and the [image classification tutorial](https://www.tensorflow.org/tutorials/images/classification) at tensorflow.org. These free official tutorials cover Conv2D, MaxPooling2D, ImageDataGenerator, and the full training pipeline tested on the exam.
*   **Required Video:** Watch the CNN lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers convolutional filters, pooling, and the Keras API for building image classifiers.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Build a CNN for image classification**: Define a Sequential model with two `Conv2D(32, (3,3), activation='relu')` + `MaxPooling2D(2,2)` blocks, followed by `Flatten()`, `Dense(64, activation='relu')`, and `Dense(1, activation='sigmoid')` for binary classification.
*   **Load images with ImageDataGenerator**: Create generators for train and validation directories with `rescale=1./255` and augmentation parameters, then use `flow_from_directory()` to create batches.
*   **Train with fit and evaluate**: Call `model.fit(train_generator, epochs=15, validation_data=val_generator)` and inspect training curves for overfitting.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and draw a CNN architecture diagram showing input → Conv → Pool → Flatten → Dense → output.
*   [ ] Work through the [TensorFlow CNN tutorial](https://www.tensorflow.org/tutorials/images/cnn) and [image classification tutorial](https://www.tensorflow.org/tutorials/images/classification).
*   [ ] Watch the CNN lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 06 lab: build and train a CNN on an image dataset.
*   [ ] Proceed to the Module 06 quiz.
