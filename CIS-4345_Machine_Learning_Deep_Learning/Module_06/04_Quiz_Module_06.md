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
