# Reading Guide: Module 03 — Risk Management Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Introduction

Welcome to Module 03. This reading guide provides comprehensive reference material on the four major risk management frameworks covered in the video lecture: NIST RMF, ISO 31000, OCTAVE, and FAIR. Risk management is the foundation of CISM Domain 2 and represents approximately 20% of the CISM exam. Mastery of these frameworks will give you both the conceptual vocabulary and the practical judgment to answer scenario-based exam questions correctly.

---

## Section 1 — Why Frameworks Matter

Organizations face risk every day — from cyber threats, natural disasters, vendor failures, and human error. Without a structured approach, risk management becomes ad hoc, inconsistent, and impossible to audit or improve. A risk management framework provides three essential benefits.

First, it creates a repeatable process. When every risk assessment follows the same steps, results are comparable over time and across business units. Leadership can see whether the organization is improving or deteriorating.

Second, it establishes accountability. Frameworks define roles — who owns a risk, who authorizes decisions, who monitors outcomes. Clear ownership prevents risks from falling through organizational cracks.

Third, it enables communication. A shared framework gives security professionals and business leaders a common language. When a CISO says "this system is categorized as High-impact under our RMF," the Authorizing Official knows exactly what that means.

### Key Concept: Framework vs. Standard vs. Control

These three terms are frequently confused on the CISM exam.

| Term | Definition | Example |
|------|-----------|---------|
| Framework | A structured process or philosophy for managing risk | NIST RMF, ISO 31000, OCTAVE |
| Standard | Specific, auditable requirements organizations must meet | ISO 27001, PCI DSS, HIPAA |
| Control | A safeguard or countermeasure that reduces risk | Multi-factor authentication, encryption, access logging |

A framework tells you *how* to manage risk. A standard tells you *what* requirements you must satisfy. A control tells you *what* technical or procedural safeguards to implement.

---

## Section 2 — NIST Risk Management Framework

### 2.1 Background and Authority

The NIST RMF is defined in NIST Special Publication 800-37, Revision 2, "Risk Management Framework for Information Systems and Organizations." It is mandatory for all U.S. federal agencies under the Federal Information Security Modernization Act (FISMA) of 2014. It is also widely adopted by defense contractors, healthcare organizations, financial institutions, and state governments that interact with federal systems.

### 2.2 The Seven Steps

**Step 1 — Prepare**
Added in Revision 2, the Prepare step establishes the organizational and system-level context before risk management activities begin. Organizational-level tasks include identifying risk executives, establishing risk tolerance levels, identifying common controls that can be inherited, and developing an organization-wide risk management strategy. System-level tasks include identifying the system owner, assigning roles and responsibilities, and documenting the system's mission and operating environment.

> Exam Tip: The Prepare step is commonly tested because it was new in Rev. 2. Questions will ask what happens "before categorization" — the answer is Prepare.

**Step 2 — Categorize**
The system is categorized based on its potential impact on organizational operations, assets, and individuals if a security breach occurred. The three impact levels are Low, Moderate, and High, assessed separately for Confidentiality, Integrity, and Availability. The overall system categorization is the highest of the three. Guidance is provided by FIPS 199 (categorization criteria) and NIST SP 800-60 (information type mappings).

**Step 3 — Select**
Based on the system's impact categorization, an appropriate baseline of security controls is selected from NIST SP 800-53. Baselines are then tailored — controls may be scoped, parameterized, or supplemented based on the specific operational environment, threats, and risk appetite. Common controls inherited from the organization are documented here.

**Step 4 — Implement**
Selected controls are implemented in the system. Implementation details — including configuration settings, architectural decisions, and deviations from the baseline — are documented in the System Security Plan (SSP). The SSP is a living document that describes the security posture of the system.

**Step 5 — Assess**
An independent Security Control Assessor (SCA) evaluates the controls to determine whether they are implemented correctly, operating as intended, and producing the desired security outcome. The results are documented in a Security Assessment Report (SAR), which identifies any deficiencies.

**Step 6 — Authorize**
The Authorizing Official (AO) reviews the SSP, SAR, and a Plan of Action and Milestones (POA&M) documenting how deficiencies will be remediated. The AO makes a formal risk acceptance decision: Authority to Operate (ATO), Interim ATO, or Denial of ATO. This is a senior management decision, not a technical one.

**Step 7 — Monitor**
Authorized systems are continuously monitored. This includes ongoing control assessments, security status reporting, configuration management, and incident response. Significant changes to the system trigger re-authorization. The ongoing monitoring program maintains the ATO's validity over time.

### 2.3 NIST RMF Key Documents

| Document | Purpose |
|----------|---------|
| NIST SP 800-37 Rev. 2 | RMF process definition |
| FIPS 199 | System categorization criteria |
| NIST SP 800-60 | Information type to impact mappings |
| NIST SP 800-53 Rev. 5 | Security and privacy control catalog |
| NIST SP 800-53A | Assessment procedures for SP 800-53 controls |

### 2.4 Strengths and Limitations

Strengths: comprehensive documentation requirements, clear accountability chain, strong auditability, federal regulatory compliance.

Limitations: resource-intensive, can be slow to implement, U.S.-centric, primarily focused on information systems rather than enterprise-wide risk.

---

## Section 3 — ISO 31000

### 3.1 Background and Scope

ISO 31000:2018, "Risk Management — Guidelines," is published by the International Organization for Standardization. Unlike ISO 27001 (which is certifiable), ISO 31000 is a guidance standard — organizations cannot be "ISO 31000 certified." Instead, they use it as a framework to shape their risk management philosophy and process.

ISO 31000 is sector-agnostic and risk-type-agnostic. It applies equally to financial risk, environmental risk, safety risk, and information security risk. This universality makes it the preferred enterprise risk management (ERM) framework for multinational organizations operating under multiple regulatory regimes.

### 3.2 The Eight Principles

The 2018 revision reduced the principles from eleven to eight, emphasizing integration and leadership.

| Principle | Description |
|-----------|-------------|
| Integrated | Risk management is part of all organizational activities |
| Structured and comprehensive | Systematic approach contributes to consistent, comparable results |
| Customized | Tailored to the organization's context and objectives |
| Inclusive | Stakeholder engagement ensures relevant, up-to-date knowledge |
| Dynamic | Risk management anticipates, detects, and responds to change |
| Best available information | Inputs based on historical data, expert judgment, and stakeholder input |
| Human and cultural factors | Human behavior influences risk management effectiveness |
| Continual improvement | Organizations learn and adapt |

### 3.3 The Framework

The ISO 31000 Framework describes the organizational infrastructure needed to implement risk management effectively. It has five components arranged in a cycle: Leadership and Commitment, Integration, Design, Implementation, and Evaluation and Improvement. The key insight is that risk management must be driven from the top of the organization. Without executive leadership commitment, risk management becomes a compliance exercise rather than a genuine management discipline.

### 3.4 The Process

The ISO 31000 Process is the operational layer where risk management work is done. It consists of six activities running continuously, supported by communication and consultation throughout.

The six activities are: Scope, Context, and Criteria (establishing the boundaries and risk evaluation criteria); Risk Assessment (identification, analysis, and evaluation); Risk Treatment (selecting and implementing options to address risk); Monitoring and Review; Recording and Reporting; and Communication and Consultation (which runs parallel to all other activities).

> Exam Tip: ISO 31000 does not prescribe specific controls. CISM questions contrasting ISO 31000 with NIST RMF often test whether candidates understand that ISO 31000 is principles-based while NIST RMF is prescriptive.

---

## Section 4 — OCTAVE

### 4.1 Background

OCTAVE — Operationally Critical Threat, Asset, and Vulnerability Evaluation — was developed by the CERT Division of Carnegie Mellon's Software Engineering Institute. It was explicitly designed as a self-directed risk assessment methodology, enabling organizations to conduct rigorous assessments using their own personnel without requiring external consultants.

OCTAVE is particularly valuable for small to mid-sized organizations with limited security budgets, and for any organization that wants risk assessments grounded in operational reality rather than theoretical frameworks.

### 4.2 OCTAVE Versions

**OCTAVE (Original):** Designed for large organizations (300+ employees). Uses multi-disciplinary teams across three workshop phases. Produces asset-based threat profiles and a protection strategy.

**OCTAVE-S:** A streamlined version for small organizations (fewer than 100 employees). Conducted by a small core team rather than large workshops.

**OCTAVE Allegro:** Focuses specifically on information assets rather than IT systems broadly. Particularly useful when the organization needs to understand risk to information regardless of where that information resides (databases, paper, cloud services, portable devices).

### 4.3 OCTAVE Allegro — Eight-Step Process

OCTAVE Allegro is the most widely used version today. Its eight steps map to three phases.

Phase 1 — Build Asset-Based Threat Profiles:

- Step 1: Establish risk measurement criteria (impact areas and relative priorities)
- Step 2: Develop an information asset profile for each critical asset
- Step 3: Identify information asset containers (where the asset lives)
- Step 4: Identify areas of concern (threat scenarios)
- Step 5: Identify threat scenarios (detailed, structured threat statements)

Phase 2 — Identify Infrastructure Vulnerabilities:

- Step 6: Identify risks to the information asset

Phase 3 — Develop Security Strategy and Plans:

- Step 7: Analyze risks to the information asset
- Step 8: Select mitigation approaches

### 4.4 OCTAVE Strengths and Exam Focus

OCTAVE's primary strength is its focus on *operational* context — the people, processes, and technology that actually create and use information. This makes OCTAVE particularly good at surfacing risks that purely technical assessments miss, such as informal data sharing, shadow IT, and inadequate staff training.

> Exam Tip: OCTAVE is the correct choice when the scenario involves a self-directed assessment, limited budget, internal teams, or a focus on information assets and operational context.

---

## Section 5 — FAIR Model

### 5.1 Background

FAIR — Factor Analysis of Information Risk — was developed by Jack A. Jones while he was CISO at Nationwide Insurance. The FAIR Institute now maintains the model and its associated standards. FAIR is the only internationally recognized model for quantifying cybersecurity and operational risk in financial terms.

FAIR does not replace NIST RMF, ISO 31000, or OCTAVE. It complements them by providing the mathematical machinery to express risk in dollars — enabling business-case analysis and investment prioritization.

### 5.2 The FAIR Ontology

FAIR decomposes risk through a hierarchical taxonomy. At the top level:

**Risk = Probable Frequency × Probable Magnitude of Future Loss**

Frequency branch:

- Threat Event Frequency (TEF): How often does a threat agent act against an asset?
- Vulnerability (Vuln): When the threat acts, how likely is it to succeed?
- Loss Event Frequency (LEF) = TEF × Vuln

Magnitude branch:

- Primary Loss: Direct losses — response costs, replacement costs, productivity loss
- Secondary Loss: Downstream losses — regulatory fines, litigation, reputational damage
- Total Loss Magnitude = Primary Loss + Secondary Loss

### 5.3 FAIR Analysis Process

A FAIR analysis typically follows five steps.

First, identify the scenario — what asset, what threat community, what type of loss?

Second, evaluate Loss Event Frequency — estimate TEF and Vulnerability using probability ranges (minimum, most likely, maximum).

Third, evaluate Loss Magnitude — estimate Primary and Secondary loss ranges.

Fourth, derive Risk — run Monte Carlo simulation across the probability distributions to produce a range of probable annual loss in dollars.

Fifth, decide — compare the cost of a proposed control against the reduction in expected annual loss it would produce.

### 5.4 FAIR in Executive Communication

FAIR's financial output transforms cybersecurity discussions. Instead of presenting a "Medium" risk to the board, a CISO can present: "This unpatched vulnerability has an expected annual loss exposure between $1.2M and $4.7M, with a 90th-percentile outcome of $6.3M. The proposed control costs $280,000 per year and would reduce expected annual loss by $2.1M."

This financial framing enables the same cost-benefit analysis the organization applies to every other business investment.

> Exam Tip: FAIR is the answer when the scenario involves financial quantification of risk, board-level communication, or justifying security investment in dollar terms.

---

## Section 6 — Framework Selection Guide

The CISM exam frequently presents scenarios and asks which framework is most appropriate. Use this decision matrix.

| Scenario Characteristic | Most Appropriate Framework |
|------------------------|---------------------------|
| Federal agency or federal contractor | NIST RMF |
| Mandatory system authorization process needed | NIST RMF |
| International organization, multiple sectors | ISO 31000 |
| Enterprise-wide risk philosophy, board integration | ISO 31000 |
| Small to mid-size org, internal team, limited budget | OCTAVE |
| Focus on information assets across all containers | OCTAVE Allegro |
| Need to quantify risk in dollar terms | FAIR |
| Preparing a security investment business case | FAIR |
| Board or executive communication about financial exposure | FAIR |

---

## Section 7 — CISM Exam Tips

**Tip 1 — Know the NIST RMF Steps in Order.** The seven steps are: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. Exam questions will test the correct sequence and what happens when the sequence is violated.

**Tip 2 — Distinguish ISO 31000 from ISO 27001.** ISO 31000 is a risk management guidance standard (not certifiable). ISO 27001 is a certifiable information security management system standard. They are complementary but distinct.

**Tip 3 — OCTAVE is Internal; NIST RMF is Formal.** OCTAVE is designed for internal teams without external consultants. NIST RMF involves formal, independently conducted assessments and senior official authorization decisions.

**Tip 4 — FAIR Does Not Replace Other Frameworks.** FAIR is an analytical model for quantification. Organizations use FAIR alongside NIST RMF or ISO 31000, not instead of them.

**Tip 5 — Risk Treatment Options Appear in Multiple Frameworks.** All four frameworks ultimately lead to risk treatment: avoid, transfer, mitigate, or accept. Module 5 covers these treatment strategies in depth.

---

## Section 8 — Glossary

**Authorizing Official (AO):** A senior organizational official with the authority to formally accept residual risk and authorize a system to operate.

**Authority to Operate (ATO):** Formal authorization granted by an AO allowing a system to operate based on accepted residual risk.

**FIPS 199:** Federal Information Processing Standard 199 — defines three impact levels (Low, Moderate, High) for categorizing federal information systems.

**FAIR:** Factor Analysis of Information Risk — a quantitative model for expressing cybersecurity risk in financial terms.

**ISO 31000:** International standard providing principles, framework, and process for enterprise risk management.

**NIST RMF:** National Institute of Standards and Technology Risk Management Framework — a seven-step system lifecycle approach to federal information system security authorization.

**OCTAVE:** Operationally Critical Threat, Asset, and Vulnerability Evaluation — a self-directed, asset-based risk assessment methodology.

**POA&M:** Plan of Action and Milestones — documents identified security deficiencies, planned remediation actions, and target completion dates.

**Residual Risk:** The risk remaining after security controls have been implemented and risk treatment actions have been taken.

**System Security Plan (SSP):** The primary artifact documenting a system's security posture, controls, and implementation details in the NIST RMF.

---

## Required Reading

- NIST SP 800-37 Rev. 2 — Chapter 2 (RMF Fundamentals) and the task tables for each step. Available free at csrc.nist.gov.
- NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments. Provides the risk assessment methodology that supports NIST RMF Step 5.
- ISO 31000:2018 — Executive summary and Section 6 (Process). Available through university library database access.
- FAIR Institute white papers — available free at fairinstitute.org.

---

## Study Checklist

- [ ] Recite the seven NIST RMF steps from memory in correct order
- [ ] Explain the difference between NIST RMF and ISO 31000 in two sentences
- [ ] Describe the three phases of OCTAVE Allegro
- [ ] Explain how FAIR decomposes risk and what output it produces
- [ ] Complete the framework selection decision matrix without notes
- [ ] Review the glossary and define each term without looking
- [ ] Proceed to the Module 03 Lab Activity
