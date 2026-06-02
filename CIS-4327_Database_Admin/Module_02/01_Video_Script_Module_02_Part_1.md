# Video Script: Module 02 — Database Design: Normalization and ERDs (Part 1)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 13–15 minutes

---

### Opening

**[SHOW SLIDE: Module 02 — Database Design: Normalization and ERDs]**

Hello, and welcome back to CIS-4327. I am Professor Nash. This is Module 02: Database Design — Normalization and Entity-Relationship Diagrams.

In Module 01 we built the SQL foundation. Now we are going to use that foundation to design databases that are correct by construction. Poor schema design is one of the most expensive problems in enterprise systems — it causes data anomalies, duplicated records, failed migrations, and query performance problems that are nearly impossible to fix after a system is in production.

In Part 1 we cover functional dependencies, the three primary normal forms, and denormalization trade-offs. In Part 2 we cover entity-relationship modeling, ERD notation, and translating an ERD into a Cloud SQL schema.

---

### Section 1 — Why Normalization Matters

**[SHOW SLIDE: Unnormalized flat table with customer info duplicated across every order row]**

Consider a table that stores everything in one place: customer name, customer email, order date, product name, product price, and quantity — all in a single flat table. This design has three serious failure modes.

The first is update anomalies. If a customer changes their email address, you must update every row that contains their information. Miss one row and the database now contains contradictory data about the same customer.

The second is insertion anomalies. You cannot record a product in the database until someone actually buys it, because product information lives in the same row as the order. The existence of a product is tied to the existence of a sale.

The third is deletion anomalies. If you delete the only order for a customer, you lose the customer's contact information entirely. Deleting a business fact destroys an unrelated business fact.

Normalization eliminates these problems by organizing data so that each fact is stored in exactly one place. A change to any fact requires updating exactly one row.

---

### Section 2 — Functional Dependencies

**[SHOW SLIDE: Dependency notation — X → Y means knowing X determines Y]**

The mathematical foundation of normalization is the functional dependency. We say that attribute X functionally determines attribute Y — written X → Y — if knowing the value of X always and uniquely identifies the value of Y.

Examples of functional dependencies in a typical business schema:

customer_id → customer_email. Knowing the customer_id tells you exactly one email address.

order_id → order_date. Knowing the order_id tells you exactly one order date.

(order_id, product_id) → quantity. Both components of the composite key are needed to determine the quantity for a specific line item.

A partial dependency occurs when a non-key attribute depends on only part of a composite primary key. For example, if a table has primary key (order_id, product_id) and product_name depends only on product_id, that is a partial dependency. The product_name can be determined without knowing the order_id at all.

A transitive dependency occurs when a non-key attribute depends on another non-key attribute rather than directly on the primary key. If an employees table stores employee_id, department_id, and department_name, and department_name depends on department_id rather than directly on employee_id, that is a transitive dependency through department_id.

Understanding these dependency types is required for all three normal forms.

---

### Section 3 — First Normal Form

**[SHOW SLIDE: Unnormalized table with multi-valued cells vs. 1NF table with atomic values]**

A table is in First Normal Form when four conditions are met.

First: every column contains atomic values — values that cannot be broken down further into meaningful sub-components. A cell containing "Alice; Bob; Carol" as a delimited list violates 1NF because the value is not atomic.

Second: every column contains values of the same data type. You cannot mix strings and integers in the same column.

Third: every row is uniquely identifiable. A primary key must exist.

Fourth: there are no repeating column groups. A design with columns phone_1, phone_2, phone_3 has a repeating group that violates 1NF.

**[SHOW SLIDE: Before — customers table with phone_1, phone_2, phone_3; After — separate customer_phones table]**

The classic 1NF fix for repeating column groups is to create a child table. Instead of storing multiple phone numbers in the same row of the customers table, create a customer_phones table with its own row for each phone number and a foreign key back to customers. The number of phone numbers a customer can have is now unlimited, and the schema stays clean.

---

### Section 4 — Second Normal Form

**[SHOW SLIDE: Composite PK table with order_id and product_id — product_name depending only on product_id highlighted]**

A table is in Second Normal Form when it satisfies 1NF and every non-key attribute is fully functionally dependent on the entire primary key — not just part of it.

2NF is only relevant for tables with composite primary keys. If your table has a single-column primary key, satisfying 1NF automatically satisfies 2NF.

**[SHOW SLIDE: Split into order_items and products tables]**

Here is a concrete example. Suppose we have an order_line_items table with composite primary key (order_id, product_id) and columns: quantity, product_name, and unit_price.

Quantity depends on both order_id and product_id — you need both to determine the quantity for a specific line item. Full dependency. Correct.

Product_name and unit_price depend only on product_id — they say nothing about which order this is. Partial dependencies. These violate 2NF.

The fix: move product_name and unit_price to a separate products table keyed on product_id alone. The order_line_items table retains only quantity — the only column that truly depends on the full composite key.

After the fix, if a product price changes, you update one row in the products table. No order rows need to change.

---

### Section 5 — Third Normal Form

**[SHOW SLIDE: employees table — employee_id → department_id → department_name transitive chain highlighted]**

A table is in Third Normal Form when it satisfies 2NF and no non-key attribute transitively depends on the primary key through another non-key attribute.

The informal mnemonic for 3NF is: every non-key attribute must depend on the key, the whole key, and nothing but the key.

**[SHOW SLIDE: employees split into employees and departments tables]**

Concrete example. An employees table stores employee_id, employee_name, department_id, and department_name. Primary key is employee_id.

Department_id depends on employee_id — direct dependency, fine.

Department_name depends on department_id, not on employee_id directly. The chain is employee_id → department_id → department_name. That transitive dependency violates 3NF.

The fix: create a departments table with department_id as primary key and department_name as a column. The employees table keeps department_id as a foreign key only.

After this fix, if the IT department renames itself to Information Technology, you update exactly one row in the departments table. Every employee in that department automatically reflects the new name through the join. No update anomaly is possible.

---

### Section 6 — Worked Normalization Example

**[SHOW SLIDE: Unnormalized student_courses flat table]**

Let me walk through a complete normalization from an unnormalized table to 3NF.

Starting table:

```text
student_courses (
    student_id, student_name, student_email,
    course_id, course_name,
    instructor_id, instructor_name, instructor_email,
    enrollment_date, grade
)
```

Composite primary key: (student_id, course_id)

Step 1 — 1NF check: all values are atomic, no repeating groups, primary key defined. The table is in 1NF.

Step 2 — 2NF check: find partial dependencies on the composite key.

student_name and student_email depend only on student_id. Partial dependency.
course_name, instructor_id, instructor_name, instructor_email depend only on course_id. Partial dependency.
enrollment_date and grade depend on both student_id and course_id together. Full dependency — these stay.

2NF fix — three tables:

```text
students (student_id PK, student_name, student_email)
courses (course_id PK, course_name, instructor_id, instructor_name, instructor_email)
enrollments (student_id FK, course_id FK, enrollment_date, grade,
             PRIMARY KEY (student_id, course_id))
```

Step 3 — 3NF check: find transitive dependencies in each remaining table.

In courses: instructor_name and instructor_email depend on instructor_id, not on course_id. Transitive dependency through instructor_id.

3NF fix — four tables:

```text
students (student_id PK, student_name, student_email)
instructors (instructor_id PK, instructor_name, instructor_email)
courses (course_id PK, course_name, instructor_id FK → instructors)
enrollments (student_id FK → students, course_id FK → courses,
             enrollment_date, grade,
             PRIMARY KEY (student_id, course_id))
```

Each fact is stored in exactly one place. No update, insertion, or deletion anomalies are possible in this schema.

---

### Section 7 — Denormalization and When to Use It

**[SHOW SLIDE: OLTP normalized schema vs. OLAP denormalized flat table]**

Normalization is the correct default for transactional (OLTP) databases like those you run on Cloud SQL or Cloud Spanner. But there are legitimate cases where you intentionally introduce controlled redundancy to improve read performance.

In analytical systems like BigQuery, data is often stored in wide, flat, denormalized tables or nested repeated fields. Joining ten tables in a query over billions of rows in a data warehouse is expensive. Pre-joining related data into a single wide table eliminates that join cost at query time.

The trade-off is write complexity. Inserts and updates must maintain redundant copies consistently. For read-heavy analytics workloads where writes are infrequent batch operations, this trade-off is acceptable and expected.

For your GCP exam: Cloud SQL and Cloud Spanner are used for normalized OLTP schemas. BigQuery is used for denormalized or semi-normalized analytical schemas. This is a direct service-selection criterion tested in exam scenarios.

---

### Closing — Part 1 Summary

**[SHOW SLIDE: Normal forms summary table]**

In Part 1 we covered functional dependencies and the three normal forms.

First Normal Form: atomic values, no repeating groups, primary key defined.

Second Normal Form: 1NF plus full functional dependency on the entire primary key — no partial dependencies.

Third Normal Form: 2NF plus no transitive dependencies through non-key attributes.

We also saw that denormalization is appropriate for analytical workloads — specifically BigQuery — where read performance outweighs write simplicity.

In Part 2 we move to entity-relationship diagrams: how to model entities, attributes, and relationships before writing SQL, and how to translate that model directly into a Cloud SQL schema.

See you in Part 2.

---

Reference: cloud.google.com/learn
