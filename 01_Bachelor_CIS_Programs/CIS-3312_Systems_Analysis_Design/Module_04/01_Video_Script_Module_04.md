# Video Script: Module 04 - Requirements Analysis and Documentation

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 22 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture &bull; Module 04</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=UI6lqHOVHic" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/UI6lqHOVHic" title="Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Lucidchart / Enterprise &bull; Systems Analysis & Software Architecture</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->


- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.

---

## Section 1: Welcome and Module Overview [00:00 - 03:00]

Welcome to Module 04. I am Professor Nash, and today we are covering Requirements Analysis and Documentation — BABOK Knowledge Area 5. After elicitation gives us raw information in Module 03, KA 5 is where we transform that raw material into well-formed, structured requirements that a development team can actually build from.

[SHOW DIAGRAM: Title slide — "Module 04: Requirements Analysis and Documentation" with BABOK KA 5 label and IIBA ECBA badge]

This module covers four key topics: the types of requirements you will document, quality characteristics of well-written requirements, requirements verification versus validation, and the Requirements Traceability Matrix. Each of these is directly tested on the ECBA exam.

---

## Section 2: Types of Requirements [03:00 - 08:30]

[SHOW DIAGRAM: Requirements classification tree — "Requirements" at top, branching to "Business Requirements," "Stakeholder Requirements," "Solution Requirements" (which branches further to "Functional" and "Non-Functional"), and "Transition Requirements"]

BABOK classifies requirements into four categories. Understanding these categories is essential for the ECBA exam.

Business requirements describe the higher-level goals of the organization — the why behind the project. Example: "Reduce customer complaint resolution time by 30% within one year." Business requirements do not describe system features; they describe the business outcome the project must achieve.

Stakeholder requirements describe what a specific stakeholder group needs from the solution. They bridge the gap between business requirements and technical specifications. Example: "Customer service representatives need to view the full interaction history of any customer within 3 seconds."

Solution requirements are the system-level specifications. These are split into two subcategories. Functional requirements describe what the system must do — specific behaviors, features, and functions. Example: "The system shall allow a supervisor to flag a complaint as escalated." Non-functional requirements describe quality attributes — how well the system must perform its functions. Categories of non-functional requirements include performance, security, availability, scalability, usability, and maintainability.

Transition requirements describe capabilities needed only during the changeover from the current state to the future state. Once the transition is complete, these requirements have no further value. Example: "A data migration utility must convert all records from the legacy database format to the new schema during the cutover weekend."

> IIBA ECBA Exam Tip: The distinction between functional and non-functional requirements is heavily tested. Functional = what the system does. Non-functional = how well the system does it. A response time requirement is non-functional. A login feature requirement is functional. Know this distinction cold.

---

## Section 3: Quality Characteristics of Well-Written Requirements [08:30 - 13:30]

[SHOW DIAGRAM: SMART requirements checklist — six rows: Specific, Measurable, Achievable, Relevant, Testable, with a checkmark column and a "Failure Mode" column showing what a bad requirement looks like for each criterion]

A requirement is not good just because it is written down. To be useful, a requirement must meet specific quality criteria. BABOK lists several. Let me walk through the most important ones.

Specific: the requirement must clearly describe a single, unambiguous need. "The system should be fast" is not specific. "The system shall respond to any search query within 2 seconds under normal load" is specific.

Measurable: stakeholders and testers must be able to verify whether the requirement has been met. "Users should find the system easy to use" is not measurable. "The system shall achieve a System Usability Scale score of at least 70 in post-deployment user testing" is measurable.

Necessary: every requirement must be traceable to a business need or stakeholder request. If you cannot identify why a requirement exists, it may not belong in the specification.

Consistent: requirements must not contradict each other. If Requirement 12 says the system must enforce dual approval for all orders, and Requirement 47 says a manager may approve orders unilaterally, these requirements conflict and must be resolved before design begins.

Testable: every requirement must have a verifiable pass/fail condition. If a QA analyst cannot write a test case for a requirement, the requirement is not testable and must be rewritten.

Complete: requirements must not have gaps — missing inputs, outputs, conditions, or edge cases.

> IIBA ECBA Exam Tip: "Testable" is the quality characteristic most commonly featured in exam questions. A requirement that uses vague language — "user-friendly," "fast," "secure," "easy" — is not testable. When an exam question asks what is wrong with a requirement, look for untestable vagueness.

---

## Section 4: Verification vs. Validation [13:30 - 17:30]

[SHOW DIAGRAM: Two boxes side by side — left box: "Verification" with question "Are we building the requirements RIGHT?" and bullet points: Well-written, Unambiguous, Complete, Consistent, Testable; right box: "Validation" with question "Are we building the RIGHT requirements?" and bullet points: Traces to business need, Solves the actual problem, Stakeholder-confirmed]

Verification and validation are two distinct quality activities in BABOK KA 5, and the distinction is tested on the exam.

Requirements verification checks whether requirements are well-formed. It asks: are the requirements written clearly? Are they complete? Are they consistent with each other? Are they testable? Verification is an internal quality check on the requirements documents themselves.

Requirements validation checks whether requirements actually represent the business need. It asks: if we build exactly what these requirements describe, will we solve the actual business problem? Validation is a stakeholder confirmation activity.

Here is the important distinction for the exam: a requirements document can pass verification — every requirement is clearly written, internally consistent, and testable — and still fail validation if the requirements address the wrong problem. The classic failure scenario is when a BA documents the current system's behavior as requirements for the new system, when the real business goal was to change or improve that behavior. Perfect verification, failed validation.

---

## Section 5: Requirements Traceability Matrix [17:30 - 20:00]

[SHOW DIAGRAM: RTM table — columns: Requirement ID, Requirement Description, Business Need (origin), Design Component, Test Case ID, Status (Implemented/Not Implemented)]

The Requirements Traceability Matrix — or RTM — is the artifact that links every requirement both backward to its source (the business need or stakeholder request that originated it) and forward to the design component and test case that satisfy it.

The RTM serves three critical functions. First, it proves that every business need has at least one requirement addressing it — ensuring completeness. Second, it proves that every requirement has been designed for and tested — ensuring coverage. Third, it enables impact analysis — when a requirement changes, the RTM immediately shows which design components and test cases are affected.

Maintaining the RTM throughout the project is one of the most labor-intensive BA activities, but it is also one of the most valuable. Projects without a maintained RTM routinely discover at the end of the testing phase that significant requirements were never implemented.

---

## Section 6: Lab Preview and Closing [20:00 - 22:00]

This week's lab asks you to classify a list of 15 requirements into the four categories, identify quality issues in poorly written requirements and rewrite them, and build a partial RTM for a provided case study.

Three exam reminders. First: know the four requirement categories — Business, Stakeholder, Solution (Functional and Non-functional), and Transition. Second: know the quality characteristics, especially testability. Third: know the difference between verification (well-formed?) and validation (right thing?).

Study BABOK Guide v3 KA 5 and visit iiba.org for the ECBA exam blueprint.

---

## End Card

## Module 04 Complete

Next: Module 05 - Use Case Modeling and User Stories

### Additional Resources

- iiba.org — BABOK Guide v3 KA 5: Requirements Analysis and Design Definition
- iiba.org — ECBA exam blueprint and KA 5 weighting
