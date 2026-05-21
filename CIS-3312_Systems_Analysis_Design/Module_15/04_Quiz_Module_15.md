# Quiz: Module 15 - Enterprise Architecture and Business Strategy Alignment
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
An organization's strategy team has documented five new strategic goals for the next three years. The BA team is asked to map current IT systems against these goals to identify which capabilities are well-supported, which are under-supported, and which have no supporting system at all. Which technique is the BA team performing?
*   A) Requirements prioritization — ranking system features by business value to guide sprint planning
*   B) Stakeholder analysis — identifying all parties affected by the strategic direction changes
*   C) Gap analysis — comparing the current state capabilities against the desired future state to identify investment needs
*   D) Feasibility analysis — assessing whether the proposed strategic goals are technically and economically achievable
*   **Correct Answer:** C) Gap analysis — comparing the current state capabilities against the desired future state to identify investment needs
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Requirements prioritization ranks known requirements by value; it does not compare current capabilities to future strategic goals.
    *   *Why B is incorrect:* Stakeholder analysis identifies parties and their interests; it is not the comparison of current vs. future state capabilities.
    *   *Why D is incorrect:* Feasibility analysis evaluates whether a specific proposed project is viable; the scenario describes a broader strategic capability assessment, not a single project evaluation.
    *   *Why C is correct:* Gap analysis (the core activity of BABOK® KA 3) compares current state to future state, identifies the gaps, and produces the evidence base for recommending which capabilities need investment. This is precisely what the scenario describes.

---

**Question 2**
In the context of enterprise architecture, which of the following is the most accurate definition of a **business capability map**?
*   A) A visual diagram showing the sequence of activities, gateways, and events in a business process from start to end
*   B) An organizational chart showing the reporting hierarchy of business units, departments, and team leads
*   C) A framework that categorizes all of an organization's capabilities — what it does — independent of how it does it or what technology supports it
*   D) A requirements traceability matrix linking each business requirement to the system component and test case that address it
*   **Correct Answer:** C) A framework that categorizes all of an organization's capabilities — what it does — independent of how it does it or what technology supports it
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A sequence of activities with gateways and events describes a BPMN process diagram, not a capability map.
    *   *Why B is incorrect:* An organizational chart shows reporting relationships between people/roles; a capability map shows what the organization is capable of doing, not who reports to whom.
    *   *Why D is incorrect:* Linking requirements to system components and test cases describes a requirements traceability matrix, not a capability map.
    *   *Why C is correct:* A business capability map is a technology-agnostic representation of what an organization does, organized into capability domains. It is used in EA to identify investment priorities, redundancy, and strategic gaps without prescribing solutions.

---

**Question 3**
Eighteen months after a new customer relationship management (CRM) system was deployed, a BA is asked to assess whether the system is delivering the expected business value. The original business case projected a 20% reduction in customer complaint resolution time. Current data shows a 7% reduction. Which BABOK® knowledge area covers this activity?
*   A) Business Analysis Planning and Monitoring (KA 2) — tracking the performance of BA activities
*   B) Elicitation and Collaboration (KA 4) — re-engaging stakeholders to gather updated requirements
*   C) Solution Evaluation (KA 7) — measuring whether the deployed solution delivers the expected value
*   D) Requirements Life Cycle Management (KA 5) — managing changes to the original requirements baseline
*   **Correct Answer:** C) Solution Evaluation (KA 7) — measuring whether the deployed solution delivers the expected value
*   **Distractor Analysis:**
    *   *Why A is incorrect:* KA 2 monitors the performance of BA work activities (are interviews on schedule, is documentation complete?), not the performance of deployed solutions.
    *   *Why B is incorrect:* KA 4 covers eliciting requirements from stakeholders; the scenario describes post-deployment performance measurement, not requirement gathering.
    *   *Why D is incorrect:* KA 5 manages the requirements lifecycle (traceability, changes, approval); the scenario is about measuring solution performance after deployment.
    *   *Why C is correct:* BABOK® KA 7 (Solution Evaluation) specifically covers measuring whether deployed solutions deliver expected value, analyzing performance gaps (7% vs. 20%), identifying solution limitations, and recommending actions to increase value — exactly what this post-deployment assessment describes.

---

**Question 4**
A BA is working on an enterprise IT modernization initiative. The project sponsor asks the BA to recommend which of 12 legacy applications should be retired, which should be upgraded, and which should be replaced with new systems. The BA uses a business capability map overlaid with current system coverage to make these recommendations. What EA decision framework is this analysis supporting?
*   A) Sprint planning — deciding which technical debt backlog items to address in the next two-week sprint
*   B) Application portfolio rationalization — optimizing the application portfolio to eliminate redundancy and close capability gaps
*   C) Data migration planning — identifying which legacy system data must be transferred to the new systems
*   D) Vendor selection — evaluating commercial software vendors against functional requirements
*   **Correct Answer:** B) Application portfolio rationalization — optimizing the application portfolio to eliminate redundancy and close capability gaps
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Sprint planning selects stories for a specific sprint; the scenario describes a strategic portfolio-level decision across 12 systems, not sprint-level work selection.
    *   *Why C is incorrect:* Data migration planning determines how to move data; the scenario involves deciding the strategic fate of each application, not data movement.
    *   *Why D is incorrect:* Vendor selection evaluates specific commercial products for purchase; the scenario assesses the entire existing portfolio, not a new purchase decision.
    *   *Why B is correct:* Application portfolio rationalization is the EA practice of reviewing all existing applications against business capabilities to identify which to retire (redundant or obsolete), modernize (valuable but aging), or replace (no longer fit for purpose). Using a capability map overlay is the standard technique for this analysis.

---

**Question 5**
After completing a gap analysis for a retail company, the BA finds that the company's strategic goal of "real-time inventory visibility across all stores" is not supported by any current system — stores still use nightly batch uploads to update central inventory. Which BABOK® Strategy Analysis output does this finding represent?
*   A) A defined change strategy — the plan for transitioning from batch to real-time inventory
*   B) A risk assessment — identifying the probability and impact of inventory discrepancies
*   C) A future state description — defining what the real-time inventory system will look like
*   D) A capability gap — the identified difference between the current batch-update capability and the strategic real-time visibility goal
*   **Correct Answer:** D) A capability gap — the identified difference between the current batch-update capability and the strategic real-time visibility goal
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A change strategy is the plan for moving from current state to future state; the finding (the gap) precedes the change strategy and informs it.
    *   *Why B is incorrect:* A risk assessment evaluates probability and impact of potential problems; identifying a capability gap is not the same as assessing a risk.
    *   *Why C is incorrect:* A future state description defines the desired end state (what real-time inventory will look like); the finding is about the gap between current and future state, not the definition of the future state itself.
    *   *Why D is correct:* A capability gap is the specific output of gap analysis in BABOK® KA 3 — the identified difference between current-state capability (nightly batch) and the strategic future-state goal (real-time visibility). This gap becomes the justification for the solution investment.
