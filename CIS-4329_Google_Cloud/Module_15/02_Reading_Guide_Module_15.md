# Reading Guide: Module 15 — GCP Cost Management and Billing

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Introduction

Module 15 covers GCP cost management and billing — a domain tested on every ACE exam and an essential operational skill for any GCP administrator. Cloud costs can grow rapidly without active governance: idle VMs accumulate charges, over-provisioned instances waste budget, and unmanaged storage transitions to high-cost tiers. This module provides the framework for understanding GCP billing, controlling costs proactively, and analyzing spending with data.

The ACE exam tests cost management through scenario questions: which discount type applies to a given workload, how to enforce a spending limit programmatically, which tool identifies over-provisioned resources, and how to implement cost allocation across teams. This guide consolidates all terms, tables, and decision frameworks needed to answer those questions correctly.

---

## Section 1: High-Yield Glossary

**Cloud Billing Account** — A GCP resource that defines who pays for a set of GCP projects. A billing account is linked to one or more projects. Each project must be linked to exactly one active billing account for paid resources to function. Billing accounts are linked to a Google payments profile (credit card or invoiced billing for enterprise customers).

**Billing account roles** — IAM roles controlling access to billing account operations:

- `roles/billing.viewer` — view costs and invoices; no modifications
- `roles/billing.admin` — full control: link/unlink projects, modify payment methods, manage budgets
- `roles/billing.projectManager` — link and unlink projects to billing accounts; no payment method access
- `roles/billing.budgetAdmin` — create and manage budgets without full billing admin access

**Cloud Billing Budget** — A spending threshold that triggers notifications when costs reach defined percentages of the budget amount. Budgets are informational by default — they do not stop resource usage. Up to five alert thresholds per budget. Notifications go to billing admins via email and/or a Pub/Sub topic.

**Programmatic cost cap** — The pattern of connecting a budget Pub/Sub notification to a Cloud Function that calls the Cloud Billing API to disable billing on a project when a threshold is exceeded. Disabling billing stops all paid resources in the project. This is the only GCP-native mechanism to automatically stop resource usage based on spending.

**Committed Use Discounts (CUDs)** — Discounts on Compute Engine resources in exchange for a usage commitment:

- Resource-based CUDs: commit to a specific amount of vCPU and memory in a specific region for 1 or 3 years. Up to 57% off on-demand pricing (3-year) or 37% (1-year). Applied at project level.
- Spend-based CUDs: commit to a minimum monthly spend on specific services (Cloud SQL, VMware Engine). Applied at billing account level.

**Sustained Use Discounts (SUDs)** — Automatic discounts applied when a Compute Engine VM runs for more than 25% of a calendar month. No commitment required; GCP applies them automatically. Maximum discount approximately 30% at 100% monthly usage. Applies to N1 and N2 machine types only. Does not apply to E2, Spot VMs, preemptible VMs, A2 GPU instances, or Cloud SQL.

**Preemptible VM** — A Compute Engine VM type that uses excess GCP capacity at up to 91% discount. Can be reclaimed by GCP at any time with 30 seconds notice. Automatically terminated after 24 hours maximum runtime. Replaced by Spot VMs as the recommended product.

**Spot VM** — The current recommended product for discounted interruptible compute. Same deep discount as preemptible VMs (up to 91%) but with no maximum 24-hour runtime. Can still be preempted at any time when GCP needs capacity back.

**Billing export to BigQuery** — The configuration that sends Cloud Billing data (standard or detailed usage cost) to a BigQuery dataset on a daily basis. Enables SQL-based cost analysis, cost allocation by label, and historical trend analysis. Not retroactive — data populates from the date export is enabled.

**Resource labels** — Key-value metadata attached to GCP resources (VMs, buckets, Cloud SQL instances, etc.). Labels appear in billing export data, enabling cost allocation by team, environment, application, or cost center. Example: `team: payments`, `env: production`, `app: checkout-service`.

**GCP Recommender** — A service that analyzes resource usage and configuration to produce actionable optimization recommendations. Cost-relevant recommenders include: Idle VM Recommender, VM Rightsizing Recommender, Unattached Disk Recommender, Idle IP Address Recommender, and CUD Recommender.

**VM Rightsizing Recommender** — Identifies Compute Engine VMs that are consistently over-provisioned based on CPU and memory utilization over the past 14 days. Recommends switching to a smaller machine type with projected monthly savings. Accessible via Cloud Console and the gcloud CLI.

**Object Lifecycle Management** — A Cloud Storage configuration that automatically transitions objects to lower-cost storage classes or deletes objects based on age or other conditions. Used to move infrequently accessed data to Nearline, Coldline, or Archive storage classes to reduce storage costs.

**Cloud Storage classes** — Storage tiers with different per-GB pricing and minimum storage duration requirements:

- Standard: no minimum duration; highest per-GB price; for frequently accessed data
- Nearline: 30-day minimum; for data accessed less than once per month
- Coldline: 90-day minimum; for data accessed less than once per quarter
- Archive: 365-day minimum; lowest per-GB price; for data accessed less than once per year

**GCP Pricing Calculator** — A web tool for estimating monthly GCP costs before provisioning resources. Supports detailed configuration of most GCP services and can compare on-demand vs. CUD pricing.

**Always Free tier** — Specific monthly quotas of GCP services that are permanently free, regardless of billing account status. Key limits: 1 f1-micro VM/month (selected US regions), 5 GB Regional storage, 10 GB BigQuery storage + 1 TB query processing, 2 million Cloud Functions invocations.

---

## Section 2: Discount Type Decision Framework

| Workload Characteristic | Recommended Discount | Reason |
|---|---|---|
| Runs 24/7, stable resource usage, 3-year horizon | Resource-based 3-year CUD | Maximum discount (57%); no usage uncertainty |
| Runs 24/7, stable usage, 1-year horizon | Resource-based 1-year CUD | 37% discount; lower commitment risk |
| Variable usage, no long-term commitment desired | Sustained Use Discount | Automatic, no commitment, up to 30% |
| Batch workload, can tolerate interruption | Spot VM | Up to 91% discount; preemption acceptable |
| Dev/test VMs, idle overnight | Schedule stop/start | Cost reduction via zero-hours billing |
| Cloud SQL production instance | Spend-based CUD | Resource-based CUD not available for Cloud SQL |

---

## Section 3: Billing Export to BigQuery Reference

### Setup Sequence

1. Create a BigQuery dataset in a project (note: dataset must be in the same organization)
2. Cloud Billing → Billing Export → BigQuery export → Enable
3. Select billing account, destination project, and dataset name
4. Data begins flowing within 24 hours of enablement

### Key Billing Export Schema Fields

| Field | Description |
|---|---|
| `project.id` | GCP project ID |
| `service.description` | GCP service name (e.g., Compute Engine) |
| `sku.description` | Specific SKU (e.g., N1 Predefined Instance Core) |
| `usage_start_time` | Start of the usage period |
| `cost` | Net cost after credits and discounts |
| `labels` | Resource labels as key-value pairs |
| `credits` | Discount credits applied (CUDs, SUDs, promotions) |

### Sample Cost Analysis Queries

Top services by cost in the past 30 days:

```sql
SELECT service.description, ROUND(SUM(cost), 2) AS total_cost
FROM `project.dataset.gcp_billing_export_v1_XXXXXXXX`
WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY service.description
ORDER BY total_cost DESC;
```

Cost by label (team allocation):

```sql
SELECT
  (SELECT value FROM UNNEST(labels) WHERE key = 'team') AS team,
  ROUND(SUM(cost), 2) AS team_cost
FROM `project.dataset.gcp_billing_export_v1_XXXXXXXX`
WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY team
ORDER BY team_cost DESC;
```

---

## Section 4: GCP Recommender Reference

### Recommender Types and Access

| Recommender | What It Finds | Access Path |
|---|---|---|
| Idle VM Recommender | VMs with < 5% CPU for 14 days | Compute Engine → VM instances → Recommendations |
| VM Rightsizing Recommender | Over-provisioned VM machine types | Compute Engine → VM instances → Recommendations |
| Unattached Disk Recommender | Persistent disks not attached for 30+ days | Compute Engine → Disks |
| Idle IP Recommender | Reserved IPs not attached to any resource | VPC Network → IP addresses |
| CUD Recommender | Recommended CUD purchases based on usage | Compute Engine → Committed use discounts |

### gcloud CLI Access

```bash
# List all cost recommendations for a project
gcloud recommender recommendations list \
  --project=PROJECT_ID \
  --location=global \
  --recommender=google.compute.instance.MachineTypeRecommender

# Mark a recommendation as claimed (applying the change)
gcloud recommender recommendations mark-claimed RECOMMENDATION_ID \
  --project=PROJECT_ID \
  --location=LOCATION \
  --recommender=RECOMMENDER_ID \
  --etag=ETAG
```

---

## Section 5: Cloud Storage Cost Optimization Reference

### Storage Class Comparison

| Class | Min Duration | Access Cost | Use Case |
|---|---|---|---|
| Standard | None | Free | Frequently accessed; active data |
| Nearline | 30 days | Per-read charge | Monthly backups; data accessed < 1x/month |
| Coldline | 90 days | Higher per-read charge | Quarterly archives; DR backups |
| Archive | 365 days | Highest per-read charge | Long-term compliance archives; annual access |

### Object Lifecycle Management Example

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
        "condition": {"age": 90}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
```

This lifecycle policy transitions objects to Nearline at 30 days, Coldline at 90 days, and deletes them at 365 days — automating cost optimization for log data, backups, or media archives.

---

## Section 6: ACE Exam Cost Scenario Patterns

### Pattern 1: Programmatic Budget Enforcement

Scenario: Enforce that spending on a development project never exceeds $500/month. When the limit is reached, all resource usage must stop automatically.

Solution: Create a budget for $500 on the project with a 100% threshold alert and a Pub/Sub topic notification. Create a Cloud Function triggered by the Pub/Sub topic that calls `billingClient.UpdateProjectBillingInfo()` with `billingAccountName: ""` to disable billing on the project.

### Pattern 2: Cost Allocation Across Teams

Scenario: An organization has 15 teams sharing a single GCP billing account. Finance needs to chargeback costs to each team monthly.

Solution: Apply consistent resource labels (`team: TEAM_NAME`) to all resources. Enable billing export to BigQuery. Create a scheduled BigQuery query that aggregates costs by the `team` label and exports to a spreadsheet or BI tool.

### Pattern 3: Storage Cost Reduction for Log Data

Scenario: A Cloud Storage bucket contains application logs. Logs older than 30 days are rarely accessed; logs older than 1 year are never accessed but must be retained for compliance.

Solution: Configure Object Lifecycle Management: transition to Nearline at 30 days, transition to Archive at 365 days (do not delete — compliance retention required).

### Pattern 4: Right-Sizing Compute

Scenario: A GCP administrator suspects several Compute Engine VMs are over-provisioned after a traffic reduction. How do they identify and right-size them without manual analysis?

Solution: Navigate to Compute Engine → VM instances → Recommendations tab and review VM Rightsizing Recommender suggestions. Apply recommended machine type changes to identified VMs during a maintenance window.

---

## Section 7: GCP Always Free Tier Reference

| Service | Always Free Limit |
|---|---|
| Compute Engine | 1 f1-micro instance/month in us-west1, us-central1, or us-east1 (combined, not per region) |
| Cloud Storage | 5 GB Regional storage in US |
| BigQuery | 10 GB storage; 1 TB query processing/month |
| Cloud Functions | 2 million invocations; 400,000 GB-seconds; 200,000 GHz-seconds |
| Cloud Run | 2 million requests; 360,000 GB-seconds; 180,000 vCPU-seconds |
| Pub/Sub | 10 GB messages/month |
| Firestore | 1 GB storage; 50,000 reads/day; 20,000 writes/day; 20,000 deletes/day |
| Cloud Shell | Free managed instance; 5 GB persistent disk |

---

## Section 8: Practice Questions

**1.** An organization's development team has been leaving VMs running overnight and on weekends. The cloud administrator wants to automatically stop all VMs in the `dev` project at 6 PM daily and restart them at 8 AM. What GCP-native solution achieves this with no custom code?

**2.** A GCP project has an active billing account. A Cloud Function is triggered by a budget alert Pub/Sub message and calls the Cloud Billing API to disable billing. What happens to the Compute Engine VMs running in the project when billing is disabled?

**3.** An organization runs 40 n1-standard-4 VMs in us-central1 continuously for the past 12 months and plans to continue for at least 3 years. SUDs are currently providing a ~30% discount. What additional discount strategy would maximize savings?

**4.** A team stores 10 TB of application logs in Cloud Storage Standard class. The logs are accessed frequently for the first 30 days, rarely for the next 60 days, and never accessed after 90 days but must be retained for 7 years for compliance. Design the Object Lifecycle Management policy.

**5.** An organization wants to identify which GCP services are driving the highest costs and allocate charges to individual engineering teams. They have no existing cost management infrastructure. List the three configuration steps required to enable team-level cost allocation.

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — Cloud Billing Budgets and Alerts**
<https://cloud.google.com/billing/docs/how-to/budgets>
Complete reference for creating and managing billing budgets: threshold rule configuration, Pub/Sub notification setup for programmatic cost enforcement, the distinction between notification-only behavior and the Cloud Function pattern required to actually stop resources, and budget scope options (billing account vs. individual project).

**2. Google Cloud Documentation — Object Lifecycle Management**
<https://cloud.google.com/storage/docs/lifecycle>
Full reference for Cloud Storage Object Lifecycle Management rules including all supported conditions (age, storage class, created before, number of newer versions) and actions (SetStorageClass, Delete, AbortIncompleteMultipartUpload), minimum storage duration requirements per storage class, and interaction with object versioning.

**3. Google Cloud Documentation — GCP Recommender Overview**
<https://cloud.google.com/recommender/docs/overview>
Overview of all Recommender types available in GCP including VM Rightsizing, Idle VM, Unattached Disk, Idle IP Address, CUD Recommender, and IAM Recommender — covering how recommendations are generated from utilization data, how to access them via gcloud CLI and Cloud Console, and the mark-claimed/mark-dismissed workflow for tracking recommendation actions.
