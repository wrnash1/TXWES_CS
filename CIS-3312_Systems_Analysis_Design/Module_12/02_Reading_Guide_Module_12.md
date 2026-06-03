# Reading Guide: Module 12 — Database Normalization for Business Analysts

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Overview

This reading guide supports Module 12's video lecture and prepares you for the lab, quiz, and discussion activities. Database normalization is a core data-modeling technique explicitly recognized in the BABOK Guide under the Data Modeling technique. Understanding normal forms allows a BA to validate that proposed data structures will support business rules without causing anomalies.

**Estimated reading and study time:** 90–120 minutes

---

## Learning Objectives

By the end of this module you will be able to:

1. Define functional dependency and identify examples in business data.
2. Distinguish between partial and transitive dependencies.
3. Apply 1NF, 2NF, and 3NF rules to a given table.
4. Document a normalization decomposition with before/after table diagrams.
5. Articulate the business case for denormalization in specific scenarios.
6. Connect normalization concepts to ECBA knowledge area: Requirements Analysis and Design Definition.

---

## Section 1 — Why Normalization Matters to a BA

### 1.1 The BA's Role in Data Design

Business analysts are not database administrators, but they are responsible for ensuring that the data requirements they capture will actually work in an implemented system. A BA who documents data requirements without understanding normalization risks producing specifications that lead to flawed database designs.

The three data anomalies that normalization prevents are central to understanding why the technique exists:

- **Update anomaly:** The same fact stored in multiple places. Changing it in one place leaves contradictory data elsewhere.
- **Insertion anomaly:** Inability to record a fact without also recording another, unrelated fact.
- **Deletion anomaly:** Removing one fact inadvertently destroys another unrelated fact.

### 1.2 BABOK Alignment

The BABOK Guide (3rd edition) includes Data Modeling as a technique under the Requirements Analysis and Design Definition knowledge area. Data models produced by BAs must be logically consistent and free of structural defects. Normalization is the mechanism that achieves logical consistency.

ECBA candidates should be familiar with:

- Entity-relationship concepts (entities, attributes, relationships)
- The purpose of primary and foreign keys
- The definition and application of normal forms through 3NF

---

## Section 2 — Functional Dependencies

### 2.1 Core Definition

A functional dependency exists between two attributes when the value of one attribute uniquely determines the value of another.

Notation: A → B ("A functionally determines B")

The attribute on the left is the **determinant**. The attribute on the right is the **dependent**.

### 2.2 Business Examples

The following examples illustrate functional dependencies found in common business systems.

| Determinant | Dependent | Context |
|---|---|---|
| EmployeeID | EmployeeName | HR system — one ID per employee |
| ProductSKU | ProductDescription | Inventory — one description per SKU |
| (OrderID, LineNum) | Quantity | Order entry — quantity is per order line |
| ZIP_Code | City | Address — ZIP determines city |
| InvoiceID | InvoiceDate | Billing — one date per invoice |

### 2.3 Identifying Dependencies Through Elicitation

During requirements elicitation, you uncover functional dependencies by asking:

- "If I give you a [CustomerID], can you always tell me exactly one [CustomerName]?"
- "Can two different [OrderIDs] ever have the same [OrderDate]?" (If yes, OrderDate is still functionally dependent on OrderID — two orders can share a date, but each order has exactly one date.)
- "Does [ProductPrice] ever change independently of [ProductID]?" (If price can vary by time period, the dependency is more complex.)

This questioning technique maps directly to the ECBA elicitation competency.

### 2.4 Composite Keys and Multi-Valued Dependencies

When no single attribute uniquely identifies a row, a composite key is needed. For example, in an enrollment table, neither StudentID alone nor CourseID alone identifies a unique row — the combination (StudentID, CourseID) does.

Any attribute that requires the full composite key to be determined is **fully functionally dependent** on that key.

Any attribute determined by only part of the composite key has a **partial dependency** — a 2NF violation.

---

## Section 3 — First Normal Form (1NF)

### 3.1 Rules

A table is in First Normal Form when:

1. All attribute values are atomic (indivisible, single-valued).
2. There are no repeating groups of columns.
3. A primary key exists.

### 3.2 Violations and Corrections

**Violation type A — Multi-valued attribute:**

A Tags column containing "urgent, review, escalated" is not atomic. Fix: create a separate Tags table with one row per tag.

**Violation type B — Repeating column groups:**

Columns named Phone1, Phone2, Phone3 represent a repeating group. Fix: create a separate PhoneNumbers table.

### 3.3 Practice Scenario

A training department tracks employee certifications in a single table with columns:

EmployeeID | EmployeeName | Cert1 | Cert2 | Cert3

Identify the 1NF violation and describe the corrected table structure.

**Answer:** The Cert1/Cert2/Cert3 columns are a repeating group. The corrected structure uses two tables: Employees (EmployeeID, EmployeeName) and Certifications (EmployeeID, CertificationName), with primary key (EmployeeID, CertificationName).

---

## Section 4 — Second Normal Form (2NF)

### 4.1 Rules

A table is in Second Normal Form when:

1. It is already in 1NF.
2. Every non-key attribute is fully functionally dependent on the entire primary key.

2NF only applies to tables with composite primary keys. A table with a single-column primary key is automatically in 2NF.

### 4.2 Identifying Partial Dependencies

Ask: "For this non-key attribute, do I need both parts of the composite key, or just one part?"

If only one part of the key determines the attribute, you have a partial dependency.

### 4.3 Decomposition Process

When a partial dependency is found:

1. Remove the partially dependent attributes from the original table.
2. Create a new table using the key part as its primary key.
3. Move the partially dependent attributes into the new table.
4. Retain the key part as a foreign key in the original table.

### 4.4 Extended Example

Consider a ProjectAssignments table:

| ProjectID | EmployeeID | HoursWorked | ProjectName | ProjectBudget | EmployeeName |
|---|---|---|---|---|---|

Primary key: (ProjectID, EmployeeID)

Dependency analysis:

- HoursWorked → (ProjectID, EmployeeID) — full dependency, stays
- ProjectName → ProjectID only — partial dependency, move to Projects
- ProjectBudget → ProjectID only — partial dependency, move to Projects
- EmployeeName → EmployeeID only — partial dependency, move to Employees

Result after 2NF decomposition:

**ProjectAssignments:** (ProjectID, EmployeeID, HoursWorked)

**Projects:** (ProjectID, ProjectName, ProjectBudget)

**Employees:** (EmployeeID, EmployeeName)

---

## Section 5 — Third Normal Form (3NF)

### 5.1 Rules

A table is in Third Normal Form when:

1. It is already in 2NF.
2. Every non-key attribute is non-transitively dependent on the primary key — that is, no non-key attribute determines another non-key attribute.

### 5.2 The Transitive Dependency Pattern

A transitive dependency follows this pattern:

PrimaryKey → AttributeA → AttributeB

AttributeB is determined by a non-key attribute (AttributeA), not directly by the primary key.

### 5.3 Business Context Example

A Vendors table:

| VendorID | VendorName | StateCode | StateName | StateTaxRate |
|---|---|---|---|---|

Primary key: VendorID

VendorID → StateCode is fine.

But StateName and StateTaxRate depend on StateCode, not on VendorID. The transitive chain is:

VendorID → StateCode → StateName
VendorID → StateCode → StateTaxRate

Fix by decomposing:

**Vendors:** (VendorID, VendorName, StateCode)

**States:** (StateCode, StateName, StateTaxRate)

### 5.4 The 3NF Mnemonic

"Every non-key attribute must depend on the key, the whole key, and nothing but the key."

This phrase encapsulates all three normal forms simultaneously and is frequently referenced in ECBA exam materials.

---

## Section 6 — Normalization in the BA Workflow

### 6.1 Inputs to Normalization

A BA typically begins normalization with these inputs:

- Stakeholder-provided spreadsheets or reports
- Screen captures of legacy system forms
- Data dictionaries from existing systems
- Interview notes describing business rules and data relationships

### 6.2 Deliverables

The outputs of a normalization exercise include:

- A list of functional dependencies
- A normalized logical data model (table definitions with keys)
- Documentation of decomposition decisions
- A data dictionary defining each attribute

### 6.3 Collaboration Points

Normalization decisions involve multiple stakeholders:

- **Subject matter experts** confirm functional dependencies
- **Database administrators** review the logical model for physical implementation feasibility
- **Developers** need the normalized schema to build data access layers
- **Project sponsors** may need to approve denormalization trade-offs

---

## Section 7 — Denormalization

### 7.1 Definition and Purpose

Denormalization is the intentional introduction of redundancy into a normalized design to achieve specific performance or usability goals. It is always a deliberate, documented decision.

### 7.2 When Denormalization Is Justified

Common business justifications for denormalization include:

- **Read performance:** Frequently queried reports run faster without multi-table joins.
- **Data warehousing:** OLAP systems and star schemas use intentional redundancy.
- **Historical accuracy:** Storing a snapshot value (e.g., price at time of sale) that must not change even if the source data changes.
- **Simplified application logic:** Some applications benefit from fewer joins at the cost of some redundancy.

### 7.3 Denormalization Risks

Denormalization introduces risks that must be managed:

- Update anomalies become possible again
- Application code must enforce consistency where the database structure no longer does
- Documentation must clearly describe which redundancies are intentional

### 7.4 BA Documentation Standard

When denormalization is approved, the BA documents:

1. Which normal form rule is being relaxed
2. The specific redundancy being introduced
3. The business justification
4. The risk mitigation approach (e.g., application-level enforcement)
5. Stakeholder sign-off

---

## Section 8 — ECBA Exam Focus Points

The following topics appear regularly in ECBA preparation materials related to data modeling:

- The definition and identification of functional dependencies
- The three normal forms and the specific rule each one addresses
- The difference between partial and transitive dependencies
- The business impact of data anomalies
- The trade-offs involved in denormalization decisions
- The relationship between normalization and requirements quality

Expect scenario-based questions where you must identify which normal form a table violates and describe the correct decomposition.

---

## Key Terms

| Term | Definition |
|---|---|
| Functional dependency | A → B: knowing A uniquely determines B |
| Determinant | The attribute on the left side of a functional dependency |
| Partial dependency | A non-key attribute depends on part, not all, of a composite key (2NF violation) |
| Transitive dependency | A non-key attribute is determined by another non-key attribute (3NF violation) |
| Decomposition | Splitting one table into two or more to remove a dependency violation |
| Referential integrity | Every foreign key value matches an existing primary key value |
| Denormalization | Deliberate introduction of redundancy for performance or usability |
| Atomic value | A single, indivisible data value in a cell |
| Composite key | A primary key composed of two or more attributes |
| Update anomaly | Inconsistency caused by updating redundant data in only some rows |

---

## Self-Check Questions

Answer these questions before attempting the quiz.

1. What three anomalies does normalization prevent?
2. Write the functional dependency notation for "CustomerID determines CustomerName."
3. A table has primary key (ProjectID, TaskID). TaskDescription depends only on TaskID. Which normal form is violated?
4. A table has EmployeeID as primary key. DeptName depends on DeptID, which depends on EmployeeID. Which normal form is violated?
5. Can a table with a single-column primary key violate 2NF? Explain why or why not.
6. Give one business scenario where denormalization is the correct decision.
7. What does the 3NF mnemonic mean in plain language?

---

## Reading Assignments

Complete all readings before the lab activity.

- BABOK Guide, Section 10.20: Data Modeling technique
- Course textbook: Chapter on logical data modeling and normalization
- Supplemental: Review any provided normalization worksheet from the course LMS

---

*Module 12 Reading Guide | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
