# Quiz: Module 07 — Convolutional Neural Networks

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

**Question 1**

A `Conv2D` layer is configured with 64 filters, a `3x3` kernel, `padding='valid'`, and `strides=1`. The input tensor has shape `(28, 28, 32)`. What is the output shape of this layer?

- A) `(28, 28, 64)`
- B) `(26, 26, 64)`
- C) `(26, 26, 32)`
- D) `(28, 28, 32)`

**Correct Answer:** B) With `padding='valid'` and a `3x3` kernel, each spatial dimension shrinks by `kernel_size - 1 = 2`. Output height and width are both `28 - 3 + 1 = 26`. The depth becomes the number of filters: 64. So the output shape is `(26, 26, 64)`.

**Distractor Analysis:**

- *Why A is incorrect:* `(28, 28, 64)` would be the output with `padding='same'`, which pads the input to preserve spatial dimensions. The question specifies `padding='valid'`, which does not add padding and therefore shrinks the spatial size.
- *Why B is correct:* Formula: `output = (input - kernel + 2*padding) / stride + 1 = (28 - 3 + 0) / 1 + 1 = 26`. Depth equals the number of filters (64), not the input depth (32). This is the most commonly tested Conv2D output shape calculation.
- *Why C is incorrect:* The depth of the output tensor is always equal to the number of filters in the Conv2D layer, not the input depth. A Conv2D(64, ...) always produces a depth of 64 regardless of input depth.
- *Why D is incorrect:* This would be the input shape passed through unchanged. Conv2D with `valid` padding changes both spatial dimensions and depth. No operation leaves all three dimensions unchanged simultaneously.

---

**Question 2**

How many trainable parameters does a `Conv2D(32, (3, 3))` layer have when its input has 3 channels (e.g., an RGB image)?

- A) `32`
- B) `288`
- C) `896`
- D) `9,632`

**Correct Answer:** C) Each of the 32 filters has shape `(3, 3, 3)` — kernel height times kernel width times input channels. Each filter also has one bias term. Total = `32 * (3 * 3 * 3) + 32 = 32 * 27 + 32 = 864 + 32 = 896`.

**Distractor Analysis:**

- *Why A is incorrect:* 32 is just the number of filters (also the number of bias terms). The weights inside each filter are not counted here. Counting only the biases ignores the vast majority of the parameters.
- *Why B is incorrect:* 288 = `32 * 9` counts the kernel weights but forgets to multiply by the input depth (3 channels). Each filter must cover all input channels, so the weight count per filter is `3*3*3 = 27`, not just `3*3 = 9`.
- *Why C is correct:* This is the standard parameter formula: `filters * (kernel_h * kernel_w * input_channels) + filters`. This calculation appears frequently on the TF Certificate exam and in `model.summary()` output. Always multiply by input depth.
- *Why D is incorrect:* 9,632 would result from incorrectly multiplying by spatial input dimensions. Parameter count in a convolutional layer does not depend on input image size — that is the key advantage of parameter sharing.

---

**Question 3**

What is the primary purpose of a `MaxPooling2D((2, 2))` layer in a CNN?

- A) It increases the number of feature maps by a factor of 4 to compensate for the loss of spatial resolution.
- B) It reduces the spatial dimensions of the feature maps by half in each dimension, lowering computational cost and providing a degree of translation invariance.
- C) It normalizes the feature map values to zero mean and unit variance, preventing vanishing gradients during backpropagation.
- D) It randomly drops 25% of the feature map values during training to act as a regularizer equivalent to Dropout.

**Correct Answer:** B) A `MaxPooling2D((2, 2))` layer with default stride of 2 replaces each non-overlapping `2x2` region with its maximum value, halving both the height and width. This reduces the number of computations in subsequent layers and provides mild translation invariance — a feature can shift by one pixel and the max value in the pooling region is likely preserved.

**Distractor Analysis:**

- *Why A is incorrect:* Max pooling reduces the spatial dimensions — it never increases the number of feature maps. The depth (channel count) is unchanged by pooling. If you want to increase depth, you add more filters in a Conv2D layer.
- *Why B is correct:* For a `(16, 16, 64)` input, `MaxPooling2D((2,2))` outputs `(8, 8, 64)`. This is applied after each conv block in standard CNN designs. Translation invariance is a key reason CNNs generalize well across slightly different image presentations.
- *Why C is incorrect:* Normalizing activations to zero mean and unit variance describes `BatchNormalization`, not max pooling. These are distinct layers with different purposes and are often used together in the same block.
- *Why D is incorrect:* Random dropout during training is the function of a `Dropout` layer, not max pooling. Max pooling is deterministic — it always takes the maximum, with no randomness and no regularization by random zeroing.

---

**Question 4**

A developer writes the following code. What error will occur when `model.summary()` is called, and how should it be fixed?

```python
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

- A) The model will raise a `ValueError` because `Conv2D` requires `padding='same'` when followed by `MaxPooling2D`.
- B) The model will raise a `ValueError` because the output of the second `MaxPooling2D` is a 3D tensor and cannot be fed directly into a `Dense` layer — a `Flatten` or `GlobalAveragePooling2D` layer is missing.
- C) The model will compile without error but will produce incorrect predictions because ReLU activation is incompatible with `MaxPooling2D`.
- D) The model will raise a `ValueError` because the second `Conv2D` layer does not specify `input_shape` explicitly.

**Correct Answer:** B) After the second `MaxPooling2D`, the tensor has shape `(5, 5, 64)` (a 3D tensor). A `Dense` layer expects a 1D input vector. Without a `Flatten()` or `GlobalAveragePooling2D()` layer between the last pooling layer and the first `Dense` layer, Keras raises a shape incompatibility error. Fix: insert `keras.layers.Flatten()` after the second `MaxPooling2D`.

**Distractor Analysis:**

- *Why A is incorrect:* `Conv2D` does not require `padding='same'` when followed by `MaxPooling2D`. `padding='valid'` (the default) is perfectly valid in this combination — the spatial dimensions simply shrink. There is no rule requiring `same` padding before pooling.
- *Why B is correct:* This is one of the most common CNN implementation errors on the TF Certificate exam. The fix is `keras.layers.Flatten()` before `Dense(128)`. Alternatively, replace both Dense layers with `GlobalAveragePooling2D() → Dense(10, softmax)` for a more modern approach.
- *Why C is incorrect:* ReLU activation and MaxPooling2D are fully compatible. ReLU outputs non-negative values; max pooling simply selects the largest non-negative value in each region. There is no incompatibility between these two operations.
- *Why D is incorrect:* In a `Sequential` model, only the first layer needs `input_shape`. Subsequent layers infer their input shape from the previous layer's output automatically. Not specifying `input_shape` on the second Conv2D is correct and expected behavior.

---

**Question 5**

Which of the following best explains why CNNs use **parameter sharing**, and what benefit it provides over a fully connected (Dense) layer for image inputs?

- A) Parameter sharing means each neuron in the Dense layer shares its bias term with all other neurons, reducing the total bias count from `N` to 1.
- B) Parameter sharing means the same filter weights are applied at every spatial position in the image, so the model learns one set of feature detectors that works everywhere — dramatically reducing the parameter count relative to a fully connected approach.
- C) Parameter sharing means the CNN splits the input image into non-overlapping patches and applies a separate Dense layer to each patch in parallel, sharing the computation graph but not the weights.
- D) Parameter sharing means the same batch of training images is reused across multiple epochs, allowing the model to see each example many times without increasing dataset size.

**Correct Answer:** B) In a Dense layer, every input pixel connects to every hidden neuron with a unique weight. For a `32x32x3` image and 128 hidden units, that is `3,072 * 128 = 393,216` parameters — just for the first layer. A Conv2D(32, 3x3) layer on the same input needs only `3*3*3*32 + 32 = 896` parameters, because one set of filter weights is reused at every spatial location. This is parameter sharing: the detector for a horizontal edge works the same in the top-left corner as in the bottom-right.

**Distractor Analysis:**

- *Why A is incorrect:* Bias sharing of this form is not a feature of CNNs or Dense layers. Each filter in a Conv2D layer has its own bias (one per filter, not one total). Bias is a small part of the parameter story; the major saving comes from the shared filter weights across spatial positions.
- *Why B is correct:* This is the foundational justification for CNNs. The inductive bias expressed is: visual features are translation-invariant — an edge detector should work everywhere in an image. This assumption is built into the architecture through shared weights, and it happens to be true for most natural images.
- *Why C is incorrect:* This describes a patch-based approach sometimes used in Vision Transformers (ViT), not standard CNNs. In a standard CNN, the filter slides continuously across the image with overlap (not divided into non-overlapping patches), and the weights are shared across all positions.
- *Why D is incorrect:* Training on the same data for multiple epochs is standard gradient descent training procedure and is entirely unrelated to parameter sharing. Reusing training batches across epochs applies to all neural network architectures equally.

---

**Question 6**

A developer trains a CNN on CIFAR-10 for 30 epochs. Training accuracy reaches 95% but validation accuracy plateaus at 65%. Which combination of changes is most likely to close this generalization gap?

- A) Increase the number of Conv2D filters in each block from 32/64/128 to 64/128/256 and train for 60 more epochs.
- B) Add `Dropout(0.25)` after each pooling layer and `Dropout(0.5)` before the final Dense layer, and consider adding data augmentation.
- C) Remove `BatchNormalization` from all blocks and switch the optimizer from Adam to SGD with momentum.
- D) Change `padding='same'` to `padding='valid'` in all Conv2D layers so the spatial dimensions shrink faster, reducing overfitting.

**Correct Answer:** B) A training accuracy of 95% vs validation accuracy of 65% is the hallmark of **overfitting** — the model has memorized the training set but fails to generalize. The standard remedies are: (1) Dropout to prevent co-adaptation of neurons; (2) data augmentation to artificially expand the training distribution; (3) reducing model capacity. Increasing filters (option A) would worsen overfitting.

**Distractor Analysis:**

- *Why A is incorrect:* Doubling filter counts increases model capacity and number of parameters. With a model already overfitting (train acc >> val acc), adding more parameters makes overfitting worse, not better. Training for more epochs would also worsen the gap.
- *Why B is correct:* `Dropout(0.25)` after pooling and `Dropout(0.5)` before the output head are the standard CNN regularization pattern. Data augmentation (Module 08) further reduces overfitting by presenting the model with transformed versions of training images, effectively multiplying the dataset size.
- *Why C is incorrect:* Removing `BatchNormalization` typically makes training slower and less stable — it is a mild regularizer, so removing it would increase (not decrease) overfitting. Switching to SGD might change convergence speed but does not address the fundamental overfitting problem.
- *Why D is incorrect:* Padding mode affects the spatial output size of conv layers but has no direct regularizing effect. Changing `same` to `valid` alters architecture dimensions and would require adjusting subsequent layer configurations, without meaningfully reducing overfitting.

---

**Question 7**

What does `GlobalAveragePooling2D()` do to a tensor of shape `(7, 7, 512)`, and why is it preferred over `Flatten()` in many modern CNN architectures?

- A) It pads the tensor to shape `(8, 8, 512)` and then averages adjacent cells, producing `(4, 4, 512)`.
- B) It averages each `7x7` feature map into a single value, producing a `(512,)` vector — dramatically fewer parameters than `Flatten()` followed by a Dense layer, and less prone to overfitting.
- C) It flattens the tensor to a `(7 * 7 * 512,)` = `(25,088,)` vector, providing the same result as `Flatten()` but with faster execution.
- D) It applies a `7x7` average pooling window to reduce `(7, 7, 512)` to `(1, 1, 512)` and then requires an explicit `Flatten()` call to remove the spatial dimensions.

**Correct Answer:** B) `GlobalAveragePooling2D` computes the spatial mean of each feature map independently. For a `(7, 7, 512)` input, each of the 512 feature maps (each `7x7`) is averaged to a single number, yielding a `(512,)` vector. Compared to `Flatten()` which produces `25,088` values, this is a `49x` reduction in parameters entering the classification head — significantly reducing overfitting risk.

**Distractor Analysis:**

- *Why A is incorrect:* GlobalAveragePooling does not pad the input, and it does not slide a window across the feature map. It computes one scalar per channel by averaging all spatial positions simultaneously. The output has no spatial dimensions at all.
- *Why B is correct:* For architectures like MobileNet and EfficientNet, `GlobalAveragePooling2D` followed by `Dense(num_classes, softmax)` replaces the traditional `Flatten → Dense(4096) → Dense(4096) → Dense(num_classes)` head. This removes millions of parameters while maintaining or improving accuracy through better regularization.
- *Why C is incorrect:* This describes `Flatten()`, not `GlobalAveragePooling2D`. These are distinct operations with different outputs. `Flatten` preserves all individual values; `GlobalAveragePooling2D` aggregates them.
- *Why D is incorrect:* `GlobalAveragePooling2D` produces a 2D output `(batch, channels)` in Keras — not a 4D tensor. No subsequent `Flatten()` call is needed. This is one of its advantages: the output is already compatible with a `Dense` layer.

---

**Question 8**

A developer builds the feature map visualization code shown below. What does `feature_model.predict(sample)` return, and what shape will the output have for a CIFAR-10 input?

```python
feature_model = keras.Model(
    inputs=model.input,
    outputs=model.layers[0].output
)
sample = x_test[0:1]
feature_maps = feature_model.predict(sample)
```

- A) The predicted class probabilities for the first test image — a vector of shape `(1, 10)`.
- B) The raw pixel values of the first test image reshaped into a column vector of shape `(1, 3072)`.
- C) The activations produced by the first `Conv2D` layer for the first test image — shape `(1, 32, 32, 32)` with `padding='same'` and 32 filters.
- D) The weights (filter values) of the first `Conv2D` layer — shape `(3, 3, 3, 32)`.

**Correct Answer:** C) `keras.Model(inputs=model.input, outputs=model.layers[0].output)` creates a sub-model whose output is the activation tensor from the first layer. For a CIFAR-10 input `(1, 32, 32, 3)` passing through `Conv2D(32, (3,3), padding='same')`, the output is `(1, 32, 32, 32)` — one sample, `32x32` spatial, 32 feature maps. Each of the 32 feature maps shows what one filter detected across the image.

**Distractor Analysis:**

- *Why A is incorrect:* Class probabilities `(1, 10)` would be the output of the final `Dense(10, softmax)` layer. This sub-model is connected to `model.layers[0].output`, which is the first Conv2D, not the last Dense layer.
- *Why B is incorrect:* The raw pixel values are the model's input, not the output of any layer. `model.input` is the input tensor; `model.layers[0].output` is the output of the first convolutional layer after applying filters and ReLU.
- *Why C is correct:* Building intermediate-output models with `keras.Model(inputs, outputs)` is the standard Keras approach to feature map visualization. The shape `(1, 32, 32, 32)` encodes: 1 sample, 32 height, 32 width (preserved by `same` padding), 32 filters.
- *Why D is incorrect:* `model.layers[0].output` is the activation tensor produced by passing data through the layer — not the layer's weights. To access filter weights, you would use `model.layers[0].get_weights()[0]`, which returns shape `(3, 3, 3, 32)`.

---

**Question 9**

Which Keras code correctly builds a CNN for binary image classification on `(150, 150, 3)` images with the output layer appropriate for binary cross-entropy loss?

- A) `keras.Sequential([Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)), MaxPooling2D(), Flatten(), Dense(1, activation='sigmoid')])`
- B) `keras.Sequential([Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)), MaxPooling2D(), Flatten(), Dense(2, activation='softmax')])`
- C) `keras.Sequential([Conv2D(32,(3,3),activation='relu',input_shape=(150,150)), MaxPooling2D(), Flatten(), Dense(1, activation='sigmoid')])`
- D) `keras.Sequential([Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)), MaxPooling2D(), Dense(1, activation='sigmoid')])`

**Correct Answer:** A) Binary classification requires `Dense(1, activation='sigmoid')` as the output layer, paired with `loss='binary_crossentropy'`. The `input_shape=(150, 150, 3)` correctly includes the channel dimension. `MaxPooling2D()` with no arguments uses the default `pool_size=(2,2)`. `Flatten()` correctly transitions from the convolutional feature maps to the Dense layer.

**Distractor Analysis:**

- *Why A is correct:* This is the canonical binary image classification pattern for the TF Certificate exam. Compile with `model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])`. The `sigmoid` activation outputs a probability between 0 and 1.
- *Why B is incorrect:* `Dense(2, softmax)` with `sparse_categorical_crossentropy` would be correct for two-class classification treated as multi-class. However, for binary classification the standard is `Dense(1, sigmoid)` with `binary_crossentropy`. Using softmax with 2 outputs and `binary_crossentropy` is a common mistake that produces incorrect loss gradients.
- *Why C is incorrect:* `input_shape=(150, 150)` is missing the channel dimension. A `Conv2D` layer requires a 3D input `(height, width, channels)`. Omitting the channel dimension raises a `ValueError` at build time.
- *Why D is incorrect:* The `Flatten()` layer is missing between the last `MaxPooling2D` and the `Dense(1)` layer. This will raise a shape incompatibility error because the pooling output is still 3D.

---

**Question 10**

Examine the `model.summary()` output below. What is the correct total parameter count for this model?

```
Layer (type)          Output Shape          Param #
Conv2D                (None, 26, 26, 16)    160
MaxPooling2D          (None, 13, 13, 16)    0
Flatten               (None, 2704)          0
Dense                 (None, 10)            27050
```

- A) `160`
- B) `27,050`
- C) `27,210`
- D) `27,370`

**Correct Answer:** C) Total parameters = sum of all non-zero parameter counts = `160 + 0 + 0 + 27,050 = 27,210`. The Conv2D(16, 3x3) on a grayscale `(28, 28, 1)` input has `16 * (3*3*1) + 16 = 144 + 16 = 160` parameters. After `MaxPooling2D`, shape is `(13, 13, 16)`. `Flatten` produces `13 * 13 * 16 = 2,704`. `Dense(10)` has `2,704 * 10 + 10 = 27,050`. Total: `160 + 27,050 = 27,210`.

**Distractor Analysis:**

- *Why A is incorrect:* 160 is only the parameter count for the Conv2D layer. The `model.summary()` total parameters sums all layers. Reading only the first non-zero row misses the Dense layer which dominates the parameter count.
- *Why B is incorrect:* 27,050 is only the Dense layer's parameter count. Summing all layers requires adding the Conv2D parameters (160) as well. This error reflects a misreading of the summary table.
- *Why C is correct:* Always sum every row's `Param #` column. Pooling and Flatten layers have zero parameters because they perform fixed mathematical operations with no learnable weights. Only Conv2D and Dense have trainable parameters in this model.
- *Why D is incorrect:* 27,370 does not correspond to any correct combination of the values shown. It may result from incorrectly double-counting bias terms or misreading the Flatten output size. Always verify the Flatten output by computing `H * W * C` from the pooling layer's output shape.

---

### Question 11 (5 points)

A `Conv2D(64, (5, 5), padding='same', strides=2)` layer receives an input of shape `(64, 64, 16)`. What is the output shape?

- A) `(64, 64, 64)`
- B) `(32, 32, 64)`
- C) `(30, 30, 64)`
- D) `(60, 60, 64)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* With `padding='same'` and `strides=2`, each spatial dimension is halved: `ceil(64/2) = 32`. The depth equals the number of filters: 64. Output shape is `(32, 32, 64)`. The `same` padding ensures the stride alone controls spatial reduction.
  - *Why A is incorrect:* `(64, 64, 64)` would result from `padding='same'` with `strides=1`. When `strides=2`, each dimension is divided by the stride value, producing 32, not 64.
  - *Why C is incorrect:* `(30, 30, 64)` applies the `valid` padding formula `(64 - 5 + 1) / 2 = 30`. The question specifies `padding='same'`, which pads the input so that the stride alone determines the output size.
  - *Why D is incorrect:* `(60, 60, 64)` would result from `(64 - 5 + 1) = 60` with `strides=1` and `valid` padding. Neither the stride nor the padding matches this scenario.

---

### Question 12 (5 points)

Which of the following statements about `BatchNormalization` in a CNN is correct?

- A) `BatchNormalization` is placed after the `Flatten` layer to normalize the flattened feature vector before the Dense classifier head.
- B) `BatchNormalization` normalizes activations across the batch dimension, reducing internal covariate shift and allowing higher learning rates.
- C) `BatchNormalization` replaces the need for `Dropout` entirely and should not be used alongside it.
- D) `BatchNormalization` is only applicable to the first convolutional layer because later layers already receive normalized inputs from the previous `MaxPooling`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Batch Normalization standardizes the output of a layer (or the input to an activation function) across the current mini-batch, keeping activations near zero mean and unit variance. This reduces internal covariate shift — the shifting of layer input distributions during training — allowing the use of higher learning rates and making the network less sensitive to weight initialization.
  - *Why A is incorrect:* While BatchNorm can be placed after Flatten, the most common and beneficial use in CNNs is after each Conv2D layer (before the activation), not solely at the Flatten transition. Placing it only after Flatten would leave all convolutional activations unnormalized.
  - *Why C is incorrect:* BatchNorm and Dropout serve complementary roles — BatchNorm addresses internal covariate shift while Dropout prevents co-adaptation of neurons. They are frequently used together. BatchNorm provides mild regularization but does not fully replace Dropout.
  - *Why D is incorrect:* MaxPooling performs a fixed spatial downsampling operation and does not normalize activation magnitudes. BatchNorm is beneficial at every convolutional block, not just the first layer.

---

### Question 13 (5 points)

A developer uses `strides=2` in a `Conv2D` layer instead of adding a `MaxPooling2D` layer after it. What is the key difference between these two spatial downsampling strategies?

- A) Strided convolution reduces spatial dimensions but loses all channel information, while MaxPooling preserves all channels.
- B) Strided convolution learns how to downsample (trainable), while MaxPooling always selects the maximum value (fixed, no learnable parameters).
- C) MaxPooling introduces more parameters than strided convolution because it learns a pooling kernel.
- D) Strided convolution can only be applied to the first layer, while MaxPooling can be placed anywhere in the network.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A strided convolution applies a learnable filter while simultaneously reducing spatial dimensions — the downsampling is learned from data. MaxPooling is a fixed, parameter-free operation that always selects the maximum activation value in each pooling window. Modern architectures (e.g., ResNet) often prefer strided convolutions because the network can learn an optimal downsampling strategy.
  - *Why A is incorrect:* Both strided convolution and MaxPooling preserve all channels (feature map depth). Neither operation reduces the channel dimension — only the spatial height and width are affected by downsampling.
  - *Why C is incorrect:* MaxPooling has zero learnable parameters. It is a fixed mathematical operation. Strided convolution has more parameters than MaxPooling because the convolution itself has learnable weights.
  - *Why D is incorrect:* Both strided convolution and MaxPooling can be applied at any layer in the network. There is no restriction limiting strided convolution to the first layer.

---

### Question 14 (5 points)

What is the receptive field of a neuron in the second convolutional layer of a network where both layers use `3x3` kernels with `strides=1` and `padding='valid'`?

- A) `3x3` — the receptive field is always determined only by the current layer's kernel size.
- B) `5x5` — two stacked `3x3` kernels cover a `5x5` region in the original input.
- C) `9x9` — two `3x3` kernels multiply: `3 * 3 = 9`.
- D) `6x6` — two `3x3` kernels add: `3 + 3 = 6`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Each neuron in the second convolutional layer looks at a `3x3` patch of the first layer's feature map. Each cell in that `3x3` patch of the first layer was computed from a `3x3` patch of the original input. The union of those patches in the original input forms a `5x5` region: `(3 - 1) + (3 - 1) + 1 = 5`. This is why deep stacked `3x3` convolutions are preferred — they build large receptive fields cheaply.
  - *Why A is incorrect:* The receptive field grows with network depth. A neuron in a deeper layer "sees" a larger region of the original input because its activations are influenced by a larger neighborhood through the chain of preceding layers.
  - *Why C is incorrect:* Receptive field does not multiply across layers. It grows additively: adding one `3x3` layer to an existing receptive field of `3x3` produces `3 + 2 = 5`, not `3 * 3 = 9`.
  - *Why D is incorrect:* The formula `3 + 3 = 6` overcounts by not accounting for overlap. The correct formula for stacked `3x3` layers is `1 + N * (kernel_size - 1)` where N is the number of layers: `1 + 2 * 2 = 5`.

---

### Question 15 (5 points)

A developer trains a CNN for 10-class image classification and calls `model.predict(x_test[0:1])`. The output is an array like `[[0.01, 0.02, 0.85, 0.03, ...]]`. What does this output represent and how would you determine the predicted class?

- A) The output is the raw logit scores before softmax; the predicted class is the index of the logit closest to zero.
- B) The output is the class probability distribution from the softmax layer; the predicted class index is `np.argmax(output[0])`.
- C) The output is the pixel reconstruction of the input image compressed by the CNN; no class can be derived from it.
- D) The output is a one-hot encoded label vector; the predicted class is the position of the `1` value.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A `Dense(10, activation='softmax')` output layer produces a probability distribution over 10 classes — 10 non-negative values that sum to 1.0. The element with the highest probability is the predicted class. `np.argmax(model.predict(x)[0])` is the standard pattern for extracting the integer class prediction from a softmax output.
  - *Why A is incorrect:* If the model uses softmax activation on the output layer (as specified), the output is already a probability distribution, not raw logits. Raw logits are produced only if the output layer has no activation (e.g., `Dense(10)` with no `activation` argument) or uses `activation='linear'`.
  - *Why C is incorrect:* A CNN with a Dense softmax head is a discriminative classifier, not a reconstruction model. Only autoencoders produce image reconstructions. The CNN output vector contains class probabilities, not pixel values.
  - *Why D is incorrect:* A one-hot vector contains exactly one `1.0` and all other values as `0.0`. A softmax probability distribution contains continuous values between 0 and 1. The model output shown (`[0.01, 0.02, 0.85, ...]`) is a probability distribution, not a binary one-hot encoding.

---

### Question 16 (5 points)

Which layer in Keras adds **L2 regularization** to a `Conv2D` layer's kernel weights?

- A) `keras.layers.Conv2D(32, (3,3), kernel_regularizer=keras.regularizers.l2(0.01))`
- B) `keras.layers.Conv2D(32, (3,3), dropout_rate=0.01)`
- C) `keras.layers.Conv2D(32, (3,3), weight_decay=0.01)`
- D) `keras.layers.L2Regularizer(lambda=0.01)(Conv2D(32, (3,3)))`

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* The `kernel_regularizer` argument in Keras layer constructors accepts a regularizer object. `keras.regularizers.l2(0.01)` creates an L2 regularizer with coefficient 0.01. During training, the L2 penalty `0.01 * sum(weights^2)` is added to the loss, discouraging large weights and reducing overfitting.
  - *Why B is incorrect:* `Conv2D` has no `dropout_rate` argument. Dropout in CNNs is applied via a separate `keras.layers.Dropout(rate)` layer placed after the convolutional block, not as a parameter of Conv2D.
  - *Why C is incorrect:* `weight_decay` is not a parameter of Keras's `Conv2D` layer. In some frameworks (e.g., PyTorch optimizers), weight decay is specified in the optimizer. In Keras, regularization is specified via `kernel_regularizer`.
  - *Why D is incorrect:* `keras.layers.L2Regularizer` is not a valid Keras layer class. Regularizers in Keras are not applied as wrapper layers — they are passed as arguments to the layer being regularized via `kernel_regularizer`, `bias_regularizer`, or `activity_regularizer`.

---

### Question 17 (5 points)

A developer wants to inspect the activation of the third layer (index 2) in a trained Keras model. Which code correctly creates the intermediate activation model?

- A) `activation_model = keras.Model(inputs=model.input, outputs=model.layers[2].output)`
- B) `activation_model = model.get_layer(index=2).predict(x_test)`
- C) `activation_model = keras.Model(inputs=model.layers[2].input, outputs=model.output)`
- D) `activation_model = keras.layers.Lambda(lambda x: model.layers[2](x))`

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* `keras.Model(inputs=model.input, outputs=model.layers[2].output)` creates a sub-model that shares all weights with the original model but terminates its output at layer index 2. When `activation_model.predict(x)` is called, it returns the activations at that specific layer. This is the standard Keras pattern for feature visualization.
  - *Why B is incorrect:* `model.get_layer(index=2)` returns a layer object, which is not callable on data directly as a predictor. A layer object does not have a `predict()` method — only `Model` instances have `predict()`. This would raise an `AttributeError`.
  - *Why C is incorrect:* This creates a model from layer 2's input to the final output, which is a partial network starting mid-way. It is the reverse of what is needed for intermediate activation extraction and would require manually providing the correctly shaped intermediate tensor as input.
  - *Why D is incorrect:* While `keras.layers.Lambda` can wrap arbitrary operations, this pattern does not create a proper Keras model and would not work correctly for prediction on batched data. The standard and correct approach is the `keras.Model(inputs, outputs)` functional API.

---

### Question 18 (5 points)

When training a CNN with `model.fit(..., validation_split=0.1)`, which samples are used for validation?

- A) A randomly selected 10% of the training data, shuffled and resampled each epoch.
- B) The last 10% of the training array (by index), held out before training begins.
- C) The first 10% of the training array (by index), held out before training begins.
- D) A stratified 10% sample selected to maintain class balance across all classes.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Keras `validation_split` takes the **last** `fraction * N` samples from the provided training array before any shuffling. For 50,000 CIFAR-10 training samples, `validation_split=0.1` reserves samples at indices `45,000–49,999` for validation. This is a deterministic operation — the same samples are always held out.
  - *Why A is incorrect:* The validation split is not re-randomized each epoch. The same held-out subset is used for validation throughout all training epochs. This is important for comparing validation metrics across epochs consistently.
  - *Why C is incorrect:* Keras takes the last fraction of data, not the first. The first samples are used for training. This matters when data is ordered (e.g., temporally) — you should shuffle the data yourself before passing it to `model.fit()` if order is a concern.
  - *Why D is incorrect:* `validation_split` does not perform stratification. For stratified splitting, use `sklearn.model_selection.train_test_split(stratify=y)` before calling `model.fit()`, and then pass `validation_data=(x_val, y_val)` explicitly.

---

### Question 19 (5 points)

What is the primary advantage of using `padding='same'` throughout a CNN architecture compared to `padding='valid'`?

- A) `padding='same'` reduces the parameter count of each Conv2D layer by avoiding border pixel computations.
- B) `padding='same'` preserves spatial dimensions through conv layers, making it easy to predict output shapes and allowing flexible depth without manual size tracking.
- C) `padding='same'` improves test accuracy because it forces the model to learn from zero-padded border regions, which act as a regularizer.
- D) `padding='same'` is required when using `BatchNormalization` to ensure the batch statistics are computed over identical-sized feature maps.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* With `padding='same'` and `strides=1`, every Conv2D layer outputs the same spatial dimensions as its input. Only MaxPooling or strided convolutions reduce spatial size. This predictability simplifies architecture design: you can stack as many conv layers as needed without computing shrinking dimensions, and the only size changes come from deliberate downsampling layers.
  - *Why A is incorrect:* `padding='same'` does not reduce parameter count — it adds zero-padding around the input, which is a computational (not parametric) operation. The parameter count of a Conv2D layer is determined entirely by `filters * kernel_h * kernel_w * input_channels + filters`, regardless of padding mode.
  - *Why C is incorrect:* Zero padding allows the filter to process border pixels but does not introduce meaningful regularization. The accuracy difference between `same` and `valid` comes from architectural choices (depth, capacity) rather than a regularizing effect of padding.
  - *Why D is incorrect:* BatchNormalization works with feature maps of any spatial size and has no requirement for `padding='same'`. BN normalizes over the batch, height, and width dimensions simultaneously, so it operates correctly regardless of whether padding changes feature map dimensions.

---

### Question 20 (5 points)

A CNN trained on 224x224 images achieves 90% test accuracy. The developer wants to apply this model to 384x384 images at inference time without retraining. Which architectural change made during training would enable this?

- A) Replace the `Flatten()` layer with `GlobalAveragePooling2D()` — this makes the model fully convolutional and input-size agnostic.
- B) Replace `MaxPooling2D` with `AveragePooling2D` — average pooling accepts variable-size inputs while max pooling requires fixed sizes.
- C) Add a `Reshape` layer at the end that resizes any input feature map to a fixed `(1, 1, 512)` tensor before the Dense head.
- D) Set `padding='valid'` on all Conv2D layers — valid padding allows the model to process larger images by producing proportionally larger feature maps.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* `Flatten()` converts a `(H, W, C)` tensor into a 1D vector of length `H * W * C`. If `H` or `W` changes (larger input image), the flattened vector length changes, making the subsequent Dense layer incompatible. `GlobalAveragePooling2D()` averages each feature map to a single value regardless of spatial dimensions, always producing a `(C,)` vector. This makes the architecture fully compatible with any input spatial size.
  - *Why B is incorrect:* Both `MaxPooling2D` and `AveragePooling2D` accept variable spatial dimensions — neither requires a fixed input size. The input-size constraint in standard CNNs comes from the `Flatten` layer, not from pooling type.
  - *Why C is incorrect:* `keras.layers.Reshape` does not resize feature maps — it only rearranges the elements of a tensor without changing its total size. If the feature map has more elements than `1*1*512`, a `Reshape` would raise an error or produce incorrect results.
  - *Why D is incorrect:* The padding mode affects how much spatial shrinkage occurs per conv layer, but the fundamental incompatibility with variable input sizes comes from `Flatten`. With `valid` padding on a larger image, the flattened vector would still have a different length, breaking the Dense head.
