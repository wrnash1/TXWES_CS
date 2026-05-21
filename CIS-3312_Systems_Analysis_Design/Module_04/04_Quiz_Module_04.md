# Quiz: Module 04 - Requirements Analysis and Documentation
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
Which of the following is an example of a non-functional requirement?
*   A) The system shall allow an administrator to create, edit, and deactivate user accounts.
*   B) The system shall generate a monthly sales report in PDF format.
*   C) The system shall respond to any search query within 2 seconds under normal load conditions.
*   D) The system shall send an email notification when an order status changes to "Shipped."
*   **Correct Answer:** C) The system shall respond to any search query within 2 seconds under normal load conditions.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is a functional requirement — it describes a specific behavior (user account management) the system must perform.
    *   *Why B is incorrect:* This is a functional requirement — it describes a specific output behavior (generating a PDF report).
    *   *Why D is incorrect:* This is a functional requirement — it describes a triggered system action (sending an email notification).
    *   *Why C is correct:* This is a non-functional requirement (performance/quality attribute) — it specifies *how well* the system must perform a search function, not what function it performs.

---

**Question 2**
In requirements engineering, which of the following is the most accurate definition of **requirements traceability**?
*   A) The process of distributing approved requirements documents to all project stakeholders through the project communication plan
*   B) The ability to link each requirement forward to the design, test cases, and implementation that satisfy it, and backward to the business need that originated it
*   C) A technique for prioritizing requirements by assigning each requirement a numerical score based on business value and implementation effort
*   D) The activity of rewriting requirements that stakeholders found unclear after the initial review meeting
*   **Correct Answer:** B) The ability to link each requirement forward to the design, test cases, and implementation that satisfy it, and backward to the business need that originated it
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Distributing documents is a communication task, not traceability.
    *   *Why C is incorrect:* This describes a requirements prioritization technique (such as MoSCoW or weighted scoring), not traceability.
    *   *Why D is incorrect:* Rewriting unclear requirements is part of verification/refinement, not traceability.
    *   *Why B is correct:* Requirements traceability provides bidirectional linkage — from business needs through requirements to design, implementation, and tests — enabling impact analysis and completeness confirmation.

---

**Question 3**
A BA presents a completed requirements document to stakeholders for review. A stakeholder confirms that all the requirements are clearly written and internally consistent but says, "These requirements don't solve our actual business problem — you've documented what the old system does, not what we need the new system to do." Which activity has failed?
*   A) Requirements verification
*   B) Requirements elicitation
*   C) Requirements validation
*   D) Requirements prioritization
*   **Correct Answer:** C) Requirements validation
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Requirements verification checks that requirements are well-formed (clear, complete, consistent, testable). The stakeholder confirmed they are clearly written — verification passed.
    *   *Why B is incorrect:* While the elicitation may have been flawed, the activity that specifically failed here is the confirmation that requirements match the business need, which is validation.
    *   *Why D is incorrect:* Prioritization is the ordering of requirements by importance; it is not what failed in this scenario.
    *   *Why C is correct:* Requirements validation answers "Are we building the right thing?" — confirming requirements reflect actual business needs. The stakeholder's feedback reveals that validation failed because the requirements describe the wrong future state.

---

**Question 4**
Which of the following best describes a *business rule* as opposed to a functional requirement?
*   A) A statement describing how fast the system must process transactions
*   B) A constraint or policy from the business domain that the system must enforce, such as "All purchase orders over $10,000 require dual approval"
*   C) A specific system behavior triggered by a user action, such as "clicking Save stores the record to the database"
*   D) A diagram showing the relationships between data entities stored in the system database
*   **Correct Answer:** B) A constraint or policy from the business domain that the system must enforce, such as "All purchase orders over $10,000 require dual approval"
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a non-functional requirement (performance), not a business rule.
    *   *Why C is incorrect:* This describes a functional requirement — a specific system behavior in response to a user action.
    *   *Why D is incorrect:* This describes an entity-relationship diagram, a data modeling artifact, not a business rule definition.
    *   *Why B is correct:* Business rules are domain-level constraints — policies, regulations, or operational procedures — that constrain system behavior but originate in the business context, not in the technology. The dual-approval threshold is a classic example from financial policy.

---

**Question 5**
A project team is preparing to hand off the requirements baseline to the development team. The BA wants to ensure that every requirement can be confirmed as implemented and tested. Which artifact should the BA create or update for this purpose?
*   A) A stakeholder register listing each stakeholder's role and communication preferences
*   B) A risk register documenting project uncertainties and their probability/impact scores
*   C) A requirements traceability matrix (RTM) linking each requirement to design components and test cases
*   D) A project schedule showing milestones and task assignments for the development team
*   **Correct Answer:** C) A requirements traceability matrix (RTM) linking each requirement to design components and test cases
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A stakeholder register documents stakeholder information for engagement planning; it does not link requirements to test cases or implementation.
    *   *Why B is incorrect:* A risk register tracks project uncertainties; it does not provide the requirement-to-test linkage the BA needs.
    *   *Why D is incorrect:* A project schedule manages timing and resource assignments; it does not ensure requirements coverage.
    *   *Why C is correct:* An RTM explicitly maps each requirement to the design element and test case that address it, giving the team a tool to confirm complete implementation and test coverage as development progresses.
