# Quiz: Module 09 — Cloud Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

This quiz contains 20 questions aligned to Security+ SY0-701 exam objectives. Questions use the same format as the actual exam: scenario-based multiple choice (single answer) and multiple-select. Time limit: 30 minutes. Each question is worth 5 points. A score of 75 or higher (15/20) is required to pass.

---

## Questions

**Question 1**

A company migrates its HR database to an AWS RDS managed database service. After migration, a vulnerability scanner detects that the underlying database engine is running an outdated version with known CVEs. Who is responsible for patching the database engine in this scenario?

- A. The company, because all software vulnerabilities are the customer's responsibility
- B. AWS, because RDS is a managed service and AWS patches the database engine
- C. The company, because RDS is IaaS and the customer manages the OS
- D. Neither party — patching managed services is an optional cloud feature

---

**Question 2**

An organization's security team wants to prevent employees from uploading sensitive documents to personal cloud storage services such as consumer Dropbox accounts. The employees use a mix of company-managed laptops and personal smartphones. Which CASB deployment mode is BEST suited for this requirement?

- A. Forward proxy, because it inspects all outbound traffic
- B. API mode, because it connects to Dropbox's API to monitor uploads
- C. Reverse proxy, because it does not require agents on unmanaged devices
- D. Inline DLP sensor, because it operates at the network perimeter

---

**Question 3**

A security engineer reviews an S3 bucket and finds the following configuration: encryption is disabled, Block Public Access is off, and there is a bucket policy granting `s3:GetObject` to `"Principal": "*"`. Which combination of actions addresses all three findings? (Select TWO)

- A. Enable Block Public Access
- B. Enable MFA delete on the bucket
- C. Enable default encryption (SSE-KMS)
- D. Enable CloudTrail for the account
- E. Change bucket storage class to Glacier

---

**Question 4**

A developer builds a Docker container for a web application. During a security review, an analyst discovers that the container runs as root, has access to all Linux capabilities, and the production database password is stored as a plain-text environment variable. Which finding poses the GREATEST immediate security risk?

- A. Running as root
- B. Access to all Linux capabilities
- C. Plain-text database password in an environment variable
- D. Using Docker instead of a virtual machine

---

**Question 5**

An organization uses AWS Lambda functions to process customer payment data. A penetration tester reports that one Lambda function's IAM execution role has the `AdministratorAccess` managed policy attached. Which security principle does this violate?

- A. Defense in depth
- B. Separation of duties
- C. Least privilege
- D. Need to know

---

**Question 6**

A company must comply with US federal government security requirements before its cloud-hosted application can process federal agency data. Which compliance authorization should the company obtain?

- A. ISO 27001 certification
- B. SOC 2 Type II report
- C. FedRAMP Authority to Operate (ATO)
- D. CSA STAR Level 2 certification

---

**Question 7**

A CASB solution is deployed in API mode. A security analyst reports that the CASB successfully audits files stored in Microsoft SharePoint but cannot block a user from uploading a sensitive file to SharePoint in real time. Which limitation of API-mode CASB explains this behavior?

- A. API mode cannot connect to Microsoft 365 services
- B. API mode inspects stored content and logs after the fact but does not intercept live traffic flows
- C. API mode requires agent installation on user devices
- D. API mode only works with IaaS services, not SaaS

---

**Question 8**

An organization stores audit logs in the same S3 bucket as the application data they audit. A ransomware attack encrypts all files in the bucket, including the logs. Which security configuration would have prevented the loss of audit integrity? (Select TWO)

- A. Enable S3 Object Lock with Compliance mode on the logging bucket
- B. Store access logs in a separate, dedicated logging bucket
- C. Enable server access logging on the same bucket
- D. Use SSE-S3 encryption instead of SSE-KMS
- E. Enable S3 Transfer Acceleration

---

**Question 9**

A cloud security architect is evaluating a vendor that provides SaaS payroll software. The architect requests documentation proving that the vendor's security controls have been independently tested over a six-month period. Which document satisfies this requirement?

- A. The vendor's ISO 27001 certificate
- B. A SOC 2 Type I report
- C. A SOC 2 Type II report
- D. The vendor's penetration test executive summary

---

**Question 10**

A multinational organization deploys workloads across AWS, Azure, and Google Cloud. The security team struggles to maintain consistent encryption and logging configurations across all three platforms. Which tool category addresses this challenge most directly?

- A. SIEM (Security Information and Event Management)
- B. CASB (Cloud Access Security Broker)
- C. CSPM (Cloud Security Posture Management)
- D. WAF (Web Application Firewall)

---

**Question 11**

Which of the following BEST describes the shared responsibility model for SaaS?

- A. The customer manages the OS and the provider manages the application
- B. The provider manages the application and the customer manages data and access
- C. The customer manages networking and the provider manages identity
- D. Both the provider and customer share equal responsibility for all layers

---

**Question 12**

A security team discovers that multiple employees have been using an unapproved file-sharing service to collaborate on work documents. This is an example of which threat category?

- A. Insider threat
- B. Shadow IT
- C. Data exfiltration
- D. Privilege escalation

---

**Question 13**

A DevOps engineer wants to ensure that container images deployed to production have not been tampered with after they were scanned and approved. Which security control addresses this requirement?

- A. Runtime application self-protection (RASP)
- B. Container image signing and verification
- C. Web application firewall (WAF) integration
- D. Network segmentation between containers

---

**Question 14**

An organization must ensure that customer data stored in a European data center cannot be accessed by the cloud provider's administrators in other regions. This requirement relates to which cloud security concept?

- A. Encryption in transit
- B. Data sovereignty and residency controls
- C. Multi-cloud federation
- D. CASB API mode inspection

---

**Question 15**

A serverless function processes user-submitted search queries and passes them directly to a database query string without sanitization. What attack is this function vulnerable to?

- A. Cross-site scripting (XSS)
- B. SQL injection
- C. CSRF (Cross-Site Request Forgery)
- D. Privilege escalation via IAM role assumption

---

**Question 16**

An organization implements federated identity management using SAML to connect Azure Active Directory to AWS, GCP, and Salesforce. What is the PRIMARY security benefit of this approach in a multi-cloud environment?

- A. It eliminates the need for MFA across all connected services
- B. It provides a single source of truth for user identities and enables centralized access revocation
- C. It automatically enforces least privilege on cloud service IAM roles
- D. It replaces the need for encryption keys in each cloud environment

---

**Question 17**

A company's security policy requires that all S3 bucket objects be encrypted and that the encryption keys can be audited and revoked by the security team. Which encryption option meets BOTH requirements?

- A. SSE-S3 (Amazon S3 managed keys)
- B. SSE-KMS with AWS-managed keys
- C. SSE-KMS with customer-managed keys in AWS KMS
- D. Client-side encryption with keys stored on developer workstations

---

**Question 18**

A Zero Trust architecture is being implemented for a multi-cloud environment. Which statement BEST describes how Zero Trust applies to cloud workloads?

- A. Workloads on the same cloud VPC are automatically trusted and do not require authentication
- B. Every service-to-service request must be authenticated and authorized regardless of network location
- C. Zero Trust applies only to user-facing applications, not to backend cloud services
- D. Zero Trust replaces the need for network segmentation in cloud environments

---

**Question 19**

During a cloud security audit, an analyst finds that a development team has disabled CloudTrail logging in a non-production AWS account to "reduce costs." Why is this a security concern even in non-production environments?

- A. Development accounts never contain sensitive data
- B. Attackers who compromise development accounts can use them as pivot points to production; logging loss eliminates the ability to reconstruct attack timelines
- C. CloudTrail is only required for PCI DSS compliance
- D. Logging is a shared responsibility and AWS is responsible for maintaining it

---

**Question 20**

A security team uses Policy as Code to enforce that all S3 buckets must have versioning enabled. A developer creates a new bucket without versioning and the automated policy check immediately flags and blocks the deployment. Which security benefit does this illustrate?

- A. Defense in depth at the data layer
- B. Shift-left security — catching misconfigurations at deployment time rather than after the fact
- C. Just-in-time access provisioning for cloud resources
- D. Separation of duties between development and operations teams

---

## Answer Key

*For instructor use only — do not distribute to students*

| Question | Answer | Objective |
|---|---|---|
| 1 | B | 2.2 — Shared responsibility (managed service) |
| 2 | C | 2.2 — CASB deployment modes |
| 3 | A, C | 2.2 — Cloud storage hardening |
| 4 | C | 2.2 — Container security |
| 5 | C | 2.3 — Least privilege |
| 6 | C | 2.2 — Cloud compliance frameworks |
| 7 | B | 2.2 — CASB limitations |
| 8 | A, B | 2.2 — Log integrity, object lock |
| 9 | C | 2.2 — SOC 2 Type II |
| 10 | C | 2.2 — CSPM |
| 11 | B | 2.2 — Shared responsibility SaaS |
| 12 | B | 2.2 — Shadow IT |
| 13 | B | 2.2 — Container image signing |
| 14 | B | 2.2 — Data sovereignty |
| 15 | B | 1.3 — Injection attacks in serverless |
| 16 | B | 2.2 — Federated identity |
| 17 | C | 2.2 — SSE-KMS customer-managed |
| 18 | B | 2.2 — Zero Trust in cloud |
| 19 | B | 4.1 — Logging and monitoring |
| 20 | B | 2.2 — Policy as Code / shift-left |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 09*
