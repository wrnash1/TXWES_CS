# Discussion Forum: Module 06 - Data Flow Diagrams and Entity-Relationship Diagrams

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Your initial post must address all three sub-questions for your chosen scenario.

Initial Post: Due Wednesday at 11:59 PM (175–225 words)

Peer Responses: Due Sunday at 11:59 PM (reply to at least two classmates who chose different scenarios; minimum 75 words each)

---

## Scenario A: The Unbalanced DFD

A junior BA delivers a two-level DFD for a hospital patient registration system. The Level 0 Context Diagram shows four data flows crossing the system boundary: "Patient Registration Form," "Insurance Verification Request," "Insurance Approval," and "Appointment Confirmation." The Level 1 diagram shows only three internal processes and includes "Patient Registration Form" and "Appointment Confirmation" as boundary flows. It is missing "Insurance Verification Request" and "Insurance Approval." The senior BA reviewing the work flags the Level 1 diagram as non-deliverable and sends it back.

Sub-questions:

1. Explain what level balancing means in the context of DFDs, and explain specifically why the Level 1 diagram in this scenario fails the balancing test. What exact correction must the BA make?
2. The Level 1 diagram also shows a data flow arrow going directly from a data store labeled "Patient Records" to a data store labeled "Billing Archive." Identify the DFD rule this violates and explain what should appear between these two data stores instead.
3. The BA argues that the missing insurance flows are handled "inside" the Level 1 processes and do not need to appear as boundary flows. Is this argument correct? Explain why or why not, using the definition of a system boundary data flow.

---

## Scenario B: Cardinality in Conflict

A development team is building a university course registration system. The data modeler on the team draws an ERD and marks the Student-to-Course relationship as 1:N — one student can enroll in many courses, and each course is associated with exactly one student. The BA reviewing the ERD immediately flags this as incorrect. When the data modeler corrects it to M:N, the database developer says: "You can't implement M:N directly in a relational database. You need a junction table." The modeler has never heard this term.

Sub-questions:

1. Explain why the original 1:N cardinality is incorrect for the Student-to-Course relationship. Use the actual real-world relationship between students and courses to justify the correct cardinality.
2. Explain what a junction table is, why it is required to resolve a many-to-many relationship in a relational database, and identify the two foreign keys the junction table would contain in this specific scenario.
3. After adding the junction table (named Enrollment), the BA also requires that the Enrollment entity capture the semester and grade for each enrollment record. Explain why these attributes belong in the Enrollment junction table rather than in the Student or Course entity.

---

## Scenario C: DFD vs. ERD — The Right Tool at the Wrong Time

A business stakeholder asks the BA to explain the data that the company's new order management system will store — specifically, how customers relate to orders, how orders relate to products, and how many products an order can contain. The BA responds by producing a Level 1 DFD showing four processes (Accept Order, Validate Payment, Update Inventory, Send Confirmation), three data stores (Customer Records, Order History, Product Catalog), and data flows between them. The stakeholder reviews the diagram and says: "This doesn't answer my question. I can see the data moves around, but I still don't know how customers and orders are actually related or how many products an order can have."

Sub-questions:

1. Explain why the DFD does not answer the stakeholder's question. What specific type of information does a DFD show, and what type of information does it not show?
2. Identify which diagram type would correctly answer the stakeholder's question. Describe what that diagram would show for the Customer-Order relationship and the Order-Product relationship, including the cardinality of each.
3. A colleague suggests that DFDs and ERDs are redundant — if you have one, you do not need the other. Evaluate this argument. Describe one scenario in which a BA would need both a DFD and an ERD to fully communicate the requirements of the same system.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5–6 pts | Addresses all three sub-questions with specific evidence from the scenario. Uses correct DFD and ERD terminology. Meets the 175–225 word count. |
| 3–4 pts | Addresses most sub-questions but lacks specificity or misuses terminology. Slightly outside the word count. |
| 1–2 pts | Addresses only one sub-question or provides only vague, generic responses. |
| 0 pts | No initial post submitted by the deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Responds to at least two classmates who chose different scenarios. Each reply is at least 75 words and adds substantive analysis. |
| 2 pts | Responds to only one classmate, or both responses are fewer than 75 words or superficial. |
| 0 pts | No peer responses submitted. |

---

## A Note from Professor Nash

DFDs and ERDs answer different questions. If a stakeholder asks "what does the system do with data?" you draw a DFD. If they ask "what data does the system store and how is it structured?" you draw an ERD. The mistake most students make is treating these as interchangeable. They are not — they model different dimensions of the same system. A complete systems analysis uses both. The DFD tells the story of data in motion; the ERD reveals the structure underneath. Professional BAs know which question they are answering before they pick up a pencil.
