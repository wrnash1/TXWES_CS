# Reading Guide: Module 12 – Test-Driven Development (TDD) and BDD

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Introduction

Welcome to **Module 12 – Test-Driven Development (TDD) and BDD**! TDD and its behavioral extension BDD are the technical practices most directly aligned with Scrum's commitment to delivering a potentially releasable Increment every Sprint. Teams that practice TDD produce code with built-in verification and significantly lower defect rates — enabling the sustainable pace the Agile Manifesto calls for.

The PSM I expects you to understand TDD's Red-Green-Refactor cycle and how these practices support Scrum's empirical framework. BDD extends TDD by writing tests in human-readable language that bridges the gap between Product Owners, stakeholders, and Developers — directly supporting Scrum's collaborative requirements approach.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Test-Driven Development (TDD):** A software development practice in which developers write a failing automated test before writing any production code. The development cycle proceeds in three steps: Red (write a failing test), Green (write the minimum code to make it pass), and Refactor (improve the code structure without changing its behavior). TDD produces executable specifications and a comprehensive regression test suite as a natural byproduct.

* **Red-Green-Refactor cycle:** The three-phase TDD loop: (1) Red — write a test that fails because the feature does not exist yet; (2) Green — write just enough code to make the test pass; (3) Refactor — clean up the code, improving design while keeping all tests green. The cycle repeats for each small piece of new behavior.

* **Behavior-Driven Development (BDD):** An extension of TDD that describes system behavior in natural language using the Gherkin format (Given-When-Then), making test scenarios readable by non-technical stakeholders. BDD closes the communication gap between Product Owners, QA, and Developers by expressing acceptance criteria as executable specifications.

* **Given-When-Then (Gherkin):** The BDD scenario format: Given (a system state or precondition), When (an action or event occurs), Then (an expected outcome is observed). Example: Given the user is logged in, When they click "Delete Account," Then a confirmation dialog appears. Tools like Cucumber and Behave execute these scenarios as automated tests.

* **Unit test:** An automated test that verifies a single unit of code (a function, method, or class) in isolation from external dependencies. Unit tests are fast, deterministic, and form the base of the test pyramid. In TDD, unit tests are written before the code they test.

---

### 2. Certification Exam Tips

* **PSM I Focus — TDD supports Sprint commitments:** Scrum's Definition of Done typically includes automated test coverage as a quality gate. TDD is the practice that builds this coverage as a natural consequence of development rather than as a separate phase. Questions about why a team consistently fails to meet the Definition of Done often have "lack of TDD or automated testing" as the root cause.
* **Scenario Trap — Writing tests after code:** A common scenario presents a team that writes all code first and adds tests at the end. This is integration testing or regression testing, not TDD. TDD requires tests to be written before the code they verify.
* **BDD as a collaboration tool:** BDD scenarios written in Given-When-Then can be reviewed and approved by the Product Owner before development begins — serving as executable acceptance criteria. PSM I questions may test whether you recognize that BDD scenarios are authored collaboratively, not just by developers.
* **Refactor does not mean "add features":** The Refactor phase in TDD is strictly about improving code structure (naming, reducing duplication, applying patterns) while keeping existing tests green. Adding new behavior requires a new Red-Green-Refactor cycle.
* **Study Resource:** [Test-Driven Development: By Example — Kent Beck](https://www.oreilly.com/library/view/test-driven-development/0321146530/) is the canonical TDD reference. The [Cucumber BDD documentation](https://cucumber.io/docs/gherkin/) covers Gherkin syntax and BDD principles for free.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** [TDD — Agile Alliance Glossary](https://www.agilealliance.org/glossary/tdd/) and [BDD — Agile Alliance Glossary](https://www.agilealliance.org/glossary/bdd/) — concise free definitions of both practices with their relationship to Agile and Scrum.
* **Required Video:** [Test Driven Development — What Is It and How Do You Use It? – Web Dev Simplified](https://www.youtube.com/watch?v=Jv2uxzhPFl4) — practical Red-Green-Refactor demonstration with a live coding walkthrough. (~14 min)

---

### Lab & Command Integration

In this week's hands-on lab, you will:

* **Practice the Red-Green-Refactor cycle:** Given a specification for a simple string-processing function, write a failing test, implement minimum code to make it pass, then refactor the implementation — cycling through at least three feature additions.
* **Write BDD scenarios:** For two user stories from your Module 07 lab, write Given-When-Then BDD scenarios (at least two per story) using language your Product Owner and stakeholders could read and validate.
* **Run tests and measure coverage:** Execute your test suite using pytest, generate a coverage report, and identify any uncovered code paths.

---

### 3. Study Checklist

* [ ] Read the Agile Alliance TDD and BDD glossary entries.
* [ ] Be able to explain the Red-Green-Refactor cycle in sequence without notes.
* [ ] Write at least one Given-When-Then BDD scenario from a user story you created in a previous module.
* [ ] Watch the required video and observe how the developer writes the test before the implementation exists.
* [ ] Proceed to the weekly hands-on lab activity.
