# Reading Guide: Module 15 — Security Operations

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### Introduction

Welcome to Module 15 — Security Operations. This module covers the day-to-day tools, processes, and practices that security teams use to protect organizations in real time. Security Operations is Domain 4 of the SY0-701 exam and represents 28% of your total score — the single largest domain. Mastering this content is essential for both the exam and a career in security.

This reading guide supports both video lectures and your own independent study. Work through each section, answer the reflection questions in writing, and complete the vocabulary matching exercise before attempting the quiz.

---

### 1. High-Yield Glossary

Review these essential definitions carefully.

**Security Operations Center (SOC):** A dedicated team and facility responsible for continuous monitoring, detection, analysis, and response to cybersecurity incidents. SOCs operate 24/7 and are staffed in analyst tiers (Tier 1: triage, Tier 2: investigation, Tier 3: threat hunting and complex response).

**SIEM (Security Information and Event Management):** A platform that collects, normalizes, correlates, and analyzes security log data from across the enterprise. SIEMs generate alerts when correlation rules match event patterns. Key functions: log aggregation, normalization, correlation, alerting, reporting, and retention. Common products: Splunk, Microsoft Sentinel, IBM QRadar, Elastic SIEM.

**Log Normalization:** The process of converting log data from heterogeneous sources (Windows Event Log, Cisco syslog, Linux auth.log) into a consistent, comparable format so the SIEM can correlate across them.

**Correlation Rule:** A SIEM logic expression that links related events from multiple sources to identify attack patterns. Example: 500 failed logins across 50 accounts in 60 seconds triggers a credential stuffing alert.

**SOAR (Security Orchestration, Automation, and Response):** A platform that integrates security tools and executes automated playbooks in response to SIEM alerts. SOAR reduces analyst workload, speeds response times, and ensures consistent handling of routine incidents. Key distinction: SIEM detects and alerts; SOAR responds and automates.

**Playbook:** A documented, automated sequence of response actions triggered by a specific alert type. Example: phishing playbook extracts the email, queries threat intel, quarantines the message, and opens a ticket — automatically.

**Alert Fatigue:** A condition where SOC analysts become desensitized to alerts due to excessive false positives, leading to real threats being overlooked. Reducing false positive rates is a key SIEM tuning activity.

**Mean Time to Detect (MTTD):** The average elapsed time between when a security incident occurs and when the SOC detects it. Shorter MTTD indicates better detection capability.

**Mean Time to Respond (MTTR):** The average elapsed time between SOC detection of an incident and successful containment or resolution. Shorter MTTR reduces attacker dwell time and minimizes damage.

**Vulnerability Scanning:** An automated process that identifies known vulnerabilities in systems and applications by querying a vulnerability database and testing discovered services. Does not exploit vulnerabilities — that is penetration testing.

**Nessus:** The most widely deployed commercial vulnerability scanner, developed by Tenable. Uses plugins (over 170,000) to check for vulnerabilities. Supports credentialed and uncredentialed scans. Ratings use CVSS scores.

**Plugin (Nessus):** An individual vulnerability check within Nessus. Each plugin tests for a specific CVE or configuration weakness. Updated continuously by Tenable as new vulnerabilities are discovered.

**Credentialed Scan:** A vulnerability scan where the scanner authenticates to each target system with valid credentials, enabling inspection of installed software, patch levels, and local configuration. More accurate and thorough than uncredentialed scans.

**Uncredentialed Scan:** A vulnerability scan that connects from outside without authentication, simulating an external attacker's view. Identifies network-accessible vulnerabilities but cannot see local system state.

**CVSS (Common Vulnerability Scoring System):** A standardized 0–10 scoring system for vulnerability severity. Scores: Critical (9.0–10.0), High (7.0–8.9), Medium (4.0–6.9), Low (0.1–3.9), Informational (0.0).

**Patch Management:** The systematic process of identifying, acquiring, testing, and deploying software updates to remediate known vulnerabilities. The patch lifecycle: inventory → monitor → risk assess → test → deploy → verify → document.

**Compensating Control:** A security measure deployed when a standard control (such as patching) cannot be applied. Examples: network segmentation, IPS signatures, enhanced monitoring around an unpatched system.

**Configuration Baseline:** A documented, approved minimum-security configuration for a specific system type. Applied before deployment to ensure every system starts from a known-good, hardened state.

**CIS Benchmarks:** Freely available hardening guides published by the Center for Internet Security for hundreds of platforms (Windows, Linux, macOS, cloud, network devices). Widely considered the gold standard for configuration baselines.

**DISA STIGs:** Security Technical Implementation Guides published by the Defense Information Systems Agency. Mandatory for DoD and defense contractor systems. Extremely detailed and prescriptive.

**Configuration Drift:** Gradual divergence of a deployed system from its approved baseline due to unauthorized changes, software installations, or misconfigurations. Detected using integrity monitoring tools such as Tripwire, AIDE, or CIS-CAT.

**Change Control (Change Management):** The formal process for requesting, reviewing, approving, implementing, and documenting changes to IT systems. Prevents unauthorized changes and provides an audit trail. Key body: Change Advisory Board (CAB).

**Change Advisory Board (CAB):** A cross-functional group (IT, security, business units, management) that reviews and approves change requests before they are implemented in production.

**Emergency Change:** A change that bypasses normal CAB review due to urgency (e.g., active incident response, zero-day patch). Still requires post-implementation review and documentation.

**Rollback Plan:** A documented procedure for reverting a system to its pre-change state if a deployment causes problems. Required as part of every change request.

**Key Performance Indicator (KPI):** A metric that measures the performance of the security program (e.g., patch compliance rate, training completion rate).

**Key Risk Indicator (KRI):** A metric that measures current risk exposure (e.g., number of unpatched critical vulnerabilities, percentage of systems without endpoint detection).

---

### 2. Certification Exam Tips

**Domain weight:** Security Operations is Domain 4 of SY0-701 at 28% — the largest single domain. If you are short on study time, prioritize this module.

**SIEM vs. SOAR distinction:** This is a very commonly tested differentiator. SIEM = visibility and detection; SOAR = automation and response. If a question describes "automating response actions" or "executing playbooks," the answer is SOAR. If it describes "correlating logs and generating alerts," the answer is SIEM.

**Credentialed vs. uncredentialed scans:** Credentialed scans are always more accurate and thorough. When an exam question asks which scan type provides a more complete view of system vulnerabilities, the answer is credentialed.

**Patch management scenarios:** The Security+ exam frequently presents scenarios where a critical vulnerability is discovered and asks what you should do. The correct order is: assess severity → test in non-production → deploy with rollback plan → verify → document. Never skip the test phase in exam scenarios.

**MTTD and MTTR:** Know what these abbreviations stand for and know that lower values are always better. If a question asks which metric reflects how quickly attackers are detected, MTTD is the answer.

**Change control questions:** Look for the CAB role in approving changes, and note that emergency changes still require documentation even when they bypass normal approval.

**CIS Benchmarks vs. DISA STIGs:** CIS Benchmarks are for commercial organizations; DISA STIGs are for DoD/defense environments. Both are hardening baseline sources.

**Study resource:** Professor Messer's free Security+ SY0-701 course at [professormesser.com](https://www.professormesser.com/) includes detailed coverage of SIEM, vulnerability management, and patch management with exam scenario walkthroughs.

---

### 3. Conceptual Connections

Understanding how these topics connect helps you answer scenario questions.

**SOC → SIEM → SOAR chain:** The SOC uses a SIEM to see everything happening across the enterprise. The SIEM generates alerts when correlation rules fire. The SOAR platform receives those alerts and either automatically executes a playbook or routes the alert to a Tier 1 analyst.

**Vulnerability scanning feeds patch management:** Nessus scans identify what vulnerabilities exist. Patch management is how you fix them. The CVSS score from the scan determines patching priority. After patching, a follow-up scan verifies the fix. This is the vulnerability management lifecycle.

**Baselines prevent problems; change control manages change:** Deploying hardened systems from baselines reduces attack surface. Change control ensures that the baseline is not degraded over time by unauthorized changes. Integrity monitoring detects drift. These three together form configuration management.

**Metrics close the loop:** Without metrics, you cannot demonstrate that patching, scanning, and SOC operations are working. MTTD and MTTR measure detection and response effectiveness. Patch compliance rate measures the state of your vulnerability remediation program.

---

### 4. Reflection Questions

Answer each question in writing before reviewing the video or moving to the lab.

1. Your organization runs uncredentialed Nessus scans monthly. A new CTO asks why so many vulnerabilities are still appearing. What would you recommend changing about the scanning program, and why?

2. The SOC receives 2,000 alerts per day, and analysts are only investigating about 300 of them. What is this problem called, and what are two strategies to address it?

3. A developer deploys a configuration change directly to a production web server without going through the change management process. Two hours later, the site is unreachable. What change control failure occurred, and what controls could have prevented it?

4. Your CVSS scores show 15 critical vulnerabilities, 47 high vulnerabilities, and 230 medium vulnerabilities. You have limited patching resources this sprint. How do you prioritize, and what factors beyond CVSS score should you consider?

5. What is the difference between a KPI and a KRI? Give one concrete example of each from a security operations context.

---

### 5. Open Educational Resources

All resources below are free and openly licensed.

**NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide**
[https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
The foundational federal guide for incident response. Covers preparation, detection, containment, eradication, and recovery. Essential background for the entire SOC operations section.

**CIS Benchmarks (Free Downloads)**
[https://www.cisecurity.org/cis-benchmarks/](https://www.cisecurity.org/cis-benchmarks/)
Download CIS Benchmarks for Windows Server, Ubuntu, macOS, or any platform you use. Review a benchmark for a system type you are familiar with to understand what configuration baselines look like in practice.

**NIST National Vulnerability Database (NVD)**
[https://nvd.nist.gov/](https://nvd.nist.gov/)
The official source for CVE information, CVSS scores, and patch references. Practice searching for a recent critical CVE to understand how vulnerability data is structured and used.

**Professor Messer — Security+ SY0-701 Course (Free)**
[https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-training-course/](https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-training-course/)
Free full video course with exam objective alignment. Focus on the Domain 4 — Security Operations sections for this module.

**Tenable Nessus Essentials (Free for students)**
[https://www.tenable.com/products/nessus/nessus-essentials](https://www.tenable.com/products/nessus/nessus-essentials)
Nessus Essentials is free for students and allows scanning up to 16 IP addresses. Use this in the lab to gain hands-on experience before the real exam.

---

### 6. Module 15 Checklist

Before moving on, confirm you can do each of the following without referring to notes.

- [ ] Describe the three SOC analyst tiers and their responsibilities
- [ ] Explain what SIEM log normalization and correlation accomplish
- [ ] Distinguish SIEM from SOAR with a concrete example
- [ ] Explain the difference between credentialed and uncredentialed Nessus scans
- [ ] List the seven steps of the patch management lifecycle
- [ ] Describe what a configuration baseline is and name two sources of baseline standards
- [ ] Explain what configuration drift is and how it is detected
- [ ] Describe the role of the CAB in change management
- [ ] Define MTTD and MTTR and explain why each should be minimized
- [ ] Distinguish KPIs from KRIs with examples from security operations

---

End of Reading Guide — Module 15
