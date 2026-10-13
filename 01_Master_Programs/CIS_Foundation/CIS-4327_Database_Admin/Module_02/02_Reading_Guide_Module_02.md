# Reading Guide: Module 02 — Database Design: Normalization and ERDs

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4327 &BULL; DATABASE ADMINISTRATION & SQL OPTIMIZATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Introduction

Module 02 covers database design — the discipline of structuring a relational schema so that data is stored correctly, efficiently, and without redundancy. The Google Cloud Professional Cloud Database Engineer exam tests normalization and schema design in the context of Cloud SQL, Cloud Spanner, and migration scenarios. A poorly normalized source schema is one of the most common root causes of failed cloud migrations.

Complete this reading guide before the lab. The normalization worked examples and ERD translation section directly support the lab deliverables.

---

### 1. High-Yield Glossary

**Relation**: A table in the relational model. A set of tuples sharing the same attribute schema.

**Functional Dependency (FD)**: X → Y. If the value of X uniquely determines the value of Y, then Y is functionally dependent on X. Functional dependencies are the mathematical basis for all normal form definitions.

**Partial Dependency**: A non-key attribute depends on only part of a composite primary key. Violates Second Normal Form.

**Transitive Dependency**: A non-key attribute depends on another non-key attribute rather than directly on the primary key. Violates Third Normal Form. Notation: PK → A → B, where B is transitively dependent.

**Candidate Key**: Any attribute or minimal set of attributes that can uniquely identify every row in a table. A table may have multiple candidate keys. One is chosen as the primary key; others are called alternate keys.

**Superkey**: Any set of attributes that uniquely identifies rows. A candidate key is a minimal superkey — no proper subset of it is also a superkey.

**Composite Key**: A primary key consisting of two or more columns. Composite keys are required when no single column is sufficient to uniquely identify every row.

**Surrogate Key**: A system-generated identifier with no business meaning, typically an auto-incrementing integer or UUID. Preferred when natural keys are unstable or complex.

**Natural Key**: A key formed from real-world attributes that have business meaning, such as email address, SSN, or product SKU. Can change over time, complicating referential integrity.

**First Normal Form (1NF)**: Every column contains atomic values, no repeating column groups exist, all rows are uniquely identifiable.

**Second Normal Form (2NF)**: Satisfies 1NF, and every non-key attribute is fully functionally dependent on the entire primary key. Applies only to tables with composite keys.

**Third Normal Form (3NF)**: Satisfies 2NF, and no non-key attribute is transitively dependent on the primary key through another non-key attribute.

**Boyce-Codd Normal Form (BCNF)**: A stricter version of 3NF. For every nontrivial functional dependency X → Y, X must be a superkey of the table.

**Normalization**: The process of restructuring a relational schema to eliminate redundancy and anomalies by applying the normal form rules.

**Denormalization**: The intentional introduction of redundancy into a schema to improve read performance. Common in analytical systems like BigQuery.

**Update Anomaly**: A data integrity problem caused by storing the same fact in multiple places. Changing the fact in one place but not all others produces contradictory data.

**Insertion Anomaly**: A data integrity problem where a fact cannot be recorded unless another unrelated fact also exists in the same row.

**Deletion Anomaly**: A data integrity problem where deleting one fact inadvertently destroys another unrelated fact stored in the same row.

**Entity**: A real-world object or concept about which data is stored. Represented as a rectangle in an ERD.

**Attribute**: A property of an entity. Represented as an oval connected to its entity rectangle in an ERD.

**Relationship**: An association between two or more entities. Represented as a diamond in Chen notation, or as a labeled line in Crow's Foot notation.

**Cardinality**: Describes how many instances of one entity relate to instances of another. Key values: one-to-one (1:1), one-to-many (1:N), many-to-many (M:N).

**Junction Table**: A table used to resolve a many-to-many relationship between two entities. Contains foreign keys to both parent tables and typically has a composite primary key. Also called a bridge table or associative entity.

**Identifying Relationship**: The child entity's primary key incorporates the parent's primary key. The child cannot exist independently. Shown as a solid line in Crow's Foot notation.

**Non-Identifying Relationship**: The child entity has its own independent primary key. The parent's key appears only as a foreign key in the child. Shown as a dashed line in Crow's Foot notation.

---

### 2. Normal Forms — Reference Table

| Normal Form | Requirement | What It Eliminates | Violation Example |
|---|---|---|---|
| 1NF | Atomic values, no repeating groups, primary key defined | Multi-valued cells, column groups like phone_1/phone_2/phone_3 | A cell containing "Red, Blue, Green" |
| 2NF | 1NF + full FD on entire composite PK | Partial dependencies on composite keys | product_name depending only on product_id in a (order_id, product_id) keyed table |
| 3NF | 2NF + no transitive FDs through non-key columns | Transitive dependencies | department_name depending on department_id in an employees table |
| BCNF | 3NF + every FD determinant is a superkey | Anomalies in tables with overlapping candidate keys | Rare in practice; exam tests definition only |

---

### 3. Normalization Worked Example — Full Walkthrough

This worked example normalizes a flat employee project table from unnormalized form to 3NF. Study each step — the lab requires you to perform this same process independently.

#### Starting Table (Unnormalized)

```text
emp_project (
    emp_id, emp_name, emp_email, dept_id, dept_name,
    project_id, project_name, project_budget,
    role, hours_logged
)
```

Composite primary key: (emp_id, project_id)

#### Step 1 — Check 1NF

All values appear atomic. No repeating column groups. Primary key defined. The table satisfies 1NF.

#### Step 2 — Check 2NF: Find Partial Dependencies

Identify which non-key attributes depend on only part of the composite key.

emp_name, emp_email, dept_id, dept_name depend only on emp_id → partial dependencies.
project_name, project_budget depend only on project_id → partial dependencies.
role and hours_logged depend on both emp_id and project_id together → full dependencies, stay in the junction table.

2NF fix — create three tables:

```text
employees (emp_id PK, emp_name, emp_email, dept_id, dept_name)
projects (project_id PK, project_name, project_budget)
emp_projects (emp_id FK, project_id FK, role, hours_logged,
              PRIMARY KEY (emp_id, project_id))
```

#### Step 3 — Check 3NF: Find Transitive Dependencies

In the employees table: dept_name depends on dept_id, not on emp_id directly.
Transitive chain: emp_id → dept_id → dept_name. Violates 3NF.

3NF fix — create a departments table:

```text
departments (dept_id PK, dept_name)
employees (emp_id PK, emp_name, emp_email, dept_id FK → departments)
projects (project_id PK, project_name, project_budget)
emp_projects (emp_id FK → employees, project_id FK → projects,
              role, hours_logged,
              PRIMARY KEY (emp_id, project_id))
```

#### Final Schema Assessment

Each table stores one and only one kind of fact. Update, insertion, and deletion anomalies are eliminated. If a department name changes, one row in the departments table is updated and the change is reflected everywhere through joins.

---

### 4. ERD Cardinality Reference

| Relationship Type | Crow's Foot Notation | SQL Implementation | Example |
|---|---|---|---|
| One-to-one (1:1) | Single bar both sides | FK with UNIQUE constraint on child | Employee — EmployeeProfile |
| One-to-many (1:N) | Single bar on parent, crow's foot on child | FK in child references parent PK | Customer — Orders |
| Many-to-many (M:N) | Crow's foot on both sides | Junction table with two FKs | Students — Courses |
| Zero-or-one-to-many (0,1:N) | Circle+bar on parent, crow's foot on child | Nullable FK in child | Order — ShippingAddress |

---

### 5. ERD to SQL Translation Rules

Use these rules to mechanically translate any ERD into DDL.

| ERD Element | SQL Artifact |
|---|---|
| Entity | CREATE TABLE |
| Attribute | Column definition |
| Primary key attribute | PRIMARY KEY constraint |
| One-to-many relationship | FOREIGN KEY in the "many" table referencing the "one" table |
| Many-to-many relationship | Junction table with composite PK and two FKs |
| Identifying relationship | Child PK includes parent PK as a component |
| Non-identifying relationship | Child has independent PK; parent key appears as FK only |
| Mandatory participation (total) | NOT NULL on FK column |
| Optional participation (partial) | NULL allowed on FK column |

---

### 6. GCP Schema Design Comparison

| Scenario | Service | Schema Approach | Normalization |
|---|---|---|---|
| Regional OLTP, lift-and-shift migration | Cloud SQL | Standard 3NF relational | Full 3NF recommended |
| Global OLTP, financial transactions | Cloud Spanner | 3NF with interleaved tables for performance | 3NF with Spanner-specific physical design |
| High-performance PostgreSQL OLTP | AlloyDB | Standard 3NF relational | Full 3NF recommended |
| Analytics, BI reporting, data warehouse | BigQuery | Denormalized wide tables or nested STRUCT/ARRAY | Controlled denormalization |
| Mobile/web app, flexible schema | Firestore | Document model — no normalization applies | Schema-less, document structure |

---

### 7. Common Exam Trap Scenarios

Scenario: A table has a composite primary key (employee_id, skill_id). The column skill_description depends only on skill_id. This violates Second Normal Form because skill_description has a partial dependency on the composite key.

Scenario: An employees table stores employee_id, manager_id, and manager_name. The manager_name depends on manager_id, not on employee_id. This violates Third Normal Form through a transitive dependency.

Scenario: An orders table stores customer_id and customer_address. Customer_address depends on customer_id. This is a transitive dependency — customer_address should live in a customers table, not in orders.

Scenario: A products table cell contains "red, blue, green" as color options in a single column. This violates First Normal Form because the value is not atomic.

---

### 8. Required Readings and Resources

**Database Design by Adrienne Watt (BCcampus OpenEd)**: Read the chapters covering functional dependencies, normalization, and entity-relationship modeling. Available at opentextbc.ca/dbdesign01 at no cost.

**GCP Documentation — Cloud SQL Schema Design Best Practices**: Review the Cloud SQL documentation on schema design for MySQL and PostgreSQL instances. Available at cloud.google.com/learn.

**GCP Documentation — Cloud Spanner Schema Design**: Review the Spanner-specific design guidance including interleaved tables and primary key selection. Available at cloud.google.com/learn.

---

### 9. Exam Tips

Tip 1: When a question describes a non-key attribute that depends on part of a composite key, the answer is a 2NF violation. The fix is always to move that attribute to a separate table keyed on the partial determinant.

Tip 2: When a question describes a non-key attribute that depends on another non-key attribute, the answer is a 3NF violation. The fix is always to extract the transitively dependent column into its own table.

Tip 3: Many-to-many relationships are always resolved with a junction table in relational implementations. If an ERD shows M:N cardinality, the SQL schema will have a bridge table.

Tip 4: BigQuery supports nested and repeated fields (STRUCT and ARRAY types) to represent one-to-many relationships without a separate table. This is the BigQuery alternative to junction tables and is tested in the analytics domain.

Tip 5: Cloud Spanner interleaved tables physically co-locate child rows with parent rows to reduce cross-server lookups in a distributed system. This is a physical storage optimization — the logical relationship is still one-to-many and the schema design principles remain the same.

Tip 6: The difference between a surrogate key and a natural key matters in migration scenarios. If a natural key is an email address that can change, using it as a primary key in Cloud SQL will require cascading updates across all foreign key references. A surrogate integer key is immune to this problem.

Tip 7: BCNF is tested by definition only on the exam. Know that it is a stricter form of 3NF where every functional dependency determinant must be a superkey. Most 3NF tables are automatically in BCNF.

Tip 8: The three types of anomalies — update, insertion, and deletion — each have a clear definition. Update anomaly: same fact in multiple places causes contradictions. Insertion anomaly: cannot add a fact without adding an unrelated fact. Deletion anomaly: deleting one fact destroys an unrelated fact. Memorize these — they appear in GCP exam scenarios about poor schema design.

---

### 10. Study Checklist

- State the definition of a functional dependency and give two examples from a business schema
- Identify a 1NF violation given an example table with multi-valued cells or repeating column groups
- Identify a 2NF violation given a table with a composite primary key
- Identify a 3NF violation given a table with a transitive dependency chain
- Complete the normalization worked example from Section 3 without looking at the solution
- Translate a four-entity ERD into CREATE TABLE statements with all appropriate constraints
- Explain the difference between an identifying and a non-identifying relationship
- Explain why BigQuery uses denormalized schemas while Cloud SQL uses normalized schemas
- Complete the Module 02 lab activity
- Pass the Module 02 quiz with at least 80 percent

---

Reference: cloud.google.com/learn

---

## 9. Supplemental Resources

**1. Database Normalization — PostgreSQL Wiki**
https://wiki.postgresql.org/wiki/Don%27t_Do_This
A community-maintained guide covering common PostgreSQL schema anti-patterns, including denormalization pitfalls and constraint misuse, grounded in normalization principles.

**2. Crow's Foot Notation Reference — Lucidchart Documentation**
https://www.lucidchart.com/pages/er-diagrams
Explains ERD symbols including Crow's Foot cardinality markers, entity types, and relationship notation with visual examples for practice.

**3. Google Cloud — Choosing Between Cloud SQL and Cloud Spanner**
https://cloud.google.com/blog/topics/developers-practitioners/choosing-between-cloud-sql-and-cloud-spanner
Discusses schema design trade-offs when selecting between Cloud SQL and Cloud Spanner, including how normalization and interleaving factor into Google Cloud architecture decisions.
