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

---

## Question 11

A BA is reviewing an acceptance criterion written as: "The system should handle errors
gracefully." Before allowing this criterion to proceed to test case development, the BA
should flag it for which reason?

A. Acceptance criteria must be written by QA analysts, not business analysts

B. The criterion is untestable because "gracefully" is a subjective qualifier with no
   measurable definition — it cannot produce a consistent pass/fail determination

C. The criterion is out of scope because error handling is a non-functional requirement
   that belongs in the design document

D. The criterion should be combined with other error-related criteria into a single
   comprehensive test case

### Distractor Analysis — Question 11

**Correct answer: B**

"Gracefully" is a subjective term. Two testers would disagree on whether a given error
message is "graceful" or not. The criterion cannot produce an objective, auditable
pass/fail result. It must be rewritten with specific, observable outcomes such as: "When
an invalid input is submitted, the system shall display an error message within 1 second
identifying the specific field and the required format."

**Why A is wrong:** BAs routinely write and review acceptance criteria. Requiring QA
authorship misrepresents the standard role division on most project teams.

**Why C is wrong:** Non-functional requirements — including error handling — absolutely
belong in the requirements specification and generate test cases. The issue here is
specificity, not requirement type or document placement.

**Why D is wrong:** Combining multiple error scenarios into a single test case reduces
traceability and makes it harder to pinpoint which scenario failed. Consolidation is not
the fix for an untestable criterion.

---

## Question 12

An RTM shows that requirement FR-015 has three test cases linked to it: TC-041 (Pass),
TC-042 (Fail — defect DEF-022 open), and TC-043 (Not Tested). What is the correct test
status to report for FR-015 in an executive status summary?

A. Pass — the majority of test cases passed

B. Fail — one test case failed and a defect is open

C. Not Tested — at least one test case has not been executed

D. Blocked — the open defect prevents further testing

### Distractor Analysis — Question 12

**Correct answer: B**

A requirement's test status reflects its worst active result. One failing test case with
an open defect means the requirement is not verified. Reporting "Pass" because two of
three cases passed would be misleading. The requirement is Fail until DEF-022 is resolved
and retested.

**Why A is wrong:** Majority voting is not a valid method for requirement status
determination. A single active failure means the requirement is unverified — regardless
of how many other test cases passed.

**Why C is wrong:** While TC-043 is not yet executed, the more severe status is Fail from
TC-042. The overall status should reflect the worst active finding, which is Fail.

**Why D is wrong:** "Blocked" status means a test cannot be executed due to an external
dependency or environment issue, not that a defect exists. TC-043 is simply not yet
executed, and TC-041 already passed — there is no blocking condition described.

---

## Question 13

A BA is writing a boundary value test case for a date field that accepts dates between
January 1, 2020 and December 31, 2030. Which set of test values most completely applies
the boundary value analysis technique?

A. January 15, 2025 (a mid-range valid date)

B. January 1, 2020 and December 31, 2030 (the exact boundary values)

C. December 31, 2019; January 1, 2020; December 31, 2030; January 1, 2031
   (one value below each boundary, each boundary value itself, and one value above each
   boundary)

D. All dates within the range tested individually to confirm each one is accepted

### Distractor Analysis — Question 13

**Correct answer: C**

Boundary value analysis tests the values just outside (invalid), at (valid boundary),
and just inside each limit. For a range with two boundaries (lower: Jan 1 2020, upper:
Dec 31 2030), the complete boundary set is: one invalid value below the lower bound, the
lower bound itself, the upper bound itself, and one invalid value above the upper bound.

**Why A is wrong:** Testing only a mid-range value provides no information about boundary
behavior. Most defects occur at boundaries, not in the middle of a valid range.

**Why B is wrong:** Testing only the boundary values without the adjacent invalid values
misses half of boundary analysis. The technique specifically requires testing values that
should be rejected as well as values that should be accepted.

**Why D is wrong:** Testing all values in the range would require testing over 4,000
dates. Boundary value analysis achieves efficient coverage of the high-risk areas with
a small number of targeted values.

---

## Question 14

During a UAT session for a payroll system, a business user discovers that the system
calculates overtime pay correctly for employees paid weekly but incorrectly for employees
paid bi-weekly. No requirement in the specification mentioned bi-weekly pay periods. How
should the BA classify and act on this finding?

A. Reject it — if it was not in the requirements, it is not a defect

B. Log it as a defect against FR-101 (overtime calculation requirement) and assign
   Critical severity

C. Log it as a requirements gap, assess business impact, and initiate a change request
   to capture the missing business rule for bi-weekly employees

D. Defer it to the next release with no documentation because it was discovered during
   UAT rather than system testing

### Distractor Analysis — Question 14

**Correct answer: C**

A finding in UAT that reveals missing business coverage is a requirements gap — a real
business need that was not elicited. The correct response is to document it, assess
business impact (are bi-weekly employees a significant population?), and use the change
control process to add the missing requirement. This finding should not be ignored or
rejected.

**Why A is wrong:** Requirements gaps discovered during UAT are legitimate project risks.
Rejecting them without investigation could leave the system unfit for the business's
actual payroll population.

**Why B is wrong:** Logging it as a defect against FR-101 is technically incorrect
because no requirement specified bi-weekly behavior. A defect is a deviation from a
stated requirement; since the requirement is absent, this is a gap, not a defect.

**Why D is wrong:** Deferring a payroll calculation issue without documentation is
professionally irresponsible. A missing business rule that affects employee compensation
may need resolution before go-live.

---

## Question 15

A test case has the following expected result: "The system processes the transaction." A
QA manager asks the BA to revise it. Which revised expected result is most appropriate?

A. "The system processes the transaction successfully and without errors."

B. "The transaction is saved to the database."

C. "A confirmation message reading 'Transaction TXN-[ID] completed. Amount: $[entered
   amount] transferred to [destination account]' is displayed within 3 seconds, and a
   corresponding entry appears in the account transaction history with the correct amount
   and timestamp."

D. "The user sees a confirmation screen."

### Distractor Analysis — Question 15

**Correct answer: C**

This expected result is specific, observable, and complete. It identifies the exact
message text with personalized data fields, specifies a timing requirement (3 seconds),
and requires confirmation of data persistence in the transaction history. Two independent
testers would agree on whether this passed or failed.

**Why A is wrong:** "Successfully and without errors" adds words without adding specificity.
It still cannot be objectively evaluated — what constitutes success, and which errors count?

**Why B is wrong:** "Saved to the database" is more specific than the original but lacks
the user-facing confirmation and the transaction history verification. A tester would need
direct database access to verify this, which is not standard UAT practice.

**Why D is wrong:** "Sees a confirmation screen" is only marginally more specific than
the original. It does not identify what the screen must display, making it impossible to
distinguish a valid confirmation from a generic error page that happens to have a heading.

---

## Question 16

A defect is logged with the following attributes: Description — "The 'Export to CSV'
button on the audit report screen is misaligned by approximately 5 pixels." Severity:
Low. The system is scheduled to go live in two days and this is the only remaining open
defect. Which disposition is most appropriate?

A. Critical — all defects must be fixed before go-live regardless of severity

B. Defer to next release — a 5-pixel misalignment has no functional impact and does not
   meet the threshold for delaying go-live for a minor cosmetic issue

C. Reject — the defect description is too vague to act on

D. Fix before go-live — all visual defects must be corrected to maintain brand standards

### Distractor Analysis — Question 16

**Correct answer: B**

A 5-pixel misalignment is a cosmetic defect with no impact on functionality, business
processes, or user task completion. With a go-live in two days and this as the only open
defect, deferring it to the next release is a rational, professionally defensible
decision. The BA should document the deferral with stakeholder acknowledgment.

**Why A is wrong:** Severity classification exists precisely to enable differentiated
responses. Treating all defects as equally blocking defeats the purpose of the severity
framework and would halt go-live for inconsequential cosmetic issues.

**Why C is wrong:** The description is specific enough to reproduce and fix. "5 pixels
misaligned" describes a visible, locatable problem. Rejecting it on grounds of vagueness
misapplies the rejection criterion.

**Why D is wrong:** Brand standards are a valid concern, but a 5-pixel alignment issue on
a back-office audit report is not a material brand risk. Blanket rules that override
severity classification produce irrational defect management decisions.

---

## Question 17

Which of the following best describes the relationship between a UAT test scenario and
the Requirements Traceability Matrix?

A. UAT test scenarios are standalone documents that replace the RTM during the testing
   phase

B. Each UAT test scenario should trace to one or more requirements in the RTM, so that
   when a scenario fails, the BA can immediately identify which requirement is not
   satisfied

C. UAT test scenarios are only linked to non-functional requirements; functional
   requirements trace only to system test cases

D. The RTM is closed and archived before UAT begins, so UAT scenarios are not linked to it

### Distractor Analysis — Question 17

**Correct answer: B**

The RTM is a living document maintained throughout the test lifecycle including UAT.
Linking UAT scenarios to requirements ensures complete traceability — when a scenario
fails, the BA and project team know which business requirement was not satisfied and can
make an informed go/no-go decision.

**Why A is wrong:** UAT scenarios complement the RTM; they do not replace it. The RTM
provides the formal traceability record; UAT scenarios provide the business workflow
context for testing.

**Why C is wrong:** Both functional and non-functional requirements generate test coverage,
including UAT scenarios. A UAT scenario testing end-to-end loan processing covers
functional requirements directly.

**Why D is wrong:** Archiving the RTM before UAT begins would prevent the project team
from tracking UAT test results, defects, and final requirement verification status. The
RTM is actively maintained until all requirements are confirmed deployed and verified.

---

## Question 18

A project team is deciding whether to include the two IT developers who built the system
as UAT participants. The BA recommends excluding them. Which justification best supports
the BA's recommendation?

A. Developers lack the technical skills needed to execute business process scenarios

B. Developers have an inherent conflict of interest — they are unlikely to report failures
   in their own work objectively, and they are not representative of the end users whose
   needs UAT is designed to validate

C. Developers are not permitted to participate in testing under BABOK guidelines

D. Including developers would make the UAT session run too long due to their tendency to
   troubleshoot defects during the session

### Distractor Analysis — Question 18

**Correct answer: B**

UAT's purpose is business validation by representative end users. Developers are not end
users, and their bias toward their own work reduces the objectivity of findings. Both
factors — conflict of interest and non-representativeness — support excluding them from
the UAT participant roster.

**Why A is wrong:** Developers are technically highly capable. The reason to exclude them
is not skill but objectivity and representativeness.

**Why C is wrong:** The BABOK Guide does not prohibit developers from participating in
testing. The exclusion is based on best practice for objective validation, not a formal
prohibition.

**Why D is wrong:** While troubleshooting during a UAT session is a facilitation risk,
it is a secondary concern. The primary reason to exclude developers is their conflict of
interest and their failure to represent the end-user perspective.

---

## Question 19

A BA discovers that a requirement in the approved RTM — FR-021, which governs export
file format — was not covered by any test case. The system has already been deployed to
production. What should the BA do?

A. Close FR-021 in the RTM as "Not Required" since it survived deployment untested

B. Document the coverage gap in the RTM, assess whether FR-021's behavior in production
   meets the requirement, and plan a post-deployment verification test or defect
   investigation

C. Delete FR-021 from the RTM to avoid audit complications

D. Log a defect against FR-021 immediately and request a production rollback

### Distractor Analysis — Question 19

**Correct answer: B**

Discovering an untested requirement post-deployment is a traceability gap that must be
addressed through the project's quality management process. The correct response is to
document the gap honestly, assess whether the production behavior satisfies the
requirement (it may work correctly despite never being formally tested), and plan the
appropriate verification or remediation.

**Why A is wrong:** "Not Required" is not a valid RTM status. Unverified requirements
represent unknown risk — not confirmed non-requirements. Closing the item as not required
misrepresents the coverage status.

**Why C is wrong:** Deleting records from the RTM to conceal a coverage gap is a data
integrity violation. In regulated environments, this could constitute fraud. In all
environments, it undermines the credibility of the quality record.

**Why D is wrong:** An untested requirement does not automatically warrant a production
rollback. A rollback is warranted only if a known defect exists. The BA should assess
whether a problem actually exists before escalating to production change actions.

---

## Question 20

The BABOK Guide places testing-related BA activities primarily under which knowledge area,
and what is the BA's primary testing responsibility in that context?

A. Strategy Analysis — the BA tests whether the proposed solution aligns with
   organizational strategy

B. Requirements Analysis and Design Definition — the BA ensures requirements are
   testable and that acceptance criteria are defined so solutions can be validated

C. Business Analysis Planning and Monitoring — the BA plans the test schedule and
   assigns resources to test execution

D. Solution Evaluation — the BA executes system test cases to confirm the solution
   is technically correct

### Distractor Analysis — Question 20

**Correct answer: B**

The BABOK Guide positions the BA's testing responsibilities primarily within Requirements
Analysis and Design Definition, specifically around ensuring requirements are testable
(requirements quality), defining acceptance criteria, and validating that solutions meet
stated requirements. The BA also contributes to Solution Evaluation (assessing whether
the implemented solution delivers business value), but the foundational testing
competency is writing testable requirements and acceptance criteria.

**Why A is wrong:** Strategy Analysis focuses on defining the business need and selecting
the right change initiative. It does not address solution testing.

**Why C is wrong:** Test scheduling and resource assignment are project management
responsibilities. The BA's testing contribution is requirements and acceptance criteria
quality, not test planning logistics.

**Why D is wrong:** Executing system test cases is primarily a QA or developer
responsibility. The BA may participate in UAT scenario execution but is not responsible
for technical system test execution.

---

*Module 14 Quiz (extended) | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
