# Reading Guide: Module 04 - Requirements Analysis and Documentation

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 04 covers BABOK Guide v3 Knowledge Area 5: Requirements Analysis and Design Definition. After elicitation provides raw information in Module 03, KA 5 is where the BA transforms that raw material into structured, well-formed requirements that a development team can actually build from. This Knowledge Area is the intellectual core of the business analysis discipline and one of the most heavily weighted areas on the ECBA exam.

---

## 1. Core Vocabulary

### 1.1 Requirements Classification

BABOK classifies requirements into four categories:

- Business requirements: the higher-level goals the organization must achieve (the "why")
- Stakeholder requirements: what a specific stakeholder group needs from the solution
- Solution requirements: system-level specifications, subdivided into functional and non-functional
- Transition requirements: capabilities needed only during the changeover to the new system; temporary by nature

### 1.2 Functional Requirement

A functional requirement describes a specific behavior, action, or capability the system must perform. It answers the question "What does the system do?" Functional requirements are testable: for every functional requirement, a QA analyst should be able to write a test case with a clear pass/fail outcome. Example: "The system shall send an email notification to the customer when their order status changes to Shipped."

### 1.3 Non-Functional Requirement (Quality Attribute)

A non-functional requirement specifies a quality characteristic or constraint the system must exhibit, rather than a specific function it must perform. It answers the question "How well does the system do it?" Categories include performance, security, availability, scalability, usability, and maintainability. Example: "The system shall respond to any product search query within 2 seconds under a load of 500 concurrent users."

### 1.4 Business Rule

A business rule is a statement defining or constraining some aspect of the business — a policy, regulation, or contractual obligation that the system must enforce. Business rules originate in the business domain, not in the technology. Example: "All purchase orders exceeding $10,000 require approval from both the department manager and the finance controller." Business rules drive functional requirements but are not themselves system behaviors.

### 1.5 Requirements Traceability

Requirements traceability is the ability to link each requirement both backward to its source (the business need or stakeholder request that originated it) and forward to the design element and test case that satisfy it. The Requirements Traceability Matrix (RTM) documents these links and enables completeness verification and impact analysis.

### 1.6 Verification vs. Validation

These are two distinct quality activities in BABOK KA 5:

- Verification: checks that requirements are well-formed — specific, measurable, consistent, complete, and testable. Asks: "Are we building the requirements right?"
- Validation: checks that requirements represent the actual business need — that implementing them will solve the real problem. Asks: "Are we building the right requirements?"

A requirements document can pass verification (all requirements are well-written) and fail validation (they describe the wrong thing).

---

## 2. Requirements Quality Characteristics

BABOK lists the following quality criteria for individual requirements:

| Characteristic | Definition | Common Failure |
|---|---|---|
| Atomic | Describes a single, cohesive need | Two or more requirements bundled into one statement |
| Complete | No missing inputs, outputs, or conditions | Requirements with gaps like "system shall handle errors" |
| Consistent | Does not contradict other requirements | Req 12 says dual approval required; Req 47 allows unilateral approval |
| Concise | Stated without unnecessary elaboration | Multi-paragraph "requirements" that mix narrative and specifications |
| Feasible | Technically and operationally achievable | Requirements for capabilities that do not yet exist |
| Unambiguous | Has only one interpretation | "The system shall be fast" or "user-friendly" |
| Testable | Can be confirmed as satisfied or not | "The system shall provide a good user experience" |
| Necessary | Traceable to a real business need | Requirements added "because we might need it someday" |

Testability is the most commonly tested characteristic on the ECBA exam. Any requirement using vague qualifiers — fast, secure, easy, user-friendly, efficient — fails the testability criterion and must be rewritten with measurable thresholds.

---

## 3. Requirements Documentation Formats

BAs use several formats to document requirements, depending on the project approach and audience:

| Format | Description | Best Used When |
|---|---|---|
| Software Requirements Specification (SRS) | Formal document following IEEE 29148 structure | Predictive/Waterfall projects with formal sign-off |
| User Story | "As a [role], I want [goal] so that [value]" format with acceptance criteria | Agile/Scrum projects |
| Use Case Specification | Actor, goal, main flow, alternate flows, pre/postconditions | Systems with complex actor-system interactions |
| Business Rules Catalog | Table of numbered business rules with owner and source | Any project with significant policy constraints |
| Data Dictionary | Definitions of all data elements, formats, and business rules | Database-intensive systems |

---

## 4. The Requirements Traceability Matrix

The RTM is a table linking each requirement to related project artifacts. A minimal RTM includes:

| Column | Contents |
|---|---|
| Requirement ID | Unique identifier (e.g., FR-001, NFR-003) |
| Requirement Description | One-sentence statement of the requirement |
| Source | Stakeholder or business need that originated the requirement |
| Design Component | System module or component that implements it |
| Test Case ID | The test case(s) that verify it |
| Status | Not Started, In Design, Implemented, Tested, Accepted |

The RTM is maintained throughout the project. When a requirement changes, the RTM immediately shows which test cases and design components are affected — enabling impact analysis.

---

## 5. Verification vs. Validation — Detailed Comparison

| Dimension | Verification | Validation |
|---|---|---|
| Core question | Are we building the requirements right? | Are we building the right requirements? |
| What it checks | Quality of the requirements document | Alignment with actual business need |
| Who performs it | BA with peer reviewers | BA with business stakeholders |
| When it occurs | During requirements analysis | During and after requirements analysis |
| Output | Corrected, well-formed requirements | Confirmed requirements that solve the real problem |
| BABOK task | Verify Requirements | Validate Requirements |

---

## 6. SDLC Phase Alignment for KA 5

KA 5 activities occur primarily during the Systems Analysis phase of the SDLC but continue into design:

- Analysis phase: specify requirements, model them (use cases, DFDs, ERDs), verify quality, validate with stakeholders
- Design phase: define design options, evaluate them against requirements, select the solution approach
- Implementation phase: maintain the RTM as development progresses; manage change requests

---

## 7. BABOK KA 5 Task Summary

| Task | Purpose |
|---|---|
| Specify and Model Requirements | Document requirements in structured formats with appropriate notation |
| Verify Requirements | Check requirements against quality criteria |
| Validate Requirements | Confirm requirements address the real business need |
| Define Requirements Architecture | Organize requirements into a coherent structure |
| Define Design Options | Identify possible solutions and their trade-offs |
| Analyze Potential Value and Recommend Solution | Recommend the best design option |

---

## 8. Certification Exam Tips

1. Functional vs. non-functional is tested on almost every ECBA exam. Functional = what the system does. Non-functional = how well it does it. "The system shall process 500 transactions per second" is non-functional (performance). "The system shall allow a manager to approve a purchase order" is functional.

2. "Testable" is the quality characteristic most commonly featured in ECBA questions. Any requirement with vague language (user-friendly, fast, secure, good, easy) fails testability and must be rewritten with a measurable threshold.

3. Verification checks the quality of the requirements document (well-written, consistent, complete). Validation checks that the requirements address the real business problem. These are two separate BABOK tasks — do not conflate them.

4. Transition requirements appear in multiple Knowledge Areas. They describe temporary capabilities needed only during the changeover — data migration scripts, cutover tools, parallel-running support. They are not ongoing system capabilities.

5. Business rules drive functional requirements but are not themselves requirements. A business rule ("all invoices over $50,000 require dual approval") generates one or more functional requirements ("the system shall prevent single-approver submission for invoices exceeding $50,000").

6. The RTM links requirements to sources, design components, and test cases. Its primary purposes are completeness verification (every requirement is implemented) and impact analysis (what changes when a requirement changes).

7. The IEEE SRS format and IEEE 29148 are referenced in BABOK and may appear on exam questions. Know that an SRS is the formal requirements specification document used in predictive projects.

8. Requirements that cannot be traced to a business need or stakeholder request should be questioned. BABOK's "Necessary" quality criterion means every requirement must have a legitimate origin.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, Knowledge Area 5: Requirements Analysis and Design Definition — all six tasks
- BABOK Guide v3, Chapter 10 (Techniques) — Business Rules Analysis, Data Dictionary, Non-Functional Requirements Analysis, Acceptance and Evaluation Criteria

Supplemental reading:

- IEEE 29148:2018 overview (summary available through IEEE or university library) — standard requirements engineering vocabulary
- Any systems analysis textbook chapter on requirements documentation and the SRS

---

## 10. Study Checklist

- [ ] Name and define all four requirement categories from memory.
- [ ] Define the eight quality characteristics of requirements and give one example failure for each.
- [ ] Explain the difference between verification and validation without looking at your notes.
- [ ] Draw a blank RTM template and label all six standard columns.
- [ ] Read BABOK Guide v3 KA 5 (all six tasks).
- [ ] Watch the Module 04 video lecture.
- [ ] Complete the Module 04 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

---

## 11. Supplemental Resources

The following open educational resources extend module content on requirements analysis and documentation. All are freely accessible without login or purchase.

1. **BABOK Guide v3 — Requirements Analysis and Design Definition (KA 5)**
   <https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/>
   Focus: Official IIBA reference for all six KA 5 tasks. Pay particular attention to the Verify Requirements and Validate Requirements task descriptions, which are directly tested on the ECBA exam.

2. **Writing Good Requirements — Karl Wiegers (Process Impact)**
   <https://www.processimpact.com/articles/reqtips.html>
   Focus: Practical, author-level guidance on writing requirements that are complete, consistent, unambiguous, and testable. Directly reinforces the quality characteristics in Section 2 of this guide.

3. **Requirements Traceability — TechTarget Definition and Guide**
   <https://www.techtarget.com/searchsoftwarequality/definition/requirements-traceability>
   Focus: Plain-language explanation of forward and backward traceability with RTM examples. Supplements Section 4 of this guide and prepares students for the Part 3 RTM lab exercise.

4. **MoSCoW Prioritization Method — Agile Business**
   <https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html>
   Focus: Official Agile Business Consortium explanation of MoSCoW. Covers all four categories with worked examples and common misapplication pitfalls tested on certification exams.

5. **IEEE 29148:2018 Systems and Software Engineering — Requirements Engineering (Overview)**
   <https://www.iso.org/standard/72089.html>
   Focus: ISO/IEEE standard for requirements engineering processes and documentation. Access the standard through your university library proxy. Review the abstract and scope sections to understand how IEEE vocabulary aligns with BABOK terminology used in this module.
