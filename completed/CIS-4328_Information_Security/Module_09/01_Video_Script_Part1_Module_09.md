# Video Script: Module 09 — Cloud Security (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Introduction and Cloud Security Fundamentals (3 minutes)

Welcome to Module 9, Cloud Security. By now you have a solid grounding in identity management and network controls. This module bridges those concepts into the cloud environment, which is where most enterprise workloads now live. For the Security+ exam, cloud security topics appear throughout Domain 2 (Architecture and Design) and Domain 4 (Operations and Incident Response), so what we cover today has direct exam weight.

Let me start with a question: when your company moves a database to AWS, who is responsible for patching the operating system underneath it? Who locks down the network ports? Who encrypts the data at rest? The answer depends entirely on which cloud service model you chose — and that is the heart of cloud security.

### The Three Cloud Service Models

Start here because everything else flows from this.

**Infrastructure as a Service (IaaS)** means you rent raw compute, storage, and networking. You get a virtual machine and a disk. You are responsible for the OS, the middleware, the application, and the data. AWS EC2, Azure Virtual Machines, and Google Compute Engine are examples. Security responsibility is heavily on you.

**Platform as a Service (PaaS)** means the provider manages the OS and runtime. You deploy your application and data. AWS Elastic Beanstalk, Azure App Service, and Google App Engine fall here. The provider patches the platform; you secure your code and data.

**Software as a Service (SaaS)** means the provider runs the entire application. You configure it and use it. Microsoft 365, Salesforce, and Google Workspace are SaaS. You are responsible for user access management and data classification. The provider handles everything underneath.

As you move from IaaS to SaaS, the provider takes on more responsibility and you take on less — but that does not mean less risk. It means the risks change shape.

---

## Segment 2 — Shared Responsibility Model in Depth (4 minutes)

The **Shared Responsibility Model** is one of the most important concepts in cloud security, and Security+ will test it directly. Every major cloud provider publishes their own version of this diagram, but the principle is always the same: security *of* the cloud belongs to the provider, and security *in* the cloud belongs to you.

### What the Provider Always Owns

- Physical security of data centers (guards, fences, biometrics, 24/7 surveillance)
- Hardware maintenance (servers, storage arrays, networking gear)
- Hypervisor security (the software that runs virtual machines)
- Global network infrastructure

No matter what service model you use, these are never your problem. If a server catches fire in Amazon's Oregon data center, that is Amazon's incident, not yours.

### What You Always Own

- Your data
- Your identity and access management decisions (who has what permissions)
- Endpoint devices that connect to cloud services
- Your contractual and regulatory obligations

If your employee downloads 50,000 customer records to a personal laptop and that laptop is stolen, that is your breach — not Amazon's.

### The Gray Zone by Service Model

Here is where students get tripped up on the exam. In IaaS, you own the OS, so OS patching is your job. If you run an unpatched Windows Server 2019 VM on AWS and it gets exploited via EternalBlue, AWS is not at fault. In PaaS, you own the application layer, so SQL injection in your code is your bug. In SaaS, you own user provisioning, so if you never remove a terminated employee's Microsoft 365 account, that is your oversight.

A practical memory device: think of the shared responsibility model as a lease on an apartment. The landlord (provider) maintains the building structure, plumbing, and electrical panel. You (the tenant) maintain what is inside your unit. If you leave the front door unlocked, the landlord is not liable.

### Exam Tip

Security+ scenario questions love this pattern: "A company uses SaaS and a data breach occurs because users had excessive permissions. Who is responsible?" The answer is the company — permission management is always the customer's responsibility regardless of service model.

---

## Segment 3 — Cloud Access Security Broker (CASB) (4 minutes)

Now that you understand the shared responsibility divide, let us talk about a control that helps enforce your side of that divide: the **Cloud Access Security Broker**, or **CASB**.

A CASB sits between your users and cloud services and enforces your security policies. Think of it as a security checkpoint on the highway between your users' devices and every cloud application they access.

### Four Core CASB Functions

**Visibility** — A CASB gives you a complete inventory of every cloud service being used in your organization, including shadow IT. Shadow IT refers to cloud apps that employees use without IT approval. A CASB can detect that your marketing team is uploading files to a consumer Dropbox account and alert security.

**Compliance** — A CASB can enforce data handling policies required by HIPAA, PCI DSS, GDPR, or your internal policy. If a user attempts to upload a file containing credit card numbers to an unauthorized service, the CASB can block or log it.

**Data Security** — CASBs integrate with data loss prevention (DLP) capabilities. They can inspect content going to cloud services in real time and apply encryption, masking, or blocking based on classification rules.

**Threat Protection** — CASBs detect anomalous behavior. If a user account suddenly downloads 10,000 files at 2 AM from an unfamiliar country, that is a behavioral anomaly the CASB flags.

### CASB Deployment Modes

**Proxy mode (forward proxy)** — traffic from your users is routed through the CASB before reaching cloud services. You get deep inspection but must configure devices to use the proxy.

**Reverse proxy mode** — traffic passes through the CASB when coming from the cloud back to users. This is useful for BYOD environments where you cannot install agents on devices.

**API mode** — the CASB connects directly to cloud service APIs (like Microsoft 365 Graph API) to inspect stored data, audit logs, and configurations. No traffic redirection required, but visibility is limited to what the API exposes.

### Exam Tip

Know the difference between a forward proxy CASB, a reverse proxy CASB, and API-mode CASB. Questions may describe a scenario — "the organization cannot install software on user devices" — and ask which CASB mode fits. Reverse proxy or API mode are the answers for BYOD/unmanaged devices.

---

## Segment 4 — Secure Cloud Storage (4 minutes)

Cloud storage introduces unique security considerations that do not exist in traditional on-premises storage.

### Encryption at Rest

Every major cloud provider offers server-side encryption. AWS S3 uses AES-256 by default. The question is: who holds the keys? There are three options:

**Provider-managed keys (SSE-S3 / Google-managed)** — easiest, zero configuration, but the provider can theoretically access your data (relevant for compliance with certain jurisdictions).

**Customer-managed keys (SSE-KMS)** — you create and control keys in AWS Key Management Service or Azure Key Vault. The provider encrypts/decrypts on your behalf using your key. You can audit key usage and revoke access.

**Customer-provided keys (SSE-C)** — you send your key with every API request. The provider uses it but never stores it. Maximum control, but you must manage key distribution yourself.

### Encryption in Transit

All data moving to and from cloud storage must use TLS 1.2 or higher. Most providers enforce this, but you must verify bucket/container policies do not allow HTTP fallback. A misconfigured S3 bucket that allows unencrypted connections is a finding in any cloud security audit.

### Access Controls and Bucket Misconfiguration

One of the most common cloud security failures is a misconfigured storage bucket. An S3 bucket set to "public" has exposed sensitive data for hundreds of organizations. Security+ expects you to know:

- **Bucket policies** control access at the bucket level (what principals can access what resources)
- **ACLs (Access Control Lists)** control access at the object level (legacy mechanism, still tested)
- **Block Public Access settings** in AWS is a guardrail that prevents public configuration even if a policy would allow it

Always enable Block Public Access. Audit bucket policies regularly. Use cloud security posture management (CSPM) tools to flag misconfigurations automatically.

### Object Versioning and Immutability

Enable versioning on storage buckets so you can recover from accidental deletion or ransomware. Some providers offer **object lock** (WORM — Write Once Read Many), which prevents objects from being deleted or modified for a defined retention period. This is valuable for compliance audit logs and legal hold scenarios.

---

## Module 09 Part 1 Summary

Let us recap what we covered:

- Cloud service models (IaaS, PaaS, SaaS) define how security responsibility is divided
- The shared responsibility model draws a clear line: provider owns the infrastructure, you own your data and identities
- CASBs enforce your cloud security policies through visibility, compliance, DLP, and threat protection
- Secure cloud storage requires encryption at rest with appropriate key management, TLS in transit, and strict access controls to prevent bucket misconfiguration

In Part 2, we will cover container security, serverless security, cloud compliance frameworks, and multi-cloud security strategy. See you there.

---

*End of Part 1 Script*
