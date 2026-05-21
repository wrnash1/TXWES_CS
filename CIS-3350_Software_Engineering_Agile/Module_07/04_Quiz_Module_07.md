# Quiz: Module 07 – User Stories and Acceptance Criteria

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

A user story reads: "As a registered customer, I want to reset my password via email so that I can regain access to my account if I forget my credentials." Which INVEST criterion does this story most clearly demonstrate?

* A) Independent — it can be developed without relying on other stories
* B) Valuable — it delivers clear, specific value to a named user type
* C) Estimable — the team can size it accurately because it has acceptance criteria
* D) Small — it will fit within a single Sprint without further splitting

Correct Answer: B) The story explicitly names a user type (registered customer) and states why the feature has value (regaining account access), satisfying the Valuable criterion.

Distractor Analysis:

* *Why B is correct:* A "Valuable" story must clearly identify who benefits and why. This story does both — specifying the user role and the business/user outcome of the feature.
* *Why A is incorrect:* Independence cannot be assessed from the story text alone; password reset likely depends on authentication infrastructure.
* *Why C is incorrect:* Estimability requires knowing technical complexity — having acceptance criteria helps but is not shown in the story text above.
* *Why D is incorrect:* Whether the story fits a Sprint depends on team velocity and technical complexity — not determinable from the story text alone.

---

### Question 2

Which of the following is the most accurate definition of acceptance criteria?

* A) The organization-wide quality standard all Increments must meet to be considered releasable.
* B) Specific, testable conditions agreed between the Product Owner and Developers that define when a particular user story is complete.
* C) A list of all features the Product Owner wants delivered by the end of the product's development.
* D) The Scrum Master's checklist used to verify that the team followed Scrum processes during the Sprint.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Acceptance criteria are story-specific — they define the boundaries of a single user story and are agreed upon before work begins so both parties share a definition of done for that story.
* *Why A is incorrect:* This describes the Definition of Done, which is an increment-level standard applied to all work — not story-specific acceptance criteria.
* *Why C is incorrect:* This describes a feature list or product roadmap, not acceptance criteria for individual stories.
* *Why D is incorrect:* The Scrum Master coaches process adherence but does not use a checklist to "verify" Scrum rule compliance — and acceptance criteria are about product functionality, not process.

---

### Question 3

A team has the following user story: "As a user, I want the system to be fast." Which INVEST criterion does this story fail most critically?

* A) Independent — it cannot be developed in isolation from other stories
* B) Negotiable — the Product Owner refuses to discuss scope changes
* C) Testable — there is no objective, verifiable condition to confirm the story is complete
* D) Small — the story is too large to complete in a single Sprint

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* "Fast" is subjective and not measurable. Without a specific performance threshold (e.g., "page loads in under 2 seconds for 95% of requests"), the story cannot be verified as complete — it fails the Testable criterion.
* *Why A is incorrect:* Performance improvements typically do depend on other work, but the most critical failure here is testability — not independence.
* *Why B is incorrect:* Negotiability refers to whether story details are open for discussion before the Sprint; the problem here is vague scope, not a Product Owner refusing to negotiate.
* *Why D is incorrect:* The story may or may not be too large — that is indeterminate without a specific scope. The primary failure is that it cannot be tested as written.

---

### Question 4

What is the key difference between a user story's acceptance criteria and the team's Definition of Done?

* A) Acceptance criteria are written by the Scrum Master; the Definition of Done is written by the Product Owner.
* B) Acceptance criteria define story-specific conditions; the Definition of Done is a quality standard applied to every Increment the team produces.
* C) The Definition of Done is optional; acceptance criteria are mandatory for all backlog items.
* D) Acceptance criteria are set by stakeholders after Sprint Review; the Definition of Done is set before Sprint Planning.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Acceptance criteria vary per story and define what makes that specific story complete. The Definition of Done is a fixed quality bar that every Increment must meet, regardless of which stories it contains.
* *Why A is incorrect:* Acceptance criteria are collaboratively agreed between the Product Owner and Developers; the Definition of Done is created by Developers (or the organization). Neither is written by the Scrum Master alone.
* *Why C is incorrect:* The Scrum Guide does not make the Definition of Done optional — every Increment must meet it. Acceptance criteria are also typically required for stories to be ready for Sprint Planning.
* *Why D is incorrect:* Acceptance criteria are agreed before Sprint work begins, not set after the Sprint Review. The Definition of Done is established before Sprint Planning, not "after" anything.

---

### Question 5

A large user story (epic) is estimated at 40 story points and the team's Sprint velocity is 20 points. What is the most appropriate action?

* A) Extend the Sprint length to two months so the epic can be completed in a single Sprint.
* B) Ask the Scrum Master to break the epic into sub-tasks and assign them to individual Developers.
* C) Split the epic into smaller, independently deliverable stories that each fit within a Sprint's capacity.
* D) Keep the epic as a single backlog item and carry it across multiple Sprints without splitting.

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Story splitting is the standard practice for making an oversized story Sprint-ready. Each resulting story should independently deliver value and be completable within a single Sprint.
* *Why A is incorrect:* Sprints are timeboxed to one month or less — extending to two months violates the Scrum Guide's Sprint definition and removes the fast feedback loop.
* *Why B is incorrect:* The Scrum Master does not break down stories or assign tasks to Developers. Story decomposition is a collaborative responsibility of the Product Owner and Developers.
* *Why D is incorrect:* Carrying a single story across multiple Sprints means no Increment is delivered from that story until the end — violating the principle of delivering potentially releasable value each Sprint.
