# Lab: Module 14 — Cost Management and Billing

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will navigate the Cloud Billing console, create a budget with alert
thresholds, configure billing export to BigQuery, label resources for cost attribution,
and review VM rightsizing recommendations from the Recommender service.

**Estimated time**: 60–75 minutes

**Cost estimate**: Under $0.50 USD (Recommender API calls and BigQuery queries are free
or minimal; no expensive resources are created)

---

### Prerequisites

- A GCP project with billing enabled
- Billing Administrator or Billing Account Viewer role (to view billing data)
- Cloud Shell or gcloud CLI authenticated

```bash
gcloud services enable \
  billingbudgets.googleapis.com \
  recommender.googleapis.com \
  bigquery.googleapis.com
```

---

### Part 1: Explore the Billing Console

#### Task 1.1: Navigate to Cloud Billing

1. In the Cloud Console, click the navigation menu and select **Billing**.
2. Click your billing account name to open the billing account overview.
3. Review the **Overview** page — note the current month's cost and the trend graph.
4. Click **Reports** — explore the chart. Change the time range to "Last 3 months."
5. Click **Cost table** — review the breakdown by project and service.
6. Record: Which service is your highest cost item this month (or last month)?

#### Task 1.2: View Billing Account Details

```bash
# List billing accounts
gcloud billing accounts list

# Note your billing account ID (format: XXXXXX-XXXXXX-XXXXXX)
BILLING_ACCOUNT_ID=YOUR_BILLING_ACCOUNT_ID

# List projects linked to the billing account
gcloud billing projects list --billing-account=$BILLING_ACCOUNT_ID
```

---

### Part 2: Create a Budget with Alert Thresholds

#### Task 2.1: Create a Budget

```bash
# Create a $10 budget with alerts at 50%, 90%, and 100%
gcloud billing budgets create \
  --billing-account=$BILLING_ACCOUNT_ID \
  --display-name="Lab14-Budget" \
  --budget-amount=10USD \
  --threshold-rule=percent=0.5 \
  --threshold-rule=percent=0.9 \
  --threshold-rule=percent=1.0

# List budgets to verify
gcloud billing budgets list \
  --billing-account=$BILLING_ACCOUNT_ID
```

#### Task 2.2: Review the Budget in the Console

1. In the Cloud Console, navigate to **Billing** → **Budgets & alerts**.
2. Click your "Lab14-Budget" to view its configuration.
3. Note the **Alert threshold rules** section — you should see three thresholds.
4. Note the **Manage notifications** section — confirm that "Email alerts to billing
   admins and users" is enabled.

Record: What happens to running resources when a budget threshold is crossed?

---

### Part 3: Configure Billing Export to BigQuery

Billing export must be configured in the Cloud Console (not available via gcloud CLI).

#### Task 3.1: Create a BigQuery Dataset for Billing Data

```bash
# Create a dataset for billing export
bq mk --dataset \
  --location=US \
  --description="Cloud Billing export data" \
  YOUR_PROJECT_ID:billing_export
```

#### Task 3.2: Enable Standard Export

1. In the Cloud Console, navigate to **Billing** → your billing account → **Billing export**.
2. Click the **BigQuery export** tab.
3. Under **Standard usage cost**, click **Edit settings**.
4. Set **Project** to your project and **Dataset** to `billing_export`.
5. Click **Save**.

Note: Data from the export starts appearing within a few hours. For this lab, you will
verify the configuration is correct rather than waiting for data.

#### Task 3.3: Verify Export Configuration

```bash
# Verify the dataset was created
bq ls YOUR_PROJECT_ID:

# Describe the dataset
bq show YOUR_PROJECT_ID:billing_export
```

Record: What is the name of the BigQuery table that will receive billing data? (Format:
`gcp_billing_export_v1_BILLING_ACCOUNT_ID`)

---

### Part 4: Label Resources for Cost Attribution

#### Task 4.1: Create a VM with Cost Attribution Labels

```bash
# Create a VM with labels for cost attribution
gcloud compute instances create lab14-labeled-vm \
  --machine-type=e2-micro \
  --zone=us-central1-a \
  --labels="environment=lab,team=student,application=cost-management"

# Verify the labels
gcloud compute instances describe lab14-labeled-vm \
  --zone=us-central1-a \
  --format="value(labels)"
```

#### Task 4.2: Create a Storage Bucket with Labels

```bash
# Create a bucket with cost attribution labels
gcloud storage buckets create gs://YOUR_PROJECT_ID-lab14-bucket \
  --location=us-central1

# Add labels to the bucket
gcloud storage buckets update gs://YOUR_PROJECT_ID-lab14-bucket \
  --update-labels="environment=lab,team=student"

# Verify bucket labels
gcloud storage buckets describe gs://YOUR_PROJECT_ID-lab14-bucket \
  --format="value(labels)"
```

Record: How would these labels appear in the BigQuery billing export? Which column name
contains the label data?

---

### Part 5: Review Recommender Suggestions

#### Task 5.1: View VM Rightsizing Recommendations

```bash
# List VM rightsizing recommendations (may be empty for a new project)
gcloud recommender recommendations list \
  --project=YOUR_PROJECT_ID \
  --location=us-central1-a \
  --recommender=google.compute.instance.MachineTypeRecommender \
  --format="table(name,description,stateInfo.state)"
```

If no recommendations appear (common for a new or low-usage project), continue to step 5.2.

#### Task 5.2: View IAM Recommendations

```bash
# List IAM recommendations
gcloud recommender recommendations list \
  --project=YOUR_PROJECT_ID \
  --location=global \
  --recommender=google.iam.policy.Recommender \
  --format="table(name,description,stateInfo.state)"
```

#### Task 5.3: Explore Recommender in the Console

1. In the Cloud Console, navigate to the navigation menu → **Active Assist** →
   **Recommender**.
2. Review the categories: **Cost**, **Security**, **Performance**, **Manageability**.
3. Click **Cost** to see any VM rightsizing or idle resource recommendations.
4. Record: What type of recommendations appear (if any), and what action do they suggest?

---

### Part 6: Pricing Calculator Exercise

1. Open `https://cloud.google.com/products/calculator` in a browser.
2. Add a Compute Engine estimate:
   - Machine type: `n2-standard-4` (4 vCPU, 16 GB RAM)
   - Region: `us-central1`
   - Usage: 730 hours/month (24/7)
3. Record the monthly on-demand cost.
4. Change the commitment to "1 year" and record the new monthly cost.
5. Change to "3 year" and record the monthly cost.
6. Calculate the percentage savings of the 3-year CUD compared to on-demand.

---

### Part 7: Reflection Questions

1. You configured a budget alert at 100% of $10. What happens to your VM when spending
   reaches $10? What additional configuration would be needed to actually stop the VM?
2. You created a budget of $10, but the billing export dataset you configured was in the
   same project that is billed. If you receive the bill, which project is charged for
   the BigQuery dataset storage?
3. A colleague suggests switching your 24/7 production database VM to a Spot VM to save
   90% on compute costs. Why is this a bad idea, and what alternative would you recommend?
4. Your billing export table has a column called `labels`. You added labels to a VM on
   Monday, but when you query billing data for Sunday (the day before), there are no
   labels. Why?
5. The Recommender says your VM has been running at less than 5% CPU for 2 weeks and
   suggests switching from `n2-standard-8` to `n2-standard-2`. What steps would you
   take before accepting this recommendation?

---

### Part 8: Cleanup

```bash
# Delete the labeled VM
gcloud compute instances delete lab14-labeled-vm \
  --zone=us-central1-a --quiet

# Delete the storage bucket
gcloud storage buckets delete gs://YOUR_PROJECT_ID-lab14-bucket --quiet

# Delete the BigQuery dataset (if no billing data has arrived yet)
bq rm --dataset --recursive --force YOUR_PROJECT_ID:billing_export

# Delete the budget
BUDGET_NAME=$(gcloud billing budgets list \
  --billing-account=$BILLING_ACCOUNT_ID \
  --format="value(name)" \
  --filter="displayName=Lab14-Budget")
gcloud billing budgets delete $BUDGET_NAME
```

---

### Submission Checklist

- Billing account explored in Cloud Console; highest cost service recorded
- Budget created with three threshold rules
- Budget behavior documented (notification-only)
- BigQuery dataset created for billing export
- Standard billing export configured pointing to the dataset
- VM and storage bucket created with cost attribution labels
- Recommender reviewed and recommendations documented
- Pricing Calculator exercise completed with three cost comparisons
- All 5 reflection questions answered
- All resources cleaned up

---

### Grading Rubric

| Task | Points |
|---|---|
| Billing account explored; highest cost service recorded | 10 |
| Budget created with 3 thresholds; behavior documented | 15 |
| BigQuery dataset and export configured | 15 |
| Resources labeled and label column identified | 15 |
| Recommender reviewed | 10 |
| Pricing Calculator exercise with three cost points | 15 |
| Reflection questions answered | 15 |
| Resources cleaned up | 5 |
| **Total** | **100** |
