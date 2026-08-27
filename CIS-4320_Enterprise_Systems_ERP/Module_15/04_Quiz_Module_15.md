# Quiz: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Questions are drawn from the video lecture, reading guide, and lab activity for Module 15.

---

## Questions

### Question 1

During which phase of the SAP ASAP methodology are business process workshops conducted, and the fit-gap log is produced?

A) Project Preparation

B) Business Blueprint

C) Realization

D) Final Preparation

**Correct Answer:** B

#### Distractor Analysis

- **A — Project Preparation** is incorrect. Project Preparation establishes scope, team structure, project governance, and the system landscape. Business process workshops have not yet started.
- **B — Business Blueprint** is correct. Business Blueprint is explicitly the phase where current-state and future-state processes are documented through workshops, and the fit-gap log is produced identifying where SAP standard functionality meets or does not meet requirements.
- **C — Realization** is incorrect. Realization is the configuration and development phase. It builds the system based on decisions made during Business Blueprint; workshops were already completed.
- **D — Final Preparation** is incorrect. Final Preparation covers end-user training, UAT, and cutover rehearsal — not requirements documentation.

---

### Question 2

A company implementing SAP S/4HANA discovers that their custom vendor approval workflow cannot be replicated through standard SAP configuration. The process change option is considered impractical because of regulatory requirements. Which resolution approach should be selected?

A) Full fit — use standard SAP functionality as-is

B) Process change — train users to adopt the SAP standard process

C) Custom development — write ABAP code to build the required workflow

D) Defer — remove the requirement from scope

**Correct Answer:** C

#### Distractor Analysis

- **A — Full fit** is incorrect. The scenario explicitly states the requirement cannot be met through standard SAP configuration.
- **B — Process change** is incorrect. The scenario explicitly states that a process change is impractical due to regulatory requirements, ruling out this option.
- **C — Custom development** is correct. When standard configuration cannot meet the requirement and the process cannot be changed, custom ABAP development is the appropriate resolution. This is a legitimate gap resolution strategy, used when the other two options are unavailable.
- **D — Defer** is not a standard gap resolution option in the fit-gap framework and would leave a regulatory requirement unaddressed.

---

### Question 3

In the Salesforce implementation lifecycle, which phase produces the Solution Design Document covering the object model, security model, automation model, and integration design?

A) Discover

B) Define

C) Design

D) Build

**Correct Answer:** B

#### Distractor Analysis

- **A — Discover** is incorrect. Discover produces requirements documentation and a prioritized feature list. Architectural decisions have not yet been made.
- **B — Define** is correct. Define translates requirements into documented architectural decisions including the object model, security model, automation approach, and integration design. The Solution Design Document is the primary deliverable of this phase.
- **C — Design** is incorrect. Design produces detailed field-level and element-level specifications. It follows Define and assumes architectural decisions have already been made.
- **D — Build** is incorrect. Build is the configuration and development phase where specifications from Design are implemented.

---

### Question 4

User Acceptance Testing (UAT) in an ERP implementation is best described as:

A) Testing performed by developers to verify individual code components function correctly

B) Performance testing that verifies the system handles production-level transaction volumes

C) Business-user-driven testing where stakeholders execute their real workflows and formally sign off that the system meets requirements

D) A security audit that verifies user permissions are correctly configured

**Correct Answer:** C

#### Distractor Analysis

- **A — Developer unit testing** is incorrect. Unit testing is a developer activity. UAT is explicitly a business user activity, not a developer activity.
- **B — Performance testing** is incorrect. Performance or load testing is a separate test type that measures system response under volume. UAT measures whether business processes work correctly.
- **C — Business-user workflow validation** is correct. UAT is distinguished from all other test types by the fact that it is owned and executed by business users — not IT — and results in a formal sign-off that the system meets business requirements.
- **D — Security audit** is incorrect. Security testing verifies permission configurations, which is a separate concern from UAT.

---

### Question 5

A global organization is implementing SAP S/4HANA across 18 countries. Rather than switching all countries to SAP simultaneously, they plan to go live in three groups of six countries, six months apart. This is an example of which cutover strategy?

A) Big bang cutover

B) Parallel run

C) Phased cutover

D) Sandbox promotion

**Correct Answer:** C

#### Distractor Analysis

- **A — Big bang** is incorrect. A big bang cutover moves the entire organization at once. Transitioning in three sequential groups is the opposite of big bang.
- **B — Parallel run** is incorrect. A parallel run means operating both legacy and new systems simultaneously during transition. The scenario describes sequential geographic waves, not simultaneous dual-system operation.
- **C — Phased cutover** is correct. Transitioning in defined groups (waves) separated by time — whether by geography, business unit, or process module — is the definition of a phased cutover strategy.
- **D — Sandbox promotion** is incorrect. Sandbox promotion refers to moving Salesforce configuration from a sandbox environment to production. It is not a cutover strategy concept.

---

### Question 6

According to Prosci research cited in the reading, projects with excellent change management are how many times more likely to meet their objectives compared to projects with poor change management?

A) Twice as likely

B) Three times as likely

C) Six times as likely

D) Ten times as likely

**Correct Answer:** C

#### Distractor Analysis

- **A — Twice** is incorrect. The research finding is more significant than a 2x improvement factor.
- **B — Three times** is incorrect. While this sounds plausible, it understates the research finding.
- **C — Six times** is correct. The Prosci research finding, cited in the reading, is that projects with excellent change management are six times more likely to meet their objectives than those with poor change management.
- **D — Ten times** is incorrect. This overstates the research finding.

---

### Question 7

Which of the following activities belongs in the Final Preparation phase of ASAP rather than the Realization phase?

A) Baseline system configuration

B) Custom ABAP development for identified gaps

C) Cutover plan rehearsal and end-user training

D) Integration testing of end-to-end business processes

**Correct Answer:** C

#### Distractor Analysis

- **A — Baseline configuration** is incorrect. Baseline system configuration is a Realization phase activity — it establishes core system settings (company code, chart of accounts, organizational structure) at the start of Realization.
- **B — Custom ABAP development** is incorrect. ABAP development is a Realization phase activity. It occurs in parallel with configuration during Realization.
- **C — Cutover rehearsal and training** is correct. Both cutover plan rehearsal and end-user training are explicitly Final Preparation activities. They occur in the weeks immediately before go-live, after Realization is complete.
- **D — Integration testing** is incorrect. Integration testing is a Realization phase activity. It verifies end-to-end process flows across modules after configuration is complete.

---

### Question 8

A sales representative who has used the same spreadsheet-based sales tracking system for 12 years tells her manager: "I don't need Salesforce — I know where all my deals are and I never lose track of anything." This represents which source of resistance to ERP change?

A) Fear of job loss

B) Distrust of management

C) Loss of familiar processes and perceived competence with the current system

D) Legitimate concern that the new system has a functional defect

**Correct Answer:** C

#### Distractor Analysis

- **A — Fear of job loss** is incorrect. The rep's statement does not suggest concern about her position being eliminated; she is expressing confidence in her current method.
- **B — Distrust of management** is incorrect. There is no indication of distrust toward leadership in the statement; the concern is about her personal workflow.
- **C — Loss of familiar processes** is correct. The rep's resistance stems from comfort with and confidence in her existing approach. This is the "loss of familiar processes" source of resistance — people resist change when their current method feels effective to them personally, even if it is inferior at the organizational level.
- **D — Legitimate functional concern** is incorrect. She has not identified a specific defect in Salesforce; she is simply expressing preference for her current tool.

---

### Question 9

Which of the following best defines the hypercare exit criteria concept?

A) The point at which the project sponsor formally approves the implementation budget

B) The date on which UAT sign-off is obtained from all business process owners

C) Defined stability thresholds — including issue backlog levels, ticket volume trends, and adoption metrics — that mark the official end of the intensive post-go-live support period

D) The date on which all custom ABAP development is unit-tested and approved for transport to production

**Correct Answer:** C

#### Distractor Analysis

- **A — Budget approval** is incorrect. Budget approval is a Project Preparation or steering committee activity, not a hypercare concept.
- **B — UAT sign-off** is incorrect. UAT sign-off occurs during Final Preparation, before go-live. Hypercare begins after go-live.
- **C — Stability thresholds** is correct. Hypercare exit criteria are measurable stability standards — no open P1 issues, P2 backlog below threshold, declining help desk ticket volume, system performance within targets, user adoption at target — that must be met before the project officially transitions to normal IT support operations.
- **D — ABAP unit testing** is incorrect. ABAP unit testing is a Realization phase activity occurring long before go-live.

---

### Question 10

The 1999 Hershey Foods ERP implementation failure resulted in $150 million in lost sales. Based on the module content, which combination of methodology failures best explains this outcome?

A) Choosing SAP over Oracle and using ABAP custom development extensively

B) Compressing testing and training timelines, implementing multiple systems simultaneously, and choosing a go-live date during peak season

C) Failing to complete a Business Blueprint and launching directly into Realization

D) Not using a dynamic dashboard for executive reporting and skipping the hypercare period

**Correct Answer:** B

#### Distractor Analysis

- **A — Software choice and ABAP** is incorrect. The module explicitly states the software worked — the failure was methodological, not a product selection issue.
- **B — Compressed timeline, multiple simultaneous systems, peak-season go-live** is correct. The module identifies these three factors: an overly compressed timeline that did not allow adequate testing and training, the decision to implement three major systems simultaneously rather than sequentially, and the choice to go live immediately before Halloween — the highest-volume period for a candy company.
- **C — Skipping Business Blueprint** is incorrect. The module does not identify skipping the Blueprint as a cause; the issues were in testing, training, scope, and timing.
- **D — Reporting and hypercare** is incorrect. The failure was an operational go-live disaster during transaction processing — reporting tools and hypercare structure were not identified causes.

---

*End of Quiz — Module 15*

---

### Question 11

(5 points)

In SAP Activate methodology, which phase is equivalent to the "Business Blueprint" phase in the older ASAP methodology, and what is the primary tool used to document fit-gap analysis in SAP Activate?

- A) Prepare phase; the primary tool is the Project Charter document
- B) Explore phase; the primary tool is the Fit-to-Standard analysis conducted in workshops using SAP best practice processes as the baseline
- C) Realize phase; the primary tool is the ABAP transport log
- D) Deploy phase; the primary tool is the Cutover Plan

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* SAP Activate replaced ASAP as SAP's official implementation methodology for S/4HANA. The Explore phase in SAP Activate corresponds to the Business Blueprint phase in ASAP. The distinguishing characteristic of SAP Activate's Explore phase is "Fit-to-Standard" workshops — rather than documenting current state and then designing the future state, teams start from SAP's delivered best practice processes and document only where deviations (gaps) are required. This inverts the traditional blueprint approach.
  - *Why A is incorrect:* The Prepare phase in SAP Activate is the project kickoff phase — establishing governance, infrastructure, and team onboarding. It does not include business process workshops or fit-gap analysis. It corresponds to ASAP's Project Preparation phase.
  - *Why C is incorrect:* The Realize phase is the configuration and development phase — equivalent to ASAP's Realization phase. By this point, fit-gap decisions have already been made in Explore; Realize implements those decisions.
  - *Why D is incorrect:* The Deploy phase covers final testing, cutover, and go-live. The Cutover Plan is a Deploy deliverable, but fit-gap analysis has long been completed before Deploy begins.

---

### Question 12

(5 points)

A Salesforce implementation project is in the Build phase when a business stakeholder requests a significant new feature that was not in the approved scope. How should the project manager respond according to implementation methodology best practices?

- A) Immediately add the feature to the Build sprint — stakeholder requests should always be accommodated
- B) Refuse the request entirely — no scope changes are permitted once Build begins
- C) Evaluate the request through a formal change control process that assesses impact on timeline, budget, and resources before making a decision with project sponsor approval
- D) Add the feature as a "nice to have" and build it during hypercare if time allows

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Change control is the formal process for evaluating scope changes during an implementation. Any new requirement must be assessed for its impact on timeline, budget, and resource allocation. The project sponsor (and often a Change Control Board) must approve scope additions. This process protects the project from scope creep — the most common cause of budget overruns and timeline delays in ERP implementations.
  - *Why A is incorrect:* Immediately accommodating every stakeholder request without assessment leads to scope creep — uncontrolled expansion of project scope that delays go-live and overruns budget. Even legitimate requests must go through change control.
  - *Why B is incorrect:* Blanket refusal of all scope changes is inflexible and may prevent legitimate business-critical requirements from being addressed. Change control exists to evaluate requests, not to block them automatically.
  - *Why D is incorrect:* Adding features informally as "nice to haves" without change control approval is scope creep by another name. Hypercare is for post-go-live support, not for completing deferred development — attempting development during hypercare while also supporting a live production system is a significant risk.

---

### Question 13

(5 points)

ADKAR is a change management model used in ERP implementations. A project team runs an awareness campaign, provides training, and asks users to start using the new system — but adoption remains low 60 days after go-live. A change management consultant diagnoses the problem as a "Desire gap." What does this mean, and what is the recommended intervention?

- A) Users are unaware the new system exists — the intervention is to run additional awareness communications
- B) Users know about the change and understand how to use the system, but they do not personally want to change — the intervention is to identify and address the motivational barrier through management reinforcement, visible sponsorship, and connecting the change to personal benefit
- C) Users lack the technical skills to operate the new system — the intervention is to provide additional hands-on training
- D) The organization has not reinforced the change after go-live — the intervention is to measure adoption metrics and celebrate successes

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* In the ADKAR model, Desire (D) is the second element — the personal motivation to support and participate in the change. A Desire gap means awareness (A) has been achieved (users know about the change) but they are not personally motivated to change their behavior. Training addresses Knowledge (K) and Ability (A), not Desire. The correct intervention for a Desire gap involves management engagement, removing barriers to personal motivation, demonstrating leadership commitment, and making the individual benefit of the change visible to users.
  - *Why A is incorrect:* Awareness (A) is the first ADKAR element. If the diagnosis is a Desire gap, Awareness has already been achieved — running more awareness communications addresses the wrong gap and will not improve adoption.
  - *Why C is incorrect:* Knowledge (K) and Ability (A) relate to users understanding how to use the system and being capable of doing so. Additional training addresses a Knowledge or Ability gap. The question specifies the diagnosis as a Desire gap — the users know how but do not want to.
  - *Why D is incorrect:* Reinforcement (R) is the fifth ADKAR element — sustaining the change after adoption. While reinforcement is important, the described issue is pre-adoption unwillingness (Desire), not post-adoption regression (which Reinforcement addresses).

---

### Question 14

(5 points)

A company's project team is conducting integration testing for their SAP S/4HANA implementation. Which of the following correctly describes the scope and purpose of integration testing, and how it differs from unit testing?

- A) Integration testing verifies individual configuration objects in isolation (e.g., a single G/L account setting); unit testing verifies end-to-end process flows across multiple modules
- B) Integration testing verifies complete end-to-end business process flows across multiple SAP modules (e.g., a full Procure-to-Pay cycle from Purchase Requisition through Vendor Payment); unit testing verifies individual configuration objects or development components in isolation
- C) Integration testing is performed by business users while unit testing is performed by consultants — the distinction is who performs the test, not what is tested
- D) Integration testing and unit testing are the same activity — both verify that configuration meets requirements

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Unit testing validates individual components in isolation: does this specific configuration object, ABAP program, or workflow step work correctly by itself? Integration testing validates whether the components work correctly together across module boundaries: does a Purchase Requisition created in MM flow correctly through Purchasing, trigger a Goods Receipt, match to an invoice in MIRO, and generate the correct FI posting? The end-to-end scope is the defining characteristic of integration testing.
  - *Why A is incorrect:* This reverses the definitions. Individual configuration object verification is unit testing. End-to-end process flows across modules is integration testing. The definitions are inverted.
  - *Why C is incorrect:* While business users do participate in UAT (which is related to integration testing), the distinction between unit and integration testing is about scope — individual vs. cross-module — not about who performs the test. Consultants and analysts often perform both types.
  - *Why D is incorrect:* Unit and integration testing have different scopes, purposes, and pass/fail criteria. They are not the same activity. Conflating them misses the fact that individually working components can fail when they interact — which is exactly what integration testing is designed to detect.

---

### Question 15

(5 points)

A project team completes a mock cutover and discovers that restoring the legacy system (executing the cutback plan) would take 18 hours — but the cutover window is only 60 hours and go-live is already 8 hours in. What does this reveal about the cutback plan, and what should be done before the production cutover?

- A) The cutback plan is fine — 18 hours is within the remaining window if go-live fails in the first 40 hours
- B) The cutback plan has a timing flaw: if a go/no-go decision is made 40+ hours into the cutover window, there would not be enough time to execute the cutback before Monday morning business operations resume; the team must either accelerate the cutback process or define an earlier go/no-go decision point that ensures the cutback can complete within the window
- C) Cutback plans are optional — the team should delete the cutback plan and commit fully to go-live
- D) The 18-hour cutback time is acceptable because the legacy system is always available as a fallback regardless of cutover duration

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The cutback plan must be executable within the cutover window. If the cutover window is 60 hours and the cutback takes 18 hours, the latest the team can decide to cut back and still complete it before the window closes is hour 42 (60 minus 18). If a go/no-go decision point is set at hour 48 — which is after the point of no return — the team could be stranded with neither a working SAP system nor enough time to restore the legacy system. The mock cutover revealed this flaw so it can be fixed before production.
  - *Why A is incorrect:* This reasoning is precisely the flaw the mock cutover exposed. Saying "18 hours is within the remaining window if go-live fails in the first 40 hours" is only true for the first 42 hours of the window. Any failure discovered after hour 42 makes the cutback impossible within the window — which is the crisis.
  - *Why C is incorrect:* Cutback plans are mandatory for any responsible cutover. "Committing fully" without a fallback is project management negligence — if a critical issue is discovered after data load, the business needs the ability to revert to the legacy system.
  - *Why D is incorrect:* Legacy systems often have cutover freeze periods (no transactions during SAP go-live) and may have data differences by the time cutback would need to occur. Assuming the legacy system is always available as a passive fallback ignores the operational complexity of a cutback scenario.

---

### Question 16

(5 points)

A company's CFO is the executive sponsor of an SAP implementation. Three months after go-live, she stops attending monthly steering committee meetings and delegates attendance to a junior finance manager. According to change management best practice, what risk does this create, and what should the change management lead do?

- A) No risk — steering committee attendance is a formality after go-live; the CFO's involvement is no longer needed
- B) This signals waning executive sponsorship, which is one of the highest-risk factors for post-go-live adoption failure; the change management lead should re-engage the CFO, explain the ongoing business impact of her visible support, and restructure her involvement to match her available time
- C) The junior finance manager should be designated the new executive sponsor — titles should match responsibility
- D) The risk is only financial — the CFO's absence may delay budget approval for Phase 2

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Executive sponsorship is not just a project kick-off role — it is critical throughout implementation and into the post-go-live adoption period. Users look to senior leadership behavior as a signal of whether the change is real and permanent. When the CFO stops visibly championing the system, resistant users interpret this as permission to revert to old behaviors. The change management lead must re-engage the sponsor and find ways to maintain visible leadership support even if the form changes (e.g., a brief monthly message vs. full meeting attendance).
  - *Why A is incorrect:* Executive sponsorship research consistently shows that visible senior leadership support is one of the top predictors of adoption success — not just during implementation but in the months following go-live when behavioral change is being reinforced or abandoned.
  - *Why C is incorrect:* Designating a junior finance manager as executive sponsor would be ineffective — the organizational authority, credibility, and signaling value of executive sponsorship depends on the seniority of the sponsor. A junior manager cannot fulfill the accountability and influence functions of the role.
  - *Why D is incorrect:* While budget implications are real, the primary risk of waning executive sponsorship is adoption failure — users reverting to legacy behaviors, workarounds proliferating, and the organizational change not sticking. Financial impacts on Phase 2 are secondary to the Phase 1 adoption risk.

---

### Question 17

(5 points)

A Salesforce implementation team is preparing to deploy configuration from a Full Sandbox to production. Which Salesforce tool packages the configuration metadata and moves it between environments, and what is a key limitation of this tool?

- A) Data Loader — it moves both data records and configuration metadata; the limitation is a 50,000-record API limit
- B) Change Sets — they package and deploy configuration metadata (objects, fields, flows, profiles); the limitation is that they are one-directional (sandbox to production) and cannot package all metadata types, particularly complex dependencies
- C) Workbench — it deploys all metadata types including data records; there are no limitations
- D) Salesforce Inspector — it packages metadata for deployment; the limitation is it requires a paid add-on license

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Change Sets are the standard Salesforce tool for deploying metadata configuration between connected orgs (sandbox to production). They package metadata components (custom objects, fields, page layouts, flows, permission sets) and deploy them without moving data records. Key limitations include: not all metadata types are supported by Change Sets, dependencies must be manually identified and included, and Change Sets do not support rollback — you cannot "undo" a deployed Change Set.
  - *Why A is incorrect:* Data Loader is a data migration and manipulation tool — it operates on data records (insert, update, delete), not configuration metadata. It cannot deploy custom object definitions, field configurations, flows, or other metadata components.
  - *Why C is incorrect:* Workbench is a community-supported tool primarily used for SOQL queries and data exploration. While it has some metadata deployment capabilities via the Metadata API, it is not the standard deployment tool and the statement "no limitations" is false for any tool.
  - *Why D is incorrect:* Salesforce Inspector is a browser extension used for viewing record data and field API names during development and debugging. It is not a deployment tool and does not package or move metadata between orgs.

---

### Question 18

(5 points)

The "parallel run" cutover strategy involves operating both the legacy system and the new ERP simultaneously for a defined period. What is the primary advantage of this strategy, and what is its most significant operational drawback?

- A) Advantage: fastest go-live execution; Drawback: requires custom development to connect the two systems
- B) Advantage: risk reduction through validation — transactions processed in both systems can be compared for accuracy before legacy is decommissioned; Drawback: double the operational workload for end users who must enter the same transactions in two systems simultaneously
- C) Advantage: reduces training requirements because users can continue using the legacy system indefinitely; Drawback: the new system never becomes the primary system
- D) Advantage: eliminates the need for a cutback plan; Drawback: requires all data to be migrated before the parallel period begins

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The parallel run strategy's core value is risk mitigation through comparison — running both systems simultaneously allows the team to verify that the new ERP produces the same outputs (financial postings, inventory balances, reports) as the proven legacy system. If discrepancies are found, the legacy system is still available as the authoritative source. The significant cost is operational: users and accounting staff must enter every transaction twice, which is time-consuming, error-prone, and unsustainable for long periods.
  - *Why A is incorrect:* Parallel run is actually one of the slower go-live strategies — it requires weeks of dual-system operation before legacy decommission. Big bang is typically the fastest. Also, parallel run does not require custom development to connect the systems — they run independently side by side.
  - *Why C is incorrect:* Parallel run has a defined end date — it is not intended to continue indefinitely. The goal is to transition fully to the new system after the validation period. If the legacy system is retained permanently, that is not a parallel run — it is a failed migration.
  - *Why D is incorrect:* The parallel run strategy does not eliminate the need for a cutback plan during the initial go-live — if the new system has critical issues even during the parallel period, the team may need to abort. Also, data migration happens before the parallel period begins in all cutover strategies, not uniquely in parallel run.

---

### Question 19

(5 points)

An organization completes an ERP implementation and transitions out of hypercare. Six months later, the help desk reports a spike in support tickets about the system "not working right" — but investigation reveals the tickets describe users working around the system rather than using it as designed. Which post-implementation concept does this pattern represent, and what is the recommended organizational response?

- A) Technical debt — the system requires re-implementation to fix underlying code issues
- B) Configuration drift — the system configuration has changed without approval
- C) Adoption regression — users have reverted to pre-ERP workarounds after the intensive support of hypercare ended; the recommended response is reinforcement through measurement of adoption metrics, manager accountability, refresher training, and renewed change management communication
- D) Data quality degradation — poor data entry is causing system errors; the recommended response is a data audit

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Adoption regression is the phenomenon where user behavior reverts toward old habits after the initial change management support (hypercare, intensive training) ends. Users who grudgingly adopted the new system during hypercare revert to familiar workarounds when support intensity drops. The ADKAR Reinforcement element addresses exactly this: sustained change requires ongoing measurement, management accountability, and visible consequences for non-adoption — not just an initial training event.
  - *Why A is incorrect:* Technical debt refers to accumulated shortcuts in code or configuration that create future maintenance problems. The description specifically states the system works correctly — users are choosing to work around it, not that the system is malfunctioning.
  - *Why B is incorrect:* Configuration drift means the system configuration has changed from its intended state, often through unauthorized changes. The symptom described is user behavioral workarounds, not system configuration changes.
  - *Why D is incorrect:* Data quality degradation could be a secondary symptom of adoption regression (if users are not entering data into the system), but the primary issue described is behavioral non-adoption, not a data quality problem that would cause system errors.

---

### Question 20

(5 points)

A company is deciding between a big bang cutover and a phased cutover for their SAP S/4HANA implementation across five business divisions. Which of the following correctly describes when a phased approach is preferable to a big bang approach?

- A) Phased is always preferable to big bang regardless of company size or complexity
- B) Big bang is preferable when the divisions are operationally interdependent and share master data; phased is preferable when divisions are operationally independent, the risk of a simultaneous cutover is too high, or the organization wants to apply lessons learned from early waves to later ones
- C) Big bang is always faster and phased is always safer — the choice is purely about risk tolerance
- D) Phased cutover is only appropriate when each division uses a different SAP module; if all divisions use the same modules, big bang is required

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The choice between big bang and phased depends on organizational structure and interdependency. Big bang is appropriate when all business units share tightly coupled processes, master data, or financial consolidation — because separate go-live dates would require complex bridging between the new and legacy systems. Phased is appropriate when divisions are operationally independent (separate P&Ls, separate supply chains), when risk management requires limiting the blast radius of any go-live issues, or when the organization wants to build organizational capability and apply lessons from early waves.
  - *Why A is incorrect:* Big bang is appropriate in many scenarios — particularly for smaller, tightly integrated organizations or when shared master data makes phasing impractical. Phased is not universally preferable.
  - *Why C is incorrect:* The statement "big bang is always faster" is generally true, but "the choice is purely about risk tolerance" oversimplifies the decision. Organizational interdependency is often the primary driver — phased cutover for tightly coupled divisions creates operational complexity (bridging between new SAP and legacy for shared transactions) that may introduce more risk than big bang.
  - *Why D is incorrect:* The cutover strategy decision is not determined by which SAP modules are used. Divisions can use the same modules and still have phased cutover if they are operationally independent. The module overlap is not the relevant factor — organizational coupling and shared master data are.
