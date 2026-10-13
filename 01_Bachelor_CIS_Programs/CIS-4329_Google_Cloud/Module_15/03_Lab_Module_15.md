# Lab Activity: Module 15 — GCP Cost Management and Billing Controls

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 90–120 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

In this lab you will implement GCP cost management controls hands-on: configure a billing export to BigQuery, create a budget with alert thresholds and a Pub/Sub notification, query billing data using SQL, review Recommender suggestions, and configure Object Lifecycle Management on a Cloud Storage bucket. You will also design a programmatic cost cap using the Cloud Function + billing disable pattern.

---

### Learning Objectives

By completing this lab you will be able to:

- Enable and configure Cloud Billing export to BigQuery
- Create a budget with multiple alert thresholds and a Pub/Sub notification
- Query the BigQuery billing dataset to analyze costs by service and label
- Access and interpret VM Rightsizing Recommender output
- Configure Object Lifecycle Management on a Cloud Storage bucket
- Describe the Pub/Sub → Cloud Function → billing disable programmatic cost cap pattern

---

### Prerequisites

- A GCP project with billing enabled
- Owner or Editor role on the project
- `gcloud` CLI installed and authenticated
- A billing account you have access to (billing.admin or billing.viewer role)

---

### Part 1: Enable Billing Export to BigQuery (20 minutes)

#### Task 1.1 — Create a BigQuery dataset for billing data

```bash
# Set your project ID
export PROJECT_ID=$(gcloud config get-value project)

# Create the BigQuery dataset
bq mk \
  --dataset \
  --location=US \
  --description="GCP Billing export dataset" \
  ${PROJECT_ID}:billing_export
```

Verify the dataset was created:

```bash
bq ls --datasets ${PROJECT_ID}
```

#### Task 1.2 — Enable billing export in Cloud Console

Billing export cannot be enabled via gcloud CLI — it requires the Cloud Console.

1. Navigate to Cloud Console → Billing → Billing Export
2. Select the BigQuery export tab
3. Click "Edit Settings"
4. Select your project and the `billing_export` dataset you just created
5. Click Save

Billing data will begin populating within 24 hours. For this lab, your instructor may provide a pre-populated billing dataset to query, or you can use the sample queries against the schema.

#### Task 1.3 — Verify export configuration

```bash
# View billing account information
gcloud billing accounts list

# The export configuration is visible in Cloud Console only
# Navigate to: Billing → Billing Export → BigQuery export tab
# Confirm status shows "Enabled" and the correct dataset is listed
```

#### Deliverable 1

Screenshot of the Cloud Console Billing Export page showing the export enabled with your dataset name.

---

### Part 2: Create a Budget with Alert Thresholds (20 minutes)

#### Task 2.1 — Create a budget via Cloud Console

1. Navigate to Cloud Billing → Budgets and Alerts → Create Budget
2. Configure the budget:

   - Name: `lab-budget-dev`
   - Scope: Select your project
   - Budget type: Specified amount
   - Amount: $50

3. Configure alert thresholds:

   - Threshold 1: 50% of budget ($25)
   - Threshold 2: 90% of budget ($45)
   - Threshold 3: 100% of budget ($50)

4. Under Manage Notifications, check "Email alerts to billing admins and users"

5. Click Finish

#### Task 2.2 — Create a budget via gcloud CLI

GCP also supports creating budgets via the Cloud Billing Budget API. The gcloud CLI does not directly expose budget creation as a first-class command, but it can be done via the REST API or Terraform. For this task, document the REST API call structure:

```bash
# View existing budgets (requires billing.budgets.get IAM permission)
gcloud billing budgets list \
  --billing-account=YOUR_BILLING_ACCOUNT_ID
```

#### Task 2.3 — Add a Pub/Sub notification to the budget

1. In Cloud Console, edit the budget you just created
2. Under Manage Notifications, click "Connect a Pub/Sub topic"
3. Create a new topic: `billing-alerts`
4. Save the budget

Verify the Pub/Sub topic was created:

```bash
gcloud pubsub topics list
```

#### Deliverable 2

Screenshot of the budget configuration page showing three threshold alerts and the Pub/Sub topic connection.

---

### Part 3: Query Billing Data in BigQuery (25 minutes)

If your billing export has populated data, run the following queries. If using a sample dataset provided by your instructor, substitute the dataset reference.

#### Task 3.1 — Top costs by service

```sql
SELECT
  service.description AS service,
  ROUND(SUM(cost), 2) AS total_cost,
  ROUND(SUM(cost) * 100.0 / SUM(SUM(cost)) OVER (), 2) AS pct_of_total
FROM `YOUR_PROJECT.billing_export.gcp_billing_export_v1_XXXXXXXX`
WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY service.description
ORDER BY total_cost DESC
LIMIT 10;
```

Replace `YOUR_PROJECT.billing_export.gcp_billing_export_v1_XXXXXXXX` with your actual dataset table path.

#### Task 3.2 — Cost by label (team allocation)

```sql
SELECT
  (SELECT value FROM UNNEST(labels) WHERE key = 'team') AS team,
  ROUND(SUM(cost), 2) AS team_cost
FROM `YOUR_PROJECT.billing_export.gcp_billing_export_v1_XXXXXXXX`
WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY team
ORDER BY team_cost DESC;
```

#### Task 3.3 — Daily cost trend for Compute Engine

```sql
SELECT
  DATE(usage_start_time) AS usage_date,
  ROUND(SUM(cost), 2) AS daily_cost
FROM `YOUR_PROJECT.billing_export.gcp_billing_export_v1_XXXXXXXX`
WHERE
  service.description = 'Compute Engine'
  AND DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY usage_date
ORDER BY usage_date;
```

#### Deliverable 3

Screenshot of BigQuery query results for at least two of the three queries. If using a sample dataset, note this in your submission.

---

### Part 4: Review Recommender Suggestions (15 minutes)

#### Task 4.1 — View VM recommendations in Cloud Console

1. Navigate to Compute Engine → VM instances
2. Look for the "Recommendations" column in the VM list, or click the "Recommendations" tab at the top
3. If recommendations exist, note the VM name, current machine type, recommended machine type, and projected monthly savings

If no recommendations appear (this is common in new or lightly used projects), proceed to Task 4.2.

#### Task 4.2 — List recommendations via gcloud

```bash
# List VM rightsizing recommendations
gcloud recommender recommendations list \
  --project=${PROJECT_ID} \
  --location=us-central1 \
  --recommender=google.compute.instance.MachineTypeRecommender \
  --format="table(name,primaryImpact.costProjection.cost.units,stateInfo.state)"
```

If no recommendations are returned in your project, that is expected for a lab environment. Document the command and expected output format.

#### Task 4.3 — Review idle resource recommendations

```bash
# List idle VM recommendations
gcloud recommender recommendations list \
  --project=${PROJECT_ID} \
  --location=us-central1 \
  --recommender=google.compute.instance.IdleResourceRecommender

# List unattached disk recommendations
gcloud recommender recommendations list \
  --project=${PROJECT_ID} \
  --location=us-central1 \
  --recommender=google.compute.disk.IdleResourceRecommender
```

#### Deliverable 4

Screenshot of the Recommender output (Cloud Console or gcloud output). If your project has no recommendations, provide a screenshot showing the Recommender page with zero recommendations and write a one-paragraph explanation of when you would expect recommendations to appear based on what you learned in the module.

---

### Part 5: Object Lifecycle Management (20 minutes)

#### Task 5.1 — Create a Cloud Storage bucket

```bash
# Create a bucket for log storage
gsutil mb -l us-central1 gs://${PROJECT_ID}-log-archive

# Upload a test file
echo "test log data" | gsutil cp - gs://${PROJECT_ID}-log-archive/test-log.txt
```

#### Task 5.2 — Create a lifecycle configuration file

Create a file named `lifecycle.json` with the following content:

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "NEARLINE"
        },
        "condition": {
          "age": 30
        }
      },
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "COLDLINE"
        },
        "condition": {
          "age": 90
        }
      },
      {
        "action": {
          "type": "SetStorageClass",
          "storageClass": "ARCHIVE"
        },
        "condition": {
          "age": 365
        }
      }
    ]
  }
}
```

#### Task 5.3 — Apply the lifecycle policy

```bash
# Apply the lifecycle configuration to the bucket
gsutil lifecycle set lifecycle.json gs://${PROJECT_ID}-log-archive

# Verify the lifecycle configuration was applied
gsutil lifecycle get gs://${PROJECT_ID}-log-archive
```

#### Deliverable 5

Terminal output showing the `gsutil lifecycle get` command confirming the three lifecycle rules are applied to the bucket.

---

### Part 6: Programmatic Cost Cap Design (design exercise, 10 minutes)

This part is a design exercise — you do not need to deploy the Cloud Function, but you must produce the design documentation.

#### Task 6.1 — Design the cost cap architecture

Draw or describe in text the architecture for a programmatic cost cap that:

- Fires when the `lab-budget-dev` budget reaches 100%
- Automatically disables billing on the `dev` project to stop all paid resource usage
- Sends a Slack notification to the `#billing-alerts` channel with the project name and the current spend amount

Your design must specify:

- What triggers the Cloud Function
- What the Cloud Function does (two API calls: one to get the Pub/Sub message data, one to disable billing)
- What IAM permissions the Cloud Function's service account needs
- What happens to running VMs after billing is disabled

#### Deliverable 6

Written architecture description (150–200 words) with an optional diagram. Must answer all four specification points.

---

### Deliverables Summary

| Deliverable | Description |
|---|---|
| Deliverable 1 | Screenshot: Billing Export enabled in Cloud Console |
| Deliverable 2 | Screenshot: Budget with three thresholds and Pub/Sub connection |
| Deliverable 3 | Screenshot: BigQuery billing query results (two queries) |
| Deliverable 4 | Screenshot: Recommender output or explanation |
| Deliverable 5 | Terminal output: gsutil lifecycle get confirming three rules |
| Deliverable 6 | Written cost cap architecture design (150–200 words) |

Submit all deliverables as a single document or PDF via Canvas LMS.

---

### Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Billing export setup (Part 1) | 15 | Export enabled; screenshot confirms correct dataset |
| Budget and alerts (Part 2) | 20 | Three thresholds configured; Pub/Sub topic connected |
| BigQuery queries (Part 3) | 25 | At least two queries with results; correct SQL structure |
| Recommender review (Part 4) | 15 | Output shown or absence explained with correct context |
| Object lifecycle management (Part 5) | 15 | Three lifecycle rules applied; gsutil output confirms |
| Cost cap design (Part 6) | 10 | All four specification points addressed; IAM permissions correct |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: Automated VM Schedule with Instance Schedules

Configure a Compute Engine resource policy that automatically stops a VM at the end of the workday and starts it each morning, eliminating overnight idle costs without writing any custom code.

1. Create a test VM to apply the schedule to:

```bash
export PROJECT_ID=$(gcloud config get-value project)
gcloud compute instances create schedule-test-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

1. Create an instance schedule resource policy (stop at 6 PM, start at 8 AM, Monday–Friday):

```bash
gcloud compute resource-policies create instance-schedule lab15-schedule \
  --region=us-central1 \
  --vm-start-schedule="0 8 * * MON-FRI" \
  --vm-stop-schedule="0 18 * * MON-FRI" \
  --timezone="America/Chicago"
```

1. Attach the schedule policy to the VM:

```bash
gcloud compute instances add-resource-policies schedule-test-vm \
  --zone=us-central1-a \
  --resource-policies=lab15-schedule
```

1. Verify the policy is attached:

```bash
gcloud compute instances describe schedule-test-vm \
  --zone=us-central1-a \
  --format="value(resourcePolicies)"
```

1. Grant the Compute Engine service account permission to start and stop the VM (required for instance schedules to function):

```bash
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID \
  --format='value(projectNumber)')
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:service-${PROJECT_NUMBER}@compute-system.iam.gserviceaccount.com" \
  --role="roles/compute.instanceAdmin.v1"
```

### Challenge 2: Billing Anomaly Detection with Log-Based Alerting

Create a Cloud Monitoring alerting policy that fires when Compute Engine costs in the BigQuery billing export exceed a daily threshold, using a scheduled BigQuery query and a Cloud Monitoring custom metric.

1. Create a scheduled BigQuery query that runs daily and writes the result to a summary table:

```bash
bq mk --dataset \
  --location=US \
  ${PROJECT_ID}:billing_alerts

bq mk --table \
  ${PROJECT_ID}:billing_alerts.daily_compute_cost \
  date:DATE,daily_cost:FLOAT64
```

1. Create a scheduled query in BigQuery (requires BigQuery Data Transfer Service):

```bash
gcloud services enable bigquerydatatransfer.googleapis.com
```

Navigate to BigQuery → Scheduled Queries → Create and use the following SQL (replace the billing export table name with your actual table):

```sql
INSERT INTO `YOUR_PROJECT.billing_alerts.daily_compute_cost`
SELECT
  DATE(usage_start_time) AS date,
  ROUND(SUM(cost), 2) AS daily_cost
FROM `YOUR_PROJECT.billing_export.gcp_billing_export_v1_XXXXXXXX`
WHERE
  service.description = 'Compute Engine'
  AND DATE(usage_start_time) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
GROUP BY date;
```

Set the schedule to run daily at 6:00 AM.

1. Create a log-based metric in Cloud Logging that counts entries when a Cloud Function (triggered by the scheduled query completion) logs a high-cost warning. As an alternative approach, use Cloud Monitoring custom metrics:

```bash
gcloud monitoring metrics-scopes create \
  --project=${PROJECT_ID}

# Document the metric descriptor you would create for tracking daily_cost:
# Type: custom.googleapis.com/billing/daily_compute_cost
# Kind: GAUGE
# Value type: DOUBLE
# Unit: USD
```

### Reflection Questions

1. In Challenge 1, the instance schedule uses cron syntax (`0 8 * * MON-FRI`). Explain what would happen to the VM if the schedule tries to start it at 8 AM but the VM is already in RUNNING state (perhaps started manually by a developer). Does the schedule produce an error, skip the action, or attempt to restart the VM?

2. In Challenge 2, there is an inherent delay between when billing costs are incurred and when they appear in the BigQuery billing export (typically 24–48 hours). How does this latency affect the usefulness of a daily cost anomaly alert, and what operational adjustment would you make to account for it when setting the alert threshold?
