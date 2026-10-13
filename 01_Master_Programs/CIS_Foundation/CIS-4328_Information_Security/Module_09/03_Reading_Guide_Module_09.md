# Reading Guide: Module 09 — Cloud Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide accompanies the Module 09 video lectures. Complete all assigned readings before attempting the quiz or lab. Cloud security is tested across multiple Security+ domains, and this module's content directly supports exam objectives in Domain 2 (Architecture and Design) and Domain 4 (Operations).

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the shared responsibility model for IaaS, PaaS, and SaaS deployments
2. Describe the four core functions of a Cloud Access Security Broker (CASB)
3. Compare CASB deployment modes and select the appropriate mode for a given scenario
4. Apply encryption and access control best practices to cloud storage
5. Identify container security risks and corresponding mitigations
6. Explain the security model for serverless computing and its unique risks
7. Map cloud deployments to relevant compliance frameworks
8. Describe the key challenges and controls in a multi-cloud security strategy

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**NIST SP 800-144 — Guidelines on Security and Privacy in Public Cloud Computing**

- Publisher: National Institute of Standards and Technology
- Access: [https://csrc.nist.gov/publications/detail/sp/800-144/final](https://csrc.nist.gov/publications/detail/sp/800-144/final)
- Read: Sections 1–4 (pages 1–38)
- Focus areas: cloud deployment models, cloud service models, threats to cloud environments, security recommendations

**CSA Security Guidance for Critical Areas of Focus in Cloud Computing v4.0**

- Publisher: Cloud Security Alliance
- Access: [https://cloudsecurityalliance.org/research/guidance/](https://cloudsecurityalliance.org/research/guidance/) (free registration required)
- Read: Domain 1 (Cloud Architecture), Domain 6 (Management Plane), Domain 9 (Incident Response)
- Focus areas: shared responsibility decomposition, management plane threats, cloud-specific IR considerations

### Supplemental Reading

**OWASP Docker Security Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- Read: Full document (approximately 20 minutes)
- Focus areas: image hardening, runtime controls, secrets handling

**CIS Benchmarks for Cloud Providers (Public Summaries)**

- Access: [https://www.cisecurity.org/cis-benchmarks](https://www.cisecurity.org/cis-benchmarks)
- Read: Download the free PDF summary for AWS Foundations or Azure Security Benchmark
- Focus areas: storage encryption settings, logging configurations, IAM hardening

---

## Key Terms and Definitions

Study these terms. Each one may appear on the Security+ exam.

**Shared Responsibility Model** — The division of security obligations between a cloud provider and cloud customer, where the provider secures the underlying infrastructure and the customer secures their data, identities, and configurations.

**IaaS (Infrastructure as a Service)** — Cloud service model where the provider delivers virtualized compute, storage, and networking; the customer manages OS, middleware, application, and data.

**PaaS (Platform as a Service)** — Cloud service model where the provider manages the OS and runtime; the customer manages the application and data.

**SaaS (Software as a Service)** — Cloud service model where the provider delivers a complete application; the customer manages access, data classification, and usage policy.

**CASB (Cloud Access Security Broker)** — A security control point between users and cloud services that enforces visibility, compliance, data security, and threat protection policies.

**Shadow IT** — Cloud applications or services used by employees without official IT approval or oversight.

**Forward Proxy CASB** — CASB deployment mode where outbound traffic is routed through the CASB before reaching cloud services; requires device configuration.

**Reverse Proxy CASB** — CASB deployment mode where traffic passes through the CASB between the cloud service and the user; does not require device agents; preferred for BYOD.

**API-mode CASB** — CASB deployment mode that connects to cloud provider APIs to inspect stored content and audit logs without intercepting traffic flows.

**SSE-KMS** — Server-Side Encryption with Key Management Service; the cloud provider encrypts data using customer-managed keys stored in a key management service.

**Object Lock / WORM** — A cloud storage feature that prevents objects from being deleted or modified for a defined retention period; Write Once Read Many.

**Container** — A lightweight, portable execution environment that packages application code and dependencies and shares the host operating system kernel.

**Container Registry** — A repository for storing and distributing container images; must be secured with access controls, image scanning, and signing.

**Serverless Computing** — A cloud execution model where the provider manages all infrastructure and the customer deploys only function code; billed per execution.

**CSPM (Cloud Security Posture Management)** — Automated tools that continuously assess cloud environment configurations against security benchmarks and compliance frameworks.

**FedRAMP** — Federal Risk and Authorization Management Program; a US government compliance framework for cloud services used by federal agencies.

**CSA CCM** — Cloud Security Alliance Cloud Controls Matrix; a framework mapping security controls to cloud-specific domains, cross-referencing major compliance standards.

**Multi-cloud** — The use of cloud services from two or more distinct cloud providers within a single organization.

**Zero Trust** — A security model that requires explicit verification of every request regardless of network location; never assumes trust based on network position.

**Policy as Code** — The practice of expressing security and compliance policies as version-controlled code that is automatically enforced across infrastructure.

---

## Concept Deep Dives

### Shared Responsibility Breakdown Table

Study this table until it is second nature:

| Security Area | IaaS | PaaS | SaaS |
|---|---|---|---|
| Physical infrastructure | Provider | Provider | Provider |
| Hypervisor / virtualization | Provider | Provider | Provider |
| Operating system | **Customer** | Provider | Provider |
| Runtime / middleware | **Customer** | Provider | Provider |
| Application code | **Customer** | **Customer** | Provider |
| Data | **Customer** | **Customer** | **Customer** |
| Identity and access | **Customer** | **Customer** | **Customer** |
| Endpoint security | **Customer** | **Customer** | **Customer** |

The customer always owns data and identity. The provider always owns physical infrastructure. Everything in between depends on the model.

### CASB Decision Framework

When a scenario question describes an organization's environment, use this logic:

1. Can the organization install software on all user devices? If yes → forward proxy CASB is viable.
2. Are users on BYOD/unmanaged devices? If yes → reverse proxy or API mode.
3. Does the organization need to inspect stored cloud data rather than live traffic? If yes → API mode.
4. Does the organization need to block uploads in real time? If yes → proxy mode (forward or reverse).

### Container Image Supply Chain Security

Understand this flow for the exam and for real-world practice:

**Developer commits code → CI/CD pipeline builds image → image scanned for vulnerabilities → image signed → image pushed to private registry → deployment pulls signed image → runtime security enforced**

Breaking the chain at any point creates risk. If the scan step is skipped, vulnerable images reach production. If signing is skipped, an attacker who compromises the registry could substitute a malicious image.

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **2.2** — Summarize virtualization and cloud computing concepts (cloud models, shared responsibility, CASB, CSPM)
- **2.4** — Summarize network infrastructure concepts (cloud networking, segmentation)
- **4.1** — Given a scenario, apply common security techniques to computing resources (container hardening, serverless security)

### High-Probability Exam Topics from This Module

- Identifying the correct CASB deployment mode for a described scenario
- Determining which party (customer or provider) is responsible for a described security failure
- Distinguishing between SSE-S3, SSE-KMS, and SSE-C
- Recognizing container security misconfigurations (running as root, embedded secrets)
- Understanding FedRAMP's role in government cloud procurement

---

## Review Questions (Self-Check — Not Graded)

Answer these before the quiz to confirm comprehension:

1. A company uses AWS EC2 virtual machines. A vulnerability is discovered in the Windows Server OS running on those VMs. Who is responsible for applying the patch?

2. An organization's employees are using personal smartphones to access Microsoft 365. The security team wants to monitor and control what data users upload to Teams. Which CASB deployment mode is most appropriate and why?

3. A developer builds a Docker container and hard-codes an API key in the Dockerfile ENV instruction. What specific security risk does this create and what is the correct remediation?

4. A federal agency evaluates cloud storage vendors. What compliance authorization should they verify the vendor holds before procurement?

5. A company operates in AWS and Azure. Security configurations in AWS are properly hardened but Azure has misconfigured storage containers with public access enabled. What tool category would detect this configuration gap automatically?

6. An AWS Lambda function processes user-submitted forms and queries a database. The function's IAM role has AdministratorAccess. What principle is violated and what is the correct fix?

---

## Preparation for the Lab

The Module 09 lab uses the AWS Free Tier and focuses on cloud storage security configuration. Before the lab session:

- Create or log in to your AWS Free Tier account at [https://aws.amazon.com/free/](https://aws.amazon.com/free/)
- Verify you can access the S3 console
- Review the AWS S3 Block Public Access documentation: [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

No cloud costs are expected for the lab. All activities use Free Tier services or read-only configurations.

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 09*
