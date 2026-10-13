# Lab Activity: Module 15 — Security Operations

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### Overview

This lab has two parts. Part A gives you hands-on experience with Nessus Essentials, the free student edition of the industry-standard vulnerability scanner. Part B walks you through evaluating a simulated patch prioritization scenario and drafting a SOC metrics report.

Both parts reinforce the Security Operations domain (Domain 4, 28% of SY0-701) through direct practice with tools and workflows used in real SOC environments.

**Estimated time:** 90–120 minutes

**Prerequisites:** A Windows or Linux VM, or your local machine. Internet access to download Nessus Essentials.

---

### Part A — Vulnerability Scanning with Nessus Essentials

#### Step 1: Install Nessus Essentials

1. Navigate to [https://www.tenable.com/products/nessus/nessus-essentials](https://www.tenable.com/products/nessus/nessus-essentials) and click "Download Nessus Essentials."
2. Register with your student email to receive a free activation code.
3. Download the installer appropriate for your operating system (Windows .msi or Linux .deb/.rpm).
4. Run the installer. Nessus runs as a local web service; after installation, open a browser and navigate to `https://localhost:8834`.
5. Accept the self-signed certificate warning and complete the setup wizard using your activation code.
6. Allow Nessus to download and compile its plugins — this may take 15–30 minutes on first run.

#### Step 2: Configure a Basic Network Scan

1. In the Nessus interface, click **New Scan** in the top-right corner.
2. Select **Basic Network Scan** from the scan templates.
3. Give the scan a name: `Module 15 Lab Scan`.
4. In the **Targets** field, enter `127.0.0.1` (your local machine) or the IP address of a VM you own.

> **Important:** Only scan systems you own or have explicit written permission to scan. Scanning systems without authorization is illegal under the Computer Fraud and Abuse Act and similar laws worldwide.

1. Leave all other settings at their defaults.
2. Click **Save**, then click the play button to launch the scan.
3. Wait for the scan to complete (typically 5–15 minutes for a single host).

#### Step 3: Review Scan Results

1. When the scan completes, click on the scan name to open the results.
2. Review the **Vulnerabilities** tab. Note the breakdown by severity: Critical, High, Medium, Low, Info.
3. Click on any Critical or High finding to expand the details. For each finding, record:
   - The plugin name and ID
   - The CVE number (if listed)
   - The CVSS score
   - The solution recommended by Nessus

#### Step 4: Run a Second Scan with Credentials

1. Create a second scan (New Scan → Basic Network Scan) targeting the same host.
2. Name it `Module 15 Lab Scan — Credentialed`.
3. Under the **Credentials** tab, add your local system credentials:
   - For Windows: select **Windows** credential type and enter a local administrator username and password.
   - For Linux: select **SSH** and enter a username and password or upload your SSH key.
4. Save and run the scan.
5. When complete, compare the number of findings in the credentialed scan versus the uncredentialed scan from Step 3.

#### Lab Questions — Part A

Answer these questions in your submission document.

1. How many total vulnerabilities did the uncredentialed scan find? How many did the credentialed scan find? What explains the difference?

2. Select one Critical or High finding from either scan. In your own words, describe what the vulnerability is, what an attacker could do if they exploited it, and what remediation is recommended.

3. If you found a Critical CVSS 9.8 vulnerability on a production web server that is internet-facing, what would be your recommended remediation timeline, and what compensating control would you deploy while waiting for the patch window?

---

### Part B — Patch Prioritization and SOC Metrics

#### Scenario

You are a Tier 2 SOC analyst at a mid-size financial services company. Your vulnerability scanner has completed its weekly scan and produced the following findings summary for your environment of 340 systems:

| Severity | Count | Notes |
|----------|-------|-------|
| Critical | 8 | All 8 are on internet-facing web servers; 3 CVEs have published exploits |
| High | 34 | Mix of internal servers and workstations |
| Medium | 187 | Largely Windows workstations; many require scheduled reboots |
| Low | 412 | Informational / configuration observations |

Your organization's patch SLA policy:

- Critical: remediate within 72 hours
- High: remediate within 14 days
- Medium: remediate within 30 days
- Low: remediate within 90 days

This week's SOC performance data:

| Metric | This Week | Last Week |
|--------|-----------|-----------|
| Total alerts generated | 1,847 | 1,923 |
| Alerts investigated | 412 | 389 |
| True positives (confirmed incidents) | 23 | 19 |
| False positives | 389 | 370 |
| Mean Time to Detect (MTTD) | 4.2 hours | 5.1 hours |
| Mean Time to Respond (MTTR) | 6.8 hours | 8.3 hours |

#### Task 1: Patch Prioritization Memo

Write a short memo (150–200 words) addressed to your IT operations manager. The memo must:

- Identify which vulnerabilities require immediate action and explain why
- Recommend a specific remediation order and timeline
- Propose at least one compensating control for critical findings while patches are being tested
- Reference the organization's patch SLA policy

#### Task 2: SOC Metrics Analysis

Using the weekly metrics table above, answer the following questions.

1. Calculate the false positive rate for this week. Show your calculation. Is this rate acceptable? What threshold would you recommend?

2. MTTD improved from 5.1 hours to 4.2 hours. Is this a positive or negative trend? What specific SIEM tuning action could further reduce MTTD?

3. MTTR improved from 8.3 hours to 6.8 hours. What SOC capability — SIEM or SOAR — would be most effective at continuing to drive MTTR downward, and why?

4. Only 412 of 1,847 alerts were investigated. What is this problem called? Describe two strategies a SOC manager could implement to address it without hiring additional analysts.

---

### Submission Requirements

Submit a single document containing:

- **Part A:** Screenshots of your Nessus scan results (uncredentialed and credentialed), and written answers to the three Part A questions.
- **Part B:** Your completed patch prioritization memo and written answers to the four metrics analysis questions.

Format your submission with clear section headers. Label each answer with its question number.

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| Nessus scan completed and screenshots provided | 20 |
| Uncredentialed vs. credentialed comparison explained correctly | 15 |
| Critical/High vulnerability analysis (Part A Q2) | 15 |
| Patch prioritization memo — accurate, complete, professional | 20 |
| SOC metrics analysis — correct calculations and sound reasoning | 30 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: SIEM Correlation Rule Design and Alert Triage

Using the scenario data from Part B, design three new SIEM correlation rules to address attack patterns not currently covered by the existing rule set. For each rule, specify:

1. A descriptive rule name and the attack technique it detects (reference the MITRE ATT&CK technique ID and name).
2. The specific log sources and event fields the rule monitors (e.g., Windows Event ID 4625, source IP, account name, time window).
3. The threshold conditions that trigger the alert (e.g., "more than 10 events matching condition X within 5 minutes from the same source IP").
4. The severity level you would assign (Critical/High/Medium/Low) and the justification for that level.
5. A brief SOAR playbook outline (3–5 automated steps) that should execute when this rule fires.

Then: select one of your three rules and write a full analyst investigation checklist — the step-by-step questions a Tier 1 analyst should answer to determine whether the alert is a true positive or false positive, and the escalation criteria for routing to Tier 2.

### Challenge 2: Vulnerability Management Program Gap Analysis

A company's IT security team has been running Nessus uncredentialed scans monthly against their 180-server environment. The most recent scan found 12 critical, 38 high, and 194 medium vulnerabilities. The CISO states that last quarter the numbers were identical — no improvement. Investigation reveals: patches are being applied but not re-scanned for verification; the patch team prioritizes by age of finding rather than CVSS score; three servers are excluded from scanning because "they are too old to scan safely"; and there is no formal patch SLA documented.

1. Identify four specific program failures and classify each as a people, process, or technology gap.
2. Design a corrected patch management workflow with at least seven steps. For each step, specify who is responsible (role), what artifact is produced, and what tool supports the step.
3. Write a one-page KPI/KRI dashboard proposal for the CISO that includes: five metrics to track (with definitions and measurement frequency), two threshold values that would trigger an executive escalation, and one metric that directly measures whether patching is actually reducing vulnerability exposure over time.

### Reflection Questions

1. A SOC manager argues that reducing false positives is more important than reducing false negatives, because alert fatigue causes analysts to miss real incidents. A peer argues the opposite — that missing real incidents (false negatives) is always worse than extra work from false positives. Evaluate both positions and describe how you would balance this trade-off when tuning SIEM correlation rules.
2. An organization's MTTD has improved from 72 hours to 4 hours over the past year, but MTTR remains at 48 hours. What does this pattern tell you about the organization's security operations maturity, and which specific capability investments would most effectively drive MTTR down?

---

End of Lab — Module 15
