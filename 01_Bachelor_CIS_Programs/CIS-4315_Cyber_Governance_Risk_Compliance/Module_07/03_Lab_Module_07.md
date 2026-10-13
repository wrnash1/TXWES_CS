# Lab Activity: Module 07 — Security Architecture and Controls

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Lab Overview

In this lab you will apply security architecture and control framework concepts to a real-world scenario. You will map an organization's existing controls to the NIST Cybersecurity Framework, identify gaps, classify controls by type and category, and draft a prioritized remediation roadmap.

This lab develops the practical skill of security architecture assessment — a core competency for CISM-aligned security managers. The deliverables are professional documents appropriate for an actual organizational security review.

**Estimated Time:** 90–120 minutes

**Submission:** Upload all deliverables as a single PDF or Word document to the Canvas LMS assignment portal.

---

## Scenario

**Hartwell Manufacturing** is a mid-size industrial manufacturer with 1,200 employees across three facilities. The company operates a mix of corporate IT (Windows-based office systems, ERP, email) and operational technology (factory floor control systems and IoT sensors).

Following a near-miss ransomware incident last quarter — in which attackers gained access to the corporate network through a phishing email but were blocked before reaching the OT environment — the board has asked for a security architecture assessment.

The security team has compiled the following inventory of current controls.

### Current Control Inventory

| Control | Type | Description |
|---|---|---|
| Perimeter firewall | Network | Stateful inspection firewall at internet edge |
| Email filtering | Network | Anti-spam and attachment scanning at email gateway |
| Antivirus | Endpoint | Signature-based AV on all Windows endpoints |
| VPN | Network | Remote access VPN for employees working off-site |
| Backup system | Data | Nightly full backup to on-premises tape |
| Password policy | Administrative | 8-character minimum, no complexity requirement, 90-day rotation |
| Incident response plan | Administrative | Written IR plan last updated 4 years ago |
| Physical badge access | Physical | Badge reader entry at all three facilities |
| Security camera system | Physical | Cameras at facility entrances and exits |
| IT admin accounts | Administrative | Shared admin credentials used by IT staff |

The following capabilities are **absent** from the current environment:

- No multi-factor authentication on any system
- No network segmentation between corporate IT and OT environments
- No security information and event management (SIEM) or centralized log management
- No endpoint detection and response (EDR) tool
- No data classification program
- No security awareness training program beyond a one-time onboarding video
- No vulnerability management or patching program

---

## Part A: CSF Mapping and Gap Analysis (40 points)

### Task Description

Map each of Hartwell's ten existing controls to the most appropriate NIST CSF 2.0 function. Then review the list of absent capabilities and map each to the CSF function it would support if implemented.

### Step 1: Map Existing Controls to CSF Functions

Create a table with these columns: Control Name, CSF Function, CSF Category (you may use a general category description rather than the alphanumeric code), and Brief Justification.

Complete this table for all ten existing controls. Reference the six CSF functions: Govern, Identify, Protect, Detect, Respond, Recover.

### Step 2: Map Absent Capabilities to CSF Functions

Create a second table with the same column structure, mapping the seven absent capabilities to the CSF functions they would support. Identify which function appears most frequently in the absent capabilities list and explain why this represents a strategic vulnerability for Hartwell.

### Step 3: Gap Statement

Write a paragraph of 4–6 sentences summarizing the most significant gaps in Hartwell's current security architecture. Reference specific CSF functions that are underrepresented and connect the gaps to the near-miss ransomware incident described in the scenario.

### Part A Grading

| Criteria | Points |
|---|---|
| Existing controls correctly mapped to CSF functions with justification | 16 |
| Absent capabilities correctly mapped with gap pattern identified | 12 |
| Gap statement is specific, accurate, and connects to scenario | 12 |

---

## Part B: Control Classification (25 points)

### Task Description

For each of the ten existing controls, classify the control using both dimensions: control type (preventive, detective, corrective, deterrent, or compensating) and control category (technical, administrative, or physical). Some controls may fit more than one type — in those cases, identify the primary type and note the secondary type.

### Deliverable Format

Create a table with these columns: Control Name, Primary Type, Secondary Type (if applicable), Category, and Justification (one sentence).

### Discussion Question

After completing the table, answer the following question in 3–5 sentences: Based on your classification analysis, what pattern do you observe in Hartwell's control portfolio? What type of control is most over-represented, and what type is most under-represented? What risk does this imbalance create?

### Part B Grading

| Criteria | Points |
|---|---|
| All ten controls correctly classified by type with justification | 15 |
| All ten controls correctly classified by category | 5 |
| Discussion question demonstrates analytical insight | 5 |

---

## Part C: Defense-in-Depth Assessment (20 points)

### Task Description

Using the architecture layer model from the reading guide (Perimeter, Network, Host, Application, Data), assess Hartwell's control coverage at each layer.

For each of the five layers, state whether coverage is adequate, partial, or absent, and list the specific controls present at that layer. Then identify the one layer with the most critical gap and explain why that gap represents the highest risk to Hartwell given the ransomware near-miss scenario.

### Deliverable Format

Present your assessment as a table with these columns: Architecture Layer, Coverage Rating, Controls Present, and Primary Gap. Below the table, write a 3–5 sentence analysis of the highest-priority gap layer.

### Part C Grading

| Criteria | Points |
|---|---|
| Five layers assessed with accurate coverage ratings and control listings | 12 |
| Highest-priority gap identified with scenario-specific rationale | 8 |

---

## Part D: Prioritized Remediation Roadmap (15 points)

### Task Description

Based on your gap analysis, select the three highest-priority absent capabilities that Hartwell should implement first. For each, write a brief implementation recommendation that includes: why this capability is the highest priority, which CSF function it supports, what control type and category it represents, and a realistic implementation timeline estimate (in months).

Present your three recommendations as a numbered priority list, with 4–6 sentences per recommendation.

Your prioritization should be risk-informed — consider the near-miss ransomware scenario, the absence of network segmentation between corporate and OT environments, and the lack of any detection capability.

### Part D Grading

| Criteria | Points |
|---|---|
| Three recommendations selected with logical risk-based prioritization | 6 |
| Each recommendation addresses all four required elements | 6 |
| Recommendations are realistic and professionally written | 3 |

---

## Submission Requirements

Your submission must be a single document (PDF or Word) containing all four parts with clear section headers. Include your name and student ID in the document header. All tables must be legible and properly formatted.

Late submissions lose 10 points per day per the course late policy.

---

## Lab Rubric Summary

| Part | Topic | Points |
|---|---|---|
| A | CSF Mapping and Gap Analysis | 40 |
| B | Control Classification | 25 |
| C | Defense-in-Depth Assessment | 20 |
| D | Prioritized Remediation Roadmap | 15 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

These challenges extend the Module 07 lab into advanced security architecture and control framework scenarios. Complete both challenges and the reflection questions for up to 15 bonus points.

---

### Challenge 1: Zero Trust Migration Planning

Cascade Logistics is a regional trucking and freight company with 800 employees distributed across 12 dispatch centers. The company's current architecture relies on a traditional perimeter model: a central data center in Dallas, site-to-site VPN connections to all dispatch centers, and an assumption that all traffic inside the VPN is trusted. The CISO has been directed to develop a Zero Trust migration roadmap following a security incident in which an attacker moved laterally from a compromised dispatch center workstation to the central payroll server.

**Step 1**: Identify at least four specific weaknesses in Cascade's current perimeter-based architecture that the lateral movement incident revealed. For each weakness, identify the Zero Trust principle or component (e.g., continuous verification, micro-segmentation, least-privilege access, device health validation) that would address it.

**Step 2**: Design a phased Zero Trust migration roadmap for Cascade over 24 months. Organize your roadmap into three phases of approximately 8 months each. For each phase, identify: the ZTA capabilities being implemented, the specific controls or technologies required, the business risk reduced by each phase, and the success criteria for completing the phase before proceeding.

**Step 3**: The CFO asks for financial justification before approving the $1.2M migration budget. Using the ALE formula, construct a financial justification. Assume: the payroll server asset value is $4,500,000; the lateral movement attack scenario has an exposure factor of 0.55; the current ARO is 0.40; after ZTA implementation the ARO is estimated at 0.05. Calculate the current ALE, the projected ALE after ZTA, and the net annual benefit. Present this as a one-paragraph executive summary suitable for a board briefing.

---

### Challenge 2: Control Framework Gap Analysis and Crosswalk

A healthcare organization (250 employees, subject to HIPAA) has been using CIS Controls v8 Implementation Group 1 as its primary security framework. Following a HIPAA audit, the organization received findings that several HIPAA Security Rule requirements are not addressed by IG1 alone. The CISO needs to perform a control gap analysis and crosswalk to identify which additional controls from CIS IG2 or NIST SP 800-53 Moderate baseline are required to satisfy the HIPAA deficiencies.

**Step 1**: The audit identified four specific HIPAA Security Rule gaps: (1) no audit controls for ePHI access (§164.312(b)), (2) no automatic log-off on workstations (§164.312(a)(2)(iii)), (3) no encryption of ePHI at rest (§164.312(a)(2)(iv)), and (4) no formal risk analysis documentation (§164.308(a)(1)). For each gap, identify the corresponding CIS Controls v8 safeguard (from IG2 or IG3 if not in IG1) and the NIST SP 800-53 control family that addresses the requirement.

**Step 2**: Construct a compliance crosswalk table with the following columns: HIPAA Security Rule Requirement, CIS Controls v8 Safeguard (number and name), NIST SP 800-53 Control ID, Current Status (Gap/Partial/Met), and Remediation Priority (High/Medium/Low).

**Step 3**: Write a 200-word gap remediation recommendation memo to the CISO prioritizing the four findings. Your memo must explain why one finding should be addressed before the others (reference both compliance risk and operational risk in your justification), and identify any control that simultaneously addresses more than one HIPAA gap.

---

### Reflection Questions

Answer each reflection question in four to six sentences.

1. Defense-in-depth is sometimes criticized as producing unnecessary complexity and cost without proportional security benefit — particularly when organizations layer controls that protect against the same attack vector rather than different vectors. Describe how a security architect should evaluate whether a proposed additional control layer genuinely adds defense-in-depth value versus redundantly duplicating an existing control, and what criteria should drive that decision.

2. The NIST Cybersecurity Framework is deliberately framework-agnostic — it can be used alongside NIST SP 800-53, CIS Controls, ISO 27001, or any other control catalog. Explain why this agnosticism is a design feature rather than a weakness, and describe a scenario where an organization would benefit from using the CSF as an overlay across two different control frameworks simultaneously.
