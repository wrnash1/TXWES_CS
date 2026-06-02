# Quiz: Module 02 — Database Design: Normalization and ERDs

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided to reinforce exam-level reasoning.

---

### Question 1

A table named `order_lines` has a composite primary key of (order_id, product_id) and the following columns: quantity, unit_price, product_name, product_category. Which normal form does this table violate, and why?

- A) Second Normal Form, because product_name and product_category depend only on product_id, not on the full composite key.
- B) First Normal Form, because the composite primary key contains two columns instead of one.
- C) Third Normal Form, because product_category depends on product_name rather than on the primary key.
- D) Boyce-Codd Normal Form only, because all non-key attributes depend on a superkey.

Correct Answer: A — A table with a composite primary key violates 2NF when any non-key attribute depends on only part of that key. Product_name and product_category depend solely on product_id, making them partial dependencies. The fix is to move those columns to a separate products table keyed on product_id.

Distractor analysis: B is incorrect because a composite primary key is not a 1NF violation; 1NF violations involve non-atomic values or repeating groups, not key composition. C is incorrect because product_category depending on product_name would be a 3NF transitive dependency, but the primary violation here is the partial dependency on the composite key, which is 2NF. D is incorrect because the table clearly violates 2NF, which is a lower-level normal form than BCNF.

---

### Question 2

A table `employees` has columns: employee_id (PK), employee_name, department_id, department_name, department_phone. Which normal form is violated and what is the correct fix?

- A) Third Normal Form is violated; create a departments table with department_id as PK containing department_name and department_phone, and keep only department_id as a FK in employees.
- B) Second Normal Form is violated; remove department_name and department_phone because they are not needed.
- C) First Normal Form is violated; the department_phone column may contain multiple phone numbers.
- D) No normal form is violated; all attributes depend on the employee_id primary key.

Correct Answer: A — Department_name and department_phone depend on department_id, not directly on employee_id. The dependency chain is employee_id → department_id → department_name (and department_phone). This transitive dependency violates 3NF. The fix is to extract department information into its own table.

Distractor analysis: B is incorrect because removing attributes rather than restructuring them discards data; the correct fix is relational decomposition, not deletion. C is incorrect because no evidence of multi-valued phone cells is stated; this is a 3NF problem, not 1NF. D is incorrect because department_name and department_phone do not depend on employee_id directly — they depend on department_id, which is the transitive dependency that violates 3NF.

---

### Question 3

Which of the following table designs violates First Normal Form?

- A) A `students` table where the `courses_enrolled` column contains a comma-separated list of course IDs in each cell.
- B) A `products` table where the `price` column allows NULL values.
- C) An `orders` table with a composite primary key of (order_id, product_id).
- D) An `employees` table where the `department_id` column is a foreign key referencing the departments table.

Correct Answer: A — Storing a comma-separated list of course IDs in a single cell produces a non-atomic value. Each cell must contain exactly one indivisible value. Storing multiple IDs in one cell violates 1NF. The fix is to create a separate student_courses table with one row per enrollment.

Distractor analysis: B is incorrect because allowing NULL values does not violate 1NF; NULL indicates the absence of a value and is a valid atomic state. C is incorrect because a composite primary key is a valid relational design and does not violate 1NF. D is incorrect because a foreign key reference is a proper relational constraint and does not affect first normal form compliance.

---

### Question 4

In an Entity-Relationship Diagram using Crow's Foot notation, a line between the Customer entity and the Order entity has a single vertical bar on the Customer side and a crow's foot on the Order side. What does this cardinality notation indicate?

- A) One customer can be associated with many orders, and each order belongs to exactly one customer.
- B) Many customers can be associated with one order, and the order belongs to all of them.
- C) The relationship is optional on both sides; a customer may have no orders.
- D) The relationship is a many-to-many association requiring a junction table.

Correct Answer: A — In Crow's Foot notation, a single vertical bar means "exactly one" and a crow's foot means "many." The bar on the Customer side means each order has exactly one customer. The crow's foot on the Order side means each customer can have many orders. This is the standard one-to-many (1:N) cardinality.

Distractor analysis: B is incorrect because the crow's foot is on the Order side, indicating many orders per customer — not many customers per order. C is incorrect because a circle (not a bar) indicates optional participation; a single bar indicates mandatory participation of exactly one. D is incorrect because M:N cardinality would be shown with crow's feet on both sides.

---

### Question 5

A developer proposes storing a many-to-many relationship between Students and Courses directly in the Students table as an array of course_ids. What is the primary design problem with this approach for a Cloud SQL relational schema?

- A) It violates First Normal Form by storing a non-atomic, multi-valued array in a single column.
- B) It violates Third Normal Form by creating a transitive dependency between student_id and course attributes.
- C) It violates Second Normal Form because the array column would become a partial dependency.
- D) Arrays are not supported in Cloud SQL for PostgreSQL, so the design would not execute.

Correct Answer: A — Storing an array of course_ids in a single column is a multi-valued, non-atomic value. This directly violates 1NF. The correct relational design is a junction table (enrollments) with foreign keys to both students and courses. Note: PostgreSQL does support array types natively, but using them this way breaks relational normalization.

Distractor analysis: B is incorrect because a transitive dependency (3NF violation) involves a non-key column depending on another non-key column, not an array in a single column. C is incorrect because 2NF violations require a composite primary key; an array column is a 1NF issue. D is incorrect because PostgreSQL does support array columns; the problem is the normalization violation, not a technical impossibility.

---

### Question 6

You are designing a Cloud SQL schema for a library system. A book can be written by multiple authors, and an author can write multiple books. How should this relationship be implemented?

- A) Create a book_authors junction table with foreign keys to both the books table and the authors table, with a composite primary key of (book_id, author_id).
- B) Add an author_id column to the books table and allow NULL when a book has multiple authors.
- C) Add an array column `author_ids` to the books table containing all author IDs.
- D) Store all author information as JSON in a single column in the books table.

Correct Answer: A — A many-to-many relationship between books and authors must be resolved with a junction table in a relational schema. The book_authors table holds one row per book-author combination with a composite primary key ensuring no duplicates.

Distractor analysis: B is incorrect because a single author_id can store only one author per book, and NULL does not represent multiple authors — it represents absence. C is incorrect because an array of IDs in one column violates 1NF. D is incorrect because storing JSON in a relational column bypasses the relational model and makes querying by author impossible without parsing the JSON, which is inefficient and error-prone.

---

### Question 7

Which of the following statements correctly describes the difference between a partial dependency and a transitive dependency?

- A) A partial dependency involves a non-key attribute depending on part of a composite key; a transitive dependency involves a non-key attribute depending on another non-key attribute.
- B) A partial dependency involves a non-key attribute depending on a foreign key; a transitive dependency involves two primary keys in the same table.
- C) A partial dependency occurs only in 1NF tables; a transitive dependency occurs only in 2NF tables.
- D) A partial dependency and a transitive dependency are two names for the same concept.

Correct Answer: A — A partial dependency requires a composite primary key; the non-key attribute depends on only a subset of that key. A transitive dependency involves a chain: PK → non-key-A → non-key-B, where non-key-B depends on non-key-A rather than directly on the primary key.

Distractor analysis: B is incorrect because partial dependencies are about composite primary keys, not foreign keys, and the definition of transitive dependency does not involve two primary keys in one table. C is incorrect because both types of dependency can exist in any table; the relevant question is which normal form they violate (2NF for partial, 3NF for transitive). D is incorrect because they are distinct concepts that represent different structural problems requiring different fixes.

---

### Question 8

You are designing a schema for Cloud Spanner to handle a global e-commerce platform. Your data model shows that every OrderItem record is always accessed through its parent Order. Which Spanner-specific design technique optimizes read performance for this access pattern?

- A) Define OrderItems as an interleaved table in the Order table so child rows are physically stored with the parent row.
- B) Normalize the schema to 3NF and rely on standard foreign key joins.
- C) Store OrderItems as a JSON column within the Orders table to avoid joins entirely.
- D) Create a separate Bigtable instance to store order line items and join it to Cloud Spanner at query time.

Correct Answer: A — Cloud Spanner supports table interleaving, which physically co-locates child rows with the parent row on the same Spanner server. When a query reads an Order and all its OrderItems, all data is on the same server, eliminating cross-server RPC calls. This is the primary performance optimization for parent-child access patterns in Spanner.

Distractor analysis: B is incorrect because standard foreign key joins in Spanner may require cross-server lookups in a globally distributed system, which is exactly the performance problem interleaving solves. C is incorrect because storing JSON in a column bypasses Spanner's relational model and prevents transactional guarantees on individual item fields. D is incorrect because Bigtable and Cloud Spanner serve different purposes; using a separate Bigtable instance for child data would complicate the architecture without providing the co-location benefit interleaving offers.

---

### Question 9

A table `invoices` stores: invoice_id (PK), customer_id, customer_name, customer_city, invoice_date, total_amount. A data analyst reports that when a customer moves to a new city, the customer_city field is correct on recent invoices but wrong on historical ones, because someone updated only new records. Which design principle was violated and what is the correct fix?

- A) Third Normal Form was violated by storing customer_city in invoices; customer attributes should be in a customers table referenced by foreign key.
- B) First Normal Form was violated because customer_city may contain a complex multi-part address.
- C) Second Normal Form was violated because customer_city depends on a partial composite key.
- D) No design violation occurred; this is an application bug in the update logic, not a schema problem.

Correct Answer: A — Customer_city depends on customer_id, not on invoice_id. The transitive dependency is invoice_id → customer_id → customer_city. Storing it in the invoices table causes the update anomaly described: the same fact (customer location) must be maintained in multiple rows. Moving customer attributes to a customers table and joining on customer_id eliminates this problem.

Distractor analysis: B is incorrect because city as a single text value is atomic; no 1NF violation is described. C is incorrect because invoice_id is a single-column primary key, making 2NF violations impossible. D is incorrect because the root cause is the schema design: storing a fact (customer location) in multiple rows makes inconsistent updates structurally inevitable; an application fix is a band-aid over a design flaw.

---

### Question 10

When translating an ERD to SQL DDL, a non-identifying relationship between the Department entity (parent) and the Employee entity (child) should be implemented as which of the following?

- A) A foreign key column in the Employee table referencing the Department primary key, where the Employee table has its own independent primary key.
- B) A composite primary key in the Employee table that includes the Department primary key as a component.
- C) A junction table between Department and Employee with foreign keys to both tables.
- D) An array column in the Department table storing all employee IDs for that department.

Correct Answer: A — A non-identifying relationship means the child entity (Employee) has its own independent primary key and is not identified by the parent. The Department's primary key appears only as a foreign key in the Employee table. The Employee can exist independently of a specific Department if needed.

Distractor analysis: B is incorrect because including the parent PK in the child's composite PK describes an identifying relationship, not a non-identifying one. C is incorrect because a junction table resolves many-to-many relationships; a one-to-many Department-to-Employee relationship does not need one. D is incorrect because storing employee IDs as an array in the parent table violates 1NF and inverts the standard foreign key direction.

---

Reference: cloud.google.com/learn
