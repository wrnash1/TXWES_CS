# Reading Guide: Module 14 – Cost Management and Billing
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 14 – Cost Management and Billing**! Managing cloud costs is a critical operational responsibility for any GCP administrator. This module covers Cloud Billing accounts, budgets and alerts, the Pricing Calculator, committed use discounts, sustained use discounts, and cost optimization strategies for Compute Engine, Cloud Storage, and managed services. The ACE exam tests your ability to configure billing controls, interpret billing reports, and recommend cost optimization strategies for given workloads.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Cloud Billing Account**: A GCP resource that defines who pays for a set of GCP projects. A billing account is linked to one or more projects. Billing accounts are managed at the organization level and can be linked to a Google payments profile (credit card or invoicing). IAM roles on a billing account control who can view costs (`roles/billing.viewer`) or manage the account (`roles/billing.admin`).

*   **Budget and Alerts**: A Cloud Billing feature that sends email notifications when spending reaches defined thresholds (e.g., 50%, 90%, 100% of budget). Budgets are informational by default — they do not stop resource usage when the budget is exceeded. To take programmatic action, configure a Pub/Sub notification on the budget and connect a Cloud Function to cap spending.

*   **Committed Use Discounts (CUDs)**: Discounts of up to 57% on Compute Engine VM resources in exchange for a 1-year or 3-year commitment to a specific amount of vCPU and memory. CUDs are applied at the project level for resource-based CUDs or at the billing account level for spend-based CUDs. CUDs do not require choosing a specific VM instance — they apply to any VM using the committed resource type in the committed region.

*   **Sustained Use Discounts (SUDs)**: Automatic discounts applied by GCP when a Compute Engine VM runs for more than 25% of a calendar month. No commitment is required — the discount applies automatically and increases incrementally as usage crosses 25%, 50%, and 75% of the month. SUDs apply to N1 and N2 machine types but not to Spot/Preemptible VMs or E2 machine types.

*   **Cloud Pricing Calculator**: A web tool at `cloud.google.com/products/calculator` that estimates monthly GCP costs before provisioning resources. Use the Pricing Calculator to compare machine types, storage classes, and regions before committing to a configuration.

*   **Recommender**: A GCP service that analyzes usage patterns and makes recommendations to reduce costs and improve security. The VM rightsizing recommender identifies oversized VMs and suggests smaller machine types. The IAM recommender identifies overly permissive roles. Recommender findings are surfaced in the Cloud Console and available via the Recommender API.

---

### 2. Certification Exam Tips

*   **Budgets do not stop resource usage**: The ACE exam frequently tests this. A budget alert sends a notification email — it does not cap spending or shut down VMs. If you need to actually stop resources when a budget is exceeded, you must configure a Pub/Sub budget notification and a Cloud Function that calls the GCP API to stop or delete resources.

*   **CUD vs. SUD — commitment vs. automatic**: CUDs require an explicit 1- or 3-year commitment and provide larger discounts. SUDs are automatic and require no commitment but provide smaller discounts. The exam tests knowing which discount type requires a commitment and which applies automatically.

*   **Spot VMs for batch workloads**: Spot VMs (formerly Preemptible VMs) cost up to 91% less than on-demand VMs but can be preempted by GCP at any time with a 30-second warning. Use Spot VMs for fault-tolerant batch jobs, rendering, or data processing that can be restarted. Do not use Spot VMs for stateful services or databases.

*   **Export billing data to BigQuery for analysis**: The ACE exam tests billing data analysis. To run SQL queries against billing data (e.g., "show me top 10 projects by spend last month"), configure a billing export to BigQuery. Standard Billing Export and Detailed Usage Cost Export are both available. Once configured, data flows continuously and can be queried with BigQuery standard SQL.

*   **Study Resource**: The freeCodeCamp ACE course covers Cloud Billing structure, budget configuration, and cost optimization strategies with hands-on examples: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Cost Management chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Cloud Billing overview including billing account structure, budgets, alerts, and billing export to BigQuery: [Cloud Billing Overview](https://cloud.google.com/billing/docs/overview). The budget alert behavior (notification-only, not enforcement) is directly exam-relevant.
*   **Required Reading**: Review committed use discounts and sustained use discounts to understand the cost optimization options available for Compute Engine workloads: [VM discounts overview](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).
*   **Required Video**: Watch the Cost Management segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Billing and Cost Management chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a budget alert, export billing data to BigQuery, and review VM rightsizing recommendations. Key commands to practice:

*   `gcloud billing budgets create --billing-account=BILLING_ACCOUNT_ID --display-name="Monthly Budget" --budget-amount=500USD --threshold-rule=percent=0.9` — creates a budget with a 90% alert threshold
*   `gcloud billing projects link PROJECT_ID --billing-account=BILLING_ACCOUNT_ID` — links a project to a billing account
*   `gcloud recommender recommendations list --project=PROJECT_ID --location=us-central1 --recommender=google.compute.instance.MachineTypeRecommender` — lists VM rightsizing recommendations
*   `gcloud billing accounts list` — lists all billing accounts accessible to the current user

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Billing Overview](https://cloud.google.com/billing/docs/overview) documentation page.
- [ ] Read the [VM discounts overview](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) documentation page.
- [ ] Watch the Cost Management segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a budget alert and review VM rightsizing recommendations.
- [ ] Proceed to the weekly quiz.

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — Cloud Billing Budgets and Alerts**
<https://cloud.google.com/billing/docs/how-to/budgets>
Complete guide to creating budget alerts including per-project scope, threshold rules, Pub/Sub notification configuration for programmatic enforcement, and the critical distinction between notification-only budgets and actual spending caps.

**2. Google Cloud Documentation — Sustained Use and Committed Use Discounts**
<https://cloud.google.com/compute/docs/sustained-use-discounts>
Detailed explanation of how Sustained Use Discounts automatically apply to N1/N2 VMs at 25%/50%/75% monthly thresholds, and how Committed Use Discounts provide larger savings with 1-year or 3-year commitments — both are high-frequency ACE exam topics.

**3. Google Cloud Documentation — Export Billing Data to BigQuery**
<https://cloud.google.com/billing/docs/how-to/export-data-bigquery>
Step-by-step setup guide for enabling Cloud Billing export to BigQuery, including the dataset location requirements, the difference between Standard and Detailed usage exports, and example SQL queries for analyzing costs by project, service, and label.
