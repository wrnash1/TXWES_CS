# Video Script: Module 01 — Relational Database Fundamentals and SQL Review (Part 1)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 12–14 minutes

---

### Opening — Welcome and Course Context

**[SHOW SLIDE: Texas Wesleyan University wordmark, course title CIS-4327 Database Administration, Module 01]**

Hello, and welcome to CIS-4327 Database Administration. I am Professor Nash, and this is Module 01: Relational Database Fundamentals and SQL Review.

Before we touch a single Google Cloud service, we need to make sure your relational database foundation is solid. Every GCP database product you will work with this semester — Cloud SQL, Cloud Spanner, AlloyDB, BigQuery — either builds directly on the relational model or requires you to understand it as a reference point. The Google Cloud Professional Cloud Database Engineer exam tests these foundations explicitly.

In Part 1 today, we cover the relational model, ACID properties, data integrity constraints, and SQL Data Definition Language. In Part 2, we move into DML — SELECT, JOIN, GROUP BY — and tie everything to exam scenarios.

Let us get started.

---

### Section 1 — What Is a Relational Database?

**[SHOW SLIDE: Table diagram — rows and columns, primary key column highlighted]**

A relational database organizes data into tables. Each table is formally called a relation. A table has columns, which define attributes, and rows, which are individual data records called tuples.

The critical concept is the primary key. A primary key is one column — or a combination of columns — whose value uniquely identifies every row in the table. No two rows can share the same primary key value, and a primary key column can never contain NULL.

**[SHOW SLIDE: Two tables — customers and orders — with a connecting arrow labeled foreign key]**

A foreign key in one table references the primary key of another table. This relationship is how the relational model links data across tables without duplicating it. If you have a customers table with a customer_id primary key, and an orders table with a customer_id foreign key, the database engine enforces that every order must belong to a real customer. Attempting to insert an order for a customer_id that does not exist will fail with a referential integrity violation.

This enforcement is not optional decoration — it is a core guarantee of the relational model, and it is what separates a properly designed relational database from a spreadsheet.

---

### Section 2 — ACID Properties

**[SHOW SLIDE: Four tiles — Atomicity, Consistency, Isolation, Durability]**

ACID is the most tested concept in the foundational domain of the GCP Database Engineer exam. Let me define each property with a concrete example.

Atomicity means that every operation in a transaction either succeeds completely or fails completely. Suppose you are transferring money between two bank accounts. That transfer requires two writes: subtract from account A, add to account B. Atomicity guarantees that both writes happen or neither does. You cannot have a situation where the money leaves account A but never arrives at account B.

Consistency means that a transaction can only bring the database from one valid state to another valid state. All data integrity constraints — primary keys, foreign keys, NOT NULL constraints, CHECK constraints — must be satisfied at the end of every committed transaction.

Isolation means that concurrent transactions do not interfere with each other. If two users are updating the same row at the same time, isolation prevents one transaction from reading an intermediate, incomplete state written by the other.

Durability means that once a transaction is committed, it is permanent. Even if the server crashes one millisecond after the commit acknowledgment, the data is preserved. This is typically implemented through write-ahead logging — the database writes a log record before applying changes to data pages.

**[SHOW SLIDE: GCP service ACID matrix]**

| GCP Service | ACID Support | Notes |
|---|---|---|
| Cloud SQL (MySQL/PostgreSQL) | Full ACID | Transaction-level |
| Cloud Spanner | Full ACID | Global, multi-region |
| AlloyDB | Full ACID | PostgreSQL-compatible |
| Firestore | Limited | Single-document only |
| Bigtable | No multi-row | Optimized for throughput |
| BigQuery | No row-level | OLAP analytics engine |

For the exam, you must know which GCP services provide full ACID compliance. Cloud SQL and Cloud Spanner are the two fully-managed relational services that guarantee complete ACID behavior. Bigtable is optimized for throughput and does not provide multi-row transactions. Firestore provides limited ACID support within a single document only.

---

### Section 3 — SQL Data Definition Language

**[SHOW SLIDE: SQL DDL command categories — CREATE, ALTER, DROP, TRUNCATE]**

SQL is divided into sublanguages. The Data Definition Language, or DDL, is the set of commands that define and modify the structure of your database objects.

**[SHOW CODE]**

```sql
-- Create the customers table
CREATE TABLE customers (
    customer_id   SERIAL        PRIMARY KEY,
    email         VARCHAR(255)  NOT NULL UNIQUE,
    full_name     VARCHAR(100)  NOT NULL,
    created_at    TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);

-- Create the orders table with a foreign key constraint
CREATE TABLE orders (
    order_id      SERIAL        PRIMARY KEY,
    customer_id   INTEGER       NOT NULL,
    order_total   NUMERIC(10,2) NOT NULL CHECK (order_total >= 0),
    order_date    DATE          NOT NULL,
    status        VARCHAR(20)   NOT NULL DEFAULT 'pending',
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE RESTRICT
);
```

**[END CODE]**

Let me walk through the important elements here.

SERIAL is a PostgreSQL shorthand that creates an auto-incrementing integer sequence. Every new row gets the next integer automatically.

The NOT NULL constraint means that column cannot be omitted. If you try to insert a row without a full_name, the database rejects it immediately.

UNIQUE on the email column means no two customers can share the same email address. Combined with NOT NULL, this gives you a strong natural identifier in addition to the surrogate primary key.

The CHECK constraint on order_total ensures that no negative order amounts can be stored. The database enforces this rule automatically.

The FOREIGN KEY with ON DELETE RESTRICT means that if you try to delete a customer who has existing orders, the delete will fail. Child records must be removed first. This prevents orphaned orders from accumulating in the database.

**[SHOW CODE]**

```sql
-- Add a column to an existing table
ALTER TABLE customers
    ADD COLUMN phone VARCHAR(20);

-- Add an index on the email column
CREATE INDEX idx_customers_email
    ON customers (email);

-- Remove a table entirely (safe form)
DROP TABLE IF EXISTS orders;
```

**[END CODE]**

ALTER TABLE lets you modify an existing table without recreating it. In Cloud SQL for PostgreSQL, adding a nullable column to a large table is a metadata-only operation and takes milliseconds. Adding a NOT NULL column with no default on a large table requires a table rewrite, which can take significant time and may lock the table.

CREATE INDEX builds a B-tree index by default. An index on the email column means the database can find a customer by email in logarithmic time rather than scanning every row. For a table with ten million rows, this difference is measured in milliseconds versus seconds.

---

### Section 4 — Data Integrity Constraints Summary

**[SHOW SLIDE: Constraint reference table]**

| Constraint | Purpose | Behavior on Violation |
|---|---|---|
| PRIMARY KEY | Unique row identifier, never NULL | INSERT or UPDATE fails |
| FOREIGN KEY | Referential integrity between tables | INSERT, UPDATE, or DELETE fails |
| UNIQUE | No duplicate values in column | INSERT or UPDATE fails |
| NOT NULL | Column must have a value | INSERT or UPDATE fails |
| CHECK | Custom business rule validation | INSERT or UPDATE fails |

Each of these constraints is enforced by the database engine, not by the application. Application-level validation can be bypassed by direct database connections, batch imports, or bugs. Database-level constraints cannot be bypassed regardless of how data arrives.

---

### Section 5 — Relational Model vs. NoSQL — Choosing the Right GCP Service

**[SHOW SLIDE: Decision flowchart — structured schema, global distribution, document storage, analytical queries]**

One of the most frequently tested skills on the GCP Database Engineer exam is service selection. Given a workload description, you must pick the right database service. Here is the framework.

If the workload has a well-defined, stable schema, requires ACID transactions, and serves a single region, the answer is almost always Cloud SQL.

If the workload has a well-defined schema, requires ACID transactions, and must serve users globally with high availability, the answer is Cloud Spanner.

If the workload stores JSON documents, needs flexible schema evolution, and serves mobile or web clients, the answer is Firestore.

If the workload involves massive volumes of time-series or sensor data at high write throughput, the answer is Bigtable.

If the workload is analytical — aggregating historical data, running complex GROUP BY queries across billions of rows — the answer is BigQuery.

We will cover each of these services in dedicated modules. What I want you to take from this module is that the relational model — with its tables, keys, constraints, and SQL — is the foundation that all of these services either implement or depart from by design.

---

### Closing — Part 1 Summary

**[SHOW SLIDE: Module 01 Part 1 Key Concepts recap]**

In Part 1 we covered the following.

A relational database organizes data into tables with rows and columns. Primary keys uniquely identify rows. Foreign keys enforce relationships between tables.

ACID stands for Atomicity, Consistency, Isolation, and Durability. Cloud SQL and Cloud Spanner provide full ACID compliance. Know which GCP services do and do not provide ACID for the exam.

SQL DDL commands — CREATE TABLE, ALTER TABLE, CREATE INDEX, DROP TABLE — define and modify database structure. Constraints including PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, and CHECK are enforced by the database engine.

In Part 2, we move into DML — SELECT, INSERT, UPDATE, DELETE, JOIN, and GROUP BY. We will also cover EXPLAIN ANALYZE and connect everything to exam scenarios.

See you in Part 2.

---

Reference: cloud.google.com/learn
