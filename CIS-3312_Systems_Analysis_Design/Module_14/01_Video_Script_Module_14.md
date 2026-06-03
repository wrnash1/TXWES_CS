# Video Script: Module 14 — Testing, Validation, and Quality Assurance

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Production Notes

- **Runtime Target:** 20–24 minutes
- **Format:** Lecture with document examples and process diagrams
- **Slides:** Approximately 27 slides

---

## SEGMENT 1 — Introduction (0:00–2:30)

[OPEN on slide: "Module 14 — Testing, Validation, and Quality Assurance"]

Welcome back to CIS-3312. I'm Professor Nash. Module 14 is about testing, validation, and quality assurance — the phase where everything comes together and we find out whether the system we built actually does what we said it would do.

Here is the hard truth about this phase: most project failures are not discovered during testing. They are caused by bad requirements that were never tested at all. Requirements that were ambiguous. Requirements that were assumed rather than validated. Requirements that said "the system shall be user-friendly" without defining what friendly means.

Testing is the mechanism by which requirements are proven. As a business analyst, your role in testing is not to write code or configure servers. Your role is to ensure that every requirement has a corresponding test — and that the test actually verifies the right thing.

In this module we cover four core topics: the requirements traceability matrix, test case development, user acceptance testing, and defect management. We close with sign-off criteria — how you know when a system is ready to go live.

Let's begin.

---

## SEGMENT 2 — The Requirements Traceability Matrix (2:30–6:00)

[SLIDE: "The Requirements Traceability Matrix — RTM"]

The Requirements Traceability Matrix, or RTM, is one of the most important documents a BA produces. Its purpose: ensure that every requirement is tested and every test traces to a requirement.

An RTM is essentially a linkage table. Each row represents a requirement. The columns extend across the full development lifecycle — from business need to design to test case to test result to deployment.

Here is a simplified structure:

| Req ID | Requirement Description | Design Reference | Test Case ID | Test Status | Defect ID |
|---|---|---|---|---|---|
| FR-001 | User shall be able to reset password via email | UI-Screen-05 | TC-023 | Pass | — |
| FR-002 | System shall lock account after 5 failed logins | Auth-Logic-02 | TC-024 | Fail | DEF-047 |

The RTM serves several critical purposes.

First: it prevents requirement orphans. Without an RTM, requirements can quietly drop out of scope during development. The RTM makes every omission visible.

Second: it prevents test orphans. If a test case has no corresponding requirement, someone invented something to test that was never asked for. That is scope creep.

Third: it enables impact analysis. When a requirement changes, the RTM immediately shows which test cases and design elements are affected.

Fourth: it provides audit evidence. In regulated industries — healthcare, finance, government — the RTM is a compliance artifact that proves requirements were tested.

Building the RTM is a BA responsibility. It starts when requirements are first approved and is updated continuously through testing and into deployment.

---

## SEGMENT 3 — Test Case Development (6:00–10:30)

[SLIDE: "Writing Test Cases — Structure and Standards"]

A test case is a specific, documented procedure for verifying that a system behavior meets a stated requirement. The keyword is specific. Vague test cases produce vague results.

A well-written test case contains seven components.

**Test Case ID:** A unique identifier that links back to the RTM.

**Requirement Reference:** The ID of the requirement being tested.

**Test Objective:** One sentence describing what the test is designed to verify.

**Preconditions:** The state the system must be in before the test begins. "User must be logged in." "Account balance must be greater than zero."

**Test Steps:** Numbered, specific actions the tester performs. Not "navigate to transfers." Instead: "1. Click the Transfers menu item. 2. Select 'External Transfer' from the dropdown."

**Expected Results:** The specific, observable outcome that indicates the requirement is met. Not "the transfer works." Instead: "A confirmation message displays 'Transfer of $500.00 scheduled for 03/15/2026' and an email confirmation is sent to the registered email address within two minutes."

**Actual Results and Pass/Fail:** Recorded during execution.

Let me say something about expected results, because this is where most test cases fail. If your expected result can be interpreted multiple ways, your test is not reliable. "The system displays a message" is not a good expected result. "The system displays the message 'Transfer successful — confirmation number TXN-20260315-00142'" is a good expected result.

[SLIDE: "Test Case Types"]

There are several types of test cases a BA works with.

**Functional test cases** verify that the system does what it is supposed to do. Most requirements produce functional test cases.

**Negative test cases** verify that the system correctly handles invalid inputs and edge cases. What happens when a user enters letters in a numeric field? What happens when a required field is left blank? These tests are just as important as positive functional tests.

**Boundary test cases** test the edges of valid ranges. If a field accepts values from 1 to 100, boundary tests check 0, 1, 100, and 101.

**Integration test cases** verify that separately developed components work correctly together.

**Regression test cases** verify that changes to the system did not break functionality that was previously working.

---

## SEGMENT 4 — User Acceptance Testing (10:30–15:00)

[SLIDE: "UAT — The Business Test"]

User Acceptance Testing, or UAT, is the final formal testing phase before a system goes live. It is conducted by end users and business stakeholders — not by the development team or QA analysts.

The purpose of UAT is to confirm that the system meets business needs in real-world conditions. System testing, performed by the development team, confirms that the system works technically. UAT confirms that it works for the people who will actually use it.

This distinction matters enormously. A system can pass every technical test and still fail UAT. Why? Because technical tests verify code against specifications. UAT verifies the solution against business reality.

[SLIDE: "UAT Process Steps"]

Here is the standard UAT process.

**Step 1 — Plan UAT.** Define the scope, participants, environment, timeline, and entry criteria. Entry criteria are the conditions that must be met before UAT begins. Common entry criteria: all functional test cases have passed, all critical defects are resolved, test data is loaded, user accounts are provisioned.

**Step 2 — Prepare test scenarios.** UAT test scenarios are different from technical test cases. They are business scenarios — end-to-end workflows that represent real work. "Process a full insurance claim from intake through payment authorization." Not individual function tests, but complete business processes.

**Step 3 — Train participants.** UAT participants need enough knowledge to perform test scenarios without being coached through the system. Brief orientation sessions are appropriate; in-depth training typically happens post-UAT.

**Step 4 — Execute scenarios.** Participants perform scenarios in the test environment. The BA observes and records results. Facilitators document exactly what participants did and what the system did in response.

**Step 5 — Log and triage defects.** Every deviation from expected behavior is logged as a defect. The BA and project team triage each defect: is it a real defect, a data issue, a misunderstood requirement, or a training gap?

**Step 6 — Iterate until exit criteria are met.** Exit criteria define when UAT is complete. Common exit criteria: all critical and high-priority defects are resolved and re-tested, a defined percentage of test scenarios pass, key business stakeholders have signed off.

---

## SEGMENT 5 — Defect Management (15:00–18:30)

[SLIDE: "Defect Management — From Discovery to Resolution"]

A defect is any deviation between actual system behavior and expected behavior as defined by requirements. Defect management is the systematic process of tracking defects from discovery through resolution.

Every defect needs a lifecycle:

**New:** The defect has been identified and logged.

**Assigned:** The defect has been assigned to a developer or team for investigation.

**In Progress:** The developer is working on the fix.

**Fixed:** The fix has been applied in the development or test environment.

**Retesting:** The QA team or BA is verifying that the fix resolved the defect without introducing new issues.

**Closed:** The fix is confirmed. The defect is resolved.

**Rejected or Deferred:** The defect is determined to be a misunderstanding, a won't-fix decision, or deferred to a future release.

Each defect record should capture: defect ID, title, severity, priority, steps to reproduce, expected result, actual result, environment, assigned to, status, and resolution notes.

Severity is how bad the defect is. Priority is how urgently it needs to be fixed. These are different dimensions. A cosmetic defect on the CEO's favorite screen might be low severity but high priority.

The BA's role in defect management: ensure that defects are correctly linked to requirements in the RTM, participate in triage decisions, confirm that fixes are tested against the original test case, and track overall defect metrics to assess release readiness.

---

## SEGMENT 6 — Sign-Off Criteria (18:30–21:00)

[SLIDE: "Sign-Off Criteria — When Is the System Ready?"]

Sign-off criteria are the defined conditions that must be satisfied before a system transitions from testing to production. Without clear sign-off criteria established before testing begins, the go/no-go decision becomes subjective and political.

Typical sign-off criteria include:

- All critical and high-priority defects have been resolved and retested
- A defined percentage of test cases have passed (often 95% or higher for critical functions)
- All UAT scenarios have been executed and signed off by designated business stakeholders
- Performance benchmarks have been met under load testing
- Security testing has passed
- Data migration has been validated
- Training materials and user documentation are complete
- Rollback procedures have been tested and documented

The sign-off document is a formal artifact. It identifies who is signing off, what they are accepting, and what known residual issues (if any) they are accepting with a remediation plan.

A BA does not make the go/no-go decision. That is an executive or sponsor decision. But the BA is responsible for ensuring that the information needed to make that decision — defect status, test completion rates, outstanding risks — is accurate, current, and clearly communicated.

---

## SEGMENT 7 — Module Wrap-Up (21:00–23:30)

[SLIDE: "Module 14 Summary"]

Let's close with today's key takeaways.

The Requirements Traceability Matrix links every requirement to its design, test cases, test results, and defects. It is your quality assurance spine.

Test cases must be specific — especially expected results. Vague test cases produce unreliable results.

User Acceptance Testing confirms that the system works for the business, not just technically. It requires real users, real scenarios, and formal sign-off.

Defect management tracks every deviation from requirements through discovery, resolution, and closure.

Sign-off criteria must be defined before testing begins. Clear criteria make the go/no-go decision rational and defensible.

For your ECBA preparation, expect questions on what an RTM contains, the purpose and process of UAT, and the BA's role in defect triage and sign-off.

Complete your reading guide, lab, and quiz. Module 15 covers implementation, change management, and transition — what happens after sign-off.

[END]

---

*Total runtime estimate: 21–23 minutes*
