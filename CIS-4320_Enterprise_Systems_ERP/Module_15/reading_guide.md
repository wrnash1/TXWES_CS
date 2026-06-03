# Reading Guide: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

Module 15 addresses the processes by which ERP systems are planned, implemented, and sustained. This content is directly relevant to both the SAP essentials examination and to professional practice — every technology career involves participation in or leadership of system implementations. Allocate approximately 90 minutes for this guide.

---

## Section 1: The ERP Implementation Challenge

### Scale and Complexity

An ERP implementation is unlike most IT projects. It touches every business process. It changes how hundreds or thousands of people do their jobs. It requires the simultaneous coordination of business analysts, technical developers, data migration specialists, change management experts, trainers, infrastructure engineers, and executive sponsors. The budget for a large SAP S/4HANA implementation at a Fortune 500 company routinely exceeds $100 million. A Salesforce Sales Cloud implementation for a 500-user company might cost $500,000 to $2 million.

Given this scale, structured methodology is not optional — it is what allows projects of this magnitude to be managed.

### The Iron Triangle of Projects

Every implementation lives within the Iron Triangle of project constraints: Scope (what will be delivered), Schedule (when it will be delivered), and Cost (what it will cost). These three constraints are interdependent — fixing two determines the third. If the business adds scope, either the schedule expands or the cost increases (or both). If the budget is cut, either scope must be reduced or the timeline extended.

ERP project managers constantly manage trade-offs within the Iron Triangle. Scope creep — the gradual, uncontrolled addition of requirements — is the most common cause of cost overruns and schedule delays because each addition looks small in isolation but accumulates into a major expansion.

### Waterfall vs. Agile in ERP

Traditional ERP methodologies like ASAP follow a broadly waterfall structure: complete one phase before beginning the next, with formal sign-offs at each phase gate. This works well when requirements are stable and the implementation team has deep domain knowledge.

Agile approaches — including SAP Activate and Salesforce Agile implementations — break the project into short iteration cycles (sprints, typically two weeks), delivering working functionality incrementally and incorporating feedback earlier. Agile reduces the risk of a "big bang" failure at go-live because functionality is validated continuously.

Most real ERP projects use a hybrid: waterfall-style planning and architecture phases, followed by Agile configuration and testing sprints, followed by a structured cutover.

---

## Section 2: SAP ASAP Methodology in Depth

### Phase 1 — Project Preparation

The project preparation phase establishes the organizational and technical foundation for everything that follows. Its success depends on genuine executive commitment, not just nominal sponsorship. An executive sponsor who attends the kick-off meeting and then delegates all decisions to a middle manager is not providing the sponsorship the project needs.

Key deliverables of Project Preparation:

**Project Charter:** documents the project objectives, scope boundaries (what is in scope and explicitly what is out of scope), key stakeholders, and authorization to proceed.

**System Landscape Design:** defines the three-tier SAP landscape — Development (DEV), Quality/Test (QAS), and Production (PRD) — and how transport requests will move configuration changes through the landscape.

**Project Organization:** identifies the executive sponsor, steering committee, project manager, functional leads (Finance, Sales, Supply Chain), technical lead, and change management lead.

**Project Schedule:** initial plan with milestones, phase durations, and major deliverable dates.

### Phase 2 — Business Blueprint

The Business Blueprint phase is the most intellectually intensive phase of ASAP. It is where the implementation team — in structured workshops with business representatives — documents how the organization's business processes will be implemented in SAP.

The Blueprint process uses SAP's Question & Answer database (Q&A DB) as a guide. For each business process, a set of predefined questions prompts the team to document current-state and to-be-state process details. The questions cover organizational structures (company codes, plants, sales organizations, controlling areas), master data (account groups, material types, payment terms), and process flows.

The output — the Business Blueprint document — becomes the primary reference document for the entire Realization phase. It must be reviewed and signed off by business stakeholders before Realization begins, because changes after sign-off require formal change control and typically cause scope creep.

### Phase 3 — Realization

Realization is the longest phase. It breaks into two configuration cycles:

**Baseline Configuration (Cycle 1):** Configure the core processes documented in the Business Blueprint. Integration testing at the end of Cycle 1 validates that the baseline configuration meets the majority of requirements and that the end-to-end process flows work correctly.

**Final Configuration (Cycle 2):** Address gaps identified in Cycle 1 integration testing. Configure remaining processes. Develop ABAP enhancements and custom reports. Complete interface development. Execute volume testing and performance testing.

The configuration framework in SAP is accessed through transaction SPRO (SAP Project Reference Object — also called the IMG, Implementation Guide). The IMG is a structured menu of all SAP configuration settings, organized by functional area. Every SAP configuration change is documented as a transport request, which is moved through the landscape from DEV to QAS to PRD in a controlled sequence.

### Phase 4 — Final Preparation

Final Preparation is often underestimated in project planning. Teams assume configuration is the hard part and that preparation is just scheduling training. In reality, Final Preparation can expose major gaps if it is rushed.

Key activities in Final Preparation:

**End-User Training:** training materials must reflect the actual configured system, not a generic SAP system. Role-specific training scripts ensure that users practice the transactions they will actually use. Training environments need to be loaded with realistic master data.

**Data Migration Dress Rehearsals:** the data migration must be rehearsed at full scale before the production migration. Dress rehearsals reveal timing issues (migration takes longer than the cutover window allows), data quality issues, and transformation errors.

**Help Desk Readiness:** the support team must be trained before go-live. Tier 1 support handles password resets and navigation questions; Tier 2 handles process and configuration questions; Tier 3 escalates to the SAP implementation consultants.

**Go/No-Go Assessment:** a formal evaluation of readiness across multiple dimensions. Typical criteria include: testing completion rate (target: 95%+), open critical defects (target: zero), training completion (target: 80%+ of users), and data migration success rate (target: 98%+ of records migrated without errors).

### Phase 5 — Go-Live and Support

Go-Live is the transition from the old system to the new. After the cutover is complete and the production system is confirmed stable, the project formally enters the Go-Live and Support phase.

Support activities immediately after go-live:

**Issue triage and resolution:** issues are categorized and resolved in priority order. The hypercare team meets daily (sometimes twice daily) to review the open issues list.

**User support:** end users encounter situations not covered by their training. Super users — experienced business users trained during the project — serve as first-line support within their departments.

**Monitor system performance:** the first weeks of production use are the peak risk period for performance problems. Basis administrators monitor response times, database load, and work process utilization closely.

### SAP Activate — Agile Evolution

SAP Activate modernizes ASAP by introducing Agile principles, pre-configured best practice content, and a fit-to-standard philosophy.

**Discover phase:** before the project officially begins, the customer uses SAP Best Practices content in a trial system to explore standard S/4HANA processes and validate that they meet business requirements. This reduces Blueprint workshop time because the team starts from a working baseline.

**Prepare phase:** equivalent to ASAP Project Preparation — project setup, landscape provisioning, initial backlog creation.

**Explore phase:** equivalent to Business Blueprint — but much shorter because the team starts from the Discover baseline. Focuses on documenting gaps between standard processes and business requirements.

**Realize phase:** multiple two-week Agile sprints. Each sprint configures, develops, and unit-tests a set of backlog items. Sprint reviews demonstrate working functionality to business stakeholders.

**Deploy phase:** equivalent to Final Preparation and Go-Live.

**Run phase:** steady-state operations and continuous improvement.

---

## Section 3: Salesforce Implementation Lifecycle

### Discovery Phase in Detail

Salesforce discovery involves understanding the current state of the business's CRM-related processes before designing the new Salesforce configuration. Effective discovery uses multiple techniques:

**Stakeholder interviews:** conversations with process owners, end users, managers, and executives to understand pain points, goals, and requirements.

**Process mapping:** documenting the current workflow for key processes (lead management, opportunity progression, case handling) in a visual format.

**Data discovery:** identifying what data exists in legacy systems, what quality it is in, and what needs to be migrated.

**Shadow reporting:** asking users to show you the reports or spreadsheets they currently rely on — these reveal the outputs the system must produce.

### Sandbox Strategy

A disciplined sandbox strategy is essential for professional Salesforce development.

**Developer Sandbox:** used for individual development work. Does not contain production data. Free with most Salesforce editions. Multiple Developer sandboxes can be provisioned for parallel workstreams.

**Developer Pro Sandbox:** larger storage capacity than Developer sandbox; useful for testing integrations.

**Partial Sandbox:** contains a configurable subset of production records (up to 5,000 records per object). Useful for testing with realistic data volumes without the full production dataset.

**Full Sandbox:** an exact copy of the production environment — same data, same configuration. Used for performance testing, UAT, and regression testing before major releases. Most expensive sandbox type; limited to one per production org in most editions.

### Change Sets vs. Salesforce DX

Change sets are the traditional Salesforce deployment mechanism. An outbound change set is created in a sandbox, populated with metadata components (objects, fields, workflows, classes), and deployed to another org. The target org applies the change set, updating its metadata to match.

Change sets have significant limitations: they cannot track which sandbox a component came from, they do not support version control, they are manual and error-prone, and they do not support rollback.

Salesforce DX (Developer Experience) introduced a source-driven development model: metadata is stored in a Git repository, and deployment is handled through CLI commands or automated CI/CD pipelines. DX supports proper version control, automated testing, and more reliable deployments.

---

## Section 4: Change Management

### The ADKAR Framework in Practice

ADKAR provides a diagnostic model for understanding why change is not sticking. A change management practitioner can assess each ADKAR stage and identify the barrier point — the stage where most people are currently stuck.

If employees score low on Awareness: the communication program needs strengthening. They do not understand why the change is happening.

If Awareness is high but Desire is low: employees understand the reason but do not support it. This often indicates fear, mistrust of leadership, or perceived personal loss. The response is targeted coaching, clarifying messages about job impact, and visible sponsorship from trusted leaders.

If Knowledge is low after training: the training content may be poor quality, not role-specific, or delivered too early (people forget what they learned six weeks before go-live).

If Knowledge is high but Ability is low: people know what to do but cannot do it in practice. This indicates a need for more hands-on practice, better job aids, or a more supportive go-live environment (super users stationed nearby, help desk readily accessible).

If Reinforcement is weak: people initially adopted the change but reverted over time. This happens when managers do not model the new behavior, when old tools (spreadsheets) remain available as workarounds, or when early users who try the new way encounter problems.

### Stakeholder Analysis

A stakeholder analysis maps each significant stakeholder or stakeholder group across two dimensions: their level of impact from the change, and their current level of support. The resulting matrix reveals:

High impact, high support: champions — engage them as advocates.

High impact, low support: resistors — require targeted engagement and possibly executive intervention.

Low impact, high support: allies — useful for communication but not the priority focus.

Low impact, low support: watchful — monitor but not the primary concern.

Stakeholder analysis should be performed at the beginning of a project and updated at each phase, because support levels change over time.

---

## Section 5: Cutover Planning and Hypercare

### Cutover Plan Structure

A formal cutover plan is a spreadsheet or project management document that lists every task with the following attributes for each task:

- Task sequence number
- Task description
- Owner (specific person, not a role)
- Estimated duration (in hours)
- Dependencies (which task must be complete before this one starts)
- Completion sign-off (confirmation that the task is done)

The cutover tasks are organized into a timeline that maps the entire cutover window — typically a weekend or holiday period when transaction volume is lowest. The critical path through the cutover task list determines the minimum time required. Most cutover windows have a rollback decision point — a time by which the go/no-go must be confirmed. If the cutover is running significantly behind, the decision to roll back must be made before the rollback becomes impossible.

### Data Migration in the Cutover

The final production data migration is typically the most time-sensitive cutover task. Migration programs have been tested in dress rehearsals, but production volumes may differ from test volumes. Monitoring the migration's progress against the time plan in real-time is essential.

Migration errors discovered during production cutover require immediate triage: is the error a blocker that prevents go-live (such as a failure to migrate all open purchase orders), or is it a low-priority cleanup item that can be handled after go-live?

### Hypercare Activities

Hypercare typically runs two to four weeks. Key activities:

**Daily issue triage call:** project team and business leads review all open issues, assign owners, confirm resolution timeline.

**War room or virtual support channel:** a dedicated support channel (Teams, Slack, or a physical room) where issues can be raised and resolved rapidly.

**Trend monitoring:** tracking the volume and severity of issues by day. A well-functioning system shows a declining issue volume as users become familiar with the system and initial bugs are resolved.

**Super user support:** trained business users who can handle first-line questions within their functional area without escalating to the project team.

---

## Section 6: Total Cost of Ownership

### The Five TCO Categories

**License and Subscription Costs:** the annual fee for using the software. For Salesforce, this is per-user-per-month pricing. For SAP, this may be a perpetual license plus annual maintenance, or a cloud subscription.

**Implementation Costs:** consulting services, internal staff time, travel, and any hardware purchased. This is usually the largest upfront investment.

**Integration Costs:** the ongoing cost of maintaining interfaces between systems. Every time a connected system is upgraded, integrations may need to be updated.

**Maintenance and Enhancement Costs:** the annual cost of keeping the system current — applying patches and updates, configuring new business requirements, and maintaining custom code.

**Support Costs:** the cost of the internal team or managed services provider that supports the system day-to-day — helpdesk, system administration, security administration.

### Salesforce vs. SAP TCO Dynamics

Salesforce's SaaS model eliminates infrastructure costs and reduces upgrade costs (Salesforce handles three major releases per year automatically). However, the per-user pricing scales steeply with user count, and licensing costs for add-on products (Einstein, Shield, CRM Analytics) accumulate quickly.

SAP's on-premises model requires significant infrastructure investment and technical staff but provides more control. SAP's cloud (S/4HANA Cloud) moves toward a subscription model similar to Salesforce.

For a 500-user Salesforce Sales Cloud implementation, a realistic 5-year TCO might be: Year 1 licensing and implementation $1.2M, Years 2–5 licensing and ongoing support $2.8M, for a total of approximately $4M.

---

## Key Terms for Module 15

**ASAP (Accelerated SAP):** SAP's classic five-phase implementation methodology.

**SAP Activate:** SAP's current Agile implementation methodology for S/4HANA.

**Business Blueprint:** the Phase 2 ASAP deliverable documenting to-be business processes.

**SPRO / IMG:** the SAP customizing framework used during Realization.

**Transport Request:** the mechanism for moving SAP configuration changes between system landscapes.

**Sandbox (Salesforce):** a copy of the production org used for development and testing.

**Change Set:** the traditional Salesforce mechanism for deploying metadata between orgs.

**Salesforce DX:** source-driven development model storing metadata in version control.

**Go/No-Go:** a formal readiness gate before production go-live.

**Cutover Plan:** the sequenced task list for transitioning from old to new system.

**Rollback Plan:** the documented procedure for reverting to the old system if go-live fails.

**Hypercare:** the intensive post-go-live support period.

**ADKAR:** Prosci's change management model — Awareness, Desire, Knowledge, Ability, Reinforcement.

**Scope Creep:** uncontrolled addition of requirements after scope is formally defined.

**TCO (Total Cost of Ownership):** complete lifecycle cost including license, implementation, integration, maintenance, and support.

**Iron Triangle:** the interdependency of Scope, Schedule, and Cost in project management.

---

## Study Questions

1. Name the five phases of the SAP ASAP methodology and describe the primary deliverable of each phase.

2. What is the difference between ASAP and SAP Activate? Why did SAP move from a waterfall to an Agile approach?

3. Explain the purpose of the three-tier SAP system landscape (DEV, QAS, PRD). What would happen if developers made configuration changes directly in the production system?

4. Compare Salesforce Change Sets to Salesforce DX. What are the limitations of change sets that DX addresses?

5. Describe the four Salesforce sandbox types and explain which one is most appropriate for user acceptance testing with realistic data.

6. Using the ADKAR model, analyze a scenario where employees have attended SAP training but are still using their old spreadsheet system after go-live. Which ADKAR stage is the barrier, and what interventions would address it?

7. What is a rollback plan, and at what point during a cutover would you make the rollback decision? What makes rolling back after a certain point impractical?

8. Define Total Cost of Ownership and list the five TCO categories. Which category do most organizations underestimate, and why?

9. What is the Go/No-Go decision, and what evidence should the project team present to support a go-live recommendation?

10. Describe how scope creep develops on a typical ERP project and explain two process controls that can prevent it.

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
