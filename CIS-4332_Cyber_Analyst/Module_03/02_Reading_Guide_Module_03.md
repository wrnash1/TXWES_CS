# Reading Guide: Module 03 - Vulnerability Management – Scanning and Prioritization
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 03 - Vulnerability Management – Scanning and Prioritization**! This module covers how organizations systematically discover, assess, and prioritize vulnerabilities across their infrastructure. You will learn how vulnerability scanners work, the difference between credentialed and non-credentialed scans, and how to use CVSS scores alongside business context to prioritize remediation. These topics are tested primarily under **Domain 2: Vulnerability Management (30%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn how to configure scan targets, interpret scan output, and communicate findings to remediation teams. Complete the glossary review and study checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Network Vulnerability Scanners**: Automated tools (e.g., Nessus, OpenVAS, Qualys) that probe hosts and services to identify known vulnerabilities, misconfigurations, and missing patches. Scanners compare discovered software versions and configurations against vulnerability databases such as the NVD and vendor advisories. CySA+ exam questions frequently ask about scanner output interpretation and scan type selection.
*   **Credentialed vs. Non-Credentialed Scans**: A credentialed scan provides the scanner with valid login credentials so it can log into target systems and inspect local registry entries, installed software, and patch levels directly — producing more accurate, fewer false-positive results. A non-credentialed scan can only probe open network ports and service banners without logging in, which may miss locally installed vulnerabilities. The exam commonly tests which scan type produces more accurate patch-level data.
*   **Nmap Vulnerability Scripts (NSE)**: Nmap's scripting engine (NSE) allows analysts to run Lua-based scripts against scan targets to perform tasks beyond port discovery, including vulnerability detection, service enumeration, and exploit checks. Scripts such as `http-shellshock` or `smb-vuln-ms17-010` extend Nmap into lightweight vulnerability scanning. CySA+ may present NSE in questions about infrastructure enumeration techniques.

---

### 2. Certification Exam Tips
*   **Focus Area – Domain 2 (30% of exam):** Vulnerability Management is the second-largest domain. Expect scenario questions asking you to choose between scan types, interpret CVSS scores, and select appropriate remediation priority. Know the five phases: Identify, Analyze, Prioritize, Remediate, Verify.
*   **Scenario Trap – Credentialed vs. Non-Credentialed:** The exam regularly presents a scenario where a scan shows far fewer findings than expected or shows only network-layer issues. The correct diagnosis is almost always that a non-credentialed scan was run instead of a credentialed one. Always associate credentialed scans with higher accuracy and more internal findings.
*   **Scan Impact on Production:** CySA+ scenario questions sometimes describe a production outage that occurred during a scan. Aggressive scan timing settings (e.g., Nmap `-T5`) can overwhelm network devices. Analysts must balance scan thoroughness with operational risk, especially on legacy or fragile systems.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist includes dedicated segments on vulnerability scanning tools and CVSS interpretation aligned to CS0-003: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource is structured around the official exam objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Vulnerability Scanning and Prioritization** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). CompTIA's official reference details the scanning concepts, CVSS metric groups, and remediation strategies tested on the exam.
*   **Required Video:** Watch the video lecture on **Vulnerability Management – Scanning and Prioritization** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist provides walkthroughs of scan output analysis and remediation prioritization scenarios.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a basic vulnerability scan target list**: Define a target IP range in your scanner configuration and select scan policy settings, comparing the differences between a full credentialed scan policy and a network-discovery-only policy.
*   **Perform a mock Nmap NSE script scan**: Run `nmap --script vuln -p 445 <target>` against a lab host and examine the output for detected vulnerabilities, noting the script name, CVE reference, and severity indicated in the results.
*   **Analyze scanning speed impacts on network bandwidth**: Compare scan results from `nmap -T1` (slow, stealthy) vs. `nmap -T4` (aggressive) against the same target and document the difference in completion time and detection rate to understand the operational tradeoff.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Vulnerability Scanning and Prioritization** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Vulnerability Management – Scanning and Prioritization** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the Nmap and scanner commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
