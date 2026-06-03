# Lab: Module 13 — Penetration Test Report Writing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

- **Duration:** 3 hours
- **Format:** Document-based exercise — no live systems
- **Materials:** Fictional assessment data package (distributed by instructor), CVSS calculator access, report template
- **Deliverable:** Complete professional penetration test report (fictional client)

This lab develops the professional writing and analytical skills required to produce a production-quality penetration test report. All findings, systems, and client data are entirely fictional.

---

## Lab Objectives

By completing this lab, students will:

1. Structure a complete penetration test report following professional standards.
2. Write an executive summary for a non-technical audience.
3. Calculate CVSS 3.1 scores for five finding types.
4. Write complete technical findings with all required components.
5. Develop a prioritized remediation roadmap.
6. Review a draft report and provide constructive quality feedback.

---

## Fictional Assessment Data

The following data represents findings from a fictional penetration test of Hartwell Manufacturing's corporate network. Students build a complete report from this raw data.

### Client Information

- **Client:** Hartwell Manufacturing Inc. (fictional)
- **Assessment Type:** External and Internal Network Penetration Test
- **Testing Period:** Fictional 5-day assessment
- **Scope:** External perimeter, DMZ, internal corporate network (10.10.0.0/16)
- **Authorized by:** Victoria Chen, CISO (fictional)

### Raw Finding Data

**Finding Data 1:**

During external reconnaissance, the subdomain `vpn-legacy.hartwell-mfg.local` was found using certificate transparency logs. The host runs Cisco ASA VPN with firmware version 9.8.1, which is vulnerable to CVE-2018-0101 (heap overflow, CVSS 10.0). Exploitation provides unauthenticated remote code execution on the firewall. Confirmed by checking the response headers and firmware version string. No patch has been applied.

**Finding Data 2:**

The company's main website (www.hartwell-mfg.local) has a login form at /admin that is vulnerable to SQL injection via the `username` parameter. Testing with `' OR '1'='1` returns all user records. The database contains 847 records including MD5-hashed passwords and email addresses. Partial output captured. MD5 hashing is used — rainbow tables can crack most passwords within minutes.

**Finding Data 3:**

Internal network scanning discovered that 14 Windows workstations in the engineering subnet (10.10.15.0/24) are running Windows 7 with no patches applied. These systems are vulnerable to MS17-010 (EternalBlue) and were successfully exploited, yielding SYSTEM-level access on all 14 machines. The engineering subnet has access to the manufacturing floor OT network (10.10.20.0/24).

**Finding Data 4:**

The HR file server (\\hrserver01) has an open SMB share called `HR_Archive` that is readable by all authenticated domain users. The share contains Excel files with employee salary data, SSNs, and performance reviews dating back to 2019. Approximately 312 employees' records are exposed.

**Finding Data 5:**

The primary domain controller (DC01, 10.10.1.10) has the LDAP service bound on port 389 without TLS (LDAPS on 636 is not configured). Domain credentials are transmitted in cleartext. Responder was used to capture the domain administrator's NTLM hash from the testing machine's network position. The hash was cracked in 4 minutes using Hashcat against rockyou.txt.

---

## Part 1: CVSS Scoring Exercise (30 minutes)

### Step 1.1: Score Each Finding

Use the CVSS 3.1 calculator at https://www.first.org/cvss/calculator/3.1 to calculate the Base Score for each of the five findings.

For each finding, document:

- Attack Vector
- Attack Complexity
- Privileges Required
- User Interaction
- Scope
- Confidentiality Impact
- Integrity Impact
- Availability Impact
- Base Score
- Qualitative Rating (Critical/High/Medium/Low)
- Complete vector string

**Lab Report Item 1:** Submit a completed CVSS scoring table for all five findings.

### Step 1.2: Environmental Adjustment

For Finding 3 (EternalBlue on engineering workstations), consider that the engineering network connects to the OT/manufacturing floor. Apply environmental metric adjustments to reflect the increased business impact. Document your adjustments and the resulting environmental score.

**Lab Report Item 2:** Explain your environmental metric choices in 150 words. How does the OT network adjacency change the effective risk compared to a purely corporate IT environment?

---

## Part 2: Writing Technical Findings (75 minutes)

### Step 2.1: Write Three Complete Findings

Choose three of the five raw findings and write each as a complete professional finding. Use the standard structure:

**Finding Title:**

**Risk Rating:**

**CVSS Score:**

**Description:** (3–5 sentences)

**Evidence:** (Describe the evidence that would be captured — what screenshot would show, what command output would include)

**Impact:** (Business impact, not just technical)

**Affected Assets:**

**Remediation (Immediate — 0 to 30 days):**

**Remediation (Long-term — 30 to 90+ days):**

**References:** (CVE identifier, vendor advisory, or relevant standard)

**Lab Report Item 3:** Submit all three complete findings.

### Step 2.2: Executive Translation Exercise

For each of your three findings, write a 2-sentence executive version: the first sentence states what is vulnerable and what an attacker can do; the second sentence states what must happen.

Example: "The company's external VPN firewall has an unpatched critical vulnerability that allows attackers to take full control of the device remotely without a password. This system must be patched or replaced within 48 hours to prevent network perimeter compromise."

**Lab Report Item 4:** Submit all three executive translations.

---

## Part 3: Remediation Roadmap (30 minutes)

Create a remediation roadmap that covers all five findings. The roadmap should be a table suitable for inclusion in the report as an appendix.

### Step 3.1: Build the Roadmap Table

| Finding | Risk Rating | CVSS | Responsible Team | Immediate Action (0–30 days) | Long-Term Action (30–90 days) | Status |
|---------|-------------|------|-----------------|------------------------------|-------------------------------|--------|
| Finding 1 | | | | | | Open |
| Finding 2 | | | | | | Open |
| Finding 3 | | | | | | Open |
| Finding 4 | | | | | | Open |
| Finding 5 | | | | | | Open |

**Lab Report Item 5:** Submit the completed remediation roadmap table.

### Step 3.2: Prioritization Justification

**Lab Report Item 6:** In 200 words, justify the order in which you would prioritize remediation. Which finding should the client address first, and why? Consider both severity and exploitability. If two findings could be addressed simultaneously to reduce total effort, note that.

---

## Part 4: Executive Summary (30 minutes)

Write a complete executive summary for the Hartwell Manufacturing penetration test. Requirements:

- Maximum 400 words
- Audience: CISO and executive leadership, limited technical background assumed
- Structure: Scope/objective (2–3 sentences) → Overall posture (2–3 sentences) → Key findings (5 bullet points, plain language) → Priority actions (3–5 bullets with timelines)
- No CVE numbers or technical acronyms without plain-language explanation
- No individual employee names
- Convey urgency for Critical findings without alarmist language

**Lab Report Item 7:** Submit your complete executive summary.

---

## Part 5: Peer Review (15 minutes)

Exchange your three findings (Lab Report Item 3) with a classmate. Review their findings against the following quality checklist and provide written feedback:

Quality Checklist:

- [ ] Title is specific and descriptive
- [ ] Description clearly explains the vulnerability mechanism
- [ ] Evidence description is specific and reproducible
- [ ] Impact is stated in business terms
- [ ] Affected assets are specifically identified
- [ ] Immediate remediation is actionable within 30 days
- [ ] Long-term remediation addresses the root cause
- [ ] References include a CVE or standard

**Lab Report Item 8:** Submit your completed quality checklist for your classmate's findings with 2–3 sentences of constructive written feedback for each finding.

---

## Lab Report Submission

Your lab report must include:

- Lab Report Items 1–8
- All CVSS scoring tables
- Three complete technical findings
- Three executive translations
- Remediation roadmap
- Executive summary
- Peer review checklist

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| CVSS scoring and environmental adjustment (Items 1–2) | 20 |
| Three technical findings (Item 3) | 30 |
| Executive translations (Item 4) | 10 |
| Remediation roadmap and justification (Items 5–6) | 20 |
| Executive summary (Item 7) | 15 |
| Peer review (Item 8) | 5 |
| **Total** | **100** |
