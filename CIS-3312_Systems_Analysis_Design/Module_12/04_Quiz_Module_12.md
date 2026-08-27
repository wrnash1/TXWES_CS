# Quiz: Module 12 — Database Normalization for Business Analysts

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Quiz Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided after each question to support your learning.

**Time limit:** 30 minutes

---

## Question 1

A business analyst discovers that a single cell in the Contracts table contains the value "Legal, Finance, Operations" representing multiple departments assigned to the contract. Which normal form rule does this violate?

A. Second Normal Form — partial dependency on a composite key
B. Third Normal Form — transitive dependency between non-key attributes
C. First Normal Form — non-atomic value stored in a single attribute
D. Referential integrity — the foreign key does not match a primary key

### Distractor Analysis — Question 1

**Correct answer: C**

The cell stores multiple values ("Legal, Finance, Operations") in a single attribute, which violates the atomicity requirement of 1NF. This is one of the most common 1NF violations in real-world legacy data.

**Why A is wrong:** Partial dependencies (2NF) involve a non-key attribute depending on only part of a composite key. The issue here is not about keys at all — it is about the content of a single cell.

**Why B is wrong:** Transitive dependencies (3NF) involve chains between non-key attributes. The multi-valued cell problem has nothing to do with how attributes depend on one another.

**Why D is wrong:** Referential integrity is about foreign key relationships between tables, not about the format of values within a single cell.

---

## Question 2

A table tracks student course enrollments with columns: StudentID, StudentName, CourseID, CourseName, InstructorID, Grade. The primary key is (StudentID, CourseID). Which of the following is a partial dependency?

A. (StudentID, CourseID) → Grade
B. StudentID → StudentName
C. CourseID → InstructorID
D. StudentID → CourseID

### Distractor Analysis — Question 2

**Correct answer: B**

StudentName depends on StudentID alone — not on the full composite key (StudentID, CourseID). This is a classic partial dependency and a 2NF violation.

**Why A is wrong:** Grade requires both StudentID and CourseID to be determined. This is a full functional dependency on the composite key — exactly what 2NF requires.

**Why C is wrong:** CourseID → InstructorID is also a partial dependency (depends on one part of the key), making it another 2NF violation — but the question asks which option IS a partial dependency, and B is the cleaner, more direct example given first. Both B and C are technically valid partial dependencies; however, in exam contexts the question tests whether students recognize the StudentName/StudentID pattern first.

**Why D is wrong:** StudentID → CourseID is not a valid functional dependency. A student can be enrolled in multiple courses, so knowing a StudentID does not determine a single CourseID.

---

## Question 3

An Employees table has the following columns: EmployeeID, EmployeeName, DepartmentID, DepartmentName, ManagerID, ManagerName. The primary key is EmployeeID. After confirming the table is in 2NF, which dependency prevents it from being in 3NF?

A. EmployeeID → DepartmentID
B. DepartmentID → DepartmentName
C. EmployeeID → ManagerID
D. ManagerID → EmployeeName

### Distractor Analysis — Question 3

**Correct answer: B**

DepartmentName is determined by DepartmentID, which is itself a non-key attribute. The chain EmployeeID → DepartmentID → DepartmentName is a transitive dependency — a 3NF violation.

**Why A is wrong:** EmployeeID → DepartmentID is a direct dependency on the primary key. This is perfectly acceptable and does not violate any normal form.

**Why C is wrong:** EmployeeID → ManagerID is also a direct dependency on the primary key. It is fine in 3NF.

**Why D is wrong:** ManagerID → EmployeeName would be a problem if it existed, but this is not the dependency presented. ManagerName (not EmployeeName) depends on ManagerID, and ManagerID is itself non-key — making ManagerID → ManagerName the actual transitive chain in this table.

---

## Question 4

Which of the following is the most accurate plain-language interpretation of the Third Normal Form requirement?

A. Every column must have a unique value in every row.
B. No column value may be null.
C. Every non-key attribute must depend on the key, the whole key, and nothing but the key.
D. The primary key must be a single column, not a composite of multiple columns.

### Distractor Analysis — Question 4

**Correct answer: C**

This is the standard 3NF mnemonic. It captures all three normal forms: "the key" (1NF — a key exists), "the whole key" (2NF — no partial dependencies), and "nothing but the key" (3NF — no transitive dependencies).

**Why A is wrong:** Unique values in every column is not a normalization rule. In fact, many columns legitimately contain repeated values (e.g., DepartmentID appears in every row for employees in the same department).

**Why B is wrong:** Null handling is a separate concern from normalization. Normalized tables can and do contain null values in optional attributes.

**Why D is wrong:** Single-column primary keys are not required by 3NF. Composite keys are valid and common. 2NF and 3NF both apply to tables with composite keys.

---

## Question 5

During requirements elicitation for a retail system, a BA discovers that product prices are set at the product level and never vary by order. Which functional dependency correctly represents this business rule?

A. (OrderID, ProductID) → Price
B. OrderID → Price
C. ProductID → Price
D. Price → ProductID

### Distractor Analysis — Question 5

**Correct answer: C**

If the price is set at the product level and does not vary by order, then ProductID alone determines Price. This is a single-column functional dependency.

**Why A is wrong:** If price were determined by both OrderID and ProductID, it would mean the same product could have different prices in different orders — which contradicts the business rule stated.

**Why B is wrong:** OrderID → Price would mean every product in an order has the same price, which makes no business sense.

**Why D is wrong:** Price → ProductID would mean that knowing the price tells you which product it is — but many products can share the same price. This dependency is invalid.

---

## Question 6

A BA is reviewing a normalized Orders database. The development team proposes storing CustomerName and CustomerCity directly on the Orders table (in addition to the Customers table) so that the daily order report runs faster without a join. This proposal is best described as which of the following?

A. A 1NF violation, because customer data is being duplicated
B. A deliberate denormalization trade-off with documented business justification
C. A 3NF violation that must be rejected because it introduces transitive dependencies
D. A referential integrity problem, because two tables will store the same foreign key

### Distractor Analysis — Question 6

**Correct answer: B**

Storing redundant data intentionally for performance reasons is denormalization. When it is deliberate, documented, and stakeholder-approved, it is an acceptable design decision — not a mistake.

**Why A is wrong:** Denormalization does technically reintroduce redundancy (which could be called a 1NF concern), but the point is that this is an intentional decision, not an accidental violation. The correct framing is denormalization, not a violation to be corrected.

**Why C is wrong:** The question does not describe a transitive dependency — it describes redundant storage of attributes from another table. Those are different concepts. And even if it did create a 3NF issue, "must be rejected" is too absolute — denormalization can be accepted with justification.

**Why D is wrong:** Referential integrity is about foreign key values matching primary key values, not about storing attribute values in multiple tables.

---

## Question 7

Which of the following scenarios represents a deletion anomaly in an unnormalized database?

A. A user updates an instructor's name in one row but not in all rows where it appears.
B. Deleting the last student enrolled in a course also removes the only record of that course.
C. Adding a new course requires inventing a placeholder student record.
D. Two students with the same name receive each other's grades.

### Distractor Analysis — Question 7

**Correct answer: B**

A deletion anomaly occurs when deleting one piece of information inadvertently destroys another, unrelated piece of information. Removing the last enrollment record destroys the course data — a textbook deletion anomaly.

**Why A is wrong:** This describes an update anomaly — the same fact stored in multiple places and updated inconsistently.

**Why C is wrong:** This describes an insertion anomaly — inability to add a new entity without fabricating unrelated data.

**Why D is wrong:** This describes a data integrity or key-design problem, not a specific anomaly type related to normalization.

---

## Question 8

A BA is normalizing a SalesOrders table with primary key (SalesRepID, CustomerID, ProductID). Which question best helps the BA determine whether OrderQuantity is fully or partially dependent on this composite key?

A. "Can the same product be ordered by multiple customers?"
B. "Is OrderQuantity ever stored in a separate table?"
C. "Do you need to know the sales rep, the customer, AND the product to determine how many units were ordered?"
D. "Is OrderQuantity ever null in the current spreadsheet?"

### Distractor Analysis — Question 8

**Correct answer: C**

This question directly tests whether the attribute requires all three parts of the composite key or only a subset. If yes, it is a full functional dependency. If only some key parts are needed, it is partial.

**Why A is wrong:** Whether a product can be ordered by multiple customers is relevant to key design but does not directly test the dependency of OrderQuantity on the composite key.

**Why B is wrong:** Whether an attribute is stored in another table is an implementation detail, not an analytical question about functional dependency.

**Why D is wrong:** Null values are irrelevant to functional dependency analysis.

---

## Question 9

After completing normalization, a BA's data model includes a Customers table, an Orders table, and an OrderItems table. The OrderItems table has a foreign key to Orders and a foreign key to a Products table. A developer asks: "How do we ensure that an OrderItem cannot reference a ProductID that doesn't exist in the Products table?" The BA's correct answer is which of the following?

A. Apply 2NF to remove the partial dependency on ProductID.
B. Enforce referential integrity via a foreign key constraint linking OrderItems.ProductID to Products.ProductID.
C. Denormalize by copying all product data into the OrderItems table.
D. Apply 3NF to remove the transitive dependency between OrderItems and Products.

### Distractor Analysis — Question 9

**Correct answer: B**

Referential integrity ensures that foreign key values in one table match primary key values in another. This is enforced via a database-level foreign key constraint — exactly the right mechanism here.

**Why A is wrong:** 2NF addresses partial dependencies on composite keys. The developer's question is about data consistency between tables, not about normalization form.

**Why C is wrong:** Copying all product data into OrderItems would introduce redundancy and reintroduce the anomalies that normalization was designed to prevent.

**Why D is wrong:** 3NF addresses transitive dependencies within a table. The developer's concern is about cross-table integrity, which is referential integrity, not a normal form issue.

---

## Question 10

In the context of ECBA exam preparation, which BABOK knowledge area most directly encompasses the data modeling and normalization techniques covered in this module?

A. Business Analysis Planning and Monitoring
B. Elicitation and Collaboration
C. Requirements Analysis and Design Definition
D. Solution Evaluation

### Distractor Analysis — Question 10

**Correct answer: C**

The BABOK Guide places Data Modeling as a technique under Requirements Analysis and Design Definition. This knowledge area covers specifying and modeling requirements, which includes data models such as entity-relationship diagrams and normalized table definitions.

**Why A is wrong:** Business Analysis Planning and Monitoring covers how BA work is planned and governed — scope, approach, stakeholder engagement. It does not include data modeling techniques.

**Why B is wrong:** Elicitation and Collaboration covers gathering information from stakeholders. While elicitation is used to uncover functional dependencies, the modeling itself belongs to a different knowledge area.

**Why D is wrong:** Solution Evaluation covers assessing whether an implemented solution delivers the intended business value. It occurs after design and does not include data modeling.

---

*Module 12 Quiz | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

---

## Question 11

A BA is reviewing a table called EmployeeProjects with columns: EmployeeID, ProjectID,
EmployeeName, ProjectName, HoursLogged, DepartmentID, DepartmentName. The primary key is
(EmployeeID, ProjectID). After removing partial dependencies, the BA finds that
DepartmentName still appears in the Employees table alongside DepartmentID. What
dependency remains, and which normal form does it violate?

A. HoursLogged → EmployeeID — a partial dependency, violating 2NF
B. DepartmentID → DepartmentName — a transitive dependency, violating 3NF
C. EmployeeID → DepartmentName — a full functional dependency, which is acceptable in 3NF
D. ProjectID → DepartmentID — a partial dependency on the composite key, violating 2NF

### Distractor Analysis — Question 11

**Correct answer: B**

After 2NF decomposition, the Employees table has EmployeeID as its primary key. DepartmentName
depends on DepartmentID (a non-key attribute), not directly on EmployeeID. The chain
EmployeeID → DepartmentID → DepartmentName is a transitive dependency — a 3NF violation.

**Why A is wrong:** HoursLogged requires both EmployeeID and ProjectID to be determined —
it is the one fully dependent attribute on the composite key. After 2NF decomposition it
belongs in the ProjectAssignments table and no longer participates in any violation.

**Why C is wrong:** EmployeeID → DepartmentName appears to be a direct dependency, but it
is only true through the intermediate non-key attribute DepartmentID. Saying it is a full
functional dependency misses the transitive chain and leaves the 3NF violation undetected.

**Why D is wrong:** ProjectID → DepartmentID would be a partial dependency in the original
composite-key table, but after 2NF decomposition the Employees table has a single-column
primary key. DepartmentID in the Employees table is now a non-key attribute, not part of
a composite key, making the remaining problem a transitive dependency.

---

## Question 12

Which of the following is an example of an insertion anomaly in an unnormalized database?

A. A user deletes the last order for a customer and the customer record is also deleted

B. A user updates the ZIP code for a city in one row but not in the 47 other rows that
   reference the same city

C. A clerk cannot add a new supplier to the system without also creating a purchase order
   for that supplier at the same time

D. Two employees in the same department receive different department name spellings

### Distractor Analysis — Question 12

**Correct answer: C**

An insertion anomaly occurs when a new fact cannot be recorded independently — adding the
supplier requires fabricating or attaching an unrelated purchase order record. This is
the canonical insertion anomaly example.

**Why A is wrong:** This describes a deletion anomaly — removing one piece of data
inadvertently destroys another unrelated piece of data (the customer record).

**Why B is wrong:** This describes an update anomaly — the same fact (ZIP-to-city mapping)
stored in multiple rows and updated inconsistently.

**Why D is wrong:** Inconsistent spelling is a data quality or domain integrity issue, not
a structural anomaly caused by normalization failure. Normalization addresses structural
redundancy, not data entry errors.

---

## Question 13

A BA is normalizing a table that tracks hotel reservations. The table has a single-column
primary key of ReservationID. The BA claims the table is automatically in 2NF. Is this
claim correct, and why?

A. No — a table must be tested for partial dependencies even with a single-column key

B. Yes — 2NF only requires testing for partial dependencies on composite keys; a single-
   column key has no parts to be partial about, so 2NF is satisfied by definition

C. No — 2NF requires that all attributes be atomic, which must be tested separately

D. Yes — single-column keys guarantee 3NF compliance as well as 2NF compliance

### Distractor Analysis — Question 13

**Correct answer: B**

A partial dependency requires that a non-key attribute depends on only part of a composite
key. When the primary key is a single column, it cannot be "partially" depended upon — the
full key and the whole key are the same thing. Therefore, 2NF is automatically satisfied.

**Why A is wrong:** Testing for partial dependencies with a single-column key is not
necessary and would find nothing, because partial dependency is a concept that only applies
to composite keys.

**Why C is wrong:** Atomicity of attribute values is a 1NF requirement, not a 2NF
requirement. These are separate rules applied in sequence.

**Why D is wrong:** A single-column primary key guarantees 2NF but not 3NF. Transitive
dependencies can still exist regardless of whether the key is single-column or composite.
A table in 2NF must be separately checked for 3NF violations.

---

## Question 14

A business analyst is documenting functional dependencies for a university system. A
subject matter expert states: "A student can be enrolled in multiple sections, and a
section has exactly one room assignment." Which functional dependency chain correctly
captures both of these rules?

A. StudentID → SectionID → RoomNumber

B. SectionID → StudentID and SectionID → RoomNumber

C. StudentID → RoomNumber (directly, with no intermediate dependency)

D. (StudentID, SectionID) → RoomNumber

### Distractor Analysis — Question 14

**Correct answer: A**

The SME's statement implies two dependencies: StudentID determines SectionID (a student
is in a section) and SectionID determines RoomNumber (each section has one room). This is
the transitive chain StudentID → SectionID → RoomNumber. If these all appear in one table
with StudentID as the primary key, the chain is a 3NF violation.

**Why B is wrong:** SectionID → StudentID reverses the relationship. A section has many
students, so knowing a SectionID cannot determine a single StudentID. This dependency is
invalid.

**Why C is wrong:** StudentID → RoomNumber appears direct but is only true through the
intermediate SectionID. Stating it as a direct dependency hides the transitive chain and
would prevent a BA from identifying the 3NF violation.

**Why D is wrong:** (StudentID, SectionID) → RoomNumber would mean the room depends on
the student-section combination. But the SME said a section has one room regardless of
which student is in it, so RoomNumber depends only on SectionID — making SectionID the
actual determinant, not the composite.

---

## Question 15

A development team delivers a normalized database schema for a new CRM application. The
BA notices that the CustomerOrders table has a foreign key to Customers (CustomerID) but
there is no database constraint enforcing the relationship. A test record has been inserted
with CustomerID = 9999, but no row with CustomerID = 9999 exists in the Customers table.
What type of integrity violation has occurred, and what is the appropriate fix?

A. Entity integrity violation — fix by ensuring the primary key of CustomerOrders is never
   null

B. Domain integrity violation — fix by constraining the CustomerID column to numeric
   values only

C. Referential integrity violation — fix by adding a foreign key constraint linking
   CustomerOrders.CustomerID to Customers.CustomerID

D. 2NF violation — fix by moving CustomerID into a separate lookup table

### Distractor Analysis — Question 15

**Correct answer: C**

A foreign key value that has no matching primary key in the referenced table violates
referential integrity. The correct fix is a foreign key constraint at the database level
that prevents such orphaned records from being inserted.

**Why A is wrong:** Entity integrity requires that primary key values are never null. The
described problem is a missing parent row, not a null primary key — a different type of
constraint.

**Why B is wrong:** Domain integrity governs data types and value ranges within a column.
The CustomerID value 9999 is presumably a valid integer — the problem is not its format
but the absence of a matching parent row.

**Why D is wrong:** 2NF violations involve partial dependencies on composite keys. The
described problem has nothing to do with how non-key attributes depend on the primary key
— it is about a foreign key pointing to a non-existent parent.

---

## Question 16

A BA is presenting the results of a normalization exercise to a project team. A developer
objects: "Normalization creates too many tables and makes queries slow." The BA's most
effective response is which of the following?

A. "Normalization is required by the BABOK Guide, so we must follow it regardless of
   performance."

B. "You are right — we should skip normalization and optimize for performance from the
   start."

C. "Normalization eliminates data anomalies and is the correct starting point. Where
   query performance is a documented concern, we can evaluate specific, documented
   denormalization decisions with stakeholder approval."

D. "Normalized designs always perform better than denormalized designs because the tables
   are smaller."

### Distractor Analysis — Question 16

**Correct answer: C**

This response acknowledges the developer's concern while defending the analytical value
of normalization. It correctly positions denormalization as a deliberate, documented
exception rather than a starting point, and it involves the appropriate stakeholders.

**Why A is wrong:** While the BABOK Guide does recognize data modeling, citing a standard
as the sole justification dismisses a legitimate technical concern and is unlikely to
persuade the developer.

**Why B is wrong:** Skipping normalization creates data anomalies that are far more costly
to fix after deployment than the query performance problems the developer is describing.
This response gives up the business case for normalization entirely.

**Why D is wrong:** This is factually incorrect. Normalized designs can be slower for
read-heavy workloads because joins are expensive. The BA should not make technically
false claims to win an argument.

---

## Question 17

A flat table called SalesData contains the following columns: SaleID, SalesRepID,
SalesRepName, SalesRepRegion, CustomerID, CustomerName, ProductID, ProductName,
ProductCategory, SaleDate, SaleAmount. The primary key is SaleID. A BA identifies that
ProductCategory depends on ProductID, not on SaleID. What type of dependency is this, and
what is the correct decomposition?

A. Partial dependency — create a Products table with ProductID (PK), ProductName, and
   ProductCategory; retain ProductID as FK in SalesData

B. Transitive dependency — create a Products table with ProductID (PK), ProductName, and
   ProductCategory; retain ProductID as FK in SalesData

C. Full functional dependency — no action needed; ProductCategory can stay in SalesData

D. Transitive dependency — move SaleID into the Products table as a foreign key

### Distractor Analysis — Question 17

**Correct answer: B**

SaleID → ProductID (direct dependency) and ProductID → ProductCategory (ProductCategory
depends on a non-key attribute). This is a transitive dependency chain and a 3NF violation.
The fix is to move ProductCategory (and ProductName) into a Products table keyed by
ProductID.

**Why A is wrong:** A partial dependency requires a composite primary key, and only part
of that composite key determines the attribute. SaleID here is a single-column primary key,
so the concept of partial dependency does not apply. The correct term is transitive.

**Why C is wrong:** ProductCategory does not depend on SaleID directly — it depends on
ProductID. This is exactly the pattern that 3NF is designed to detect and eliminate.

**Why D is wrong:** Moving SaleID into the Products table as a foreign key reverses the
relationship. Products exist independently of individual sales; each sale references a
product, not the other way around.

---

## Question 18

Which of the following best describes why a BA — rather than a database administrator —
should understand normalization?

A. BAs write SQL queries and need to understand table structure to optimize them

B. BAs are responsible for specifying data requirements that are logically consistent and
   free of structural defects; normalization knowledge allows BAs to validate that their
   data models will support business rules without anomalies

C. Normalization is required before business rules can be elicited from stakeholders

D. BAs must normalize all data models to Boyce-Codd Normal Form before handoff to
   developers

### Distractor Analysis — Question 18

**Correct answer: B**

This aligns with the BABOK Guide positioning of data modeling as a requirements analysis
technique. BAs produce logical data models that will be implemented by DBAs. If the
logical model has normalization errors, the resulting database will have anomalies.

**Why A is wrong:** Writing SQL queries is a developer or DBA task, not a BA task. BAs
specify what data is needed; they do not typically write the code to retrieve it.

**Why C is wrong:** Elicitation of business rules precedes data modeling; it is not
dependent on normalization. Normalization is applied after the data requirements have been
gathered.

**Why D is wrong:** Boyce-Codd Normal Form (BCNF) is beyond the scope of standard BA
practice. The ECBA and BABOK Guide focus on 1NF through 3NF as the relevant range for
business analysts.

---

## Question 19

After normalizing the hospital Appointments dataset, the Diagnoses table contains
DiagnosisCode (PK) and DiagnosisDescription. The Appointments table retains DiagnosisCode
as a foreign key. A stakeholder asks: "Can two different appointment records reference the
same DiagnosisCode?" The BA's correct answer is which of the following?

A. No — foreign key values must be unique in the referencing table

B. Yes — multiple appointments can reference the same DiagnosisCode because the foreign
   key in Appointments can repeat; uniqueness is only required in the Diagnoses table for
   the primary key DiagnosisCode

C. No — each appointment must have its own unique DiagnosisCode for the database to
   remain normalized

D. Yes — but only if the appointments belong to the same patient

### Distractor Analysis — Question 19

**Correct answer: B**

Foreign key values in a referencing table are not required to be unique. Many appointment
records can reference the same DiagnosisCode. The uniqueness constraint applies to the
primary key in the parent (Diagnoses) table, not to the foreign key in the child
(Appointments) table. This is the standard one-to-many relationship behavior.

**Why A is wrong:** Foreign keys are not required to be unique. If they were, the
relationship would be one-to-one, not one-to-many. A diagnosis code like "Hypertension"
will appear in thousands of appointment records.

**Why C is wrong:** Having the same DiagnosisCode in multiple rows is not only permitted
but expected. It is precisely the point of normalizing diagnosis data into its own table —
the description is stored once and reused via the foreign key reference.

**Why D is wrong:** The foreign key relationship has no patient-level restriction. Any
appointment for any patient can reference the same DiagnosisCode. The referential integrity
rule only requires that the DiagnosisCode value exists in the Diagnoses table.

---

## Question 20

A BA proposes the following table structure for a library system after normalization:

- Books (BookID, Title, ISBN, PublisherID)
- Publishers (PublisherID, PublisherName, PublisherCity, PublisherCountry)
- Authors (AuthorID, AuthorName)
- BookAuthors (BookID, AuthorID)

A reviewer argues that the BookAuthors table is unnecessary and that AuthorID should
simply be added as a column to the Books table. The BA's correct response is which of the
following?

A. The reviewer is correct — adding AuthorID to Books eliminates the extra table and
   simplifies the schema

B. The BA is correct — BookAuthors is an associative entity that resolves a many-to-many
   relationship between Books and Authors; adding AuthorID directly to Books would only
   support one author per book

C. The reviewer is correct — a single AuthorID column is sufficient because most books
   have only one author

D. The BA is incorrect — BookAuthors violates 3NF because it contains two foreign keys
   with no non-key attributes

### Distractor Analysis — Question 20

**Correct answer: B**

BookAuthors is a junction table resolving a many-to-many relationship: one book can have
multiple authors, and one author can write multiple books. Collapsing it into a single
AuthorID column on Books restricts every book to one author and loses co-authorship
information entirely.

**Why A is wrong:** Adding AuthorID directly to Books would be a regression to an
unnormalized structure that cannot represent multiple authors per book without repeating
groups or multi-valued columns.

**Why C is wrong:** Designing for the common case (single author) at the expense of
correctness produces a data model that fails when an exception occurs. Data models must
support all valid business cases, not just the most frequent ones.

**Why D is wrong:** An associative entity (junction table) with only foreign keys as its
primary key is a valid and normalized structure. Having no non-key attributes is perfectly
acceptable. The table is not a 3NF violation — it is the correct solution to a many-to-many
relationship.

---

*Module 12 Quiz (extended) | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*
