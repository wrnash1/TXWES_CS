# Reading Guide: Module 14 — Testing, Validation, and Quality Assurance

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3312 &BULL; SYSTEMS ANALYSIS & DESIGN</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Overview

This reading guide supports Module 14's video lecture on testing, validation, and quality assurance. Testing is where requirements prove their quality. A BA who writes clear, specific, testable requirements produces a system that can be verified. A BA who writes vague requirements produces a system that cannot be proven to work. This module connects requirements quality directly to testing practice.

**Estimated reading and study time:** 90–120 minutes

---

## Learning Objectives

By the end of this module you will be able to:

1. Construct a Requirements Traceability Matrix linking requirements to design and test artifacts.
2. Write specific, testable test cases with clear preconditions and expected results.
3. Distinguish between functional, negative, boundary, and regression test cases.
4. Explain the purpose and process of User Acceptance Testing.
5. Describe the defect lifecycle and the BA's role at each stage.
6. Define entry and exit criteria for UAT.
7. Identify sign-off criteria and the stakeholders responsible for authorizing go-live.

---

## Section 1 — Requirements Quality and Testability

### 1.1 The Link Between Requirements and Testing

Every test case begins with a requirement. If the requirement is ambiguous, the test case will be ambiguous. If the requirement is missing, the behavior goes untested. The quality of testing is bounded by the quality of requirements.

The BABOK Guide lists testability as a core characteristic of well-formed requirements. A testable requirement:

- Describes a specific, observable behavior
- States conditions under which the behavior occurs
- Defines a measurable outcome
- Is free of subjective qualifiers like "user-friendly," "fast," or "appropriate"

### 1.2 Converting Poor Requirements Into Testable Requirements

Consider this requirement: "The system should respond quickly."

This is not testable. "Quickly" has no agreed meaning. A tester cannot pass or fail this.

A testable version: "The search results page shall load within 2.0 seconds for 95% of requests under a concurrent load of 500 users."

Now a tester can define a specific test, execute it, measure the result, and make a definitive pass/fail determination.

As a BA, reviewing requirements for testability is a quality gate before design begins. If you cannot write a test for a requirement, the requirement needs revision.

---

## Section 2 — Requirements Traceability Matrix

### 2.1 Purpose

The Requirements Traceability Matrix (RTM) is a document that maps requirements to their origins, design artifacts, test cases, test results, and deployment status. It provides end-to-end traceability across the project lifecycle.

The RTM answers questions like:

- Is every requirement covered by at least one test case?
- Which test cases are affected if Requirement FR-014 changes?
- Which requirements had defects filed against them?
- Are all requirements confirmed as implemented in the delivered system?

### 2.2 RTM Structure

A standard RTM includes the following columns, though organizations vary in their specific implementations:

| Column | Description |
|---|---|
| Requirement ID | Unique identifier (e.g., FR-001, NFR-005) |
| Requirement Type | Functional, non-functional, business rule, etc. |
| Requirement Description | Brief statement of the requirement |
| Priority | High / Medium / Low or MoSCoW classification |
| Source | Stakeholder, document, or elicitation session where requirement originated |
| Design Reference | Pointer to design artifact (screen, component, module) |
| Test Case ID(s) | One or more test cases that verify this requirement |
| Test Status | Not Tested / Pass / Fail / Blocked |
| Defect ID(s) | Any defects raised against this requirement |
| Deployment Status | In development / Deployed / Verified in production |

### 2.3 Maintaining the RTM

The RTM is a living document. It is created when requirements are baselined and updated throughout:

- When new requirements are added
- When requirements change (change control process)
- When test cases are written or modified
- When test execution produces pass/fail results
- When defects are opened and closed
- When requirements are confirmed deployed

Stale RTMs provide false confidence. A BA who builds an RTM and never updates it has produced a document that actively misleads the project team.

### 2.4 RTM in Regulated Environments

In regulated industries such as healthcare, financial services, and government contracting, the RTM is a compliance artifact. Auditors and regulatory bodies may request the RTM to verify that requirements were formally tested. In FDA-regulated software environments, RTM maintenance is mandatory.

---

## Section 3 — Test Case Development

### 3.1 Anatomy of a Test Case

A complete test case includes the following elements.

**Test Case ID:** Unique alphanumeric identifier.

**Requirement Reference:** The ID of the requirement being verified.

**Test Objective:** One sentence stating what the test is designed to confirm.

**Test Type:** Functional, negative, boundary, integration, regression, performance, security, etc.

**Preconditions:** All conditions that must be true before the test begins. Unmet preconditions invalidate the test result.

**Test Data:** Specific input values to be used. "Amount: 500.00" not "enter an amount."

**Test Steps:** Numbered sequence of specific actions.

**Expected Result:** The exact, observable outcome that constitutes a pass. This is the most critical element — it must be specific enough that two different testers would agree on whether the test passed.

**Actual Result:** Recorded during execution.

**Pass/Fail:** Final determination.

**Tester and Date:** Execution record for audit trail.

### 3.2 Test Case Types

Understanding test types helps BAs ensure complete coverage.

**Functional test cases** verify that the system performs its intended functions. Each positive workflow scenario produces one or more functional test cases.

**Negative test cases** verify that the system handles invalid inputs and error conditions correctly. For every field, a negative test should confirm that invalid input is rejected with an appropriate error message. For every required field, a negative test should confirm that submitting without a value is blocked.

**Boundary test cases** test the limits of valid input ranges. The boundary value analysis technique tests the values just below, at, and just above each boundary. For a quantity field accepting 1–999: test 0, 1, 999, and 1000.

**Integration test cases** verify that components developed separately interact correctly. They test the interfaces and data flows between modules.

**Regression test cases** verify that previously working functionality still works after a change. A regression suite is re-executed whenever code is modified.

**Performance test cases** verify non-functional requirements related to speed, capacity, and reliability under load.

### 3.3 The BA's Role in Test Case Development

On many projects, the BA writes test cases for business-logic requirements and hands technical test cases to QA analysts. On smaller projects, the BA may write all test cases. The BA's specific contribution:

- Writing acceptance criteria that directly generate test cases
- Ensuring test cases cover both positive and negative paths
- Validating that expected results match documented requirements
- Linking test cases to requirements in the RTM

---

## Section 4 — User Acceptance Testing

### 4.1 Distinguishing UAT from System Testing

System testing is conducted by the development or QA team to verify that the system works as specified. UAT is conducted by business users to verify that the system meets business needs.

The critical difference: system testing validates the solution against requirements documents. UAT validates the solution against business reality. A system can pass system testing and still fail UAT if the requirements themselves were incomplete or misunderstood.

### 4.2 UAT Participants

UAT participants should be:

- Representative end users from the affected business units
- Subject matter experts for complex business rules
- Key business stakeholders who will authorize go-live

UAT participants should not be:

- IT staff or developers (they have a conflict of interest in finding problems)
- Managers who do not perform the actual work (they may not represent true end-user behavior)
- People unfamiliar with the business process being automated

### 4.3 UAT Entry Criteria

Entry criteria define conditions that must be met before UAT begins. Starting UAT with an unstable system wastes participants' time and erodes confidence. Common entry criteria:

- All functional and integration test cases have been executed
- All critical and high-priority defects from system testing are resolved
- Test environment is stable and loaded with representative test data
- UAT test scenarios are written, reviewed, and approved
- Participants are identified and oriented
- A defect logging mechanism is in place

### 4.4 UAT Test Scenarios

UAT scenarios differ from technical test cases. They are business process scenarios — end-to-end workflows that represent real work, described in business language.

A technical test case might say: "Verify that the POST /api/transfers endpoint returns HTTP 200 with the correct transaction ID."

A UAT scenario says: "Process a payment to a new external vendor who has never been paid before, including the required two-approver authorization workflow, and confirm that the vendor receives a remittance email."

The UAT scenario is what business users can understand and execute. The BA bridges the gap by ensuring that technical test cases cover the same ground as the business scenarios.

### 4.5 UAT Exit Criteria

Exit criteria define the conditions under which UAT is declared complete and sign-off can be obtained. Typical exit criteria:

- All UAT scenarios have been executed
- A defined pass rate has been achieved (commonly 95%+ for critical scenarios, 100% for highest-priority scenarios)
- All critical and high-priority defects are resolved and retested
- No critical defects remain open
- Designated stakeholders have reviewed and accepted the results

---

## Section 5 — Defect Management

### 5.1 Defect Definition

A defect is any deviation between the actual behavior of a system and its expected behavior as defined by requirements or accepted test cases. Defects are not limited to code errors. They include:

- Incorrect data displayed on screen
- Missing functionality
- Incorrect calculation results
- Security vulnerabilities
- Performance failures under load
- Accessibility violations

### 5.2 Defect Attributes

A complete defect record includes:

- Defect ID
- Title (brief description)
- Severity (impact on system functionality)
- Priority (urgency of fix)
- Environment (where the defect was found)
- Steps to reproduce
- Expected result
- Actual result
- Screenshot or evidence
- Assigned to
- Status
- Resolution notes

### 5.3 Severity vs. Priority

Severity and priority are independent dimensions. Every combination is possible.

| Severity | Priority | Example |
|---|---|---|
| High | High | Login fails for all users |
| High | Low | Rarely used admin export crashes |
| Low | High | CEO's name misspelled on the dashboard header |
| Low | Low | Minor formatting inconsistency on help page |

BAs participate in triage decisions to ensure that defects related to requirements are classified correctly and that the business impact is understood.

### 5.4 Defect Lifecycle

New → Assigned → In Progress → Fixed → Retesting → Closed (or Rejected / Deferred)

The BA's role spans the lifecycle: ensuring defects are correctly described and linked to requirements, participating in triage, confirming that fixed defects are retested against original test cases, and tracking overall defect trends to inform release readiness decisions.

---

## Section 6 — Sign-Off and Release Readiness

### 6.1 Sign-Off Criteria

Sign-off criteria must be defined and agreed upon before testing begins. They make the go/no-go decision objective rather than political.

Sign-off criteria typically include:

- Defect thresholds by severity (e.g., zero open critical defects, no more than three open high-priority defects)
- Test completion percentages
- UAT sign-off from designated business stakeholders
- Compliance testing pass confirmation (for regulated systems)
- Performance benchmark confirmation
- Data migration validation

### 6.2 The BA's Role in Sign-Off

The BA does not make the final go/no-go decision — that is an executive decision. The BA's role is to:

- Ensure sign-off criteria are defined and documented before testing
- Maintain accurate, current test status reporting
- Communicate defect status and risk clearly to decision-makers
- Ensure that any deferred defects have a documented remediation plan and stakeholder acknowledgment
- Document the sign-off decision with appropriate signatures

---

## Key Terms

| Term | Definition |
|---|---|
| Requirements Traceability Matrix | Document linking requirements to design, test cases, results, and deployment |
| Test case | Documented procedure for verifying a specific requirement |
| Precondition | State the system must be in before a test can be executed |
| Expected result | Specific, observable outcome that constitutes a test pass |
| Negative test | Test case verifying correct handling of invalid inputs or error conditions |
| Boundary value analysis | Technique testing values at and around the edges of valid input ranges |
| User Acceptance Testing | Final testing phase conducted by end users to confirm business readiness |
| Entry criteria | Conditions that must be met before a test phase begins |
| Exit criteria | Conditions that must be met before a test phase is declared complete |
| Defect severity | Measure of a defect's impact on system functionality |
| Defect priority | Measure of urgency for resolving a defect |
| Sign-off | Formal stakeholder approval that testing is complete and the system is ready |

---

## Self-Check Questions

Answer these before attempting the quiz.

1. What is the purpose of the Requirements Traceability Matrix?
2. What makes an expected result well-written vs. vague?
3. What is the difference between system testing and UAT?
4. Why should developers not conduct UAT?
5. What are entry criteria, and why do they matter?
6. Give an example of a high-severity, low-priority defect.
7. What is the BA's role when a fixed defect is ready for retesting?

---

## Supplemental Resources

The following open educational resources extend module content on testing, traceability,
and quality assurance. All are freely accessible without login or purchase.

1. **Software Testing Fundamentals — ISTQB Foundation Level Syllabus (free download)**
   <https://www.istqb.org/certifications/certified-tester-foundation-level>
   Focus: The foundational testing standard covering test types, test case design
   techniques (including boundary value analysis), defect lifecycle, and test management.
   Reinforces Sections 3–5 of this reading guide and provides deeper coverage of testing
   concepts tested on the ECBA exam.

2. **Requirements Traceability — IIBA BABOK Guide Technique Reference**
   <https://www.iiba.org/standards-and-resources/babok/>
   Focus: The BABOK Guide's coverage of traceability as a requirements management
   technique under Requirements Life Cycle Management. Connecting this to the RTM
   structure in Section 2 reinforces how traceability supports ECBA exam competencies.

3. **User Acceptance Testing Guide — Ministry of Testing**
   <https://www.ministryoftesting.com/dojo/lessons/an-introduction-to-user-acceptance-testing-uat>
   Focus: Practical introduction to UAT planning, participant selection, scenario writing,
   entry and exit criteria, and defect management during UAT. Directly supports the UAT
   planning tasks in Part 3 of the lab.

4. **Defect Management Best Practices — Atlassian Jira Documentation**
   <https://www.atlassian.com/agile/software-development/bugs>
   Focus: Practical guidance on defect logging, severity vs. priority classification,
   triage processes, and defect lifecycle management in agile contexts. Supplements
   Section 5 of the reading guide and the defect triage task in Part 4 of the lab.

5. **Writing Testable Requirements — Requirements Engineering Journal (open access)**
   <https://re2023.ieeecomputer.org/>
   Focus: Academic and practitioner resources on requirements quality, testability
   criteria, and the cost of untestable requirements discovered late in development.
   Reinforces Section 1 of this reading guide on the link between requirements quality
   and testing outcomes.

---

*Module 14 Reading Guide | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
