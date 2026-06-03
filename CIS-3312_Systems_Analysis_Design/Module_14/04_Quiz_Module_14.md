# Quiz: Module 14 — Testing, Validation, and Quality Assurance

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Quiz Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided after each question to support your learning.

**Time limit:** 30 minutes

---

## Question 1

A BA reviews a requirement that states: "The system shall provide a good user experience." The BA flags this requirement before test case development begins. What is the primary reason for flagging it?

A. The requirement is out of scope for system testing.
B. The requirement is not testable because it lacks a specific, measurable outcome.
C. User experience requirements belong in the design document, not the requirements specification.
D. The requirement cannot be linked to a functional test case because it is non-functional.

### Distractor Analysis — Question 1

**Correct answer: B**

"Good user experience" is a subjective qualifier with no agreed measurement. A tester cannot determine objectively whether it passes or fails. The requirement must be rewritten with specific, measurable criteria before a valid test case can be written.

**Why A is wrong:** Whether a requirement is in scope for system testing is a planning decision, not the reason to flag it. The problem is testability, not scope.

**Why C is wrong:** Non-functional quality requirements belong in the requirements specification. Placing them only in the design document would mean they never get formally tested.

**Why D is wrong:** Non-functional requirements absolutely can and do generate test cases — performance tests, accessibility tests, and usability tests all verify non-functional requirements. The issue here is specificity, not requirement type.

---

## Question 2

A project team is preparing the Requirements Traceability Matrix. A QA analyst discovers that three test cases in the test suite have no corresponding requirement ID in the RTM. What does this most likely indicate?

A. The three test cases are regression tests and do not need requirement links.
B. The test cases may be testing functionality that was not formally required — a potential scope issue.
C. The RTM is incomplete and the requirements for these test cases must have been accidentally deleted.
D. These test cases should be promoted to UAT scenarios since they are not covered by requirements.

### Distractor Analysis — Question 2

**Correct answer: B**

Test cases without corresponding requirements are "test orphans." They may indicate that the development team built functionality that was not formally requested — a scope creep signal. They may also indicate that requirements exist but were not documented. Either way, this is a discrepancy that needs investigation.

**Why A is wrong:** Regression tests should still trace to requirements. A regression test verifies that previously working functionality still works — and that functionality must have been required in the first place.

**Why C is wrong:** While RTM maintenance errors are possible, the first interpretation should be that this represents untraced functionality, not a clerical error. Assuming clerical error without investigation would mask a real problem.

**Why D is wrong:** UAT scenarios must also trace to requirements. Promoting untraceable test cases to UAT does not resolve the fundamental problem of missing requirement documentation.

---

## Question 3

A test case for a customer registration form includes the expected result: "The account is created." A QA manager asks the BA to revise this expected result. What is the most appropriate revised version?

A. "The account is created successfully without errors."
B. "A confirmation message displays stating 'Account created for [entered email address]' and a welcome email is sent to the entered email address within 2 minutes."
C. "The user is redirected to the dashboard and the system does not display any error messages."
D. "The registration process completes and the user can log in."

### Distractor Analysis — Question 3

**Correct answer: B**

This expected result is specific and observable. It identifies the exact message text, confirms the personalization element (email address in message), and specifies a measurable timing requirement for the follow-up email. Two different testers would agree whether this passed or failed.

**Why A is wrong:** "Successfully without errors" is still vague. What constitutes success? What counts as an error? This version is only marginally better than the original.

**Why C is wrong:** This version is better than the original but still incomplete. It does not specify what appears on the dashboard or confirm that the account data was actually stored correctly.

**Why D is wrong:** "Can log in" is an important validation but this version lacks specificity about what immediate feedback the user receives, making it difficult to confirm the test result at the moment of execution.

---

## Question 4

Which test type is specifically designed to verify that a system modification did not break functionality that was working correctly before the change was made?

A. Boundary value test
B. Integration test
C. Negative test
D. Regression test

### Distractor Analysis — Question 4

**Correct answer: D**

Regression testing re-executes previously passing test cases after a change to confirm that the change did not introduce new defects in existing functionality. It is the standard mechanism for maintaining system stability across iterative changes.

**Why A is wrong:** Boundary value testing targets the edges of valid input ranges. It is a test design technique, not a re-verification mechanism for existing functionality.

**Why B is wrong:** Integration testing verifies that separately built components work together correctly. It focuses on interfaces between modules, not on re-verifying previously stable functionality after a change.

**Why C is wrong:** Negative testing verifies correct handling of invalid inputs. It is a test type based on input class, not on the timing or context of system changes.

---

## Question 5

A BA is setting UAT entry criteria for a payroll system replacement. Which of the following is the most appropriate entry criterion?

A. The business stakeholders have approved the project charter.
B. All critical and high-priority defects from system testing have been resolved and retested.
C. The development team has completed at least 50% of the planned sprint backlog.
D. The BA has reviewed the requirements specification one final time.

### Distractor Analysis — Question 5

**Correct answer: B**

Entry criteria ensure that UAT begins with a stable, minimally defect-free system. Starting UAT with unresolved critical defects wastes participants' time and erodes stakeholder confidence. Requiring resolution of critical and high defects before UAT is the professional standard.

**Why A is wrong:** Project charter approval is a project initiation activity, not a UAT entry criterion. It occurs months before testing.

**Why C is wrong:** Completing 50% of the sprint backlog means the system is only half-built. UAT on an incomplete system produces incomplete and potentially misleading results.

**Why D is wrong:** A final requirements review is a good practice but is not a standard UAT entry criterion. Entry criteria focus on system readiness, not document review activities.

---

## Question 6

During UAT, a business stakeholder discovers that the system calculates loan interest correctly but rounds to two decimal places, while the business process requires rounding to four decimal places for regulatory reporting. No requirement specified the rounding precision. How should the BA classify and respond to this finding?

A. Reject it as out of scope because it was not in the requirements.
B. Log it as a defect against the existing functional requirement and escalate to the change control process.
C. Log it as a requirements gap, assess the business impact, and initiate a change request to add the missing requirement.
D. Defer it to the next release and document it as a known limitation.

### Distractor Analysis — Question 6

**Correct answer: C**

This is a requirements gap — a business need that was not captured during elicitation. The correct response is to document it as missing, assess its business and regulatory impact, and initiate a change request. Since it was not a documented requirement, it is not technically a defect.

**Why A is wrong:** Dismissing a regulatory reporting precision issue as out of scope without investigation is professionally irresponsible and could expose the organization to compliance risk.

**Why B is wrong:** Logging it as a defect against an existing requirement is incorrect because no requirement specified the rounding behavior. A defect is a deviation from a stated requirement; a gap is a missing requirement.

**Why D is wrong:** Deferring a regulatory precision issue to the next release without a business impact assessment is inappropriate. The severity of this finding — regulatory risk — may require it to be resolved before go-live.

---

## Question 7

A BA is reviewing a defect log entry. The defect description reads: "The quarterly revenue chart on the executive dashboard displays a gray background. The approved mockup shows a white background." The defect is marked Severity: Low, Priority: High. What is the most likely explanation for the high priority despite low severity?

A. The tester made an error — a cosmetic defect should always be low priority.
B. A senior executive or key stakeholder considers the visual appearance significant, elevating the urgency despite minimal functional impact.
C. The defect is actually high severity because dashboard appearance affects user productivity.
D. High priority means the defect should be fixed in the next sprint, regardless of severity.

### Distractor Analysis — Question 7

**Correct answer: B**

Severity and priority are independent. A cosmetic defect on a screen viewed by the CEO or executive leadership can legitimately be low severity (it does not affect function) but high priority (the stakeholder wants it fixed immediately). This is a common real-world scenario.

**Why A is wrong:** Severity and priority are explicitly defined as independent dimensions. Asserting that cosmetic defects must always be low priority misunderstands the framework.

**Why C is wrong:** A background color change does not affect user productivity in any meaningful way. This would not justify reclassifying severity.

**Why D is wrong:** This describes what high priority means in terms of scheduling, which is correct, but it does not explain the rationale for the specific low-severity/high-priority combination in this scenario.

---

## Question 8

What is the primary difference between a UAT test scenario and a system test case?

A. UAT test scenarios are written by developers; system test cases are written by BAs.
B. UAT test scenarios cover end-to-end business processes in business language; system test cases verify technical specifications at a granular level.
C. UAT test scenarios do not require expected results; system test cases do.
D. UAT test scenarios are executed only once; system test cases can be executed multiple times.

### Distractor Analysis — Question 8

**Correct answer: B**

UAT scenarios describe complete business workflows in terms end users understand. System test cases are granular, technical, and mapped to specific functional specifications. Both need expected results; the difference is scope, audience, and language level.

**Why A is wrong:** BAs typically write or heavily contribute to both types. UAT scenarios are often written by the BA and reviewed with business stakeholders. System test cases may be written by BAs, QA analysts, or both.

**Why C is wrong:** UAT scenarios absolutely require expected results — without them, there is no objective basis for determining whether UAT passed or failed.

**Why D is wrong:** Both scenario types can and should be re-executed as needed, particularly for regression purposes after defect fixes.

---

## Question 9

The BA documents the following sign-off criterion: "UAT is complete when stakeholders feel comfortable with the system." Why is this criterion problematic?

A. Stakeholder comfort is irrelevant to technical testing outcomes.
B. The criterion is subjective and cannot produce a consistent, auditable go/no-go decision.
C. Sign-off criteria should only address defect counts, not stakeholder sentiment.
D. UAT should not require stakeholder sign-off — that is the sponsor's responsibility.

### Distractor Analysis — Question 9

**Correct answer: B**

"Feel comfortable" has no measurable definition. Different stakeholders will have different thresholds, and the standard cannot be audited or defended objectively. Sign-off criteria must be specific and measurable so that the go/no-go decision is rational and defensible.

**Why A is wrong:** Stakeholder confidence is genuinely relevant to release readiness — but it must be expressed as a measurable condition (e.g., all designated stakeholders have signed the UAT sign-off document), not a vague sentiment.

**Why C is wrong:** Sign-off criteria legitimately include stakeholder sign-off requirements — the problem is not that stakeholders are involved, but that "feel comfortable" is not a measurable standard.

**Why D is wrong:** Business stakeholder sign-off on UAT is standard practice and appropriate. The sponsor is often one of the designated sign-off parties.

---

## Question 10

Which of the following best describes the BA's role during defect retesting after a developer has applied a fix?

A. The BA reruns the original test case to confirm the defect is resolved and verifies no new defects were introduced in adjacent functionality.
B. The BA writes a new test case to replace the original test case that caught the defect.
C. The BA closes the defect in the tracking system without re-executing any tests, trusting the developer's confirmation.
D. The BA escalates the defect to the project manager for retesting authorization before any verification occurs.

### Distractor Analysis — Question 10

**Correct answer: A**

After a fix is applied, the BA or QA tester reruns the original test case to confirm resolution, then performs a targeted check of adjacent functionality (smoke regression) to catch any regression introduced by the fix. This is the standard retesting process.

**Why B is wrong:** The original test case is valid and should be reused. Writing a new test case for every fix would create test suite bloat and lose the direct traceability to the original defect and requirement.

**Why C is wrong:** Closing a defect without retesting defeats the purpose of defect tracking. Developer confirmation is not a substitute for independent verification.

**Why D is wrong:** Retesting authorization does not require a project manager escalation as a standard step. The BA or QA team has standing authority to retest resolved defects as part of normal workflow.

---

*Module 14 Quiz | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
