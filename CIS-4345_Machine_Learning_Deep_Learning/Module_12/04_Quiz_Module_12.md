# Quiz: Module 12 — Model Optimization and Hyperparameter Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points (100 points total).

---

## Question 1

In Keras Tuner, what is the purpose of the `hp` object passed to the `build_model(hp)` function?

A. It is a pre-built Keras model that the tuner modifies by adding layers based on past trial results.
B. It is a HyperParameters object that defines the search space — each call to `hp.Int`, `hp.Float`, or `hp.Choice` registers a searchable dimension that the tuner will sample during each trial.
C. It is a hyperparameter dictionary loaded from a YAML configuration file that specifies fixed values for each trial.
D. It is a callback object that logs hyperparameter values to TensorBoard during training.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Keras Tuner does not start from a pre-built model and modify it. The `build_model` function is called fresh for each trial, and the `hp` object provides sampled values for the current trial's configuration.
- B — Correct. The `hp` object is an instance of `keras_tuner.HyperParameters`. Every `hp.Int(name, ...)`, `hp.Float(name, ...)`, `hp.Choice(name, ...)`, or `hp.Boolean(name)` call registers a dimension of the search space. During each trial, the tuner samples one combination of values from all registered dimensions and passes the resulting `hp` object to `build_model`, which then uses those values to construct and compile the model for that trial.
- C — Incorrect. There is no YAML configuration in the Keras Tuner API. The search space is defined programmatically inside the `build_model` function through `hp.*` method calls.
- D — Incorrect. Keras Tuner has separate integration with TensorBoard via `TensorBoard` callbacks. The `hp` object is a search space definition tool, not a logging mechanism.

---

## Question 2

What is the key difference between `kt.RandomSearch` and `kt.Hyperband` in Keras Tuner?

A. RandomSearch requires a GPU; Hyperband runs only on CPU.
B. RandomSearch evaluates each trial for the full number of epochs; Hyperband uses a successive halving strategy that allocates more compute to promising configurations and discards poor ones early.
C. Hyperband searches only over learning rate; RandomSearch searches over all hyperparameter types.
D. RandomSearch supports `hp.Choice` parameters; Hyperband supports only `hp.Int` and `hp.Float`.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Both search strategies are hardware-agnostic and run on CPU, GPU, or TPU without restriction.
- B — Correct. RandomSearch draws random samples from the search space and trains each for the full epoch budget. Hyperband implements the Hyperband algorithm: it starts many trials at low epoch budgets, keeps the top `1/factor` performers, allocates more epochs to survivors, and repeats. This makes Hyperband much more compute-efficient for large search spaces, because poor configurations are terminated early rather than trained to completion.
- C — Incorrect. Both strategies support the full range of hyperparameter types: `hp.Int`, `hp.Float`, `hp.Choice`, `hp.Boolean`, and `hp.Fixed`. Neither is restricted to specific parameter types.
- D — Incorrect. `hp.Choice` works identically in both RandomSearch and Hyperband. The choice of search strategy is orthogonal to which hyperparameter types are used in the model.

---

## Question 3

After running `tuner.search()`, how do you retrieve the best hyperparameters and use them to build the final model?

A. Call `tuner.best_model()` which returns a compiled, trained model ready for evaluation.
B. Call `tuner.get_best_hyperparameters(num_trials=1)[0]` to get the best `HyperParameters` object, then call `tuner.hypermodel.build(best_hps)` to construct the model with those values.
C. Access `tuner.results['best_trial']['hyperparameters']` to read the best values from the results dictionary.
D. Call `tuner.fit()` a second time — it automatically uses the best configuration from the search.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. There is no `tuner.best_model()` method in the Keras Tuner API. The tuner stores trial results but requires you to explicitly retrieve hyperparameters and build the model.
- B — Correct. This is the standard two-step pattern in Keras Tuner. `get_best_hyperparameters(num_trials=1)[0]` returns a `HyperParameters` object populated with the best-found values. `tuner.hypermodel.build(best_hps)` calls your `build_model` function with those values and returns a compiled Keras model, which you then train to full convergence on the complete dataset.
- C — Incorrect. Keras Tuner does not expose results through a `results` dictionary attribute. Trial results are stored internally and accessed through the `get_best_hyperparameters` and `get_best_models` methods.
- D — Incorrect. Keras Tuner does not have a `tuner.fit()` method. `tuner.search()` is the method that runs the hyperparameter search. The final training run is a separate `model.fit()` call on the model built from the best hyperparameters.

---

## Question 4

What does `converter.optimizations = [tf.lite.Optimize.DEFAULT]` do during TFLite conversion?

A. It enables hardware-specific optimizations for the target device, which must be specified separately with `converter.target_device`.
B. It applies dynamic range quantization, converting float32 model weights to int8 while keeping activations in float32 during inference, typically reducing model size by approximately 4x.
C. It enables full integer quantization for both weights and activations, requiring a representative calibration dataset.
D. It applies float16 quantization, reducing size by 2x and targeting GPU-accelerated edge devices.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. `tf.lite.Optimize.DEFAULT` is not a device-specific optimization flag. It does not require or accept a target device specification. Device-specific delegation (e.g., GPU, Edge TPU) is configured separately through `converter.target_spec`.
- B — Correct. `tf.lite.Optimize.DEFAULT` enables dynamic range quantization. The converter quantizes weight tensors from float32 to int8 at conversion time. During inference, weights are dequantized back to float32 before computations. This typically achieves a 4x size reduction with less than 1% accuracy loss and requires no calibration data. It is the recommended first-pass optimization for most deployment scenarios.
- C — Incorrect. Full integer quantization requires additional configuration: a `representative_dataset` function and `target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]`. Setting only `Optimize.DEFAULT` without these additional settings produces dynamic range quantization, not full integer quantization.
- D — Incorrect. Float16 quantization requires explicitly setting `converter.target_spec.supported_types = [tf.float16]`. The `DEFAULT` flag alone does not select float16 quantization.

---

## Question 5

When running TFLite inference using the `Interpreter` API, what is the correct sequence of operations?

A. `load_model()` → `set_input()` → `run()` → `get_output()`
B. `Interpreter(model_content=...)` → `allocate_tensors()` → `set_tensor()` → `invoke()` → `get_tensor()`
C. `TFLiteModel.load()` → `TFLiteModel.predict()` → `TFLiteModel.result()`
D. `tf.lite.run_model(tflite_bytes, input_data)` which returns predictions directly

Correct Answer: B

Distractor Analysis:

- A — Incorrect. The TFLite Interpreter API does not have `load_model`, `set_input`, `run`, or `get_output` methods. These method names do not exist in the TFLite Python API.
- B — Correct. The correct TFLite inference sequence is: (1) create an `Interpreter` with `model_content=tflite_bytes`; (2) call `allocate_tensors()` to allocate memory for all input and output tensors; (3) set the input with `set_tensor(input_details[0]['index'], input_data)`; (4) call `invoke()` to run inference; (5) retrieve the output with `get_tensor(output_details[0]['index'])`.
- C — Incorrect. There is no `TFLiteModel` class in the TensorFlow Lite Python API. The `Interpreter` class is the correct entry point for TFLite inference.
- D — Incorrect. There is no `tf.lite.run_model` function. The Interpreter class must be used for TFLite inference, following the multi-step sequence described in option B.

---

## Question 6

A model trained on a server achieves 92% accuracy. After applying full integer quantization and deploying to a mobile device, the accuracy drops to 89%. Which statement best describes this result?

A. The quantization process corrupted the model and it must be retrained from scratch.
B. A 3 percentage point accuracy drop from full integer quantization is a catastrophic failure — acceptable degradation should be less than 0.1%.
C. A 3 percentage point accuracy drop from full integer quantization is larger than typical (less than 1% is common) and suggests the model may benefit from quantization-aware training or a larger calibration dataset.
D. The 3 percentage point drop proves that int8 quantization is always incompatible with accuracy above 90%.

Correct Answer: C

Distractor Analysis:

- A — Incorrect. Quantization does not corrupt model weights — it approximates them at lower precision. If accuracy degrades unacceptably, the model should undergo quantization-aware training (QAT), not retraining from scratch, since QAT preserves the learned representations while making the model robust to quantization noise.
- B — Incorrect. While less than 1% is the typical benchmark for dynamic range and full integer quantization on well-behaved models, 3 percentage points is not described as a "catastrophic failure" — it is a meaningful degradation that warrants investigation and remediation. It does not signal a broken model, only one that is sensitive to quantization.
- C — Correct. Post-training full integer quantization typically degrades accuracy by less than 1% on well-behaved models with sufficient calibration data. A 3 percentage point drop indicates the model is sensitive to the precision reduction. Remediation options include: increasing the calibration dataset size (use 500–1000 representative samples instead of the minimum 100), applying quantization-aware training (QAT) which simulates quantization during training to make the model robust to it, or switching to dynamic range quantization which keeps activations in float32.
- D — Incorrect. Many models quantized to int8 maintain accuracy within 1% of the float32 baseline. The 3 percentage point drop is not a universal property of int8 quantization — it is specific to this model's sensitivity and calibration setup.

---

## Question 7

In a TFX pipeline, what is the role of the `Evaluator` component?

A. It evaluates the model's inference speed on the target deployment hardware.
B. It computes evaluation metrics on held-out data and compares the new model against a previously deployed baseline, blocking promotion if the new model does not meet a defined threshold.
C. It generates evaluation data by running the trained model against the training set to detect overfitting.
D. It evaluates the data schema for anomalies and rejects batches that contain missing or out-of-range values.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Inference speed benchmarking is not the purpose of the TFX Evaluator component. Hardware performance profiling is done with separate tools like TFLite benchmarking utilities or TF Profiler.
- B — Correct. The TFX Evaluator component computes metrics on the evaluation split and performs a **model blessing** check: it compares the candidate model against a baseline (typically the currently deployed model) on defined metrics. If the candidate model does not improve on the baseline by at least the configured threshold, the Evaluator does not bless the model, and the Pusher component will not deploy it. This creates an automated quality gate for production ML systems.
- C — Incorrect. Evaluating against the training set to detect overfitting is not the Evaluator's purpose. That kind of analysis is handled during training via validation metrics in `model.fit`. The TFX Evaluator always uses held-out evaluation data, not training data.
- D — Incorrect. Detecting data anomalies and schema violations is the role of the `ExampleValidator` component, not the Evaluator. ExampleValidator compares incoming data statistics against the schema produced by SchemaGen.

---

## Question 8

What is the primary reason that the learning rate is considered the most important hyperparameter in deep learning?

A. The learning rate determines the number of epochs required for training, and more epochs always produce a better model.
B. The learning rate directly controls the size of parameter updates at each gradient step — a value that is too high causes divergence or oscillation, while a value that is too low makes training so slow it never reaches a good solution within a practical compute budget.
C. The learning rate is the only hyperparameter that cannot be searched automatically with Keras Tuner, requiring manual selection.
D. The learning rate controls the ratio of training to validation examples, affecting how much data the model sees during each epoch.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. More training epochs do not always produce a better model — overtraining leads to overfitting, and early stopping is used precisely to prevent this. The number of epochs is a separate hyperparameter from the learning rate.
- B — Correct. The learning rate scales every gradient update across every parameter in the network at every training step. Even a small change — from `1e-3` to `1e-2` — can destabilize training entirely. Conversely, a rate of `1e-6` on a large network may require hundreds of epochs to reach the same loss that `1e-3` reaches in 10 epochs. No other single hyperparameter has this level of global impact on training dynamics, which is why practitioners invest in learning rate diagnostics (range tests, warmup schedules, adaptive optimizers) more than any other hyperparameter.
- C — Incorrect. Keras Tuner fully supports learning rate search through `hp.Choice('lr', values=[1e-4, 5e-4, 1e-3])` or `hp.Float('lr', min_value=1e-5, max_value=1e-2, sampling='log')`. It is one of the most commonly searched hyperparameters.
- D — Incorrect. The learning rate has no effect on train/validation split ratios. Data splitting is controlled by `validation_split` or by the dataset construction, independently of the optimizer configuration.

---

## Question 9

Which Keras Tuner hyperparameter method is most appropriate for searching over learning rate values spanning multiple orders of magnitude, such as `1e-5` to `1e-1`?

A. `hp.Int('lr', min_value=1, max_value=5)` with a manual mapping to powers of 10
B. `hp.Float('lr', min_value=1e-5, max_value=1e-1, sampling='log')` which samples values on a logarithmic scale
C. `hp.Choice('lr', values=[1e-5, 1e-4, 1e-3, 1e-2, 1e-1])` is always preferred because it limits the search to exact known-good values
D. `hp.Fixed('lr', value=1e-3)` to avoid wasting trials on learning rate when other hyperparameters are more important

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Using `hp.Int` with a manual mapping is a workaround that is both fragile and unnecessary. `hp.Float` with `sampling='log'` handles logarithmic ranges natively and is the intended API for this use case.
- B — Correct. `hp.Float('lr', min_value=1e-5, max_value=1e-1, sampling='log')` tells Keras Tuner to sample values on a logarithmic scale between `1e-5` and `1e-1`. Because learning rate performance is typically log-linear (the difference between `1e-4` and `1e-3` is as significant as between `1e-2` and `1e-1`), log-scale sampling is the correct choice. Linear sampling would over-represent values near the upper bound.
- C — Incorrect. `hp.Choice` with a fixed list is appropriate when you have strong prior knowledge about good values. For exploration across multiple orders of magnitude, `hp.Float` with `sampling='log'` provides finer-grained coverage and is more flexible. Neither is "always preferred" — the choice depends on whether the search should explore continuously or test specific values.
- D — Incorrect. Fixing the learning rate with `hp.Fixed` removes it from the search entirely. While this is sometimes appropriate when the optimal learning rate is already known, it defeats the purpose of automated hyperparameter search for a new problem.

---

## Question 10

A team deploys a Keras model as a TFLite model to a fleet of Android devices. Six months later, they retrain the model with new data and observe that the original float32 Keras model improved from 91% to 94% accuracy. They apply the same dynamic range quantization as before and deploy the new `.tflite` file. They report that quantized accuracy is now only 88% — worse than before quantization and worse than the original deployment. What is the most likely explanation?

A. Dynamic range quantization does not support model retraining — a new converter instance must be installed on each device to re-enable quantization.
B. The new model architecture is more complex (more layers or larger weights) and therefore more sensitive to quantization noise than the original model, suggesting quantization-aware training or a larger calibration dataset would help.
C. TFLite quantized models have a hard accuracy ceiling of 90% and cannot exceed it regardless of the float32 baseline.
D. The quantization conversion step resets all model weights to their initialization values, effectively discarding the new training.

Correct Answer: B

Distractor Analysis:

- A — Incorrect. Dynamic range quantization is a converter-side operation that works on any Keras model regardless of whether the model was previously quantized. There is no restriction on retraining, and no per-device converter installation is required.
- B — Correct. When a retrained model is more complex — more layers, larger weight matrices, or weights with a wider dynamic range — it may be more sensitive to the precision loss introduced by int8 weight quantization. This is a known phenomenon: some architectures and training regimes produce weight distributions that are harder to approximate in int8 without accuracy loss. Remediation options include quantization-aware training (QAT), which simulates quantization noise during training so the optimizer can compensate, or increasing the number of representative calibration samples if full integer quantization is being used.
- C — Incorrect. TFLite quantized models routinely achieve accuracies above 90% across standard benchmarks. There is no architectural ceiling. For example, MobileNetV2 quantized to int8 achieves approximately 71% Top-1 on ImageNet — limited by the base architecture, not by quantization.
- D — Incorrect. The TFLite converter reads the trained weights from the Keras model and stores their quantized approximations. It does not reset, reinitialize, or modify the learned parameter values in any destructive way.

---

*End of Quiz — Module 12*
