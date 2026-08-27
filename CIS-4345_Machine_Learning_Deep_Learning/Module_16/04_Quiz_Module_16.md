# Quiz: Module 16 - Final Exam Prep and TensorFlow Developer Certificate

## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Question 1 (10 points)

The TensorFlow Developer Certificate exam is administered in which environment, and what does a candidate submit to receive credit for each problem?

* A) A browser-based IDE with automatic grading — the candidate writes code in a web editor and the system evaluates it live against hidden test cases without any file submission.
* B) A PyCharm IDE environment with the TF exam plugin — the candidate builds and trains a model that meets an accuracy/loss threshold, then submits the saved `.h5` model file for automated evaluation.
* C) A Jupyter Notebook submitted to a Kaggle competition — the exam evaluates the candidate's notebook output cells and the final confusion matrix printed at the end of execution.
* D) A command-line terminal where the candidate types TensorFlow commands from memory — the exam is closed-book with no internet access and graded on command accuracy by a human proctor.
* **Correct Answer:** B) The TF Developer Certificate uses the PyCharm TF exam plugin. Candidates download problem sets, write and train models locally in PyCharm, verify that their model meets the required threshold, and upload the saved `.h5` file through the plugin. The exam is five hours, open-book, and open-internet — candidates may use tensorflow.org and keras.io documentation.
* **Distractor Analysis:**
  * *Why A is incorrect:* The exam is not browser-based. It runs in PyCharm on the candidate's own machine. There is no live automatic grading of code — the submitted artifact is the trained `.h5` model file, which is evaluated against a hidden test set.
  * *Why B is correct:* Key exam logistics: PyCharm + TF exam plugin; five-hour window; four task categories; model saved with `model.save('model.h5')`; each problem has a minimum accuracy/loss threshold. Open-book and open-internet (tensorflow.org, keras.io) are explicitly allowed.
  * *Why C is incorrect:* The TF Developer Certificate has no connection to Kaggle or Jupyter Notebooks. Notebook-based coding assessments are used in other certifications (e.g., Databricks) but not the TF exam.
  * *Why D is incorrect:* The exam is explicitly open-book and open-internet. Closed-book, command-line-based, human-proctored typing tests describe a completely different kind of assessment.

---

### Question 2 (10 points)

Which of the following is the most accurate definition of the **build-compile-fit pattern** in TensorFlow and Keras?

* A) A three-phase deployment pipeline where a trained model is built into a Docker container, compiled to a TFLite flatbuffer, and fit into a mobile app distribution package for the App Store or Google Play.
* B) The fundamental Keras model training workflow: define the architecture with `tf.keras.Sequential` or the Functional API (build), configure the loss function, optimizer, and metrics with `model.compile()` (compile), then train on data with `model.fit()` (fit) — the three-step pattern used for every model on the TF Developer Certificate exam.
* C) A machine learning cross-validation technique that builds k different train/test splits, compiles performance metrics across all splits, and fits a final model on the full dataset after hyperparameter selection.
* D) A TensorFlow graph execution mode where the computational graph is built statically at import time, compiled to XLA for hardware acceleration, and fit to GPU memory before any data is processed.
* **Correct Answer:** B) Every TF Developer Certificate exam problem follows this exact three-step pattern. Build: `model = tf.keras.Sequential([layers...])`. Compile: `model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])`. Fit: `model.fit(train_data, epochs=N, validation_data=val_data, callbacks=[...])`. Internalizing this pattern for all four task categories is the single most important exam preparation task.
* **Distractor Analysis:**
  * *Why A is incorrect:* This describes a model deployment pipeline (containerization, TFLite conversion, app packaging) — an entirely different workflow from the Keras training API. The build-compile-fit pattern refers specifically to training, not deployment.
  * *Why B is correct:* The three methods map directly to the exam workflow: `Sequential` or Functional API for architecture → `compile()` for training configuration → `fit()` for training execution. All four exam task categories use this pattern with task-specific layers and loss functions.
  * *Why C is incorrect:* This describes k-fold cross-validation, a model evaluation strategy. Cross-validation involves no `compile()` or `fit()` calls in the Keras sense — it is a data splitting and evaluation methodology.
  * *Why D is incorrect:* XLA compilation and graph execution are TensorFlow infrastructure concerns that happen automatically in TF2 eager mode. The build-compile-fit pattern is a user-facing Keras API workflow, not a description of TF's internal execution engine.

---

### Question 3 (10 points)

A candidate is working on the NLP text classification task on the TF Developer Certificate exam. They define a tokenizer with `vocab_size = 10000` and build a model starting with an Embedding layer. Which line correctly defines the Embedding layer?

* A) `tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length)`
* B) `tf.keras.layers.Embedding(vocab_size + 1, embedding_dim, input_length=max_length)`
* C) `tf.keras.layers.Embedding(embedding_dim, vocab_size, input_length=max_length)`
* D) `tf.keras.layers.Embedding(max_length, embedding_dim, input_dim=vocab_size)`
* **Correct Answer:** B) The `input_dim` (first argument) of the Embedding layer must be `vocab_size + 1`, not `vocab_size`. The `Tokenizer` assigns indices starting at 1 (index 0 is reserved for padding). If `input_dim=vocab_size`, index `vocab_size` (the highest valid token index) falls outside the embedding table and raises an index-out-of-bounds error at runtime.
* **Distractor Analysis:**
  * *Why A is incorrect:* Using `vocab_size` (without +1) is the most common NLP exam mistake. With `num_words=10000`, the tokenizer can assign tokens indices 1 through 10000. The embedding table needs 10001 rows (indices 0–10000) — so `input_dim` must be 10001.
  * *Why B is correct:* `Embedding(vocab_size + 1, embedding_dim, input_length=max_length)` is the correct call. The argument order is `(input_dim, output_dim, input_length)`. `input_dim` = vocabulary size + 1 for the 0 padding index. `output_dim` = embedding vector dimension (e.g., 16, 32, 64). `input_length` = the padded sequence length.
  * *Why C is incorrect:* The argument order is reversed — `(input_dim, output_dim)`, not `(output_dim, input_dim)`. Swapping these would create a tiny embedding table with 16 rows (if `embedding_dim=16`) and vectors of length 10000, producing a model that does not learn meaningful word representations.
  * *Why D is incorrect:* `Embedding` does not have an `input_dim` keyword argument — `input_dim` is the first positional argument. Additionally, placing `max_length` as the first argument would set the vocabulary size to `max_length`, which is incorrect semantically.

---

### Question 4 (10 points)

During the image classification task on the exam, a candidate unfreezes the top 20 layers of a MobileNetV2 base model for fine-tuning. After setting `layer.trainable = True` for those layers, what must happen before calling `model.fit()` again?

* A) The model must be saved and reloaded with `tf.keras.models.load_model()` to force TensorFlow to rebuild the computational graph with the new trainable configuration.
* B) The model must be recompiled with `model.compile()` using a lower learning rate before resuming training — Keras requires recompilation to register changes to layer `trainable` attributes.
* C) The frozen layers must be re-initialized to random weights because unfreezing restores the original pre-training initialization, discarding the pre-trained ImageNet weights.
* D) No additional steps are needed — TensorFlow automatically detects changes to `trainable` attributes and adjusts gradient computation on the next `model.fit()` call without recompilation.
* **Correct Answer:** B) In Keras, `trainable` attribute changes only take effect after `model.compile()` is called. Without recompilation, the optimizer's gradient computation plan does not update and the newly unfrozen layers will not actually receive gradient updates during training. The learning rate for fine-tuning should be much lower than the initial training rate (e.g., `1e-5` vs. `1e-3`) to avoid destroying the pre-trained weights.
* **Distractor Analysis:**
  * *Why A is incorrect:* Saving and reloading is not required and would be time-consuming. Recompilation with `model.compile()` is the correct and sufficient step to register `trainable` changes — no save/reload cycle is needed.
  * *Why B is correct:* The fine-tuning pattern: `for layer in base_model.layers[-20:]: layer.trainable = True` → `model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), loss=..., metrics=['accuracy'])` → `model.fit(...)`. The recompile step is mandatory; forgetting it is the most common transfer learning mistake.
  * *Why C is incorrect:* Unfreezing layers does not reset their weights. The pre-trained weights are preserved — unfreezing only allows those weights to be updated by gradient descent during subsequent training. This is the whole point of fine-tuning.
  * *Why D is incorrect:* TensorFlow does not automatically detect `trainable` changes between `fit()` calls. The computational graph for gradient computation is fixed at compile time. Changing `trainable` without recompiling results in the unfrozen layers still receiving no gradients.

---

### Question 5 (10 points)

A candidate submits their time series LSTM model for the forecasting task but receives a score below the threshold. The model's validation MAE is only slightly better than the naive forecast. Which combination of changes is most likely to improve performance enough to meet the threshold?

* A) Switch from MAE loss to categorical cross-entropy loss and add a softmax output layer — the forecasting task requires classification-style output, not regression.
* B) Reduce the window size to 1 (single-step input) and remove the LSTM layers, replacing them with a single Dense(1) layer — simpler models always generalize better on time series.
* C) Increase the window size to capture more temporal context, add a learning rate schedule or `ReduceLROnPlateau` callback, and add a `Lambda` layer as the first layer to expand input dims to `(window_size, 1)` for the LSTM — then retrain with more epochs and `EarlyStopping(restore_best_weights=True)`.
* D) The model cannot be improved further — a validation MAE only slightly better than naive indicates the time series has no autocorrelation and no neural network can forecast it accurately.
* **Correct Answer:** C) Marginal improvement over naive most commonly indicates one of three fixable problems: the window is too short (model lacks temporal context), the learning rate is not optimal (model stopped improving prematurely), or the LSTM input shape is wrong (flat `(batch, W)` instead of 3D `(batch, W, 1)`). The Lambda expand_dims fix, a longer window, a learning rate schedule, and `EarlyStopping(restore_best_weights=True)` together address all three issues.
* **Distractor Analysis:**
  * *Why A is incorrect:* Time series forecasting is a regression problem — the output is a continuous numerical value (the next time step's value). Categorical cross-entropy and softmax are for classification problems with discrete class labels. Changing to these would break the model entirely.
  * *Why B is incorrect:* Reducing the window to 1 eliminates all temporal context — the model can only see the most recent value, which is equivalent to the naive forecast. Removing LSTM layers destroys the model's ability to learn temporal patterns. Simpler is not always better; the problem requires learning sequences.
  * *Why C is correct:* The LSTM input shape bug (`(batch, W)` instead of `(batch, W, 1)`) is the single most common time series exam error. A Lambda layer `tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1))` as the first layer fixes it. Increasing window size and adding `ReduceLROnPlateau` or `EarlyStopping(restore_best_weights=True)` are the standard performance improvement techniques.
  * *Why D is incorrect:* Slightly beating naive does not imply no autocorrelation — it more likely indicates a correctable implementation issue (wrong input shape, too-small window, premature convergence). Real-world time series almost always have learnable structure. The appropriate response is to diagnose and fix the implementation, not conclude the problem is unsolvable.

---

### Question 6 (5 points)

On the TF Developer Certificate exam, a candidate is working on a CNN image classifier and adds `ImageDataGenerator` for data augmentation. They apply `rescale=1./255` to the training generator but forget to apply it to the validation generator. What is the most likely consequence?

* A) The model trains normally; the validator generator does not affect weight updates so rescaling there is optional
* B) The validation accuracy reported during training will be unreliably low because validation images have pixel values 0–255 while the model was trained to expect 0–1 inputs
* C) Training will crash immediately with a shape mismatch error because TensorFlow detects inconsistent preprocessing between generators
* D) The model will silently rescale validation data automatically to match training data before computing metrics

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* The validation generator directly feeds inputs to the model for metric computation during training. Incorrect preprocessing distorts those metrics, even though it does not affect weight updates.
  * *Why B is correct:* The model's learned weights expect inputs in [0, 1]. Validation images arriving as [0, 255] activate neurons at 255× their intended scale, producing near-random predictions and artificially low validation accuracy — even though the model is learning correctly on training data.
  * *Why C is incorrect:* TensorFlow does not compare preprocessing configurations between generators. No shape mismatch occurs; both generators produce the same tensor shapes. The error is statistical, not structural.
  * *Why D is incorrect:* Keras performs no automatic rescaling or normalization at inference time. What the generator outputs is what the model receives.

---

### Question 7 (5 points)

On the TF Developer Certificate exam, when saving a model for submission, a candidate calls `model.save('my_model.h5')`. A classmate saves using `model.save('my_model')` (no extension). What is the key difference between these two saved artifacts?

* A) The `.h5` format is deprecated and will fail to load in TF 2.x; `model.save('my_model')` is always preferred
* B) Both are functionally identical and can be loaded with `tf.keras.models.load_model()` without any difference in inference behavior
* C) `.h5` saves to a single HDF5 file (Keras legacy format); omitting the extension saves to a SavedModel directory with a `saved_model.pb` graph and a `variables/` folder
* D) The SavedModel format does not include the optimizer state, so a model saved without `.h5` cannot be fine-tuned after loading

* **Correct Answer:** C
* **Distractor Analysis:**
  * *Why A is incorrect:* `.h5` is not deprecated in TF 2.x — both formats are fully supported. The exam specifically instructs candidates to save as `.h5`.
  * *Why B is incorrect:* Functionally both can be used for inference, but the file format and directory structure differ significantly — SavedModel is a directory, `.h5` is a single file.
  * *Why C is correct:* `.h5` produces a single-file HDF5 archive. No extension (or `.tf`) produces a directory containing `saved_model.pb` (frozen graph) and a `variables/` subdirectory. Both are loadable with `tf.keras.models.load_model()`.
  * *Why D is incorrect:* SavedModel format preserves the full model including optimizer state when saved via `model.save()`. The optimizer state claim is false for both formats.

---

### Question 8 (5 points)

A candidate's NLP model on the exam achieves high training accuracy but the validation accuracy plateaus at a low value from epoch 3 onward. Which of the following is the most likely cause and best fix?

* A) The Embedding layer `trainable` flag is set to False, preventing the model from learning word representations; set `trainable=True`
* B) The model is overfitting — add `Dropout` after the LSTM/Dense layers and reduce model capacity, or increase the dataset size with augmentation
* C) The learning rate is too high; switch from `adam` to `sgd` with `lr=0.1`
* D) The `pad_sequences` `padding='post'` argument is incorrect; change to `padding='pre'` for LSTM models

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* Embedding layers are trainable by default. Setting them non-trainable would slow convergence but would not cause the specific pattern of high training accuracy with low validation accuracy diverging from epoch 3.
  * *Why B is correct:* High training accuracy with stagnant low validation accuracy from early epochs is the classic overfitting pattern. The fix is regularization: Dropout layers, reducing LSTM/Dense units, or using pre-trained frozen embeddings (GloVe) to reduce the parameter count.
  * *Why C is incorrect:* A too-high learning rate typically causes training loss to oscillate or diverge, not to achieve high training accuracy. Switching to SGD at lr=0.1 would not target the overfitting root cause.
  * *Why D is incorrect:* While `padding='post'` vs `padding='pre'` can affect LSTM performance (pre-padding is sometimes preferred), it does not cause the sharp train/val accuracy divergence described. Both settings produce valid padded sequences.

---

### Question 9 (5 points)

Which `EarlyStopping` callback configuration is most appropriate when submitting models on the TF Developer Certificate exam?

* A) `EarlyStopping(monitor='loss', patience=1)` — stops training as soon as training loss increases, maximizing speed
* B) `EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)` — stops when validation loss fails to improve for 3 epochs and restores the best weights before saving
* C) `EarlyStopping(monitor='accuracy', patience=5)` — monitors training accuracy to avoid stopping before convergence
* D) `EarlyStopping(monitor='val_accuracy', patience=0)` — stops immediately on the first epoch where validation accuracy does not increase

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* Monitoring `'loss'` (training loss) and stopping at patience=1 would halt training at the first normal fluctuation, before the model has converged. The submitted model would be undertrained.
  * *Why B is correct:* `val_loss` as the monitor targets generalization, not training performance. `patience=3` allows several non-improving epochs before stopping, avoiding premature termination. `restore_best_weights=True` ensures the saved model has the lowest validation loss, not the final epoch's weights.
  * *Why C is incorrect:* Monitoring `'accuracy'` (training accuracy) does not guard against overfitting. A model can achieve 99% training accuracy while generalizing poorly — the exam evaluates on a hidden test set.
  * *Why D is incorrect:* `patience=0` stops at the first non-improvement epoch, making training highly sensitive to noise. The model may stop at epoch 2 due to a random bad batch.

---

### Question 10 (5 points)

On the TF Developer Certificate exam, a candidate's CNN model for image classification uses `model.fit()` with `steps_per_epoch` set but forgets to set `validation_steps`. What is the most likely result?

* A) Training crashes immediately because `validation_steps` is required when using a generator
* B) Keras automatically infers `validation_steps` from the validation generator's dataset size, so no error occurs
* C) Keras will iterate through the entire validation generator repeatedly, causing memory overflow
* D) The model will skip validation entirely and no val_loss or val_accuracy will be reported

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* `validation_steps` is only required when using an infinite `tf.data` dataset or when you want to limit how many batches of validation data are evaluated. Many generator setups work without it.
  * *Why B is correct:* When `validation_steps` is omitted and the validation generator has a finite length (e.g., `ImageDataGenerator.flow_from_directory`), Keras uses the generator's `__len__()` to determine how many batches to evaluate. No error is raised and validation metrics are reported normally.
  * *Why C is incorrect:* Keras does not loop indefinitely over the validation generator when `validation_steps` is omitted for finite generators. Memory overflow from generator repetition is not a risk in this scenario.
  * *Why D is incorrect:* Validation is not skipped — Keras evaluates the validation generator at the end of each epoch. Only if `validation_data=None` is passed is validation skipped entirely.

---

### Question 11 (5 points)

A candidate is preparing for the TF Developer Certificate exam and wants to practice the build-compile-fit pattern for a binary classification task. Which loss function and final activation combination is correct?

* A) Loss: `'sparse_categorical_crossentropy'`, activation: `'softmax'` with 2 output units
* B) Loss: `'binary_crossentropy'`, activation: `'sigmoid'` with 1 output unit
* C) Loss: `'mean_squared_error'`, activation: `'relu'` with 1 output unit
* D) Loss: `'categorical_crossentropy'`, activation: `'sigmoid'` with 2 output units

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* `sparse_categorical_crossentropy` is for multi-class classification with integer labels. While 2-class softmax is technically valid for binary classification, it is nonstandard; the binary cross-entropy + sigmoid pattern is the expected approach.
  * *Why B is correct:* Binary classification: one output neuron with `sigmoid` (outputs a probability in [0, 1]) + `binary_crossentropy` loss. This is the standard and exam-expected pattern for two-class problems.
  * *Why C is incorrect:* MSE with ReLU is a regression configuration. Using it for binary classification would not produce probability outputs and the loss gradient would not push the model toward correct class boundaries.
  * *Why D is incorrect:* `categorical_crossentropy` requires one-hot encoded labels and matches softmax with multiple output units. Using sigmoid with 2 output units would produce two independent probabilities rather than a valid probability distribution.

---

### Question 12 (5 points)

During the four-problem mock exam, a candidate trains an LSTM model on a windowed time series dataset. The LSTM is defined as `tf.keras.layers.LSTM(64, input_shape=[30, 1])`. At inference time, the candidate wants to forecast the next value given a single window stored as a 1D NumPy array `window` of shape `(30,)`. What transformation is needed before calling `model.predict(window)`?

* A) No transformation is needed; the LSTM accepts 1D arrays and reshapes them internally
* B) `window = window.reshape(30, 1)` to add the channel dimension before prediction
* C) `window = window.reshape(1, 30, 1)` to add both the batch dimension and the channel dimension
* D) `window = np.expand_dims(window, axis=0)` to add only the batch dimension, giving shape `(1, 30)`

* **Correct Answer:** C
* **Distractor Analysis:**
  * *Why A is incorrect:* Keras does not automatically reshape inputs. A 1D array of shape `(30,)` would raise a dimension mismatch error.
  * *Why B is incorrect:* `reshape(30, 1)` gives shape `(30, 1)` which is missing the batch dimension. `model.predict()` requires a leading batch axis.
  * *Why C is correct:* The LSTM expects shape `(batch, time_steps, features)`. A single sample needs shape `(1, 30, 1)` — batch size 1, 30 time steps, 1 feature per step. Both the batch and channel dimensions must be added explicitly.
  * *Why D is incorrect:* `np.expand_dims(window, axis=0)` gives shape `(1, 30)` — 2D, missing the required channel dimension. The LSTM would raise an input shape error.

---

### Question 13 (5 points)

The TF Developer Certificate exam allows the use of tensorflow.org and keras.io documentation. A candidate needs to quickly find which `tf.keras.losses` function to use for a multi-class classification problem where labels are integers (not one-hot). Which is correct?

* A) `tf.keras.losses.CategoricalCrossentropy()` — always correct for multi-class problems regardless of label format
* B) `tf.keras.losses.SparseCategoricalCrossentropy()` — designed specifically for integer class labels in multi-class classification
* C) `tf.keras.losses.BinaryCrossentropy()` — works for any classification task with two or more classes
* D) `tf.keras.losses.MeanSquaredError()` — used for classification when class probabilities are needed

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* `CategoricalCrossentropy` expects one-hot encoded labels (e.g., `[0, 0, 1, 0, 0]`). Passing integer labels directly will produce incorrect results or errors.
  * *Why B is correct:* `SparseCategoricalCrossentropy` (or the string `'sparse_categorical_crossentropy'`) accepts integer class labels directly, without requiring one-hot encoding. This is the standard choice when labels are integers.
  * *Why C is incorrect:* `BinaryCrossentropy` is specific to two-class problems (sigmoid output). Using it for multi-class classification would not produce meaningful gradients.
  * *Why D is incorrect:* MSE is a regression loss. For classification, it does not produce the probability calibration behavior that cross-entropy losses provide, resulting in a model that learns slowly and poorly.

---

### Question 14 (5 points)

A candidate on the TF Developer Certificate exam is using a pre-trained MobileNetV2 base model. They call `tf.keras.applications.MobileNetV2(input_shape=(160, 160, 3), include_top=False, weights='imagenet')`. What does `include_top=False` do?

* A) It removes the batch normalization layers from the MobileNetV2 architecture to allow fine-tuning
* B) It removes the final classification Dense layer and global average pooling layer so the candidate can add a custom classification head for their specific number of classes
* C) It freezes all layers except the final convolutional block so only the top is trainable
* D) It prevents the model from loading ImageNet weights and initializes all layers randomly

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* `include_top=False` has no effect on batch normalization layers. It specifically controls whether the final dense classification layers are included.
  * *Why B is correct:* `include_top=False` omits the final pooling and dense classification head (the "top" of the network), returning the feature extraction backbone only. The candidate then appends `GlobalAveragePooling2D()` and `Dense(num_classes, activation='softmax')` to match their specific task.
  * *Why C is incorrect:* `include_top=False` does not freeze any layers. Layer freezing is controlled separately with `base_model.trainable = False`.
  * *Why D is incorrect:* The `weights='imagenet'` argument is independent of `include_top`. With `include_top=False, weights='imagenet'`, the convolutional layers still receive their pretrained ImageNet weights.

---

### Question 15 (5 points)

Across all four TF Developer Certificate exam task categories, which Keras callback is most critical to include in every `model.fit()` call to ensure the submitted `.h5` model contains the best-performing weights rather than the final epoch's weights?

* A) `tf.keras.callbacks.TensorBoard(log_dir='./logs')` — logs training metrics and saves model snapshots
* B) `tf.keras.callbacks.ReduceLROnPlateau(patience=2, factor=0.5)` — reduces learning rate and implicitly saves the best model
* C) `tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)` — stops training when val_loss stops improving and restores the weights from the best epoch
* D) `tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-3 * 0.9 ** epoch)` — decays the learning rate per epoch and stabilizes final weights

* **Correct Answer:** C
* **Distractor Analysis:**
  * *Why A is incorrect:* TensorBoard logs metrics and graph visualizations but does not save model weights. It has no effect on which weights are present in the model at the end of training.
  * *Why B is incorrect:* `ReduceLROnPlateau` adjusts the learning rate when improvement stalls but does not restore best weights or save model checkpoints. The model will still end on the final epoch's weights.
  * *Why C is correct:* `restore_best_weights=True` is the key argument. After training stops (either by `patience` or by reaching `epochs`), Keras reverts the model's weights to those from the epoch with the best monitored metric. This guarantees the submitted `.h5` has the best generalization.
  * *Why D is incorrect:* A learning rate scheduler decays the learning rate but does not track or restore the best weights. A smaller learning rate late in training does not mean better weights — the model may have already overfit before the decay takes effect.

---

### Question 16 (5 points)

A candidate finishes training a time series LSTM model and calls `model.save('ts_model.h5')` before submitting. The exam grader reports that the model does not meet the MAE threshold. The candidate realizes they used `EarlyStopping(monitor='val_loss', patience=3)` without `restore_best_weights=True`. What happened?

* A) The model was saved at the epoch with the lowest training loss, which always corresponds to the lowest validation MAE
* B) The model was saved at the final epoch, which may have higher validation loss than earlier epochs because `restore_best_weights=False` is the default
* C) `EarlyStopping` without `restore_best_weights` raises a warning and saves randomly selected epoch weights
* D) The submitted model is identical to what would have been saved with `restore_best_weights=True` because LSTM weights converge monotonically

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* Training loss and validation MAE are not necessarily minimized at the same epoch. Training loss can continue decreasing while validation metrics worsen (overfitting). Saving at the training-loss minimum does not guarantee best generalization.
  * *Why B is correct:* `restore_best_weights` defaults to `False`. When `EarlyStopping` triggers after `patience` non-improving epochs, training stops at epoch N+patience — but the model weights remain from epoch N+patience, not epoch N (the best epoch). The candidate should always set `restore_best_weights=True` on the exam.
  * *Why C is incorrect:* Keras raises no warning for missing `restore_best_weights`. The callback silently uses default behavior, which retains the final epoch's weights.
  * *Why D is incorrect:* LSTM weights do not converge monotonically on validation metrics. Validation loss typically has a U-shaped curve — it decreases then increases as overfitting sets in. The best weights are near the minimum of that curve, not at the final epoch.

---

### Question 17 (5 points)

A candidate is building a multi-class CNN classifier for the exam using `flow_from_directory`. The training directory has 5 class subdirectories with 1000 images each. The candidate sets `batch_size=32`. How many steps per epoch does `model.fit()` need to process the full training set once?

* A) 32 — one step per batch, and `batch_size=32` means 32 steps
* B) 1000 — one step per image class directory
* C) 157 — `ceil(5000 / 32)` = 157 steps to cover all 5000 images with batches of 32
* D) 5000 — one step per training image

* **Correct Answer:** C
* **Distractor Analysis:**
  * *Why A is incorrect:* `batch_size=32` means each step processes 32 images, not that there are 32 steps total. Number of steps depends on dataset size divided by batch size.
  * *Why B is incorrect:* Steps per epoch is not determined by the number of class directories. The class structure determines the label mapping, not the step count.
  * *Why C is correct:* Total images = 5 classes × 1000 = 5000. Steps per epoch = ceil(5000 / 32) = 157 (156 full batches of 32 + 1 partial batch of 8). `flow_from_directory` sets `__len__()` to this value, so Keras uses it automatically when `steps_per_epoch` is not specified.
  * *Why D is incorrect:* One step per image would mean `batch_size=1`. With `batch_size=32`, each step processes 32 images simultaneously — dividing the total work by 32.

---

### Question 18 (5 points)

On the TF Developer Certificate exam, a candidate is training a text classification model with an LSTM. After padding sequences to length 100, they add the layers `Embedding(10001, 16, input_length=100)` → `LSTM(64)` → `Dense(1, activation='sigmoid')`. The model runs but validation accuracy never exceeds 52%. Which diagnostic step should the candidate perform first?

* A) Increase the LSTM units from 64 to 512 to give the model more capacity to learn patterns
* B) Verify that the training labels are correct and that the Tokenizer was fit on training data only (not the full dataset including validation)
* C) Replace `sigmoid` with `softmax` and change the loss to `categorical_crossentropy`
* D) Add more Dense layers after the LSTM to increase model depth

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* 52% accuracy on a binary task is near random chance. Adding LSTM capacity would not help if the underlying data pipeline (labels or tokenization) is broken. Diagnosis should precede architectural changes.
  * *Why B is correct:* Near-random accuracy (52%) strongly suggests a data pipeline bug rather than a model capacity issue. Common causes: labels are swapped or shuffled incorrectly, the Tokenizer was accidentally fit on both train and validation text (data leakage that inflates training accuracy but not val), or the sequences are not aligned with their labels after shuffling. These must be verified before tuning the architecture.
  * *Why C is incorrect:* For binary classification, `sigmoid` + `binary_crossentropy` is correct. Switching to `softmax` + `categorical_crossentropy` with a single output unit would break the model further.
  * *Why D is incorrect:* Adding depth addresses underfitting, not near-random accuracy. A deeper broken model is still broken.

---

### Question 19 (5 points)

A candidate on the TF Developer Certificate exam wants to add `ModelCheckpoint` to save the best model during training. Which callback configuration correctly saves the best model to `'best_model.h5'` based on validation accuracy?

* A) `ModelCheckpoint('best_model.h5', monitor='val_accuracy', save_best_only=False)`
* B) `ModelCheckpoint('best_model.h5', monitor='val_accuracy', save_best_only=True, mode='max')`
* C) `ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True, mode='max')`
* D) `ModelCheckpoint('best_model.h5', save_best_only=True)` with no monitor argument

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why A is incorrect:* `save_best_only=False` saves the model at every epoch, overwriting the file each time. The final saved model is from the last epoch, not the best epoch.
  * *Why B is correct:* `monitor='val_accuracy'` tracks validation accuracy; `save_best_only=True` saves only when an improvement occurs; `mode='max'` tells Keras that higher is better for accuracy (the default for accuracy metrics, but explicit is safer on an exam). This saves the single best checkpoint.
  * *Why C is incorrect:* `monitor='val_loss'` with `mode='max'` is contradictory — for loss, improvement means a lower value (`mode='min'`). Using `mode='max'` with val_loss would save the model with the highest validation loss instead of the lowest.
  * *Why D is incorrect:* Without a `monitor` argument, `ModelCheckpoint` defaults to monitoring `'val_loss'`. If the candidate wants to optimize for accuracy (not loss), the monitor must be specified explicitly.

---

### Question 20 (5 points)

When preparing for the TF Developer Certificate exam, a candidate reviews the four task categories. Which pairing of task category to the correct output layer configuration is correct for all four categories?

* A) Basic regression → `Dense(1)` no activation; binary image classification → `Dense(1, activation='sigmoid')`; NLP multi-class → `Dense(num_classes, activation='softmax')`; time series forecast → `Dense(1)` no activation
* B) Basic regression → `Dense(1, activation='relu')`; binary image classification → `Dense(2, activation='softmax')`; NLP multi-class → `Dense(num_classes, activation='sigmoid')`; time series forecast → `Dense(1, activation='tanh')`
* C) Basic regression → `Dense(1, activation='sigmoid')`; binary image classification → `Dense(1, activation='sigmoid')`; NLP multi-class → `Dense(1, activation='softmax')`; time series forecast → `Dense(1, activation='relu')`
* D) All four task categories use `Dense(num_classes, activation='softmax')` as the output layer regardless of task type

* **Correct Answer:** A
* **Distractor Analysis:**
  * *Why A is correct:* Regression (predicting a continuous value) → linear output `Dense(1)`, no activation. Binary classification → `Dense(1, activation='sigmoid')` outputting a probability. Multi-class NLP → `Dense(num_classes, activation='softmax')` outputting a probability distribution. Time series one-step-ahead forecasting → `Dense(1)` linear output, same as regression. Memorizing this table is essential exam preparation.
  * *Why B is incorrect:* Regression with `relu` clips negative predictions to zero — invalid for targets that can be negative (e.g., temperature forecasting). Binary classification with `softmax(2)` is non-standard. Time series with `tanh` clips output to [-1, 1], preventing accurate forecasting of values outside that range.
  * *Why C is incorrect:* Sigmoid for regression would clip all outputs to [0, 1], which is wrong for general continuous value prediction. `Dense(1, activation='softmax')` with a single unit always outputs 1.0 — a degenerate configuration.
  * *Why D is incorrect:* Softmax with `num_classes` is for multi-class classification only. Applying it to regression or binary classification tasks would produce incorrect output semantics and inappropriate loss gradients.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | C |
| 6 | B |
| 7 | C |
| 8 | B |
| 9 | B |
| 10 | B |
| 11 | B |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | C |
| 16 | B |
| 17 | C |
| 18 | B |
| 19 | B |
| 20 | A |
