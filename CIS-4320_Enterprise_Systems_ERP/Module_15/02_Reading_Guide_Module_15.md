# Reading Guide: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

This reading guide covers the structured methodologies used to plan, execute, and close enterprise ERP implementations. You will examine SAP's ASAP framework in depth, walk through the Salesforce implementation lifecycle phase by phase, and study the three practices that most frequently determine whether a go-live succeeds or fails: change management, cutover planning, and hypercare.

**Estimated Reading Time:** 95–115 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name and describe each phase of the SAP ASAP methodology and its key deliverables.
2. Name and describe each phase of the Salesforce implementation lifecycle.
3. Explain the purpose of a Business Blueprint and a fit-gap analysis in an SAP implementation.
4. Distinguish between big bang and phased cutover strategies and identify appropriate use cases for each.
5. Describe the core activities and objectives of the hypercare period.
6. Explain the role of change management in ERP adoption and identify the key components of a change management plan.
7. Identify the most common causes of ERP implementation failure and connect them to specific methodology gaps.

---

## Section 1 — Why Methodology Matters

### 1.1 The Cost of Implementation Failure

ERP implementations are among the most expensive and organizationally complex technology projects an enterprise undertakes. Scope typically spans multiple business functions, affects hundreds or thousands of users, involves replacing systems that have been in place for decades, and requires data migration from multiple legacy sources.

When implementations fail or significantly underperform, the consequences are severe: project cost overruns (often 50–100% above original budget), schedule delays, operational disruptions at go-live, user rejection of the new system, and in extreme cases, material financial harm to the organization.

The Gartner and McKinsey research on ERP project outcomes consistently shows that the primary causes of failure are not technical — they are methodological and organizational. Projects fail when scope is not controlled, when testing is compressed, when training is inadequate, or when change management is absent. Methodology provides the structure that prevents these failures.

### 1.2 What a Good Methodology Provides

A good implementation methodology provides:

- A defined sequence of activities so nothing critical is skipped
- Clear deliverable definitions so the team knows what "done" means for each phase
- Phase gates — formal checkpoints where a go/no-go decision is made before proceeding
- Roles and responsibilities so accountability is clear
- Risk management frameworks for identifying and mitigating implementation risks
- Templates and accelerators (pre-built configuration tools, questionnaires, test scripts) that reduce rework

Both ASAP and the Salesforce lifecycle provide all of these elements. They differ in structure because SAP implementations are typically larger, more complex, and more configuration-intensive than Salesforce CRM implementations — but the underlying principles are the same.

---

## Section 2 — SAP ASAP Methodology

### 2.1 Phase 1 — Project Preparation

Project Preparation establishes the foundation for the entire implementation. The primary activities are:

- **Scope definition** — documenting which SAP modules will be implemented (FI/CO, MM, SD, HR, etc.), which business processes are in scope, and which are explicitly excluded
- **Project team staffing** — identifying and committing business process owners (subject matter experts from each functional area), key users (who will become the internal experts and trainers), IT resources, and the implementation partner team
- **System landscape setup** — provisioning the three-system landscape: Development (DEV), Quality Assurance (QAS), and Production (PRD)
- **Project governance** — establishing the steering committee, escalation paths, decision-making authority, and change control procedures
- **Initial project plan** — timeline, milestones, resource plan, and budget baseline

The critical output is a signed Project Charter. The phrase "signed" is important — verbal agreement on scope is not scope. Scope is what is written down and agreed to by the project sponsor and key stakeholders.

### 2.2 Phase 2 — Business Blueprint

Business Blueprint is the most intellectually intensive phase of an SAP implementation. It is where the organization's business requirements are mapped to SAP's capabilities.

The mechanism is structured workshops — one for each business process area. In a Finance implementation, workshops cover: general ledger configuration, accounts payable, accounts receivable, asset accounting, cost center accounting, and profit center accounting. Each workshop follows the same pattern:

1. Current state documentation — how the process works today
2. Future state design — how the process should work in SAP
3. Fit-gap analysis — where SAP's standard functionality matches the requirement (fit) and where it does not (gap)

The fit-gap log is the most important artifact of the Business Blueprint phase. Every gap must be resolved through one of three approaches:

- **Configuration** — SAP provides enough flexibility through standard configuration options to meet the requirement
- **Custom development** — the requirement cannot be met through configuration alone; ABAP code must be written
- **Process change** — the business agrees to change its process to match how SAP works, avoiding custom development

Custom development should be minimized. Every ABAP customization increases implementation cost, complicates future upgrades, and creates a maintenance burden. The best practice guidance is to follow SAP's standard processes unless there is a compelling competitive reason to deviate.

The Business Blueprint document — sometimes hundreds of pages — is formally approved by business process owners and the project sponsor before the Realization phase begins.

### 2.3 Phase 3 — Realization

Realization is where configuration and development occur. It is typically the longest phase. The work is organized into two sub-phases:

**Baseline configuration (Cycle 1):** The technical team configures the core system settings — company code, chart of accounts, plant structure, sales organization, purchasing organization. This establishes the skeleton on which all other configuration is layered.

**Final configuration (Cycle 2):** Detailed configuration based on all Business Blueprint decisions. Each requirement from the fit-gap log is addressed. Custom ABAP development is built and unit-tested. Data migration programs are developed and tested with sample legacy data.

Integration testing runs throughout Realization. Integration testing verifies that end-to-end business processes work correctly across modules. A procure-to-pay integration test follows a purchase requisition from creation through purchase order, goods receipt, invoice verification, and vendor payment — exercising FI, MM, and SD simultaneously.

The Realization phase ends with a formal sign-off that all configuration is complete, all development is unit-tested, and integration testing has been completed to an acceptable level.

### 2.4 Phase 4 — Final Preparation

Final Preparation is the last phase before go-live. It runs four to eight weeks before the planned go-live date and includes:

**End-user training:** Every user who will work in SAP is trained on their specific role. Training is role-based — an accounts payable clerk does not sit through a session on cost center accounting. Training uses a training client (a separate SAP client with realistic data) so users can practice without affecting any real data. Training completion rates are tracked and reported to the steering committee.

**User Acceptance Testing (UAT):** Business users run through their actual workflows in the QAS system and formally sign off that the system meets requirements. UAT is not IT testing — it is business testing. If the business does not sign off, you do not go live.

**Cutover planning and rehearsal:** The cutover plan is documented in detail (task by task, with owner, estimated duration, and dependency) and rehearsed at least twice before the real cutover. Rehearsal reveals timing problems and sequencing errors that would be catastrophic if discovered during the actual cutover weekend.

**Go/no-go criteria:** The project defines specific, measurable criteria that must be met before go-live authorization is granted: training completion above X%, all P1 test defects resolved, cutover rehearsal completed successfully, data migration acceptance rate above Y%, and executive sponsor sign-off.

### 2.5 Phase 5 — Go-Live and Support

Go-Live and Support is the final ASAP phase. The cutover happens, the system goes live, and the project transitions to operational support. The hypercare period (covered in Section 5) runs during this phase. After hypercare, the formal project is closed and ongoing support transfers to the internal IT support organization.

---

## Section 3 — Salesforce Implementation Lifecycle

### 3.1 Discover

Discover is the initial requirements-gathering phase. The implementing team conducts stakeholder interviews, process observations, and document reviews to understand:

- The business problems being solved
- The current-state processes and their pain points
- The desired future-state capabilities
- Integration requirements with other systems
- Data migration scope and quality
- User personas and adoption challenges

The output is a requirements register and a prioritized feature list. In agile-influenced Salesforce implementations, requirements are often expressed as user stories: "As a sales rep, I want to see all of my open opportunities on a single dashboard so that I can prioritize my day."

### 3.2 Define

Define translates requirements into architectural decisions. The team produces a Solution Design Document covering:

- **Object model** — which standard Salesforce objects will be used, which custom objects are needed, what the relationships between objects are
- **Security model** — OWD settings, role hierarchy design, profiles and permission sets, sharing rules
- **Automation model** — which processes will be automated via Flow, which require Apex, which are handled via Process Builder (legacy) or Approval Processes
- **Integration design** — how Salesforce will connect to external systems (ERP, marketing automation, data warehouse), which integration patterns will be used (real-time API, batch file, middleware)
- **Data migration approach** — what data will be migrated from legacy systems, how it will be mapped, what quality standards apply

### 3.3 Design

Design produces detailed specifications for each configured element. Where Define answers "what" and "why," Design answers "exactly how." Typical Design outputs include:

- Field specifications (API name, data type, validation rules, help text)
- Page layout designs (which fields appear in which sections, which related lists are included)
- Flow diagrams (element-by-element logic for each automated process)
- Report type specifications
- Integration message schemas

Design is often done in a sandbox to show stakeholders a working prototype before committing to the approach.

### 3.4 Build

Build is the configuration and development sprint. Salesforce Administrators configure declarative features. Salesforce Developers write Apex, build LWC components, and create integrations. Data migration developers build import files and test loads.

In larger implementations, Build runs in multiple sprints (agile methodology), delivering working functionality incrementally for stakeholder review rather than waiting until everything is built before showing the business anything.

### 3.5 Test

Test verifies that the built system meets requirements. The testing sequence follows a pyramid:

- **Unit tests** — individual components verified by developers
- **System integration tests** — end-to-end process tests run by the QA team
- **User Acceptance Tests** — business users execute test scripts covering their workflows and formally sign off
- **Performance/load tests** — verify system response times under expected concurrent user load

Defects discovered in testing are tracked in a defect log with severity ratings. Critical defects (P1 — system cannot perform a core function) must be resolved before UAT sign-off. High defects (P2 — significant workaround required) must be resolved before go-live authorization. Medium and low defects may be deferred to a subsequent release.

### 3.6 Deploy

Deploy moves the validated configuration from sandbox to production. Salesforce deployment mechanisms:

- **Change Sets** — the standard tool for moving metadata between orgs; suitable for most declarative changes
- **Salesforce CLI and DX** — command-line deployment of version-controlled metadata packages; required for complex development pipelines
- **Managed/Unmanaged Packages** — for deploying ISV applications or reusable component libraries

Post-deployment smoke testing verifies that critical functions work in production. Hypercare begins immediately after a successful smoke test.

---

## Section 4 — Change Management

### 4.1 The Human Side of ERP

Research by Prosci (the leading change management research organization) consistently finds that projects with excellent change management are six times more likely to meet objectives than projects with poor change management. The technical implementation of an ERP system is often the easier half of the project. The harder half is getting hundreds or thousands of people to actually use it correctly.

### 4.2 Stakeholder Analysis

Stakeholder analysis identifies all groups affected by the ERP implementation and assesses their current state (awareness, understanding, support level) and desired end state (active users, passive supporters). Common stakeholder segments in an ERP implementation:

- Executive leadership — need to understand ROI and strategic benefit; are the visible champions
- Functional managers — need to understand how their team's processes change; often the most influential resistors or advocates
- End users — need role-based training and clear answers to "what does this mean for my job"
- IT staff — need technical training and clarity on ongoing support responsibilities
- External parties (customers, suppliers) — if the ERP change affects how they interact with the organization, they need advance notice and communication

### 4.3 Communication Planning

A change management communication plan answers five questions for every message:

1. What is the message?
2. Who is the audience?
3. Who delivers it (sender)?
4. When and how often?
5. Through what channel (email, all-hands meeting, team meeting, intranet)?

The most effective communications in ERP projects come from senior leaders, not project managers. When the CFO emails the finance team to say "I am personally committed to this implementation and I expect everyone to complete their training by October 15," compliance goes up. When the project manager sends the same message, it is easier to ignore.

### 4.4 Training Strategy

Training for ERP implementations should be:

- **Role-based** — each user receives training only on the transactions and processes relevant to their job
- **Hands-on** — users practice in a training environment, not just watch demonstrations
- **Just-in-time** — delivered close enough to go-live that users remember it, but early enough that they have time to ask questions and practice
- **Supported** — job aids (step-by-step reference cards), quick reference guides, and a help desk for post-go-live questions

Training conducted too far before go-live produces users who have forgotten what they learned by the time they need it. Training conducted the week before go-live produces anxiety, not competence.

### 4.5 Resistance Management

Resistance to ERP implementations is normal and expected. Common sources of resistance include:

- Fear of job loss (will this system eliminate my position?)
- Fear of incompetence (what if I cannot learn the new system?)
- Loss of familiar processes (I have done it this way for 15 years)
- Distrust of management (this is the third "transformation" in five years)
- Legitimate concerns about the system (the new process is genuinely worse for my role)

Effective resistance management acknowledges the resistance, investigates its root cause, and addresses it directly. Ignoring resistance allows it to become organized opposition.

---

## Section 5 — Cutover Planning

### 5.1 Cutover Strategy Selection

The cutover strategy determines how the organization transitions from legacy systems to the new ERP.

**Big bang:** The entire organization transitions at once. The legacy system is decommissioned on cutover weekend, and everyone begins using the ERP on Monday. Advantages: single cutover event, no need to run parallel systems, simpler reconciliation. Disadvantages: maximum organizational risk concentrated in one event.

**Phased/Wave:** The organization transitions in defined waves — by geography, business unit, or process module. Advantages: lower risk per wave, lessons from early waves improve later ones, smaller training population per wave. Disadvantages: parallel operations are expensive and complex, transactions may need to be recorded in both systems during transition.

**Parallel run:** Both the legacy system and the new ERP run simultaneously for a defined period. Users enter transactions in both systems, and outputs are reconciled. Advantages: highest confidence in ERP accuracy before full cutover. Disadvantages: extremely resource-intensive — users are doing double the work, reconciliation is complex, it is difficult to terminate the legacy system when parallel run becomes comfortable.

### 5.2 Cutover Plan Content

A detailed cutover plan documents every task required to transition from legacy to production ERP. Each task entry includes:

- Task description
- Responsible owner (named individual, not a role)
- Estimated duration
- Start dependency (what must be completed before this task can begin)
- Go/no-go checkpoint (tasks that, if they fail, trigger the decision to abort cutover)
- Rollback procedure (how to reverse the task if cutover is aborted)

Critical path analysis identifies which tasks, if delayed, will delay the entire cutover. These tasks receive additional contingency time and monitoring.

### 5.3 Data Migration in Cutover

Data migration is typically the most time-consuming and risk-prone element of cutover. Legacy data must be extracted, cleaned, transformed to match ERP data structures, and loaded in the correct sequence (master data before transactional data). Data migration must be tested at least twice before the production run to validate timing and acceptance rates.

Acceptance criteria for data migration define the minimum data completeness and accuracy required to proceed with go-live. If the migration produces an acceptance rate below the defined threshold, cutover is halted and the migration is corrected.

---

## Section 6 — Hypercare

### 6.1 Hypercare Objectives

Hypercare is the intensive support period immediately following go-live. Its objectives are to:

- Stabilize the system rapidly by resolving production issues with maximum speed
- Support users through the first weeks on the new system when error rates and confusion are highest
- Monitor system performance and transaction integrity
- Build user confidence and adoption

### 6.2 Hypercare Structure

During hypercare, the project team remains fully engaged. Key structural elements:

- **War room** (physical or virtual) — central coordination point for all issue management
- **Daily stand-up calls** — brief (15–30 minute) meetings each morning to review open issues, overnight events, and planned activities
- **Issue triage process** — incoming issues are classified by severity and routed to the correct resolver within defined SLA windows
- **Escalation path** — critical issues that cannot be resolved within the SLA window escalate immediately to the project manager and sponsor
- **Go-live metrics dashboard** — tracks help desk ticket volume, P1/P2 issue counts, transaction error rates, and user adoption metrics daily

### 6.3 Hypercare Exit Criteria

Hypercare ends when defined stability criteria are met, typically:

- No open P1 (critical) issues
- P2 issue backlog below a defined threshold
- Help desk ticket volume declining week over week and approaching normal baseline
- System performance within defined response time targets
- User adoption metrics (login rates, transaction completion rates) at or above target

When exit criteria are met, the project formally transitions to run-and-maintain operations, with standard IT support replacing the hypercare war room.

---

## Key Terms

- **ASAP** — Accelerated SAP; SAP's structured ERP implementation methodology
- **Business Blueprint** — Phase 2 of ASAP; documents how business processes will be configured in SAP
- **Fit-Gap Analysis** — comparison of business requirements to SAP standard functionality; identifies gaps requiring configuration, development, or process change
- **Realization** — Phase 3 of ASAP; configuration, development, and integration testing
- **Final Preparation** — Phase 4 of ASAP; end-user training, UAT, and cutover rehearsal
- **Go/No-Go Decision** — formal phase gate decision whether to proceed to the next phase or go-live
- **Discover** — Phase 1 of the Salesforce lifecycle; requirements gathering and scoping
- **Define** — Phase 2 of the Salesforce lifecycle; architectural and solution design
- **User Acceptance Testing (UAT)** — business-driven testing that formally validates the system meets requirements
- **Change Management** — the discipline of managing the human side of organizational change
- **Stakeholder Analysis** — systematic identification of affected groups and their readiness for change
- **Big Bang Cutover** — single-event transition from legacy to ERP for the entire organization
- **Phased Cutover** — transition in waves by geography, business unit, or process area
- **Parallel Run** — operating both legacy and new systems simultaneously during transition
- **Cutover Plan** — detailed task-by-task plan for transitioning to production ERP
- **Hypercare** — intensive post-go-live support period with elevated staffing and rapid issue response
- **Hypercare Exit Criteria** — defined stability thresholds that mark the end of the hypercare period

---

## Review Questions

1. What is the purpose of the Business Blueprint phase in ASAP, and what is the key output?

2. Describe the three options available to resolve a gap identified during fit-gap analysis. Which option should be minimized, and why?

3. What is the difference between integration testing and user acceptance testing? Why are both necessary?

4. Describe the six phases of the Salesforce implementation lifecycle in sequence, and identify the primary output of each phase.

5. What is the go/no-go decision, and at what points in an ERP implementation should it be applied?

6. A company is implementing SAP S/4HANA across 14 countries simultaneously. What cutover strategy would you recommend, and why?

7. Why is executive sponsorship identified as the most reliable predictor of ERP implementation success?

8. Describe three sources of user resistance to ERP implementations and an appropriate management response for each.

9. What are the components of a hypercare war room, and what metrics should be tracked during hypercare?

10. The Hershey Foods implementation failure in 1999 is discussed in the module. Identify three specific methodology failures that contributed to the outcome.

---

## Pre-Lab Preparation

Before attending Lab 15, complete the following:

- Review Trailhead module "Salesforce Implementation Basics" (trailhead.salesforce.com — search "Implementation Basics")
- Read the SAP ASAP methodology overview at help.sap.com (search "ASAP Methodology")
- Prepare a brief (one-paragraph) description of a fictional company you will use as the subject of your Lab 15 implementation plan — include industry, size (number of employees), current systems, and ERP implementation goal

---

---

## 9. Supplemental Resources

**1. Prosci — ADKAR Change Management Model**
<https://www.prosci.com/methodology/adkar>
Prosci's official ADKAR model resource covers each element (Awareness, Desire, Knowledge, Ability, Reinforcement) with diagnostic tools for identifying change resistance and interventions for each gap type. Directly relevant to the change management content in this module and the adoption failure scenarios covered in Lab 15.

**2. SAP Learning — SAP Activate Methodology**
<https://learning.sap.com/learning-journeys/discover-sap-activate>
Official SAP learning journey for SAP Activate — the current SAP S/4HANA implementation methodology that replaced ASAP. Covers the Prepare, Explore, Realize, Deploy, and Run phases, Fit-to-Standard workshop approach, and agile sprint planning within the methodology framework tested in this module's quiz.

**3. Salesforce Trailhead — Salesforce Implementation Basics**
<https://trailhead.salesforce.com/content/learn/modules/salesforce-implementation-basics>
Official Salesforce module covering the Discover, Define, Design, Build, Test, and Deploy phases of the Salesforce implementation lifecycle. Maps directly to the Salesforce methodology content in Section 2 of this Reading Guide and the phase deliverables tested in Quiz 15.

*End of Reading Guide — Module 15*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials
