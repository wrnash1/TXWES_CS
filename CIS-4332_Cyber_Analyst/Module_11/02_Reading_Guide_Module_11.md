# Reading Guide: Module 11 - Cloud Security Monitoring
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 11 - Cloud Security Monitoring**! This module covers how security analysts monitor cloud environments for threats, misconfigurations, and compliance violations. You will learn how cloud service models (IaaS, PaaS, SaaS) affect the shared responsibility for security monitoring, how cloud-native logging and audit trail tools work, and how to detect common cloud-specific attack techniques such as misconfigured storage, credential abuse, and excessive IAM permissions. These topics are tested under **Domain 1: Security Operations (33%)** and **Domain 2: Vulnerability Management (30%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn cloud audit logging, CSPM concepts, and how to identify cloud misconfigurations that expose data or allow unauthorized access. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Shared Responsibility Model**: A cloud security framework that defines which security controls are the cloud provider's responsibility and which are the customer's responsibility — and the boundary shifts depending on service model. In IaaS, the customer is responsible for the OS, applications, and data; in PaaS, the provider manages the infrastructure and runtime; in SaaS, the provider manages nearly everything and the customer is responsible only for data and access management. CySA+ tests whether you correctly assign responsibility for a given control to the provider or customer in specific service model scenarios.
*   **Cloud Security Posture Management (CSPM)**: A category of tooling that continuously audits cloud environment configurations against security best practices and compliance benchmarks, alerting when resources are misconfigured — for example, an S3 bucket set to public, a security group with port 22 open to the entire internet, or MFA not enabled on a root account. CSPM is the primary mechanism for detecting cloud misconfiguration, which is the leading cause of cloud data breaches.
*   **Cloud Audit Logs (e.g., AWS CloudTrail, Azure Monitor)**: Cloud-native logging services that record all API calls, configuration changes, and user/service account activity within a cloud environment. Analysts use these logs to detect unauthorized access, privilege escalation attempts, and data exfiltration from cloud services. CySA+ tests knowledge of what these logs record and how they are used in incident investigation.

---

### 2. Certification Exam Tips
*   **Focus Area – Shared Responsibility (Domain 1):** CySA+ CS0-003 scenario questions often describe a cloud security gap and ask who is responsible for fixing it. The shared responsibility model is the framework for answering: the customer always owns data classification and access management regardless of service model; the provider owns physical infrastructure security in all models.
*   **Scenario Trap – Misconfiguration vs. Vulnerability:** Cloud data breaches most commonly result from misconfiguration (public S3 buckets, overpermissive IAM roles, disabled MFA) rather than software vulnerabilities. CySA+ tests whether you recognize that CSPM and configuration auditing — not just patch management — are required for cloud security.
*   **Cloud IAM Privilege Escalation:** Attackers who compromise a low-privilege cloud account often attempt IAM privilege escalation by attaching more permissive policies or assuming higher-privileged roles. Cloud audit logs (CloudTrail, Azure Activity Log) record these `AttachRolePolicy` and `AssumeRole` API calls, making them detectable. Know these log sources for CySA+ investigation scenarios.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist includes cloud security monitoring concepts, misconfiguration identification, and cloud audit log analysis scenarios mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource covers cloud-specific threat detection and shared responsibility scenarios.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Cloud Security** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details cloud service models, shared responsibility, and cloud monitoring techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Cloud Security Monitoring** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of cloud audit log review and misconfiguration detection workflows.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Review AWS CloudTrail logs for suspicious API calls**: Using a provided sample CloudTrail log export (JSON format), identify any `CreateUser`, `AttachUserPolicy`, or `AssumeRole` API calls made outside business hours or from unexpected source IP addresses — document the principal, action, timestamp, and source IP for each suspicious call.
*   **Identify a cloud misconfiguration using a CSPM audit report**: Review a provided CSPM scan report showing an S3 bucket with public read access enabled and an EC2 security group with `0.0.0.0/0` allowed on port 22 — classify each finding by severity, identify the correct remediation, and explain which party (provider or customer) is responsible for the fix under the shared responsibility model.
*   **Map a cloud attack to an ATT&CK technique**: Using the suspicious API calls identified in step one, map the activity to the most relevant MITRE ATT&CK for Cloud technique (e.g., T1078.004 – Valid Accounts: Cloud Accounts, or T1098 – Account Manipulation) and document the mapping in the lab report.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Cloud Security** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Cloud Security Monitoring** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the cloud audit log analysis and CSPM review steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
