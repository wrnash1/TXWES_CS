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

---

### Question 11 (5 points)

A table `sales_rep_territories` has columns: rep_id (PK), rep_name, territory_id, territory_name, territory_manager. Which normal form is violated and why?

- A) Third Normal Form — territory_name and territory_manager depend on territory_id, not directly on rep_id.
- B) Second Normal Form — rep_name depends on only part of a composite primary key.
- C) First Normal Form — territory_manager may represent multiple managers in one cell.
- D) No normal form is violated — all attributes depend on rep_id.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The primary key is rep_id alone (single column), so a 2NF violation (partial dependency) is impossible; 2NF violations require a composite primary key.
  - C) No evidence of multi-valued cells is given; the question describes single-valued columns, which satisfies 1NF atomicity.
  - D) Territory_name and territory_manager depend on territory_id, not rep_id; the transitive chain rep_id → territory_id → territory_name violates 3NF.

---

### Question 12 (5 points)

Which of the following correctly describes an insertion anomaly in a poorly designed relational table?

- A) A new fact cannot be recorded without also inserting an unrelated fact as part of the same row.
- B) An INSERT statement fails because a NOT NULL constraint is violated.
- C) Two rows with the same primary key value are inserted, causing a duplicate key error.
- D) An inserted row references a non-existent parent row, violating a foreign key constraint.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A NOT NULL constraint violation is an integrity enforcement mechanism, not a design anomaly; it reflects a constraint working correctly, not a schema deficiency.
  - C) A duplicate primary key is a constraint violation, not a normalization anomaly; it indicates the application attempted to insert a duplicate row.
  - D) A foreign key violation is a referential integrity issue, not an insertion anomaly as defined in normalization theory; an insertion anomaly occurs when valid data cannot be stored without introducing unrelated data.

---

### Question 13 (5 points)

A database designer is creating a schema where a `Project` entity can have many `Tasks`, and each `Task` belongs to exactly one `Project`. The `Task` entity's primary key is composed of (project_id, task_number), where task_number is only unique within a project. What type of relationship does this represent?

- A) An identifying relationship, because the child entity's primary key includes the parent entity's primary key.
- B) A non-identifying relationship, because the child has its own independent primary key.
- C) A many-to-many relationship, because each project has multiple tasks.
- D) A reflexive relationship, because the task_number is derived from the project.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A non-identifying relationship means the child's primary key is independent of the parent's; here the child's PK includes the parent's PK (project_id), which is the definition of an identifying relationship.
  - C) A many-to-many relationship requires each entity on both sides to have multiple associations with the other; here each task belongs to exactly one project, making it one-to-many.
  - D) A reflexive relationship is a self-referencing relationship within the same entity (e.g., an employee who manages other employees); this describes a parent-child relationship between two different entities.

---

### Question 14 (5 points)

When decomposing a table to eliminate a 3NF violation, which property must be preserved to ensure that the original table can be reconstructed from the decomposed tables?

- A) Lossless-join decomposition — the natural join of the decomposed tables produces exactly the original table with no spurious tuples.
- B) Functional dependency preservation — all functional dependencies from the original table are preserved in at least one of the decomposed tables.
- C) Referential integrity — all foreign key constraints in the decomposed tables reference valid primary keys.
- D) Domain-key normal form — all constraints in the decomposed tables are consequences of domain and key constraints.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Dependency preservation is also desirable but is a separate property; it ensures that all business rules (FDs) can be checked without joining tables, but it does not guarantee that original rows are recoverable.
  - C) Referential integrity is a constraint property, not a decomposition property; it must be maintained but does not define whether decomposition is lossless.
  - D) Domain-key normal form is a theoretical concept above BCNF and is not the property evaluated when assessing whether a decomposition is correct.

---

### Question 15 (5 points)

In Crow's Foot ERD notation, what does a circle followed by a crow's foot on one end of a relationship line indicate?

- A) Zero or many — the entity on that side may have zero or more related instances.
- B) One and only one — the entity must have exactly one related instance.
- C) One or many — the entity must have at least one related instance.
- D) Zero or one — the entity may have at most one related instance.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) One and only one is represented by two vertical bars (||); a circle indicates the zero/optional side.
  - C) One or many is represented by a vertical bar followed by a crow's foot (|<); a circle, not a bar, is on the minimum side in option A.
  - D) Zero or one is represented by a circle followed by a single vertical bar (O|); a crow's foot indicates "many," not "one."

---

### Question 16 (5 points)

A retail company's `product_catalog` table stores product_id, product_name, supplier_id, supplier_name, supplier_contact_email, and unit_cost. When the supplier changes their contact email, a DBA must update hundreds of rows. Which anomaly type does this represent?

- A) Update anomaly — the same fact (supplier email) is stored redundantly in multiple rows, requiring multiple updates to maintain consistency.
- B) Deletion anomaly — deleting a product row removes the supplier's contact information permanently.
- C) Insertion anomaly — a new supplier cannot be added until they supply at least one product.
- D) Referential anomaly — the supplier_id foreign key does not reference a separate suppliers table.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A deletion anomaly would occur if deleting the last product for a supplier also destroyed the only record of that supplier's contact info; the question specifically describes the update scenario.
  - C) An insertion anomaly would prevent adding a supplier with no products yet; the question describes an update problem with existing data, not an inability to insert new data.
  - D) "Referential anomaly" is not a standard normalization term; the issue is a design anomaly caused by denormalization (storing supplier attributes in the product table), not a constraint violation.

---

### Question 17 (5 points)

Which statement correctly describes why BigQuery schemas are deliberately denormalized while Cloud SQL schemas follow normalization principles?

- A) BigQuery is optimized for columnar analytical scans where JOINs are expensive; denormalization reduces JOIN overhead at the cost of storage redundancy. Cloud SQL handles OLTP workloads where JOINs are efficient and normalization prevents update anomalies.
- B) BigQuery does not support JOIN operations, so all data must be in a single flat table.
- C) Cloud SQL cannot store duplicate column values, forcing normalization, while BigQuery has no uniqueness constraints.
- D) Normalized schemas in BigQuery would violate its row-size limits, making denormalization technically required.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) BigQuery fully supports JOIN operations; the reason for denormalization is performance optimization for analytical workloads, not a technical limitation.
  - C) Cloud SQL can store duplicate column values in non-key columns; normalization is a design discipline, not a technical enforcement mechanism in the storage engine.
  - D) BigQuery has no practical row-size constraint that forces denormalization; the motivation is query performance on columnar data, not storage mechanics.

---

### Question 18 (5 points)

A `flights` table has a composite primary key of (flight_number, departure_date). The table also stores: airline_id, airline_name, aircraft_type, origin_airport, destination_airport. Which 2NF violation is present?

- A) airline_name depends only on airline_id, not on the full composite key (flight_number, departure_date).
- B) departure_date depends only on flight_number, not on the full composite key.
- C) origin_airport depends on destination_airport rather than on the primary key.
- D) aircraft_type is a transitive dependency through airline_id.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Departure_date is part of the primary key itself, not a non-key attribute; it cannot participate in a partial dependency.
  - C) origin_airport depending on destination_airport would be a transitive dependency (3NF violation), not a partial dependency (2NF violation); additionally no evidence for this dependency is given.
  - D) A transitive dependency violates 3NF, not 2NF; the question asks specifically about a 2NF violation, which requires a partial dependency on the composite key.

---

### Question 19 (5 points)

A DBA is migrating an on-premises Oracle schema to Cloud SQL for PostgreSQL. The source schema contains a table with 47 columns and is in 1NF but not 2NF. The migration requires the destination schema to be in at least 3NF. What is the correct order of normalization steps?

- A) Eliminate partial dependencies to reach 2NF, then eliminate transitive dependencies to reach 3NF.
- B) Eliminate transitive dependencies to reach 3NF first, then check for partial dependencies.
- C) Eliminate multi-valued attributes to reach 1NF, then eliminate all non-key dependencies at once.
- D) Convert to BCNF directly, which automatically satisfies 1NF, 2NF, and 3NF requirements.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Normal form levels must be achieved in order (1NF → 2NF → 3NF); a table cannot be in 3NF unless it is first in 2NF; skipping 2NF to address transitive dependencies leaves partial dependencies unresolved.
  - C) The table is already stated to be in 1NF, so eliminating multi-valued attributes is already done; the remaining work is achieving 2NF then 3NF in sequence.
  - D) BCNF cannot be achieved without first achieving 3NF; converting directly to BCNF is not a defined single-step process and could result in loss of functional dependency preservation if not done carefully.

---

### Question 20 (5 points)

An ERD shows a `Customer` entity connected to a `Shipping_Address` entity with a relationship labeled "has" and cardinality markers showing one customer to zero-or-many addresses. Which SQL DDL pattern correctly implements this relationship?

- A) Add a `customer_id` foreign key column to the `shipping_addresses` table referencing the `customers` table.
- B) Add a `shipping_address_id` foreign key column to the `customers` table referencing the `shipping_addresses` table.
- C) Create a junction table `customer_addresses` with foreign keys to both `customers` and `shipping_addresses`.
- D) Store address data as a JSON array column in the `customers` table.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Placing the foreign key in the parent (customers) table means each customer can only reference one address; to support multiple addresses the FK must be in the child (shipping_addresses) table.
  - C) A junction table is used for many-to-many relationships; this is a one-to-many relationship (one customer, many addresses) and does not require a junction table.
  - D) Storing addresses as a JSON array violates 1NF and prevents indexing, querying, or constraining individual address fields in the relational model.
