# Video Script: Module 02 — Database Design: Normalization and ERDs (Part 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 11–13 minutes

---

### Opening

**[SHOW SLIDE: Module 02 Part 2 — Entity-Relationship Diagrams and Schema Translation]**

Welcome back. I am Professor Nash, and this is Part 2 of Module 02.

In Part 1 we normalized a schema from unnormalized form through 1NF, 2NF, and 3NF. Now we are going to work on the design phase that should happen before you write any SQL at all: the Entity-Relationship Diagram, or ERD.

An ERD is a visual representation of the entities in your system, the attributes those entities have, and the relationships between them. Building an ERD first prevents the kinds of normalization violations we fixed in Part 1 from appearing in the first place.

---

### Section 1 — ERD Components: Entities, Attributes, and Relationships

**[SHOW SLIDE: ERD symbol reference — rectangle, oval, diamond, connecting lines]**

An ERD uses four main symbols.

A rectangle represents an entity — a real-world object or concept that you store data about. Customer, Order, Product, and Employee are all entities.

An oval represents an attribute — a property of an entity. Customer has attributes like customer_id, full_name, and email.

A diamond represents a relationship — an association between two entities. The relationship between Customer and Order might be called "places."

Lines connect entities to their attributes and entities to relationships. The style of the line at each end indicates the cardinality of the relationship.

---

### Section 2 — Cardinality Notation

**[SHOW SLIDE: Crow's Foot notation symbols — one, many, zero-or-one, one-or-many, zero-or-many]**

Cardinality describes how many instances of one entity relate to instances of another entity. The most common notation you will see in professional tools is Crow's Foot notation.

A single vertical bar on a line means exactly one. A crow's foot (three-pronged fork) means many. A circle means zero.

The combinations you need to know:

One-to-one (1:1): One customer has exactly one loyalty profile. Drawn as a single bar on both sides.

One-to-many (1:N): One customer can place many orders, but each order belongs to exactly one customer. Drawn as a single bar on the customer side and a crow's foot on the order side.

Many-to-many (M:N): One student can enroll in many courses, and one course can have many students. Drawn as crow's feet on both sides.

**[SHOW SLIDE: Many-to-many resolved with junction table — students, enrollments, courses]**

A many-to-many relationship in an ERD cannot be directly implemented in a relational database. It must be resolved into two one-to-many relationships using a junction table — also called an associative entity or bridge table. The enrollments table we built in Part 1 is exactly this: it resolves the many-to-many between students and courses.

---

### Section 3 — Identifying vs. Non-Identifying Relationships

**[SHOW SLIDE: Identifying vs. non-identifying relationship lines — solid vs. dashed]**

An identifying relationship means the child entity's primary key includes the parent entity's primary key as a component. The child cannot exist independently — its identity depends on the parent. In Crow's Foot notation, identifying relationships are shown with a solid line.

A non-identifying relationship means the child entity has its own independent primary key and references the parent through a foreign key only. In Crow's Foot notation, non-identifying relationships are shown with a dashed line.

Example of an identifying relationship: order_items identified by (order_id, product_id). An order item cannot exist without an order.

Example of a non-identifying relationship: an employee is assigned to a department. The employee has their own employee_id primary key independent of the department.

---

### Section 4 — Translating an ERD to SQL

**[SHOW CONSOLE: Cloud SQL Studio or Cloud Shell with PostgreSQL prompt]**

Now let me walk through translating the four-entity student registration ERD from Part 1 into actual SQL DDL. The entities are students, instructors, courses, and enrollments.

**[SHOW CODE]**

```sql
-- Entity: students
CREATE TABLE students (
    student_id    SERIAL       PRIMARY KEY,
    full_name     VARCHAR(100) NOT NULL,
    email         VARCHAR(255) NOT NULL UNIQUE,
    enrolled_year INTEGER      NOT NULL
);

-- Entity: instructors
CREATE TABLE instructors (
    instructor_id SERIAL       PRIMARY KEY,
    full_name     VARCHAR(100) NOT NULL,
    email         VARCHAR(255) NOT NULL UNIQUE,
    department    VARCHAR(100)
);

-- Entity: courses (non-identifying FK to instructors)
CREATE TABLE courses (
    course_id     SERIAL       PRIMARY KEY,
    course_code   VARCHAR(20)  NOT NULL UNIQUE,
    course_name   VARCHAR(200) NOT NULL,
    credits       INTEGER      NOT NULL CHECK (credits BETWEEN 1 AND 6),
    instructor_id INTEGER      NOT NULL,
    CONSTRAINT fk_course_instructor
        FOREIGN KEY (instructor_id)
        REFERENCES instructors(instructor_id)
        ON DELETE RESTRICT
);

-- Junction table: enrollments (identifying relationship)
CREATE TABLE enrollments (
    student_id    INTEGER      NOT NULL,
    course_id     INTEGER      NOT NULL,
    enrolled_at   TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    grade         CHAR(2),
    PRIMARY KEY (student_id, course_id),
    CONSTRAINT fk_enroll_student
        FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_enroll_course
        FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
        ON DELETE RESTRICT
);
```

**[END CODE]**

Notice the direct mapping from ERD to SQL. Each entity becomes a table. Each attribute becomes a column. Each one-to-many relationship becomes a foreign key constraint. The many-to-many relationship between students and courses becomes the enrollments junction table with a composite primary key.

---

### Section 5 — ERD Design in Practice: Cloud SQL Schema Design

**[SHOW CONSOLE: Google Cloud Console — Cloud SQL instance, Cloud SQL Studio]**

In practice, you will design your ERD first — either on paper, in a tool like draw.io, Lucidchart, or dbdiagram.io — and then translate it to DDL. GCP's Cloud SQL Studio provides a visual schema browser, but the initial design still happens before the instance is created.

**[SHOW SLIDE: Design checklist for Cloud SQL schemas]**

When designing a Cloud SQL schema, follow this checklist.

One: define all entities and their primary keys before writing any JOIN logic.

Two: resolve every many-to-many relationship into a junction table.

Three: verify the schema is in 3NF before building application code against it. Retrofitting normalization after code is written is extremely expensive.

Four: add indexes on all foreign key columns at schema creation time. In PostgreSQL, foreign key constraints do not automatically create indexes on the referencing column — only on the referenced column. Missing FK indexes are one of the most common causes of slow DELETE and JOIN operations.

Five: document cardinality constraints in comments within your DDL. Future developers will thank you.

---

### Section 6 — Boyce-Codd Normal Form (Brief)

**[SHOW SLIDE: BCNF definition — for every nontrivial FD X→Y, X must be a superkey]**

For completeness, I want to mention Boyce-Codd Normal Form, or BCNF. BCNF is a stricter version of 3NF. A table is in BCNF if for every functional dependency X → Y, X is a superkey — meaning X uniquely identifies every row in the table.

Most tables that are in 3NF are also in BCNF. The distinction matters in tables with multiple overlapping candidate keys, which is a rare edge case. You will occasionally see BCNF referenced in the GCP exam's database design domain, so you should know the definition. For most practical schemas, achieving 3NF is sufficient.

---

### Section 7 — Exam Tips for Module 02

**[SHOW SLIDE: Five exam tips for normalization and ERDs]**

Here are five exam tips specifically for the design domain.

Tip one: the GCP exam will present an unnormalized table and ask you to identify which normal form it violates. If a non-key attribute depends on part of a composite key — 2NF violation. If a non-key attribute depends on another non-key attribute — 3NF violation. If cells contain non-atomic values or repeating column groups — 1NF violation.

Tip two: many-to-many relationships always resolve to a junction table. An ERD question showing M:N cardinality on both sides is telling you a junction table is required.

Tip three: Cloud SQL and Cloud Spanner support fully normalized relational schemas. BigQuery uses denormalized wide tables and nested/repeated fields for performance. Service selection questions about schema design hinge on OLTP vs. OLAP workload type.

Tip four: in Cloud Spanner, the recommended approach for related tables is to use interleaved tables rather than standard foreign keys for performance. This is an advanced topic covered in Module 04, but know that normalization principles still apply — the physical storage strategy differs from standard relational databases.

Tip five: the term "referential integrity" on the exam always connects to foreign key constraints. If a scenario says referential integrity is being violated, the answer involves adding or enforcing a foreign key constraint.

---

### Closing — Module 02 Wrap-Up

**[SHOW SLIDE: Module 02 complete]**

That completes Module 02. You now know how to design a normalized relational schema using both formal normalization theory and entity-relationship diagrams.

Your lab for this module walks you through normalizing a provided unnormalized relation to 3NF with full written justification, then implementing the resulting schema in Cloud SQL for PostgreSQL. Complete the lab before the quiz.

In Module 03 we go deep on Cloud SQL — creating and configuring MySQL and PostgreSQL instances, managing users and connections, automated backups, and read replicas.

See you there.

---

Reference: cloud.google.com/learn
