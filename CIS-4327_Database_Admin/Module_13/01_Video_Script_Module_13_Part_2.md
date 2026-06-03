# Video Script: Module 13 — Database Security (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Part 2 Introduction

Welcome back. In Part 1 we covered encryption, IAM authentication, and audit logging.

In Part 2 we focus on network-level isolation with VPC Service Controls, data masking
techniques, and column-level security in BigQuery. These topics represent the application
and network layers of our defense-in-depth model.

---

## SLIDE 2 — VPC Service Controls Overview

VPC Service Controls (VPC-SC) is a GCP security feature that creates a logical security
perimeter around GCP services, preventing data from being exfiltrated even by authorized
users operating from outside the perimeter.

The problem VPC-SC solves: IAM alone controls who can access a service, but it does not
prevent an authorized user from copying data outside your organization. For example, a
GCP project admin with BigQuery access could export your data to a BigQuery dataset in
their personal GCP project. VPC-SC blocks this class of attack.

How VPC-SC works:

1. You create an **Access Policy** at the organization level.
2. Within the policy, you create a **Service Perimeter** that includes one or more
   GCP projects and one or more GCP services (e.g., BigQuery, Cloud Storage, Cloud SQL).
3. API calls that attempt to cross the perimeter boundary are blocked — even if the
   caller has valid IAM permissions.

This is the key mental model: VPC-SC adds a perimeter check on top of IAM. Both must
pass for an operation to succeed.

---

## SLIDE 3 — VPC Service Controls for BigQuery

For BigQuery specifically, VPC-SC prevents:

- Data exfiltration from a protected project to an unprotected project via `bq cp` or
  API calls that reference resources outside the perimeter
- Access from untrusted networks (e.g., a developer's home network) to protected datasets
- Cross-project query references to datasets outside the perimeter

Access levels allow you to define conditions under which perimeter restrictions are
relaxed. For example, you might define an access level that allows connections from
your corporate office IP range or from devices that are corporate-managed (via
BeyondCorp / Identity-Aware Proxy).

Creating a service perimeter with gcloud:

```bash
gcloud access-context-manager perimeters create analytics-perimeter \
  --policy=POLICY_ID \
  --title="Analytics Data Perimeter" \
  --resources=projects/PROJECT_NUMBER \
  --restricted-services=bigquery.googleapis.com,storage.googleapis.com \
  --access-levels=accessPolicies/POLICY_ID/accessLevels/corp-network
```

**Exam note**: VPC Service Controls operate at the API level, not at the network
packet level. They work in conjunction with Private IP (which controls network routing)
but are separate features. An instance with Private IP still needs VPC-SC to prevent
API-level data exfiltration.

---

## SLIDE 4 — Private IP and Authorized Networks for Cloud SQL

Private IP configuration for Cloud SQL places the instance in a VPC network, making
it accessible only from resources within the same VPC (or peered VPCs). No public IP
is required.

Benefits of Private IP:

- Reduces attack surface — the instance is not reachable from the internet.
- Eliminates the need for SSL certificates for network-level security (the VPC network
  itself provides isolation, though SSL should still be used for data-in-transit).
- Required for compliance scenarios where public endpoints are prohibited.

Configuring Private IP on a new Cloud SQL instance:

```bash
gcloud sql instances create my-private-instance \
  --database-version=POSTGRES_15 \
  --region=us-central1 \
  --network=projects/PROJECT_ID/global/networks/default \
  --no-assign-ip
```

The `--no-assign-ip` flag ensures no public IP is assigned.

**Authorized Networks** (for public IP instances): A whitelist of CIDR ranges allowed
to connect to the Cloud SQL instance's public IP. This is a weaker isolation model than
Private IP and should only be used when Private IP is not feasible.

For the exam: prefer Private IP over Authorized Networks for production databases.
Use VPC Service Controls on top of Private IP for the strongest isolation.

---

## SLIDE 5 — Data Masking in BigQuery

Data masking hides or transforms sensitive data for users who should not see the
original values, while allowing those users to still query the data productively.

BigQuery supports **dynamic data masking** through column-level security combined
with masking rules. The masking is applied at query time — the underlying data is
stored unmasked, but users with masking policies applied to them see transformed values.

Masking functions available:

- **SHA256**: Replaces the value with its SHA-256 hash — useful for joining on masked
  values while hiding the original.
- **DEFAULT**: Replaces the value with the column's default value (NULL for most types,
  0 for numeric, empty string for STRING).
- **EMAIL_MASK**: Shows only the domain of an email address (e.g., `***@company.com`).
- **LAST_FOUR_CHARACTERS**: Shows only the last 4 characters (e.g., for credit card
  or SSN fields).
- **DATE_YEAR_MASK**: Shows only the year of a DATE or TIMESTAMP field.

---

## SLIDE 6 — Implementing Column-Level Security in BigQuery

BigQuery column-level security uses **Policy Tags** and the **Data Catalog Taxonomy**
to classify columns, and then masking policies control what users see.

Step 1 — Create a taxonomy and policy tags in Data Catalog:

```bash
gcloud data-catalog taxonomies create \
  --location=us-central1 \
  --display-name="PII Classification"

gcloud data-catalog taxonomies policy-tags create \
  --taxonomy=TAXONOMY_ID \
  --location=us-central1 \
  --display-name="PII-High"
```

Step 2 — Apply a policy tag to a BigQuery column in the table schema:

```json
{
  "name": "ssn",
  "type": "STRING",
  "policyTags": {
    "names": ["projects/PROJECT/locations/us-central1/taxonomies/TAXONOMY_ID/policyTags/TAG_ID"]
  }
}
```

Step 3 — Grant `roles/datacatalog.categoryFineGrainedReader` to users who should
see unmasked data. Users without this role will see masked values.

Step 4 — Create a data masking rule and assign it to a masking policy in BigQuery:

Users without the fine-grained reader role will automatically see the masking
function output (e.g., `DEFAULT`, `SHA256`) instead of the real value.

**Exam insight**: Column-level security and masking are separate from table-level IAM.
A user can have `roles/bigquery.dataViewer` on a table (can query it) but still see
masked values on policy-tagged columns if they lack the fine-grained reader role.

---

## SLIDE 7 — Authorized Views as a Security Pattern

We covered authorized views technically in Module 12. From a security perspective,
authorized views are one of the most practical mechanisms for controlling access to
sensitive BigQuery data.

Security pattern:

1. The raw `customers` table in dataset `raw_data` contains full PII (name, SSN,
   address, phone).
2. You create a view in dataset `analytics_views` that selects only non-PII columns
   from `customers`.
3. You grant analysts access to `analytics_views` only.
4. You add `analytics_views` as an authorized view in `raw_data`'s settings.

Now analysts can query the view to get the data they need without ever having access
to the raw PII. Even if an analyst attempts to query `raw_data.customers` directly,
their IAM permissions prevent it.

This pattern is preferred over column-level masking when you want complete column
exclusion rather than value transformation.

---

## SLIDE 8 — IAM Roles for Database Security

Understanding which IAM roles are needed for which database operations is essential
for the exam. Here are the key roles for Cloud SQL and BigQuery:

**Cloud SQL IAM roles**:

| Role | Access Level |
|---|---|
| `roles/cloudsql.admin` | Full control including instance creation and deletion |
| `roles/cloudsql.editor` | Start/stop instances, manage databases and users |
| `roles/cloudsql.viewer` | View instance metadata, no data access |
| `roles/cloudsql.client` | Connect to instances via Cloud SQL Auth Proxy |
| `roles/cloudsql.instanceUser` | IAM database authentication login |

**BigQuery IAM roles**:

| Role | Access Level |
|---|---|
| `roles/bigquery.admin` | Full control of all BigQuery resources |
| `roles/bigquery.dataOwner` | Read/write/delete tables and datasets they own |
| `roles/bigquery.dataEditor` | Read/write data in datasets they are granted on |
| `roles/bigquery.dataViewer` | Read-only data access |
| `roles/bigquery.jobUser` | Run query jobs (required alongside data access roles) |
| `roles/bigquery.user` | Run jobs and list datasets; includes jobUser |

A common exam trap: `roles/bigquery.dataViewer` alone is not sufficient to query data.
The user also needs `roles/bigquery.jobUser` to create and run query jobs.

---

## SLIDE 9 — Secrets Management for Database Credentials

When applications connect to Cloud SQL using traditional password authentication
(not IAM authentication), passwords must be stored and accessed securely. Hardcoding
credentials in application code or environment variables is a critical security failure.

**Secret Manager** is the GCP service for storing and accessing secrets at runtime.

Storing a database password:

```bash
echo -n "my-db-password" | gcloud secrets create sql-db-password \
  --replication-policy=automatic \
  --data-file=-
```

Granting a service account access to read the secret:

```bash
gcloud secrets add-iam-policy-binding sql-db-password \
  --member="serviceAccount:myapp@PROJECT.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

Accessing the secret in application code (Python example):

```python
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
name = "projects/PROJECT_ID/secrets/sql-db-password/versions/latest"
response = client.access_secret_version(request={"name": name})
password = response.payload.data.decode("UTF-8")
```

For the exam: always recommend Secret Manager over environment variables or config
files for database credential storage. Combined with IAM authentication where possible.

---

## SLIDE 10 — Security Checklist and Best Practices

For the exam and real deployments, here is a security checklist for GCP databases:

**Network isolation**:

- Use Private IP for Cloud SQL production instances
- Enable VPC Service Controls for sensitive BigQuery datasets
- Use the Cloud SQL Auth Proxy for all application connections

**Authentication and authorization**:

- Enable IAM database authentication for Cloud SQL where supported
- Apply least-privilege IAM roles; avoid `roles/cloudsql.admin` for application accounts
- Store all credentials in Secret Manager

**Encryption**:

- Use CMEK for regulated data requiring customer-controlled key management
- Enable `ENCRYPTED_ONLY` or `TRUSTED_CLIENT_CERTIFICATE_REQUIRED` SSL mode for Cloud SQL
- Verify BigQuery CMEK configuration when using customer-controlled keys for warehoused data

**Data protection**:

- Apply Policy Tags and masking rules to PII columns in BigQuery
- Use authorized views to limit column access for analytical users
- Export and review Data Access audit logs regularly

**Monitoring**:

- Enable Data Access audit logs for all production databases
- Enable `pgaudit` for Cloud SQL PostgreSQL for query-level logging
- Set up Cloud Monitoring alerts for failed authentication attempts

---

## SLIDE 11 — Module 13 Summary

Let's wrap up Module 13:

**Encryption**: GMEK is the default. CMEK gives you key control and revocation power.
Encryption in transit is enforced by default for BigQuery; configurable via SSL modes
for Cloud SQL.

**IAM authentication**: Replaces database passwords with short-lived IAM tokens.
Simplifies access management and improves audit quality.

**Audit logging**: Admin Activity logs are always on. Enable Data Access logs for
compliance. Use pgaudit for SQL-level logging in PostgreSQL.

**VPC Service Controls**: Creates a perimeter around projects/services to prevent
API-level data exfiltration, even by authorized users.

**Column-level security**: Policy Tags in Data Catalog combined with BigQuery masking
rules to transform sensitive column values at query time.

**Authorized views**: The simplest pattern for restricting column access entirely.

**Secret Manager**: The correct way to store and rotate database credentials used by
applications.

Complete the lab, quiz, and discussion to reinforce these concepts. In Module 14 we
move into database migration strategies.

---

*End of Part 2 Script*
