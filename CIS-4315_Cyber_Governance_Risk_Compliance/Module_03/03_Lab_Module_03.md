# Lab Activity: Module 03 — Risk Management Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Lab Overview

In this lab you will apply three of the four frameworks covered in Module 03 to a realistic organizational scenario. You will map a system through selected NIST RMF steps, apply ISO 31000 context-setting to an enterprise scenario, and conduct a simplified OCTAVE Allegro asset threat profile for a critical information asset. No special software is required — all work is document-based and can be completed in a word processor or spreadsheet.

**Estimated Time:** 90–120 minutes

**Submission:** Upload your completed Lab 03 Report to the Canvas assignment portal before the due date.

---

## Scenario Background

Lone Star Regional Medical Center (LSRMC) is a 450-bed regional hospital in Fort Worth, Texas. The organization recently completed a strategic technology review and identified three priority systems for security risk assessment.

**System A — Electronic Health Records (EHR) Platform:** Hosts patient medical records, treatment histories, and diagnostic imaging for 180,000 active patients. Accessed by 1,200 clinical staff. Subject to HIPAA. Classified as business-critical.

**System B — Billing and Revenue Cycle Management:** Processes insurance claims, stores patient financial data including credit card numbers, and interfaces with Medicare/Medicaid. Accessed by 90 finance staff. Subject to PCI DSS and HIPAA.

**System C — Internal Staff Scheduling Portal:** Allows 1,800 employees to view schedules, request shift changes, and access internal HR announcements. No patient data. No external interfaces.

The hospital's new CISO, hired from a federal contractor background, wants to apply the NIST RMF to the EHR platform, use ISO 31000 to establish an enterprise risk context, and use OCTAVE Allegro to assess the risk to patient records as an information asset.

---

## Task 1 — NIST RMF: System Categorization (25 points)

Apply NIST RMF Step 2 (Categorize) to System A — the EHR Platform.

### Step 1a — Define the Information Types

Using the NIST SP 800-60 categories as a reference, identify at least three information types processed by the EHR system. For each, provide a brief description.

Document your information types in the following format.

| Information Type | Description | Examples in EHR |
|-----------------|-------------|-----------------|
| (Type 1) | | |
| (Type 2) | | |
| (Type 3) | | |

### Step 1b — Assign Impact Levels

For each information type, assign a Confidentiality, Integrity, and Availability impact level (Low, Moderate, or High) and provide a written justification of two to three sentences for each assignment.

| Information Type | Confidentiality | Integrity | Availability | Justification Summary |
|-----------------|----------------|-----------|-------------|----------------------|
| (Type 1) | | | | |
| (Type 2) | | | | |
| (Type 3) | | | | |

### Step 1c — Determine Overall System Categorization

Apply the "high water mark" rule: the overall system categorization equals the highest impact level assigned across all three security objectives (Confidentiality, Integrity, Availability).

State the final system categorization for the EHR platform and explain in two to three paragraphs why this categorization is appropriate given LSRMC's mission and the nature of patient health information.

### Step 1d — Reflection Question

The NIST RMF categorization result determines which control baseline the hospital must implement from NIST SP 800-53. If you categorized the EHR as High-impact, the hospital faces a very large set of required controls. Write one paragraph explaining how the hospital's CISO might justify this significant security investment to the hospital's CFO.

---

## Task 2 — ISO 31000: Establishing Risk Context (25 points)

Apply ISO 31000's context-establishment activity to LSRMC as an enterprise.

### Step 2a — External Context

Identify and document at least four external factors that shape LSRMC's risk environment. For each factor, describe the risk it creates and its potential impact on the hospital's mission.

| External Factor | Risk Created | Potential Impact |
|----------------|-------------|-----------------|
| (Factor 1) | | |
| (Factor 2) | | |
| (Factor 3) | | |
| (Factor 4) | | |

Examples to consider (do not simply copy — explain each in your own words): regulatory environment (HIPAA, state health laws), threat landscape (ransomware targeting healthcare), vendor dependency (cloud EHR provider), patient expectations for privacy.

### Step 2b — Internal Context

Identify and document at least four internal factors that shape LSRMC's risk management capability.

| Internal Factor | Implication for Risk Management |
|----------------|--------------------------------|
| (Factor 1) | |
| (Factor 2) | |
| (Factor 3) | |
| (Factor 4) | |

Examples to consider: IT staff size and expertise, existing security controls, organizational culture around data handling, prior security incidents.

### Step 2c — Risk Criteria

ISO 31000 requires organizations to define criteria for evaluating whether a risk is acceptable. Define three risk criteria for LSRMC, explaining what level of likelihood and impact the hospital is willing to accept before requiring treatment action.

Present your criteria in a table with columns: Criteria Name, Description, Threshold for Treatment.

### Step 2d — Stakeholder Analysis

ISO 31000 emphasizes inclusive stakeholder engagement. Identify five stakeholders who should be involved in LSRMC's risk management process. For each, describe their interest in risk management outcomes and what input they should provide.

---

## Task 3 — OCTAVE Allegro: Asset Threat Profile (30 points)

Apply OCTAVE Allegro Steps 2 through 5 to the information asset: Patient Medical Records.

### Step 3a — Information Asset Profile (Allegro Step 2)

Complete the following asset profile for the Patient Medical Records asset.

| Field | Your Response |
|-------|--------------|
| Asset Name | Patient Medical Records |
| Asset Owner | |
| Asset Description | |
| Security Requirements (Confidentiality) | |
| Security Requirements (Integrity) | |
| Security Requirements (Availability) | |
| Most Important Security Requirement | |
| Rationale for Most Important Requirement | |

### Step 3b — Asset Containers (Allegro Step 3)

Identify at least five containers where Patient Medical Records exist or travel. For each, specify whether it is a technical container (database, server, cloud service), a physical container (paper, portable media), or a people container (staff who carry or transmit information).

| Container | Container Type | Location | Access Controls in Place? |
|-----------|---------------|----------|--------------------------|
| (Container 1) | | | |
| (Container 2) | | | |
| (Container 3) | | | |
| (Container 4) | | | |
| (Container 5) | | | |

### Step 3c — Areas of Concern (Allegro Step 4)

Identify at least four areas of concern — situations or conditions that could harm the Patient Medical Records asset. For each, identify the threat actor, the threat action, the container affected, and the potential outcome.

| Area of Concern | Threat Actor | Threat Action | Container Affected | Potential Outcome |
|----------------|-------------|--------------|-------------------|------------------|
| (Concern 1) | | | | |
| (Concern 2) | | | | |
| (Concern 3) | | | | |
| (Concern 4) | | | | |

### Step 3d — Threat Scenarios (Allegro Step 5)

Select two of your four areas of concern and develop them into structured OCTAVE Allegro threat scenarios. Each scenario should include: the threat actor and intent, the threat access method, the threat outcome, and the operational impact on LSRMC if the outcome occurs.

Write each threat scenario as a narrative paragraph of at least 100 words.

---

## Task 4 — Framework Comparison Essay (20 points)

Write a 300–400 word essay comparing the three frameworks you applied in this lab. Your essay must address all of the following questions.

- Which framework provided the most actionable output for LSRMC's CISO? Why?
- Which framework would be most valuable when presenting risk findings to the hospital's Board of Directors? Why?
- If LSRMC had a budget of only 80 staff hours for a complete risk assessment, which framework would you recommend and why?
- Where do the three frameworks complement each other, and how might LSRMC use all three together in a mature risk program?

---

## Deliverables Summary

Submit a single document (PDF or Word) containing all four tasks. Your submission must include the following components.

| Deliverable | Points | Completion Check |
|------------|--------|-----------------|
| Task 1: EHR Categorization (all four sub-tasks) | 25 | |
| Task 2: ISO 31000 Context Tables and Stakeholder Analysis | 25 | |
| Task 3: OCTAVE Allegro Asset Profile, Containers, Concerns, and Scenarios | 30 | |
| Task 4: Framework Comparison Essay (300–400 words) | 20 | |
| Total | 100 | |

---

## Grading Rubric

| Criterion | Full Credit | Partial Credit | No Credit |
|-----------|------------|---------------|-----------|
| FIPS 199 impact levels are correctly applied with justification | Levels match scenario facts; justification is substantive | Levels assigned without justification or one level is clearly wrong | No attempt or all levels incorrect |
| ISO 31000 context tables are complete and contextually relevant | All fields populated with hospital-specific content | Generic or incomplete entries | Missing or copied from examples |
| OCTAVE Allegro threat scenarios are structured and realistic | Narrative is specific, realistic, and addresses all required components | Scenarios are vague or missing one required component | No scenarios written |
| Framework comparison essay addresses all four questions | All four questions answered with specific evidence from the lab | Two or three questions addressed | One or no questions addressed |
| Document is professional: organized, free of errors, properly labeled | Clean formatting, labeled sections, spell-checked | Minor formatting issues | Disorganized or unreadable |

---

## Academic Integrity Notice

This lab requires original analysis. Your threat scenarios, context descriptions, and essay must reflect your own reasoning applied to the LSRMC scenario. Copying framework definitions verbatim from readings without applying them to the scenario will not receive credit. Cite any external sources you consult using APA format.
