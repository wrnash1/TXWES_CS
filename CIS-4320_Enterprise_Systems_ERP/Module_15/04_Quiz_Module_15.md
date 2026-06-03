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

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials
