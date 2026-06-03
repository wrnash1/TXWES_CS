# Video Script: Module 14 — GCP Security and Compliance (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 14. Security is woven throughout every GCP service, but this module
focuses on the dedicated security and compliance tools: VPC Service Controls, Cloud DLP,
Cloud KMS, Binary Authorization, and Security Command Center. We also cover how GCP maps
to compliance frameworks like HIPAA, FedRAMP, and PCI-DSS. Part 1 covers VPC Service
Controls, Cloud DLP, and Cloud KMS. Part 2 covers Binary Authorization, Security Command
Center, and compliance.

---

### Section 1: The GCP Security Model

GCP security operates in layers:

- **Network perimeter** — VPC firewalls, Private Google Access, VPC Service Controls
- **Identity and access** — IAM, service accounts, Workload Identity Federation
- **Data protection** — encryption at rest and in transit, CMEK, Cloud KMS, Cloud DLP
- **Application security** — Binary Authorization, Artifact Analysis, Cloud Armor
- **Visibility** — Security Command Center, Cloud Audit Logs, Cloud Monitoring

The ACE exam tests your ability to select the right tool for each layer. A common trap
is confusing IAM (who can call an API) with VPC Service Controls (which network context
can call an API). Both are access controls but they operate at different boundaries.

---

### Section 2: VPC Service Controls

VPC Service Controls creates a security perimeter around GCP services to prevent data
exfiltration.

**Problem VPC SC solves**: Without it, a user with Storage Admin role could copy data
from a sensitive bucket to any network including their personal laptop. VPC SC adds a
network context check: the request must originate from an authorized access level or
VPC network.

#### Key Concepts

- **Service perimeter** — a logical boundary around one or more GCP projects and services
- **Access level** — a condition that requests must satisfy (IP range, device policy,
  identity)
- **Access policy** — a container for perimeters and access levels; scoped to an
  organization
- **Restricted services** — GCP APIs protected by the perimeter (Cloud Storage, BigQuery,
  Cloud SQL, etc.)
- **VPC accessible services** — services that GCE VMs inside the perimeter can reach

#### Creating a Service Perimeter

```bash
# Create an access policy at the org level (done once per organization)
gcloud access-context-manager policies create \
  --organization=ORGANIZATION_ID \
  --title="My Access Policy"

# List policies
gcloud access-context-manager policies list \
  --organization=ORGANIZATION_ID

# Create an access level allowing requests from a corporate IP range
gcloud access-context-manager levels create corporate-network \
  --policy=POLICY_NAME \
  --title="Corporate Network" \
  --basic-level-spec=level-spec.yaml
```

```bash
# Create a dry-run (simulation) service perimeter
gcloud access-context-manager perimeters dry-run create my-perimeter \
  --policy=POLICY_NAME \
  --title="Data Perimeter" \
  --resources=projects/PROJECT_NUMBER \
  --restricted-services=storage.googleapis.com,bigquery.googleapis.com \
  --access-levels=accessPolicies/POLICY_NAME/accessLevels/corporate-network

# Enforce the perimeter (convert dry-run to enforced)
gcloud access-context-manager perimeters dry-run enforce my-perimeter \
  --policy=POLICY_NAME
```

Key ACE points for VPC Service Controls:

- VPC SC operates at the **organization** level, not project level
- Always test with dry-run mode before enforcing to avoid locking out users
- VPC SC does not replace IAM — both checks must pass for a request to succeed
- Perimeter violation logs appear in Cloud Audit Logs under `POLICY_DENIED` entries

---

### Section 3: Cloud Data Loss Prevention (DLP)

Cloud DLP identifies and protects sensitive data in text, images, and structured data.

#### What Cloud DLP Does

- **Inspect** — scan content for sensitive data types (PII, PHI, financial data, secrets)
- **De-identify** — transform sensitive data (redact, mask, tokenize, encrypt)
- **Re-identify** — reverse tokenization or encryption using authorized keys
- **Risk analysis** — compute statistical risk metrics on structured BigQuery data

#### Built-in Info Types

Cloud DLP has over 100 built-in info types including:

- `PERSON_NAME`, `EMAIL_ADDRESS`, `PHONE_NUMBER`
- `US_SOCIAL_SECURITY_NUMBER`, `CREDIT_CARD_NUMBER`
- `IP_ADDRESS`, `DATE_OF_BIRTH`, `PASSPORT`
- Custom regex patterns and dictionaries are also supported

#### Inspecting Content

```bash
# Inspect a string for sensitive data
gcloud dlp text inspect \
  --content="My SSN is 555-12-3456 and email is user@example.com" \
  --info-types=US_SOCIAL_SECURITY_NUMBER,EMAIL_ADDRESS

# Create a DLP job to scan a Cloud Storage bucket
gcloud dlp jobs create \
  --project=PROJECT_ID \
  --location=us-central1 \
  --storage-config=storage-config.json \
  --inspect-config=inspect-config.json
```

#### De-identifying Data

```bash
# De-identify text by masking SSNs
gcloud dlp text de-identify \
  --content="SSN: 555-12-3456" \
  --info-types=US_SOCIAL_SECURITY_NUMBER \
  --masking-character="*" \
  --number-to-mask=9
```

De-identification transformations include:

- **Redaction** — replace with a fixed string or character mask
- **Pseudonymization** — replace with a reversible token using a cryptographic key
- **Bucketing** — replace numeric values with ranges (age 34 becomes "30-39")
- **Date shifting** — shift dates by a random number of days for each record

#### ACE Exam Focus: Cloud DLP

- Cloud DLP is the correct answer for "detect and protect PII in Cloud Storage or
  BigQuery"
- De-identification (not just detection) is the pattern for HIPAA and GDPR compliance
- DLP jobs can scan Cloud Storage, BigQuery, and Datastore
- Findings are published to Cloud Logging or BigQuery for analysis

---

### Section 4: Cloud Key Management Service (KMS)

Cloud KMS is a managed cryptographic key service. It stores encryption keys, performs
cryptographic operations, and integrates with GCP services for Customer-Managed
Encryption Keys (CMEK).

#### KMS Key Hierarchy

```text
Key Ring
  └── Cryptographic Key
        └── Key Version (ENABLED / DISABLED / DESTROYED)
```

- **Key ring** — a container for keys in a specific location; cannot be deleted
- **Key** — a named resource within a key ring; has a purpose (ENCRYPT_DECRYPT,
  ASYMMETRIC_SIGN, etc.)
- **Key version** — the actual cryptographic material; versions can be enabled, disabled,
  or destroyed

#### Creating KMS Keys

```bash
# Create a key ring in us-central1
gcloud kms keyrings create my-keyring \
  --location=us-central1

# Create a symmetric encryption key
gcloud kms keys create my-cmek-key \
  --location=us-central1 \
  --keyring=my-keyring \
  --purpose=encryption

# List keys
gcloud kms keys list \
  --location=us-central1 \
  --keyring=my-keyring

# Describe a key (shows rotation period and primary version state)
gcloud kms keys describe my-cmek-key \
  --location=us-central1 \
  --keyring=my-keyring
```

#### Encrypting and Decrypting Data

```bash
# Encrypt a file using KMS
gcloud kms encrypt \
  --location=us-central1 \
  --keyring=my-keyring \
  --key=my-cmek-key \
  --plaintext-file=secret.txt \
  --ciphertext-file=secret.enc

# Decrypt the file
gcloud kms decrypt \
  --location=us-central1 \
  --keyring=my-keyring \
  --key=my-cmek-key \
  --ciphertext-file=secret.enc \
  --plaintext-file=secret-decrypted.txt
```

#### Using CMEK with GCP Services

```bash
# Create a Cloud Storage bucket with CMEK
gsutil mb \
  -l us-central1 \
  -k projects/PROJECT_ID/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-cmek-key \
  gs://my-cmek-bucket

# Create a BigQuery dataset with CMEK
bq mk \
  --location=US \
  --default_kms_key=projects/PROJECT_ID/locations/us/keyRings/my-keyring/cryptoKeys/my-cmek-key \
  my_dataset
```

#### Key Rotation

```bash
# Set automatic rotation period (90 days = 7776000 seconds)
gcloud kms keys update my-cmek-key \
  --location=us-central1 \
  --keyring=my-keyring \
  --rotation-period=7776000s

# Manually create a new key version
gcloud kms keys versions create \
  --location=us-central1 \
  --keyring=my-keyring \
  --key=my-cmek-key

# Disable an old key version
gcloud kms keys versions disable VERSION_NUMBER \
  --location=us-central1 \
  --keyring=my-keyring \
  --key=my-cmek-key
```

#### ACE Exam Focus: Cloud KMS

- Google-managed encryption is the default for all GCP services (no action required)
- CMEK means you supply the key stored in Cloud KMS; revoke access by disabling the key
  version
- CSEK (Customer-Supplied Encryption Keys) means you supply the raw key material; GCP
  never stores it; used with Cloud Storage and Compute Engine disk operations
- Key rotation does not re-encrypt existing data; new writes use the new version, old
  versions remain to decrypt old data until disabled
- Cloud KMS is regional; choose the same region as your data to avoid cross-region latency

---

### Module 14 Part 1 Summary

In Part 1 we covered:

- **VPC Service Controls** — service perimeters that restrict API calls to authorized
  network contexts; always test with dry-run before enforcement
- **Cloud DLP** — inspect, de-identify, and risk-analyze sensitive data across Cloud
  Storage, BigQuery, and Datastore
- **Cloud KMS** — managed key rings, keys, and versions; CMEK integration with Storage
  and BigQuery; key rotation and version management

In Part 2 we cover Binary Authorization, Security Command Center, and GCP compliance
frameworks.
