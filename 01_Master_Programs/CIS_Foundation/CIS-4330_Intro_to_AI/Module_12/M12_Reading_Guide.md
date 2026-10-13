# Reading Guide: Module 12 — MLOps and AI Solutions Architecture

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4330 &BULL; INTRODUCTION TO ARTIFICIAL INTELLIGENCE</text>
    
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


## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

This reading guide prepares you to engage with the Module 12 lecture and lab by establishing the conceptual foundation for MLOps. You will read selected Microsoft documentation and third-party resources, then complete the guided annotations and reflection prompts. Budget approximately 90 minutes for all readings and responses.

---

## Required Readings

### Reading 1 — Microsoft Learn: What Is Azure Machine Learning?

**URL:** `https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning`

**Focus Areas:**

- The workspace resource hierarchy
- Compute types and when to use each
- The relationship between assets (data, models, environments, components)

**Annotation Prompts — answer in your course notebook:**

1. How does Microsoft define the purpose of the AML workspace?
2. What is the difference between a Compute Instance and a Compute Cluster?
3. List three types of assets you can register in an AML workspace.

---

### Reading 2 — Microsoft Learn: MLOps with Azure Machine Learning

**URL:** `https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment`

**Focus Areas:**

- Model lifecycle stages
- The model registry and versioning
- Deployment strategies (online vs. batch)

**Annotation Prompts:**

1. What metadata does the model registry store for each registered model?
2. Describe one scenario where a batch endpoint is more appropriate than an online endpoint.
3. How does AML support blue-green deployment?

---

### Reading 3 — Microsoft Learn: Monitor Data Drift

**URL:** `https://learn.microsoft.com/en-us/azure/machine-learning/how-to-monitor-datasets`

**Focus Areas:**

- Definition of data drift vs. concept drift
- How the drift monitor is configured
- Alert thresholds and notification options

**Annotation Prompts:**

1. What statistical measures does AML use to detect feature drift?
2. What is a "baseline dataset" in the context of drift monitoring?
3. At what point should a team consider full retraining versus threshold adjustment?

---

### Reading 4 — Microsoft Learn: Azure Machine Learning Pipelines

**URL:** `https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines`

**Focus Areas:**

- Pipeline components and steps
- Input/output data passing between steps
- Caching and reuse of pipeline steps

**Annotation Prompts:**

1. What is the benefit of caching intermediate pipeline steps?
2. How does parameterization enable pipeline reuse?
3. What is the difference between a pipeline component and a pipeline job?

---

## Key Concept Summaries

Read each concept block carefully. These are tested on quizzes and the AI-900 exam.

### MLOps Defined

MLOps (Machine Learning Operations) is the practice of applying DevOps principles to the machine learning lifecycle. It encompasses version control for data, code, and models; automated training and deployment pipelines; continuous monitoring of live predictions; and governance frameworks that ensure compliance and reproducibility.

The goal of MLOps is to reduce the time from model concept to production value while maintaining reliability, security, and fairness.

### The Model Lifecycle

A complete model lifecycle has nine stages:

1. **Business problem framing** — Define success metrics and constraints
2. **Data acquisition** — Source, ingest, and version training data
3. **Data preparation** — Clean, transform, and document feature logic
4. **Experimentation** — Train models, track hyperparameters, compare runs
5. **Evaluation** — Validate accuracy, fairness, and robustness
6. **Registration** — Store the approved model artifact with lineage
7. **Deployment** — Expose the model as an endpoint
8. **Monitoring** — Track prediction quality and data distribution
9. **Retraining** — Update the model when performance degrades

Each stage produces artifacts (datasets, code snapshots, model files, evaluation reports) that must be versioned and stored.

### Azure ML Workspace Components

The AML workspace contains these primary components:

| Component | Purpose |
|---|---|
| Compute | Provisioned virtual machines for training and inference |
| Data Assets | Versioned references to training and evaluation datasets |
| Environments | Conda/Docker specs defining the software stack |
| Jobs | Tracked records of training runs with metrics and artifacts |
| Models | Registered model artifacts with versioning |
| Endpoints | Deployed model services (online or batch) |
| Pipelines | Reusable multi-step workflows |
| Components | Individual reusable pipeline steps |

### Experiment Tracking

Experiment tracking is the practice of logging every training run with enough metadata to reproduce and compare results. In AML, each Job record captures:

- Input parameters and hyperparameters
- Evaluation metrics (accuracy, F1, AUC, loss curves)
- Model artifacts and plots
- Environment snapshot
- Source code snapshot (optional Git integration)
- Duration, compute cost, and resource utilization

Tracking enables data science teams to make evidence-based decisions about model selection rather than relying on memory.

### Deployment Endpoint Types

**Managed Online Endpoint**

- Handles synchronous, real-time HTTP requests
- Client sends a request, endpoint returns a prediction in <500ms typically
- Supports traffic splitting between multiple model versions
- Auto-scales based on request volume
- Best for: web applications, mobile apps, API consumers

**Batch Endpoint**

- Handles asynchronous bulk scoring jobs
- Client submits a dataset job; results written to output storage
- No latency requirement; optimized for throughput
- Supports large input files
- Best for: nightly ETL scoring, compliance reporting, bulk analytics

### Drift Monitoring

**Data Drift:** The statistical distribution of features in live inference data diverges from the distribution in the training data. The model has not changed, but the world has. Example: an e-commerce recommendation model trained before a holiday season encounters purchase patterns that differ significantly from normal months.

**Concept Drift:** The underlying relationship between features and labels changes over time. Example: a spam classifier trained in 2020 fails as spammers adopt new vocabulary and tactics.

**Response Strategies:**

- **Retrain:** Collect fresh labeled data; re-run training pipeline
- **Recalibrate:** Adjust prediction thresholds without full retraining
- **Rollback:** Revert to a prior registry version if a new deployment is the cause

---

## Vocabulary Builder

Define each term in your own words. Use the readings above as your source.

1. MLOps
2. Model registry
3. Pipeline step
4. Compute cluster
5. Managed online endpoint
6. Batch endpoint
7. Data drift
8. Concept drift
9. Feature store
10. Experiment tracking
11. Blue-green deployment
12. AutoML
13. Baseline dataset
14. CI/CD for ML
15. Model lineage

---

## Conceptual Diagrams — Draw These

Complete these two diagrams in your notebook. They will help you on the quiz.

### Diagram 1 — The ML Lifecycle Feedback Loop

Draw a circular flow chart showing the nine lifecycle stages. Add arrows showing:

- The feedback loop from monitoring back to retraining
- The handoff from experimentation to registration
- The handoff from registration to deployment

### Diagram 2 — AML Workspace Resource Hierarchy

Draw a containment diagram showing:

- The workspace as the outer container
- Compute, Data, Models, Experiments, Endpoints, Pipelines as inner resources
- Which resources feed into which (e.g., Data → Experiments → Models → Endpoints)

---

## Reflective Questions

Answer each question in 3–5 sentences. These prepare you for the module discussion and the lab reflection.

**Question 1:** A data science team at a hospital trains a patient readmission prediction model. They achieve 88% accuracy in testing. Six months after deployment, clinicians report the model seems less useful. What MLOps practices, if properly in place, would have caught this problem earlier?

**Question 2:** Why is versioning data as important as versioning code? Give a specific scenario where unversioned data would cause a serious problem.

**Question 3:** A startup says they cannot afford MLOps infrastructure and will just retrain manually when the model breaks. Evaluate this argument. What hidden costs are they likely underestimating?

**Question 4:** Compare online endpoints and batch endpoints. Describe one business scenario that demands online endpoints and one that is well-suited to batch endpoints.

---

## AI-900 Exam Alignment

Module 12 content maps to the following AI-900 exam domain:

**Domain: Describe features of Azure AI services (25–30% of exam)**

Specific objectives:

- Describe capabilities of Azure Machine Learning
- Identify the steps in a machine learning solution
- Describe core machine learning concepts
- Understand deployment and monitoring concepts

**Exam Tip:** The AI-900 does not require you to write code. Focus on *what* each service does and *when* to use it rather than *how* to configure it in detail.

---

## Supplemental Resources (Optional)

The following are not required but strongly recommended for students pursuing the full AI-900 certification or a deeper career in ML engineering:

- **MLOps on Azure GitHub Repository:** `https://github.com/Azure/mlops-v2`
- **MLflow Documentation (open-source tracking):** `https://mlflow.org/docs/latest/index.html`
- **Google's Machine Learning Crash Course — Production ML Systems:** `https://developers.google.com/machine-learning/crash-course/production-ml-systems`
- **"Designing Machine Learning Systems" by Chip Huyen** — Chapter 9 (Continual Learning)

---

## Pre-Lab Checklist

Before starting the Module 12 lab, confirm:

- [ ] You have an active Azure free account or Azure for Students subscription
- [ ] You can access Azure Machine Learning Studio at `ml.azure.com`
- [ ] You have completed Readings 1 and 2 from this guide
- [ ] You have drawn Diagram 2 (workspace hierarchy) in your notebook
- [ ] You have completed vocabulary items 1–8

---

*Reading Guide prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
