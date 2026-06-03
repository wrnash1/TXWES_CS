# Lab Activity: Module 16 — Capstone Architecture Design

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Lab Overview

**Title**: Capstone — Multi-Tier GCP Database Architecture Design and Review

**Estimated Time**: 90–120 minutes

**Difficulty**: Advanced

This is the capstone lab for CIS-4327. Unlike previous labs that focused on a
single service or task, this lab challenges you to design, justify, and review a
complete multi-tier database architecture for a realistic enterprise scenario.

You will produce an architecture document and answer a structured set of review
questions that span the full course curriculum. This lab prepares you directly for
the scenario-based questions on the Google Cloud Professional Database Engineer exam.

---

## Prerequisites

- Completion of Modules 1–15
- Access to Google Cloud Console (read-only is fine for this lab — no resources are billed)
- GCP Pricing Calculator: cloud.google.com/products/calculator
- Architecture diagramming tool (Google Slides, draw.io, Lucidchart, or similar)

---

## Scenario: GlobalMart E-Commerce Platform

GlobalMart is a mid-size e-commerce company preparing to migrate their entire
on-premises database infrastructure to Google Cloud Platform. You have been hired
as the lead database architect.

### Current On-Premises Stack

| System | Technology | Size | Usage |
|---|---|---|---|
| Orders Database | Oracle 19c | 2.5 TB | OLTP — 3,000 TPS peak |
| Product Catalog | MySQL 5.7 | 500 GB | OLTP — read-heavy, 95% reads |
| Customer Profiles | PostgreSQL 13 | 800 GB | OLTP — reads and writes |
| Analytics Warehouse | Teradata | 15 TB | OLAP — 50 complex reports daily |
| Session Cache | Redis 6 (self-managed) | 64 GB RAM | In-memory cache — 1ms SLA |
| Search Index | Elasticsearch | 200 GB | Full-text search |

### Business Requirements

1. **Global availability**: Orders database must serve customers in North America,
   Europe, and Asia-Pacific with < 100ms latency and zero-downtime regional failover.
2. **Compliance**: All customer PII (name, email, address, payment info) must use
   CMEK encryption. Data must not leave the US for North American customers
   (data residency).
3. **Analytics SLA**: Finance reports must complete in under 2 minutes (currently 45 minutes).
4. **Minimal downtime**: Migrations must not exceed 4 hours of total downtime across
   all systems combined. Some systems may require zero downtime.
5. **Cost efficiency**: Current infrastructure costs $120,000/month. The CTO expects
   cloud costs to be at or below this after 18 months.
6. **Security**: All database connections must use encryption in transit.
   IAM authentication must replace static passwords where supported.
7. **Automation**: All database infrastructure must be managed via Terraform.
   Staging and production environments must be identical in configuration.

---

## Part 1 — Service Selection

### Task 1.1

For each of the six on-premises systems, select the appropriate GCP database service.
Complete the table below in your submission document:

| System | Selected GCP Service | Primary Justification (2–3 sentences) |
|---|---|---|
| Orders Database | | |
| Product Catalog | | |
| Customer Profiles | | |
| Analytics Warehouse | | |
| Session Cache | | |
| Search Index | | |

**Guidance**: Consider the workload type (OLTP vs. OLAP), scale requirements (global
vs. regional), and compatibility requirements. For Search Index, which GCP service or
pattern replaces Elasticsearch functionality?

---

## Part 2 — Architecture Design

### Task 2.1 — Architecture Diagram

Create an architecture diagram showing:

- All six database services with their GCP equivalents
- Network connections between services (with encryption annotations)
- VPC structure (Private IP, VPC peering if applicable)
- Data flow from the application tier to each database
- Any CDC/streaming connections between databases (e.g., OLTP to analytics)

Your diagram should be clear enough that a new engineer could understand the
overall data architecture without additional explanation.

### Task 2.2 — High Availability Design

For each database service in your architecture, describe:

- The HA mechanism used
- The expected failover time
- The RTO (Recovery Time Objective) and RPO (Recovery Point Objective) you would
  commit to in the SLA

Complete this table:

| Service | HA Mechanism | Failover Time | RTO | RPO |
|---|---|---|---|---|
| Orders (GCP equivalent) | | | | |
| Product Catalog (GCP equivalent) | | | | |
| Customer Profiles (GCP equivalent) | | | | |
| Analytics Warehouse | | | | |
| Session Cache | | | | |

---

## Part 3 — Security Architecture

### Task 3.1 — Encryption Plan

For each database service, complete the encryption plan:

| Service | Encryption at Rest | Encryption in Transit | CMEK Required? |
|---|---|---|---|
| Orders | | | |
| Product Catalog | | | |
| Customer Profiles | | | |
| Analytics Warehouse | | | |
| Session Cache | | | |

### Task 3.2 — Access Control Design

Design the IAM role assignments for these three principals:

- **Application service account** (`globalmart-app@PROJECT.iam.gserviceaccount.com`):
  Used by the e-commerce application to read/write operational databases.
- **Analytics service account** (`globalmart-analytics@PROJECT.iam.gserviceaccount.com`):
  Used by the reporting engine to query the analytics warehouse.
- **DBA team group** (`dba-team@globalmart.com`): Human operators who manage
  schema changes and monitor databases.

For each principal, list the minimum IAM roles needed across all relevant services.

### Task 3.3 — BigQuery Data Protection

Customer email addresses and payment card last-four-digits are stored in BigQuery
tables used by the analytics team. Describe the BigQuery security configuration
(Policy Tags, masking rules, authorized views, or row access policies) you would
implement to ensure:

- Analysts can query customer revenue metrics by region without seeing PII
- Senior data stewards can see all columns including email
- Reports exported to third parties contain no PII

---

## Part 4 — Migration Plan

### Task 4.1 — Migration Sequencing

Order the six systems for migration from first to last, with a one-paragraph
justification for your sequencing. Consider:

- Which systems are safest to migrate first (lowest risk)?
- Which systems have hard dependencies that require other systems to be migrated first?
- Which systems require the most preparation (schema conversion, testing)?

### Task 4.2 — Orders Database Migration Detail

The Orders database is the highest-risk migration (Oracle 19c → your selected GCP
service, 2.5 TB, 3,000 TPS, zero downtime requirement). Provide a detailed migration
plan covering:

1. Pre-migration preparation steps (what must be done before the migration job starts)
2. Migration tool selection and configuration
3. Schema conversion challenges specific to Oracle-to-PostgreSQL migration
4. Validation strategy (which of the three validation levels you will use and why)
5. Cutover plan with estimated downtime window
6. Rollback plan if a critical issue is discovered within 30 minutes of cutover

---

## Part 5 — Cost Estimate

### Task 5.1 — Monthly Cost Estimate

Using the GCP Pricing Calculator (cloud.google.com/products/calculator), produce
a rough monthly cost estimate for your proposed architecture. Document your assumptions.

At minimum, estimate costs for:

- The Orders database service (instance tier + storage + HA)
- The Analytics Warehouse (BigQuery storage + estimated query volume)
- The Session Cache (Memorystore tier)

### Task 5.2 — Cost Optimization Recommendations

Identify three specific cost optimization measures you would implement at launch
and their estimated impact. Reference specific BigQuery, Cloud SQL, or Cloud Spanner
pricing features.

---

## Part 6 — Monitoring and Automation Plan

### Task 6.1 — Monitoring Strategy

List the top five Cloud Monitoring alerts you would configure for this architecture,
specifying for each:

- The metric name
- The threshold and duration
- The justification (what incident does this prevent or detect?)
- The notification channel

### Task 6.2 — Terraform Organization

Describe how you would organize the Terraform project for this architecture:

- Directory/module structure
- State file organization (one state file or multiple? Per service or per environment?)
- How you would manage the difference between staging and production configurations

---

## Deliverables

Submit a single document (PDF or Google Doc) containing:

1. Part 1: Service selection table with justifications
2. Part 2: Architecture diagram + HA design table
3. Part 3: Security tables + BigQuery data protection narrative
4. Part 4: Migration sequence justification + Orders migration detail
5. Part 5: Cost estimate with assumptions + optimization recommendations
6. Part 6: Monitoring alerts + Terraform organization description

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1: Service selection — all six correct and justified | 15 |
| Part 2: Architecture diagram clear and complete; HA table correct | 20 |
| Part 3: Encryption plan correct; IAM least privilege; BigQuery security correct | 20 |
| Part 4: Migration sequence justified; Orders plan detailed and realistic | 20 |
| Part 5: Cost estimate with documented assumptions; optimizations specific | 10 |
| Part 6: Monitoring alerts complete with all fields; Terraform structure sensible | 15 |
| **Total** | **100** |

---

Module 16 Lab — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
