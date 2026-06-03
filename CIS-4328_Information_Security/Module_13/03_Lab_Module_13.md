# Lab: Module 13 — Risk Management

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

In this lab you will apply quantitative and qualitative risk analysis to a realistic organizational scenario, construct a risk register for a small company, perform a Business Impact Analysis for critical business functions, and evaluate risk response decisions. All activities are document-based and require no special software beyond a spreadsheet application.

**Estimated completion time:** 90 to 120 minutes

**Tools required:** Microsoft Excel, Google Sheets, or LibreOffice Calc; a text editor for written responses

---

## Learning Outcomes

By completing this lab you will be able to:

- Perform AV, EF, SLE, ARO, and ALE calculations and interpret the results.
- Evaluate control cost-effectiveness using the value of safeguard formula.
- Construct a risk register with at least five entries across multiple risk categories.
- Perform a simplified Business Impact Analysis and establish RTO and RPO values.
- Select and justify risk response strategies for identified risks.

---

## Scenario Background

Riverstone Medical Associates is a 12-physician medical practice with 85 employees. Their environment includes:

- An on-premises EMR (Electronic Medical Record) server storing 22,000 patient records.
- A medical billing system hosted by a third-party SaaS provider.
- 30 clinical workstations running Windows 10.
- A public-facing patient portal for appointment scheduling.
- A server room with basic access control (keypad lock) but no security cameras.
- Internet connectivity through a single ISP with no redundancy.
- Backups that run nightly to a NAS device in the server room.

Riverstone has no dedicated IT security staff. The office manager handles IT with help from a managed service provider (MSP) that performs monthly maintenance.

---

## Part 1 — Quantitative Risk Calculations

Use the following information to complete the calculations in this part.

### Scenario 1 — Ransomware Attack

The EMR server has an Asset Value of $1,800,000 (accounting for HIPAA fines, patient notification costs, recovery, lost revenue, and reputational impact). Security analysts estimate that a ransomware attack affecting the EMR would render 80% of operations inaccessible until resolved. Given recent industry data on medical practices of this size, the estimated frequency is once every three years.

**Lab Question 1:** Calculate the following and show all work:

- Exposure Factor (EF)
- Single Loss Expectancy (SLE)
- Annual Rate of Occurrence (ARO)
- Annual Loss Expectancy (ALE)

**Lab Question 2:** The MSP offers a managed backup and immutable recovery solution for $14,400 per year ($1,200/month). This solution would reduce the Exposure Factor from 80% to 15% by ensuring complete, tested recovery within 4 hours. Calculate the ALE after implementing the control, then calculate the Value of Safeguard (also called return on security investment). Is the control economically justified?

### Scenario 2 — Physical Break-In

The server room contains the EMR server and backup NAS device. If both were stolen, the AV (hardware replacement + data recovery attempt + downtime) is $240,000. A break-in would affect 100% of server room assets. Based on crime statistics for the area, the practice estimates a 25% chance of break-in per year.

**Lab Question 3:** Calculate SLE and ALE for the physical break-in scenario.

**Lab Question 4:** Installing security cameras and a biometric lock on the server room costs $3,500 one-time and $600/year in maintenance. These controls reduce the likelihood of break-in by 70% (ARO drops to 0.075). Calculate the new ALE and the Value of Safeguard for the first year (including the one-time cost). Is this control justified?

---

## Part 2 — Qualitative Risk Matrix

Using the 5×5 qualitative risk matrix below, assess five risks facing Riverstone Medical Associates. For each risk, assign a Likelihood score (1–5) and an Impact score (1–5), compute the Risk Score (Likelihood × Impact), and recommend a response.

**Likelihood Scale**: 1 = Rare, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Almost Certain

**Impact Scale**: 1 = Negligible, 2 = Minor, 3 = Moderate, 4 = Major, 5 = Catastrophic

Risks to assess:

1. Phishing email leads to staff credentials being stolen.
2. Internet outage due to single ISP failure.
3. HIPAA audit finds that patient data was accessed by a terminated employee.
4. Patient portal is defaced by a hacktivist group.
5. A physician's laptop containing unencrypted appointment notes is lost.

**Lab Question 5:** Complete the qualitative risk matrix table below. For each risk, include: Risk Description, Likelihood (1–5), Impact (1–5), Risk Score, and Recommended Response (Avoid/Transfer/Mitigate/Accept).

Create a table with columns: Risk ID | Description | Likelihood | Impact | Score | Response

**Lab Question 6:** Which risk received the highest score? Describe two specific mitigation controls that would reduce either the likelihood or the impact of that risk. For each control, state whether it reduces likelihood, impact, or both.

---

## Part 3 — Risk Register Construction

Using the five risks from Part 2 plus two additional risks you identify, construct a risk register for Riverstone Medical Associates. Include all seven risks.

**Lab Question 7:** Create a risk register spreadsheet with the following columns for each entry:

- Risk ID
- Risk Description
- Category (Technical/Operational/Regulatory/Physical)
- Likelihood (H/M/L)
- Impact (H/M/L)
- Risk Score
- Existing Controls
- Risk Response
- Residual Risk (H/M/L after existing controls)
- Risk Owner (assign a plausible role: Office Manager, MSP, Lead Physician, etc.)
- Target Date

For your two additional risks, identify risks not already covered in Part 2. Consider Riverstone's single ISP dependency, SaaS billing provider, or the absence of dedicated security staff.

---

## Part 4 — Business Impact Analysis

Riverstone has three critical business functions that must be evaluated in the BIA.

**Function 1 — Patient Scheduling System**: Used by front desk staff to schedule appointments. If unavailable, staff must use paper-based scheduling. Maximum tolerable downtime before physicians cannot see patients: 8 hours.

**Function 2 — EMR System**: Used by all physicians during patient visits. Without EMR, patient care degrades significantly but can continue with paper records. After 4 hours without EMR, patient safety risk increases due to missing allergy and medication data.

**Function 3 — Medical Billing System (SaaS)**: Revenue cycle management. Claims cannot be submitted during outage. Revenue impact begins after 24 hours. Business viability threatened after 5 business days.

**Lab Question 8:** For each function, establish:

- MTD (Maximum Tolerable Downtime): Based on the scenario descriptions.
- RTO (Recovery Time Objective): Set this at a value shorter than MTD.
- RPO (Recovery Point Objective): Based on how much data loss the function could tolerate (e.g., 4-hour RPO means daily backups are insufficient — backups must occur every 4 hours or less).

**Lab Question 9:** Riverstone's current backup runs nightly (once every 24 hours) to the same server room NAS. Based on your RPO values from Question 8, which functions are NOT adequately protected by the current backup scheme? Describe the backup changes required for each under-protected function.

---

## Part 5 — Risk Response Justification

**Lab Question 10:** Riverstone's office manager reviews the risk register and asks: "We are a small practice with limited budget. Can we just accept the risk of the patient portal being defaced? It's just a scheduling page."

Write a 150 to 200-word response to the office manager that:

- Explains what formal risk acceptance requires (vs. informal tolerance).
- Identifies at least one risk acceptance would not be appropriate here (HIPAA/regulatory context).
- Recommends a specific, proportionate mitigation that makes the risk acceptable within a small-practice budget.

---

## Deliverables

Submit a lab report containing:

- All calculations from Part 1 with work shown (Questions 1–4).
- Completed qualitative risk matrix table (Question 5).
- Written answer to Question 6.
- Completed risk register spreadsheet exported as PDF or screenshot (Question 7).
- BIA table from Part 4 (Questions 8–9).
- Written response from Part 5 (Question 10).

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Quantitative calculations, all formulas shown correctly (Questions 1–4) | 30 |
| Part 2 — Qualitative matrix, five risks with scores and responses (Questions 5–6) | 20 |
| Part 3 — Risk register, seven entries with all fields completed (Question 7) | 20 |
| Part 4 — BIA with MTD/RTO/RPO and backup gap analysis (Questions 8–9) | 20 |
| Part 5 — Risk acceptance response memo (Question 10) | 10 |
| **Total** | **100** |

---

*End of Lab — Module 13*
