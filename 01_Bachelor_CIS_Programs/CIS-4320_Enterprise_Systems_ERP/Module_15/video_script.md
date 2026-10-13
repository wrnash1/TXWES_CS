# Video Script: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Production Notes

**Duration:** Approximately 25–30 minutes
**Format:** Lecture with slide transitions and case study references
**Segments:** 6 segments with natural pause points

---

## Segment 1: Introduction — Why Methodology Matters (Lines 1–40)

[SLIDE: Title card — "Module 15: ERP Implementation Methodology"]

Welcome to Module 15. I am Professor Nash. Today we shift from how ERP systems work to how ERP projects get done — and sometimes, how they fail. Implementation methodology is the structured approach that guides an ERP project from initial planning through go-live and beyond. Without a methodology, an ERP project is a multi-million-dollar improvisation.

[SLIDE: ERP failure statistics]

The track record of large ERP implementations is sobering. Studies over the past two decades consistently find that 50 to 75 percent of ERP implementations experience significant overruns in cost or schedule, and 20 to 30 percent are classified as failures — meaning the organization either abandoned the project, reverted to the old system, or achieved so little of the planned benefit that the investment was not justified.

What causes these failures? The top factors, according to post-mortem analyses, are: poor scope management (the project kept growing), inadequate change management (people resisted the new system), insufficient testing, poor data quality going into the new system, and unrealistic timelines.

[SLIDE: The role of methodology]

A structured methodology does not guarantee success, but it dramatically reduces the probability of the most common failure modes. A methodology provides a sequence of activities, defined deliverables at each phase, roles and responsibilities, risk management practices, and quality gates — checkpoints where the project must prove it is ready to proceed.

[SLIDE: Learning objectives]

Today we cover four areas: the SAP ASAP methodology and its modern evolution; the Salesforce implementation lifecycle and Salesforce's recommended delivery approach; change management as a discipline; and cutover planning, hypercare, and total cost of ownership.

[PAUSE]

---

## Segment 2: SAP ASAP Methodology (Lines 41–85)

[SLIDE: ASAP — Accelerated SAP]

ASAP stands for Accelerated SAP. It was developed by SAP in the mid-1990s as a structured implementation methodology that combined proven project management practices with SAP-specific content, including pre-built configuration templates, test scripts, and training materials.

ASAP has evolved over the years. The current SAP framework for S/4HANA implementations is called SAP Activate, but ASAP's phase structure remains foundational knowledge for any SAP professional, and the Activate methodology builds directly on ASAP concepts. The certification exam tests ASAP terminology, so let me walk through the phases.

[SLIDE: Phase 1 — Project Preparation]

Phase 1 is Project Preparation. The objective is to establish the organizational foundation for the project. Deliverables include: the project charter, the project organization chart (who is the executive sponsor? who is the project manager? what functional teams are involved?), the project schedule, the technical infrastructure plan, and the initial scope definition.

A critical output of Phase 1 is the identification of the SAP system landscape: development system, quality/test system, and production system. No project proceeds without these three environments.

[SLIDE: Phase 2 — Business Blueprint]

Phase 2 is Business Blueprint. This is where the team documents the to-be business processes. SAP's pre-built process documentation — the Question & Answer database (Q&A DB) — guides consultants through a structured set of questions for each functional area: How does your accounts payable process work? How many company codes do you have? How do you handle intercompany transactions?

The output is the Business Blueprint document — a detailed specification of how the organization's processes will be implemented in SAP. This document becomes the contract between the business and the implementation team. Changes to the blueprint after approval require formal change control.

[SLIDE: Phase 3 — Realization]

Phase 3 is Realization, which is the configuration and build phase. The project team configures SAP using the SPRO (SAP Project Reference Object) customizing framework. ABAP developers build any required enhancements. Interfaces to other systems are developed. Data migration programs are coded.

Realization is divided into two cycles: Baseline Configuration (core processes configured first and validated with key users) and Final Configuration (remaining processes configured, integration tested, performance tested).

[SLIDE: Phase 4 — Final Preparation]

Phase 4 is Final Preparation. The focus shifts from building to validating and preparing for go-live. Activities include: end-user training, system performance testing and tuning, final data migration rehearsals, help desk setup, and the Go/No-Go decision meeting.

The Go/No-Go decision is a formal gate. The project team presents evidence — testing completion percentages, open issues count, data migration readiness, training completion rates — and the executive sponsor makes a documented decision to proceed or delay.

[SLIDE: Phase 5 — Go-Live and Support]

Phase 5 is Go-Live and Support. The production system goes live. The cutover plan (detailed in a later slide) is executed. The hypercare period begins — an intensive post-go-live support phase where consultants and the project team remain available to resolve issues quickly as real users encounter the new system for the first time.

After hypercare, the project transitions to a steady-state support model: typically the company's own support team or a managed services provider.

[SLIDE: SAP Activate — the modern evolution]

SAP Activate is SAP's current delivery methodology for S/4HANA. It introduces an Agile approach organized into sprints, with a focus on "fit-to-standard" — meaning organizations are encouraged to adopt SAP's standard best-practice processes rather than customizing extensively. SAP Activate includes three phases: Prepare (like ASAP Project Preparation), Explore (like Business Blueprint, but shorter), and Realize (multiple agile sprints). It also adds Discover — a pre-project phase where customers use SAP Best Practices and a trial system to validate scope.

[PAUSE — transition to Salesforce]

---

## Segment 3: Salesforce Implementation Lifecycle (Lines 86–125)

[SLIDE: Salesforce implementation overview]

Salesforce implementations are generally faster and less technically complex than SAP implementations, but they involve the same fundamental phases: plan, build, test, and go-live. The Salesforce ecosystem has produced several competing methodologies — Salesforce's own guidance, Agile Scrum frameworks, and hybrid approaches.

Salesforce's recommended methodology is formalized through the Salesforce Implementation Lifecycle and the concepts behind Salesforce certifications for architects and consultants.

[SLIDE: Discovery and Requirements]

Every Salesforce implementation begins with Discovery — understanding the business problem to be solved, the current state, and the desired future state. Discovery involves: stakeholder interviews, process mapping, data model assessment, and requirements documentation.

A common failure in Salesforce projects is skipping thorough discovery and jumping directly to configuration. The result is a configured system that does not match the actual business requirements.

[SLIDE: Design and Architecture]

The Design phase translates business requirements into a technical architecture. Decisions made here include: what objects and fields are needed, what the security model will look like (profiles, OWD, sharing rules), what automation will be used (flows, process builders, validation rules), and what integrations are required.

The output is a Solution Design Document (SDD) or Technical Design Document (TDD). Like SAP's Business Blueprint, this document is the contract between business and implementation team.

[SLIDE: Build and Configuration]

Configuration is done in a developer or sandbox environment — never in production. Salesforce has several environment types: Developer sandboxes (small, free, for individual development), Full sandboxes (exact copy of production data and metadata, most expensive), Partial sandboxes (a percentage of production data), and Developer Pro sandboxes (slightly larger than Developer).

Changes are deployed from sandbox to production using Salesforce's change management tools: Change Sets, Salesforce DX (source-driven development), and third-party CI/CD tools.

[SLIDE: Testing phases]

Testing in Salesforce follows three phases.

**Unit Testing:** individual components tested by developers.

**User Acceptance Testing (UAT):** business users validate that the configured system matches their requirements. UAT is critical — it is the users' last chance to identify gaps before go-live.

**Regression Testing:** ensures that new changes do not break existing functionality. Particularly important when adding new features to a system already in use.

[SLIDE: Salesforce DevOps and source control]

Modern Salesforce development uses Salesforce DX (Developer Experience), which treats Salesforce metadata as source code stored in a version control system like Git. This enables true CI/CD pipelines — automated testing and deployment pipelines that run every time code is committed.

This is the direction the Salesforce ecosystem is moving: away from manual change sets, toward professional software development practices applied to Salesforce configuration.

[PAUSE — transition to change management]

---

## Segment 4: Change Management (Lines 126–165)

[SLIDE: Why technology is the easy part]

Here is a truth that experienced ERP practitioners know but rarely admit up front: the technology is almost never the hardest part of an ERP implementation. The hardest part is getting people to change how they work.

Change management is the structured process of preparing, supporting, and helping individuals through a transition. It addresses the human side of change — why people resist, how to build buy-in, and how to minimize productivity loss during the transition.

[SLIDE: Prosci ADKAR Model]

The most widely used change management framework in ERP projects is Prosci's ADKAR model. ADKAR is an acronym:

**A — Awareness:** people understand why the change is necessary.

**D — Desire:** people want to participate in the change.

**K — Knowledge:** people know how to change — they have been trained.

**A — Ability:** people are able to perform the new behaviors and use the new system.

**R — Reinforcement:** the change is sustained over time; people do not revert.

Change management activities must address each of these stages. Training alone addresses only the K — Knowledge stage. Without Awareness and Desire, people will sit through training and then ignore what they learned.

[SLIDE: Resistance to ERP change]

The most common sources of resistance in ERP implementations are:

Fear of job loss: employees worry that the new system will automate their role.

Loss of control: experienced users who were experts in the old system become novices in the new one.

Distrust: employees do not believe the project will succeed or that management is committed.

Information overload: employees are given too much information too late.

Each of these resistance sources requires a different intervention. Fear of job loss requires transparent communication about the impact on roles. Loss of control requires early involvement of power users in testing and design.

[SLIDE: Communication planning]

A structured communication plan maps what messages will be delivered, by whom, to which audience, and on what schedule. General principles:

Executives should communicate why — the strategic rationale and commitment.

Middle managers should communicate what it means for the team — how their day-to-day work will change.

Project team members should communicate how — the mechanics of the new system.

Early, honest, and frequent communication reduces anxiety more effectively than a single big announcement.

[SLIDE: Training strategy]

Effective ERP training addresses three dimensions: knowledge (conceptual understanding of the system), skills (hands-on proficiency in specific transactions), and role-specific context (how does this system relate to my specific job?).

Just-in-time training — delivered close to go-live rather than weeks before — produces better retention. Blended approaches that combine classroom training, job aids (quick reference cards), and system simulations work better than lecture-only formats.

[PAUSE]

---

## Segment 5: Cutover, Hypercare, and TCO (Lines 166–208)

[SLIDE: Cutover planning]

The cutover is the moment when the old system is turned off and the new system goes live. For large ERP systems, this is one of the most stressful periods in the entire project. A poorly planned cutover can leave a company unable to process orders, make payments, or track inventory for days or weeks.

A cutover plan is a detailed, sequenced list of every task that must be completed before, during, and after the go-live event. It includes: tasks, owners, estimated duration, dependencies, and rollback criteria.

[SLIDE: Cutover elements]

Key elements of a cutover plan:

**Data migration:** final extraction of data from the legacy system, transformation, and load into the new system. Must be rehearsed multiple times — typically two or three dress rehearsals — to confirm the migration runs within the cutover window.

**Interface cutovers:** switches external systems from the old API endpoints to the new ones. Timed carefully to minimize dual-running complexity.

**User provisioning:** all user accounts created, roles assigned, and access tested before go-live.

**Communication:** stakeholders notified of system downtime windows and go-live confirmation.

**Rollback plan:** if something goes wrong and the new system cannot go live, how long can the business tolerate downtime, and what is the procedure to revert to the old system? Every cutover plan must include an explicitly defined rollback decision point and procedure.

[SLIDE: Hypercare]

Hypercare is the post-go-live intensive support period, typically lasting two to four weeks. During hypercare:

All consultants and project team members are available for rapid issue resolution.

A war room is established — a central coordination point for tracking and resolving issues.

Issues are triaged into severity levels: critical (system down or major process blocked), high (significant workaround needed), medium (workaround available), and low (cosmetic or minor).

The hypercare period ends when the system is stable and the support team has demonstrated they can handle the issue volume independently.

[SLIDE: Total Cost of Ownership (TCO)]

TCO is the complete cost of an ERP system over its useful life — not just the initial implementation cost. ERP decision-makers frequently underestimate TCO because they focus on the vendor license fee and the implementation services invoice.

TCO components for Salesforce:

- License fees (annual subscription, per user)
- Implementation services (consultants, internal staff)
- Integration development and maintenance
- Customization maintenance across Salesforce releases
- Training (initial and ongoing)
- System administration (internal admin salary or managed services)
- AppExchange third-party app subscriptions
- Data storage overage fees

TCO components for SAP S/4HANA:

- License fees (perpetual license or cloud subscription)
- Implementation services
- SAP Basis / infrastructure (hardware for on-premises, or cloud hosting)
- Annual maintenance fee (22% of license per year for on-premises)
- Upgrade projects (major version upgrades every several years)
- Custom ABAP code maintenance
- Consulting support for system changes

For both platforms: a three-to-five-year TCO model is standard for executive decision-making. The implementation cost is often 3–5 times the first-year license cost.

[PAUSE]

---

## Segment 6: Summary and Certification Preparation (Lines 209–240)

[SLIDE: Methodology comparison]

Let me compare the two methodologies side by side.

ASAP/SAP Activate is a heavyweight methodology designed for large, complex, multi-module SAP implementations. Projects typically run 12 to 36 months for a full S/4HANA implementation. The Business Blueprint/Explore phase is extensive, reflecting the configuration depth of SAP.

Salesforce implementations can be much faster — an initial Sales Cloud go-live can be achieved in 8 to 12 weeks for a focused scope. The platform's configuration-over-code design philosophy and the abundance of AppExchange pre-built solutions reduce build time significantly.

Both methodologies emphasize: thorough discovery, documented requirements, disciplined change management, structured testing, and planned cutover.

[SLIDE: Common implementation failure modes]

Knowing the failure modes is as important as knowing the methodology. The top five causes of ERP implementation failure:

Scope creep: requirements that were not in the original scope are added mid-project.

Inadequate executive sponsorship: without visible, sustained executive commitment, resistance wins.

Poor data quality: the migration fails or loads dirty data, undermining confidence in the new system.

Underestimating change management: the technology works; the people do not adopt it.

Insufficient testing: defects discovered in production are much more expensive to fix than defects discovered in UAT.

[SLIDE: Certification exam tips]

SAP essentials exam: know the five ASAP phases (Project Preparation, Business Blueprint, Realization, Final Preparation, Go-Live and Support), know what each phase produces, and know what SAP Activate is.

Salesforce Admin exam: while implementation lifecycle is less directly tested, understanding sandbox types, change sets, and the distinction between development and production environments appears in exam scenarios.

[SLIDE: Key terms]

ASAP: Accelerated SAP — SAP's classic implementation methodology.

SAP Activate: SAP's current Agile implementation methodology for S/4HANA.

Business Blueprint: Phase 2 of ASAP — the documented to-be process design.

SPRO: SAP Project Reference Object — the customizing framework used during Realization.

Sandbox (Salesforce): a copy of the production environment used for development and testing.

Go/No-Go: the formal decision gate before production go-live.

Cutover Plan: the sequenced task list for transitioning from old system to new.

Hypercare: the intensive post-go-live support period.

ADKAR: Prosci's change management model — Awareness, Desire, Knowledge, Ability, Reinforcement.

TCO: Total Cost of Ownership — full lifecycle cost including license, implementation, and ongoing support.

Scope Creep: uncontrolled expansion of project requirements after initial scope is defined.

[SLIDE: Next module preview]

Module 16 is our final module — Certification Exam Preparation and Capstone. We will do a comprehensive review of all Salesforce Admin exam topic areas, a summary of SAP S/4HANA Essentials topics, 20 practice questions, and a capstone implementation scenario that synthesizes everything from the course. Come prepared.

Complete the Reading Guide, Lab, and Discussion. The quiz is available starting Monday.

See you for the final module.

[END OF VIDEO SCRIPT]

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
