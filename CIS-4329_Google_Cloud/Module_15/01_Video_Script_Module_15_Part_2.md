# Video Script: Module 15 — GCP Cost Management and Billing (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome back. This is Part 2 of Module 15. In Part 1 we covered the billing hierarchy, budget alerts, committed use discounts, sustained use discounts, and Spot VMs. In this part we cover billing export to BigQuery, the Recommender service for automated cost optimization recommendations, cost optimization strategies for common GCP services, and the GCP free tier.

---

### Section 1: Billing Export to BigQuery

GCP Cloud Billing can export detailed billing data to a BigQuery dataset automatically. Once configured, billing data flows into BigQuery on a daily basis, where it can be queried with SQL to analyze spending by project, service, resource, label, or time period.

**Types of billing export:**

- **Standard usage cost export** — Line-item billing data per resource, per day. Includes service, SKU, project, labels, usage amount, and cost.
- **Detailed usage cost export** — Includes resource-level granularity (specific VM instance names, disk names). Richer than standard but produces larger datasets.
- **Pricing export** — The current pricing list for all GCP SKUs. Useful for cost forecasting and comparison.

**Configuration steps:**

1. Create a BigQuery dataset in a project where the billing export will be stored
2. Go to Cloud Billing → Billing Export → BigQuery export
3. Select the billing account, the destination project, and the dataset name
4. Enable the export

Note: Export data is not retroactive. Data only populates from the date export is enabled. Always enable billing export on day one of a new billing account.

**Querying billing data.** Once data is in BigQuery, standard SQL queries can analyze it:

```sql
SELECT
  project.id AS project,
  service.description AS service,
  SUM(cost) AS total_cost
FROM `billing_dataset.gcp_billing_export_v1_XXXXXX`
WHERE DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY project, service
ORDER BY total_cost DESC
LIMIT 20;
```

This query shows the top 20 most expensive services across all projects in the past 30 days.

**Cost allocation with labels.** Teams can tag GCP resources with labels (key-value pairs like `team: payments`, `env: production`). These labels appear in billing export data, allowing cost allocation by team, environment, or application. Label-based cost allocation is a foundational practice for FinOps.

**ACE exam pattern:** "An organization wants to analyze historical GCP spending by team and environment. What should they configure?" — Answer: Enable billing export to BigQuery, apply resource labels for team and environment, and query the BigQuery billing dataset with SQL.

---

### Section 2: GCP Recommender Service

The **Recommender** is a GCP service that analyzes your usage and configuration and produces actionable recommendations to improve cost, security, performance, and reliability.

**Cost-related Recommenders:**

- **Idle VM Recommender** — Identifies VMs with very low CPU, network, and disk utilization over the past 14 days. Recommends stopping or deleting idle VMs.
- **VM Rightsizing Recommender** — Identifies VMs that are consistently over-provisioned. Recommends switching to a smaller machine type with projected cost savings.
- **Unattached Disk Recommender** — Identifies persistent disks not attached to any VM for more than 30 days. Recommends deleting or snapshotting them.
- **Idle IP Address Recommender** — Identifies reserved static IP addresses not attached to any resource. Reserved IPs that are not in use still incur hourly charges.
- **Committed Use Discount Recommender** — Analyzes current usage patterns and recommends CUD purchases sized to actual usage, with projected savings.

**Accessing Recommender.** Recommendations appear in the Cloud Console on the relevant resource pages (Compute Engine, Cloud SQL, etc.) and in the Recommender API. Recommendations can be accessed programmatically via `gcloud recommender recommendations list` or the REST API.

**ACE exam pattern:** "A GCP administrator wants to identify over-provisioned VM instances automatically. What service should they use?" — Answer: The VM Rightsizing Recommender in the Recommender service.

---

### Section 3: Cost Optimization Strategies

### Compute Engine

- Use Spot VMs for interruptible batch workloads (up to 91% savings)
- Purchase resource-based CUDs for stable baseline workloads (up to 57% savings)
- Apply SUDs by running VMs continuously when possible
- Use Managed Instance Groups with autoscaling to right-size capacity to demand
- Use the Rightsizing Recommender to downsize over-provisioned VMs
- Prefer E2 machine types for cost-efficiency on general workloads (note: E2 does not receive SUDs)
- Stop VMs during non-business hours for development/test environments using Cloud Scheduler + Cloud Functions

### Cloud Storage

- Use the correct storage class for each access pattern:
  - Standard — frequently accessed data (no minimum storage duration)
  - Nearline — data accessed less than once per month (30-day minimum)
  - Coldline — data accessed less than once per quarter (90-day minimum)
  - Archive — data accessed less than once per year (365-day minimum)
- Configure Object Lifecycle Management to automatically transition objects to lower-cost storage classes as they age, or delete objects after a retention period
- Use regional buckets (not multi-regional) for data that does not require global replication
- Enable compression for text-based objects (JSON, logs, CSV) to reduce storage volume

### Cloud SQL

- Use Committed Use Discounts (spend-based CUDs) for production Cloud SQL instances running continuously
- Stop Cloud SQL development instances outside business hours (cannot stop production instances with replicas)
- Right-size machine types based on actual CPU and memory utilization — Cloud SQL instance costs are dominated by machine type, not storage
- Use read replicas to offload read traffic rather than over-provisioning the primary instance

### BigQuery

- Use on-demand pricing for ad hoc or infrequent queries
- Use flat-rate pricing (slot commitments) for high-volume, predictable query workloads
- Partition tables by date and cluster by commonly filtered columns to reduce bytes scanned per query (billing is per bytes scanned on on-demand pricing)
- Use `bq query --dry_run` to estimate bytes scanned before running expensive queries
- Archive old data to BigQuery long-term storage (data not modified in 90 days automatically qualifies)

---

### Section 4: GCP Free Tier

GCP provides two types of free usage:

**Always Free tier.** Specific quotas of services that are free every month, indefinitely, as long as usage stays within the limits. Key always-free limits include:

- Compute Engine: 1 f1-micro VM in us-west1, us-central1, or us-east1 (1 per month — all three regions combined)
- Cloud Storage: 5 GB of Regional storage in US regions per month
- BigQuery: 10 GB of storage per month; 1 TB of query processing per month
- Cloud Functions: 2 million invocations per month; 400,000 GB-seconds compute time
- Cloud Run: 2 million requests per month; 360,000 GB-seconds compute time
- Pub/Sub: 10 GB of message data per month
- Firestore: 1 GB storage; 50,000 reads, 20,000 writes, 20,000 deletes per day

**Free trial.** New GCP accounts receive a $300 credit valid for 90 days. Credits can be used for any GCP service. When the $300 credit is exhausted or the 90 days expire, the account is either upgraded to a paid account (with user confirmation) or services are suspended. Free trial accounts cannot upgrade to production without manual conversion.

**ACE exam note:** Always Free resources are independent of the $300 credit and continue after the trial expires. The f1-micro always-free VM is a common exam topic — it is limited to one per month across three specific US regions, not one per region.

---

### Section 5: GCP Pricing Calculator

The **GCP Pricing Calculator** is a web tool for estimating costs before provisioning resources. It supports detailed configuration of Compute Engine instances (machine type, storage, networking, sustained use), Cloud SQL, GKE, Cloud Storage, BigQuery, and other services.

Key features:

- Estimate costs with CUDs applied vs. on-demand pricing
- Compare pricing across regions (costs vary by region)
- Export estimates as a PDF or share via URL
- Calculate total estimated monthly cost for a complete architecture

**ACE exam pattern:** "Before deploying a new production GCP environment, a team wants to estimate the monthly cost. What tool should they use?" — Answer: GCP Pricing Calculator.

---

### Section 6: Cost Management Best Practices Summary

The ACE exam tests cost management knowledge through scenario questions about which tool, discount type, or configuration addresses a specific cost problem. The most commonly tested patterns are:

1. **Predictable, continuous workloads** → CUDs (commit, maximize discount)
2. **Variable, unpredictable workloads** → SUDs (no commitment, automatic discount for sustained usage)
3. **Interruptible batch workloads** → Spot VMs (maximum discount, tolerate preemption)
4. **Over-provisioned VMs** → Rightsizing Recommender + downsize machine type
5. **Budget enforcement** → Budget → Pub/Sub → Cloud Function → disable billing
6. **Cost analysis and allocation** → Billing export to BigQuery + resource labels
7. **Infrequently accessed storage** → Object Lifecycle Management to transition to Nearline/Coldline/Archive
8. **Idle resources** → Idle VM Recommender, Unattached Disk Recommender

---

### Module Wrap-Up

This module covered the full GCP cost management toolkit: the billing hierarchy and IAM roles, budget alerts and programmatic cost control, CUDs, SUDs, Spot VMs, billing export to BigQuery, the Recommender service, cost optimization strategies for compute, storage, SQL, and BigQuery, and the GCP free tier.

In Module 16 — the final module — we review all ACE exam domains, work through twenty practice questions, and prepare you for the Associate Cloud Engineer certification exam.

See you there.

---

### PRODUCTION NOTES

- Slide: Billing export to BigQuery setup flow diagram
- Screen share: BigQuery billing dataset — run a sample SQL query showing top costs by project/service
- Slide: Recommender service — five recommender types with icons
- Screen share: Cloud Console — Compute Engine → Recommendations panel showing VM rightsizing suggestion
- Slide: Cloud Storage class comparison table (access frequency, minimum duration, use case)
- Slide: ACE exam cost scenario decision tree (workload type → discount strategy)
- Slide: GCP Always Free tier limits table
