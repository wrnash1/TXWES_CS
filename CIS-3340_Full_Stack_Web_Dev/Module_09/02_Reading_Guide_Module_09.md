# Reading Guide: Module 09 - Relational Databases with PostgreSQL

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3340 &BULL; FULL STACK WEB DEVELOPMENT</text>
    
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


**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module introduces PostgreSQL — a relational database — and the `pg` (node-postgres) driver for connecting a Node.js/Express application to it. You will design a database schema, write SQL queries, implement CRUD operations with parameterized queries, and handle transactions. These skills apply directly to Module 14 (AWS RDS deployment) and the DVA-C02 certification.

---

## 1. Relational Database Concepts

A relational database organizes data into tables. Each table has:

- Columns (fields) with defined data types and constraints
- Rows (records) containing one entry per row
- A primary key column that uniquely identifies each row
- Optional foreign key columns that reference rows in other tables

### Key Constraints

| Constraint | Purpose |
|---|---|
| `PRIMARY KEY` | Uniquely identifies each row; implies NOT NULL and UNIQUE |
| `NOT NULL` | Column cannot be null |
| `UNIQUE` | No two rows may have the same value in this column |
| `FOREIGN KEY REFERENCES` | Value must exist as a primary key in the referenced table |
| `CHECK` | Value must satisfy a boolean expression |
| `DEFAULT` | Provides a fallback value when no value is supplied |

---

## 2. PostgreSQL Data Types

| Type | Use Case |
|---|---|
| `SERIAL` | Auto-incrementing integer (use for primary keys) |
| `INTEGER` | Whole numbers |
| `NUMERIC(p, s)` | Exact decimal (use for money — never `FLOAT`) |
| `VARCHAR(n)` | Variable-length string up to n characters |
| `TEXT` | Unlimited-length string |
| `BOOLEAN` | True/false |
| `TIMESTAMPTZ` | Timestamp with timezone (use this — not `TIMESTAMP`) |
| `DATE` | Date without time |
| `JSONB` | Binary JSON (indexable; preferred over `JSON`) |

---

## 3. Schema Design

### Creating Tables

```sql
CREATE TABLE authors (
  id          SERIAL PRIMARY KEY,
  name        VARCHAR(255) NOT NULL,
  country     VARCHAR(100),
  created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE books (
  id          SERIAL PRIMARY KEY,
  title       VARCHAR(255) NOT NULL,
  author_id   INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
  year        INTEGER CHECK (year BETWEEN 1000 AND 2100),
  genre       VARCHAR(100),
  created_at  TIMESTAMPTZ DEFAULT NOW()
);
```

### ON DELETE Behavior

| Option | Behavior when referenced row is deleted |
|---|---|
| `ON DELETE CASCADE` | Child rows are automatically deleted |
| `ON DELETE SET NULL` | Foreign key column is set to NULL |
| `ON DELETE RESTRICT` | Deletion is blocked if child rows exist (default) |

### Indexes

```sql
CREATE INDEX idx_books_author_id ON books(author_id);
CREATE INDEX idx_books_genre ON books(genre);
```

Indexes speed up `WHERE`, `JOIN ON`, and `ORDER BY` operations on the indexed column. They slightly slow down INSERT/UPDATE/DELETE.

---

## 4. SQL CRUD Operations

### SELECT

```sql
-- All rows
SELECT * FROM books;

-- Specific columns with alias
SELECT b.id, b.title, b.year, a.name AS author
FROM books b
INNER JOIN authors a ON a.id = b.author_id;

-- Filter and sort
SELECT * FROM books WHERE genre = 'JavaScript' ORDER BY year DESC;

-- Aggregate
SELECT genre, COUNT(*) AS book_count FROM books GROUP BY genre;
```

### INSERT with RETURNING

```sql
-- Insert and return the new row
INSERT INTO books (title, author_id, year)
VALUES ('Refactoring', 1, 1999)
RETURNING *;
```

### UPDATE

```sql
UPDATE books SET genre = 'Software Engineering' WHERE id = 3;

-- Update and return the result
UPDATE books SET title = $1, year = $2 WHERE id = $3 RETURNING *;
```

### DELETE

```sql
DELETE FROM books WHERE id = 5;
```

---

## 5. JOIN Types

| JOIN Type | Returns |
|---|---|
| `INNER JOIN` | Rows where the join condition matches in both tables |
| `LEFT JOIN` | All left table rows; NULL for unmatched right table columns |
| `RIGHT JOIN` | All right table rows; NULL for unmatched left table columns |
| `FULL OUTER JOIN` | All rows from both tables; NULL where no match |

```sql
-- INNER JOIN: books with their author name
SELECT b.title, a.name
FROM books b
INNER JOIN authors a ON a.id = b.author_id;

-- LEFT JOIN: all authors, including those with no books
SELECT a.name, b.title
FROM authors a
LEFT JOIN books b ON b.author_id = a.id;
```

---

## 6. Connecting Node.js to PostgreSQL

### Installation

```bash
npm install pg dotenv
```

### Connection Pool (db.js)

```javascript
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host:     process.env.DB_HOST,
  port:     parseInt(process.env.DB_PORT) || 5432,
  database: process.env.DB_NAME,
  user:     process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  max: 10,
  idleTimeoutMillis: 30000
});

module.exports = pool;
```

### .env File

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bookstore
DB_USER=postgres
DB_PASSWORD=yourpassword
```

Add `.env` to `.gitignore`. Never commit credentials.

### Pool vs. Client

| Approach | When to Use |
|---|---|
| `pool.query(sql, params)` | Single queries — pool manages the connection |
| `pool.connect()` + `client` | Transactions — hold one connection across multiple queries |

---

## 7. Parameterized Queries

Always use parameterized queries with user input. Never concatenate strings.

```javascript
// CORRECT — parameterized
const { rows } = await pool.query(
  'SELECT * FROM books WHERE id = $1',
  [req.params.id]
);

// WRONG — SQL injection vulnerability
const { rows } = await pool.query(
  `SELECT * FROM books WHERE id = ${req.params.id}`
);
```

The `pg` driver replaces `$1`, `$2`, etc. with the values from the second argument array, treating them as data and never as SQL syntax.

### Node-postgres Result Object

```javascript
const result = await pool.query('SELECT * FROM books');

result.rows        // array of row objects
result.rowCount    // number of rows affected or returned
result.fields      // column metadata
```

---

## 8. Async Route Handlers

```javascript
router.get('/', async (req, res, next) => {
  try {
    const { rows } = await pool.query('SELECT * FROM books ORDER BY title');
    res.status(200).json(rows);
  } catch (err) {
    next(err);
  }
});

// POST with RETURNING
router.post('/', requireFields(['title', 'author_id']), async (req, res, next) => {
  try {
    const { title, author_id, year, genre } = req.body;
    const { rows } = await pool.query(
      'INSERT INTO books (title, author_id, year, genre) VALUES ($1, $2, $3, $4) RETURNING *',
      [title, author_id, year, genre]
    );
    res.status(201).set('Location', `/api/books/${rows[0].id}`).json(rows[0]);
  } catch (err) {
    next(err);
  }
});

// DELETE with rowCount check
router.delete('/:id', async (req, res, next) => {
  try {
    const { rowCount } = await pool.query(
      'DELETE FROM books WHERE id = $1',
      [req.params.id]
    );
    if (rowCount === 0) return res.status(404).json({ error: 'Book not found' });
    res.status(204).send();
  } catch (err) {
    next(err);
  }
});
```

---

## 9. Transactions

Use transactions when multiple queries must all succeed or all fail together.

```javascript
const transferFunds = async (fromId, toId, amount) => {
  const client = await pool.connect();
  try {
    await client.query('BEGIN');
    await client.query(
      'UPDATE accounts SET balance = balance - $1 WHERE id = $2',
      [amount, fromId]
    );
    await client.query(
      'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
      [amount, toId]
    );
    await client.query('COMMIT');
  } catch (err) {
    await client.query('ROLLBACK');
    throw err;
  } finally {
    client.release(); // always release back to the pool
  }
};
```

---

## 10. AWS RDS for PostgreSQL

Amazon RDS for PostgreSQL is a managed database service:

- Automated backups with configurable retention
- Multi-AZ deployment for high availability
- Read replicas for horizontal read scaling
- VPC network isolation (not publicly accessible by default)

### RDS Proxy

Lambda functions create new connections on cold starts. At scale, this exhausts the database connection limit. RDS Proxy sits between Lambda and RDS, maintaining a connection pool:

```text
Lambda (many instances) → RDS Proxy (pools connections) → RDS (limited connections)
```

RDS Proxy is configured in AWS — no application code changes are required.

---

## 11. Exam and Interview Tips

1. `SERIAL` is shorthand for an auto-incrementing integer primary key. PostgreSQL 10+ also supports `GENERATED ALWAYS AS IDENTITY`.

2. `RETURNING *` in INSERT/UPDATE returns the affected row without a second query. This is a PostgreSQL extension.

3. Parameterized queries (`$1`, `$2`) are the required SQL injection prevention mechanism. String concatenation with user input is always wrong.

4. Use `pool.query()` for single queries and `pool.connect()` for transactions. Always call `client.release()` in `finally`.

5. `rowCount === 0` after DELETE means the row did not exist — return `404`. `rows.length === 0` after SELECT means not found.

6. `TIMESTAMPTZ` stores timestamps in UTC. Always use it instead of `TIMESTAMP` for application data.

7. Amazon RDS is for relational (SQL) workloads. DynamoDB is for NoSQL workloads. DVA-C02 tests this distinction frequently.

8. RDS Proxy prevents connection exhaustion when Lambda scales. This is a tested DVA-C02 pattern.

---

## 12. Study Checklist

- [ ] Create a PostgreSQL database and tables with psql
- [ ] Define a schema with PRIMARY KEY, FOREIGN KEY, NOT NULL, and CHECK constraints
- [ ] Write SELECT, INSERT, UPDATE, and DELETE queries
- [ ] Write a JOIN query combining two tables
- [ ] Connect Node.js to PostgreSQL using `pg` Pool
- [ ] Store credentials in `.env` and add `.env` to `.gitignore`
- [ ] Use parameterized queries for all user-supplied values
- [ ] Write async route handlers with `try/catch` and `next(err)`
- [ ] Use `RETURNING *` to retrieve the inserted row
- [ ] Implement a transaction with BEGIN/COMMIT/ROLLBACK
- [ ] Explain when to use RDS versus DynamoDB and what RDS Proxy solves

---

## 13. Supplemental Resources

The following free, open-access resources go deeper on Module 09 topics:

**1. PostgreSQL Official Documentation — Tutorial**
[https://www.postgresql.org/docs/current/tutorial.html](https://www.postgresql.org/docs/current/tutorial.html)
The official PostgreSQL tutorial covering SQL basics, table creation, constraints, joins, and transactions — directly aligned to the schema design and CRUD query sections in this reading guide and Lab 09.

**2. node-postgres (pg) Documentation**
[https://node-postgres.com/](https://node-postgres.com/)
The complete reference for the `pg` driver used to connect Node.js to PostgreSQL, covering Pool configuration, parameterized queries, transactions, and the result object fields (`rows`, `rowCount`) used in the async route handlers.

**3. MDN Web Docs — SQL injection**
[https://developer.mozilla.org/en-US/docs/Glossary/SQL_Injection](https://developer.mozilla.org/en-US/docs/Glossary/SQL_Injection)
A concise explanation of SQL injection attacks and why parameterized queries (`$1`, `$2`) are the required defense — reinforces the critical security principle that all user-supplied values must be passed as parameters, never interpolated into SQL strings.

**4. AWS Documentation — Amazon RDS for PostgreSQL**
[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
The official AWS guide for deploying PostgreSQL on RDS, covering Multi-AZ setup, automated backups, VPC configuration, and RDS Proxy — the managed deployment target for the Node.js/PostgreSQL application built in this module and deployed in Module 14.
