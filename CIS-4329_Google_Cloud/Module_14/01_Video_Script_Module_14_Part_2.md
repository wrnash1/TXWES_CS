# Video Script: Module 14 — Cost Management and Billing (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 12 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction to Part 2

Welcome back. In Part 1 we covered the billing hierarchy, budget alerts, and discount
types. In Part 2 we cover billing export to BigQuery for cost analysis, the Recommender
service, label-based cost allocation, Cloud Storage cost optimization, and the ACE exam
patterns for cost management.

---

### Section 1: Billing Export to BigQuery

To analyze historical spending with SQL, configure a **Cloud Billing export to BigQuery**.
Once enabled, GCP writes a row for each billing line item (service, project, SKU, labels)
to a BigQuery dataset in near-real time.

There are two export types:

- **Standard usage cost** — daily cost summary by project, service, and SKU
- **Detailed usage cost** — adds resource-level detail (VM name, Cloud Storage bucket,
  etc.) and label dimensions; recommended for granular analysis

```bash
# Enable the export via Cloud Console:
# Cloud Billing → Billing account → Billing export → Standard usage cost
# Select BigQuery project and dataset name
# (cannot be configured via gcloud — must use Console)

# Once export is running, query the data in BigQuery:
# SELECT
#   project.id,
#   service.description,
#   SUM(cost) AS total_cost
# FROM `MY_PROJECT.billing_export.gcp_billing_export_v1_*`
# WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
# GROUP BY 1, 2
# ORDER BY total_cost DESC
```

Key billing export column names to know:

| Column | Description |
|---|---|
| `project.id` | GCP project ID |
| `service.description` | Service name (Compute Engine, Cloud Storage, etc.) |
| `sku.description` | Specific SKU (e.g., "N1 Predefined Instance Core") |
| `cost` | Net cost for this line item |
| `usage.amount` | Usage quantity (hours, bytes, requests) |
| `labels` | Resource labels for cost attribution |
| `resource.name` | Specific resource name (bucket name, VM name) |

---

### Section 2: The Recommender Service

The **Recommender** service analyzes usage patterns and generates actionable cost and
security recommendations.

#### VM Rightsizing Recommender

The VM rightsizing recommender identifies VMs that are consistently underutilizing their
allocated CPU and memory. It suggests switching to a smaller machine type to reduce cost
without performance impact.

```bash
# List VM rightsizing recommendations
gcloud recommender recommendations list \
  --project=MY_PROJECT \
  --location=us-central1-a \
  --recommender=google.compute.instance.MachineTypeRecommender \
  --format="table(name,description,stateInfo.state)"

# View a specific recommendation
gcloud recommender recommendations describe RECOMMENDATION_ID \
  --project=MY_PROJECT \
  --location=us-central1-a \
  --recommender=google.compute.instance.MachineTypeRecommender
```

#### IAM Recommender

The IAM recommender identifies users and service accounts with IAM roles that include
permissions they have never exercised. It recommends replacing overly broad roles with
more restrictive ones that match actual usage.

```bash
# List IAM recommendations
gcloud recommender recommendations list \
  --project=MY_PROJECT \
  --location=global \
  --recommender=google.iam.policy.Recommender
```

#### Other Recommenders

- **Idle VM recommender** — identifies VMs that have been running but unused for 14+ days
- **Idle persistent disk recommender** — identifies unattached disks
- **Committed use discount recommender** — recommends CUD purchases based on steady VM
  usage patterns

---

### Section 3: Label-Based Cost Allocation

**Resource labels** are key-value pairs attached to GCP resources. When billing export
is configured, labels appear in the billing data and can be used to group and attribute
costs to teams, environments, or applications.

Best practice label schema:

| Label Key | Example Values | Purpose |
|---|---|---|
| `environment` | `prod`, `staging`, `dev` | Attribute costs by environment |
| `team` | `backend`, `data-eng`, `ml` | Attribute costs by team |
| `application` | `payments`, `analytics` | Attribute costs by application |
| `cost-center` | `CC-1234` | Financial chargeback |

```bash
# Add labels to a VM
gcloud compute instances add-labels my-vm \
  --labels="environment=prod,team=backend,application=payments" \
  --zone=us-central1-a

# Add labels to a Cloud Storage bucket
gcloud storage buckets update gs://my-bucket \
  --update-labels="environment=prod,team=data-eng"

# Add labels to a BigQuery dataset
bq update --set_label environment:prod MY_PROJECT:my_dataset
```

After labeling resources, query the billing export data grouped by label to produce
team- or application-level cost reports.

---

### Section 4: Cloud Storage Cost Optimization

Cloud Storage costs have two components: **storage cost** (per GB/month) and **operation
cost** (per API call). Choosing the right storage class significantly reduces storage cost:

| Storage Class | Use Case | Monthly Cost | Retrieval Cost |
|---|---|---|---|
| Standard | Frequently accessed data | ~$0.02/GB | None |
| Nearline | Accessed ~1x/month | ~$0.01/GB | $0.01/GB |
| Coldline | Accessed ~1x/quarter | ~$0.004/GB | $0.02/GB |
| Archive | Accessed ~1x/year | ~$0.0012/GB | $0.05/GB |

Use **Object Lifecycle Management** to automatically transition objects to cheaper
storage classes as they age:

```bash
# Create a lifecycle rule: move to Nearline after 30 days, Archive after 365 days
cat > lifecycle.json << 'EOF'
{
  "rule": [
    {
      "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
      "condition": {"age": 30}
    },
    {
      "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},
      "condition": {"age": 365}
    },
    {
      "action": {"type": "Delete"},
      "condition": {"age": 1825}
    }
  ]
}
EOF

gcloud storage buckets update gs://my-data-bucket \
  --lifecycle-file=lifecycle.json
```

---

### Section 5: ACE Exam Cost Management Patterns

**Budget alerts do not stop resources** — This is the most tested concept. If a scenario
asks "how do you prevent overspending," the budget alert alone is not the answer. You need
Pub/Sub + Cloud Function + billing API to disable billing or stop VMs.

**CUD vs. SUD** — CUDs require commitment and give larger discounts; SUDs are automatic
and smaller. For workloads running 24/7, CUDs give better savings. For workloads running
50–75% of the month, SUDs kick in automatically.

**Spot VMs for batch** — When a scenario mentions fault-tolerant, checkpointed, or
interruptible batch workloads (genomics, video rendering, data pipeline), the cost
optimization answer is Spot VMs. When reliability is required, Spot VMs are wrong.

**Billing export to BigQuery for analysis** — Any scenario asking "how do you analyze
spending trends" or "how do you query billing data with SQL" is answered with BigQuery
billing export. The Cloud Billing Reports page cannot run custom queries.

**Label early, label consistently** — Labels only appear in billing export going forward
from when they are added. Retroactive labeling does not add historical billing data.

---

### Module 14 Summary

Module 14 covered Cost Management and Cloud Billing:

- **Billing hierarchy** — organization → billing account → project → resource
- **Budget alerts** — notification-only; Pub/Sub + Cloud Function for enforcement
- **Discount types** — on-demand (flexible), SUDs (automatic), CUDs (committed,
  higher discount), Spot VMs (90% off, interruptible)
- **Billing export to BigQuery** — standard and detailed; SQL analysis of historical costs
- **Recommender** — VM rightsizing, IAM, idle VMs; actionable cost reduction suggestions
- **Labels** — key-value tags enabling cost attribution by team, environment, application
- **Cloud Storage classes** — Standard/Nearline/Coldline/Archive; lifecycle management

For the ACE exam: budget alerts are notification-only; CUDs need a commitment but offer
higher discounts than SUDs; Spot VMs are for interruptible batch workloads; billing export
to BigQuery enables SQL cost queries.

Complete the lab, take the quiz, and join the discussion. Module 15 covers GCP ACE exam
review and key CLI command practice.
