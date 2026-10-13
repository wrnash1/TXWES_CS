# Discussion Forum: Module 15 — Database Automation and Monitoring

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

Operational maturity in database management means more than keeping databases running —
it means knowing when they are unhealthy before users do, automating repetitive tasks
to prevent human error, and treating infrastructure configuration as code. This
discussion invites you to design operational frameworks for realistic production environments.

**Due date**: See course schedule in Canvas.

**Grading**: See rubric at the bottom of this prompt.

---

## Primary Post Prompt

Choose **one** of the following scenarios and write a primary post of at least
250 words addressing all questions.

---

### Scenario A — The Monitoring Gap

A fintech startup has 12 Cloud SQL instances supporting their payment processing
platform. They currently have no Cloud Monitoring configuration beyond the default
GCP dashboard. Last week, a Cloud SQL instance's disk filled to 100%, causing
4 hours of downtime. The incident post-mortem identified that disk usage had been
growing steadily for 3 weeks before the outage.

Address the following:

1. Design a complete monitoring strategy for the 12 Cloud SQL instances. List at
   least six distinct metric alerts (not just CPU and disk) you would configure,
   specifying the metric name, threshold, alert duration, and justification for each.
   Explain how you would organize these alerts into an incident response workflow.

2. A single dashboard should show the health of all 12 instances at a glance.
   Describe what panels (charts, gauges, tables) you would include and how you
   would structure the dashboard for an on-call engineer to quickly identify which
   instance needs attention.

3. The disk-full incident could have been prevented by enabling Cloud SQL's automatic
   storage increase feature. Explain what this feature does, its limitations, and
   the monitoring alert that provides an early warning before storage increase is
   needed — even with auto-increase enabled.

---

### Scenario B — The IaC Adoption

A mid-size logistics company has 30 GCP database resources created manually through
the GCP console over the past 2 years: Cloud SQL instances, BigQuery datasets, and
Cloud Spanner instances. The new engineering manager wants to adopt Terraform so that
all future changes are code-reviewed, auditable, and reproducible.

Address the following:

1. Describe the process for migrating the 30 existing resources into Terraform
   management without destroying and recreating them. What Terraform command is
   used, what risks exist during the migration, and how would you validate that
   Terraform now accurately represents the actual state of each resource?

2. The team has three environments: development, staging, and production. Design a
   Terraform project structure that manages all three environments with shared
   modules but separate state files. Include specific directory structure and explain
   how you would prevent a `terraform apply` in production from accidentally
   targeting development resources.

3. Two junior engineers argue about whether to store `terraform.tfvars` (which
   contains database passwords) in the team's git repository. One says "it's
   convenient." The other says "it's a security risk." Settle the argument: explain
   the correct approach to managing secrets in Terraform configurations for GCP
   databases, naming the specific GCP service involved.

---

### Scenario C — The Reliability Engineering Challenge

A streaming media company runs a global Cloud Spanner database for user account
management and a Cloud SQL for PostgreSQL cluster for content metadata. The SRE team
must define SLOs for both databases and build an automated reliability testing program.

Address the following:

1. Define SLOs for both databases. For each, specify the SLI (what you measure),
   the SLO target (numerical), the measurement window, and what constitutes a
   "bad minute" for error budget tracking. Consider that Spanner and Cloud SQL have
   fundamentally different failure modes.

2. The SRE team wants to run monthly automated failover tests for Cloud SQL and wants
   to verify that the application recovers within 3 minutes. Design the test pipeline:
   what steps it runs, what it measures, and how it determines pass/fail. What GCP
   services would orchestrate and execute this pipeline?

3. After 6 months, the error budget for Cloud SQL has been consumed twice (the SLO
   was violated). Analysis shows both violations were caused by the same application
   team deploying a schema migration that held a table lock for 10 minutes. What
   technical controls and processes would you implement to prevent this class of
   incident from consuming future error budget?

---

## Response Posts

After your primary post, reply to **two classmates** who chose different scenarios.
Each reply must be at least 100 words and do one of the following:

- Add a monitoring metric or automation technique the original poster overlooked
- Challenge a design decision with a specific alternative and justification
- Describe a production incident from your experience (or a case study) that
  illustrates the importance of the topic in the scenario

---

## Grading Rubric

| Criteria | Points |
|---|---|
| Primary post meets 250-word minimum | 10 |
| Correct and specific use of GCP monitoring and automation features | 30 |
| All three sub-questions addressed with technical depth | 30 |
| Operational reasoning (tradeoffs, not just feature lists) | 15 |
| Two substantive peer responses | 15 |
| **Total** | **100** |

---

## Technical Vocabulary Checklist

Strong posts naturally use these terms where appropriate:

- Cloud Monitoring / alerting policy / notification channel
- GAUGE / DELTA / CUMULATIVE metric
- Cloud SQL Insights / query latency / wait events
- Log-based metric
- Maintenance window / deny maintenance period
- Automated backup / PITR (point-in-time recovery)
- Terraform / HCL / state file / GCS backend
- `terraform import` / `terraform plan` / `deletion_protection`
- Terraform module / lifecycle block / `prevent_destroy`
- HA failover / forced failover / recovery time
- SLO / SLI / error budget
- Cloud Build / Cloud Scheduler

---

Module 15 Discussion — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
