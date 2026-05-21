# Quiz: Module 11 - Cloud Security and Virtualization
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A company migrates its web application to a cloud provider. The cloud provider manages the physical servers, storage, networking, and the hypervisor. The company's IT team retains responsibility for the operating system, middleware, application code, and all data stored in the application. Which cloud service model describes this arrangement?
A) Software as a Service (SaaS)
B) Platform as a Service (PaaS)
C) Infrastructure as a Service (IaaS)
D) Function as a Service (FaaS)
*   **Correct Answer:** C) Infrastructure as a Service (IaaS)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* In SaaS, the provider manages everything including the application — the customer only configures and uses the software. The customer in this scenario manages the OS, middleware, and application code, which is far more responsibility than SaaS allows.
    *   *Why B is incorrect:* In PaaS, the provider manages the infrastructure and runtime environment — the customer is responsible only for the application code and data, not the OS. This scenario explicitly includes OS management as the customer's responsibility.
    *   *Why D is incorrect:* FaaS (serverless) is a subset of PaaS where the customer manages only individual functions — there is no OS, middleware, or application server for the customer to manage. The scenario describes OS-level responsibility.

---

---

**Question 2**
A security researcher discovers that a process running inside a virtual machine has exploited a vulnerability in the hypervisor to gain access to the host operating system and other guest VMs on the same physical server. Which attack type does this describe?
A) Container breakout
B) Side-channel attack
C) VM escape
D) Privilege escalation within the guest OS
*   **Correct Answer:** C) VM escape
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Container breakout involves escaping the isolation boundary of a container (such as Docker) to access the host OS or other containers — it targets container runtime vulnerabilities, not hypervisor vulnerabilities. Containers share the host kernel rather than running on a hypervisor.
    *   *Why B is incorrect:* A side-channel attack extracts information from a system by analyzing indirect physical signals such as power consumption, timing, or electromagnetic emissions — it does not involve breaking the hypervisor isolation boundary to gain active control.
    *   *Why D is incorrect:* Privilege escalation within a guest OS means a user gains elevated privileges (e.g., root or admin) inside the VM — this attack stays within the VM boundary and does not breach the hypervisor to reach the host or other VMs.

---

---

**Question 3**
An organization uses multiple SaaS applications, including cloud storage, CRM software, and a collaboration platform. The security team has discovered that employees are also using unsanctioned cloud applications (shadow IT) to share sensitive files. Which security control is specifically designed to provide visibility into cloud application usage and enforce data loss prevention policies across both sanctioned and unsanctioned cloud services?
A) Web Application Firewall (WAF)
B) Cloud Access Security Broker (CASB)
C) Security Information and Event Management (SIEM)
D) Network Access Control (NAC)
*   **Correct Answer:** B) Cloud Access Security Broker (CASB)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A WAF protects web applications from attacks like SQL injection and XSS by filtering HTTP/HTTPS traffic to a specific application — it does not provide visibility across an employee's use of multiple cloud services or enforce DLP policies for shadow IT.
    *   *Why C is incorrect:* A SIEM aggregates and correlates security logs and events from across the environment for threat detection and compliance reporting — it does not act as an enforcement point between users and cloud services or provide real-time cloud application access control.
    *   *Why D is incorrect:* NAC controls which devices are allowed to connect to the corporate network based on security posture — it enforces network admission policy but does not monitor or control cloud application usage once a device is connected.

---

**Question 4**
A DevOps team deploys a containerized application using a base Docker image pulled from a public registry. A security scan later reveals that the image contains several unpatched critical vulnerabilities in its included libraries. Which cloud/container security practice would have most directly prevented this risk?
A) Enable full disk encryption on the container host server.
B) Scan container images for known vulnerabilities before deployment and use minimal, vetted base images.
C) Run all containers with root privileges to ensure the application has sufficient permissions to function.
D) Store the container image in a private S3 bucket instead of a public registry.
*   **Correct Answer:** B) Scan container images for known vulnerabilities before deployment and use minimal, vetted base images.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full disk encryption on the host protects data at rest if the physical server is stolen or decommissioned — it does not inspect container image contents for software vulnerabilities or prevent vulnerable libraries from running inside containers.
    *   *Why C is incorrect:* Running containers as root is a security anti-pattern that increases risk — if a container breakout occurs, the attacker gains root access to the host. Containers should run as non-root users with the minimum required permissions.
    *   *Why D is incorrect:* Moving the image to a private S3 bucket controls who can access the image but does not remediate the vulnerabilities already present inside it — a private repository containing a vulnerable image is still a vulnerable image.

---

**Question 5**
An organization's cloud security team is reviewing their AWS environment and discovers that several S3 storage buckets containing customer PII are configured as publicly accessible, an IAM role has administrator-level permissions attached to a Lambda function that only needs read access to one database table, and a security group allows inbound SSH from 0.0.0.0/0. Which cloud security tool is designed to continuously identify these types of misconfigurations at scale?
A) Cloud Access Security Broker (CASB)
B) Intrusion Detection System (IDS)
C) Cloud Security Posture Management (CSPM)
D) Vulnerability scanner targeting network services
*   **Correct Answer:** C) Cloud Security Posture Management (CSPM)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A CASB focuses on monitoring and controlling user access to cloud applications and enforcing data loss prevention policies — it is not designed to audit the configuration of cloud infrastructure resources such as IAM roles, storage bucket permissions, and security groups.
    *   *Why B is incorrect:* An IDS monitors network traffic for signatures of known attacks and anomalous behavior — it detects active intrusions but does not assess the configuration state of cloud resources to identify policy violations or misconfigurations before they are exploited.
    *   *Why D is incorrect:* A network vulnerability scanner probes exposed services for known software vulnerabilities (open ports, unpatched services) — it does not evaluate cloud-native configuration settings such as IAM permission boundaries, bucket access policies, or security group rules.
