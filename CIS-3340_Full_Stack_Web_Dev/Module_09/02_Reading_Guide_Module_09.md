# Reading Guide: Module 09 - Relational Databases with PostgreSQL

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
