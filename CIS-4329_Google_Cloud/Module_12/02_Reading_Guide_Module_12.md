# Reading Guide: Module 12 – Cloud Security: Security Command Center and Cloud KMS
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 12 – Cloud Security: Security Command Center and Cloud KMS**! Securing cloud resources requires both visibility into threats and control over encryption keys. This module covers Security Command Center (SCC) for centralized security posture management, Cloud Key Management Service (Cloud KMS) for customer-managed encryption keys, and related security controls including Cloud Armor, VPC Service Controls, and Binary Authorization. The ACE exam tests your ability to select and configure the right security tool for a given threat or compliance requirement.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Security Command Center (SCC)**: GCP's centralized security and risk management platform. SCC aggregates findings from built-in detectors (Security Health Analytics, Web Security Scanner, Container Threat Detection) and third-party security tools. It provides a unified view of misconfigurations, vulnerabilities, and active threats across your GCP organization. SCC Standard tier is free; Premium tier adds Event Threat Detection and Security Health Analytics continuous monitoring.

*   **Cloud KMS (Key Management Service)**: A hosted key management service that lets you create, rotate, import, and destroy cryptographic keys. With Cloud KMS, you manage the keys used to encrypt your data — this is called Customer-Managed Encryption Keys (CMEK). Cloud KMS keys can be software-protected (default) or hardware-protected via Cloud HSM (FIPS 140-2 Level 3 validated hardware security modules).

*   **Customer-Managed Encryption Keys (CMEK)**: An encryption model where GCP services (Cloud Storage, BigQuery, Compute Engine disks, etc.) encrypt data using a key you manage in Cloud KMS rather than a Google-managed key. CMEK lets you control key rotation schedules, restrict which principals can use the key, and destroy the key to render data irrecoverable.

*   **Cloud Armor**: A managed DDoS protection and web application firewall (WAF) service that integrates with the Global HTTP(S) Load Balancer. Cloud Armor policies can allow or deny traffic based on IP address, geographic region, or custom request attributes (headers, query parameters). Use Cloud Armor to block known malicious IP ranges or restrict access to specific countries.

*   **VPC Service Controls**: A GCP security feature that creates a service perimeter around GCP API services (like Cloud Storage, BigQuery, and Cloud KMS), preventing data exfiltration by restricting API calls to those originating from inside the perimeter. VPC Service Controls work at the GCP API level — they protect against insider threats and compromised credentials attempting to copy data to external projects.

*   **Binary Authorization**: A deploy-time security control for GKE and Cloud Run that requires container images to be signed by trusted authorities before they can be deployed. Binary Authorization enforces a policy that only images attested by your CI/CD pipeline (e.g., after passing security scans) can run in your cluster.

---

### 2. Certification Exam Tips

*   **SCC findings vs. Cloud Monitoring alerts — different purposes**: SCC surfaces security findings (misconfigurations, vulnerabilities, active threats). Cloud Monitoring surfaces operational metrics (CPU, latency, error rates). The ACE exam distinguishes these: if a question asks how to detect a publicly exposed Cloud Storage bucket or an overly permissive firewall rule, the answer is SCC Security Health Analytics, not Cloud Monitoring.

*   **CMEK vs. Google-managed keys — when CMEK is required**: Google encrypts all data at rest by default using Google-managed keys. CMEK is required only when compliance mandates customer control over keys (e.g., ability to revoke access by deleting the key). The exam tests whether you know this distinction — CMEK adds operational overhead and is not the default recommendation unless compliance requires it.

*   **Cloud Armor attaches to Global HTTP(S) Load Balancer only**: Cloud Armor cannot be attached to Internal Load Balancers or Network Load Balancers. It also cannot protect Cloud Run services that are not behind a Global HTTP(S) LB. The exam tests this integration constraint.

*   **VPC Service Controls protect against data exfiltration, not unauthorized access**: VPC Service Controls restrict where GCP API calls can come from — they do not replace IAM. A user with `roles/storage.objectViewer` can still be blocked by a service perimeter from accessing a bucket in a different project. The exam tests the layered model: IAM controls who, VPC Service Controls control from where.

*   **Study Resource**: The freeCodeCamp ACE course covers Security Command Center, Cloud KMS, and Cloud Armor with scenario-based walkthroughs: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Security chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Security Command Center overview including finding types, asset inventory, and the difference between Standard and Premium tiers: [Security Command Center Overview](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview). Security Health Analytics finding types are directly exam-relevant.
*   **Required Reading**: Review Cloud KMS concepts including key rings, key versions, CMEK integration, and the difference between software and hardware (HSM) keys: [Cloud KMS Overview](https://cloud.google.com/kms/docs/key-management-overview).
*   **Required Video**: Watch the Security segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Cloud Security chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a Cloud KMS key ring and key, enable CMEK on a Cloud Storage bucket, and review Security Command Center findings. Key commands to practice:

*   `gcloud kms keyrings create my-keyring --location=us-central1` — creates a Cloud KMS key ring
*   `gcloud kms keys create my-key --location=us-central1 --keyring=my-keyring --purpose=encryption` — creates a symmetric encryption key
*   `gcloud storage buckets create gs://my-cmek-bucket --default-kms-key=projects/PROJECT/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key` — creates a bucket with CMEK
*   `gcloud scc findings list --organization=ORG_ID --filter='state="ACTIVE"'` — lists active SCC findings for an organization

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Security Command Center Overview](https://cloud.google.com/security-command-center/docs/concepts-security-command-center-overview) documentation page.
- [ ] Read the [Cloud KMS Overview](https://cloud.google.com/kms/docs/key-management-overview) documentation page.
- [ ] Watch the Cloud Security segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a Cloud KMS key and enable CMEK on a Cloud Storage bucket.
- [ ] Proceed to the weekly quiz.
