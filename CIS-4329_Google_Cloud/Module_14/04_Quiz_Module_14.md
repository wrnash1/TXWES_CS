# Quiz: Module 14 — Cost Management and Billing

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

**Question 1**
Your finance team has set a monthly Cloud Billing budget of $5,000 for a production project. You have configured budget alerts at 50%, 90%, and 100% thresholds with email notifications to the billing administrators. Midway through the month, spending reaches $5,500 — 110% of budget. What actually happens to the running GCP resources?

A) GCP automatically stops all Compute Engine VMs and Cloud SQL instances in the project to prevent further charges.
B) GCP sends an email alert notification to the billing administrators, but all resources continue running and charges continue to accumulate.
C) GCP suspends the project and places it in a read-only state until the billing administrator increases the budget.
D) GCP applies a spending cap that throttles API calls for the project until the next billing cycle resets the counter.

*   **Correct Answer:** B) GCP sends an email alert notification to the billing administrators, but all resources continue running and charges continue to accumulate.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Billing budget alerts are notification-only — they never automatically stop, modify, or delete any GCP resources. To programmatically cap spending, you must configure a Pub/Sub notification on the budget and build a Cloud Function that calls the GCP API to stop resources when the threshold is exceeded.
    *   *Why C is incorrect:* GCP does not automatically suspend projects when a budget is exceeded. Projects are only suspended for non-payment of an invoice or violation of terms of service, not for exceeding a self-configured budget threshold.
    *   *Why D is incorrect:* There is no API throttling mechanism associated with budget alerts. Budget alerts are a reporting and notification feature only — they have no enforcement capability on API call rates or resource usage.

---

**Question 2**
Your team runs a data analytics workload on a fleet of Compute Engine N2 VMs. The VMs run continuously 24 hours a day, 7 days a week, every day of the month. You want to reduce costs without changing the workload architecture or committing to specific VM instance names. Which discount type provides automatic cost reduction with no action required?

A) Preemptible VM pricing — switch all VMs to preemptible to get up to 91% discount automatically.
B) Sustained Use Discounts (SUDs) — GCP automatically applies incremental discounts when N2 VMs run for more than 25% of a calendar month.
C) Committed Use Discounts (CUDs) — purchase a 1-year commitment for the vCPU and memory resources used by the fleet.
D) Custom machine types — resize the VMs to custom configurations to eliminate wasted resources and reduce the hourly rate.

*   **Correct Answer:** B) Sustained Use Discounts (SUDs) — GCP automatically applies incremental discounts when N2 VMs run for more than 25% of a calendar month.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Preemptible VMs provide large discounts but can be terminated by GCP at any time with only a 30-second warning. For a continuously running analytics workload that cannot tolerate interruption, Preemptible VMs are not appropriate — and they require explicitly selecting the preemptible option, not an automatic discount on existing VMs.
    *   *Why C is incorrect:* CUDs do provide discounts on N2 VMs, and for a 24/7 workload they would provide larger savings than SUDs. However, the question specifically asks for a discount that requires no action — SUDs are automatic. CUDs require an explicit commitment purchase, making B the answer that satisfies the "no action required" constraint.
    *   *Why D is incorrect:* Custom machine types can reduce costs by right-sizing VMs, but this requires modifying the VM configuration (stopping and resizing each instance), which changes the workload architecture. It does not provide an automatic discount on the existing configuration.

---

**Question 3**
Your organization wants to analyze GCP spending trends by service, project, and label over the past 12 months. The finance team wants to run custom SQL queries to build monthly cost reports and identify the top cost drivers. Which configuration enables this analysis?

A) Enable detailed billing export to a BigQuery dataset in Cloud Billing settings, then use BigQuery standard SQL to query the exported billing data.
B) Use the Cloud Billing Reports page in the Cloud Console, which provides an interactive dashboard with 12 months of cost history and export to CSV.
C) Configure a Cloud Monitoring dashboard with a billing metric and set the retention window to 365 days for historical analysis.
D) Use the GCP Pricing Calculator to retroactively calculate what each service should have cost based on usage estimates.

*   **Correct Answer:** A) Enable detailed billing export to a BigQuery dataset in Cloud Billing settings, then use BigQuery standard SQL to query the exported billing data.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* The Cloud Billing Reports page provides a useful visual dashboard but does not support custom SQL queries. It shows pre-built charts with limited filtering and cannot be used to run ad hoc analysis like "top 10 projects by spend, broken down by service, for each of the last 12 months." BigQuery export enables full SQL flexibility.
    *   *Why C is incorrect:* Cloud Monitoring stores operational metrics (CPU, latency, request rates) — it does not ingest Cloud Billing cost data. Billing costs are not available as Cloud Monitoring metrics and cannot be queried there. The billing export to BigQuery is the correct mechanism for cost data analysis.
    *   *Why D is incorrect:* The Pricing Calculator is a forward-looking estimation tool — it calculates projected costs for resources you are considering provisioning. It cannot retroactively analyze actual historical spending, which requires billing export data.

---

**Question 4**
Your company runs a batch genomics processing workload on Compute Engine. The jobs run for 6–8 hours, can be restarted from a checkpoint if interrupted, and do not have strict timing requirements. The current monthly cost for the VM fleet is $12,000. Which compute pricing option would most significantly reduce this cost?

A) Purchase 3-year Committed Use Discounts for the vCPU and memory capacity used by the batch VMs.
B) Switch the batch VMs to Spot VMs (formerly Preemptible VMs), accepting that jobs may be interrupted and restarted from checkpoints.
C) Enable sustained use discounts by ensuring the VMs run for at least 25% of each calendar month.
D) Move the batch workload to a custom machine type with fewer vCPUs to reduce the per-hour cost.

*   **Correct Answer:** B) Switch the batch VMs to Spot VMs (formerly Preemptible VMs), accepting that jobs may be interrupted and restarted from checkpoints.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 3-year CUDs provide up to 57% discount for long-term committed workloads. However, batch processing that only runs for 6–8 hours per job is not a continuously running workload — committing to 3 years of 24/7 capacity for an intermittent batch job would result in paying for committed capacity that is mostly idle. Spot VMs provide up to 91% discount and are specifically designed for interruptible batch workloads.
    *   *Why C is incorrect:* SUDs apply automatically when VMs run for more than 25% of a calendar month. A batch workload that runs for a few hours per job does not run continuously enough to benefit from SUDs. Spot VMs provide far larger discounts for the actual hours the batch jobs run.
    *   *Why D is incorrect:* Rightsizing to a smaller machine type reduces costs proportionally to the size reduction — a 50% smaller VM costs 50% less. Spot VMs cost up to 91% less than the same on-demand VM regardless of size. For a fault-tolerant batch workload, Spot VMs provide a much larger cost reduction than rightsizing alone.

---

**Question 5**
You are reviewing your GCP billing report and notice that a development project has unexpectedly high Cloud Storage costs — $800 this month versus the typical $50. You need to identify which Cloud Storage bucket is generating the excess charges and what type of storage operations are responsible. Which tool provides the most granular breakdown to investigate this?

A) Cloud Monitoring — create a dashboard showing Cloud Storage byte counts per bucket to identify the largest buckets.
B) Cloud Billing detailed export in BigQuery — query the exported data filtered by service `Cloud Storage`, grouped by `resource.labels.bucket_name` and `sku.description` to see costs per bucket and operation type.
C) The Cloud Billing Reports page — use the service filter to select Cloud Storage and view the cost breakdown by project.
D) Security Command Center — run a storage asset inventory scan to list all buckets and their sizes.

*   **Correct Answer:** B) Cloud Billing detailed export in BigQuery — query the exported data filtered by service `Cloud Storage`, grouped by `resource.labels.bucket_name` and `sku.description` to see costs per bucket and operation type.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Monitoring tracks Cloud Storage operational metrics (bytes stored, request counts) but does not show cost data. Knowing which bucket is the largest does not directly identify which bucket is the most expensive — costs depend on storage class, operation type (Class A vs. Class B), and egress, not just data volume.
    *   *Why C is incorrect:* The Cloud Billing Reports page can show Cloud Storage costs at the project and SKU level, but it does not provide bucket-level cost attribution. You can see that Class A operations cost $400, but you cannot see which specific bucket generated those operations without the BigQuery detailed export.
    *   *Why D is incorrect:* Security Command Center's asset inventory lists storage buckets and their configurations (public access, encryption settings) — it is a security posture tool, not a cost analysis tool. It does not show billing charges, operation counts, or cost breakdowns by bucket.

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 6

A company wants to attribute GCP costs to individual teams for chargeback purposes.
The finance team needs to run SQL queries to see monthly spending broken down by team.
What is the correct implementation?

- A) Create separate GCP projects for each team; view costs by project in the Cloud
  Billing Reports page
- B) Apply resource labels with a `team` key to all billable resources, enable detailed
  billing export to BigQuery, and query by the `labels.value` column
- C) Assign each team a separate billing account and link their projects to it
- D) Use Cloud Monitoring to create a cost dashboard filtered by resource owner

Correct answer: B — Resource labels allow cost attribution within a project. When
detailed billing export to BigQuery is enabled, label data appears as an array in the
`labels` column, enabling SQL queries like `WHERE labels.key = 'team'`. Creating
separate billing accounts per team is an option but adds administrative overhead and
does not enable SQL analysis of costs. Cloud Monitoring does not contain billing data.

---

### Question 7

A development team runs CI/CD test jobs on Compute Engine VMs. The jobs take 2–4 hours,
can restart from any failure point, and run during business hours only. The team wants
to reduce the compute cost for these test jobs by the maximum amount possible. Which
option is most cost-effective?

- A) Purchase a 1-year committed use discount for the vCPU and memory used by the VMs
- B) Enable sustained use discounts by ensuring the VMs run for more than 25% of each
  month
- C) Switch the test VMs to Spot VM provisioning model
- D) Move the test VMs to the cheapest region regardless of latency

Correct answer: C — Spot VMs cost up to 91% less than on-demand pricing and are ideal
for workloads that can tolerate interruption and restart. CI/CD test jobs that can restart
from any failure point match this pattern exactly. CUDs would require paying for committed
capacity even during off-hours when the VMs are not running, making them less efficient
for part-time workloads. SUDs require VMs running more than 25% of the month, which may
not apply to business-hours-only workloads.

---

### Question 8

A team member asks: "We set up a Cloud Billing budget for $1,000. Why are we still being
charged $1,200 this month?" What is the correct explanation?

- A) The budget was configured incorrectly; a properly configured budget would have
  stopped charges at $1,000
- B) Cloud Billing budget alerts are notification-only and do not prevent resource usage
  or cap charges; the budget sends alerts but does not stop any services
- C) The overage is automatically added to next month's budget as a credit
- D) The 20% overage is within the allowed variance; GCP automatically approves up to
  20% over any configured budget

Correct answer: B — This is the most commonly misunderstood Cloud Billing concept. A
budget is a notification tool, not an enforcement mechanism. When spending exceeds the
budget, GCP sends configured alerts but continues charging for all running resources.
To actually stop charges at a threshold, you must configure a Pub/Sub notification on
the budget and build a Cloud Function that calls the GCP API to stop resources or disable
billing when triggered. There is no automatic credit, variance allowance, or enforcement.

---

### Question 9

Your organization uses GCP across multiple teams. Each team has its own GCP project but
all projects share one billing account. A new compliance requirement mandates that each
team's cloud spending must not exceed a defined monthly limit, and teams must be
automatically notified when they reach 80% of their limit. Which design meets this
requirement?

- A) Create one organization-wide budget with a single 80% threshold; all billing
  administrators receive the notification
- B) Create a separate per-project budget for each team's project with an 80% threshold
  rule; configure notifications to each team's billing contact
- C) Create a Cloud Monitoring alert that fires when project spending exceeds 80% of the
  limit
- D) Set the project-level billing account quota to limit spending per project

Correct answer: B — Cloud Billing budgets support per-project scope. Creating a separate
budget for each team's project, with thresholds configured to the team's limit and
notifications routed to the team's contact, is the correct implementation. A single
organization-wide budget would alert all admins together and not track individual team
limits. Cloud Monitoring does not contain billing spend metrics. Project-level billing
quotas are not a billing feature — GCP does not provide a "spend cap" quota at the
project level.

---

### Question 10

A data engineering team stores 200 TB of log files in a Cloud Storage Standard bucket.
The files are queried heavily during the first 7 days after upload, occasionally in the
following 30 days, and almost never after 60 days. The team wants to minimize storage
costs without changing how files are accessed. Which solution is correct?

- A) Move all files to Coldline storage to minimize monthly storage cost
- B) Configure Object Lifecycle Management rules: transition to Nearline after 7 days,
  Coldline after 30 days, and optionally Archive after 365 days
- C) Enable versioning on the bucket to deduplicate files and reduce storage size
- D) Create a second bucket in a cheaper region and copy old files to it

Correct answer: B — Object Lifecycle Management automatically transitions objects to
cheaper storage classes as they age, matching the access pattern. Standard is appropriate
for the first 7 days; Nearline ($0.01/GB) for files accessed monthly; Coldline
($0.004/GB) for files rarely accessed after 30 days. Moving everything immediately to
Coldline would incur high retrieval costs for the actively queried recent files. Bucket
versioning does not deduplicate content — it keeps multiple versions of each object,
increasing storage. Copying to a different region adds egress costs and operational
complexity.
