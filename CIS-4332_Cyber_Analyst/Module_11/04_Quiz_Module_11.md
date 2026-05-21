# Quiz: Module 11 - Cloud Security Monitoring
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Under the cloud shared responsibility model, which security control is ALWAYS the customer's responsibility regardless of whether the service model is IaaS, PaaS, or SaaS?

*   A) Physical security of the data center hardware and network infrastructure
*   B) Patching and maintaining the hypervisor and underlying virtualization layer
*   C) Data classification and management of user access to the data
*   D) Operating system patching and configuration hardening on underlying servers
*   **Correct Answer:** C) Data classification and management of user access to the data.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Physical security of the data center is always the cloud provider's responsibility across all service models — the customer never owns or manages the physical infrastructure.
    *   *Why B is incorrect:* Hypervisor patching and virtualization layer maintenance is the provider's responsibility in all cloud service models; the customer does not have access to the hypervisor layer.
    *   *Why C is correct:* Regardless of service model, the customer always retains responsibility for classifying their own data and controlling who has access to it. The provider cannot determine data sensitivity or authorize specific users — only the customer can. CySA+ consistently uses this as the "always customer" anchor in shared responsibility questions.
    *   *Why D is incorrect:* OS patching responsibility varies by service model — it is the customer's responsibility in IaaS (they manage the OS) but the provider's in PaaS and SaaS (they manage the OS and runtime). It is not universally the customer's responsibility across all models.

---

**Question 2**
In cloud security monitoring, which of the following most accurately defines **Cloud Security Posture Management (CSPM)**?

*   A) A service that provides real-time DDoS protection by scrubbing volumetric attack traffic before it reaches cloud-hosted applications
*   B) A category of tooling that continuously audits cloud resource configurations against security best practices and compliance benchmarks, alerting when misconfigurations create security risk
*   C) A cloud-native key management service that generates, rotates, and stores cryptographic keys used to encrypt data at rest in cloud storage services
*   D) A network access control mechanism that enforces zero-trust policies by requiring device compliance verification before allowing connections to cloud workloads
*   **Correct Answer:** B) A category of tooling that continuously audits cloud resource configurations against security best practices and compliance benchmarks, alerting when misconfigurations create security risk.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DDoS scrubbing describes a network protection service (e.g., AWS Shield, Cloudflare); it is unrelated to configuration auditing. CSPM addresses misconfigurations, not volumetric attacks.
    *   *Why B is correct:* CSPM tools (e.g., AWS Security Hub, Microsoft Defender for Cloud, Prisma Cloud) continuously scan cloud environment configurations — IAM policies, storage permissions, network security groups, encryption settings — and alert when they deviate from security benchmarks such as CIS Cloud Foundations. Misconfiguration is the leading cause of cloud data breaches, making CSPM a critical detective control.
    *   *Why C is incorrect:* Cloud key management services (e.g., AWS KMS, Azure Key Vault) manage cryptographic keys for encryption — a data protection function, not a configuration posture auditing function.
    *   *Why D is incorrect:* Zero-trust network access control describes a device/identity verification mechanism; it addresses who can connect, not whether the cloud environment's configuration is secure.

---

**Question 3**
A security analyst reviews AWS CloudTrail logs and finds that a low-privilege IAM user account executed `AttachUserPolicy` to add the `AdministratorAccess` managed policy to their own account at 2:47 AM, followed immediately by the creation of a new IAM user with administrative rights. Which threat does this activity most strongly indicate?

*   A) A data exfiltration attempt — the user is downloading sensitive data from S3 buckets using the new administrative account credentials
*   B) Cloud IAM privilege escalation — the compromised low-privilege account is elevating its own permissions to gain administrative control of the cloud environment
*   C) A denial-of-service attack — the attacker is launching EC2 instances at scale to exhaust the organization's cloud compute quota
*   D) A supply chain attack — the attacker has compromised a third-party cloud provider integration to inject malicious code into the deployment pipeline
*   **Correct Answer:** B) Cloud IAM privilege escalation — the compromised low-privilege account is elevating its own permissions to gain administrative control of the cloud environment.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The described API calls (`AttachUserPolicy`, new admin user creation) are privilege escalation actions — they establish elevated access. Data exfiltration would be indicated by S3 `GetObject` calls with large data volumes or unusual destination IPs, not IAM policy modification.
    *   *Why B is correct:* Attaching `AdministratorAccess` to one's own account and then creating a backdoor admin user are the textbook indicators of cloud IAM privilege escalation (MITRE ATT&CK T1098 – Account Manipulation). CloudTrail logs capturing these `AttachUserPolicy` calls at an unusual hour from a low-privilege account represent a high-confidence confirmed attack.
    *   *Why C is incorrect:* A denial-of-service via EC2 instance launch would appear as `RunInstances` API calls at scale, not IAM policy modification events.
    *   *Why D is incorrect:* A supply chain attack targets the software delivery pipeline; the described activity is direct IAM manipulation using a compromised credential, not pipeline code injection.

---

**Question 4**
A CSPM tool reports that an S3 bucket containing customer records has `Block Public Access` disabled and a bucket policy granting `s3:GetObject` to `"Principal": "*"`. The analyst must remediate this finding immediately. Which action directly resolves the misconfiguration?

*   A) Enable server-side encryption on the S3 bucket using AWS KMS to ensure all objects are encrypted at rest
*   B) Enable `Block Public Access` on the S3 bucket and remove or restrict the bucket policy so that public unauthenticated access is no longer permitted
*   C) Enable AWS CloudTrail logging for the S3 bucket to capture all future access events for audit purposes
*   D) Move the customer records to an encrypted EBS volume attached to an EC2 instance to prevent S3-layer exposure
*   **Correct Answer:** B) Enable `Block Public Access` on the S3 bucket and remove or restrict the bucket policy so that public unauthenticated access is no longer permitted.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Enabling encryption protects data confidentiality if storage media is physically compromised; it does not prevent unauthenticated access over the internet from a misconfigured public bucket. The data is still fully readable by anyone who can retrieve the objects.
    *   *Why B is correct:* The misconfiguration has two components: `Block Public Access` is disabled (allowing public access settings to take effect) and the bucket policy grants `s3:GetObject` to `"*"` (everyone). Fixing both — enabling Block Public Access and removing the public-grant policy — directly removes the unauthenticated access exposure. This is the correct CSPM remediation action.
    *   *Why C is incorrect:* Enabling CloudTrail logging records who accessed the bucket after the fact; it does not prevent public access. Logging is a detective control, not a preventive one — and does not resolve the misconfiguration.
    *   *Why D is incorrect:* Moving data to an EBS volume is an infrastructure redesign, not a targeted remediation. It also introduces new complexity and does not address the root cause (the misconfigured S3 access policy).

---

**Question 5**
An organization migrating workloads to a public cloud IaaS environment wants to ensure it can detect unauthorized configuration changes and suspicious API activity across its cloud accounts. Which two controls together best achieve this goal?

*   A) Deploy full-disk encryption on all virtual machine instances and configure automatic key rotation through the cloud provider's key management service
*   B) Enable cloud audit logging (e.g., AWS CloudTrail, Azure Activity Log) across all accounts and regions, and integrate the logs into a SIEM with correlation rules that alert on high-risk API calls such as IAM policy changes, security group modifications, and root account usage
*   C) Configure auto-scaling groups to automatically replace any EC2 instance that fails a health check, ensuring continuous application availability
*   D) Require all developers to use MFA for console access and enforce least-privilege IAM roles scoped to each team's specific job functions
*   **Correct Answer:** B) Enable cloud audit logging across all accounts and regions, and integrate the logs into a SIEM with correlation rules that alert on high-risk API calls such as IAM policy changes, security group modifications, and root account usage.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disk encryption and key rotation protect data confidentiality at rest; they do not detect unauthorized configuration changes or suspicious API activity. Encryption is a preventive data protection control, not a monitoring control.
    *   *Why B is correct:* Cloud audit logs (CloudTrail, Azure Activity Log) capture every API call — who made it, what resource was affected, and when. Without them, there is no visibility into cloud configuration changes. Integrating these logs into a SIEM with targeted correlation rules on high-risk actions (IAM modifications, security group changes, root usage) provides the alert layer that surfaces suspicious activity for analyst review. Together these deliver the detection capability the question requires.
    *   *Why C is incorrect:* Auto-scaling health checks address application availability and fault tolerance; they do not monitor for unauthorized configuration changes or security-relevant API calls.
    *   *Why D is incorrect:* MFA and least-privilege IAM reduce the risk of compromise and limit blast radius, but they are preventive access controls — they do not detect unauthorized configuration changes that occur through compromised or overpermissive credentials already in use.
