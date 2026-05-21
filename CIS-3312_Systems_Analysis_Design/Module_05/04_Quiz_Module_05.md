# Quiz: Module 05 - Use Case Modeling and User Stories
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
In a use case diagram, what does the `<<include>>` relationship between two use cases indicate?
*   A) The included use case is optional and only executes when a specific condition is true
*   B) The included use case is always invoked as a mandatory part of the base use case
*   C) The included use case inherits all behaviors from the base use case through generalization
*   D) The included use case is performed by a secondary actor rather than the primary actor
*   **Correct Answer:** B) The included use case is always invoked as a mandatory part of the base use case
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Optional, condition-based execution describes the `<<extend>>` relationship, not `<<include>>`.
    *   *Why C is incorrect:* Inheritance of behavior is represented by a generalization relationship (open arrow), not `<<include>>`.
    *   *Why D is incorrect:* Actor involvement is shown by association lines, not by `<<include>>` relationships between use cases.
    *   *Why B is correct:* `<<include>>` indicates a mandatory sub-flow — every time the base use case runs, the included use case is also triggered; it is used to factor out shared behavior across multiple use cases.

---

**Question 2**
In Agile development, which of the following is the most accurate definition of **acceptance criteria**?
*   A) A prioritized list of all features and tasks the development team may be asked to build during the project
*   B) A set of specific, verifiable conditions that a user story must satisfy for the product owner to accept it as complete
*   C) A formal document signed by the project sponsor that authorizes the development team to begin construction
*   D) A series of automated regression tests that the development team runs before each code commit
*   **Correct Answer:** B) A set of specific, verifiable conditions that a user story must satisfy for the product owner to accept it as complete
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes the product backlog, not acceptance criteria.
    *   *Why C is incorrect:* This describes a project authorization document (project charter or sign-off), not acceptance criteria for a user story.
    *   *Why D is incorrect:* Automated regression tests are a QA/DevOps artifact; acceptance criteria define what "done" means for a story, not the testing automation implementation.
    *   *Why B is correct:* Acceptance criteria make user stories testable and define the completion boundary; they are typically written in Given/When/Then (Gherkin) or bulleted list format and reviewed by the product owner.

---

**Question 3**
A team writes the following user story: "As a customer service representative, I want to manage all customer records, billing histories, refund requests, order adjustments, and account notes so that I have everything in one place." Which INVEST quality problem does this story have?
*   A) It is not Independent — it depends on other stories to be completed first
*   B) It is not Valuable — there is no clear business benefit stated
*   C) It is not Small (too large / is an epic) — it covers too many features to be completed in a single sprint
*   D) It is not Negotiable — the implementation approach is already locked in
*   **Correct Answer:** C) It is not Small (too large / is an epic) — it covers too many features to be completed in a single sprint
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The story does not appear to depend on other stories; independence is not the primary issue.
    *   *Why B is incorrect:* The story states clear business value ("everything in one place"), so the Valuable criterion is met.
    *   *Why D is incorrect:* The story does not prescribe an implementation approach; negotiability is not the problem.
    *   *Why C is correct:* The story bundles five distinct features (records, billing, refunds, adjustments, notes) into a single item — a classic epic. It violates the Small criterion and should be split into individual, sprint-sized user stories.

---

**Question 4**
Which of the following correctly represents the standard user story format recommended by the Agile Alliance?
*   A) "The system shall allow a registered customer to reset their password via email verification within 30 seconds."
*   B) "As a registered customer, I want to reset my password via email so that I can regain access to my account without contacting support."
*   C) "Given a customer is locked out, when they request a password reset, then the system sends a reset email within 60 seconds."
*   D) "Password Reset: High Priority. Estimated effort: 3 story points. Assigned to Sprint 2."
*   **Correct Answer:** B) "As a registered customer, I want to reset my password via email so that I can regain access to my account without contacting support."
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This is a functional requirement written in IEEE "shall" format — not a user story.
    *   *Why C is incorrect:* This is an acceptance criterion written in Given/When/Then format — it defines done, but it is not the user story itself.
    *   *Why D is incorrect:* This is a backlog item metadata entry (priority, points, sprint), not a user story narrative.
    *   *Why B is correct:* "As a [role], I want [goal] so that [business value]" is the standard three-part user story format — it captures who benefits, what they want to do, and why it matters.

---

**Question 5**
A BA is building a product backlog for a new HR onboarding system. One item reads: "As an HR coordinator, I want to generate a new-hire welcome packet so that new employees have all their Day 1 materials before they arrive." The product owner wants to ensure this story is testable. What should be added?
*   A) A Gantt chart showing when in the project schedule the feature will be built
*   B) A use case diagram showing the HR coordinator as an actor interacting with the system
*   C) Specific acceptance criteria defining exactly what the welcome packet must contain and what constitutes successful generation
*   D) A data flow diagram showing how employee data moves through the onboarding process
*   **Correct Answer:** C) Specific acceptance criteria defining exactly what the welcome packet must contain and what constitutes successful generation
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Gantt chart is a scheduling artifact; it does not make the user story testable.
    *   *Why B is incorrect:* A use case diagram provides context and scope but does not define the acceptance conditions for a specific story.
    *   *Why D is incorrect:* A data flow diagram models the system's data movement; it does not define what "done" means for this user story.
    *   *Why C is correct:* Acceptance criteria specify the verifiable conditions the product owner will check when accepting the story — they are what make a user story testable, satisfying the "T" in the INVEST criteria.
