# Discussion Forum: Module 13 — Database Security

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

Database security involves more than configuring individual features — it requires
reasoning about threat models, regulatory requirements, and the practical tradeoffs
between security and usability. This discussion invites you to apply Module 13 concepts
to realistic security scenarios.

**Due date**: See course schedule in Canvas.

**Grading**: See rubric at the bottom of this prompt.

---

## Primary Post Prompt

Choose **one** of the following scenarios and write a substantive primary post
(minimum 250 words) addressing all questions in the scenario.

---

### Scenario A — The Healthcare Database Breach

A regional hospital network stores patient records in Cloud SQL for PostgreSQL.
After a routine security review, the security team discovers that:

- The Cloud SQL instance has a public IP with authorized networks set to `0.0.0.0/0`
  (open to the world)
- SSL mode is set to `ALLOW_UNENCRYPTED_AND_ENCRYPTED`
- Database users have static passwords stored in application environment variables
- No audit logging is enabled
- The service account used by the application has `roles/cloudsql.admin`

Address the following:

1. Identify each security vulnerability and explain the specific threat it creates.
   Use the defense-in-depth model from the module to categorize each vulnerability
   by layer (network, identity, data, audit).

2. Propose a remediation plan that addresses all five vulnerabilities. For each fix,
   explain what it does and acknowledge any operational impact the fix might cause
   (e.g., requiring application code changes, downtime, user re-training).

3. The hospital's CISO asks: "If we implement all these fixes, are we HIPAA compliant
   for database security?" How would you answer? What does HIPAA require of database
   configurations, and what does GCP provide versus what the hospital must configure?

---

### Scenario B — The Analytics Platform Access Control Design

A university research institute is building a BigQuery analytics platform for
three groups of users:

- **Research analysts**: Can query all non-PII columns across all research datasets
- **Data stewards**: Can query all columns including PII for data quality work
- **External collaborators**: University partners who need aggregate statistics only —
  no row-level data and no PII

The data includes student records subject to FERPA (Family Educational Rights and
Privacy Act), which prohibits disclosing personally identifiable information without
consent.

Address the following:

1. Design a BigQuery security architecture that satisfies all three user groups'
   access requirements while maintaining FERPA compliance. Specify which BigQuery
   security features you would use for each group and why.

2. An external collaborator discovers they can query a view that returns per-student
   revenue data aggregated by student cohort. Each cohort has only 2–3 students,
   making it easy to identify individuals. How does this violate FERPA's intent even
   without exposing explicit PII columns? What technical control addresses this
   class of problem?

3. The institute receives a FERPA audit request for logs showing who accessed student
   data and when over the past 12 months. Walk through exactly which GCP services
   and log types you would use to produce this report, and what fields you would
   include in the audit evidence.

---

### Scenario C — The Multi-Cloud Security Architecture

A global e-commerce company runs transaction data in Cloud SQL for PostgreSQL in
GCP and also synchronizes a subset of data to an on-premises Oracle database for
reporting. The security team has the following concerns:

- Data in transit between GCP Cloud SQL and on-premises Oracle travels over a VPN
- Encryption keys for Cloud SQL must be managed on-premises (hardware security
  module — HSM) for regulatory compliance
- All database access from application servers must be logged with user identity
- The on-premises DBA team should be able to manage the Cloud SQL schema but not
  read production data

Address the following:

1. GCP's standard CMEK uses Cloud KMS. The company requires keys to stay in their
   on-premises HSM. Does GCP support this? Describe Cloud External Key Manager (EKM)
   and how it integrates with Cloud KMS and Cloud SQL CMEK.

2. Design the IAM role assignments for the on-premises DBA team that allows schema
   management (DDL operations) but prevents reading production data. Is this fully
   achievable with GCP IAM alone, or does it require database-engine-level controls
   as well?

3. The VPN connection between GCP and on-premises experiences intermittent outages.
   During an outage, the Cloud SQL Auth Proxy cannot reach the Cloud SQL API to
   validate IAM tokens. What happens to existing connections and new connection
   attempts? How would you design the connection architecture to tolerate VPN outages?

---

## Response Posts

After submitting your primary post, reply to **two classmates** who chose different
scenarios. Each reply must be at least 100 words and do one of the following:

- Identify a security control the original poster overlooked
- Challenge a recommendation with a specific alternative approach
- Connect the scenario to a regulatory framework not mentioned (e.g., GDPR, PCI DSS,
  SOC 2, NIST 800-53)

---

## Grading Rubric

| Criteria | Points |
|---|---|
| Primary post meets 250-word minimum | 10 |
| Correct and specific use of GCP security features | 30 |
| All three sub-questions addressed | 30 |
| Regulatory/compliance reasoning demonstrated | 15 |
| Two substantive peer responses (100+ words each) | 15 |
| **Total** | **100** |

---

## Technical Vocabulary Checklist

Strong posts will naturally incorporate these terms where appropriate:

- CMEK / GMEK / Cloud KMS
- Envelope encryption
- SSL mode (ENCRYPTED_ONLY, TRUSTED_CLIENT_CERTIFICATE_REQUIRED)
- Cloud SQL Auth Proxy
- IAM database authentication
- Admin Activity logs / Data Access logs
- pgaudit
- VPC Service Controls
- Policy Tags / column-level security
- Authorized view / row access policy
- Secret Manager
- Least-privilege IAM
- Private IP

---

Module 13 Discussion — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.
