# Lab Activity: Module 06 - Data Flow Diagrams and Entity-Relationship Diagrams

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab gives you hands-on practice with two foundational visual modeling techniques: Data Flow Diagrams (DFDs) and Entity-Relationship Diagrams (ERDs). You will draw diagrams using a single case study, write a brief analysis of a DFD rule violation, and document a many-to-many resolution. No software installation or terminal commands are required. You may use any diagramming tool (draw.io, Lucidchart, PowerPoint, or hand-drawn and photographed).

---

## Case Study: Ridgeview Community Library — Checkout System

Ridgeview Community Library is modernizing its patron services system. A BA has conducted requirements elicitation and identified the following information:

- Patrons register for a library card by providing their name, address, and email. The system assigns a unique patron ID.
- Patrons can search the catalog and check out physical books. When a patron checks out a book, the system records the checkout date and calculates the due date (21 days).
- Patrons can return books. When a book is returned, the system marks it available and checks whether a hold is waiting.
- Patrons can place holds on books that are currently checked out. When a held book is returned, the system notifies the patron by email.
- Librarians can add new books to the catalog, update book information, and remove items from circulation.
- The system sends overdue notices to patrons when items are not returned by the due date. Overdue notices are generated automatically.
- An external Email Service processes all outgoing notifications (hold notifications and overdue notices).

---

## Part 1: Context Diagram (Level 0 DFD) — 25 Points

### Part 1 Instructions

Draw a Context Diagram (Level 0 DFD) for the Ridgeview Community Library Checkout System.

Your diagram must include:

- A single process bubble labeled "Ridgeview Library Checkout System"
- A system boundary rectangle
- All external entities identified from the case study (minimum 3)
- All data flows between the system and the external entities, each labeled with the name of the data being carried
- Correct DFD notation for all symbols (rectangle for entity, arrow for flow)

You do not need to show any internal processes, data stores, or internal flows at Level 0.

### Grading Rubric — Part 1

| Criterion | Points |
|---|---|
| System boundary present with labeled process bubble | 4 |
| All external entities correctly identified and labeled (3 pts each, minimum 3) | 9 |
| All data flows present and labeled between entities and system | 8 |
| Correct DFD notation used for all symbols | 4 |

Part 1 Total: 25 points

---

## Part 2: Level 1 DFD — 35 Points

### Part 2 Instructions

Decompose the Context Diagram into a Level 1 DFD for the Ridgeview Library Checkout System.

Your Level 1 diagram must include:

- At least four numbered processes with descriptive verb-noun names (e.g., "Validate Patron," "Record Checkout")
- At least three data stores with descriptive names derived from the case study
- Internal data flows between processes and data stores, each labeled
- All external entities from Part 1, with data flows from Part 1 re-appearing at this level (level balancing)
- Correct DFD notation for all symbols

After drawing the diagram, answer the following question in 3–5 sentences: How did you verify that your Level 1 DFD is balanced with your Level 0 Context Diagram? Identify one specific data flow that appears in both levels and explain how you confirmed they match.

### Grading Rubric — Part 2

| Criterion | Points |
|---|---|
| At least 4 processes with descriptive verb-noun names (3 pts each) | 12 |
| At least 3 data stores correctly labeled | 6 |
| Internal data flows labeled between processes and data stores | 7 |
| Level balancing: all Level 0 boundary flows present at Level 1 | 6 |
| Written balancing analysis (3–5 sentences) | 4 |

Part 2 Total: 35 points

---

## Part 3: Entity-Relationship Diagram — 25 Points

### Part 3 Instructions

Draw an Entity-Relationship Diagram (ERD) for the Ridgeview Library Checkout System using Crow's Foot notation.

Your ERD must include:

- At least five entities derived from the case study, each with at least two attributes listed (including the primary key, underlined)
- Correct Crow's Foot notation for all relationship lines (cardinality indicators on both ends)
- At least one 1:N relationship correctly modeled
- At least one M:N relationship, resolved with a junction entity (the junction entity must appear in the diagram with its own attributes)
- Relationship names (verb phrases) labeled on each relationship line

After drawing the diagram, answer the following question in 2–3 sentences: Identify the M:N relationship in your diagram. Name the junction entity you created to resolve it and list the two foreign keys the junction entity contains.

### Grading Rubric — Part 3

| Criterion | Points |
|---|---|
| At least 5 entities with primary keys and attributes (2 pts each) | 10 |
| Crow's Foot cardinality notation correctly applied on both ends of each relationship | 6 |
| At least one M:N relationship resolved with a correctly drawn junction entity | 5 |
| Written M:N resolution analysis (2–3 sentences) | 4 |

Part 3 Total: 25 points

---

## Part 4: DFD Rule Violation Analysis — 15 Points

### Part 4 Instructions

Read the following description of a flawed DFD and answer the three questions below. Write your answers in complete sentences. Each answer should be 2–4 sentences.

Scenario: A junior analyst draws a DFD for a payroll system. The diagram shows a data store labeled "Employee Records" with an arrow going directly to a data store labeled "Payroll Archive." The diagram also shows an external entity labeled "Tax Authority" with an arrow going directly to an external entity labeled "State Comptroller" without passing through any system process. Finally, one process bubble labeled "Generate Report" has three incoming data flows but no outgoing data flows.

Question 1: Identify the DFD rule violated by the direct data store to data store connection. Explain what should replace it and why.

Question 2: Identify the DFD rule violated by the direct external entity to external entity connection. Explain why this violates DFD principles.

Question 3: What is the name for the type of process error shown in the "Generate Report" bubble? Explain what is wrong and how it should be corrected.

### Grading Rubric — Part 4

| Criterion | Points |
|---|---|
| Question 1: Correctly identifies violation and explains fix (5 pts) | 5 |
| Question 2: Correctly identifies violation and explains principle (5 pts) | 5 |
| Question 3: Names the error type, explains the problem, and describes the correction (5 pts) | 5 |

Part 4 Total: 15 points

---

## Submission Instructions

Combine all four parts into one document with clearly labeled sections. For diagram parts, embed the diagram image or include a link to the shared diagram file. For written analysis parts, type your responses directly in the document. Submit to the Canvas Module 06 Lab assignment by the due date shown in the course calendar.

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced modeling practice aligned with ECBA exam competencies.

### Challenge Step 1: Level 2 DFD Decomposition

Select one of the processes from your Level 1 DFD completed in the main lab. Decompose it into a Level 2 DFD showing the internal sub-processes, data flows, and data stores within that single process. Your Level 2 must be balanced with the Level 1 — every data flow entering or leaving the parent process at Level 1 must also appear as a boundary flow at Level 2. Label all elements using the correct DFD naming conventions. Include a brief written note explaining how you verified balance between Level 1 and Level 2. This exercise practices the DFD leveling and balancing rules that are among the most commonly tested concepts on the ECBA exam.

### Challenge Step 2: ERD Extended Modeling with Weak Entities

Review your ERD from the main lab. Identify whether any entity in your diagram is a weak entity — one that cannot be uniquely identified without reference to a parent entity (for example, an "OrderLine" that only makes sense in the context of a specific "Order"). If a weak entity exists, model it correctly using a double rectangle and a double diamond relationship. If no weak entity exists, redesign one entity to introduce a weak entity scenario and explain your reasoning. Write a one-paragraph explanation of what a weak entity is, why it arises in business data models, and how it is physically implemented in a relational database.

### Challenge Step 3: Cross-Model Consistency Audit

Perform a consistency audit across your three diagrams (Context Diagram, Level 1 DFD, and ERD). Check: (1) Every data element named in a DFD data flow should correspond to an entity or attribute in the ERD — list any DFD flows that reference data not represented in the ERD. (2) Every data store in the DFD should correspond to an entity or table in the ERD. (3) Every external entity in the DFD should be referenced in at least one data flow that connects to the data stored in the ERD. Document your findings as a three-column audit table: DFD Element | ERD Counterpart | Consistent (Yes/No). This cross-model consistency check mirrors the traceability work that BAs perform when handing off models to database architects.
