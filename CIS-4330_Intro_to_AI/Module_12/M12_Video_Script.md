# Video Script: Module 12 — MLOps and AI Solutions Architecture

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Slide Deck:** M12_Slides.pptx
- **Screen Recording:** Azure Machine Learning Studio live demo
- **Tone:** Conversational, professional; use real-world analogies

---

## SEGMENT 1 — Hook and Module Overview (Slides 1–3) [3 min]

[ON CAMERA]

Welcome back, everyone. I want to start today with a question — have you ever wondered what happens *after* a machine learning model is built? In most courses, we train a model, look at the accuracy, and call it done. But in the real world, that's maybe 20% of the actual work.

The other 80% is getting that model deployed, monitored, updated, and governed reliably at scale. That discipline has a name: **MLOps**.

[SLIDE 1: Title Slide — "MLOps and AI Solutions Architecture"]

Today is Module 12, and it is one of the most practically important modules in this course. If you are planning any kind of career in AI, data science, cloud architecture, or even IT management, what we cover today will show up in your interviews and your day-to-day work.

[SLIDE 2: Module Learning Objectives]

By the end of this module you will be able to:

- Define MLOps and explain the full model lifecycle
- Navigate the Azure Machine Learning workspace
- Describe pipelines, experiment tracking, and model registries
- Explain deployment endpoints and their tradeoffs
- Describe monitoring for model drift and data drift

[SLIDE 3: Why MLOps Matters — Stat Card]

A 2023 survey by Gartner found that fewer than 54% of AI models ever make it to production. Of those that do, a significant percentage degrade in accuracy within six months without active monitoring. MLOps is the practice that closes that gap.

---

## SEGMENT 2 — What Is MLOps? (Slides 4–8) [5 min]

[SLIDE 4: DevOps → DataOps → MLOps]

If you have a software development background, you already know DevOps — the combination of development and operations practices designed to shorten the software delivery lifecycle. MLOps applies the same philosophy to machine learning: continuous integration, continuous delivery, and continuous monitoring, but adapted for the unique challenges of data-driven systems.

[SLIDE 5: The Three Pillars of MLOps]

MLOps rests on three pillars.

The first pillar is **Reproducibility** — given the same data and the same code, you should always get the same model. This sounds obvious, but it is surprisingly hard when experiments involve randomness, package version drift, and untracked data snapshots.

The second pillar is **Automation** — training, testing, validation, and deployment pipelines that run with minimal human intervention so you can push new model versions quickly and safely.

The third pillar is **Governance** — audit trails, access controls, lineage tracking, and documentation so you always know which model is running in production, who approved it, and what data it was trained on.

[SLIDE 6: The ML Lifecycle — Diagram]

Let's walk through the end-to-end lifecycle.

**Step 1 — Problem Framing**: What business problem are we solving? What does success look like quantitatively?

**Step 2 — Data Acquisition and Preparation**: Source data, clean it, version it, register it.

**Step 3 — Feature Engineering**: Transform raw data into model-ready features. Document every transformation.

**Step 4 — Model Training and Experimentation**: Run experiments, track hyperparameters, log metrics.

**Step 5 — Model Evaluation and Validation**: Compare against baseline. Validate on held-out test sets. Check for bias.

**Step 6 — Model Registration**: Store the approved model artifact with metadata.

**Step 7 — Deployment**: Package and expose the model as an endpoint.

**Step 8 — Monitoring**: Watch prediction quality, data distribution, and infrastructure health.

**Step 9 — Retraining Trigger**: When drift is detected or a schedule fires, loop back to Step 3 or Step 4.

[SLIDE 7: MLOps Maturity Levels]

Microsoft defines MLOps maturity across three levels. Level 0 is manual — data scientists run notebooks, deploy manually, no versioning. Level 1 introduces automated training pipelines and model registries. Level 2 is full CI/CD for ML — code commits trigger automated retraining, evaluation, and deployment with human-in-the-loop approval gates.

Most organizations are at Level 0 or early Level 1. Reaching Level 2 is a multi-year journey.

[SLIDE 8: MLOps vs Traditional Software — Key Difference]

Here is the key difference from traditional software: in regular software, if the code does not change, the behavior does not change. In ML, the *world changes*, so the behavior changes even if the code is identical. A fraud detection model trained on 2022 patterns will drift as fraudsters adapt. A demand-forecasting model trained pre-pandemic will fail post-pandemic. Monitoring is not optional.

---

## SEGMENT 3 — Azure Machine Learning Workspace (Slides 9–14) [7 min]

[SLIDE 9: AML Workspace — What It Is]

Azure Machine Learning is Microsoft's end-to-end MLOps platform. The **workspace** is the top-level resource — think of it as a project folder in the cloud that contains everything: your compute, your data, your experiments, your models, and your endpoints.

[SCREEN RECORDING — DEMO START]

Let me open Azure Machine Learning Studio and walk you through the key areas.

[NARRATE OVER SCREEN: Navigate to ml.azure.com]

When you first log in, you land on the Studio home page. On the left sidebar you can see the main sections: Notebooks, Automated ML, Designer, Data, Jobs, Components, Pipelines, Environments, Models, Endpoints, and Monitoring.

[SLIDE 10: Core Workspace Components]

Let me break down the most important components.

**Compute** — This is where you provision the machines that run your training jobs. You have Compute Instances, which are personal dev VMs, and Compute Clusters, which are auto-scaling pools for training. For inference, you have Inference Clusters and Managed Online Endpoints.

**Data Assets** — AML stores references to datasets with versioning. You register a dataset once and reference it by name and version number in every experiment.

**Environments** — Conda or Docker specifications that define the Python packages available during training. Versioned so every job is reproducible.

**Jobs (Experiments)** — Every training run is logged as a Job. Jobs belong to an experiment group. Each job records parameters, metrics, artifacts, and logs.

[SLIDE 11: The Designer — Low-Code Pipeline Builder]

For students new to ML, the **Designer** is a drag-and-drop pipeline builder. You can build a complete training pipeline without writing a single line of code — drag a dataset node, connect it to a data transformation module, connect that to a training module, and connect to an evaluation module.

[SCREEN RECORDING — DEMO: Show Designer canvas briefly]

The Designer generates YAML pipeline definitions under the hood, which means anything you build visually can be exported and automated later.

[SLIDE 12: Automated ML — AutoML]

**Automated ML** takes a dataset and a target column and automatically tries hundreds of model algorithms and hyperparameter combinations, selecting the best performer. For classification, regression, and time-series forecasting, AutoML is often the fastest path to a production baseline.

Important for the AI-900 exam: AutoML does not guarantee the best possible model. It guarantees the best model found within the time and budget you specify.

[SLIDE 13: Compute Targets — Choosing the Right One]

Choosing compute is an architectural decision.

- **Compute Instance**: Single-node, always-on, great for development notebooks.
- **Compute Cluster**: Multi-node, auto-scales to zero when idle, best for training large models or running parallel experiments.
- **Serverless Compute**: Managed by Azure, no cluster to provision, pay-per-second, launched in 2023.
- **Attached Compute**: Bring your own cluster — Databricks, Synapse, on-premises.

[SLIDE 14: AML Integration with Azure Ecosystem]

AML does not live in isolation. It integrates with Azure Data Factory for data orchestration, Azure DevOps for CI/CD pipelines, GitHub Actions for automated retraining, Azure Key Vault for secrets management, and Azure Monitor for operational telemetry.

---

## SEGMENT 4 — Pipelines, Experiment Tracking, and Model Registry (Slides 15–19) [6 min]

[SLIDE 15: What Is a Pipeline?]

An AML pipeline is a reusable, parameterized workflow composed of steps. Each step runs a specific task — data prep, feature engineering, training, evaluation — on its own compute with its own environment. Steps are connected by data dependencies. Change the data or parameters, rerun the pipeline, and only the affected steps re-execute — upstream cached steps are skipped.

[SLIDE 16: Pipeline YAML — Code View]

[SHOW CODE SNIPPET ON SLIDE]

In code, a pipeline is defined in YAML. You specify inputs, outputs, and a sequence of component steps. Each component is a self-contained piece of code registered in the component registry. This separation of concerns means your data scientists write training logic, your ML engineers write pipeline orchestration, and the two never step on each other.

[SLIDE 17: Experiment Tracking — Why It Matters]

Every ML project involves dozens or hundreds of training runs with different hyperparameters. Without tracking, you lose the ability to reproduce a result or understand why one configuration outperformed another.

AML experiment tracking logs:

- Run parameters and hyperparameters
- Evaluation metrics per epoch or step
- Artifacts — model files, confusion matrices, ROC curves
- Environment snapshots
- Tags for grouping and filtering

[SLIDE 18: Comparing Runs in the Jobs UI]

[SCREEN RECORDING — DEMO: Show Jobs tab, select two runs, open comparison view]

In the Studio Jobs view, you can select multiple runs and open a comparison panel. This shows a side-by-side table of all logged parameters and metrics. You can also plot metrics over time — for instance, validation loss curves for two runs on the same chart.

This is how you justify your model selection to a stakeholder: "We ran 47 experiments. Here is the best run, and here is what made it different."

[SLIDE 19: The Model Registry]

After training, a model artifact — the serialized model files — is registered in the **Model Registry**. Each registration creates a versioned entry with:

- Model name and version number
- Training job lineage (which job produced it)
- Metrics snapshot
- Custom tags (environment, approval status, owner)
- Input dataset references

The registry is the handoff point between experimentation and deployment. Only models that pass evaluation gates are promoted to the registry. Only models in the registry can be deployed to endpoints.

---

## SEGMENT 5 — Deployment Endpoints (Slides 20–23) [5 min]

[SLIDE 20: From Registry to Endpoint]

Deployment means taking a registered model and exposing it as a web service that can receive inference requests. Azure ML supports two primary endpoint types.

[SLIDE 21: Online Endpoints — Real-Time Inference]

**Managed Online Endpoints** handle real-time, low-latency inference. When a client sends a JSON payload, the endpoint returns a prediction in milliseconds. These are backed by managed Kubernetes clusters. You specify CPU/memory per instance, instance count, and autoscaling rules.

Blue-green deployment is supported natively: traffic can be split across multiple model versions (deployments) within a single endpoint. You can route 90% to the current stable model and 10% to a new candidate — monitor quality — then shift traffic gradually.

[SLIDE 22: Batch Endpoints — Offline Scoring]

**Batch Endpoints** process large volumes of data asynchronously. You submit a job with an input dataset, it scores all records, and writes outputs to storage. No latency requirement. Ideal for nightly scoring jobs, bulk predictions, and compliance reporting.

[SLIDE 23: Endpoint Monitoring and Logging]

Once deployed, every request and response can be logged to Azure Blob Storage or Azure Monitor. This feeds the monitoring pipeline. You can also enable **Application Insights** integration to get request latency percentiles, error rates, and custom telemetry dashboards out of the box.

---

## SEGMENT 6 — Monitoring Model Drift (Slides 24–27) [4 min]

[SLIDE 24: What Is Drift?]

Drift is the gradual degradation of model performance over time. There are two types.

**Data Drift** occurs when the statistical distribution of input features shifts. The model receives data that looks different from its training set. For example, a customer churn model trained in 2021 encounters new product categories introduced in 2023 — the feature distribution has changed.

**Concept Drift** occurs when the relationship between inputs and the correct output changes. A credit scoring model trained before an economic recession may have learned different default patterns than what holds true post-recession.

[SLIDE 25: Azure ML Data Drift Monitor]

AML provides a built-in **Data Drift Monitor** that continuously compares the distribution of live inference data against a registered baseline dataset. It computes drift scores per feature using statistical tests. When drift exceeds a configured threshold, it triggers alerts via Azure Monitor or email.

[SLIDE 26: Responding to Drift]

When drift is detected, you have three options:

1. **Retrain on fresh data** — collect recent labeled examples and run the training pipeline.
2. **Adjust the model threshold** — for classification models, recalibrate the decision threshold without full retraining.
3. **Rollback** — if a newly deployed model is the drift source, use the registry to roll back to the previous version.

[SLIDE 27: Responsible AI and Monitoring]

Monitoring is also a responsible AI practice. Fairness metrics — error rates across demographic groups — should be monitored alongside accuracy metrics. A model that starts out fair can drift into biased behavior if the data distribution changes asymmetrically across groups.

---

## SEGMENT 7 — Summary and Exam Tips (Slides 28–30) [2 min]

[SLIDE 28: Module 12 Summary]

Today we covered the full MLOps story: the model lifecycle, the Azure Machine Learning workspace, pipelines, experiment tracking, the model registry, deployment endpoints, and drift monitoring.

[SLIDE 29: AI-900 Key Takeaways]

For the AI-900 exam, focus on these facts:

- AML workspace is the central resource for all ML operations in Azure
- AutoML automates algorithm and hyperparameter selection
- Online endpoints = real-time; batch endpoints = asynchronous bulk
- Data drift = distribution shift in inputs; concept drift = relationship shift
- Model registry is the handoff point between training and deployment

[SLIDE 30: Next Module Preview]

In Module 13 we shift from the technical to the strategic: AI Applications in Business. We will look at industry-specific use cases, how companies calculate AI ROI, and how to manage AI projects effectively.

Complete the Module 12 lab in Azure Machine Learning Studio this week. The reading guide covers the MLOps whitepaper and I want you to reference the real documentation. See you in Module 13.

[END OF VIDEO]

---

*Script prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
