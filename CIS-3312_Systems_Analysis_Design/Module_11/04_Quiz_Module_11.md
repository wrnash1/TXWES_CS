# Quiz: Module 11 - Database Design and Normalization
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
A database table named `StudentCourses` stores: StudentID, StudentName, CourseID, CourseName, InstructorName, InstructorOffice. The primary key is StudentID + CourseID. A database administrator points out that InstructorOffice depends only on InstructorName, not on the full primary key. Which normal form does this violate?
*   A) First Normal Form (1NF) — because there is a repeating group of course information
*   B) Second Normal Form (2NF) — because InstructorOffice depends on only part of the composite key
*   C) Third Normal Form (3NF) — because InstructorOffice depends on InstructorName, which is a non-key attribute
*   D) The table is fully normalized — there are no violations in this structure
*   **Correct Answer:** C) Third Normal Form (3NF) — because InstructorOffice depends on InstructorName, which is a non-key attribute
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 1NF concerns atomic values and repeating groups; no multi-valued column is described. The table appears to be in 1NF.
    *   *Why B is incorrect:* 2NF concerns partial dependence on part of a composite key. InstructorOffice depends on InstructorName, which is itself a non-key attribute — this is a transitive dependency, not a partial key dependency.
    *   *Why D is incorrect:* The transitive dependency (InstructorOffice → via InstructorName, not directly on the key) is a clear 3NF violation.
    *   *Why C is correct:* 3NF is violated when a non-key attribute determines another non-key attribute (transitive dependency). Here, InstructorOffice → InstructorName → (not the primary key). The fix is to create a separate Instructor table.

---

**Question 2**
In database design, which of the following is the most accurate definition of **referential integrity**?
*   A) The rule that every table in a relational database must have a primary key that uniquely identifies each row
*   B) The guarantee that a foreign key value in one table always corresponds to an existing primary key value in the referenced table
*   C) The process of converting a flat, unnormalized data structure into a series of related tables to eliminate redundancy
*   D) The property of a database transaction that ensures all operations either complete successfully or are fully rolled back
*   **Correct Answer:** B) The guarantee that a foreign key value in one table always corresponds to an existing primary key value in the referenced table
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Requiring primary keys in every table is a relational database design rule, but it is not the definition of referential integrity specifically.
    *   *Why C is incorrect:* Converting flat structures to normalized tables describes the normalization process, not referential integrity.
    *   *Why D is incorrect:* Ensuring complete or rollback behavior describes ACID transaction atomicity, not referential integrity.
    *   *Why B is correct:* Referential integrity ensures that no orphan records exist — every foreign key value must match a real row in the parent table, preventing data inconsistency across related tables.

---

**Question 3**
A legacy database table for employee data contains a column called `PhoneNumbers` that stores values like "555-1234, 555-5678, 555-9999" — multiple phone numbers in a single comma-separated field. Which normal form does this violate?
*   A) Third Normal Form (3NF) — because the phone numbers depend on a non-key attribute
*   B) Second Normal Form (2NF) — because the phone numbers only partially depend on the composite primary key
*   C) First Normal Form (1NF) — because the column contains non-atomic, multi-valued data
*   D) The table does not violate any normal form — storing delimited lists is an accepted relational practice
*   **Correct Answer:** C) First Normal Form (1NF) — because the column contains non-atomic, multi-valued data
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 3NF concerns transitive dependencies between non-key attributes; the issue here is a multi-valued single column, which is a 1NF problem.
    *   *Why B is incorrect:* 2NF concerns partial key dependencies in tables with composite keys; the issue here is atomic value violation, which is 1NF.
    *   *Why D is incorrect:* Storing delimited lists in a single column is explicitly prohibited by 1NF; it is not an accepted relational practice and causes serious query and maintenance problems.
    *   *Why C is correct:* 1NF requires that every column contain atomic (indivisible) values. A comma-separated list of phone numbers in a single column is a multi-valued attribute that violates 1NF; the fix is to create a separate EmployeePhones table.

---

**Question 4**
A developer proposes denormalizing a frequently queried reports table by storing redundant customer name and address data alongside each order record, rather than joining to a separate Customers table at query time. What is the primary trade-off the BA should document?
*   A) Denormalization reduces database file size, while normalization increases it proportionally
*   B) Denormalization improves read query performance by reducing JOINs, but increases the risk of data inconsistency if customer data changes
*   C) Denormalization makes the database non-relational and prevents the use of SQL queries on the affected tables
*   D) Denormalization violates the primary key uniqueness rule and requires table restructuring to maintain referential integrity
*   **Correct Answer:** B) Denormalization improves read query performance by reducing JOINs, but increases the risk of data inconsistency if customer data changes
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Denormalization generally increases storage size (due to redundant data), not decreases it; this is not the primary trade-off.
    *   *Why C is incorrect:* Denormalized relational tables are still relational and fully support SQL queries; denormalization does not change the database paradigm.
    *   *Why D is incorrect:* Storing redundant data does not inherently violate primary key uniqueness or referential integrity rules; it is a design choice, not a constraint violation.
    *   *Why B is correct:* The classic normalization/denormalization trade-off is: denormalized = faster reads but update anomaly risk (if a customer changes their address, every order row must be updated); normalized = slower reads (JOIN needed) but single source of truth (only one place to update).

---

**Question 5**
A new database table for online orders has the following columns: OrderID (PK), CustomerID (FK), CustomerEmail, ProductID (FK), ProductName, Quantity, OrderDate. A senior DBA notes that ProductName depends on ProductID, not on the OrderID primary key. Which normalization fix resolves this issue?
*   A) Add a NOT NULL constraint to the ProductName column to prevent missing product names on order records
*   B) Create a separate Products table with ProductID as the primary key and ProductName as an attribute, then remove ProductName from the Orders table
*   C) Change the primary key to a composite key of OrderID + ProductID to fully capture the product dependency
*   D) Store ProductName as a JSON object inside a single column to accommodate future product attribute additions
*   **Correct Answer:** B) Create a separate Products table with ProductID as the primary key and ProductName as an attribute, then remove ProductName from the Orders table
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A NOT NULL constraint enforces data presence but does not eliminate the functional dependency violation — ProductName still inappropriately resides in the Orders table.
    *   *Why C is incorrect:* Changing the primary key to a composite does not resolve the partial dependency; it would introduce a different 2NF structure without addressing the root cause.
    *   *Why D is incorrect:* Storing ProductName as JSON embeds multiple normalization violations and is the opposite of normalization best practice.
    *   *Why B is correct:* The dependency ProductName → ProductID (not OrderID) means ProductName belongs in a Products table, not in Orders. Removing it from Orders and referencing it through the existing ProductID foreign key eliminates the transitive dependency and brings the table to 3NF.
