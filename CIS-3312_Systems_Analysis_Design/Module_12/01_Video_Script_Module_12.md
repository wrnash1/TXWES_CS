# Video Script: Module 12 — Database Normalization for Business Analysts

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Production Notes

- **Runtime Target:** 20–24 minutes
- **Format:** Lecture with whiteboard diagrams and table examples
- **Slides:** Approximately 28 slides

---

## SEGMENT 1 — Introduction and Context (0:00–2:30)

[OPEN on slide: "Module 12 — Database Normalization for Business Analysts"]

Welcome back to CIS-3312. I'm Professor Nash, and in Module 12 we are diving into database normalization — one of those foundational skills that separates a competent business analyst from a great one.

Now, I hear you already. "Professor Nash, I'm a BA, not a database administrator. Why do I need to know normalization?" Fair question.

Here is the honest answer: when you gather requirements for a new system, you will almost always be describing data. What data is collected, where it lives, how it relates to other data. If you do not understand how well-structured data looks, you will accept designs that cause real problems later — duplicate records, update anomalies, reports that give wrong answers.

The IIBA ECBA body of knowledge explicitly recognizes data modeling as a core BA technique. Normalization is how you make sure a data model actually works.

So today's goals are clear. By the end of this module you will be able to explain functional dependencies, walk a table through first, second, and third normal form, recognize when normalization is complete, and explain to a stakeholder why denormalization is sometimes the right business decision.

Let's go.

---

## SEGMENT 2 — What Is Normalization? (2:30–5:00)

[SLIDE: "The Problem Normalization Solves"]

Imagine you are building a system for a university. Someone hands you a spreadsheet. Every row represents a student enrolled in a course.

The columns are: StudentID, StudentName, StudentEmail, CourseID, CourseName, InstructorID, InstructorName, Grade.

Looks fine at first glance. But watch what happens when data changes.

[WHITEBOARD: Draw simple flat table with 4 rows showing same InstructorName repeated]

If Instructor Johnson changes departments and you need to update their name, you must update every single row where Johnson appears. Miss one row and now you have data that contradicts itself. This is called an **update anomaly**.

If you delete the last student enrolled in a course, you lose the course record entirely. That is a **deletion anomaly**.

If you cannot add a new instructor until they teach at least one course, that is an **insertion anomaly**.

Normalization is the systematic process of decomposing tables to eliminate these anomalies. It works by removing data redundancy — storing each piece of information in exactly one place.

Edgar Codd, the mathematician who invented the relational model, defined normal forms in the 1970s. We still use his framework today.

---

## SEGMENT 3 — Functional Dependencies (5:00–8:30)

[SLIDE: "Functional Dependencies — The Foundation"]

Before we can normalize, we need to understand functional dependencies. This is the analytical work a BA actually does.

A **functional dependency** exists when one attribute uniquely determines another. We write it with an arrow.

StudentID → StudentName

This means: if I know the StudentID, I can determine exactly one StudentName. The StudentID is the **determinant**. StudentName is the **dependent**.

[WHITEBOARD: Write notation clearly]

Let's be precise. This does NOT mean a student can only have one name at a time. It means that for any given StudentID, there is exactly one corresponding StudentName in the table.

Now consider this: CourseID → CourseName. Fine. One course, one name.

But what about Grade? Grade depends on BOTH StudentID AND CourseID together. Neither alone determines the grade. This is a **composite key dependency**.

We write it: (StudentID, CourseID) → Grade

When you are doing requirements work, you identify functional dependencies by asking stakeholders: "Given this piece of information, can you always tell me exactly what this other piece of information is?" If yes, you have a functional dependency.

A few more examples from business:

- OrderID → OrderDate — yes, one order has one date
- ProductID → ProductPrice — yes, assuming price is set at product level
- (OrderID, ProductID) → Quantity — yes, you need both to know how many were ordered

This analytical step is where a BA's interviewing and modeling skills matter most. You are discovering business rules, not just drawing tables.

---

## SEGMENT 4 — First Normal Form (8:30–11:30)

[SLIDE: "1NF — Atomic Values and No Repeating Groups"]

First Normal Form has two requirements.

**Requirement 1:** Every attribute must contain atomic values — no lists, no sets, no nested tables.

**Requirement 2:** There are no repeating groups — no columns like Phone1, Phone2, Phone3.

[SLIDE: Show unnormalized table with PhoneNumbers as comma-separated list]

Here is an unnormalized table:

| CustomerID | CustomerName | PhoneNumbers |
|---|---|---|
| 101 | Acme Corp | 555-1000, 555-1001 |
| 102 | Globex | 555-2000 |

PhoneNumbers stores multiple values in one cell. That violates 1NF.

To fix it, we create a separate row for each phone number:

| CustomerID | CustomerName | PhoneNumber |
|---|---|---|
| 101 | Acme Corp | 555-1000 |
| 101 | Acme Corp | 555-1001 |
| 102 | Globex | 555-2000 |

Now every cell has one value. We are in 1NF.

Notice the trade-off: CustomerName now appears twice for CustomerID 101. That redundancy is exactly what higher normal forms will address.

The primary key question: what uniquely identifies each row? For this table, it is (CustomerID, PhoneNumber) together.

A common 1NF mistake students make: using column names like ProductA, ProductB, ProductC instead of a separate Products table. Every time you see numbered columns, that is a signal the data model is not even in 1NF.

---

## SEGMENT 5 — Second Normal Form (11:30–14:30)

[SLIDE: "2NF — Eliminate Partial Dependencies"]

Second Normal Form requires:

1. The table is already in 1NF.
2. Every non-key attribute is **fully functionally dependent** on the entire primary key.

A **partial dependency** occurs when a non-key attribute depends on only part of a composite key.

[WHITEBOARD: Draw OrderItems table]

Let's look at an OrderItems table:

| OrderID | ProductID | Quantity | ProductName | ProductPrice |
|---|---|---|---|---|

Primary key: (OrderID, ProductID)

Quantity depends on both — you need both OrderID and ProductID to know the quantity ordered. That is a full dependency. Good.

But ProductName depends only on ProductID. You do not need OrderID to know what a product is called. That is a **partial dependency** — a 2NF violation.

Same with ProductPrice — it depends only on ProductID.

To fix this, we decompose into two tables:

**OrderItems:** (OrderID, ProductID, Quantity)

**Products:** (ProductID, ProductName, ProductPrice)

Now OrderItems is in 2NF. Every non-key attribute depends on the full composite key.

Important note: if your table has a single-column primary key — not composite — it is automatically in 2NF. Partial dependencies can only exist with composite keys.

As a BA, when you see a table with a composite key and attributes that belong to only one of the key columns, that is a partial dependency. Ask yourself: "Could I move this attribute to its own table with just that key part?"

---

## SEGMENT 6 — Third Normal Form (14:30–17:30)

[SLIDE: "3NF — Eliminate Transitive Dependencies"]

Third Normal Form requires:

1. The table is already in 2NF.
2. No non-key attribute determines another non-key attribute.

A **transitive dependency** exists when: Key → AttributeA → AttributeB. AttributeB depends on the key indirectly, through another non-key attribute.

[WHITEBOARD: Draw Employees table]

Consider this Employees table:

| EmployeeID | EmployeeName | DepartmentID | DepartmentName | DepartmentBudget |
|---|---|---|---|---|

Primary key: EmployeeID

EmployeeID → DepartmentID is fine.

But DepartmentName is determined by DepartmentID, not directly by EmployeeID. The chain is:

EmployeeID → DepartmentID → DepartmentName

That middle step — DepartmentID determines DepartmentName — is the transitive dependency.

Fix it by decomposing:

**Employees:** (EmployeeID, EmployeeName, DepartmentID)

**Departments:** (DepartmentID, DepartmentName, DepartmentBudget)

Now Employees is in 3NF. Every non-key attribute describes the key, the whole key, and nothing but the key.

That last phrase — "the key, the whole key, and nothing but the key" — is the classic 3NF mnemonic. Write it down.

For most business systems, reaching 3NF is the target. Beyond 3NF exists Boyce-Codd Normal Form and 4NF, which address more exotic dependency issues. In practice, ECBA-level BA work focuses on 1NF through 3NF.

---

## SEGMENT 7 — Normalization Process in Practice (17:30–20:00)

[SLIDE: "Normalization Workflow for Business Analysts"]

Here is the practical workflow you will use on real projects.

**Step 1:** Gather the raw data. Spreadsheets from stakeholders, existing reports, screenshots of legacy systems.

**Step 2:** Identify all attributes. What data is being captured?

**Step 3:** Identify functional dependencies. Interview stakeholders. Ask "what uniquely identifies X?" for every entity.

**Step 4:** Define candidate keys. Which attributes or combinations could serve as the primary key?

**Step 5:** Apply 1NF. Eliminate non-atomic values and repeating groups.

**Step 6:** Apply 2NF. Remove partial dependencies by splitting tables.

**Step 7:** Apply 3NF. Remove transitive dependencies by splitting further.

**Step 8:** Verify referential integrity. Every foreign key points to a valid primary key.

The result is a normalized data model that becomes the foundation for your system's physical database design. Your development partners will thank you for doing this work thoroughly.

---

## SEGMENT 8 — When to Denormalize (20:00–22:30)

[SLIDE: "Denormalization — A Deliberate Business Decision"]

Here is where business analysis meets data architecture. Normalization is the default goal — but it is not always the final answer.

**Denormalization** is the deliberate introduction of redundancy to improve read performance. We do this when the cost of joining tables exceeds the benefit of eliminating redundancy.

Common denormalization scenarios include the following.

**Reporting and analytics databases.** A data warehouse intentionally stores pre-aggregated, redundant data because analysts run millions of queries and need fast reads.

**High-volume transactional reads.** If a web page displays a product with its category name and supplier name, joining three tables on every page load might be too slow. Storing CategoryName on the Products table avoids that join.

**Historical snapshots.** An invoice should store the price at the time of sale, even if the current price changes later. That stored price is intentional denormalization — it preserves historical accuracy.

As a BA, you never make the denormalization decision alone. You document the trade-off: here is the redundancy we are accepting, here is the anomaly risk, and here is the business justification. Stakeholders sign off on the decision explicitly.

---

## SEGMENT 9 — Module Wrap-Up (22:30–24:00)

[SLIDE: "Module 12 Summary"]

Let's close with the key takeaways.

Normalization is a systematic process for eliminating data anomalies by identifying and removing problematic functional dependencies.

First Normal Form: atomic values, no repeating groups.

Second Normal Form: no partial dependencies on a composite key.

Third Normal Form: no transitive dependencies between non-key attributes.

The practical mnemonic: "the key, the whole key, and nothing but the key."

Denormalization is sometimes right — but it is always a documented, stakeholder-approved decision, never an accident.

For your ECBA preparation, expect questions on functional dependencies, normal forms, and the business reasons for both normalization and denormalization.

Complete the reading guide, the lab exercise, and the quiz before our next module. Module 13 covers solution design and prototyping — where all this clean data structure gets a user interface.

See you there.

[END]

---

*Total runtime estimate: 22–24 minutes*
