# Quiz: Module 16 - Final Exam Prep and TensorFlow Developer Certificate
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
The TensorFlow Developer Certificate exam is administered in which environment, and what does a candidate submit to receive credit for each problem?
*   A) A browser-based IDE with automatic grading — the candidate writes code in a web editor and the system evaluates it live against hidden test cases without any file submission.
*   B) A PyCharm IDE environment with the TF exam plugin — the candidate builds and trains a model that meets an accuracy/loss threshold, then submits the saved `.h5` model file for automated evaluation.
*   C) A Jupyter Notebook submitted to a Kaggle competition — the exam evaluates the candidate's notebook output cells and the final confusion matrix printed at the end of execution.
*   D) A command-line terminal where the candidate types TensorFlow commands from memory — the exam is closed-book with no internet access and graded on command accuracy by a human proctor.
*   **Correct Answer:** B) The TF Developer Certificate uses the PyCharm TF exam plugin. Candidates download problem sets, write and train models locally in PyCharm, verify that their model meets the required threshold, and upload the saved `.h5` file through the plugin. The exam is five hours, open-book, and open-internet — candidates may use tensorflow.org and keras.io documentation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The exam is not browser-based. It runs in PyCharm on the candidate's own machine. There is no live automatic grading of code — the submitted artifact is the trained `.h5` model file, which is evaluated against a hidden test set.
    *   *Why B is correct:* Key exam logistics: PyCharm + TF exam plugin; five-hour window; four task categories; model saved with `model.save('model.h5')`; each problem has a minimum accuracy/loss threshold. Open-book and open-internet (tensorflow.org, keras.io) are explicitly allowed.
    *   *Why C is incorrect:* The TF Developer Certificate has no connection to Kaggle or Jupyter Notebooks. Notebook-based coding assessments are used in other certifications (e.g., Databricks) but not the TF exam.
    *   *Why D is incorrect:* The exam is explicitly open-book and open-internet. Closed-book, command-line-based, human-proctored typing tests describe a completely different kind of assessment.

---

**Question 2**
Which of the following is the most accurate definition of the **build-compile-fit pattern** in TensorFlow and Keras?
*   A) A three-phase deployment pipeline where a trained model is built into a Docker container, compiled to a TFLite flatbuffer, and fit into a mobile app distribution package for the App Store or Google Play.
*   B) The fundamental Keras model training workflow: define the architecture with `tf.keras.Sequential` or the Functional API (build), configure the loss function, optimizer, and metrics with `model.compile()` (compile), then train on data with `model.fit()` (fit) — the three-step pattern used for every model on the TF Developer Certificate exam.
*   C) A machine learning cross-validation technique that builds k different train/test splits, compiles performance metrics across all splits, and fits a final model on the full dataset after hyperparameter selection.
*   D) A TensorFlow graph execution mode where the computational graph is built statically at import time, compiled to XLA for hardware acceleration, and fit to GPU memory before any data is processed.
*   **Correct Answer:** B) Every TF Developer Certificate exam problem follows this exact three-step pattern. Build: `model = tf.keras.Sequential([layers...])`. Compile: `model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])`. Fit: `model.fit(train_data, epochs=N, validation_data=val_data, callbacks=[...])`. Internalizing this pattern for all four task categories is the single most important exam preparation task.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a model deployment pipeline (containerization, TFLite conversion, app packaging) — an entirely different workflow from the Keras training API. The build-compile-fit pattern refers specifically to training, not deployment.
    *   *Why B is correct:* The three methods map directly to the exam workflow: `Sequential` or Functional API for architecture → `compile()` for training configuration → `fit()` for training execution. All four exam task categories use this pattern with task-specific layers and loss functions.
    *   *Why C is incorrect:* This describes k-fold cross-validation, a model evaluation strategy. Cross-validation involves no `compile()` or `fit()` calls in the Keras sense — it is a data splitting and evaluation methodology.
    *   *Why D is incorrect:* XLA compilation and graph execution are TensorFlow infrastructure concerns that happen automatically in TF2 eager mode. The build-compile-fit pattern is a user-facing Keras API workflow, not a description of TF's internal execution engine.

---

**Question 3**
A candidate is working on the NLP text classification task on the TF Developer Certificate exam. They define a tokenizer with `vocab_size = 10000` and build a model starting with an Embedding layer. Which line correctly defines the Embedding layer?
*   A) `tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length)`
*   B) `tf.keras.layers.Embedding(vocab_size + 1, embedding_dim, input_length=max_length)`
*   C) `tf.keras.layers.Embedding(embedding_dim, vocab_size, input_length=max_length)`
*   D) `tf.keras.layers.Embedding(max_length, embedding_dim, input_dim=vocab_size)`
*   **Correct Answer:** B) The `input_dim` (first argument) of the Embedding layer must be `vocab_size + 1`, not `vocab_size`. The `Tokenizer` assigns indices starting at 1 (index 0 is reserved for padding). If `input_dim=vocab_size`, index `vocab_size` (the highest valid token index) falls outside the embedding table and raises an index-out-of-bounds error at runtime.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Using `vocab_size` (without +1) is the most common NLP exam mistake. With `num_words=10000`, the tokenizer can assign tokens indices 1 through 10000. The embedding table needs 10001 rows (indices 0–10000) — so `input_dim` must be 10001.
    *   *Why B is correct:* `Embedding(vocab_size + 1, embedding_dim, input_length=max_length)` is the correct call. The argument order is `(input_dim, output_dim, input_length)`. `input_dim` = vocabulary size + 1 for the 0 padding index. `output_dim` = embedding vector dimension (e.g., 16, 32, 64). `input_length` = the padded sequence length.
    *   *Why C is incorrect:* The argument order is reversed — `(input_dim, output_dim)`, not `(output_dim, input_dim)`. Swapping these would create a tiny embedding table with 16 rows (if `embedding_dim=16`) and vectors of length 10000, producing a model that does not learn meaningful word representations.
    *   *Why D is incorrect:* `Embedding` does not have an `input_dim` keyword argument — `input_dim` is the first positional argument. Additionally, placing `max_length` as the first argument would set the vocabulary size to `max_length`, which is incorrect semantically.

---

**Question 4**
During the image classification task on the exam, a candidate unfreezes the top 20 layers of a MobileNetV2 base model for fine-tuning. After setting `layer.trainable = True` for those layers, what must happen before calling `model.fit()` again?
*   A) The model must be saved and reloaded with `tf.keras.models.load_model()` to force TensorFlow to rebuild the computational graph with the new trainable configuration.
*   B) The model must be recompiled with `model.compile()` using a lower learning rate before resuming training — Keras requires recompilation to register changes to layer `trainable` attributes.
*   C) The frozen layers must be re-initialized to random weights because unfreezing restores the original pre-training initialization, discarding the pre-trained ImageNet weights.
*   D) No additional steps are needed — TensorFlow automatically detects changes to `trainable` attributes and adjusts gradient computation on the next `model.fit()` call without recompilation.
*   **Correct Answer:** B) In Keras, `trainable` attribute changes only take effect after `model.compile()` is called. Without recompilation, the optimizer's gradient computation plan does not update and the newly unfrozen layers will not actually receive gradient updates during training. The learning rate for fine-tuning should be much lower than the initial training rate (e.g., `1e-5` vs. `1e-3`) to avoid destroying the pre-trained weights.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Saving and reloading is not required and would be time-consuming. Recompilation with `model.compile()` is the correct and sufficient step to register `trainable` changes — no save/reload cycle is needed.
    *   *Why B is correct:* The fine-tuning pattern: `for layer in base_model.layers[-20:]: layer.trainable = True` → `model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), loss=..., metrics=['accuracy'])` → `model.fit(...)`. The recompile step is mandatory; forgetting it is the most common transfer learning mistake.
    *   *Why C is incorrect:* Unfreezing layers does not reset their weights. The pre-trained weights are preserved — unfreezing only allows those weights to be updated by gradient descent during subsequent training. This is the whole point of fine-tuning.
    *   *Why D is incorrect:* TensorFlow does not automatically detect `trainable` changes between `fit()` calls. The computational graph for gradient computation is fixed at compile time. Changing `trainable` without recompiling results in the unfrozen layers still receiving no gradients.

---

**Question 5**
A candidate submits their time series LSTM model for the forecasting task but receives a score below the threshold. The model's validation MAE is only slightly better than the naive forecast. Which combination of changes is most likely to improve performance enough to meet the threshold?
*   A) Switch from MAE loss to categorical cross-entropy loss and add a softmax output layer — the forecasting task requires classification-style output, not regression.
*   B) Reduce the window size to 1 (single-step input) and remove the LSTM layers, replacing them with a single Dense(1) layer — simpler models always generalize better on time series.
*   C) Increase the window size to capture more temporal context, add a learning rate schedule or `ReduceLROnPlateau` callback, and add a `Lambda` layer as the first layer to expand input dims to `(window_size, 1)` for the LSTM — then retrain with more epochs and `EarlyStopping(restore_best_weights=True)`.
*   D) The model cannot be improved further — a validation MAE only slightly better than naive indicates the time series has no autocorrelation and no neural network can forecast it accurately.
*   **Correct Answer:** C) Marginal improvement over naive most commonly indicates one of three fixable problems: the window is too short (model lacks temporal context), the learning rate is not optimal (model stopped improving prematurely), or the LSTM input shape is wrong (flat `(batch, W)` instead of 3D `(batch, W, 1)`). The Lambda expand_dims fix, a longer window, a learning rate schedule, and `EarlyStopping(restore_best_weights=True)` together address all three issues.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Time series forecasting is a regression problem — the output is a continuous numerical value (the next time step's value). Categorical cross-entropy and softmax are for classification problems with discrete class labels. Changing to these would break the model entirely.
    *   *Why B is incorrect:* Reducing the window to 1 eliminates all temporal context — the model can only see the most recent value, which is equivalent to the naive forecast. Removing LSTM layers destroys the model's ability to learn temporal patterns. Simpler is not always better; the problem requires learning sequences.
    *   *Why C is correct:* The LSTM input shape bug (`(batch, W)` instead of `(batch, W, 1)`) is the single most common time series exam error. A Lambda layer `tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1))` as the first layer fixes it. Increasing window size and adding `ReduceLROnPlateau` or `EarlyStopping(restore_best_weights=True)` are the standard performance improvement techniques.
    *   *Why D is incorrect:* Slightly beating naive does not imply no autocorrelation — it more likely indicates a correctable implementation issue (wrong input shape, too-small window, premature convergence). Real-world time series almost always have learnable structure. The appropriate response is to diagnose and fix the implementation, not conclude the problem is unsolvable.
