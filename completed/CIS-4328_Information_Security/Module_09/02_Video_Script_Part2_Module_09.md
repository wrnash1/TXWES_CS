# Video Script: Module 09 — Cloud Security (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Container Security Basics (4 minutes)

Welcome back to Module 9. In Part 1 we covered the shared responsibility model, CASBs, and secure cloud storage. Now we dig into containers, serverless, compliance, and multi-cloud strategy.

Containers are everywhere in modern cloud deployments. Docker and Kubernetes have become the default way organizations package and deploy applications. Security+ expects you to understand the security implications.

### What Is a Container?

A container packages application code, dependencies, and configuration into a portable, isolated unit. Unlike virtual machines, containers share the host OS kernel. That sharing is both a performance advantage and a security consideration — a compromised container running with excessive privileges could potentially affect the host or neighboring containers.

### Container Security Concepts

**Image security** — Every container starts from an image. If that image contains vulnerable software, every container deployed from it inherits that vulnerability. Best practices:

- Use minimal base images (Alpine Linux instead of Ubuntu where possible)
- Scan images with tools like Trivy, Clair, or AWS ECR scanning before deployment
- Never pull images from unverified public registries without scanning
- Use image signing (Docker Content Trust, Sigstore/Cosign) to verify image integrity

**Runtime security** — Once a container is running, enforce the principle of least privilege:

- Run containers as non-root users
- Use read-only file systems where possible
- Limit Linux capabilities with `--cap-drop=ALL` and add back only what is needed
- Use security profiles (AppArmor, seccomp) to restrict system calls

**Network security for containers** — Containers communicate over virtual networks. In Kubernetes, use Network Policies to restrict which pods can communicate with which other pods. Apply a default-deny posture and explicitly allow required connections.

**Secrets management** — Never embed secrets (passwords, API keys, certificates) in container images or environment variables in plain text. Use Kubernetes Secrets (with encryption at rest enabled), HashiCorp Vault, or AWS Secrets Manager.

### Registry Security

The container registry is where images are stored. Secure it like any other software artifact repository:

- Enable access controls — not everyone needs push rights
- Enable vulnerability scanning on push
- Implement image lifecycle policies to delete old, unpatched images
- Use private registries for production images; avoid public Docker Hub for sensitive workloads

---

## Segment 2 — Serverless Security (3 minutes)

Serverless computing — AWS Lambda, Azure Functions, Google Cloud Functions — takes the PaaS model even further. You write a function, deploy it, and the provider handles everything: OS, runtime, scaling, and availability. You are billed per execution, not per server.

### Security Benefits of Serverless

- No OS to patch — the provider manages the runtime
- Short-lived execution environments limit persistence for attackers
- Fine-grained IAM roles per function enforce least privilege
- Automatic scaling eliminates some DDoS vectors

### Serverless Security Risks

**Over-privileged functions** — The most common serverless security mistake is giving a Lambda function an IAM role with `AdministratorAccess` "because it was easy." Every function should have a role granting only the exact permissions it needs. If a function only reads from one S3 bucket, its role should only allow `s3:GetObject` on that specific bucket ARN.

**Injection attacks** — Serverless functions still process untrusted input. SQL injection, command injection, and SSRF (Server-Side Request Forgery) attacks are all possible if input is not validated. The code is your responsibility.

**Dependency vulnerabilities** — Functions import libraries. Those libraries have vulnerabilities. Scan your function packages as part of your CI/CD pipeline.

**Event source abuse** — Functions are triggered by events: HTTP requests, S3 uploads, SQS messages, database changes. An attacker who can write to an S3 bucket can trigger your Lambda. Validate and sanitize all event data.

**Cold start information leakage** — Some developers log debugging information during cold starts. Ensure logging does not include secrets, credentials, or sensitive data.

### Exam Tip

Serverless is tested in the context of shared responsibility and least privilege. Expect questions about which layer the customer secures in a serverless model (function code, IAM roles, data) versus what the provider secures (runtime, OS, infrastructure).

---

## Segment 3 — Cloud Compliance Frameworks (4 minutes)

Cloud environments must comply with the same regulatory requirements as on-premises environments — sometimes more, because cloud introduces new data flow patterns. Security+ tests your awareness of how compliance frameworks apply in the cloud.

### Key Compliance Frameworks

**CSA Cloud Controls Matrix (CCM)** — Published by the Cloud Security Alliance, the CCM maps security controls to cloud-specific risk areas across 17 domains including data security, identity management, and infrastructure security. It cross-references ISO 27001, NIST, PCI DSS, and HIPAA.

**FedRAMP (Federal Risk and Authorization Management Program)** — Required for cloud services used by US federal agencies. Providers get a FedRAMP authorization (Authority to Operate) that agencies can reuse. If you work with government clients, your cloud provider must be FedRAMP authorized.

**ISO/IEC 27017** — An extension of ISO 27001 specifically for cloud services. Provides guidance for both cloud service providers and cloud service customers.

**SOC 2 Type II** — A third-party audit report covering security, availability, processing integrity, confidentiality, and privacy. Type II covers controls over a period of time (usually 6-12 months). Requesting SOC 2 reports from your cloud vendors validates their control effectiveness.

### Cloud Compliance Responsibilities

Even with a compliant cloud provider, your workloads must independently comply. A HIPAA-covered entity using AWS cannot assume AWS's HIPAA compliance covers their application. The business associate agreement (BAA) with AWS covers the provider's infrastructure; the covered entity must still implement application-level controls.

Key cloud compliance controls you are responsible for:

- Data classification and labeling
- Encryption key management
- Access control and audit logging
- Incident response capability
- Data residency requirements (some regulations require data to stay within specific geographic regions)

### Cloud Security Posture Management (CSPM)

CSPM tools continuously assess cloud configurations against compliance benchmarks. Examples: AWS Security Hub (maps to CIS Benchmarks, NIST, PCI DSS), Microsoft Defender for Cloud, Prisma Cloud. These tools flag misconfigurations before auditors do.

---

## Segment 4 — Multi-Cloud Security Strategy (4 minutes)

Most enterprises today use multiple cloud providers. A 2024 survey found over 87% of organizations use more than one cloud. Multi-cloud brings resilience and vendor negotiating leverage, but it multiplies the security complexity.

### Multi-Cloud Security Challenges

**Inconsistent identity management** — AWS IAM, Azure Active Directory, and Google Cloud IAM have different models, different terminology, and different default behaviors. A user might have least-privilege access in AWS and accidentally over-privileged access in Azure because the configuration was assumed to work the same way.

**Fragmented visibility** — Security alerts are spread across three different consoles. Without centralization, incidents can be missed or slow to detect.

**Configuration drift** — Enforcing consistent security baselines (encryption enabled, logging on, public access blocked) across three clouds with different native tools is operationally difficult.

**Data governance across clouds** — Data flows between clouds create jurisdiction and classification challenges. GDPR data stored in AWS EU and processed in Google Cloud must meet requirements in both platforms.

### Multi-Cloud Security Controls

**Centralized SIEM** — Forward security logs from all clouds to a single SIEM (Splunk, Microsoft Sentinel, IBM QRadar). Correlate events across providers.

**Cloud-agnostic IAM federation** — Use a federated identity provider (Okta, Azure AD, Ping) as the single source of truth for user identities. Each cloud trusts this IdP through SAML or OIDC federation. Users authenticate once and get time-limited credentials in each cloud.

**Policy as Code** — Define security policies in code using tools like HashiCorp Sentinel, Open Policy Agent (OPA), or AWS Service Control Policies. Version-control these policies and apply them consistently across providers.

**Multi-cloud CSPM** — Use a vendor-neutral CSPM tool that covers all your clouds. Wiz, Prisma Cloud, and Orca Security are examples that provide unified posture management across AWS, Azure, and GCP.

**Zero Trust in multi-cloud** — Never assume workloads are trusted because they are in your cloud. Authenticate and authorize every request explicitly, regardless of network location. Use mutual TLS between services, short-lived credentials, and just-in-time access.

### Defense in Depth for Cloud

Apply the same defense-in-depth principle you know from on-premises:

- **Perimeter layer**: WAF, DDoS protection, network ACLs
- **Network layer**: VPC segmentation, security groups, private endpoints
- **Compute layer**: OS hardening, container security, patch management
- **Application layer**: input validation, secure coding, secrets management
- **Data layer**: encryption at rest and in transit, DLP, access logging
- **Identity layer**: MFA, least privilege, PAM for privileged access

---

## Module 09 Full Summary

Cloud security is not a separate discipline — it is the application of security fundamentals to an environment where someone else runs the hardware. The core concepts you must own for Security+ are:

- Shared responsibility model across IaaS, PaaS, and SaaS
- CASB deployment modes and the four visibility, compliance, DLP, threat-protection functions
- Secure cloud storage: encryption key management, access controls, bucket misconfiguration risks
- Container security: image scanning, runtime least privilege, secrets management
- Serverless security: over-privileged functions, injection risks, event source validation
- Compliance: CSA CCM, FedRAMP, SOC 2 Type II, your independent obligations
- Multi-cloud strategy: federated identity, centralized logging, CSPM, Zero Trust

Read the Reading Guide, complete the lab exercise, and take the quiz before the discussion deadline. See you in Module 10.

---

*End of Part 2 Script*
