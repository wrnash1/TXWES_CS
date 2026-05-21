# Reading Guide: Module 12 - Cloud and Container Penetration Testing
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 12 - Cloud and Container Penetration Testing**! Modern enterprise infrastructure is increasingly built on cloud platforms (AWS, Azure, GCP) and containerized workloads (Docker, Kubernetes). Penetration testers must understand how cloud-specific misconfigurations, IAM policy weaknesses, and container escape techniques create exploitable vulnerabilities that differ significantly from traditional on-premises networks. This module maps to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**) and covers cloud and container security testing concepts the exam tests directly.

Cloud environments introduce unique authorization considerations — testing AWS, Azure, or GCP resources typically requires specific written permission from both the client and the cloud provider, as standard penetration testing authorization letters do not automatically cover cloud infrastructure.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud IAM Misconfiguration**: Identity and Access Management (IAM) policies in cloud environments define what actions users, roles, and services are permitted to perform. Misconfigurations — such as overly permissive policies, wildcard permissions (`"Action": "*"`), or publicly accessible S3 buckets — are among the most common cloud vulnerabilities. Attackers who gain access to an IAM key with excessive permissions can enumerate resources, exfiltrate data, escalate privileges to administrator roles, or pivot to other cloud services.

*   **Instance Metadata Service (IMDS) Attack**: Cloud virtual machines (EC2 on AWS, VMs on Azure) expose a metadata service at a link-local IP address (`169.254.169.254`) that provides instance configuration data including temporary IAM role credentials. If a web application running on the instance is vulnerable to Server-Side Request Forgery (SSRF), an attacker can use the SSRF vulnerability to query the metadata service and retrieve the instance's IAM credentials — then use those credentials to authenticate to the cloud API. This is one of the most critical cloud attack chains tested on PT0-002.

*   **S3 Bucket Misconfiguration**: Amazon S3 (Simple Storage Service) buckets store files in the cloud. Buckets configured with public read or write access expose their contents to any unauthenticated internet user. Sensitive data — backups, configuration files, credentials, customer PII — has frequently been exposed through publicly readable S3 buckets. Penetration testers check for misconfigured buckets using tools like `aws s3 ls s3://bucket-name` (if credentials exist) or by testing public access directly via HTTP.

*   **Container Escape**: A technique by which an attacker who has compromised a process inside a Docker container breaks out of the container's isolation boundary to access the underlying host system. Common escape techniques include: exploiting a privileged container (`--privileged` flag removes most isolation), mounting the host filesystem into the container, abusing the Docker socket (`/var/run/docker.sock`) if it is mounted inside the container, and exploiting kernel vulnerabilities. Container escape findings are high-severity because they demonstrate that container isolation cannot be trusted.

*   **Kubernetes (K8s) Attack Surface**: Kubernetes orchestrates containerized workloads and introduces its own attack surface. Key misconfigurations tested on PT0-002 include: unauthenticated access to the Kubernetes API server, overly permissive RBAC (Role-Based Access Control) policies, exposed `kubectl` proxy endpoints, and containers running as root. An attacker with API server access can enumerate pods, deploy malicious containers, or access secrets stored in the cluster.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002**. Cloud and container attacks are a growing exam focus — know cloud-specific attack patterns and how they differ from traditional network attacks.
*   **Cloud Authorization Requirement:** PT0-002 tests that cloud penetration testing requires explicit authorization from the cloud provider in addition to the client's authorization letter. AWS, Azure, and GCP all have penetration testing policies — some actions (DDoS simulation, certain scanning) require advance notice or are prohibited entirely. This is a common exam scenario question.
*   **SSRF → IMDS is a Critical Chain:** Server-Side Request Forgery combined with the Instance Metadata Service is PT0-002's canonical cloud attack chain. Recognize this pattern in scenario questions: web app with SSRF vulnerability + cloud VM = potential IAM credential theft.
*   **Shared Responsibility Model:** In cloud environments, security responsibility is split between the provider (physical infrastructure, hypervisor) and the customer (IAM policies, OS configuration, application security, data encryption). PT0-002 tests awareness that misconfigurations in customer-controlled areas are the tester's focus — the cloud provider's infrastructure is out of scope.
*   **Docker Socket Privilege Escalation:** If `/var/run/docker.sock` is mounted inside a container, the container can spawn new privileged containers with host filesystem access — effectively escaping to root on the host. This is one of the most common real-world container escape techniques and is tested on PT0-002.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Cloud Security" and "Docker" rooms provide browser-based guided practice with cloud misconfiguration enumeration, IAM exploitation concepts, and container security testing in a legal lab environment.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Cloud and Specialized Systems section for content covering cloud attack techniques, container security, and the shared responsibility model mapped to PT0-002 domain 3.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Cloud Security and Docker/container rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — all labs run in your browser without requiring a local cloud account or container environment. The cloud rooms cover IAM misconfiguration enumeration, S3 bucket analysis, and SSRF-to-metadata attack chains with guided walkthroughs.
*   **Required Video:** Watch the Cloud and Specialized Systems segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the cloud security content covering IAM misconfigurations, container escapes, and the shared responsibility model.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Enumerate AWS IAM permissions: `aws iam get-user` and `aws iam list-attached-user-policies`**: Using lab-provided credentials, you will determine what identity those credentials belong to and what permissions are attached — simulating the enumeration step an attacker performs after obtaining cloud credentials through phishing, SSRF, or an exposed key.
*   **Test for public S3 bucket access**: You will attempt to list and access objects in lab S3 buckets using both authenticated CLI access and unauthenticated HTTP requests — demonstrating the difference between proper bucket access controls and a misconfigured public bucket, and documenting the data exposure risk.
*   **Analyze Docker container isolation**: You will inspect a running lab container to identify misconfigurations (privileged flag, mounted Docker socket, root user) that would enable container escape — documenting which configuration changes would remediate each finding and what access an attacker would gain from exploiting them.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Cloud Security and Docker rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Cloud and Specialized Systems section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
