# Discussion Forum: Module 14 — Model Deployment and Production ML Pipelines

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Overview

This discussion has three scenarios focused on deployment decisions. Respond to **one** scenario with an original post of 175–225 words, then provide **two peer responses** of 75–100 words each. Peer responses must add new analysis, counterarguments, or concrete examples beyond what the original post stated.

**Due dates:** Original post by Wednesday 11:59 PM; peer responses by Sunday 11:59 PM.

---

## Scenario A — The Right Tool for the Job

A startup is launching a plant disease detection app for farmers in rural India. The app uses a CNN trained on 50,000 labeled crop images to classify 12 disease types from phone camera photos. Most target users have low-end Android phones and unreliable internet connectivity. The engineering team is debating between three deployment options: (1) a Flask server in the cloud that receives photos and returns predictions, (2) a TFLite model bundled directly in the Android APK, and (3) a TensorFlow Serving cluster behind a load balancer.

Argue which deployment option is most appropriate for this specific use case. Address all three options, explaining why the chosen approach solves the connectivity and device constraint problems and why the other two fall short. What quantization strategy would you apply to the TFLite model, and what accuracy tradeoff would you monitor?

**Sample response (for instructor reference — do not post):**

Option 2, TFLite bundled in the APK, is clearly the correct choice for this use case. Rural India connectivity is unreliable — a cloud Flask server or TF Serving cluster would be unusable during network outages, which is precisely when farmers need offline diagnostics. Bundling the model into the APK enables fully offline inference: the farmer takes a photo, and the classification happens on-device in milliseconds. The Flask server fails on both connectivity and latency grounds; the TF Serving cluster adds infrastructure complexity and cost with no benefit over Flask for this traffic profile. For quantization, I would apply dynamic range quantization first (4x size reduction, minimal accuracy loss) and measure accuracy on a held-out test set from the same distribution as target devices. If accuracy degradation exceeds 1–2%, I would investigate full integer quantization with a representative calibration dataset from actual field images. The key metric to monitor is per-class accuracy across all 12 disease types — some rare diseases may be disproportionately affected by quantization noise.

---

## Scenario B — SavedModel Versioning and Zero-Downtime Updates

A retail company runs a product recommendation engine as a TensorFlow Serving deployment. The current model (version 3) has been live for two months. The ML team trained an improved model (version 4) that achieves 8% better click-through rate in offline evaluation. The DevOps engineer wants to simply replace version 3 with version 4 and restart the container. The ML engineer argues this approach is risky and proposes a blue/green deployment using TF Serving's versioning capabilities.

Explain how TF Serving's model versioning system works. Describe the specific risk the ML engineer is worried about, and explain what a blue/green or canary deployment strategy looks like using TF Serving. What metrics would you monitor during the rollout to decide whether version 4 is safe to promote fully?

**Sample response (for instructor reference — do not post):**

TF Serving automatically discovers and serves the highest-numbered SavedModel version in the model directory. When you copy version 4 alongside version 3, TF Serving loads it while keeping version 3 in memory during a configurable grace period. The DevOps engineer's approach — replacing and restarting — creates a brief outage window and offers no rollback path if version 4 performs poorly in production. The ML engineer is right to be cautious: offline evaluation (click-through rate on historical data) does not always predict live production behavior. A canary strategy would route 5–10% of live traffic to version 4 via a load balancer or API gateway while version 3 handles the remainder. You monitor real-time metrics: click-through rate, revenue per session, latency, and error rate. If version 4's live metrics match or exceed offline predictions after 24–48 hours, promote it to 100% traffic. If any metric degrades, roll back by pointing the load balancer back to version 3, which is still loaded and warm. TF Serving's grace period configuration (keep_latest_versions policy) ensures both versions remain in memory during the canary window.

---

## Scenario C — When TFX Is and Is Not Worth It

A hospital radiology department is building a chest X-ray triage model that flags potential pneumonia cases for urgent radiologist review. The model will be trained on 80,000 labeled X-rays and retrained quarterly as new labeled cases accumulate. A junior ML engineer argues that TFX is overkill — the team can just run a Colab notebook quarterly, check accuracy, and manually push the SavedModel to TF Serving. The senior ML engineer disagrees, citing regulatory compliance and patient safety requirements.

Take a position on whether TFX is appropriate for this specific deployment. Consider: what happens if a quarterly retrain accidentally ingests corrupted or mislabeled data? What does the audit trail requirement look like for FDA-regulated medical AI? Conversely, if you agree TFX is appropriate, are there components you would prioritize implementing first, and which could be deferred?

**Sample response (for instructor reference — do not post):**

TFX is not optional here — it is essential. The manual Colab notebook approach the junior engineer proposes has no safeguards against data corruption. If a batch of mislabeled X-rays enters the training data during a quarterly retrain, there is no automated mechanism to detect the anomaly before the bad model reaches production. In a hospital context, a degraded triage model could delay care for pneumonia patients — a patient safety failure. The senior engineer is correct on regulatory grounds as well: FDA guidance on Software as a Medical Device (SaMD) requires complete version control, data lineage, and validation records. The MLMD store in TFX provides exactly this audit trail. I would prioritize four components first: ExampleGen and ExampleValidator to catch data anomalies before training begins, Trainer for reproducible versioned training runs, and Evaluator to automatically gate model promotion based on performance thresholds versus the deployed baseline. SchemaGen and Transform can be phased in as the team becomes comfortable with the platform. The junior engineer's concern about overhead is legitimate — TFX has a steep learning curve — but in a regulated medical AI context, that overhead is the minimum bar for responsible deployment.

---

## Peer Response Guidelines

Strong peer responses will do at least one of the following:

- Raise a deployment constraint the original post did not address (cost, latency SLA, team size)
- Provide a specific counterexample or edge case
- Reference a specific TF Serving, TFLite, or TFX feature that supports or challenges a claim
- Connect the scenario to a real industry deployment decision

Peer responses that only paraphrase or affirm the original without adding substance receive 0 points on the Peer Response criterion.

---

## Grading Rubric (10 points total)

| Criterion | Points |
|-----------|--------|
| Original post addresses the scenario directly | 2 |
| Technical accuracy of deployment claims | 2 |
| Depth of reasoning — considers tradeoffs | 2 |
| Word count within 175–225 range | 1 |
| Peer response 1 — substantive addition | 1.5 |
| Peer response 2 — substantive addition | 1.5 |
| **Total** | **10** |
