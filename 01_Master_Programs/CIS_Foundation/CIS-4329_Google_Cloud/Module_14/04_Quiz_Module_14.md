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

---

### Question 11 (5 points)

A new GCP engineer asks: "I created a budget alert for $500. After we hit $600 this
month, why are our VMs still running?" Which response is correct?

* A) The VMs are still running because the budget alert was not attached to the
  correct billing account
* B) Cloud Billing budget alerts are notification-only tools; they send emails when
  thresholds are exceeded but do not stop or modify any running resources
* C) The VMs are still running because the team has not acknowledged the alert in
  the Cloud Console
* D) Budget alerts only stop new resource creation; existing resources continue
  running until manually stopped

* **Correct Answer:** B
* **Distractor Analysis:**
  * A) Whether the budget is attached to the correct billing account affects which projects' spending it tracks, but even a correctly configured budget would not stop VMs; the notification-only behavior is fundamental to how budgets work.
  * C) Cloud Billing budget alerts do not require acknowledgment in the Console to take effect; they fire the email notification automatically when the threshold is crossed.
  * D) Budget alerts do not block new resource creation either; they have absolutely no enforcement capability on any GCP API calls or resource operations.

---

### Question 12 (5 points)

Which GCP service provides automated recommendations to right-size an oversized
Compute Engine VM based on its historical CPU and memory utilization?

* A) Cloud Monitoring alert policies with VM metric thresholds
* B) Security Command Center's vulnerability findings
* C) The Recommender service with the `MachineTypeRecommender` recommender type
* D) Cloud Profiler continuous profiling on the VM's processes

* **Correct Answer:** C
* **Distractor Analysis:**
  * A) Cloud Monitoring alert policies fire notifications when metrics cross thresholds; they identify performance anomalies but do not generate machine type change recommendations.
  * B) Security Command Center identifies security vulnerabilities and misconfigurations; it does not analyze compute utilization or recommend cost optimizations.
  * D) Cloud Profiler analyzes CPU and memory usage within application code using instrumentation; it does not produce GCP infrastructure change recommendations.

---

### Question 13 (5 points)

A company has 10 GCP projects all linked to the same billing account. The finance
team wants to receive a single bill but also see a per-project cost breakdown.
Which billing export configuration supports this?

* A) Link each project to its own separate billing account and export each account
  to a separate BigQuery dataset
* B) Keep all projects under one billing account and enable detailed billing export
  to BigQuery; query by `project.id` to see per-project costs
* C) Create 10 separate Cloud Billing Reports dashboards, one per project
* D) Enable Cloud Monitoring billing metrics and filter by project in Metrics Explorer

* **Correct Answer:** B
* **Distractor Analysis:**
  * A) Using separate billing accounts produces separate invoices and complicates centralized payment; the consolidated billing model keeps a single invoice while enabling per-project analysis via BigQuery export.
  * C) Cloud Billing Reports dashboards show costs for the billing account's projects but do not support custom SQL analysis or exporting per-project breakdowns for finance systems.
  * D) Cloud Monitoring does not contain billing cost data; Metrics Explorer shows operational metrics (CPU, latency) but not financial charges.

---

### Question 14 (5 points)

A team purchases a 1-year resource-based Committed Use Discount for 10 vCPUs
of `N2` in `us-central1`. The team subsequently migrates their workload to
`us-east1` N2 VMs. What happens to the CUD?

* A) The CUD automatically transfers to `us-east1` to follow the workload
* B) The CUD continues to apply to any `N2` usage in `us-central1`; since the
  VMs moved to `us-east1`, the committed capacity in `us-central1` is billed
  whether used or not
* C) The CUD is cancelled and a partial refund is issued for the unused months
* D) The CUD is paused until the workload returns to `us-central1`

* **Correct Answer:** B
* **Distractor Analysis:**
  * A) Resource-based CUDs are region-specific; they do not follow workloads to other regions. Separate CUDs must be purchased for each region.
  * C) GCP CUDs are non-cancellable commitments; there is no refund mechanism for unused committed capacity. The commitment must be honored for the full term.
  * D) CUDs are not pausable; the commitment to pay for the reserved capacity in the specified region continues regardless of actual usage.

---

### Question 15 (5 points)

A company's Cloud Billing account shows unexpectedly high network egress charges.
They suspect data is being transferred out of GCP to the internet from a specific
project. Which tool and query approach identifies the exact project and destination
region responsible for the egress charges?

* A) Cloud Monitoring Network dashboard showing bytes transmitted per VM
* B) VPC Flow Logs exported to BigQuery — query by destination IP and project
* C) Cloud Billing detailed export in BigQuery — query by `service.description`,
  `project.id`, and `sku.description` filtering for `Egress`
* D) Cloud Logging Admin Activity logs — filter for network resource modifications

* **Correct Answer:** C
* **Distractor Analysis:**
  * A) Cloud Monitoring shows network bytes transmitted as an operational metric but does not contain cost data; you can see which VM sent the most bytes but not the corresponding dollar charges or destination region.
  * B) VPC Flow Logs show network flow records (source/destination IP, bytes) and can help understand traffic patterns, but they do not contain billing cost data; identifying the dollar amount of egress charges requires the billing export.
  * D) Admin Activity audit logs record GCP API calls that create or modify resources; they do not contain network traffic or billing cost data.

---

### Question 16 (5 points)

Which Compute Engine VM pricing model applies a discount automatically and
incrementally as a VM runs longer within a calendar month, with no commitment
required?

* A) Committed Use Discount (CUD)
* B) Spot VM pricing
* C) Sustained Use Discount (SUD)
* D) Extended Use Discount (EUD)

* **Correct Answer:** C
* **Distractor Analysis:**
  * A) CUDs require an explicit 1- or 3-year commitment purchase; they are not automatic and do not apply incrementally based on monthly runtime.
  * B) Spot VM pricing is a flat reduced rate (up to 91% off) for preemptible VMs; it is not a discount that increases based on runtime duration within a month.
  * D) Extended Use Discount is not a GCP pricing concept; this option is a distractor.

---

### Question 17 (5 points)

A team enables the Cloud Billing standard export to BigQuery. After 48 hours, they
run a query but find the BigQuery table is empty. What is the most likely cause?

* A) Standard billing export has a 48-hour delay; data will appear after 72 hours
* B) The BigQuery dataset is in a different region than the billing account
* C) Billing export was enabled but the BigQuery dataset was created after the
  export was configured, causing the export to fail silently
* D) The BigQuery dataset and the billing export must be in the same GCP project
  as the billing account's linked projects

* **Correct Answer:** C
* **Distractor Analysis:**
  * A) Standard billing export typically populates within a few hours; a 48-hour wait is not a documented delay. Empty data after 48 hours indicates a configuration error, not a propagation delay.
  * B) The billing export to BigQuery does not require the dataset to be in any specific region relative to the billing account; the export works across regions.
  * D) The BigQuery dataset for billing export does not need to be in the same project as the linked projects; it only needs to be accessible to the Cloud Billing export service account.

---

### Question 18 (5 points)

A startup uses GCP primarily for Cloud Run and Cloud Storage. Neither service
uses Compute Engine VMs. Which discount type can reduce their Cloud Run costs?

* A) Sustained Use Discounts — automatically applied to Cloud Run requests above
  25% monthly utilization
* B) Resource-based Committed Use Discounts for Cloud Run vCPU and memory
* C) Spend-based Committed Use Discounts — commit to a minimum monthly dollar
  spend on Cloud Run
* D) Neither CUDs nor SUDs apply to Cloud Run; only on-demand pricing is
  available

* **Correct Answer:** C
* **Distractor Analysis:**
  * A) Sustained Use Discounts apply to Compute Engine N1 and N2 VMs only; they do not apply to Cloud Run, which is billed on actual request duration.
  * B) Resource-based CUDs are specific to Compute Engine machine types; they do not apply to Cloud Run, which uses serverless pricing.
  * D) Spend-based CUDs do apply to services like Cloud Run; a minimum monthly spend commitment provides a percentage discount on actual usage.

---

### Question 19 (5 points)

A team uses labels to track costs by environment (`env: production`, `env: staging`).
They query the BigQuery billing export and find that many resources show no label
data. What is the most likely reason?

* A) Labels are not exported to the BigQuery billing dataset
* B) Resources created before labels were applied, or resources that do not support
  labeling (e.g., some network resources), do not have label data in the export
* C) The BigQuery billing export only includes label data for Compute Engine resources
* D) Labels must be applied at the billing account level, not the resource level, to
  appear in billing exports

* **Correct Answer:** B
* **Distractor Analysis:**
  * A) Labels are included in the BigQuery billing export in the `labels` repeated field; absence of label data indicates the resources were not labeled, not that labels are excluded from the export.
  * C) The BigQuery billing export includes labels for all GCP resources that support labeling, not just Compute Engine; Storage buckets, BigQuery datasets, Cloud Run services, and many others support labels.
  * D) Labels are applied at the resource level (VM, bucket, etc.), not at the billing account level; applying them at the billing account level is not how GCP resource labeling works.

---

### Question 20 (5 points)

An organization wants to automatically disable billing on a project when its
monthly spend exceeds $1,000 to prevent runaway costs. A budget alert with a
$1,000 threshold is already configured. What additional configuration is required?

* A) Enable the "auto-stop" option on the budget configuration
* B) Configure a Pub/Sub topic on the budget notification, then deploy a Cloud
  Function that calls `billing.projects.updateBillingInfo` to unlink the billing
  account when triggered
* C) Set a project-level spending quota to $1,000 in the GCP Console
* D) Enable VPC Service Controls on the project to block API calls after the
  budget is exceeded

* **Correct Answer:** B
* **Distractor Analysis:**
  * A) There is no "auto-stop" option on Cloud Billing budget alerts; budgets are notification-only by default and require custom automation for enforcement.
  * C) GCP does not have a "spending quota" at the project level; quotas in GCP limit API call rates and resource quantities, not dollar amounts.
  * D) VPC Service Controls restrict which networks and identities can access GCP services; they do not have any integration with billing spend thresholds.
