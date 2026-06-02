# Video Script: Module 09 - Relational Databases with PostgreSQL

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 23 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code, psql terminal, pgAdmin or TablePlus
- Use [SHOW CODE] for VS Code; [SHOW TERMINAL] for psql; [SHOW BROWSER] for Postman/Thunder Client
- Install PostgreSQL locally before recording
- Have a `bookstore` database pre-created; show the psql commands live

---

## Section 1: Introduction - Why Databases? [00:00 - 04:00]

Welcome to Module 09. I am Professor Nash. For the last two modules we have stored data in memory — JavaScript arrays that reset every time the server restarts. That is fine for learning Express syntax. It is completely unusable in a real application.

Databases persist data. They survive server restarts, handle concurrent access from multiple users, enforce data integrity, and support complex queries that would be impractical with in-memory arrays.

We are learning PostgreSQL — a relational database. Relational databases organize data into tables with rows and columns, relationships between tables using foreign keys, and enforce constraints that guarantee data quality. PostgreSQL is open source, battle-tested, and one of the most widely deployed databases in production systems.

[SHOW TERMINAL]

Let me verify PostgreSQL is installed:

```bash
psql --version
```

And connect to the PostgreSQL server:

```bash
psql -U postgres
```

You should see the `postgres=#` prompt. This is the psql interactive terminal — the command-line interface to PostgreSQL.

**AWS Exam Tip:** Amazon RDS for PostgreSQL is a managed PostgreSQL service on AWS. It handles backups, patching, Multi-AZ failover, and read replicas. DVA-C02 tests when to use RDS (structured relational data with SQL queries) versus DynamoDB (key-value and document data with predictable access patterns). Know the difference.

---

## Section 2: Database Design and SQL [04:00 - 09:30]

[SHOW TERMINAL]

Let us create a database for the bookstore:

```sql
CREATE DATABASE bookstore;
\c bookstore
```

Now create the tables. The `\c bookstore` command connects to the new database.

```sql
CREATE TABLE authors (
  id        SERIAL PRIMARY KEY,
  name      VARCHAR(255) NOT NULL,
  country   VARCHAR(100),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE books (
  id          SERIAL PRIMARY KEY,
  title       VARCHAR(255) NOT NULL,
  author_id   INTEGER REFERENCES authors(id) ON DELETE CASCADE,
  year        INTEGER CHECK (year BETWEEN 1000 AND 2100),
  genre       VARCHAR(100),
  created_at  TIMESTAMPTZ DEFAULT NOW()
);
```

Key concepts in this schema:

- `SERIAL PRIMARY KEY` — auto-incrementing integer; PostgreSQL assigns the ID automatically
- `VARCHAR(255) NOT NULL` — text column that cannot be empty
- `REFERENCES authors(id)` — foreign key constraint; every `author_id` in books must exist in authors
- `ON DELETE CASCADE` — when an author is deleted, all their books are deleted automatically
- `CHECK (year BETWEEN 1000 AND 2100)` — rejects invalid year values at the database level

Insert some seed data:

```sql
INSERT INTO authors (name, country) VALUES
  ('Robert C. Martin', 'USA'),
  ('Andy Hunt', 'USA'),
  ('Kyle Simpson', 'USA');

INSERT INTO books (title, author_id, year, genre) VALUES
  ('Clean Code', 1, 2008, 'Software Engineering'),
  ('The Pragmatic Programmer', 2, 1999, 'Software Engineering'),
  ('You Don''t Know JS', 3, 2015, 'JavaScript');
```

Note the `''` (double single-quote) to escape an apostrophe inside a string literal.

Query with a JOIN:

```sql
SELECT b.id, b.title, b.year, a.name AS author
FROM books b
INNER JOIN authors a ON a.id = b.author_id
ORDER BY b.year;
```

[SHOW CODE]

This JOIN returns a combined result set — the book columns and the author name in the same row. This is how relational data is retrieved.

---

## Section 3: Connecting Node.js to PostgreSQL with node-postgres [09:30 - 15:00]

[SHOW CODE]

The `pg` package (node-postgres) is the official PostgreSQL driver for Node.js.

```bash
npm install pg dotenv
```

Create a `db.js` file that exports a connection pool:

```javascript
// db.js
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host:     process.env.DB_HOST     || 'localhost',
  port:     parseInt(process.env.DB_PORT) || 5432,
  database: process.env.DB_NAME     || 'bookstore',
  user:     process.env.DB_USER     || 'postgres',
  password: process.env.DB_PASSWORD || '',
  max: 10,          // maximum connections in the pool
  idleTimeoutMillis: 30000
});

pool.on('error', (err) => {
  console.error('PostgreSQL pool error:', err);
});

module.exports = pool;
```

Create a `.env` file with your local database credentials:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bookstore
DB_USER=postgres
DB_PASSWORD=yourpassword
```

Never commit `.env` to version control. It contains database credentials.

Now update `routes/books.js` to query the database instead of the in-memory array:

```javascript
const pool = require('../db');

// GET /api/books — list all books with author name
router.get('/', async (req, res, next) => {
  try {
    const result = await pool.query(`
      SELECT b.id, b.title, b.year, b.genre, a.name AS author
      FROM books b
      INNER JOIN authors a ON a.id = b.author_id
      ORDER BY b.title
    `);
    res.status(200).json(result.rows);
  } catch (err) {
    next(err);
  }
});
```

The key change: route handlers are now `async` functions, `pool.query()` is awaited, errors are forwarded with `next(err)`.

---

## Section 4: Parameterized Queries and CRUD [15:00 - 19:30]

[SHOW CODE]

Never concatenate user input into SQL strings. This is the SQL injection vulnerability. Use parameterized queries — PostgreSQL's driver handles escaping automatically.

```javascript
// GET /api/books/:id — parameterized query
router.get('/:id', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT b.*, a.name AS author FROM books b JOIN authors a ON a.id = b.author_id WHERE b.id = $1',
      [req.params.id]  // $1 is replaced by the first array element — safely
    );
    if (rows.length === 0) {
      return res.status(404).json({ error: 'Book not found', code: 'BOOK_NOT_FOUND' });
    }
    res.status(200).json(rows[0]);
  } catch (err) {
    next(err);
  }
});

// POST /api/books — insert and return the new row
router.post('/', requireFields(['title', 'author_id']), async (req, res, next) => {
  try {
    const { title, author_id, year, genre } = req.body;
    const { rows } = await pool.query(
      'INSERT INTO books (title, author_id, year, genre) VALUES ($1, $2, $3, $4) RETURNING *',
      [title, author_id, year, genre]
    );
    res.status(201)
      .set('Location', `/api/books/${rows[0].id}`)
      .json(rows[0]);
  } catch (err) {
    next(err);
  }
});

// DELETE /api/books/:id
router.delete('/:id', async (req, res, next) => {
  try {
    const { rowCount } = await pool.query(
      'DELETE FROM books WHERE id = $1',
      [req.params.id]
    );
    if (rowCount === 0) {
      return res.status(404).json({ error: 'Book not found' });
    }
    res.status(204).send();
  } catch (err) {
    next(err);
  }
});
```

The `RETURNING *` clause in the INSERT statement returns the newly created row — including the database-assigned `id` and `created_at` — without requiring a second SELECT query.

**AWS Exam Tip:** When a Node.js Lambda function connects to RDS, it should use a connection pool. However, Lambda's stateless execution model means the pool is re-created on cold starts. Use RDS Proxy (an AWS managed connection pooler) to avoid connection exhaustion when Lambda scales horizontally. DVA-C02 tests this RDS Proxy use case.

---

## Section 5: Transactions and Lab Preview [19:30 - 23:00]

[SHOW CODE]

A transaction groups multiple database operations into an atomic unit — all succeed or all fail together.

```javascript
// Transfer: deduct from one account, add to another — atomically
const transfer = async (fromId, toId, amount) => {
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
    client.release();
  }
};
```

The pattern: `BEGIN` → operations → `COMMIT` on success, `ROLLBACK` on error, `client.release()` in `finally`. Always release the client back to the pool.

In the lab this week you will set up a local PostgreSQL database, create the authors and books tables, seed the data, replace the in-memory arrays in your Express server with database queries, and test all CRUD endpoints. You will also verify that your SQL injection protection works by testing with Thunder Client.

Thank you for watching. See you in Module 10 where we explore MongoDB — a document database with a very different data model.

---

## Additional Resources

- developer.mozilla.org — search "PostgreSQL" and "node-postgres" for driver documentation
- aws.amazon.com/certification — review RDS and RDS Proxy documentation for DVA-C02 exam preparation
