# Quiz: Module 12 — MLOps and AI Solutions Architecture

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. The quiz is closed-book and should be completed in 20 minutes.

---

## Questions

**Question 1**

A data science team trained a fraud detection model six months ago. The model's accuracy on production data has gradually declined even though the model code has not changed. What is the most likely explanation?

A. The model was deployed to the wrong endpoint type.

B. The model registry was not updated after training.

C. Concept drift has occurred as fraud patterns have changed over time.

D. The compute cluster is undersized for the prediction volume.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Endpoint type (online vs. batch) affects latency and throughput, not model accuracy.
- **B** is incorrect. Registry updates affect versioning metadata, not prediction quality.
- **C** is correct. Concept drift occurs when the relationship between features and labels changes over time — exactly what happens as fraudsters adapt tactics.
- **D** is incorrect. Compute sizing affects latency and cost, not model prediction accuracy.

---

**Question 2**

Which Azure Machine Learning component is the handoff point between the experimentation phase and the deployment phase?

A. Compute cluster

B. Managed online endpoint

C. Model registry

D. AutoML experiment

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Compute clusters are infrastructure resources used during training, not the handoff point.
- **B** is incorrect. Endpoints are the output of deployment, not the handoff point between experimentation and deployment.
- **C** is correct. The model registry stores versioned, approved model artifacts. Only models in the registry can be deployed to endpoints.
- **D** is incorrect. AutoML experiments are part of the experimentation phase, not the handoff mechanism.

---

**Question 3**

A retail company needs to score 10 million customer records every night to generate personalized recommendations for the next business day. Which Azure ML deployment option is most appropriate?

A. Managed online endpoint with auto-scaling

B. Batch endpoint with scheduled trigger

C. Compute instance running a manual notebook

D. Designer pipeline with drag-and-drop export

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Online endpoints are designed for real-time, low-latency individual requests, not bulk nightly scoring.
- **B** is correct. Batch endpoints process large volumes asynchronously and are ideal for scheduled, high-throughput scoring jobs.
- **C** is incorrect. Manual notebooks are not production-grade, not scalable, and not reliable for overnight automation.
- **D** is incorrect. Designer pipelines are used for training workflow, not production inference scheduling.

---

**Question 4**

In Azure Machine Learning, a team notices that the input features being sent to their production model have a different statistical distribution than the features in the original training dataset. What type of issue is this?

A. Model overfitting

B. Data drift

C. Concept drift

D. Pipeline failure

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Overfitting is a training-time phenomenon where the model learns noise in the training data. It is not a production monitoring concept.
- **B** is correct. Data drift refers specifically to changes in the statistical distribution of input features in live data compared to the training baseline.
- **C** is incorrect. Concept drift is when the relationship between inputs and correct outputs changes, not the input distribution itself.
- **D** is incorrect. Pipeline failure is an infrastructure/execution issue, not a model quality issue.

---

**Question 5**

What does Automated ML (AutoML) in Azure Machine Learning automate?

A. The deployment of models to production endpoints without human approval

B. The selection of algorithms and hyperparameters to find the best-performing model within defined constraints

C. The monitoring of data drift and automatic retraining of models

D. The creation of data assets and the registration of datasets

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. AutoML does not automatically deploy to production. Human review and approval are still required.
- **B** is correct. AutoML automates the search over algorithms and hyperparameter values, returning the best model found within the time budget and constraints defined by the user.
- **C** is incorrect. Drift monitoring and retraining triggers are separate AML features (Data Drift Monitor, Event Grid triggers), not AutoML.
- **D** is incorrect. Data asset registration is a manual or scripted operation in the Data section, unrelated to AutoML.

---

**Question 6**

A machine learning pipeline in Azure ML has five steps. Steps 1 and 2 process data and have not changed since the last run. Steps 3 through 5 involve new training code. What happens when the pipeline is rerun?

A. All five steps are rerun from scratch to ensure consistency.

B. Steps 1 and 2 use cached outputs; steps 3 through 5 rerun with the new code.

C. Steps 3 through 5 are skipped because they contain changed code.

D. The pipeline fails unless all steps are re-executed.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. AML pipeline step caching is explicitly designed to avoid rerunning unchanged steps.
- **B** is correct. AML caches step outputs when the step code, parameters, and inputs have not changed. Downstream steps with changes are rerun from that point forward.
- **C** is incorrect. Changed steps are the ones that *must* rerun, not skip.
- **D** is incorrect. Pipelines support partial reruns by design; failure to cache unchanged steps would not cause a pipeline error.

---

**Question 7**

Which of the following best describes the purpose of experiment tracking in a machine learning workflow?

A. It encrypts model artifacts before they are stored in the model registry.

B. It automatically deploys the highest-accuracy model to a production endpoint.

C. It records parameters, metrics, artifacts, and environment details for each training run to enable comparison and reproducibility.

D. It monitors live prediction requests for data drift and triggers retraining alerts.

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Encryption of artifacts is handled by Azure storage and Key Vault, not experiment tracking.
- **B** is incorrect. Automatic deployment is a CI/CD pipeline feature and requires human approval gates, not a function of experiment tracking.
- **C** is correct. Experiment tracking creates a complete audit trail of every training run, enabling teams to compare results, reproduce experiments, and make evidence-based model selection decisions.
- **D** is incorrect. Drift monitoring of live predictions is handled by the Data Drift Monitor feature, not experiment tracking.

---

**Question 8**

A company needs to roll out a new model version but wants to route only 10% of production traffic to it initially while monitoring for quality issues. What deployment feature supports this?

A. Batch endpoint job queuing

B. Traffic splitting between deployments in a managed online endpoint

C. Model registry versioning with approval workflows

D. AutoML ensemble models

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Batch endpoints handle bulk asynchronous jobs, not percentage-based real-time traffic routing.
- **B** is correct. Managed online endpoints support multiple named deployments (e.g., blue and green) with configurable traffic weights. This enables gradual rollout and canary deployment patterns.
- **C** is incorrect. Model registry versioning manages the store of approved models but does not control live traffic routing.
- **D** is incorrect. AutoML ensembles combine multiple models into one — they are a training technique, not a deployment routing feature.

---

**Question 9**

Which MLOps maturity level involves fully automated CI/CD pipelines where a code commit automatically triggers retraining, evaluation, and deployment with approval gates?

A. Level 0

B. Level 1

C. Level 2

D. Level 3

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Level 0 is the manual level — notebooks, manual deployment, no automation.
- **B** is incorrect. Level 1 introduces automated training pipelines and model registries but not full CI/CD.
- **C** is correct. Level 2 represents full CI/CD for ML: code commits trigger end-to-end automated workflows with human-in-the-loop approval gates before production deployment.
- **D** is incorrect. Microsoft's MLOps maturity model defines three levels (0, 1, 2). Level 3 is not a defined tier in this framework.

---

**Question 10**

A Gartner survey found that fewer than 54% of AI models ever make it to production. Which statement best explains why MLOps practices help close this gap?

A. MLOps replaces the need for data scientists by automating all model training.

B. MLOps provides automation, governance, and monitoring that reduce the friction between experimentation and production deployment.

C. MLOps guarantees that models trained on historical data will perform accurately on future data.

D. MLOps eliminates the need for model evaluation by automatically approving high-accuracy models.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. MLOps augments data scientists with better tooling; it does not replace them. Human expertise remains essential for problem framing, feature engineering, and evaluation.
- **B** is correct. The primary value of MLOps is closing the gap between experimental model development and reliable production systems through automation, versioning, governance, and continuous monitoring.
- **C** is incorrect. No framework guarantees future accuracy. Drift monitoring and retraining exist precisely because models degrade over time.
- **D** is incorrect. MLOps strengthens evaluation gates; it does not bypass them. Approving models without evaluation would increase production risk, not reduce it.

---

*Quiz prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
