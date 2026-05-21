# Quiz: Module 12 – Test-Driven Development (TDD) and BDD

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

What is the correct sequence of phases in the Test-Driven Development (TDD) cycle?

* A) Refactor, Write Code, Write Test
* B) Write Test (Red), Implement Code (Green), Refactor
* C) Design, Code, Test, Release
* D) Deploy, Assert, Cleanup

Correct Answer: B) TDD proceeds in a tight loop: write a failing test (Red), implement just enough code to make it pass (Green), then improve the code structure without changing behavior (Refactor).

Distractor Analysis:

* *Why B is correct:* The Red-Green-Refactor sequence is the defining characteristic of TDD. Tests are always written before the code they verify.
* *Why A is incorrect:* Starting with Refactor before writing a test or code makes no sense — there is nothing to refactor yet. This sequence reverses TDD's intent entirely.
* *Why C is incorrect:* Design-Code-Test-Release is a Waterfall phase model, not TDD. TDD does not have a separate "design" phase before coding — the test serves as the design specification.
* *Why D is incorrect:* Deploy-Assert-Cleanup is not a recognized development cycle. It conflates deployment with testing in a way that does not reflect TDD practice.

---

### Question 2

Which of the following is the most accurate definition of Behavior-Driven Development (BDD)?

* A) A testing methodology where QA engineers write automated regression tests after all development is complete.
* B) An extension of TDD that expresses system behaviors in natural language (Given-When-Then) so that tests serve as executable specifications readable by non-technical stakeholders.
* C) A deployment strategy that releases new features to a small subset of users before full rollout to detect behavioral regressions.
* D) A project management approach where the Product Owner defines system behavior and Developers implement it without discussion.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* BDD bridges the collaboration gap between technical and non-technical team members by writing test scenarios in human-readable Gherkin (Given-When-Then) format that can be validated by the Product Owner before development and executed as automated tests.
* *Why A is incorrect:* Writing tests after all development is complete is regression testing, not TDD or BDD. Both TDD and BDD require tests to be written before or alongside production code.
* *Why C is incorrect:* This describes a canary release or feature flag deployment strategy — unrelated to BDD as a development practice.
* *Why D is incorrect:* BDD is explicitly collaborative — Product Owners, QA, and Developers author scenarios together. It is not a one-way specification delivery model.

---

### Question 3

A developer writes the following BDD scenario: "Given a logged-in user, When they submit an empty search query, Then an error message 'Please enter a search term' is displayed." At what point in the Sprint should this scenario be written?

* A) After the search feature is fully implemented and manually tested
* B) Before the implementation code is written, to serve as the acceptance criterion driving development
* C) During the Sprint Review, when stakeholders can validate the scenario against the live system
* D) During the Sprint Retrospective, when the team reflects on what was built

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* In BDD, scenarios are written collaboratively before implementation begins — they serve as executable acceptance criteria that define what "done" looks like for the story, driving the development from the outside in.
* *Why A is incorrect:* Writing BDD scenarios after implementation converts them from specifications into documentation. This misses BDD's core purpose of guiding development and catching specification ambiguities early.
* *Why C is incorrect:* Sprint Review inspects completed Increments. Writing scenarios during the review would mean development happened without a clear acceptance criterion.
* *Why D is incorrect:* Sprint Retrospective is for process improvement, not for defining product acceptance criteria.

---

### Question 4

During the Refactor phase of the TDD cycle, a developer adds a new "export to CSV" feature while cleaning up existing code. What is wrong with this approach?

* A) Refactoring should only happen in the Sprint Retrospective, not during active development.
* B) The Refactor phase is strictly for improving existing code structure — adding new features requires starting a new Red-Green-Refactor cycle.
* C) CSV export is a non-functional requirement and should be added to the Definition of Done, not the Sprint Backlog.
* D) Nothing is wrong — the Refactor phase is the appropriate time to add new features because tests are already passing.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* The Refactor phase is exclusively for restructuring code — improving naming, eliminating duplication, applying patterns — without changing external behavior. Adding a new feature during Refactor bypasses the Red phase and skips the failing test that should drive the new behavior.
* *Why A is incorrect:* Refactoring happens continuously during development as part of the TDD cycle — not only during the Sprint Retrospective.
* *Why C is incorrect:* CSV export is a functional feature, not a non-functional requirement. Its placement in the Definition of Done vs. Sprint Backlog depends on whether it is a universal quality standard or a specific deliverable.
* *Why D is incorrect:* Adding features without a failing test violates TDD's core discipline. Tests must be written first to ensure the new behavior is intentional and verifiable.

---

### Question 5

A Scrum Team never practices TDD and instead writes manual tests at the end of each Sprint. Over time, the team notices their Sprint velocity is declining and they spend more time fixing bugs than building new features. What is the most likely root cause?

* A) The Sprint timeboxes are too short and need to be extended to one month.
* B) Accumulating technical debt from untested code makes each Sprint's work harder and riskier as the codebase grows.
* C) The Product Owner is adding too many backlog items to each Sprint, exceeding the team's capacity.
* D) The Scrum Master is not facilitating the Daily Scrum correctly, causing misalignment.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Without automated test coverage built incrementally through TDD, defects accumulate and interactions between features become unpredictable. The team spends increasing Sprint capacity on regression fixes rather than new value delivery — a classic technical debt spiral.
* *Why A is incorrect:* Sprint timebox length does not determine defect accumulation rates. A longer Sprint with the same testing practices would produce the same accumulation problem over a longer period.
* *Why C is incorrect:* Over-commitment is a separate Sprint Planning problem. The specific symptom described — more bug-fixing over time — points to codebase quality, not Sprint commitment size.
* *Why D is incorrect:* Daily Scrum facilitation issues affect daily alignment, not the long-term trend of increasing defect rates. The described pattern is a code quality and testing practice problem.
