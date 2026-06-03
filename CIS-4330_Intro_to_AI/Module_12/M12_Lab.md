# Lab: Module 12 — MLOps and AI Solutions Architecture

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Title:** Building an MLOps Pipeline in Azure Machine Learning Studio

**Estimated Time:** 90–120 minutes

**Skill Level:** Intermediate

**Prerequisites:**

- Azure free account or Azure for Students subscription
- Completed Module 12 Reading Guide (Readings 1–2 at minimum)
- Basic familiarity with Python (reading, not writing from scratch)

**Learning Objectives:**

By completing this lab you will be able to:

1. Create and configure an Azure Machine Learning workspace
2. Register a dataset as a versioned data asset
3. Run a training job and log metrics using the Jobs interface
4. Register a trained model in the model registry
5. Deploy a model to a managed online endpoint
6. Examine an experiment comparison view with multiple runs

---

## Part 1 — Workspace Setup (20 minutes)

### Task 1.1 — Access Azure Machine Learning Studio

1. Open a browser and navigate to `https://portal.azure.com`.
2. Sign in with your Azure account credentials.
3. In the search bar, type **Machine Learning** and select **Azure Machine Learning**.
4. Click **+ Create** and select **New workspace**.
5. Fill in the required fields:

   - **Subscription:** Your student or free subscription
   - **Resource Group:** Create new → name it `rg-cis4330-m12`
   - **Workspace name:** `ws-cis4330-m12-[your initials]`
   - **Region:** East US (or your nearest region)

6. Leave all other settings at defaults and click **Review + Create**, then **Create**.
7. Wait for deployment to complete (approximately 3–5 minutes).
8. Click **Go to resource**, then click **Launch studio**.

**Checkpoint 1.1:** You are now in Azure Machine Learning Studio. Take a screenshot of the Studio home page showing your workspace name in the top-left corner.

---

### Task 1.2 — Explore the Studio Interface

Navigate to each of the following sections in the left sidebar and note what each contains:

- **Notebooks** — Describe what you see in 1 sentence.
- **Data** — Describe what you see in 1 sentence.
- **Jobs** — Describe what you see in 1 sentence.
- **Models** — Describe what you see in 1 sentence.
- **Endpoints** — Describe what you see in 1 sentence.

Record your five descriptions in your lab notebook. These will appear in your lab report.

---

## Part 2 — Dataset Registration (15 minutes)

### Task 2.1 — Upload and Register Training Data

We will use the classic Diabetes dataset for this lab.

1. In Studio, click **Data** in the left sidebar.
2. Click **+ Create**.
3. Select **Data type: File**.
4. Name the asset: `diabetes-training-m12`
5. Version: `1`
6. Under **Data source**, select **From local files**.
7. Download the sample dataset:

   - Navigate to: `https://raw.githubusercontent.com/MicrosoftLearning/mslearn-azure-ml/main/Labs/02/data/diabetes.csv`
   - Save the file as `diabetes.csv` on your local machine.

8. Upload `diabetes.csv` using the Studio upload interface.
9. Click **Next** through the schema review steps, accepting defaults.
10. Click **Create**.

**Checkpoint 2.1:** Navigate back to the Data section. Confirm `diabetes-training-m12` version 1 appears in the list. Screenshot the data asset details page.

---

## Part 3 — Experiment Tracking (30 minutes)

### Task 3.1 — Create a Compute Instance

1. In the left sidebar, click **Compute**.
2. Click the **Compute instances** tab.
3. Click **+ New**.
4. Configure the instance:

   - **Name:** `ci-m12-[your initials]`
   - **Virtual machine type:** CPU
   - **Virtual machine size:** Standard_DS11_v2 (2 cores, 14 GB RAM)

5. Click **Create** and wait for the instance to start (3–5 minutes).

### Task 3.2 — Open a Notebook and Run a Training Job

1. Once the compute instance is running, click **Notebooks** in the left sidebar.
2. Click the **+** icon to create a new notebook.
3. Name it `m12_training.ipynb`.
4. Select your compute instance as the kernel.
5. In the first cell, paste and run the following code:

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import mlflow

# Connect to workspace
ml_client = MLClient.from_config(credential=DefaultAzureCredential())

# Set experiment name
mlflow.set_experiment("diabetes-experiment-m12")

# Load data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
import numpy as np

data = pd.read_csv("diabetes.csv")
X = data.drop("Diabetic", axis=1)
y = data["Diabetic"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Run 1 — default regularization
with mlflow.start_run(run_name="run-C1.0"):
    C = 1.0
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])
    mlflow.log_param("C", C)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("auc", auc)
    print(f"Run 1 — C={C}: Accuracy={acc:.4f}, AUC={auc:.4f}")

# Run 2 — higher regularization
with mlflow.start_run(run_name="run-C0.1"):
    C = 0.1
    model2 = LogisticRegression(C=C, max_iter=1000)
    model2.fit(X_train, y_train)
    preds2 = model2.predict(X_test)
    acc2 = accuracy_score(y_test, preds2)
    auc2 = roc_auc_score(y_test, model2.predict_proba(X_test)[:,1])
    mlflow.log_param("C", C)
    mlflow.log_metric("accuracy", acc2)
    mlflow.log_metric("auc", auc2)
    print(f"Run 2 — C={C}: Accuracy={acc2:.4f}, AUC={auc2:.4f}")
```

6. Execute the cell and wait for both runs to complete.

**Checkpoint 3.2:** Record the accuracy and AUC values for both runs in your lab notebook.

### Task 3.3 — Compare Runs in Studio

1. Navigate to **Jobs** in the left sidebar.
2. Find the experiment `diabetes-experiment-m12`.
3. Select both runs using the checkboxes.
4. Click **Compare**.
5. In the comparison view, examine the parameter table and metrics table.

**Lab Question 1:** Which run achieved higher AUC? What does the difference in the C parameter mean for model complexity?

**Checkpoint 3.3:** Screenshot the run comparison view showing both runs' accuracy and AUC values.

---

## Part 4 — Model Registration (10 minutes)

### Task 4.1 — Register the Best Model

1. Return to the Jobs view and click on the run with the higher AUC.
2. In the run detail page, click the **Outputs + logs** tab.
3. Locate the model artifact folder.
4. Click **Register model**.
5. Configure the registration:

   - **Name:** `diabetes-classifier-m12`
   - **Version:** `1`
   - **Description:** `Logistic regression diabetes classifier — M12 lab`

6. Click **Register**.

**Checkpoint 4.1:** Navigate to **Models** in the sidebar. Confirm `diabetes-classifier-m12` version 1 is listed. Screenshot the model details page showing the training job lineage.

**Lab Question 2:** Why is tracking the training job lineage (which job produced a registered model) important for a production system?

---

## Part 5 — Endpoint Deployment (20 minutes)

### Task 5.1 — Deploy to a Managed Online Endpoint

1. In the **Models** view, click on `diabetes-classifier-m12` version 1.
2. Click **Deploy** → **Real-time endpoint**.
3. Configure the endpoint:

   - **Endpoint name:** `ep-diabetes-m12-[your initials]`
   - **Deployment name:** `blue`
   - **Virtual machine:** Standard_DS2_v2
   - **Instance count:** 1

4. Click **Deploy** and wait for the endpoint to become active (5–10 minutes).

**Checkpoint 5.1:** Navigate to **Endpoints** → find your endpoint → confirm status is **Succeeded**. Screenshot the endpoint page.

### Task 5.2 — Test the Endpoint

1. On the endpoint detail page, click the **Test** tab.
2. Paste the following sample input:

```json
{
  "input_data": {
    "columns": ["Pregnancies","PlasmaGlucose","DiastolicBloodPressure",
                 "TricepsThickness","SerumInsulin","BMI",
                 "DiabetesPedigree","Age"],
    "data": [[6, 148, 72, 35, 0, 33.6, 0.627, 50]]
  }
}
```

3. Click **Test** and record the prediction output.

**Lab Question 3:** What did the model predict? Does this align with a patient who has multiple diabetes risk factors?

**Checkpoint 5.2:** Screenshot the test panel showing the input payload and the prediction response.

---

## Part 6 — Reflection and Cleanup (10 minutes)

### Task 6.1 — Lab Reflection Questions

Answer the following in your lab report (minimum 3 sentences each):

**Reflection 1:** Describe the flow of data and artifacts from dataset registration through endpoint deployment. Which step did you find most technically interesting and why?

**Reflection 2:** In this lab you ran two training experiments with different hyperparameters. How would this process scale if you needed to try 50 hyperparameter combinations? What AML feature would help?

**Reflection 3:** If this were a production hospital system predicting patient readmission rather than a training exercise, what additional steps would you require before allowing the model to be deployed to a live endpoint?

### Task 6.2 — Resource Cleanup

To avoid incurring charges on your Azure account:

1. Navigate to **Compute** → **Compute instances** → Stop your compute instance.
2. Navigate to **Endpoints** → Select your endpoint → Click **Delete**.
3. Optionally, delete the resource group `rg-cis4330-m12` from the Azure Portal to remove all resources.

---

## Lab Submission Requirements

Submit a single PDF document containing:

1. **Cover page:** Name, date, course, module number
2. **All checkpoints:** Screenshots labeled Checkpoint 1.1, 2.1, 3.2, 3.3, 4.1, 5.1, 5.2
3. **Lab Questions 1–3:** Written responses (minimum 3 sentences each)
4. **Reflection Questions 1–3:** Written responses (minimum 3 sentences each)
5. **Task 1.2 descriptions:** Five one-sentence descriptions of Studio sections

**Grading Rubric:**

| Component | Points |
|---|---|
| All 7 screenshots present and labeled | 30 |
| Lab Questions 1–3 answered correctly | 30 |
| Reflection Questions 1–3 show depth | 30 |
| Task 1.2 descriptions accurate | 10 |
| **Total** | **100** |

---

*Lab prepared by Professor Nash | Texas Wesleyan University | CIS-4330*
