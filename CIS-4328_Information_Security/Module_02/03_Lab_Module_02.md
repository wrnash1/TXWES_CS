# Lab Activity — Module 02: Social Engineering Analysis Exercise

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | Authorized Educational Use Only

---

## Lab Overview

**Lab Title:** Social Engineering Attack Analysis and Countermeasure Design

**Estimated Completion Time:** 60–90 minutes

**Submission:** Upload completed deliverables to Canvas before the module deadline.

**Learning Objectives:**

- Identify and classify social engineering techniques from realistic scenario descriptions.
- Analyze the psychological principles exploited in each attack.
- Map defenses to the correct control categories and functions.
- Analyze email headers for spoofing indicators.
- Connect analysis to SY0-701 performance-based question reasoning.

---

## Background

This lab uses scenario-based analysis only. No tools, scripts, or real systems are used. All activities are analytical and document-based, consistent with the approach used on SY0-701 performance-based questions (PBQs).

You are a security analyst at Broadfield University, a mid-size private university with approximately 4,500 students and 800 faculty and staff. The university has recently experienced an increase in social engineering incidents and you have been asked to analyze six reported incidents, classify each attack, and recommend countermeasures.

---

## Part A — Social Engineering Incident Classification (36 points)

Analyze each incident below. For each one, provide:

1. The **specific social engineering technique** used (use the correct SY0-701 term)
2. The **psychological principle(s)** exploited (select from: Authority, Urgency, Fear, Familiarity, Social Proof, Reciprocity, Intimidation, Scarcity)
3. The **attack delivery channel** (in-person, email, phone, SMS, online)
4. The **CIA Triad property** most at risk if the attack succeeds
5. One **specific countermeasure** — with correct category and function labels — that would prevent or detect this attack

### Incident Reports

**Incident 2-A:**
A faculty member received a text message that appeared to come from the university's IT department. The message read: "SECURITY ALERT: Your university account will be locked in 2 hours due to suspicious activity. Verify your identity now: [link]." The link led to a page that looked identical to the university login portal but was hosted at broadfield-secure-login.com rather than broadfield.edu. The faculty member entered their credentials.

**Incident 2-B:**
An unknown individual dressed in a Facilities Services uniform carrying a toolbox walked through the main entrance of the Administration building and into the server room hallway. He told a passing administrative assistant that he was there to check the air conditioning in the server room. The assistant, not wanting to be unhelpful, used her badge to let him into the server room "just for a minute." The visitor spent 15 minutes alone in the server room before leaving.

**Incident 2-C:**
The Director of Finance received an email appearing to come from the University President's email address. The email stated that the university was closing a confidential real estate transaction that day and urgently needed a wire transfer of $287,000 to a title company. The email asked the Finance Director to process the transfer immediately and keep it confidential until the announcement. The Finance Director almost authorized the transfer before calling the President's office directly.

**Incident 2-D:**
A student worker in the IT help desk received a phone call from someone claiming to be "Dr. Martinez, Chair of the Biology Department." The caller said his computer was infected with a virus, that he needed his network password reset immediately, and that if IT didn't help him in the next ten minutes he would "be on the phone with the Provost." He provided the last four digits of his faculty ID when asked for verification. The student worker reset the password without completing the standard multi-step verification process.

**Incident 2-E:**
Ten USB drives were found in the campus parking lot near the library. Each drive was labeled "Student Scholarship Application Data — Fall 2024 — Do Not Delete." Three students plugged the drives into their laptops in the library. Two of the three laptops subsequently showed signs of malware infection.

**Incident 2-F:**
An attacker posted in a private Facebook group for Broadfield University students, claiming to be offering free premium streaming service subscriptions as part of a "student appreciation initiative." Students were directed to a website where they entered their university email address and created a password. Many students used the same password as their university account. The attacker used the collected credentials to attempt access to university systems.

### Part A Deliverable

Complete this table for each incident:

| Incident | Social Engineering Technique | Psychological Principle(s) | Delivery Channel | CIA Property at Risk | Countermeasure (Category / Function) |
|---|---|---|---|---|---|
| 2-A | | | | | |
| 2-B | | | | | |
| 2-C | | | | | |
| 2-D | | | | | |
| 2-E | | | | | |
| 2-F | | | | | |

**Part A is worth 36 points — 6 points per incident.**

Full credit requires all five fields correctly completed with appropriate terminology. Partial credit of 4 points if four of five fields are correct.

---

## Part B — Simulated Email Header Analysis (24 points)

Review the following simulated email header data from Incident 2-C. Answer the questions that follow. This is a simplified representation of real email header fields for educational purposes.

```text
From: president@broadfield.edu
Return-Path: <president@broadfield-univ.net>
Reply-To: finance-request@protonmail.com
Received: from mail.broadfield-univ.net (IP: 203.0.113.42)
X-Originating-IP: 203.0.113.42
DKIM-Signature: v=1; d=broadfield-univ.net; s=default
Authentication-Results: spf=pass (domain: broadfield-univ.net)
                        dkim=pass (domain: broadfield-univ.net)
                        dmarc=fail (p=reject; pct=100; domain: broadfield.edu)
Subject: CONFIDENTIAL - Urgent Wire Transfer Required Today
```

**Question B-1:** The DMARC result shows "fail." In the context of this email, explain specifically why the DMARC check failed even though both SPF and DKIM passed. (6 points)

**Question B-2:** The From header shows president at broadfield.edu but the Return-Path shows president at broadfield-univ.net. What is the significance of this discrepancy to an email security analyst? What attack technique does this represent? (6 points)

**Question B-3:** The DMARC policy shows "p=reject; pct=100." Given that DMARC failed, why did this email still reach the Finance Director's inbox? Describe one plausible technical explanation. (6 points)

**Question B-4:** The Reply-To address is a Protonmail address. Why would an attacker use a different Reply-To address from the From address in a phishing campaign, and how does this help the attacker? (6 points)

---

## Part C — Security Awareness Program Design (40 points)

The university president has asked you to design a basic security awareness program to address the social engineering incidents described in Part A. Your program design must address the following:

### Section C-1 — Training Topics (10 points)

List five specific training topics your program will cover, each with a one-sentence explanation of why that topic directly addresses one or more of the incidents from Part A.

### Section C-2 — Training Delivery Methods (10 points)

Describe three different training delivery methods you will use. For each method, explain:

- What format the training takes (video module, simulated phishing, in-person session, etc.)
- Which incident type(s) from Part A it primarily addresses
- How you will measure whether the training was effective

### Section C-3 — Phishing Simulation Plan (10 points)

Describe a phishing simulation plan for the university. Your plan must include:

- The simulation frequency (how often simulations will run)
- At least two different simulation scenarios you will use, written as brief descriptions of the lure content
- What happens when an employee clicks the test link — the immediate intervention
- How you will use simulation results to identify high-risk users who need additional training

### Section C-4 — Metrics and Success Criteria (10 points)

Define three measurable metrics you will use to assess the effectiveness of the security awareness program over time. For each metric, define what a successful outcome looks like at the end of one year, and explain how you will collect the data.

---

## Submission Instructions

Submit the following to Canvas before the module deadline:

- Part A: Completed classification table
- Part B: Written answers to all four questions
- Part C: Security awareness program design document with all four sections

Label each part clearly. Include your full name and student ID on all submitted documents.

---

## 100-Point Rubric

| Component | Points | Scoring Criteria |
|---|---|---|
| Part A — Incident Classification Table | 36 | 6 pts per incident. Full credit: all five fields correct with proper SY0-701 terminology. 4 pts: four of five fields correct. 2 pts: two to three fields correct. |
| Part B — Email Header Analysis | 24 | 6 pts per question. Full credit: technically accurate explanation demonstrating understanding of SPF/DKIM/DMARC mechanics. Partial credit for partially correct analysis. |
| Part C — Awareness Program Design | 40 | See section breakdown: C-1 = 10 pts, C-2 = 10 pts, C-3 = 10 pts, C-4 = 10 pts. Full credit requires complete, technically sound answers that directly address the scenarios. |
| **Total** | **100** | |

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Live Phishing Infrastructure Analysis

Using only publicly available tools and resources — no credential entry, no clicking suspicious links — analyze a recent real-world phishing campaign report.

1. Visit the APWG eCrime Trends reports page at <https://apwg.org/resources/apwg-reports/> and locate the most recent quarterly report. Identify: the top three most-impersonated brand categories, the predominant attack delivery channel for that quarter, and the percentage of phishing sites using HTTPS. Explain why HTTPS usage on phishing sites undermines the common user heuristic of "look for the padlock."
2. Using the Google Safe Browsing Transparency Report at <https://transparencyreport.google.com/safe-browsing/overview>, locate current statistics on sites detected for phishing. Record the weekly detection count and describe how this data is used operationally by URL sandboxing and reputation-filtering controls.
3. Select one of the phishing incidents from Broadfield University's Part A scenario (2-A through 2-F) and map it to a specific MITRE ATT&CK technique. Navigate to <https://attack.mitre.org/techniques/T1566/> (Phishing) and identify the correct sub-technique that best describes the attack. Record the technique ID, name, and at least two detection data sources listed in the ATT&CK entry.
4. Based on your research, write a one-paragraph threat briefing — suitable for a non-technical university VP — describing the current phishing threat landscape and recommending one immediate priority action.

### Challenge 2: DMARC Policy Deployment Gap Analysis

A regional hospital network has the following email authentication posture for its three domains: `hospital-main.org` has SPF and DKIM configured with DMARC at `p=none`; `hospital-billing.org` has SPF only, no DKIM, no DMARC; `hospital-staff.org` has no SPF, DKIM, or DMARC configured.

1. For each of the three domains, classify the current protection level as: (a) fully protected, (b) monitoring only, or (c) unprotected. Justify each classification using the SPF/DKIM/DMARC mechanics from Module 02 Section 5.
2. Construct the DMARC DNS TXT record string that `hospital-billing.org` should deploy as an initial monitoring-only policy. Then construct the record that represents the final enforcement target (p=reject; pct=100). Explain what `pct=100` means and why an organization might start with `pct=10` instead.
3. A threat actor sends a spoofed email from `billing@hospital-billing.org` to a hospital employee while the domain has only SPF configured (no DKIM, no DMARC). Walk through the receiving mail server's authentication check sequence and explain exactly why the spoofed email could still reach the inbox despite SPF being present.
4. Prioritize a remediation roadmap for all three domains — list which domain should be addressed first, second, and third — and justify each prioritization decision using the CIA Triad property most at risk for each domain based on its function (main communications, billing, staff).

### Reflection Questions

1. In Challenge 1, you identified that many phishing sites now use HTTPS. A user argues that HTTPS proves a site is safe because it means the connection is encrypted. Explain in your own words why this reasoning is dangerously incorrect, and describe what HTTPS actually guarantees versus what it does not guarantee about the legitimacy of a website.
2. In Challenge 2, you analyzed DMARC deployment across three domains. A security manager argues that deploying DMARC at `p=reject` immediately is better than a gradual rollout because "half-measures don't stop attacks." How would you respond to this argument? Identify at least one specific operational risk of jumping directly to `p=reject` without a monitoring phase, and explain how DMARC reporting helps mitigate that risk during the rollout.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 02 Lab

Proprietary and Confidential. Not for disclosure outside of authorized course use.
