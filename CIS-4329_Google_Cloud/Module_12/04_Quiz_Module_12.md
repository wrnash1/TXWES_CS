# Quiz: Module 12 – Cloud Security: Security Command Center and Cloud KMS
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your security team runs a weekly manual audit of GCP project configurations to find publicly accessible Cloud Storage buckets, overly permissive firewall rules, and service accounts with the Owner role. This process takes several hours each week. Which GCP service continuously monitors for these misconfigurations and surfaces them as findings without manual effort?

A) Cloud Monitoring with custom alerting policies on IAM and firewall metrics
B) Security Command Center Security Health Analytics
C) Cloud Logging with log-based metrics on resource configuration changes
D) Cloud Audit Logs exported to BigQuery with scheduled queries for policy violations

*   **Correct Answer:** B) Security Command Center Security Health Analytics
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Monitoring alerting policies evaluate time-series metrics (CPU, latency, request rates). IAM policy bindings and firewall rule configurations are not exposed as numeric metrics — they are resource configurations that Security Health Analytics is specifically designed to evaluate against security best practices.
    *   *Why C is incorrect:* Cloud Logging captures change events (e.g., a bucket was made public), but log-based metrics only count occurrences and require you to write specific filters for each misconfiguration type. Security Command Center provides a built-in library of detectors that continuously scan resource configurations without custom filter development.
    *   *Why D is incorrect:* Exporting audit logs to BigQuery and writing scheduled queries is a valid custom solution, but it requires significant development effort, ongoing query maintenance, and only catches changes at the query schedule interval. SCC Security Health Analytics scans continuously and provides findings in a purpose-built security console.

---

**Question 2**
Your organization's compliance framework requires that encryption keys for a regulated Cloud Storage bucket be managed by your team — including the ability to rotate keys on a custom schedule and revoke data access by destroying the key. Which encryption model should you implement?

A) Google-managed encryption keys (the default) — Google handles all key management automatically.
B) Customer-Managed Encryption Keys (CMEK) using a Cloud KMS key assigned to the bucket.
C) Client-side encryption — encrypt all objects before uploading them to Cloud Storage using your own encryption library.
D) Enable Cloud Storage uniform bucket-level access, which provides enhanced encryption for regulated data.

*   **Correct Answer:** B) Customer-Managed Encryption Keys (CMEK) using a Cloud KMS key assigned to the bucket.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Google-managed encryption keys are controlled entirely by Google — your team has no ability to rotate them on a custom schedule or destroy them to revoke access. Google-managed keys are appropriate for most workloads but do not satisfy compliance requirements that mandate customer control over key lifecycle.
    *   *Why C is incorrect:* Client-side encryption is technically viable but places the entire key management burden on your team, requires encrypting every object before upload, and means the data is opaque to GCP services (no server-side processing). CMEK provides customer control while keeping the data usable by GCP services.
    *   *Why D is incorrect:* Uniform bucket-level access is an IAM configuration that simplifies access control by disabling object-level ACLs — it has no effect on the encryption model used. Enabling it does not change how objects are encrypted or who controls the encryption keys.

---

**Question 3**
Your application receives HTTP traffic from the public internet via a Global HTTP(S) Load Balancer. You need to block traffic from a known malicious IP range (`198.51.100.0/24`) and reject requests that contain SQL injection patterns in the query string. Which GCP service implements both of these controls?

A) VPC firewall rules with a deny rule for the malicious IP range and a Cloud Function that inspects query strings
B) Cloud Armor security policy attached to the load balancer's backend service, with an IP-based deny rule and a preconfigured WAF rule for SQL injection
C) Security Command Center Event Threat Detection, which automatically blocks detected threats at the load balancer
D) Identity-Aware Proxy (IAP) configured to restrict access to authenticated users only, which prevents unauthenticated malicious requests

*   **Correct Answer:** B) Cloud Armor security policy attached to the load balancer's backend service, with an IP-based deny rule and a preconfigured WAF rule for SQL injection
*   **Distractor Analysis:**
    *   *Why A is incorrect:* VPC firewall rules operate at Layer 4 and can block IP ranges, but they cannot inspect HTTP request contents such as query string parameters for SQL injection patterns. A Cloud Function adds significant latency and complexity compared to Cloud Armor's native WAF rule evaluation at the load balancer edge.
    *   *Why C is incorrect:* Security Command Center Event Threat Detection identifies threats and surfaces them as findings — it is a detection and alerting tool, not an inline traffic blocking mechanism. SCC does not automatically modify firewall rules or block load balancer traffic in response to findings.
    *   *Why D is incorrect:* Identity-Aware Proxy restricts access to authenticated and authorized users — it provides application-level authentication, not request content inspection. IAP does not evaluate IP reputation or detect SQL injection patterns in query strings.

---

**Question 4**
A developer accidentally committed a GCP Service Account key JSON file to a public GitHub repository. The key has `roles/editor` on a production project. You need to revoke the compromised key's access immediately. What is the fastest and most direct remediation step?

A) Rotate the Service Account key by creating a new key, then delete the compromised key from the Service Account in the IAM console.
B) Remove the `roles/editor` binding from the Service Account in the project's IAM policy, then delete the compromised key.
C) Disable or delete the compromised key immediately using `gcloud iam service-accounts keys delete`, then audit Cloud Audit Logs for any unauthorized API calls made with the key.
D) Revoke the Service Account's OAuth token by navigating to `myaccount.google.com/permissions` and removing the application's access.

*   **Correct Answer:** C) Disable or delete the compromised key immediately using `gcloud iam service-accounts keys delete`, then audit Cloud Audit Logs for any unauthorized API calls made with the key.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Creating a new key first does not revoke the compromised key — the attacker can still use the old key until it is explicitly deleted. The compromised key must be deleted or disabled immediately, not after creating a replacement.
    *   *Why B is incorrect:* Removing the IAM role binding from the Service Account would revoke access, but it also breaks all legitimate workloads that use the same Service Account for the same role. Deleting only the specific compromised key is more targeted and does not disrupt legitimate operations.
    *   *Why D is incorrect:* `myaccount.google.com/permissions` manages OAuth 2.0 user consent grants for applications — it is not relevant to Service Account keys. Service Account keys use long-lived JSON credentials that authenticate directly via the GCP API, not via OAuth user consent flows.

---

**Question 5**
You are designing a multi-project GCP environment where the analytics team's project needs read access to data in the finance team's Cloud Storage bucket. Your security team is concerned that a compromised analytics project credential could be used to exfiltrate the finance data to an external storage location outside your organization. Which security control specifically prevents this data exfiltration risk at the API level?

A) Grant the analytics Service Account `roles/storage.objectViewer` on the finance bucket using IAM conditional bindings restricted to the analytics project's VPC.
B) Configure VPC Service Controls to create a service perimeter that includes both the analytics and finance projects, preventing API calls that move data outside the perimeter.
C) Enable Cloud Armor on the finance project's load balancer to block requests from the analytics project's IP range.
D) Use Cloud KMS CMEK on the finance bucket so that the analytics project's Service Account cannot decrypt the objects without an explicit KMS key grant.

*   **Correct Answer:** B) Configure VPC Service Controls to create a service perimeter that includes both the analytics and finance projects, preventing API calls that move data outside the perimeter.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IAM controls whether a principal can access a resource — it does not restrict where the data can be copied after access is granted. A compromised analytics credential with `objectViewer` can still read the bucket and write the data to an external project's bucket or public location. VPC Service Controls prevent the copy operation itself.
    *   *Why C is incorrect:* Cloud Armor protects HTTP(S) Load Balancer endpoints from external traffic — it does not protect Cloud Storage API calls made directly via `gsutil` or the Storage API. Cloud Storage does not use the HTTP(S) Load Balancer, so Cloud Armor has no visibility into these requests.
    *   *Why D is incorrect:* CMEK controls who can decrypt data using the KMS key. If the analytics Service Account is granted `roles/cloudkms.cryptoKeyDecrypter` to perform its legitimate read operations, that same grant also allows a compromised credential to decrypt and exfiltrate the data. CMEK does not restrict the destination of decrypted data — VPC Service Controls does.
