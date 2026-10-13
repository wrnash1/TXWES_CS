# Discussion: Module 10 — Cloud Operations: Monitoring and Logging

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This discussion asks you to design an observability strategy for a production application
on GCP. You will apply the monitoring, logging, and alerting concepts from Module 10 to
a realistic scenario, then reflect on a real or hypothetical observability challenge.

**Initial post due**: Thursday at 11:59 PM Central

**Peer responses due**: Sunday at 11:59 PM Central

---

### Scenario

A healthcare technology company has deployed a patient portal on Google Cloud. The
platform includes:

- A fleet of 20 Compute Engine VMs running the web application behind a load balancer
- A Cloud SQL PostgreSQL database
- A Cloud Storage bucket storing patient documents
- A Cloud Functions function that processes uploaded documents

The security and compliance team has three requirements:

1. All administrative actions (resource create, modify, delete) must be retained for
   at least 2 years for HIPAA audit purposes
2. The operations team must receive an alert within 5 minutes when average CPU
   utilization across the VM fleet exceeds 75% for more than 3 consecutive minutes
3. All application errors (HTTP 500 responses) must be tracked and the team must be
   notified when the error rate exceeds 10 per minute

The platform currently has no observability configuration beyond GCP's default logging.

---

### Response Requirements

#### Part 1: Audit Log Retention Strategy

For requirement 1, design a solution using Cloud Logging. Explain:

- Which audit log type captures administrative actions and what its default retention is
- Why the default retention is insufficient for HIPAA compliance (2-year requirement)
- The specific Cloud Logging resources you would create to achieve 2-year retention,
  including the sink destination and any permissions that must be granted

Limit to 4–5 sentences.

#### Part 2: CPU Alerting Policy Design

For requirement 2, describe the complete alerting policy configuration:

- The metric you would monitor and any aggregation needed to compute fleet-wide average
- The threshold, comparison, and duration settings
- The notification channel type you would use

Explain your duration choice — why 3 minutes instead of alerting immediately?
Limit to 4–5 sentences.

#### Part 3: HTTP 500 Error Rate Alert

Requirement 3 involves an application-level metric that does not exist as a native
Cloud Monitoring metric. Describe the two-step approach to create this alert:

- Step 1: What Cloud Logging feature creates a countable metric from log entries?
- Step 2: How do you use that metric in an alerting policy?
- What log filter would you write to count only HTTP 500 responses from the VM fleet?

Limit to 4–5 sentences.

#### Part 4: Reflection

Describe a monitoring or logging challenge you have encountered in your own work,
coursework, or personal projects. What was missing in the observability setup that made
it difficult to diagnose or respond to problems? How would the tools covered in Module 10
have helped? (3–5 sentences; hypothetical scenarios are acceptable.)

---

### Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Correct audit log retention strategy with sink details | 25 |
| Part 2: Complete alerting policy design with duration justification | 25 |
| Part 3: Log-based metric approach with correct log filter | 25 |
| Part 4: Thoughtful reflection | 10 |
| Peer response 1: Substantive technical engagement | 7 |
| Peer response 2: Substantive technical engagement | 8 |
| **Total** | **100** |

---

### Peer Response Guidelines

A substantive peer response does at least one of the following:

- Suggests a more specific log filter or a different sink destination and explains why
- Identifies a gap in the alerting policy design (e.g., missing notification channel
  type, incorrect aggregation for fleet-wide average)
- Points out a compliance consideration the original poster did not address
- Shares a related monitoring pattern or tool they have used in practice

---

### Discussion Hints

For Part 1: The default `_Required` bucket retention is 400 days. HIPAA requires 2 years
(approximately 730 days). Think about what happens to logs after 400 days if you only
use the default bucket, and what sink destination would give you control over long-term
retention.

For Part 2: A fleet-wide average requires aligning all VM metrics and computing the mean
across the group. Consider whether you want to alert when the mean exceeds the threshold
or when any individual VM exceeds it — these are different alert designs with different
operational meanings.

For Part 3: The phrase "log-based metric" is the key. You cannot alert on something that
is not a metric. The log filter must target the correct resource type and HTTP status in
the request log format used by your web server.
