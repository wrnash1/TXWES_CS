# Lab 09: PostgreSQL Integration with Express

**Course:** CIS-3340 Full Stack Web Development
**Module:** 09 - Relational Databases with PostgreSQL
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will connect the Express bookstore server from Module 08 to a real PostgreSQL database. You will create the database schema, seed data, replace in-memory arrays with async database queries, and verify SQL injection protection. By the end you will have a persistent, database-backed REST API.

---

## Prerequisites

- PostgreSQL installed locally (version 14 or higher — run `psql --version` to verify)
- Completion of Lab 08 (or the provided starter code)
- VS Code with Thunder Client or Postman

---

## Part 1: Database Setup

### Step 1: Create the Database and Tables

Open a terminal and connect to the PostgreSQL server:

```bash
psql -U postgres
```

Run the following SQL to create the database, connect to it, and create the tables:

```sql
CREATE DATABASE bookstore;
\c bookstore

CREATE TABLE authors (
  id         SERIAL PRIMARY KEY,
  name       VARCHAR(255) NOT NULL,
  country    VARCHAR(100),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE books (
  id         SERIAL PRIMARY KEY,
  title      VARCHAR(255) NOT NULL,
  author_id  INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
  year       INTEGER CHECK (year BETWEEN 1000 AND 2100),
  genre      VARCHAR(100),
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

Verify the tables were created:

```sql
\dt
```

You should see both `authors` and `books` in the output. Screenshot this terminal output.

### Step 2: Seed the Database

Run this SQL to insert the initial data:

```sql
INSERT INTO authors (name, country) VALUES
  ('Robert C. Martin', 'USA'),
  ('Andy Hunt', 'USA'),
  ('Kyle Simpson', 'USA'),
  ('Martin Fowler', 'UK');

INSERT INTO books (title, author_id, year, genre) VALUES
  ('Clean Code', 1, 2008, 'Software Engineering'),
  ('The Pragmatic Programmer', 2, 1999, 'Software Engineering'),
  ('You Don''t Know JS', 3, 2015, 'JavaScript'),
  ('Refactoring', 4, 1999, 'Software Engineering');
```

Verify the seed data with a JOIN query:

```sql
SELECT b.id, b.title, b.year, b.genre, a.name AS author
FROM books b
INNER JOIN authors a ON a.id = b.author_id
ORDER BY b.year;
```

Screenshot the query result. You should see 4 rows.

---

## Part 2: Connect Node.js to PostgreSQL

### Step 3: Install Dependencies

In your `lab08-express` project folder (copy it to `lab09-postgres` first):

```bash
npm install pg dotenv
```

### Step 4: Create db.js

Create a file called `db.js` in the project root:

```javascript
// db.js
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host:     process.env.DB_HOST     || 'localhost',
  port:     parseInt(process.env.DB_PORT) || 5432,
  database: process.env.DB_NAME     || 'bookstore',
  user:     process.env.DB_USER     || 'postgres',
  password: process.env.DB_PASSWORD || ''
});

pool.on('error', (err) => {
  console.error('Unexpected PostgreSQL error:', err.message);
});

// TODO 1: Export the pool so route files can import it
module.exports = /* YOUR CODE HERE */;
```

Complete TODO 1 — export the pool object.

### Step 5: Create .env

Create a `.env` file in the project root. Fill in your actual PostgreSQL credentials:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bookstore
DB_USER=postgres
DB_PASSWORD=
```

Verify that `.env` is listed in `.gitignore`. If it is not, add it now.

### Step 6: Add dotenv to index.js

At the very top of `index.js`, add:

```javascript
require('dotenv').config();
```

This must be the first line — before any other `require()` calls — so that `process.env` variables are available when `db.js` is loaded.

---

## Part 3: Implement Database-Backed Routes

### Step 7: Update routes/books.js

Replace the in-memory array implementation with database queries. The file structure stays the same — only the route handler bodies change.

Start with the GET all books route:

```javascript
const pool = require('../db');

// TODO 2: GET / — query the database for all books with author name
// Use a JOIN between books and authors tables
// Return status 200 with the rows array
router.get('/', async (req, res, next) => {
  try {
    // YOUR CODE HERE
  } catch (err) {
    next(err);
  }
});
```

The SQL query should select `b.id`, `b.title`, `b.year`, `b.genre`, and `a.name AS author` with an INNER JOIN on `author_id`. Order by `b.title`.

Implement the remaining routes using this template:

```javascript
// TODO 3: GET /:id — find one book by id using $1 parameter
// Return 404 if rows.length === 0
router.get('/:id', async (req, res, next) => {
  try {
    // YOUR CODE HERE
  } catch (err) {
    next(err);
  }
});

// TODO 4: POST / — insert a new book; use RETURNING * to get the created row
// Required fields: title, author_id (already validated by requireFields middleware)
router.post('/', requireFields(['title', 'author_id']), async (req, res, next) => {
  try {
    // YOUR CODE HERE
  } catch (err) {
    next(err);
  }
});

// TODO 5: PUT /:id — update title, year, genre; use RETURNING *
// Return 404 if rowCount === 0
router.put('/:id', requireFields(['title']), async (req, res, next) => {
  try {
    // YOUR CODE HERE
  } catch (err) {
    next(err);
  }
});

// TODO 6: DELETE /:id — delete by id; return 204 on success, 404 if rowCount === 0
router.delete('/:id', async (req, res, next) => {
  try {
    // YOUR CODE HERE
  } catch (err) {
    next(err);
  }
});
```

### Step 8: Update routes/authors.js

Replace the in-memory authors array with database queries. Implement these three routes:

```javascript
// GET / — all authors
// GET /:id — one author or 404
// POST / — insert author with RETURNING *
```

Use `requireFields(['name'])` on the POST route.

---

## Part 4: Add a Nested Route

### Step 9: Get Books by Author

Add this route to `routes/authors.js` after the existing routes:

```javascript
// GET /api/authors/:authorId/books — list books by a specific author
router.get('/:authorId/books', async (req, res, next) => {
  try {
    // TODO 7: First verify the author exists; return 404 if not found.
    // Then query books WHERE author_id = $1.
    // Return status 200 with the books array.
  } catch (err) {
    next(err);
  }
});
```

Complete TODO 7. The route should:

1. Query `SELECT * FROM authors WHERE id = $1` with `req.params.authorId`
2. Return `404` if the author is not found
3. Query `SELECT * FROM books WHERE author_id = $1 ORDER BY year` with the author ID
4. Return `200` with the books array

---

## Part 5: Test All Endpoints

### Step 10: Verify the API

Start the server with `npm run dev`. Test each endpoint with Thunder Client:

| Request | Expected Status | Notes |
|---|---|---|
| `GET /api/books` | 200 | Returns 4 books with author names |
| `GET /api/books/1` | 200 | Returns Clean Code |
| `GET /api/books/999` | 404 | Error object |
| `POST /api/books` (valid) | 201 | `author_id: 1` in body; Location header present |
| `POST /api/books` (missing title) | 400 | Validation error |
| `PUT /api/books/1` | 200 | Updated book returned |
| `DELETE /api/books/4` | 204 | Empty body |
| `DELETE /api/books/4` again | 404 | Already deleted |
| `GET /api/authors` | 200 | Returns 4 authors |
| `GET /api/authors/1/books` | 200 | Returns books by Robert C. Martin |
| `GET /api/authors/999/books` | 404 | Author not found |

Screenshot each response.

### Step 11: Verify SQL Injection Protection

In Thunder Client, send a GET request to:

```text
GET /api/books/1'; DROP TABLE books; --
```

The server should return `404 Not Found` (not a server error). The parameterized query treats the entire string as a data value, not SQL. Screenshot the response.

---

## Deliverables

Submit to Canvas:

1. `db.js` — pool configuration file
2. `routes/books.js` — database-backed books routes
3. `routes/authors.js` — database-backed authors routes including nested route
4. `.env` — with your credentials (note: in a real project never submit this; exception for this lab only for grading)
5. Screenshot: `\dt` output showing both tables in psql
6. Screenshot: JOIN query result in psql showing 4 seeded books
7. Thunder Client screenshots for all 11 test cases
8. Screenshot: SQL injection test returning 404 (not 500)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Database schema created with correct constraints (PK, FK, NOT NULL, CHECK) | 10 |
| `db.js` exports Pool with credentials from environment variables | 10 |
| `GET /api/books` returns books with author names (JOIN query) | 10 |
| `GET /api/books/:id` returns correct 200 or 404 | 5 |
| `POST /api/books` inserts and returns new row with RETURNING * | 15 |
| `PUT /api/books/:id` updates and returns row or 404 | 10 |
| `DELETE /api/books/:id` returns 204 or 404 using rowCount | 10 |
| Authors routes (GET all, GET one, POST) database-backed | 10 |
| Nested route `GET /api/authors/:authorId/books` functional | 10 |
| SQL injection test returns 404 (not 500 or server error) | 5 |
| psql screenshots showing schema and seed data | 5 |
| **Total** | **100** |
