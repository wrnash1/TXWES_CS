# Quiz: Module 01 - Introduction to Systems Analysis and the SDLC

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

According to BABOK Guide v3, what is the primary purpose of business analysis?

A) To write source code that implements the business requirements

B) To manage the project schedule and budget on behalf of the sponsor

C) To enable change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders

D) To test the delivered system and certify it meets performance benchmarks

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Writing source code is the responsibility of developers, not business analysts.
- Why B is incorrect: Managing schedules and budgets is the role of the project manager, a distinct role from the BA.
- Why D is incorrect: Certifying system performance is a QA/testing function; BAs may participate in acceptance testing but it is not their primary purpose.
- Why C is correct: This is the verbatim IIBA BABOK Guide v3 definition of business analysis purpose.

---

## Question 2

In the context of systems analysis, which of the following is the most accurate definition of a stakeholder?

A) A person who writes the technical specifications and architecture documents for a new system

B) Any individual, group, or organization that has an interest in or is affected by the outcome of a system change

C) The senior developer responsible for approving code commits and managing the version control repository

D) A formal document that records the agreed-upon requirements baseline signed by the project sponsor

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Writing technical specifications is a task, not a definition of a stakeholder category.
- Why C is incorrect: A senior developer is one specific type of stakeholder, not the definition of the concept itself.
- Why D is incorrect: This describes a requirements baseline document, not a stakeholder.
- Why B is correct: This aligns with the BABOK Guide v3 definition; stakeholders include users, sponsors, SMEs, regulators, and the development team.

---

## Question 3

A project team has just completed the planning phase and confirmed executive sponsorship. Which SDLC phase should they enter next?

A) System Design

B) Implementation

C) Systems Analysis (Requirements)

D) Maintenance

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: System design cannot begin until requirements have been elicited and analyzed.
- Why B is incorrect: Implementation is among the last phases; beginning here skips requirements and design entirely.
- Why D is incorrect: Maintenance occurs after a system is deployed and operating; it is not a successor to planning.
- Why C is correct: After planning confirms the project is authorized, the team moves into systems analysis to elicit and document stakeholder requirements before any design work begins.

---

## Question 4

During a feasibility study, the project team determines that the proposed system cannot be built with current staff skills and available technology within the project timeline. Which type of feasibility has failed?

A) Economic feasibility

B) Legal feasibility

C) Operational feasibility

D) Technical feasibility

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: Economic feasibility concerns whether the benefits justify the costs; it does not address staff skills or technology availability.
- Why B is incorrect: Legal feasibility addresses regulatory and compliance concerns, not technical capability.
- Why C is incorrect: Operational feasibility assesses whether users will adopt the system and whether it fits organizational processes, not whether it can technically be built.
- Why D is correct: Technical feasibility evaluates whether the organization has or can acquire the technology, infrastructure, and skills needed to build and operate the proposed system.

---

## Question 5

A business analyst is reviewing a project charter and notices that the document focuses entirely on budget, schedule, and resource allocation but contains no statement of business need or problem description. Which critical element of good systems analysis is missing?

A) A Gantt chart showing task dependencies and milestone dates

B) A clear problem statement that identifies the root cause the system is intended to solve

C) A data dictionary defining all database field names and data types

D) A network diagram showing server topology and firewall placement

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: A Gantt chart is a project management planning tool; its absence does not represent a systems analysis deficiency.
- Why C is incorrect: A data dictionary is a design-phase artifact produced after requirements are established, not an early project charter element.
- Why D is incorrect: Network and infrastructure diagrams are physical design artifacts; they are not expected in an early project charter.
- Why B is correct: The BABOK Guide emphasizes that business analysis begins with a clear understanding of the business need or problem; without this, requirements are likely to be misaligned with organizational goals.

---

## Question 6

Which of the following activities belongs in the Systems Design phase of the SDLC, not the Systems Analysis phase?

A) Conducting stakeholder interviews to understand current-state pain points

B) Creating a context diagram to define the system boundary and external entities

C) Specifying that the system will use a PostgreSQL database with a React front end

D) Documenting a business rule that all purchase orders over $5,000 require manager approval

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Stakeholder interviews are an elicitation technique performed during Systems Analysis to gather requirements.
- Why B is incorrect: A context diagram defines scope; it is a systems analysis artifact belonging in the analysis phase.
- Why D is incorrect: Documenting business rules is a requirements activity belonging in Systems Analysis.
- Why C is correct: Naming specific technologies (PostgreSQL, React) is a physical design decision belonging in Systems Design. Analysis produces technology-neutral requirements; design maps those requirements to specific platforms.

---

## Question 7

The Business Analysis Core Concept Model (BACCM) defines six interrelated concepts that frame all BA work. Which of the following is NOT one of the six BACCM concepts?

A) Change

B) Value

C) Risk

D) Context

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Change is one of the six BACCM concepts — it represents the act of transformation an enterprise undertakes in response to a need.
- Why B is incorrect: Value is one of the six BACCM concepts — it represents the worth of a solution to stakeholders.
- Why D is incorrect: Context is one of the six BACCM concepts — it encompasses the circumstances and environment influencing the change.
- Why C is correct: Risk is not one of the six BACCM concepts. The six are: Change, Need, Solution, Stakeholder, Value, and Context. Risk management is addressed separately in BABOK under BA Planning, not in the BACCM.

---

## Question 8

A large retail company is building a new inventory management system. A BA interviews warehouse staff and discovers they rely entirely on handwritten logs because the current digital system crashes frequently. The BA documents this finding as part of the analysis. Which SDLC phase activity does this best represent?

A) Planning — assessing whether the new system is economically justified

B) Systems Analysis — understanding the current state and documenting stakeholder pain points

C) Systems Design — specifying the reliability requirements for the new system's uptime

D) Maintenance — logging a defect report against the existing production system

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Planning involves high-level feasibility assessment; detailed discovery of how users cope with system failures is an analysis-phase activity.
- Why C is incorrect: Translating the finding into a non-functional reliability requirement would be a design artifact; documenting the current-state pain point itself is analysis work.
- Why D is incorrect: Maintenance involves managing changes to a deployed system; the team is performing analysis on the current-state system to define future-state needs.
- Why B is correct: Current-state analysis — observing how users actually work today, including workarounds and pain points — is a core Systems Analysis activity. This finding will drive the reliability requirement for the new system.

---

## Question 9

Which of the following best describes the difference between functional requirements and non-functional requirements?

A) Functional requirements are written by developers; non-functional requirements are written by business analysts

B) Functional requirements describe what the system must do; non-functional requirements describe how well the system must do it

C) Functional requirements apply to the user interface only; non-functional requirements apply to the database layer only

D) Functional requirements are mandatory; non-functional requirements are optional enhancements

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Both types of requirements are elicited and documented by the BA in collaboration with stakeholders; authorship does not distinguish them.
- Why C is incorrect: Functional requirements apply to all system behaviors regardless of layer; non-functional requirements apply system-wide.
- Why D is incorrect: Non-functional requirements are not optional; a system that fails its performance or security requirements has failed even if all functional behaviors work correctly.
- Why B is correct: This is the standard BABOK and IEEE definition. Functional = what the system does (behaviors, features). Non-functional = quality attributes — how fast, how secure, how available, how usable.

---

## Question 10

A stakeholder tells the BA: "I know what the system should do — just build it the way the old one works, but faster." The BA suspects this statement contains an unstated assumption about the solution and may be masking a deeper business need. Which BA approach is most appropriate?

A) Accept the statement at face value and document it as a confirmed functional requirement

B) Escalate the stakeholder's comment to the project manager as a scope change request

C) Use elicitation techniques such as asking "why" and exploring root causes to uncover the underlying business need behind the stated solution preference

D) Reject the requirement because stakeholders are not permitted to propose solutions

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Accepting a solution preference as a requirement without understanding the underlying need is a classic analysis error; it risks implementing the wrong solution.
- Why B is incorrect: This is an elicitation and requirements problem, not a scope change; escalating prematurely is inappropriate before the BA has clarified the actual need.
- Why D is incorrect: Stakeholders are permitted — and encouraged — to propose solutions; the BA's job is to distinguish between a stated solution and the underlying need it is meant to address, not to reject stakeholder input.
- Why C is correct: Using root-cause elicitation (asking "why does the system need to be faster?" and "what problem does the current speed cause?") surfaces the actual need and enables the team to evaluate multiple solution options, not just the one the stakeholder suggested.
