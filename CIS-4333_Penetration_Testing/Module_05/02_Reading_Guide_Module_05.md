# Reading Guide: Module 05 - Vulnerability Scanning – Nessus and OpenVAS
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 05 - Vulnerability Scanning – Nessus and OpenVAS**! This module covers automated vulnerability scanning — the systematic process of probing target systems with credentialed or uncredentialed scans to identify known vulnerabilities, misconfigurations, default credentials, and missing patches. Vulnerability scanning sits at the intersection of the **Information Gathering and Vulnerability Scanning** domain (22% of PT0-002) and feeds directly into the exploitation phase. Understanding how to configure scanners, interpret results, and distinguish real vulnerabilities from noise is a core professional skill and an exam requirement.

Nessus (by Tenable) and OpenVAS (open-source) are the two most widely used vulnerability scanners and are explicitly referenced in PT0-002 exam objectives.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Configuring Scanning Parameters**: The process of defining the scope, intensity, and credentials of a vulnerability scan before execution. Key parameters include: target IP range, scan policy (basic network scan vs. credentialed audit vs. web application scan), scan timing (to avoid disrupting production systems), and port range. Credentialed scans (authenticated scans) provide deeper visibility into patch levels and local configuration because the scanner logs into the target as a privileged user.

*   **False Positives vs. False Negatives**: A false positive occurs when a scanner reports a vulnerability that does not actually exist on the target — often due to version string matching without confirming exploitability or due to scanner logic errors. A false negative occurs when a real vulnerability exists but the scanner fails to detect it — common with heavily customized systems, non-standard ports, or vulnerabilities requiring manual confirmation. Both types affect the quality of the assessment and require analyst judgment to resolve.

*   **Analyzing Severity Levels (CVSS)**: The Common Vulnerability Scoring System (CVSS) assigns each vulnerability a score from 0.0 to 10.0 based on exploitability (attack vector, complexity, privileges required, user interaction) and impact (confidentiality, integrity, availability). PT0-002 tests the CVSS v3.1 severity ranges: Critical (9.0–10.0), High (7.0–8.9), Medium (4.0–6.9), Low (0.1–3.9). Testers prioritize remediation recommendations based on CVSS scores combined with environmental context (e.g., internet-facing vs. internal).

*   **Credentialed vs. Uncredentialed Scans**: An uncredentialed (unauthenticated) scan probes services from the outside, limited to what is visible over the network. A credentialed scan provides the scanner with valid login credentials, allowing it to examine patch levels, installed software, registry settings, and local file permissions — producing far fewer false negatives. PT0-002 expects you to know when each type is appropriate and that credentialed scans are more accurate for patch assessment.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Information Gathering and Vulnerability Scanning is **22% of PT0-002**. Vulnerability scanning questions focus on scanner selection, result interpretation, and CVSS scoring — not memorizing scanner menus.
*   **Nessus vs. OpenVAS:** Both are vulnerability scanners. Nessus is commercial (Tenable); OpenVAS is the open-source alternative (maintained by Greenbone). PT0-002 may ask you to identify which tool is appropriate for a given scenario — know that both perform credentialed and uncredentialed scans, produce CVSS-scored results, and support compliance auditing.
*   **Exam Trap — Vulnerability Scanner vs. Exploitation Tool:** PT0-002 distinguishes between tools that identify vulnerabilities (Nessus, OpenVAS, Nikto) and tools that exploit them (Metasploit, sqlmap). A scanner finding a vulnerability does not mean it has been exploited — they serve different phases.
*   **Exam Trap — False Positive Handling:** When a scanner flags a vulnerability, the professional response is to manually verify before reporting it as confirmed. PT0-002 tests that testers validate scanner findings rather than reporting everything uncritically.
*   **CVSS Components Tested:** Attack Vector (Network/Adjacent/Local/Physical), Attack Complexity (Low/High), Privileges Required, User Interaction, Scope, and the three impact metrics (C/I/A). Know that a CVSS 10.0 requires: network-accessible, low complexity, no privileges, no user interaction, scope change, full C/I/A impact.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Vulnerability Scanning" rooms provide hands-on practice with Nessus and OpenVAS in a guided lab environment, covering scan configuration, result interpretation, and CVSS scoring.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Vulnerability Scanning section for PT0-002 domain 2 content covering Nessus, OpenVAS, scan types, and CVSS.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Vulnerability Scanning rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). These rooms walk through Nessus and OpenVAS configuration, scan execution, and result analysis with hands-on exercises against vulnerable lab targets.
*   **Required Video:** Watch the Vulnerability Scanning segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). Use chapter markers to navigate to domain 2 content on scanner configuration, CVSS scoring, and result interpretation.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Set up target scanning profiles**: You will configure a vulnerability scan policy in OpenVAS or Nessus, defining the target IP range, scan intensity, port range, and whether to use credentials — and explain the expected difference in result quality between credentialed and uncredentialed modes.
*   **Filter scanning reports for critical CVE disclosures**: You will run a scan against a lab target, then filter results by CVSS severity to identify Critical and High findings, look up associated CVE numbers in the NVD, and document what each vulnerability would allow an attacker to do.
*   **Review scan performance indicators**: You will analyze scan logs and timing data to assess whether the scan completed successfully, identify any timed-out or unreachable targets, and evaluate the trade-off between scan speed and detection accuracy.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Vulnerability Scanning rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Vulnerability Scanning section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
