# Video Script: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22–26 minutes

---

## Pre-Production Notes

- Slide deck: 32 slides
- Diagrams: SAP ASAP methodology phases (Waterfall arc), Salesforce implementation lifecycle (Discover/Define/Design/Build/Test/Deploy hexagonal flow), change management resistance curve (Kübler-Ross adaptation), cutover checklist timeline, hypercare dashboard mockup, parallel run vs. big-bang cutover comparison
- Key terms on screen: ASAP, Business Blueprint, Realization, Go-Live, Discover, Define, Design, Build, Test, Deploy, Change Management, Cutover, Hypercare, User Acceptance Testing, Parallel Run, Big Bang, Fit-Gap Analysis, Configuration Workbook
- End card: Lab 15, Quiz 15, Discussion Forum 15

---

## [00:00 – 02:30] Opening Hook

[PROFESSOR ON CAMERA]

In 1999, Hershey Foods — the chocolate company — went live with SAP. They chose to implement SAP ERP, a new CRM system, and a new supply chain system simultaneously, in a compressed timeline, right before Halloween. Halloween is the single highest-volume sales period of the year for a candy company.

The implementation ran into serious problems during go-live. Orders could not be processed correctly. Shipments were delayed. Retailers who had placed orders for Halloween candy received partial deliveries or nothing at all. Hershey's sales that quarter dropped by $150 million. Their stock price fell 8% in a single day.

What went wrong? The core issue was not the software. SAP worked. The issue was implementation methodology. They compressed a timeline that should not have been compressed. They went live during peak season rather than choosing a lower-risk period. They combined three major system changes at once. They did not have adequate time for testing and training. The implementation approach failed, and the business paid the price.

ERP implementation methodology is not bureaucracy. It is the difference between a successful go-live and a $150 million disaster. Today we cover the two dominant methodologies — SAP's ASAP framework and Salesforce's implementation lifecycle — and the critical practices that make or break any implementation: change management, cutover planning, and hypercare.

[SHOW TITLE SLIDE: Module 15 — ERP Implementation Methodology]

---

## [02:30 – 08:00] SAP ASAP Methodology

[SHOW SLIDE: ASAP — Accelerated SAP]

ASAP stands for Accelerated SAP. It is the structured project methodology that SAP developed to guide S/4HANA and predecessor ERP implementations. ASAP has five phases.

[SHOW SLIDE: Phase 1 — Project Preparation]

Phase 1 is Project Preparation. This is where the implementation starts before anyone touches the system. The activities in this phase include: defining the project scope (what business processes will be implemented), establishing the project team (which business stakeholders and IT resources are committed), setting up the project infrastructure (development, quality assurance, and production system landscape), and completing the initial project plan.

The key deliverable of Phase 1 is an approved project charter with defined scope, timeline, budget, and governance structure. Scope creep is the silent killer of ERP implementations. If you do not define and document scope in Phase 1, you will be arguing about it in every subsequent phase.

[SHOW SLIDE: Phase 2 — Business Blueprint]

Phase 2 is Business Blueprint. This phase documents how the organization's business processes will be configured in SAP. The project team conducts workshops with business process owners — one for each functional area: Finance, Procurement, Sales, HR, and so on.

In each workshop, the current state process is documented, the desired future state is defined, and the gap between how SAP works out of the box and what the business needs is identified. This gap analysis produces the fit-gap log — a list of every place where a business requirement does not fit standard SAP functionality and must be addressed through configuration, custom development (ABAP), or a process change.

The Business Blueprint document is a signed, approved record of all decisions made about how the system will be configured. Every subsequent design decision traces back to it.

[SHOW SLIDE: Phase 3 — Realization]

Phase 3 is Realization. This is the longest phase — where the system is actually configured based on the approved Business Blueprint. Activities include: baseline configuration (the initial system setup), final configuration (detailed settings based on business blueprint decisions), custom development (ABAP programs for gaps that cannot be addressed through configuration), integration testing (verifying that all configured processes work end to end across modules), and data migration preparation (cleaning and mapping legacy data to SAP structures).

The Realization phase produces a fully configured and tested system. It ends with a formal go/no-go decision based on test results and readiness criteria.

[SHOW SLIDE: Phase 4 — Final Preparation]

Phase 4 is Final Preparation. This phase runs in the weeks immediately before go-live. Activities include: end-user training (every person who will use the system gets trained on their specific processes), stress and volume testing (verifying the system handles production-level data loads), cutover planning and rehearsal (detailed step-by-step plan for migrating from the old system to SAP), and the final go/no-go decision.

The go/no-go decision at the end of Final Preparation is not ceremonial. It is a formal gate review. If training completion is below target, if critical test failures are unresolved, if data migration results are not clean — you do not go live. You delay. The cost of a delayed go-live is finite. The cost of a failed go-live can be catastrophic.

[SHOW SLIDE: Phase 5 — Go-Live and Support]

Phase 5 is Go-Live and Support. This is the transition to productive operations. The cutover happens — legacy systems are frozen, data is migrated, and users begin working in SAP. The hypercare period begins immediately — intensive support staffing, daily status calls, rapid response to issues. After hypercare, the project transitions to normal IT support operations.

---

## [08:00 – 14:00] Salesforce Implementation Lifecycle

[SHOW SLIDE: Salesforce — Six-Phase Lifecycle]

Salesforce implementations follow a six-phase lifecycle designed for CRM and cloud deployments. The phases are: Discover, Define, Design, Build, Test, and Deploy. Unlike ASAP, which is sequential with hard phase gates, the Salesforce lifecycle is iterative — many implementations run multiple build-test-deploy cycles to deliver functionality in waves.

[SHOW SLIDE: Discover Phase]

Discover is the discovery and scoping phase. The team interviews stakeholders, reviews current-state processes, identifies pain points, and documents requirements. In Salesforce terms, this means understanding: what business processes will run in Salesforce, what data needs to be migrated, what integrations are needed, and who the users are.

The key output of Discover is a requirements document and a prioritized feature backlog.

[SHOW SLIDE: Define Phase]

Define translates requirements into a documented solution design. The team maps business processes to Salesforce capabilities, identifies configuration vs. custom development requirements, and produces an architecture decision record covering: object model (standard vs. custom objects), automation approach (flows vs. Apex), security model (profiles, permission sets, OWD), and integration design.

The Define phase produces the Solution Design Document — the Salesforce equivalent of the SAP Business Blueprint.

[SHOW SLIDE: Design Phase]

Design produces the detailed technical specifications. For each requirement, the team documents exactly how it will be implemented: which fields, which page layouts, which validation rules, which flows. Design sessions are often done with prototypes or mock-ups to validate the approach with business stakeholders before build begins.

[SHOW SLIDE: Build Phase]

Build is where the system is configured and developed. Salesforce Administrators configure standard features: fields, objects, layouts, automation, reports, dashboards. Salesforce Developers build custom components where configuration is insufficient: Apex triggers, Lightning Web Components, custom integrations. Data migration scripts are built and tested.

[SHOW SLIDE: Test Phase]

Test is where the configured system is validated. Testing layers in a Salesforce implementation include: unit testing (developers verify individual components), system integration testing (verify that all configured features work together), user acceptance testing (business users run through their actual workflows and sign off), and performance testing (verify response times under expected load).

UAT — User Acceptance Testing — is the most critical test layer. It is the business's formal sign-off that the system meets requirements. UAT that is rushed or skipped is a primary cause of post-go-live problems.

[SHOW SLIDE: Deploy Phase]

Deploy is the move to production. In Salesforce, the deployment mechanism is Change Sets (declarative configuration) or Salesforce DX with version-controlled metadata (advanced). Production deployment is followed immediately by the hypercare period — intensive monitoring and support.

---

## [14:00 – 18:00] Change Management

[SHOW SLIDE: Why ERP Implementations Fail]

Studies of ERP implementation outcomes consistently find that technical failure is rarely the primary cause of project failure. The most common causes are: insufficient change management, inadequate user training, scope creep, and executive sponsor disengagement. The system worked. The people did not adopt it.

Change management is the discipline of managing the human side of organizational change — addressing resistance, building readiness, and driving adoption.

[SHOW SLIDE: The Change Curve]

Organizational change follows a predictable emotional arc. When a change is announced, people typically move through stages: awareness (this is happening), understanding (this is what it means for me), acceptance (I can see why this might be better), and commitment (I will actively use and support this). The change management role is to accelerate people through this curve and prevent them from getting stuck at resistance.

[SHOW SLIDE: Change Management Activities]

Core change management activities in an ERP implementation include:

Stakeholder analysis — identify every group affected by the change, assess their current level of support, and develop targeted engagement plans. A skeptical VP whose team must adopt the system is a different stakeholder than a frontline user who is afraid of losing their job to automation.

Communication plan — regular, honest communication about the project: what is changing, why it is changing, when it is changing, and how people will be supported. Communication should come from senior leaders, not just project managers.

Training program — role-based training that teaches users exactly what they need to know for their specific job functions. Generic training that covers all features for all roles is a waste of time and money.

Resistance management — identify resistance early, understand its root cause (fear of job loss, skepticism about the system, distrust of management, process loss), and address it directly.

[SHOW SLIDE: The Role of Executive Sponsorship]

Executive sponsorship is the single most reliable predictor of ERP implementation success. An engaged executive sponsor visibly champions the project, resolves organizational conflicts, removes blockers, and signals to the entire organization that this change is real, important, and supported at the top. When the executive sponsor is disengaged — attends only the kickoff and the go-live celebration and nothing in between — the project is in danger.

---

## [18:00 – 22:00] Cutover and Hypercare

[SHOW SLIDE: Cutover Planning]

Cutover is the process of transitioning from the old system to the new ERP. It is the highest-risk period in any implementation. Cutover planning begins months before go-live and culminates in a cutover weekend — typically a Friday evening through Sunday night — during which:

Legacy systems are frozen (no new transactions after the cutover cutoff time). Final data extracts are taken from legacy systems. Data migration scripts run, loading historical data into the new system. Technical go-live activities complete (transport to production, activation of integrations, DNS changes). Smoke tests verify that critical business processes work in production. Go/no-go decision is made. Users begin working in the new system Monday morning.

[SHOW SLIDE: Big Bang vs. Phased Cutover]

Two primary cutover strategies exist.

Big bang cutover: the entire organization switches from legacy to ERP at the same time. Higher risk, but simpler — there is only one cutover event and no need to run systems in parallel.

Phased cutover (also called parallel run or wave approach): different business units, geographies, or process areas go live in separate waves. The organization runs both systems simultaneously during transition. Lower risk per wave, but more complex and expensive — you are running two systems and the same transaction may need to be entered in both.

Most large SAP implementations use a phased approach by geography or module. Most Salesforce implementations use big bang for initial go-live, with additional features released in subsequent waves.

[SHOW SLIDE: Hypercare]

Hypercare is the intensive support period immediately following go-live — typically two to four weeks. During hypercare:

Support staffing is maximized. Consultants, project team members, and functional experts are on-site or on-call. Issue response times are minutes, not days.

Daily status meetings track open issues, escalate blockers, and communicate progress.

Go-live metrics are monitored: system performance, transaction error rates, help desk ticket volume, user adoption rates.

Production issues are triaged by severity. Critical issues (users cannot complete core processes) are resolved immediately. High issues (significant workaround required) are resolved within 24 hours. Medium and low issues are scheduled.

Hypercare ends when the system is stable, ticket volumes have normalized, and the support team can transition to standard IT operations.

---

## [22:00 – 26:00] Implementation Lessons and Module Summary

[SHOW SLIDE: Common Implementation Mistakes]

Let me close with the most common mistakes in ERP implementations — many of which contributed to the Hershey situation I described at the opening.

Compressing the timeline. Every project manager feels pressure to go live faster. But each phase of ASAP and the Salesforce lifecycle exists for a reason. Skipping or compressing testing, training, or cutover rehearsal creates a debt that is paid at go-live.

Going live at peak season. Choose a go-live date during the organization's lowest-volume period. If you are a retailer, do not go live in November. If you are an accountant, do not go live in March.

Underestimating data migration. Data migration is always harder than the project plan shows. Legacy data is dirty. Mapping rules have exceptions. Test the migration multiple times before the real cutover.

Treating training as an afterthought. Training is not a half-day session the week before go-live. Role-based training, with hands-on practice in a training environment, takes weeks.

[SHOW SLIDE: Module 15 Summary]

SAP's ASAP methodology provides five phases: Project Preparation, Business Blueprint, Realization, Final Preparation, and Go-Live and Support. The Salesforce implementation lifecycle provides six phases: Discover, Define, Design, Build, Test, and Deploy. Both frameworks emphasize the same fundamentals — define scope before building, test before deploying, train before going live. Change management addresses the human side of ERP adoption, and executive sponsorship is the most reliable success predictor. Cutover requires meticulous planning with a clear go/no-go decision point. Hypercare ensures intensive support in the critical weeks after go-live.

Your lab this week puts you in the role of a project manager planning a Salesforce implementation for a fictional company. Your quiz covers ASAP phases, Salesforce lifecycle phases, change management concepts, and cutover strategy.

See you in the discussion forum.

[END CARD: Lab 15 | Quiz 15 | Discussion Forum 15]

---

*End of Video Script — Module 15*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials
