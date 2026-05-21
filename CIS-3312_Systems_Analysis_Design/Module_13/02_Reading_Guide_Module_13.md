# Reading Guide: Module 13 - Implementation and Change Management
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 13 – Implementation and Change Management**! A technically perfect system that is deployed without proper change management can still fail if users do not adopt it or if the organizational transition is not managed effectively. This module covers the implementation phase of the SDLC — deployment strategies, training, and the critically important human side of system change: organizational change management (OCM).

BABOK® Guide v3 Knowledge Area 3 (Strategy Analysis) and KA 7 (Solution Evaluation) both address the transition to the future state, and BABOK® explicitly identifies change management as a core business analysis concern. The ECBA exam tests whether candidates understand that deploying technology is only part of implementation — enabling people to change how they work is equally critical.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Deployment Strategy**: A deployment strategy is the planned approach for transitioning users and data from the existing (current state) system to the new (future state) system. The four primary strategies are: (1) Direct cutover (big bang) — switching all users over at once on a fixed date; (2) Phased rollout — deploying to one group or region at a time; (3) Parallel operation — running old and new systems simultaneously until confidence is established; (4) Pilot — deploying to a small representative group first to validate before full rollout.

*   **Organizational Change Management (OCM)**: Organizational Change Management is the structured process of managing the people side of change — ensuring that stakeholders understand, accept, and effectively adopt new processes, tools, and behaviors. OCM models (such as Prosci's ADKAR: Awareness, Desire, Knowledge, Ability, Reinforcement) provide frameworks for guiding individuals through change. Inadequate OCM is consistently cited as the primary cause of system implementation failures.

*   **Training Plan**: A training plan is a document that defines who needs to be trained on the new system, what they need to learn, in what format (classroom, e-learning, job aid, peer coaching), and by when. Training must be role-specific — end users need different training than administrators, who need different training than managers. Training delivered too early (before go-live) or too late (after users are confused) reduces effectiveness.

*   **Data Migration**: Data migration is the process of extracting data from legacy systems, transforming it to meet the new system's data structure and quality requirements, and loading it into the new system before go-live. Migration involves data cleansing (correcting errors, removing duplicates), transformation (mapping old field formats to new schemas), and validation (confirming data arrived correctly). Failed or incomplete data migration is a common implementation risk.

*   **Go-Live Readiness Assessment**: A go-live readiness assessment is a structured checklist review conducted in the days immediately before a planned system launch to confirm that all deployment prerequisites have been met: training complete, data migration validated, infrastructure stable, rollback plan documented, support team briefed, and key stakeholders signed off. Failing the readiness assessment typically delays go-live rather than proceeding with known risks.

*   **Transition Requirements**: In BABOK® KA 3, transition requirements are a specific requirement type that describes capabilities the solution must have to support the transition from the current state to the future state but that are not needed once the transition is complete. Examples include: data migration scripts, parallel-run reporting, user training materials embedded in the system, and bulk data import utilities. Transition requirements are temporary by definition and are separate from persistent solution requirements.

---

### 2. Certification Exam Tips
*   **Transition Requirements are Temporary**: The ECBA exam tests the distinction between solution requirements (permanent) and transition requirements (needed only during cutover). If a requirement is only needed to support the move from old to new (e.g., a data import tool), it is a transition requirement. Know this category specifically because it appears as a named output in BABOK® KA 3.
*   **Deployment Strategy Trade-offs**: Know when each strategy is most appropriate: Big bang → fast, low cost, high risk; Parallel operation → low risk, high cost, resource-intensive; Phased rollout → balanced risk and effort; Pilot → validates before full commitment. The ECBA exam will present a scenario and ask which strategy is most appropriate based on risk tolerance and available resources.
*   **ADKAR Model**: The ADKAR model (Awareness → Desire → Knowledge → Ability → Reinforcement) is the most commonly tested OCM framework on business analysis certifications. Know what each element means and how a BA addresses each through stakeholder engagement, training, and reinforcement activities.
*   **Study Resource**: Prosci, the developer of the ADKAR model, publishes free OCM articles and the full ADKAR overview at [https://www.prosci.com/adkar/](https://www.prosci.com/adkar/) — this is the primary reference for the OCM concepts tested on the ECBA exam.

---

### Required Readings & Videos
*   **Required Reading**: BABOK® Guide v3 Chapter 4 (Strategy Analysis) — "Assess Risks" and "Define Transition State and Release Plan." These tasks define transition requirements and release planning. Also review BABOK® KA 7 (Solution Evaluation) Task "Recommend Actions to Increase Solution Value," which includes change management recommendations.
*   **Supplemental Reading**: Review the Prosci ADKAR model overview at [https://www.prosci.com/adkar/](https://www.prosci.com/adkar/) — the free article series explains each of the five ADKAR elements with practical examples directly relevant to system implementation scenarios.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Given a project scenario, recommend a deployment strategy (big bang, phased, parallel, or pilot) with a written justification referencing the project's risk profile and resource constraints.
*   Identify three transition requirements for the same scenario that are needed only during cutover and explain why each is temporary.
*   Create a one-page go-live readiness checklist with at least eight items organized into categories (training, data, infrastructure, communication, support).

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Read BABOK® Guide v3 Chapter 4 — "Assess Risks" and "Define Transition State and Release Plan."
- [ ] Watch the Module 13 video lecture.
- [ ] Review the Prosci ADKAR model overview at [https://www.prosci.com/adkar/](https://www.prosci.com/adkar/).
- [ ] Complete the deployment strategy and go-live readiness lab before taking the quiz.
