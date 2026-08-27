# Lab Activity: Module 01 - Introduction to Systems Analysis and the SDLC

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab introduces you to the two foundational skills of a business analyst: recognizing where you are in the SDLC and understanding your system's scope. There are no terminal commands, no programming, and no software to install. This is a thinking and communication lab — the kind of work business analysts actually do.

You will complete two parts. Part 1 asks you to identify the correct SDLC phase for a set of real-world project scenarios. Part 2 asks you to sketch a system boundary diagram for a university registration system.

Read each part carefully before you begin. Submit your completed lab as a single document (Word or PDF) to the Canvas assignment portal.

---

## Part 1: SDLC Phase Identification (50 points)

### Background

The five classic SDLC phases are:

1. Planning — feasibility, project charter, go/no-go decision
2. Systems Analysis — requirements elicitation, stakeholder analysis, process modeling
3. Systems Design — logical and physical design, architecture decisions
4. Implementation — coding, testing, data migration, training, deployment
5. Maintenance and Support — post-deployment enhancements, bug fixes, ongoing change requests

### Instructions

For each of the ten scenarios below, identify which single SDLC phase is most accurately described. Write the phase name and a one-sentence justification explaining why that phase applies.

### Scenarios

**Scenario A:** The IT steering committee at Westbrook Bank has received a proposal to replace its 15-year-old branch teller system. A team has been assigned to investigate whether the replacement is technically achievable within the bank's infrastructure and whether the projected cost savings over five years justify the $4.2 million investment estimate.

**Scenario B:** A business analyst at a regional healthcare network is conducting structured interviews with nurses, physicians, billing specialists, and compliance officers to understand what information a new patient portal must display and what actions users must be able to perform.

**Scenario C:** A development team at an e-commerce company is writing Python code for the order fulfillment microservice, while the QA team is executing 340 test cases against the completed checkout and payment modules.

**Scenario D:** The database architect at a logistics company is translating an approved entity-relationship diagram into a PostgreSQL schema with table definitions, indexes, and foreign key constraints.

**Scenario E:** The help desk team at a manufacturing firm has received 22 tickets this month from users of the production scheduling system. Seventeen tickets are enhancement requests and five are bug reports. The BA is reviewing them to determine which should be addressed in the next quarterly update.

**Scenario F:** A BA at a university is facilitating a requirements workshop with the registrar's office, financial aid, and the bursar to define the business rules that govern course add/drop eligibility and financial holds on student accounts.

**Scenario G:** A project manager at an insurance company is preparing a project proposal document that defines the business problem, the proposed solution concept, the estimated duration, and the names of the executive sponsors. No requirements have been gathered yet.

**Scenario H:** A trainer at a city government agency is conducting four-hour sessions for 60 municipal clerks on how to use the newly deployed permit management system, using a test environment loaded with simulated permit applications.

**Scenario I:** A BA is reviewing an approved requirements specification and creating a context diagram and a Level 1 Data Flow Diagram to represent the information flows in the proposed inventory management system — without specifying any database product or programming language.

**Scenario J:** The operations team at a telecommunications company notices that the billing system is producing duplicate invoices for customers who change their service plan mid-month. A BA has been assigned to analyze the defect, document the corrected business rule, and coordinate the fix with the development team.

### Part 1 Deliverable

For each scenario (A through J), write:

- Phase name
- One-sentence justification

---

## Part 2: System Boundary Diagram (50 points)

### Background

A system boundary diagram (also called a context diagram or Level 0 DFD) presents the entire system as a single process, defines the boundary between the system and its environment, and identifies all external entities that either send data to the system or receive data from it.

This type of diagram is one of the first artifacts a BA produces because it communicates scope — what is inside the system and what is outside — before any detailed requirements work begins.

### The Case Study: Sparrow Ridge University Course Registration System

Sparrow Ridge University wants to build a new online course registration system. You have conducted stakeholder interviews and gathered the following information:

- Students search the course catalog, register for courses, drop courses, and view their personal schedule. After registration closes, students receive a confirmation email.
- Faculty submit their course offerings (course title, section, time, room, capacity) before each semester opens for registration. Faculty also receive an enrollment report at the end of the registration period.
- The Registrar's Office manages course prerequisites rules and can override enrollment restrictions for individual students. The Registrar receives daily enrollment summary reports.
- The Financial Aid Office must be notified when a student's total registered credits drop below 12 (full-time threshold), because aid eligibility may change.
- The University Billing System (a separate existing system) receives a nightly batch file containing each registered student's credit hours so it can calculate tuition charges.
- The system must check the Campus Facilities Database (another existing system) when a faculty member requests a room assignment to confirm that the requested room is available.

### Instructions

Using the information above, create a system boundary diagram for the Sparrow Ridge Course Registration System.

Your diagram must include:

- One central process bubble labeled "Course Registration System"
- A dashed or solid boundary rectangle enclosing the process bubble
- All external entities as labeled rectangles outside the boundary
- All data flows as labeled arrows showing direction (into or out of the system)
- Every data flow must have a descriptive name (for example, "Course Offering Submission" or "Enrollment Confirmation Email")

You may draw this diagram by hand and photograph it, use any diagramming tool (Lucidchart, Draw.io, Microsoft Visio, PowerPoint SmartArt, or pencil and paper), or use any format that is legible and clearly labeled.

### Part 2 Deliverable

Submit your completed system boundary diagram as an image or embedded in your lab document.

---

## Grading Rubric

### Part 1 — SDLC Phase Identification (50 points)

| Criterion | Points |
|---|---|
| Each of the 10 scenarios correctly identified (5 pts each) | 50 |

Partial credit: 3 points for a plausible answer with a weak justification; 0 points for an incorrect phase with no justification.

### Part 2 — System Boundary Diagram (50 points)

| Criterion | Points |
|---|---|
| All external entities present and correctly labeled (6 entities x 3 pts) | 18 |
| Central process bubble labeled correctly | 5 |
| System boundary clearly shown | 5 |
| All data flows present with directional arrows (minimum 10 flows) | 15 |
| Data flow labels are descriptive and accurate | 7 |

Total: 100 points

---

## Submission Instructions

Combine both parts into one document. Label each section clearly. Submit to the Canvas Module 01 Lab assignment by the due date shown in the course calendar.

---

## Part 9 — Challenge Exercise

This section is optional but strongly recommended for students pursuing the IIBA ECBA certification or seeking a deeper understanding of systems analysis practice. Challenge exercises are not graded separately; exceptional work here can be cited in your discussion board responses.

### Challenge Step 1: Stakeholder Register Construction

Using the Sparrow Ridge University Course Registration System case study from Part 2, build a formal stakeholder register. For each external entity you identified in your context diagram, create a stakeholder register entry with the following fields:

- Stakeholder name or role
- Stakeholder category (End User / Sponsor / SME / Regulator / External System)
- Primary interest in the system (what they want or need from it)
- Potential concern or risk (what could go wrong for this stakeholder)
- Engagement level needed (Inform / Consult / Collaborate / Approve)

Document at least six stakeholder entries. Justify your engagement level assignment for each one with a one-sentence rationale. This exercise mirrors BABOK KA 2 (BA Planning and Monitoring) stakeholder identification tasks that appear on the ECBA exam.

### Challenge Step 2: Feasibility Recommendation Memo

Write a one-page (approximately 300–400 word) feasibility recommendation memo addressed to the fictional Sparrow Ridge University CIO. Your memo must:

- Assess all four feasibility dimensions (Technical, Economic, Operational, Legal) for the proposed registration system
- Identify at least one significant risk for each dimension based on what you know from the case study
- Conclude with a clear recommendation: Proceed, Proceed with Modifications, or Do Not Proceed
- Use professional business memo format (To / From / Date / Subject / Body / Recommendation)

This exercise mirrors the Planning phase deliverable expected of a BA before a project receives formal sponsorship. ECBA exam scenarios frequently test whether students can identify which feasibility dimension applies to a described risk condition.

### Challenge Step 3: BACCM Mapping

Select any real-world technology project you have read about, experienced, or observed (a mobile app, a campus system change, a government digital service, etc.). Write a short analysis (one paragraph per concept) mapping the project to all six BACCM concepts: Change, Need, Solution, Stakeholder, Value, and Context. Be specific — do not write generic definitions; apply each concept to your chosen project. This exercise develops the analytical habit of mapping real-world scenarios to the BABOK framework, which is the primary skill tested on the ECBA exam.
