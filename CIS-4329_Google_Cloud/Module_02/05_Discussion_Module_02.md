# Discussion: Module 02 — IAM and Access Control in GCP

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion asks you to reason through real-world IAM security scenarios.
Strong IAM design prevents data breaches and compliance violations. Weak IAM
design is one of the top causes of cloud security incidents. The scenarios below
reflect the kinds of situations cloud engineers encounter in the field.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — IAM Incident Analysis (Choose One)

A financial services company suffered a data breach. Investigation revealed the
following configuration in their GCP environment:

- All developers had `roles/editor` granted at the Organization level
- The production Cloud SQL database was in the same project as the development
  environment
- A service account used by the CI/CD pipeline had `roles/owner` on all projects
- The CI/CD service account had a JSON key file stored in the GitHub repository
- Data Access audit logs were not enabled on Cloud Storage or Cloud SQL

In your post:

1. Identify at least four specific security misconfigurations in this scenario.
2. For each misconfiguration, describe the specific risk it creates.
3. Propose a corrected IAM design. Include specific role names and hierarchy
   structure in your answer.
4. Explain how IAM Conditions and Workload Identity Federation could have
   prevented two of the risks.

---

## Prompt B — Principle of Least Privilege Design (Choose One)

You are the cloud architect for a hospital that is migrating to GCP. The
hospital has the following team members and workloads:

- Clinical data analysts who need to run queries against patient data in BigQuery
- Application developers who build and deploy microservices on Cloud Run
- A nightly ETL pipeline that moves data from Cloud Storage to BigQuery
- A database administrator who manages Cloud SQL instances
- An IT auditor who reviews access logs but never modifies resources

Design an IAM configuration for this organization. In your post:

1. For each person or workload type, specify the exact role(s) you would assign
   and at what level in the hierarchy (organization, folder, or project).
2. Explain why you chose each role over alternatives (e.g., why not just give
   the analyst `roles/bigquery.admin`).
3. Describe how you would structure the resource hierarchy (projects/folders)
   to support isolation between production and non-production environments.
4. Explain what HIPAA compliance considerations affect your IAM design and how
   GCP features address them.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- Specific GCP role names (e.g., `roles/bigquery.dataViewer`, not just "viewer")
- Reasoning for each design decision, not just conclusions
- At least one ACE exam concept from Module 02 applied in a practical context

Your two peer responses must be at least 100 words each and do one of the
following:

- Challenge a role assignment decision and suggest an alternative with reasoning
- Identify a gap or edge case the original post did not address
- Share a real-world parallel that adds context to the design

---

## Discussion Tips

- The IAM roles reference at cloud.google.com/iam/docs/understanding-roles
  lists every predefined role and its included permissions. Use it.
- Think through attack scenarios: if a service account is compromised, what
  is the blast radius with the permissions you assigned?
- For HIPAA and regulatory compliance considerations, GCP's compliance page at
  cloud.google.com/security/compliance/hipaa is a useful reference.

---

## Reflection Question (Optional — Extra Credit)

After reading your classmates' designs, did you identify any trade-offs between
security and operational convenience? Describe one specific tension you observed
and explain how you would resolve it. Minimum 150 words for extra credit.

---

End of Discussion — Module 02

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash
