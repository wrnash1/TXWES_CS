# Lab: Module 13 — Risk Management for Security+

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

**Title:** Risk Register and Risk Analysis Workshop

**Duration:** Approximately 90 minutes

**Environment:** No special software required — Microsoft Excel/Google Sheets recommended; paper works also

**Skill Level:** Intermediate — requires completion of Module 13 video lectures and Reading Guide

---

## Objectives

Upon completing this lab, you will be able to:

1. Perform a quantitative risk analysis including AV, EF, SLE, ARO, and ALE calculations
2. Conduct a cost-benefit analysis to justify a proposed security control investment
3. Create a qualitative risk matrix and apply it to multiple identified risks
4. Construct a formatted risk register entry for at least three risks
5. Derive BIA metrics (MTD, RTO, RPO) from organizational requirements
6. Classify identified security controls by function and type

---

## Scenario: Cascade Regional Medical Center

**Organization Overview:** Cascade Regional Medical Center is a 350-bed regional hospital with 2,000 employees. They operate a mix of on-premises and cloud-hosted systems including:

- Electronic Health Record (EHR) system — hosted on-premises; stores PHI for 180,000 patients
- Medical billing system — on-premises; processes insurance claims and stores financial data
- Hospital website and patient portal — cloud-hosted (AWS); allows appointment scheduling and test result access
- Clinical imaging systems (PACS — Picture Archiving and Communication System) — on-premises; stores 15 TB of radiology images
- Building management system (BMS) — controls HVAC, access control, and medical gas systems
- Nurse workstations — 320 Windows PCs throughout the hospital

**Security concerns identified in the annual risk assessment:**

1. The EHR system runs on Windows Server 2019 and has 14 unpatched critical CVEs outstanding; patch testing is required before deployment (risk: ransomware exploitation)
2. Nurse workstation accounts use shared passwords (departmental passwords) and no MFA (risk: unauthorized access to patient records)
3. The patient portal has not had a penetration test in three years; OWASP Top 10 vulnerabilities are suspected (risk: patient data breach through web application attack)
4. Staff cybersecurity awareness training was last conducted 18 months ago; phishing simulation shows a 34% click rate (risk: phishing leading to credential compromise)
5. The PACS imaging system has no backup; data is stored on a single RAID array with no offsite copy (risk: permanent data loss from hardware failure or ransomware)

---

## Part 1 — Quantitative Risk Analysis (25 minutes)

### Task 1.1 — EHR Ransomware Risk Analysis

Using the information below, perform a full quantitative risk analysis for Risk #1 (EHR ransomware):

**Given values:**

- Asset: EHR system and the patient data it contains
- Asset Value (AV): $3,500,000 (estimated regulatory fines + breach notification costs + data reconstruction + operational disruption)
- Exposure Factor (EF): 0.65 (estimated 65% of EHR data/system would be impacted in a ransomware event)
- Annual Rate of Occurrence (ARO): 0.35 (industry base rate for healthcare ransomware, adjusted for the presence of 14 unpatched critical CVEs)

**Calculate and record:**

1. SLE (Single Loss Expectancy) = AV × EF
2. ALE (Annual Loss Expectancy) = SLE × ARO

**Proposed control: Emergency Patch Deployment Program**

- Cost: $85,000 one-time implementation + $40,000/year ongoing
- Effect: Reduces ARO from 0.35 to 0.08 (by closing the vulnerability window)
- First year total cost: $125,000 ($85,000 + $40,000)
- Ongoing annual cost: $40,000

**Calculate:**

3. New ALE after control (using ARO = 0.08)
4. ALE reduction = Old ALE − New ALE
5. First-year net benefit = ALE reduction − First-year control cost
6. Ongoing annual net benefit = ALE reduction − Annual control cost (years 2+)

**Task 1.2 — Interpretation**

Based on your calculations, write a three- to four-sentence recommendation to hospital leadership addressing: Is the patch deployment program financially justified? What does the ALE reduction represent in practical terms?

### Task 1.3 — Patient Portal Web Application Risk Analysis

Using the following given values, repeat the quantitative analysis for Risk #3 (patient portal web application breach):

- **AV:** $1,200,000
- **EF:** 0.45
- **ARO:** 0.20

**Proposed control: Annual Penetration Testing**

- Cost: $35,000/year
- Effect: Reduces ARO from 0.20 to 0.08

Calculate: SLE, original ALE, new ALE, ALE reduction, net annual benefit.

---

## Part 2 — Qualitative Risk Matrix (15 minutes)

### Task 2.1 — Build the Risk Matrix

Create a 3×3 qualitative risk matrix using the following scale:

**Likelihood:** Low (L), Medium (M), High (H)

**Impact:** Low (1), Medium (2), High (3)

**Risk Rating:** Combine to produce: Low, Medium, High, or Critical

Fill in the nine cells of the matrix with appropriate risk ratings.

### Task 2.2 — Rate All Five Risks

For each of the five identified risks at Cascade Regional, assign a likelihood and impact rating using the qualitative scale, then determine the risk rating from your matrix.

Complete the following table:

| Risk # | Risk Description | Likelihood | Impact | Risk Rating | Justification (2 sentences) |
|---|---|---|---|---|---|
| 1 | EHR unpatched CVEs | | | | |
| 2 | Shared passwords / no MFA | | | | |
| 3 | Patient portal no pen test | | | | |
| 4 | Phishing — 34% click rate | | | | |
| 5 | PACS no backup | | | | |

### Task 2.3 — Prioritization

Based on your risk ratings, rank the five risks from highest to lowest priority for treatment. Write one paragraph (four to five sentences) explaining your prioritization rationale. Note if any risks should be treated together.

---

## Part 3 — Risk Register Construction (20 minutes)

### Task 3.1 — Populate Risk Register Entries

Using the template below, create complete risk register entries for Risks #1, #4, and #5. For each entry, fill in all fields. Use your quantitative analysis results where applicable and supplement with reasonable assumptions for fields not covered by the scenario.

**Risk Register Template:**

| Field | Risk #1 | Risk #4 | Risk #5 |
|---|---|---|---|
| Risk ID | CAS-001 | CAS-004 | CAS-005 |
| Risk Description | | | |
| Risk Category | | | |
| Threat | | | |
| Vulnerability | | | |
| Likelihood | | | |
| Impact | | | |
| Risk Rating | | | |
| Risk Owner (role title) | | | |
| Current Controls | | | |
| Risk Response (Avoid/Transfer/Mitigate/Accept) | | | |
| Planned Actions | | | |
| Residual Risk (after planned actions) | | | |
| Target Completion Date | | | |
| Status | Open | Open | Open |
| Review Date | | | |

### Task 3.2 — Risk Ownership Analysis

Write a two- to three-sentence explanation of who should be the Risk Owner for Risk #5 (PACS no backup). Why should the Risk Owner NOT be the CISO or the security team? What principle does this assignment reflect?

---

## Part 4 — Business Impact Analysis (15 minutes)

### Task 4.1 — Identify MTD for Critical Systems

For each system below, the hospital operations team has provided the business context. Based on this context, assign a Maximum Tolerable Downtime (MTD) and justify your choice:

**EHR System:** Without the EHR, nurses use paper records. After 12 hours, paper records cannot be reconciled with EHR data and patient safety errors become likely. After 24 hours, critical clinical functions (medication orders, lab results) are severely impaired.

- Your MTD assignment: ______
- Justification (2 sentences): ______

**Medical Billing System:** Insurance claims can be queued manually for up to 5 business days before cash flow becomes critical. After 5 days, the hospital cannot meet payroll obligations.

- Your MTD assignment: ______
- Justification (2 sentences): ______

**Patient Portal:** Patients cannot schedule appointments or view lab results online. Staff can handle scheduling by phone. Minor operational impact — no patient safety risk.

- Your MTD assignment: ______
- Justification (2 sentences): ______

**Building Management System (BMS):** Controls HVAC, medical gas systems, and physical access. Without HVAC, operating rooms exceed safe temperature limits within 4 hours. Without medical gas control, surgical procedures cannot continue.

- Your MTD assignment: ______
- Justification (2 sentences): ______

### Task 4.2 — Derive RTO and RPO

For each system, set the RTO and RPO based on your MTD assignments:

| System | MTD | RTO | RPO | Backup Frequency Required |
|---|---|---|---|---|
| EHR | | | | |
| Billing | | | | |
| Patient Portal | | | | |
| BMS | | | | |

**Note:** RTO must be less than MTD. RPO determines backup frequency (if RPO = 4 hours, backups must run at least every 4 hours).

### Task 4.3 — Gap Analysis

The hospital's current backup and recovery plan specifies:

- EHR: nightly backups (RPO = up to 24 hours), RTO = 6 hours
- PACS: no backup
- Billing: daily backup (RPO = up to 24 hours), RTO = 12 hours
- Patient Portal: AWS handles recovery (cloud provider SLA of 4 hours)
- BMS: no documented recovery plan

Identify which systems have a gap between their current plan and the requirements you established in Task 4.2. For each gap, state the specific problem and propose a one-sentence remediation.

---

## Part 5 — Security Controls Classification (15 minutes)

### Task 5.1 — Classify the Controls

For each control below, classify by both function (Preventive, Detective, Corrective, Deterrent, Compensating, Directive) and type (Technical, Administrative, Physical):

| Control | Function | Type |
|---|---|---|
| Requiring MFA on all hospital workstations | | |
| Monthly phishing simulation with training for employees who click | | |
| Security camera coverage in the server room | | |
| Incident response plan and playbooks | | |
| Encrypted backup copies of PACS images in AWS S3 | | |
| Visible signage: "This area is monitored. Unauthorized access will be prosecuted." | | |
| Audit logging of all EHR access with alerts on anomalous access patterns | | |
| Using a jump server to access the BMS from the administrative network | | |
| Annual security awareness training program | | |
| Network segmentation isolating BMS from clinical and administrative networks | | |

### Task 5.2 — Defense in Depth Analysis

Write a paragraph (five to seven sentences) analyzing how the controls above, when combined, represent a defense-in-depth strategy for protecting the EHR. Identify at least one gap in the control coverage and propose a specific control to address it.

---

## Lab Report Submission Requirements

Submit a single document containing all completed tables, calculations, and written responses.

**Format:** PDF or Word document

**Minimum length:** 800 words excluding tables and calculations

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Quantitative analysis (correct calculations and interpretation) | 25 |
| Part 2 — Risk matrix construction and risk ratings with justification | 20 |
| Part 3 — Risk register entries complete and ownership analysis | 20 |
| Part 4 — BIA: MTD assignments, RTO/RPO derivation, gap analysis | 20 |
| Part 5 — Controls classification and defense-in-depth analysis | 15 |
| **Total** | **100** |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 13*
