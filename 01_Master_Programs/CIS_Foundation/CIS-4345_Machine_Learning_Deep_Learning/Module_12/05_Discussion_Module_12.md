# Discussion Forum: Module 12 — Model Optimization and Hyperparameter Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Forum Instructions

Read all three scenarios below. Choose **one scenario** to respond to in your initial post. Your initial post must be 175–225 words and directly address the scenario prompt. Then reply to at least **one peer** who chose a different scenario with a substantive response of 60 or more words.

Initial posts are due by **Thursday at 11:59 PM**. Peer responses are due by **Sunday at 11:59 PM**.

---

## Scenario A — Choosing a Hyperparameter Search Strategy

A fintech startup is developing a fraud detection model for real-time transaction scoring. Their dataset has 500,000 labeled transactions (2% positive — fraudulent). They want to tune the following hyperparameters: number of dense layers (1–4), units per layer (32–512), dropout rate (0.1–0.5), learning rate (1e-5 to 1e-2), and whether to use batch normalization (yes or no). Their compute budget allows approximately 40 GPU-hours for the entire search.

The lead ML engineer wants to use `BayesianOptimization` because "it finds good solutions with fewer trials." A junior engineer argues for `RandomSearch` because "it's simpler and less likely to get stuck in a bad region of the search space." A data scientist on the team suggests they run both and compare results.

Respond to the following: Which strategy would you recommend for this specific search space and compute budget, and why? How does the class imbalance (2% positive) affect the choice of tuner objective metric? Is the data scientist's suggestion to run both strategies worthwhile or a waste of the compute budget? What practical steps would you take before launching a full search to ensure the compute is spent efficiently?

### Sample Response — Scenario A

For this search space — 5 hyperparameters spanning a meaningful range — with a 40 GPU-hour budget, I would recommend `Hyperband` over both `BayesianOptimization` and `RandomSearch`. The junior engineer's instinct about Bayesian optimization getting stuck in local optima is legitimate for high-dimensional spaces. Hyperband's successive halving approach efficiently eliminates poor configurations early without requiring the surrogate model that BayesianOptimization depends on. With 40 GPU-hours, Hyperband can evaluate many more configurations than Bayesian optimization can model accurately.

The class imbalance is critically important for the objective metric. Using `val_accuracy` as the tuner objective would be misleading — a model predicting "no fraud" for every transaction achieves 98% accuracy. The tuner objective should be `val_auc` (area under the ROC curve) or a custom metric tracking recall at a fixed precision threshold, which directly measures fraud detection quality.

The data scientist's suggestion is interesting but I would not run both strategies in parallel from the start. I would first spend 2–3 GPU-hours on a small `RandomSearch` with 10 trials to validate that the `build_model` function is correct and that at least some configurations converge. Only after confirming the search space is well-formed would I launch the full `Hyperband` search. This validation step prevents wasting 40 hours on a buggy hypermodel.

---

## Scenario B — Quantization Accuracy Degradation in Production

A medical device company has deployed a retinal disease screening model on a tablet used by ophthalmologists in low-resource clinics. The original float32 Keras model achieves 95.2% sensitivity and 93.8% specificity on their test set. After dynamic range quantization and TFLite conversion for the tablet's ARM processor, sensitivity drops to 91.4% — a 3.8 percentage point loss.

The regulatory affairs team flags this as a potential issue: the device is classified as a Class II medical device, and the submitted accuracy data was based on the float32 model. The engineering team argues: "3.8% is acceptable — the model is still clinically useful." The clinical team disagrees: "In retinal screening, missed diagnoses have serious consequences. 3.8% degradation is not acceptable."

Respond to the following: Who is right, and what technical options exist to recover the lost sensitivity? What is quantization-aware training and how would it help here? Should the company re-submit regulatory documentation for the quantized model? What is the correct order of technical steps to address the degradation before considering a re-submission?

### Sample Response — Scenario B

The clinical team is right in this context. A 3.8 percentage point drop in sensitivity for a Class II medical screening device is clinically meaningful — it translates directly to missed diagnoses at scale. The engineering framing of "still clinically useful" applies the wrong standard. Regulatory submissions for medical devices are tied to specific claimed performance metrics; the quantized model's performance is what the deployed device actually achieves, and that is what matters for patient safety and regulatory compliance.

The correct technical remediation sequence is: first, increase the calibration dataset for post-training quantization from the typical 100–200 samples to 500–1000 representative samples covering diverse pathology presentations. Many quantization sensitivity issues trace back to inadequate calibration. Second, if that does not recover sensitivity, apply quantization-aware training (QAT). QAT inserts fake quantization nodes into the computation graph during training, simulating int8 precision so the optimizer can adjust weights to compensate for rounding errors. This typically recovers all or most of the accuracy lost to post-training quantization. Third, consider switching from dynamic range quantization to float16 quantization, which introduces less precision loss at a modest size penalty.

On the regulatory question: yes, if the deployed device uses the quantized model, the performance of the quantized model is the submitted claim. A re-evaluation against the test set with the final quantized model is the correct procedure before deployment, regardless of submission requirements.

---

## Scenario C — Designing a Production ML Pipeline

A retail company runs a product recommendation engine that currently requires a data scientist to manually retrain the model each month. The process involves downloading a CSV of new user interaction data, running a Jupyter notebook to retrain, evaluating metrics manually, and uploading the new model file to the serving API. The team has grown and the manual process takes 2–3 days per retraining cycle and has produced two incidents where a worse model was deployed because evaluation was skipped under time pressure.

The engineering team proposes building a TFX pipeline to automate the workflow. A skeptical VP of Engineering asks: "What does TFX actually give us that we can't get from a well-written Python script? Why add this complexity?"

Respond to the following: How would you answer the VP's question — what does TFX provide that a script cannot? Map each TFX component (ExampleGen, StatisticsGen, SchemaGen, ExampleValidator, Transform, Trainer, Evaluator, Pusher) to the specific pain point it addresses in the current manual workflow. What is the most important single component for preventing the "deployed a worse model" incident, and why? What would you tell the team about the learning curve cost vs. long-term benefit?

### Sample Response — Scenario C

The VP's question is legitimate, and the honest answer is: a well-written Python script can do most of what TFX does, but a script requires discipline and documentation to maintain correctly as team members change, while TFX enforces the correct workflow structurally.

Mapping TFX components to the current pain points: ExampleGen eliminates the manual CSV download by automating data ingestion and consistent train/eval splitting. StatisticsGen and SchemaGen replace the ad hoc data inspection step that is often skipped under time pressure. ExampleValidator catches the specific scenario where corrupted or shifted data enters training and produces a quietly worse model. Transform ensures that the feature engineering applied during training is identical at serving time — a subtle bug that scripts often introduce. Trainer automates the retraining run. Evaluator is the most important single component for preventing the "deployed a worse model" incident: it compares the new model against the baseline and can automatically block deployment if the candidate model does not improve on defined metrics. The Pusher then deploys only blessed models.

The learning curve cost is real — TFX has a steeper initial setup than a script. I would frame it to the team this way: the 2–3 day manual cycle and the two deployment incidents represent ongoing operational cost. The incidents alone likely justified the TFX investment. A one-time 2–3 week integration that eliminates recurring risk and manual labor is a straightforward trade.

---

## Peer Response Examples

### Peer Response to Scenario A (67 words)

Your point about using `val_auc` instead of `val_accuracy` as the tuner objective is exactly right, and it is a detail that would completely change the search results. I want to add that for fraud detection specifically, you might want a custom metric that directly optimizes recall at a specific false positive rate threshold — say, recall at 1% FPR — rather than AUC across the entire ROC curve. That aligns the tuner objective with the actual business constraint.

### Peer Response to Scenario B (64 words)

You made a strong case for quantization-aware training, and I agree it is the right technical fix. I want to add one point about the regulatory question that you raised but did not fully resolve: in the US, FDA guidance for AI/ML-based software as a medical device (the 2021 action plan) explicitly addresses algorithm change protocols. A 3.8% sensitivity change would likely trigger a predetermined change control plan review, not necessarily a full re-submission.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post is 175–225 words (counted) | 2 |
| Addresses all parts of the chosen scenario prompt | 3 |
| Demonstrates accurate understanding of optimization concepts from Module 12 | 3 |
| Peer response is 60 or more words and adds substantive new content | 2 |
| **Total** | **10** |

---

## Professor Nash — Discussion Note

Scenario A surfaces the tension between systematic automated search and practical compute constraints that every ML team faces. The "right" answer depends on the specific search space size, the compute budget, and whether the team has strong prior knowledge about good configurations. No single strategy is universally optimal.

Scenario B is one I have thought about carefully — the intersection of quantization, accuracy, and regulated industries is genuinely difficult. The engineering team and the clinical team are both right within their own framing. The question is which framing governs, and in a regulated medical device context, the clinical and regulatory framing must win.

Scenario C reflects a real conversation that happens in many data engineering organizations. The VP's skepticism is not unreasonable — TFX is complex and the ramp-up time is real. Strong responses will acknowledge that cost honestly while making the case based on the specific pain points described, not on a generic argument that "pipelines are better than scripts."

---

*End of Discussion Forum — Module 12*
