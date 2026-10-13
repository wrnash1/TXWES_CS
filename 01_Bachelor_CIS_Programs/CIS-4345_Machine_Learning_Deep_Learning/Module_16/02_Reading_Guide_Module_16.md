# Reading Guide: Module 16 - Final Exam Prep and TensorFlow Developer Certificate

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4345 &BULL; MACHINE LEARNING & DEEP LEARNING SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction

Welcome to **Module 16 - Final Exam Prep and TensorFlow Developer Certificate**! This final module consolidates everything you have learned across the course and prepares you for the **TensorFlow Developer Certificate** exam. The certification tests your ability to build, train, and evaluate deep learning models using TensorFlow 2.x and the Keras API — demonstrating professional-level proficiency in the four core task categories the exam emphasizes.

This module reviews the complete exam structure, summarizes the highest-yield patterns from every prior module, and provides a targeted study strategy for the five-hour PyCharm-based exam environment.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **TensorFlow Developer Certificate exam format**: A five-hour, open-book, open-internet examination administered in a PyCharm IDE environment using the TF exam plugin. Candidates download problem sets, build and train models that meet accuracy/loss thresholds, and submit trained `.h5` model files. The exam covers four task categories: (1) basic TF/Keras model building, (2) image classification with CNNs, (3) NLP with text classification, and (4) time series forecasting.

* **Build-Compile-Fit pattern**: The fundamental Keras workflow tested throughout the exam. Build: define the model architecture with `tf.keras.Sequential([...])` or the Functional API. Compile: specify loss, optimizer, and metrics with `model.compile(loss=..., optimizer=..., metrics=[...])`. Fit: train with `model.fit(train_data, epochs=..., validation_data=..., callbacks=[...])`. Every exam problem follows this three-step pattern.

* **Callbacks**: Keras objects that run at specific points in the training loop, used to implement early stopping, learning rate scheduling, and model checkpointing. `EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)` stops training when validation loss stops improving and restores the best weights. `ModelCheckpoint` saves the best model to disk. Callbacks are passed as a list to `model.fit()`.

* **Transfer learning pattern**: The two-stage pattern used for image classification tasks. Stage 1: load a pre-trained base model with `include_top=False`, freeze all base layers (`base_model.trainable = False`), add a classification head, and train only the head. Stage 2 (fine-tuning): unfreeze the top layers of the base model, recompile with a very low learning rate (e.g., `1e-5`), and continue training. Recompiling is mandatory after changing `trainable` attributes.

* **NLP pipeline**: The standard sequence for text classification tasks. Tokenize: `Tokenizer(num_words=vocab_size, oov_token='<OOV>')` → `fit_on_texts(train_texts)` → `texts_to_sequences()`. Pad: `pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')`. Model: `Embedding(vocab_size+1, embedding_dim, input_length=max_length)` → LSTM or Conv1D → Dense. The `vocab_size+1` off-by-one is a common exam trap.

* **Time series windowed dataset**: The pipeline for converting a raw 1D time series to supervised learning format. `tf.data.Dataset.from_tensor_slices(series)` → `.window(size+1, shift=1, drop_remainder=True)` → `.flat_map(lambda w: w.batch(size+1))` → `.map(lambda w: (w[:-1], w[-1]))` → `.shuffle()` → `.batch(batch_size)` → `.prefetch(1)`. Input shape for LSTM: `(window_size, 1)` — requires a Lambda or reshape layer to add the channel dimension.

---

### 2. Certification Exam Tips

* **Know all four task categories cold:** The exam always includes: (1) a basic model (Dense layers, regression or classification); (2) an image classification CNN (possibly with transfer learning); (3) an NLP text classifier (Embedding + LSTM or Conv1D); (4) a time series forecaster (LSTM or Conv1D with windowed dataset). Practice each category until the build-compile-fit code is automatic.
* **Accuracy thresholds:** Each exam problem has a minimum accuracy/loss threshold that the submitted `.h5` model must meet for credit. Build in `EarlyStopping(restore_best_weights=True)` and `ModelCheckpoint` on every problem to ensure you submit the best-performing checkpoint, not just the final epoch.
* **Common exam traps:** (1) NLP: `input_dim=vocab_size+1` in the Embedding layer (not `vocab_size`); (2) LSTM time series: add `tf.expand_dims` or a Lambda layer to get 3D input shape `(batch, window, 1)`; (3) Transfer learning: always call `model.compile()` again after changing `base_model.trainable`; (4) ImageDataGenerator: `rescale=1./255` must be on both training and validation generators.
* **Study Resource:** The [TensorFlow Developer Certificate program page](https://www.tensorflow.org/certificate) at tensorflow.org describes the full exam curriculum, candidate handbook, and preparation resources. The [TensorFlow Developer Certificate course on Coursera](https://www.coursera.org/professional-certificates/tensorflow-in-practice) by Laurence Moroney (free to audit) covers all four exam task categories in dedicated modules and is the most exam-representative free resource available.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Review the [TensorFlow Developer Certificate candidate handbook](https://www.tensorflow.org/certificate) at tensorflow.org. This covers the exact exam format, task categories, scoring criteria, and allowed resources. Also review the [Keras API documentation](https://keras.io/api/) for the specific layers and methods used across all four task categories.
* **Required Video:** Watch the final review lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers the full TF Developer Certificate exam structure, common pitfalls, and a walkthrough of each task category using the build-compile-fit pattern.

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Four-problem mock exam**: Build, compile, train, and save models for all four exam task categories — (1) basic Dense classifier, (2) CNN image classifier with data augmentation, (3) NLP text classifier with Embedding+LSTM, and (4) LSTM time series forecaster with windowed dataset. Save each as `.h5` using `model.save()`.
* **Accuracy threshold testing**: For each model, evaluate on the provided validation set and verify that the model meets a target threshold (e.g., >85% accuracy for classification, MAE below naive baseline for time series). Add `EarlyStopping(restore_best_weights=True)` to each training call to ensure the best epoch is saved.
* **Exam environment simulation**: Open each problem in PyCharm, use only tensorflow.org and keras.io documentation, and time yourself — practice completing all four problems within the five-hour window.

---

### 3. Study Checklist

* [ ] Review the glossary terms and write out the build-compile-fit pattern for each of the four exam task categories from memory.
* [ ] Read the [TensorFlow Developer Certificate candidate handbook](https://www.tensorflow.org/certificate) and review the exam scoring criteria.
* [ ] Watch the final review lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
* [ ] Complete the Module 16 mock exam lab: four task categories, all models saved as `.h5`, all thresholds verified.
* [ ] Proceed to the Module 16 final exam quiz.

---

## 9. Supplemental Resources

**1. [TensorFlow Developer Certificate — Official Candidate Handbook](https://www.tensorflow.org/certificate)**
The authoritative source for the exam format, task category breakdown, scoring criteria, allowed resources, and the PyCharm plugin setup process. Required reading before attempting the mock exam lab. Covers the exact four task categories tested, the minimum accuracy/loss thresholds per problem type, and how to submit `.h5` model files through the exam plugin.

**2. [DeepLearning.AI TensorFlow Developer Professional Certificate (Coursera)](https://www.coursera.org/professional-certificates/tensorflow-in-practice)**
A four-course specialization by Laurence Moroney (Google Brain) that directly maps to the four TF Developer Certificate exam categories: basic Keras, CNNs with ImageDataGenerator, NLP with Tokenizer and LSTM, and time series forecasting with windowed datasets. Free to audit. Each course includes coding exercises in Colab that mirror the exam's build-compile-fit format. The most exam-representative free preparation resource available.

**3. [Keras API Documentation — Layers, Losses, Callbacks](https://keras.io/api/)**
The primary open-internet reference permitted during the exam. Key sections to bookmark: `tf.keras.layers` (Embedding, LSTM, Conv2D, Dense), `tf.keras.losses` (BinaryCrossentropy, SparseCategoricalCrossentropy), `tf.keras.callbacks` (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau), and `tf.keras.applications` (MobileNetV2, VGG16, ResNet50). Practicing navigation of this documentation under time pressure is as important as knowing the API itself.
