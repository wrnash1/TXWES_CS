# Video Script: Module 14 — Cost Management and Billing (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 14. I am Professor Nash. This module covers GCP Cost Management
and Cloud Billing — how GCP charges for services, how to control and forecast costs,
and how to prevent billing surprises in a production environment.

Cost management is tested on the ACE exam in scenario questions about billing accounts,
budget alerts, discount types, and billing data analysis. It is also a real operational
skill — cloud costs can grow unexpectedly if not actively managed.

By the end of this two-part video you will understand the GCP billing hierarchy, budget
alerts, committed use vs. sustained use discounts, Spot VMs, billing export to BigQuery,
the Recommender service, and cost optimization strategies for common GCP services.

---

### Section 1: GCP Billing Hierarchy

GCP billing has three levels:

```text
Organization
  └── Billing Account
        └── Projects
              └── Resources
```

- **Billing Account** — the entity that receives the invoice; linked to a payment method
  (credit card or bank transfer); managed at the organization level
- **Project** — each project is linked to exactly one billing account; all resource costs
  in the project are charged to that billing account
- **Resources** — VMs, storage buckets, BigQuery queries, etc.; costs accumulate at the
  resource level and roll up to the project and billing account

A single billing account can be linked to many projects. This is the standard pattern in
organizations — one billing account for the entire organization, with different projects
for different teams or environments.

#### Billing Account IAM Roles

| Role | Description |
|---|---|
| `roles/billing.admin` | Full control of the billing account; can link/unlink projects |
| `roles/billing.viewer` | View costs and invoices; cannot make changes |
| `roles/billing.projectManager` | Link and unlink projects to billing accounts |
| `roles/billing.costsManager` | Create and manage budgets |

```bash
# List billing accounts accessible to the current user
gcloud billing accounts list

# Describe a specific billing account
gcloud billing accounts describe BILLING_ACCOUNT_ID

# Link a project to a billing account
gcloud billing projects link PROJECT_ID \
  --billing-account=BILLING_ACCOUNT_ID

# View the billing account linked to a project
gcloud billing projects describe PROJECT_ID
```

---

### Section 2: Budget Alerts

A Cloud Billing **budget** defines a spending target and sends email notifications when
spending reaches configured thresholds.

Key facts about budgets:

- **Budgets are notification-only** — they do NOT stop resource usage or cap spending
- **Thresholds** — configure multiple percentage alerts (e.g., 50%, 90%, 100%, 110%)
- **Notification channels** — email to billing administrators; optionally Pub/Sub for
  programmatic response
- **Budget scope** — can cover the entire billing account, a specific project, or
  specific services/labels

```bash
# Create a budget with a 90% alert threshold
gcloud billing budgets create \
  --billing-account=BILLING_ACCOUNT_ID \
  --display-name="Monthly Production Budget" \
  --budget-amount=5000USD \
  --threshold-rule=percent=0.5 \
  --threshold-rule=percent=0.9 \
  --threshold-rule=percent=1.0
```

#### Programmatic Budget Response

To actually stop resources when a budget is exceeded:

1. Enable Pub/Sub notifications on the budget
2. Create a Pub/Sub topic for budget notifications
3. Deploy a Cloud Function subscribed to the topic
4. The function calls the GCP API to stop VMs, disable billing, or take other action

This is a common ACE exam scenario: "Budget alerts alone are not enough to stop
overspending — you need a Pub/Sub + Cloud Function integration."

---

### Section 3: Discount Types

GCP offers several discount models for Compute Engine VMs:

#### On-Demand Pricing

Pay the standard per-second rate for each VM. No commitment required. Suitable for
development, variable workloads, and new applications where usage is unpredictable.

#### Sustained Use Discounts (SUDs)

GCP automatically reduces the per-hour rate as a VM runs longer within a calendar month:

| Hours of use (% of month) | Discount |
|---|---|
| 0–25% | 0% (full price) |
| 25–50% | ~20% |
| 50–75% | ~40% |
| 75–100% | ~30% (net: ~30% off full month) |

SUDs are applied automatically — no action required. They apply to N1 and N2 machine
types but NOT to E2, Spot/Preemptible, or custom machine types on some families.

#### Committed Use Discounts (CUDs)

Purchase a 1-year or 3-year commitment for a specific amount of vCPU and memory in a
region. In exchange, GCP charges at a significantly reduced rate:

- **1-year commitment**: up to ~37% discount
- **3-year commitment**: up to ~57% discount

CUDs apply to any VM using the committed resource type — you are not locked to specific
VM names. Resource-based CUDs cover vCPU, memory, GPUs, and SSDs. Spend-based CUDs
cover Cloud SQL and Cloud Spanner.

```bash
# Purchase a committed use discount (via Console or API)
# gcloud compute commitments create is the CLI method
gcloud compute commitments create my-commitment \
  --plan=TWELVE_MONTH \
  --region=us-central1 \
  --resources=vcpu=32,memory=128GB
```

#### Spot VMs (formerly Preemptible VMs)

Spot VMs use excess GCP capacity at up to 91% discount. Trade-off: GCP can preempt
(terminate) a Spot VM at any time with a 30-second warning.

Use Spot VMs for:

- Batch processing jobs that can be restarted from a checkpoint
- Fault-tolerant data processing (Dataproc, Dataflow)
- Rendering and simulation workloads

Do NOT use Spot VMs for:

- Databases or stateful services
- Web servers requiring guaranteed uptime
- Jobs that cannot tolerate interruption

```bash
# Create a Spot VM
gcloud compute instances create my-spot-vm \
  --machine-type=n2-standard-4 \
  --provisioning-model=SPOT \
  --instance-termination-action=STOP \
  --zone=us-central1-a
```

---

### Section 4: GCP Pricing Calculator

The **Cloud Pricing Calculator** at `cloud.google.com/products/calculator` estimates
monthly costs before provisioning resources. Use it to:

- Compare VM machine types and pricing models (on-demand vs. CUD vs. Spot)
- Estimate Cloud Storage costs by class, region, and expected operations
- Model BigQuery costs based on expected query volumes
- Compare region pricing (pricing varies by region)

The calculator supports saving and sharing estimates. For the ACE exam, know that the
Pricing Calculator is a forward-looking estimation tool — it does not analyze historical
actual spending.

---

### Closing — Part 1

In Part 1 we covered:

- GCP billing hierarchy: organization → billing account → project → resource
- Billing account IAM roles
- Budget alerts: notification-only; Pub/Sub + Cloud Function for enforcement
- Discount types: on-demand, SUDs (automatic), CUDs (commitment), Spot VMs (90% off)
- GCP Pricing Calculator for cost estimation

In Part 2 we cover billing export to BigQuery, the Recommender service, label-based
cost attribution, Cloud Storage cost optimization, and ACE exam patterns.

See you in Part 2.
