# Reading Guide: Module 05 - Use Case Modeling and User Stories

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


**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 05 covers two of the most widely used techniques for modeling functional requirements from the user's perspective: use cases (common in traditional and UML-based approaches) and user stories (standard in Agile/Scrum environments). Both techniques shift the focus of requirements from system features to user goals, making requirements far more understandable to both business stakeholders and developers. This module bridges traditional systems analysis with modern Agile practice.

---

## 1. Core Vocabulary

### 1.1 Use Case

A use case describes a sequence of interactions between an actor and the system to achieve a specific goal. Use cases focus on the value delivered to the actor rather than on internal system mechanisms. A complete use case specification includes: name, primary actor, preconditions, main success scenario (step-by-step), alternative flows, exception flows, and postconditions.

### 1.2 Actor

An actor is any entity outside the system boundary that interacts with the system — a human user, an external system, or an automated process. Actors are not part of the system; they initiate or receive results from use cases. The same person can play multiple actor roles depending on context.

### 1.3 Use Case Diagram

A use case diagram is a UML behavioral diagram showing the system boundary, actors, use cases, and the associations between them. It provides a high-level visual overview of functional scope. It does not show the sequence of steps within a use case — that belongs in the written use case specification.

### 1.4 Include Relationship

The include relationship between two use cases indicates that the base use case always invokes the included use case as a mandatory part of its execution. The arrow points from the base use case to the included use case, labeled with the stereotype. Example: "Process Order" always includes "Validate Payment."

### 1.5 Extend Relationship

The extend relationship indicates that the extending use case optionally adds behavior to the base use case under a specific condition. The arrow points from the extending use case to the base use case, labeled with the stereotype, often with a condition note. Example: "Apply Restocking Fee" extends "Process Return" only when the item is open-box.

### 1.6 User Story

A user story is a brief, informal description of a feature written from the end user's perspective: "As a [role], I want [goal] so that [business value]." User stories are deliberately lightweight — they invite conversation rather than serve as comprehensive documentation. The detail lives in the acceptance criteria.

### 1.7 Acceptance Criteria

Acceptance criteria are the specific, verifiable conditions a user story must satisfy for the product owner to accept it as complete. They are commonly written in Given/When/Then format. They make user stories testable and define the implementation boundary.

### 1.8 INVEST Criteria

INVEST is a quality standard for user stories:

- Independent: deliverable without dependency on another story
- Negotiable: details are open to discussion
- Valuable: delivers clear value to user or business
- Estimable: the team can estimate the effort required
- Small: completable within a single sprint
- Testable: acceptance criteria can be written

---

## 2. Use Case Diagram Notation Reference

| Symbol | Notation | Represents |
|---|---|---|
| Stick figure | Actor | A person, system, or device outside the boundary |
| Ellipse | Use case | A named goal pursued through system interaction |
| Rectangle | System boundary | The scope of the system under development |
| Solid line | Association | Connects actor to use case they participate in |
| Dashed arrow with stereotype | Include or Extend | Relationship between two use cases |

---

## 3. Include vs. Extend Comparison

| Dimension | Include | Extend |
|---|---|---|
| Execution | Always mandatory | Optional, condition-based |
| Arrow direction | Base use case to included use case | Extending use case to base use case |
| Use when | Factoring out shared sub-flows | Modeling optional or exception behaviors |
| Example | "Place Order" includes "Validate Payment" | "Apply Discount" extends "Place Order" if promo code entered |

---

## 4. Use Case Specification Template

A complete use case specification contains:

| Section | Contents |
|---|---|
| Use Case Name | Verb-noun phrase describing the actor's goal |
| Use Case ID | Unique identifier (e.g., UC-007) |
| Primary Actor | The actor who initiates the use case |
| Secondary Actors | Other actors involved |
| Preconditions | Conditions that must be true before the use case begins |
| Main Success Scenario | Numbered step-by-step interaction when all goes well |
| Alternate Flows | Valid variations from the main path |
| Exception Flows | Failure or error paths |
| Postconditions | What is true after the use case completes successfully |

---

## 5. User Story Format and Acceptance Criteria

The standard user story format: "As a [role], I want [goal] so that [value]."

The three parts serve distinct purposes:

- Role: identifies who benefits — enables the team to prioritize by impact on real users
- Goal: describes the feature at a functional level — what the user wants to do
- Value: explains the business reason — prevents teams from implementing features without understanding their purpose

Acceptance criteria in Given/When/Then format:

- Given: the precondition or starting state
- When: the action the user or system takes
- Then: the expected outcome

Example: "Given a registered customer is on the login page and has clicked Forgot Password, when they enter a valid registered email and click Submit, then they receive a password reset email within 60 seconds."

---

## 6. Epics vs. User Stories

An epic is a large user story that is too big to complete in a single sprint. It must be broken down into smaller, sprint-sized stories before development can begin. Signs that a story is actually an epic:

- The story contains the word "and" multiple times, bundling separate features
- The team cannot estimate it because the scope is unclear
- It would take more than one sprint to complete
- It addresses multiple user roles or multiple system areas

---

## 7. Use Cases vs. User Stories Comparison

| Dimension | Use Case | User Story |
|---|---|---|
| Format | Formal specification document | Brief narrative card |
| Detail level | High — full flows, conditions, exceptions | Low — invites conversation for details |
| Methodology | Traditional/UML, Waterfall | Agile/Scrum |
| Audience | Technical and business stakeholders | Product owner and development team |
| Acceptance | Formal sign-off on specification | Product owner accepts against criteria |
| When to use | Complex interactions, multiple flows | Sprint-sized features in iterative delivery |

---

## 8. Certification Exam Tips

1. The include relationship is always mandatory — the included use case runs every time. The extend relationship is optional — the extending use case runs only under a specific condition. The exam tests this distinction directly.

2. The arrow direction for extend is often tested as a trap. The arrow points from the extending use case to the base use case — not the other way around.

3. INVEST violations are tested by presenting a badly written user story and asking which criterion is violated. The most common violation tested is "not Small enough" (the story is actually an epic). Look for stories that bundle multiple features with "and."

4. Acceptance criteria make user stories testable. When a question asks what element of a user story ensures it meets the Testable criterion, the answer is acceptance criteria.

5. A use case diagram shows scope — what the system does and who interacts with it — but not sequence. Sequence is shown in sequence diagrams or the written use case specification.

6. The product backlog is owned and prioritized by the Product Owner, not the BA or the Scrum Master. Backlog prioritization is a Product Owner responsibility.

7. Given/When/Then is the standard format for acceptance criteria. Know all three parts: Given = precondition, When = action, Then = expected outcome.

8. Use cases and user stories are both techniques in BABOK KA 5 (Requirements Analysis and Design Definition). The exam may present either in the context of KA 5 tasks.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, Chapter 10 (Techniques) — Use Cases and Scenarios; User Stories
- BABOK Guide v3, KA 5: Requirements Analysis and Design Definition — Specify and Model Requirements task

Supplemental reading:

- Agile Alliance glossary entries for User Story and Acceptance Criteria (free at agilealliance.org)
- OMG UML specification — Use Case Diagram notation reference (free at omg.org)

---

## 10. Study Checklist

- [ ] Draw a use case diagram from memory with all five notation elements (actors, use cases, boundary, associations, relationships).
- [ ] Explain include vs. extend in your own words with one example each.
- [ ] Write a complete use case specification for a simple scenario (two flows minimum).
- [ ] Write three user stories in the correct format with two acceptance criteria each in Given/When/Then format.
- [ ] Name all six INVEST criteria and give one example of a story that violates each.
- [ ] Watch the Module 05 video lecture.
- [ ] Complete the Module 05 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 11. Supplemental Resources

The following open educational resources extend module content on use case modeling and user stories. All are freely accessible without login or purchase.

1. **Use Case Modeling — BABOK Guide v3 Technique Reference**
   <https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/>
   Focus: Official IIBA technique descriptions for Use Cases and Scenarios and User Stories. Review both entries in BABOK Chapter 10 to align terminology with the ECBA exam.

2. **UML Use Case Diagram Tutorial — Visual Paradigm**
   <https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/>
   Focus: Illustrated guide to all UML use case notation elements: actors, system boundaries, use cases, include, extend, and generalization. Directly supports Part 1 of the lab diagram exercise.

3. **User Stories — Agile Alliance**
   <https://www.agilealliance.org/glossary/user-stories/>
   Focus: Official Agile Alliance definition of user stories including the INVEST criteria, the three-part format, and acceptance criteria. The canonical reference for Section 1.6–1.8 of this guide.

4. **Writing Effective Acceptance Criteria — Mountain Goat Software**
   <https://www.mountaingoatsoftware.com/blog/acceptance-criteria-for-user-stories>
   Focus: Practical guidance on writing Given/When/Then acceptance criteria with worked examples. Directly supports Part 3 of the lab.

5. **Cockburn Use Case Template — Alistair Cockburn**
   <https://alistair.cockburn.us/use-cases/>
   Focus: The original Cockburn use case template used throughout this module for the use case specification format. Review the template structure and the distinction between main success scenario and alternate/exception flows.
