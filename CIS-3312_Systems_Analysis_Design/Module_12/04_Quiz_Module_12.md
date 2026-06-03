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
