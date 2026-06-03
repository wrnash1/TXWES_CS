# Video Script: Module 04 — Risk Assessment and Analysis Techniques

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 22–24 minutes

## CISM Domain Alignment: Domain 2 — Information Risk Management

---

## Production Notes

- Slides: 20 slides total
- Recording environment: lecture capture with slide overlay
- Display risk matrix diagrams and formula tables clearly; use zoom for formula slides

---

## Opening Segment (2 minutes)

[SHOW SLIDE 1 — Title: Risk Assessment and Analysis Techniques]

Welcome back. I'm Professor Nash, and this is Module 4 of CIS-4315.

Last module we explored the frameworks that give organizations a structured process for managing risk — NIST RMF, ISO 31000, OCTAVE, and FAIR. Today we go one level deeper. We are going to look at the specific techniques that analysts use *inside* those frameworks to actually measure and analyze risk.

[PAUSE — 2 seconds]

Think of it this way: a framework is the recipe, and assessment techniques are the cooking methods. Knowing that NIST RMF requires a risk assessment in Step 5 is one thing. Knowing *how* to conduct that assessment — what questions to ask, what data to gather, what analytical methods to apply — is a completely different skill.

[SHOW SLIDE 2 — Module 04 Learning Objectives]

By the end of this module, you will be able to distinguish between qualitative and quantitative risk assessment methods and explain when each is appropriate. You will be able to calculate Single Loss Expectancy and Annualized Loss Expectancy. You will be able to describe how a Business Impact Analysis is conducted and what it produces. And you will understand the purpose and outputs of threat modeling.

These are core CISM Domain 2 competencies, and they are heavily tested on the exam. Let's go.

[PAUSE — 2 seconds]

---

## Part 1 — Qualitative vs. Quantitative Assessment (6 minutes)

[SHOW SLIDE 3 — The Two Approaches to Risk Analysis]

Risk analysis — the step where we evaluate the likelihood and impact of identified risks — can be approached in two fundamentally different ways: qualitatively or quantitatively. Understanding the difference between these approaches, and knowing which one to use in a given situation, is a critical skill for the CISM exam and for your professional practice.

[PAUSE — 2 seconds]

[SHOW SLIDE 4 — Qualitative Risk Analysis]

In qualitative risk analysis, we assign descriptive ratings rather than numerical values. Likelihood might be rated as Rare, Unlikely, Possible, Likely, or Almost Certain. Impact might be rated as Negligible, Minor, Moderate, Major, or Critical. These ratings are typically placed on a risk matrix — sometimes called a heat map — where likelihood is one axis and impact is the other. The intersection of likelihood and impact gives you a risk priority: High, Medium, or Low.

[PAUSE — 2 seconds]

The great strengths of qualitative analysis are its speed and accessibility. You do not need detailed financial data or statistical expertise. A working group of knowledgeable subject matter experts can conduct a qualitative assessment in a few days, even for a complex organization. The outputs are easy to visualize and communicate — everyone understands a red-yellow-green heat map.

The limitations are equally important to understand. Qualitative ratings are inherently subjective. Two analysts looking at the same risk may assign different likelihood ratings based on their experience and assumptions. The categories are ordinal, not cardinal — "High" does not mean twice as bad as "Medium." And qualitative analysis does not give you the financial data needed to justify a specific security investment to senior leadership.

[SHOW SLIDE 5 — Quantitative Risk Analysis]

Quantitative risk analysis replaces descriptive ratings with numerical values — specifically, financial estimates. The goal is to express risk as an expected dollar loss over a defined time period, typically one year.

The quantitative approach uses a chain of formulas. Let me walk through them carefully because these are directly testable on the CISM exam.

[PAUSE — 2 seconds]

**Asset Value (AV):** The monetary value of the asset at risk. This might be replacement cost, revenue dependency, or a combination of both. For a customer database, AV might represent both the replacement cost of the data infrastructure and the revenue at risk if the data were compromised.

**Exposure Factor (EF):** The percentage of the asset's value that would be lost in a single occurrence of the risk event. If a server room fire would destroy 60% of the datacenter's equipment, the EF is 0.60.

**Single Loss Expectancy (SLE):** The expected monetary loss from a single occurrence of the risk. The formula is: SLE equals Asset Value multiplied by Exposure Factor. SLE = AV × EF.

[PAUSE — 3 seconds]

[SHOW SLIDE 6 — ALE Formula]

**Annualized Rate of Occurrence (ARO):** The estimated frequency with which the risk event will occur in a given year. If we expect a ransomware attack once every two years, the ARO is 0.5. If we expect phishing attempts twelve times per year, the ARO is 12.

**Annualized Loss Expectancy (ALE):** The expected annual financial loss from this risk. The formula is: ALE equals Single Loss Expectancy multiplied by Annualized Rate of Occurrence. ALE = SLE × ARO.

Let me give you a worked example. Suppose we have a database server with an Asset Value of $500,000. A ransomware attack would damage 80% of the data, so the Exposure Factor is 0.80. We estimate ransomware hits once every two years, so ARO is 0.5.

SLE = $500,000 × 0.80 = $400,000.

ALE = $400,000 × 0.5 = $200,000 per year.

This means we can justify spending up to $200,000 annually on ransomware controls for this server. If a control costs $50,000 per year and reduces the ALE from $200,000 to $80,000, we have saved $120,000 per year — a clear business case.

[PAUSE — 3 seconds]

[SHOW SLIDE 7 — Comparison Table]

Here is a comparison table to anchor both approaches.

Qualitative: faster, subjective, accessible, visual output (heat map), no financial data required, suited for broad initial assessments.

Quantitative: slower, objective (when good data exists), requires financial expertise, produces dollar estimates, suited for investment justification and detailed analysis.

For the CISM exam, the key judgment question is: which approach is appropriate given the organization's available data, time constraints, and purpose of the assessment? When financial data is unavailable or the scope is very broad, qualitative is appropriate. When the purpose is to justify a specific investment or prioritize remediation spending, quantitative is appropriate.

[PAUSE — 3 seconds]

---

## Part 2 — Business Impact Analysis (6 minutes)

[SHOW SLIDE 8 — What Is a Business Impact Analysis?]

A Business Impact Analysis — or BIA — is one of the most important tools in the risk manager's toolkit. A BIA does not ask "what could go wrong?" It asks "if something did go wrong, what would the consequences be for the business?"

[PAUSE — 2 seconds]

The BIA is the foundation of business continuity planning and disaster recovery planning. It identifies which business processes and supporting systems are most critical to the organization's survival and success, and it quantifies the harm that would result if those processes or systems were unavailable.

The BIA produces several key outputs that the CISM exam tests directly.

[SHOW SLIDE 9 — BIA Key Metrics]

**Maximum Tolerable Downtime (MTD):** Also called Maximum Tolerable Period of Disruption (MTPD). This is the longest period a business process can be unavailable before the organization suffers irreversible harm — loss of customers, regulatory non-compliance, financial collapse, or mission failure. MTD is set by business owners, not IT.

**Recovery Time Objective (RTO):** The target time within which a system or process must be restored following a disruption. RTO must always be less than MTD. If the MTD for order processing is 48 hours, the RTO might be set at 24 hours to provide a safety margin.

**Recovery Point Objective (RPO):** The maximum amount of data loss the organization can tolerate, measured in time. If the RPO for the customer database is 4 hours, then backups must be taken at least every 4 hours — because losing more than 4 hours of transaction data is unacceptable.

[PAUSE — 2 seconds]

[SHOW SLIDE 10 — BIA Metrics Relationships]

Let me illustrate the relationship between these metrics with a diagram. Imagine a timeline. At Time Zero, a disruption occurs — perhaps a server failure. The clock starts. The RPO defines how far back in time we can afford to roll back data — the maximum acceptable data gap. The RTO defines how long we have to restore systems before business damage becomes serious. The MTD is the absolute deadline — beyond this point, the organization may not recover.

For example, a financial trading platform might have an RPO of 15 minutes — meaning no more than 15 minutes of trade data can be lost. Its RTO might be 30 minutes. Its MTD might be 2 hours. All three metrics must be defined by the business, and all three drive the technical recovery architecture.

[PAUSE — 2 seconds]

[SHOW SLIDE 11 — Conducting a BIA]

How is a BIA actually conducted? The process has four main activities.

First, identify critical business processes. Work with business unit managers to identify every process the organization depends on to fulfill its mission. This is not an IT exercise — business owners drive it.

Second, identify dependencies. For each critical process, identify the systems, data, personnel, vendors, and facilities it depends on. A process is only as resilient as its weakest dependency.

Third, determine impact of disruption. For each process, assess the operational, financial, regulatory, and reputational impact of disruption over time. A process that causes minor inconvenience after one day but regulatory violation after three days has a very different risk profile than one that causes immediate financial loss.

Fourth, define MTD, RTO, and RPO. Based on the impact analysis, set formal targets. These targets become the requirements that drive recovery architecture, backup schedules, and continuity planning.

[PAUSE — 3 seconds]

[SHOW SLIDE 12 — BIA Output Example]

Here is a simplified BIA output table to make this concrete. The Payroll System has an MTD of 72 hours, an RTO of 24 hours, and an RPO of 24 hours. The E-Commerce Platform has an MTD of 4 hours, an RTO of 1 hour, and an RPO of 30 minutes. The Internal HR Portal has an MTD of 2 weeks, an RTO of 5 days, and an RPO of 24 hours.

This table immediately tells you which systems need the most robust recovery infrastructure and where to invest your limited continuity budget.

[PAUSE — 3 seconds]

---

## Part 3 — Threat Modeling (5 minutes)

[SHOW SLIDE 13 — Introduction to Threat Modeling]

The third major technique we are covering today is threat modeling. While qualitative and quantitative analysis help us evaluate risks that have already been identified, threat modeling is a structured technique for *discovering* threats that might otherwise be overlooked — particularly in the design phase of systems and applications.

[PAUSE — 2 seconds]

Threat modeling answers four fundamental questions. What are we building or operating? What can go wrong? What are we going to do about it? Did we do a good enough job?

[SHOW SLIDE 14 — STRIDE Threat Model]

The most widely used threat modeling framework in the security industry is STRIDE, developed by Microsoft. STRIDE is an acronym for six categories of threats.

**Spoofing:** Impersonating a user, system, or component to gain unauthorized access.

**Tampering:** Unauthorized modification of data in transit or at rest.

**Repudiation:** The ability of a user to deny having performed an action, due to insufficient logging or audit trails.

**Information Disclosure:** Unauthorized exposure of sensitive data.

**Denial of Service:** Disrupting availability of a system or service.

**Elevation of Privilege:** Gaining access or permissions beyond what is authorized.

[PAUSE — 2 seconds]

[SHOW SLIDE 15 — STRIDE Application Process]

In practice, threat modeling using STRIDE follows a structured process. First, the team creates a Data Flow Diagram (DFD) of the system — mapping data flows, process steps, trust boundaries, and external entities. Then, for each element in the diagram, the team systematically asks: could this element be the target of Spoofing? Tampering? Repudiation? Information Disclosure? Denial of Service? Elevation of Privilege?

Each identified threat is documented with its source, target, attack path, and potential mitigation. The output is a threat model — a structured catalog of threats that feeds directly into control selection and security requirements.

[PAUSE — 2 seconds]

[SHOW SLIDE 16 — PASTA Threat Model]

A more advanced threat modeling methodology is PASTA — Process for Attack Simulation and Threat Analysis. PASTA is a seven-stage, risk-centric approach that connects technical threat analysis to business impact. Where STRIDE identifies threats at the system design level, PASTA ties those threats to business objectives and uses attack simulation to evaluate realistic attack paths.

For the CISM exam, you do not need deep expertise in PASTA, but you should know that it exists and that it produces business-aligned threat analysis output.

[PAUSE — 2 seconds]

[SHOW SLIDE 17 — Threat Modeling Output and Integration]

The outputs of threat modeling — regardless of the method — are threat lists, attack scenarios, data flow diagrams, and prioritized security requirements. These outputs feed directly into risk assessment: each identified threat becomes a risk scenario that can be analyzed qualitatively or quantitatively.

Threat modeling is most valuable when conducted early in the system development lifecycle, before architecture decisions are locked in. Fixing a design flaw in threat modeling costs orders of magnitude less than fixing it after deployment.

[PAUSE — 3 seconds]

---

## Summary and Closing (2 minutes)

[SHOW SLIDE 18 — Technique Integration]

Before we close, let me show you how these three techniques work together in practice.

A typical risk assessment process might begin with threat modeling to identify the threat landscape for a specific system. Then qualitative analysis using a risk matrix provides a rapid, broad prioritization of identified threats — separating the critical few from the manageable many. Then quantitative analysis using SLE and ALE is applied to the highest-priority threats to build the financial business case for control investments. And throughout this process, the BIA ensures that the analysis is grounded in business impact — that the risks we are most focused on are the ones that would most harm the organization's mission.

[PAUSE — 2 seconds]

[SHOW SLIDE 19 — CISM Exam Priorities for Module 04]

For your CISM exam preparation, prioritize the following from this module.

Memorize the ALE formula chain: SLE = AV × EF; ALE = SLE × ARO. Expect calculation questions.

Know when qualitative is appropriate versus quantitative. Scenario questions will test this judgment.

Know the definitions and relationships between MTD, RTO, and RPO. These appear in both Domain 2 (Risk Management) and Domain 4 (Incident Management) contexts.

Know that STRIDE is the primary threat modeling framework and what each letter stands for.

[SHOW SLIDE 20 — Module 04 Summary]

In Module 5, we will complete our risk management arc by covering risk treatment — how organizations decide to avoid, transfer, mitigate, or accept the risks we have now identified and analyzed.

Your lab this week involves hands-on calculation of SLE and ALE for a realistic scenario, and a qualitative risk matrix exercise. I think you will find the calculations very straightforward once you work through them yourself.

[PAUSE — 2 seconds]

Great work today. I will see you in Module 5.

---

*End of Module 04 Video Script*

*Total estimated runtime: 23 minutes*
