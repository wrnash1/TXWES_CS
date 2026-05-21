# Reading Guide: Module 12 - Software Testing and Quality Assurance
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 12 – Software Testing and Quality Assurance**! Testing ensures that the system built actually satisfies the requirements defined by business analysts and stakeholders. This module covers the testing landscape from a business analyst perspective — the types of testing, how requirements drive test design, the BA's role in acceptance testing, and quality assurance principles that span the entire SDLC.

For the ECBA exam, testing is important because BABOK® Guide v3 treats acceptance testing as a BA responsibility and links testing directly to requirements traceability. Understanding how each test type maps to requirements helps you answer scenario questions about which testing activity is appropriate at a given SDLC stage.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Unit Testing**: Unit testing is the lowest level of software testing, in which individual components or functions are tested in isolation to verify that each performs its intended behavior correctly. Unit tests are typically written and executed by developers, often using testing frameworks (e.g., JUnit, pytest). From a BA perspective, unit tests validate that the code correctly implements individual business rules and functional requirements at the component level.

*   **Integration Testing**: Integration testing verifies that multiple components or systems work together correctly when combined. Where unit testing isolates individual pieces, integration testing checks the interfaces and data flows between them. Integration issues — such as incorrect data formats passed between systems, missing fields, or incorrect API responses — are commonly discovered during this phase. System integration testing (SIT) is the enterprise-scale version of this activity.

*   **User Acceptance Testing (UAT)**: User Acceptance Testing is the final testing phase before a system is deployed, in which business users and stakeholders verify that the system satisfies the agreed-upon requirements and is fit for purpose. UAT is business-driven rather than technically focused — users execute real business scenarios using realistic data to confirm the system supports their actual work. UAT sign-off (formal acceptance) is typically required before production deployment. The BA often facilitates or coordinates UAT.

*   **Regression Testing**: Regression testing is the re-execution of previously passed test cases after a system change (bug fix, new feature, or configuration change) to ensure that existing functionality has not been broken by the change. In Agile environments, automated regression test suites run after every code commit to catch regressions early. The BA's concern with regression testing is ensuring that requirements met in a previous release are not inadvertently broken by new development.

*   **Test Case**: A test case is a documented set of conditions, inputs, actions, and expected results that defines a specific scenario to be tested. A well-written test case is derived directly from a requirement and is specific enough that any tester can reproduce the same steps and determine pass/fail without ambiguity. BAs are often responsible for writing or reviewing acceptance test cases, which directly trace back to user stories or functional requirements.

*   **Defect (Bug)**: A defect is a variance between the expected behavior (as defined by requirements or acceptance criteria) and the actual behavior observed during testing. Defects are logged in a defect tracking system with severity (impact on business operation) and priority (urgency of fix). The BA's role in defect management includes clarifying whether an observed behavior is truly a defect (requirements were not met) or a change request (the requirement itself needs updating).

---

### 2. Certification Exam Tips
*   **UAT is a BA Responsibility**: The ECBA exam expects you to know that BAs facilitate User Acceptance Testing — writing UAT test cases from requirements, coordinating UAT sessions with business stakeholders, and managing defects vs. change requests. This is explicitly covered in BABOK® KA 5 and KA 7.
*   **Test Type Sequencing**: Know the standard testing sequence: unit → integration → system → UAT → production. The ECBA exam may describe a defect found and ask at which testing phase it should have been caught. A data format mismatch between two services → integration testing. A business rule violation not visible until full workflow → system or UAT.
*   **Defect vs. Change Request**: A critical ECBA scenario type: a user finds unexpected behavior during UAT. If the system does what the requirements say but the user wants something different → change request (requirements change needed). If the system does NOT do what the requirements say → defect (fix needed). BAs must distinguish these correctly or the project scope spirals.
*   **Study Resource**: The ISTQB (International Software Testing Qualifications Board) publishes a free glossary and foundation-level syllabus at [https://www.istqb.org/](https://www.istqb.org/) — while ISTQB is a testing certification, its terminology and test type definitions align directly with ECBA exam testing concepts.

---

### Required Readings & Videos
*   **Required Reading**: BABOK® Guide v3 Chapter 8 (Solution Evaluation), Task "Evaluate Solution Performance" — covers how BAs assess whether deployed solutions meet requirements. Also review BABOK® Techniques — "Acceptance and Evaluation Criteria Definition" and "Reviews."
*   **Supplemental Reading**: Review the ISTQB Foundation Level Syllabus overview (testing types section) freely available at [https://www.istqb.org/](https://www.istqb.org/) — this provides the standard vocabulary for test type definitions that appears on the ECBA exam.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Write three test cases (in Given/When/Then format) for three functional requirements from a provided requirements document, ensuring each test case has a clear pass/fail criterion.
*   Given a defect report and requirements document, classify each of five defects as either a true defect (system fails to meet requirement) or a change request (new stakeholder desire beyond the current requirement).
*   Create a simple test coverage matrix mapping three requirements to their test cases and indicating current pass/fail status.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Read BABOK® Guide v3 Chapter 8 — "Evaluate Solution Performance" and Techniques for "Acceptance and Evaluation Criteria Definition."
- [ ] Watch the Module 12 video lecture.
- [ ] Review the ISTQB glossary and test type definitions at [https://www.istqb.org/](https://www.istqb.org/).
- [ ] Complete the test case writing and defect classification lab before taking the quiz.
