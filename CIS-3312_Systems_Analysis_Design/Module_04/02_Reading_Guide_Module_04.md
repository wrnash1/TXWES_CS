# Reading Guide: Module 04 - Requirements Analysis and Documentation
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 04 – Requirements Analysis and Documentation**! After information is elicited from stakeholders, the business analyst must analyze that raw information to identify actual requirements, resolve conflicts, fill gaps, and organize the requirements into a structured, usable form. This module aligns with BABOK® Guide v3 Knowledge Area 5: Requirements Analysis and Design Definition.

This knowledge area is the intellectual core of business analysis work. You will learn how to specify requirements precisely, distinguish functional from non-functional requirements, model requirements visually, verify and validate them, and produce requirements documents that stakeholders and developers can both understand and use.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Functional Requirement**: A functional requirement describes a specific behavior, action, or capability that a system must perform in order to meet a business need. It defines *what* the system will do — for example, "The system shall allow a registered customer to reset their password via email verification." Functional requirements are testable: for every functional requirement, it should be possible to write a test case that definitively confirms whether the system satisfies it.

*   **Non-Functional Requirement (Quality Attribute)**: A non-functional requirement specifies a quality characteristic or constraint that the system must exhibit, rather than a specific function it must perform. Examples include performance ("The system shall process 500 concurrent transactions without degradation"), security ("All data at rest shall be encrypted using AES-256"), usability, reliability, scalability, and maintainability. Non-functional requirements are often called quality attributes or system constraints.

*   **Business Rule**: A business rule is a statement that defines or constrains some aspect of the business and reflects business policy, regulatory requirement, or contractual obligation. Business rules are not system behaviors; they are conditions the system must enforce. For example, "A customer must be at least 18 years old to apply for a credit account" is a business rule that drives multiple functional requirements in a financial system.

*   **Requirements Traceability**: Requirements traceability is the ability to track each requirement forward to the design elements, test cases, and implemented system features that satisfy it, and backward to the business need or stakeholder request that originated it. A requirements traceability matrix (RTM) documents these linkages, ensuring that every requirement is implemented and tested, and that no implementation exists without a justifying requirement.

*   **Requirements Validation**: Requirements validation is the process of confirming that the documented requirements actually reflect the stakeholders' true needs and that implementing them will address the original business problem. Validation answers the question "Are we building the right thing?" It differs from verification, which answers "Are we building the thing right?" (i.e., do the requirements meet quality standards for completeness, clarity, and consistency).

*   **Software Requirements Specification (SRS)**: A Software Requirements Specification is a formal document that completely describes what a software system must do, the constraints under which it must operate, and the standards it must meet. An SRS typically includes an introduction, overall description, specific functional and non-functional requirements, interface descriptions, and appendices. The IEEE 830 standard provides widely used guidelines for SRS structure.

---

### 2. Certification Exam Tips
*   **Functional vs. Non-Functional**: The ECBA exam regularly tests the ability to classify requirements. If a requirement describes a system *behavior* or *output*, it is functional. If it describes *how well* the system must perform, *how secure* it must be, or *what constraints* it operates under, it is non-functional. A common trap is a requirement like "The system shall be available 99.9% of the time" — this is non-functional (availability/reliability), not functional.
*   **Verification vs. Validation**: Memorize this distinction: **Verification** = are the requirements well-written (complete, clear, consistent, unambiguous, testable)? **Validation** = do the requirements correctly represent stakeholder needs? The ECBA exam will present a scenario and ask which activity is being performed.
*   **Traceability Matrix**: Know that an RTM maps requirements to their source (stakeholder, business need) and forward to design components and test cases. The exam may ask what the *purpose* of an RTM is — the answer is to ensure completeness (every requirement is addressed) and to manage impact analysis (if requirement X changes, which test cases and design elements are affected?).
*   **Study Resource**: The IEEE Computer Society publishes IEEE Std 830-1998 (SRS guidelines) and the newer ISO/IEC/IEEE 29148:2018 on requirements engineering — summaries are available at [https://standards.ieee.org/](https://standards.ieee.org/). The BABOK® techniques appendix also includes a detailed "Requirements Documentation" technique worth studying.

---

### Required Readings & Videos
*   **Required Reading**: BABOK® Guide v3 Chapter 6 — "Requirements Analysis and Design Definition." Focus on: Specify and Model Requirements, Verify Requirements, Validate Requirements, Define Requirements Architecture, and Define Design Options. Pay particular attention to the techniques: business rules analysis, data dictionary, functional decomposition, and non-functional requirements analysis.
*   **Supplemental Reading**: Review the IEEE 830 SRS template overview at [https://standards.ieee.org/](https://standards.ieee.org/) to understand how formal requirements documents are structured in professional practice.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Given a paragraph of elicitation notes, extract and classify at least six requirements (functional vs. non-functional vs. business rule) using a structured table.
*   Write three well-formed functional requirements using the "The system shall..." format, ensuring each is clear, complete, and testable.
*   Create a mini requirements traceability matrix mapping three requirements to their source stakeholder and to a corresponding test case description.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Read BABOK® Guide v3 Chapter 6 (Requirements Analysis and Design Definition).
- [ ] Watch the Module 04 video lecture.
- [ ] Review IEEE 830 SRS structure guidelines at [https://standards.ieee.org/](https://standards.ieee.org/).
- [ ] Complete the requirements classification and traceability matrix lab before taking the quiz.
