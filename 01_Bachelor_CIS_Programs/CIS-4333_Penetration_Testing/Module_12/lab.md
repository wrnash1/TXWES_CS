# Lab: Module 12 — Physical Security Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Authorization Statement

This lab is a case analysis and methodology exercise. No physical trespass, lock picking, badge cloning, or access control bypass is performed on any real facility. Students analyze documented physical penetration test scenarios, develop assessment methodology documents, and produce professional findings reports.

Physical security testing techniques described in this lab are taught for assessment and defensive purposes. Applying any physical entry technique against any facility, lock, or access control system without explicit written authorization from the property owner constitutes criminal trespass and potentially breaking and entering. Any student found applying these techniques without authorization will receive a failing grade and be referred for criminal prosecution referral.

---

## Lab Overview

- **Duration:** 3 hours
- **Format:** Case analysis, methodology development, and report writing
- **Materials:** Three fictional physical pen test scenario briefs (distributed by instructor), blank finding templates, CVSS calculator access
- **Deliverable:** Physical Security Assessment Report (fictional)

---

## Lab Objectives

By completing this lab, students will:

1. Analyze a physical penetration test scenario and identify all vulnerabilities present.
2. Apply the concentric rings model to map findings to security layers.
3. Develop a physical security assessment methodology document for a fictional client.
4. Write professional physical security findings with appropriate risk ratings.
5. Produce an executive summary suitable for a non-technical audience.
6. Develop prioritized remediation recommendations with implementation timelines.

---

## Part 1: Scenario Analysis — Concentric Rings Mapping (45 minutes)

### Scenario Brief: Meridian Financial Group

Meridian Financial Group operates a three-story office building with 200 employees. A physical penetration test was conducted over two days. The following observations were made:

**Observation 1:** The parking lot perimeter fence has a 4-foot gap near the loading dock that allows access to the building's rear without crossing the main gate.

**Observation 2:** The main entrance uses HID Prox 125 kHz cards. The tester used a Proxmark3 to read an employee's card from 3 inches while standing in line at the coffee kiosk in the lobby. A cloned card was created and used to access the building successfully the following morning.

**Observation 3:** The second-floor server room door uses a keypad with a 4-digit PIN. The keypad buttons show visible wear on 1, 4, 7, and 0 — suggesting these four digits comprise the PIN. After 3 attempts, the tester discovered the PIN: 1-0-4-7.

**Observation 4:** During the lunch period, the tester walked through the open office floor and observed two unlocked workstations displaying email, three documents left face-up on desks including one labeled "Q3 Financial Projections — Confidential," and one whiteboard visible from the aisle showing a network diagram including the IP addresses of the domain controllers.

**Observation 5:** The company's dumpsters (in the publicly accessible loading dock area) contained 14 unshredded documents, including a printed employee directory, a vendor invoice for Cisco ISE (identity management software), and a partial network design document.

**Observation 6:** The tester attempted tailgating through the main entrance 5 times during business hours. 4 of 5 attempts succeeded without challenge. The one challenge came from a security guard, who accepted the tester's fabricated explanation ("I'm here for a 10 o'clock meeting with Sarah in HR") without verification.

### Step 1.1: Concentric Rings Mapping

Create a table mapping each observation to its security layer:

| Observation | Security Layer | Vulnerability Category |
|-------------|---------------|----------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |

**Lab Report Item 1:** Complete the mapping table. For each observation, provide one sentence explaining why you assigned it to that layer.

### Step 1.2: Attack Chain Analysis

Identify which combination of observations creates the highest-risk attack chain — the sequence of actions that would give an attacker the greatest access to sensitive data.

**Lab Report Item 2:** Write a narrative (200 words maximum) describing the optimal attack chain. Start from the parking lot and end at the most sensitive asset accessible. Number each step.

---

## Part 2: Risk Rating and CVSS Scoring (45 minutes)

### Step 2.1: Assign Risk Ratings

For each of the six observations, assign:

- A qualitative risk rating: Critical, High, Medium, or Low
- A CVSS 3.1 Base Score using the calculator at first.org/cvss/calculator/3.1

Note: For physical vulnerabilities, use AV:P (Attack Vector: Physical) when direct physical presence is required. When the finding enables network access (e.g., Observation 2 enables building access leading to network jack), use the attack vector applicable to the final impact.

**Lab Report Item 3:** Complete this risk rating table:

| Observation | Risk Rating | CVSS Score | Key CVSS Metrics |
|-------------|-------------|------------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

### Step 2.2: Justify Ratings

**Lab Report Item 4:** Choose the two findings you rated highest. For each, write a 100-word justification of your rating. Address: What is the realistic worst-case scenario if this vulnerability is exploited? Why is this rating appropriate relative to the other findings?

---

## Part 3: Methodology Document Development (30 minutes)

Develop a physical security assessment methodology document for a fictional client (you may use Meridian Financial Group or a different fictional company). The methodology document is a pre-assessment planning artifact that the client reviews and approves.

### Step 3.1: Scope Definition

Write a physical assessment scope section that includes:

- Description of facility to be tested (fictional)
- Specific authorized techniques (list at least 6)
- Explicitly excluded techniques (at least 3)
- Geographic boundaries (describe authorized areas)
- Time windows for testing (business hours vs. after-hours)

### Step 3.2: Get-Out-of-Jail Letter Template

Draft a get-out-of-jail letter that a fictional client executive would sign. Include all required elements:

- Client organization name and letterhead placeholder
- Tester name(s) and firm
- Authorization statement
- Specific authorized activities
- Testing dates
- Emergency contact information
- Executive signature line

**Lab Report Item 5:** Submit your complete scope section and get-out-of-jail letter template.

---

## Part 4: Professional Findings Writing (45 minutes)

### Step 4.1: Write Three Full Findings

Choose three of the six observations and write each as a complete penetration test finding using this format:

**Finding Title:**

**Risk Rating:** [Critical/High/Medium/Low]

**CVSS Score:** [X.X]

**Summary:** [1-2 sentences]

**Technical Description:** [3-5 sentences explaining the vulnerability, how it was identified, and what was possible as a result]

**Evidence:** [Description of evidence collected — no real photos in this lab, describe what would be photographed/documented]

**Impact:** [What can an attacker accomplish using this vulnerability?]

**Affected Assets:** [List specific assets]

**Remediation (Short-term, 0-30 days):** [Immediate mitigation step]

**Remediation (Long-term, 30-90 days):** [Permanent fix]

**References:** [Relevant standard or framework reference]

**Lab Report Item 6:** Submit all three complete findings.

---

## Part 5: Executive Summary (15 minutes)

Write an executive summary for the Meridian Financial Group physical penetration test. The executive summary is for a non-technical audience (CEO, board members).

Requirements:

- 250-350 words
- No technical jargon without plain-language explanation
- Include: overall assessment of physical security posture, top 3 findings, and 3 prioritized action items
- Convey urgency without causing panic
- Do not name individual employees who failed security tests

**Lab Report Item 7:** Submit your executive summary.

---

## Lab Report Submission

Your lab report must include:

- Lab Report Items 1–7
- All tables completed
- Narrative attack chain analysis
- Complete methodology document with scope and letter template
- Three professional findings
- Executive summary

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Concentric rings mapping and attack chain analysis (Items 1–2) | 20 |
| Risk ratings and CVSS justification (Items 3–4) | 25 |
| Methodology document (Item 5) | 20 |
| Three professional findings (Item 6) | 25 |
| Executive summary (Item 7) | 10 |
| **Total** | **100** |
