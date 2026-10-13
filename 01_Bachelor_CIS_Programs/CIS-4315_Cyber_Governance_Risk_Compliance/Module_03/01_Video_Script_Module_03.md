# Video Script: Module 03 — Risk Management Frameworks

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 2 — Information Risk Management

---

## Production Notes

- Slides: 18 slides total
- Recording environment: lecture capture with slide overlay
- Use pointer tool to highlight framework diagrams

---

## Opening Segment (2 minutes)

[SHOW SLIDE 1 — Title: Risk Management Frameworks]

Welcome back, everyone. I'm Professor Nash, and this is Module 3 of CIS-4315, Cyber Governance, Risk, and Compliance.

In the last two modules, we established why information security governance matters and how organizations structure their security programs. Today we shift our focus to one of the most critical skills you will use throughout your career: selecting and applying a risk management framework.

[PAUSE — 2 seconds]

Think about the last time you made a decision with incomplete information. Maybe you were evaluating a job offer, deciding whether to take a road trip in uncertain weather, or choosing between two technology vendors. In each case, you were doing informal risk management — weighing likelihood against consequences and deciding how to proceed.

[SHOW SLIDE 2 — "What Is a Risk Framework?"]

Organizations face that same challenge at enormous scale, across thousands of systems, vendors, employees, and processes. Risk management frameworks give us structured, repeatable methods for identifying, analyzing, and responding to those uncertainties in a disciplined way.

By the end of this module, you will be able to describe the NIST Risk Management Framework, ISO 31000, OCTAVE, and the FAIR model. More importantly, you will understand when and why you would choose one over another — a skill that will serve you well on the CISM exam and in your professional life.

[PAUSE — 2 seconds]

Let's get started.

---

## Part 1 — NIST Risk Management Framework (6 minutes)

[SHOW SLIDE 3 — NIST RMF Overview]

The National Institute of Standards and Technology Risk Management Framework — which we call the NIST RMF — is the dominant framework for U.S. federal agencies and any organization that does business with the federal government. It was formalized in NIST Special Publication 800-37, Revision 2, published in 2018.

[PAUSE — 2 seconds]

The NIST RMF operates on a foundational premise: risk management is not a one-time event. It is a continuous process embedded in the organization's operations from the very beginning of a system's life cycle.

[SHOW SLIDE 4 — NIST RMF Seven Steps]

The framework defines seven steps. Let me walk through each one carefully.

**Step 1: Prepare.** This step was added in Revision 2 and is critically important. Before you can assess or authorize a system, the organization must establish the context. Who are the risk executives? What are the organization's risk tolerance levels? What common controls are already in place that all systems can inherit? Prepare answers these questions.

[PAUSE — 2 seconds]

**Step 2: Categorize.** Using FIPS Publication 199 and NIST SP 800-60, you categorize each information system based on the potential impact — low, moderate, or high — to confidentiality, integrity, and availability. This categorization drives every subsequent decision in the framework.

**Step 3: Select.** Based on your categorization, you select an appropriate set of security controls from NIST SP 800-53. A low-impact system gets a baseline set of controls. A high-impact system gets a more comprehensive set. You also tailor controls to fit your specific environment.

[SHOW SLIDE 5 — NIST RMF Steps 4 Through 7]

**Step 4: Implement.** You implement the selected controls and document how they are deployed. Configuration settings, architecture decisions, and compensating controls are all recorded here.

**Step 5: Assess.** An independent assessor evaluates whether the controls have been implemented correctly and are operating effectively. This is not self-attestation — the assessment must be objective.

**Step 6: Authorize.** A senior official — the Authorizing Official — reviews the assessment results and the residual risk, then makes a formal risk acceptance decision. The system either receives an Authority to Operate, an Interim Authority to Operate, or a denial.

[PAUSE — 2 seconds]

**Step 7: Monitor.** The authorized system is continuously monitored. Controls are assessed on a defined schedule, changes to the system trigger re-evaluation, and the organization maintains ongoing awareness of its security posture.

[SHOW SLIDE 6 — NIST RMF Key Strengths]

The great strength of the NIST RMF is that it connects individual system-level risk decisions to the organization's overall risk posture. Every authorization decision is visible to organizational leadership, and the continuous monitoring requirement means that authorization is never truly "done."

For the CISM exam, remember that NIST RMF is prescriptive and compliance-oriented. It is ideal for organizations with regulatory obligations to federal standards.

[PAUSE — 3 seconds]

---

## Part 2 — ISO 31000 (5 minutes)

[SHOW SLIDE 7 — ISO 31000 Overview]

Let's move now to ISO 31000. Where NIST RMF is prescriptive and U.S.-centric, ISO 31000 is principles-based and internationally applicable. It can be used by any organization in any sector, in any country, managing any type of risk — financial, operational, reputational, or information security risk.

[PAUSE — 2 seconds]

ISO 31000 was first published in 2009 and revised in 2018. The 2018 version is leaner and more leadership-focused than its predecessor. It does not define specific controls. Instead, it defines a philosophy and a process that organizations adapt to their unique context.

[SHOW SLIDE 8 — ISO 31000 Three Core Elements]

ISO 31000 is organized around three interconnected elements: Principles, Framework, and Process.

**Principles** define the characteristics of effective risk management. The 2018 standard identifies eight principles. Risk management should be integrated into the organization's work — not bolted on as a separate program. It should be structured and comprehensive. It should be customized to the organization's context. It should be inclusive of all relevant stakeholders. It should be dynamic, meaning it adapts as the risk environment changes. It should use the best available information. It should account for human and cultural factors. And finally, it should support continual improvement.

[PAUSE — 3 seconds]

[SHOW SLIDE 9 — ISO 31000 Framework and Process]

The **Framework** describes how risk management is established, embedded, and sustained in an organization. Leadership commitment is the starting point. The organization integrates risk management into its governance structures, strategy, and decision-making processes. The framework is regularly evaluated and improved over time.

The **Process** is where practitioners do the actual work. It begins with establishing context — understanding the organization's internal and external environment, its objectives, and the stakeholders who care about those objectives. Next comes risk identification, risk analysis, risk evaluation, risk treatment, monitoring and review, and communication throughout.

[SHOW SLIDE 10 — ISO 31000 vs. NIST RMF Comparison]

Here is a comparison worth committing to memory for the CISM exam. NIST RMF is compliance-driven and information-system-focused. ISO 31000 is strategy-driven and enterprise-wide. NIST RMF tells you specifically which controls to implement. ISO 31000 tells you how to think about and manage risk at a conceptual level.

Many organizations use both: ISO 31000 sets the enterprise risk philosophy, while NIST RMF handles technical implementation.

[PAUSE — 3 seconds]

---

## Part 3 — OCTAVE (4 minutes)

[SHOW SLIDE 11 — OCTAVE Overview]

Our third framework is OCTAVE — the Operationally Critical Threat, Asset, and Vulnerability Evaluation methodology. OCTAVE was developed by Carnegie Mellon University's Software Engineering Institute and is now maintained by CERT.

[PAUSE — 2 seconds]

OCTAVE was designed specifically for organizations that need to conduct risk assessments with internal teams rather than bringing in expensive external consultants. It is a self-directed methodology, meaning the people who know the organization best — its own staff — lead the assessment.

[SHOW SLIDE 12 — OCTAVE Three Phases]

OCTAVE exists in three versions: the original OCTAVE for large organizations, OCTAVE-S for small organizations, and OCTAVE Allegro, which focuses specifically on information assets.

All versions share a three-phase structure.

**Phase 1: Build Asset-Based Threat Profiles.** The team identifies the organization's critical assets — not just IT systems, but information assets that matter to the mission. For each asset, the team identifies threats to that asset, security requirements for protecting it, and current organizational practices around it.

[PAUSE — 2 seconds]

**Phase 2: Identify Infrastructure Vulnerabilities.** The team examines the technical infrastructure that supports critical assets, identifying technical vulnerabilities that could be exploited.

**Phase 3: Develop Security Strategy and Plans.** The team brings together findings from the first two phases to evaluate risks and develop a practical, action-oriented risk mitigation strategy.

[SHOW SLIDE 13 — OCTAVE Distinguishing Features]

What distinguishes OCTAVE from the other frameworks is its emphasis on organizational and people-centered risk alongside technical risk. OCTAVE explicitly considers human vulnerabilities — untrained staff, poor processes, cultural norms — as risk factors on par with unpatched software.

For the CISM exam, OCTAVE is the answer when the question involves an internal team conducting a risk assessment with limited budget, or when the focus is on operationally critical assets and business context rather than compliance checklists.

[PAUSE — 3 seconds]

---

## Part 4 — FAIR Model (4 minutes)

[SHOW SLIDE 14 — FAIR Overview]

Our fourth framework is FAIR — Factor Analysis of Information Risk. FAIR was developed by Jack Jones and is now maintained by the FAIR Institute. It represents a fundamentally different approach from the three frameworks we have already covered.

[PAUSE — 2 seconds]

NIST RMF, ISO 31000, and OCTAVE all produce risk ratings in qualitative terms — high, medium, low — or in ordinal scales. FAIR produces dollar estimates of risk. It answers the question: how much money does this risk cost the organization?

[SHOW SLIDE 15 — FAIR Ontology]

FAIR is built on a precise ontology — a defined vocabulary for decomposing risk into measurable components. At the top level, FAIR defines risk as the probable frequency and probable magnitude of future loss.

Frequency is decomposed into Threat Event Frequency — how often does a threat agent act against an asset — and Vulnerability — how likely is the threat to succeed when it acts.

Magnitude is decomposed into Primary Loss — direct financial impact — and Secondary Loss — reputational damage, regulatory fines, and other downstream costs.

[PAUSE — 2 seconds]

[SHOW SLIDE 16 — FAIR in Practice]

In practice, FAIR analysts use probability distributions to model uncertainty in each factor. Monte Carlo simulation then produces a range of probable annual loss expressed in dollars.

This quantitative output is extremely powerful for business communication. When a CISO tells the board "this vulnerability represents between two million and eight million dollars in expected annual loss," leadership can make a truly informed investment decision about whether to spend four hundred thousand dollars on a control.

[SHOW SLIDE 17 — Framework Comparison Summary]

Let me give you a comparison to anchor all four frameworks together.

NIST RMF: U.S. federal focus, system lifecycle, prescriptive controls, compliance-driven.

ISO 31000: International, enterprise-wide, principles-based, strategy-driven.

OCTAVE: Self-directed, asset-centric, operationally focused, budget-friendly.

FAIR: Quantitative, financial output, board communication, investment decisions.

For the CISM exam, know that no single framework is universally best. The right choice depends on the organization's regulatory environment, available resources, audience for the risk output, and maturity level.

[PAUSE — 3 seconds]

---

## Summary and Closing (2 minutes)

[SHOW SLIDE 18 — Module 03 Summary]

Let's bring everything together.

This module covered four major risk management frameworks, each with a distinct philosophy and use case.

The NIST Risk Management Framework provides a seven-step, system-lifecycle approach that is mandatory for federal systems and widely adopted in regulated industries. Its continuous monitoring requirement is a key differentiator.

ISO 31000 gives us a universally applicable, principles-based approach that integrates risk management into organizational strategy and governance at the enterprise level.

OCTAVE empowers internal teams to conduct asset-based, operationally focused risk assessments without requiring deep technical expertise or significant budget.

FAIR gives us the language and mathematics to express cybersecurity risk in financial terms, enabling more effective executive communication and prioritized investment decisions.

[PAUSE — 2 seconds]

For your CISM exam preparation, pay particular attention to scenarios that ask which framework is most appropriate for a given situation. The answer almost always depends on the context: regulatory environment, organization size, available expertise, and the intended audience for the risk output.

Your lab this week will ask you to apply OCTAVE Allegro to a realistic scenario, and your reading guide expands on all four frameworks with additional depth.

I will see you in Module 4, where we move from frameworks to specific risk assessment and analysis techniques.

[PAUSE — 2 seconds]

Take care, and keep asking great questions.

---

*End of Module 03 Video Script*

*Total estimated runtime: 22 minutes*
