# Lab 08: Express Router and Custom Middleware

**Course:** CIS-3340 Full Stack Web Development
**Module:** 08 - Server-Side Routing & Middleware
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will refactor the single-file bookstore server from Module 07 into a structured, production-ready Express application using Express Router and custom middleware. You will also add a second resource (authors), configure CORS, and implement a reusable validation middleware factory.

---

## Prerequisites

- Completion of Lab 07 (working single-file Express server)
- VS Code with Thunder Client or Postman installed
- Node.js 18 or higher

---

## Starter Code

Copy your `lab07-express` folder and rename it `lab08-express`. You will refactor this code rather than starting from scratch. All changes are made to the existing files and new files are added.

If you did not complete Lab 07, use this minimal `index.js` as your starting point:

```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;
app.use(express.json());

let books = [
  { id: 1, title: 'Clean Code', author: 'Robert C. Martin', year: 2008 },
  { id: 2, title: 'The Pragmatic Programmer', author: 'Hunt & Thomas', year: 1999 },
  { id: 3, title: "You Don't Know JS", author: 'Kyle Simpson', year: 2015 }
];
let nextId = 4;

app.get('/api/books', (req, res) => res.status(200).json(books));
app.get('/api/books/:id', (req, res) => {
  const book = books.find(b => b.id === parseInt(req.params.id));
  if (!book) return res.status(404).json({ error: 'Book not found' });
  res.status(200).json(book);
});
app.post('/api/books', (req, res) => {
  const { title, author } = req.body;
  if (!title || !author) return res.status(400).json({ error: 'title and author required' });
  const newBook = { id: nextId++, ...req.body };
  books.push(newBook);
  res.status(201).set('Location', `/api/books/${newBook.id}`).json(newBook);
});
app.put('/api/books/:id', (req, res) => {
  const index = books.findIndex(b => b.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'Not found' });
  books[index] = { id: parseInt(req.params.id), ...req.body };
  res.status(200).json(books[index]);
});
app.delete('/api/books/:id', (req, res) => {
  const index = books.findIndex(b => b.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'Not found' });
  books.splice(index, 1);
  res.status(204).send();
});
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

---

## Part 1: Create the Middleware Files

### Step 1: Create the Request Logger

Create the folder `middleware/` in the project root. Inside it, create `logger.js`:

```javascript
// middleware/logger.js

const requestLogger = (req, res, next) => {
  const start = Date.now();
  const timestamp = new Date().toISOString();

  res.on('finish', () => {
    const duration = Date.now() - start;
    // TODO 1: Log the following fields separated by spaces:
    //   timestamp, req.method, req.path, res.statusCode, duration + 'ms'
    // Example output: [2025-09-22T14:01:00.000Z] GET /api/books 200 12ms
    console.log(/* YOUR CODE HERE */);
  });

  next();
};

module.exports = requestLogger;
```

Fill in the `console.log()` call inside the `finish` event handler.

### Step 2: Create the Validation Middleware Factory

Create `middleware/validate.js`:

```javascript
// middleware/validate.js

// requireFields takes an array of field names and returns a middleware function.
// The middleware checks req.body for each field. If any are missing or empty,
// it responds with 400 and a structured error. Otherwise it calls next().
const requireFields = (fields) => {
  return (req, res, next) => {
    // TODO 2: Filter fields to find those that are undefined or empty string in req.body
    const missing = /* YOUR CODE HERE */;

    if (missing.length > 0) {
      return res.status(400).json({
        error: 'Validation failed',
        code: 'MISSING_REQUIRED_FIELDS',
        details: missing.map(f => ({ field: f, message: `${f} is required` }))
      });
    }

    next();
  };
};

module.exports = { requireFields };
```

Complete the `missing` assignment on TODO 2.

---

## Part 2: Create the Books Router

### Step 3: Create routes/books.js

Create the folder `routes/` and inside it create `books.js`. This file receives the books array and nextId counter from `index.js` via a factory function pattern — this keeps the data accessible from both the router and `index.js`:

```javascript
// routes/books.js
const express = require('express');
const { requireFields } = require('../middleware/validate');

const router = express.Router();

// Shared data — populated by the factory function in index.js
let books;
let nextId;

// Factory: call this once from index.js to inject the data store
const init = (booksArray, startId) => {
  books = booksArray;
  nextId = startId;
};

// TODO 3: GET / — return all books; support optional ?author= and ?year= query filters
router.get('/', (req, res) => {
  // YOUR CODE HERE
});

// TODO 4: GET /:id — return one book or 404
router.get('/:id', (req, res) => {
  // YOUR CODE HERE
});

// POST / — create a book (validation provided)
router.post('/', requireFields(['title', 'author']), (req, res) => {
  const { title, author, year } = req.body;
  const newBook = { id: nextId++, title, author, year: year || null };
  books.push(newBook);
  res.status(201).set('Location', `/api/books/${newBook.id}`).json(newBook);
});

// TODO 5: PUT /:id — replace a book entirely, 404 if not found
router.put('/:id', requireFields(['title', 'author']), (req, res) => {
  // YOUR CODE HERE
});

// TODO 6: DELETE /:id — remove a book, 204 if success, 404 if not found
router.delete('/:id', (req, res) => {
  // YOUR CODE HERE
});

module.exports = { router, init };
```

Complete TODOs 3 through 6. For TODO 3, filter the books array using `req.query.author` (case-insensitive substring match) and `req.query.year` (exact match after `parseInt`).

---

## Part 3: Create the Authors Router

### Step 4: Create routes/authors.js

Create `routes/authors.js` with this complete implementation — no TODOs here, read it carefully to understand the pattern:

```javascript
// routes/authors.js
const express = require('express');
const { requireFields } = require('../middleware/validate');

const router = express.Router();

let authors = [
  { id: 1, name: 'Robert C. Martin', country: 'USA' },
  { id: 2, name: 'Andrew Hunt', country: 'USA' },
  { id: 3, name: 'Kyle Simpson', country: 'USA' }
];
let nextId = 4;

// GET /api/authors
router.get('/', (req, res) => {
  res.status(200).json(authors);
});

// GET /api/authors/:id
router.get('/:id', (req, res) => {
  const author = authors.find(a => a.id === parseInt(req.params.id));
  if (!author) return res.status(404).json({ error: 'Author not found', code: 'AUTHOR_NOT_FOUND' });
  res.status(200).json(author);
});

// POST /api/authors
router.post('/', requireFields(['name']), (req, res) => {
  const newAuthor = { id: nextId++, ...req.body };
  authors.push(newAuthor);
  res.status(201).set('Location', `/api/authors/${newAuthor.id}`).json(newAuthor);
});

// DELETE /api/authors/:id
router.delete('/:id', (req, res) => {
  const index = authors.findIndex(a => a.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'Author not found' });
  authors.splice(index, 1);
  res.status(204).send();
});

module.exports = router;
```

---

## Part 4: Refactor index.js

### Step 5: Rewrite index.js

Replace the entire contents of `index.js` with the refactored version. Fill in the three TODOs:

```javascript
const express = require('express');
const cors = require('cors');
const requestLogger = require('./middleware/logger');
const { router: booksRouter, init: initBooks } = require('./routes/books');
const authorsRouter = require('./routes/authors');

const app = express();
const PORT = process.env.PORT || 3000;

// ─── Initial data ────────────────────────────────────────────────────────────
const books = [
  { id: 1, title: 'Clean Code', author: 'Robert C. Martin', year: 2008 },
  { id: 2, title: 'The Pragmatic Programmer', author: 'Hunt & Thomas', year: 1999 },
  { id: 3, title: "You Don't Know JS", author: 'Kyle Simpson', year: 2015 }
];
initBooks(books, 4);

// ─── Global middleware ───────────────────────────────────────────────────────
// TODO 7: Register cors() allowing only http://localhost:3000 as the origin
app.use(/* YOUR CODE HERE */);

app.use(express.json());

// TODO 8: Register the requestLogger middleware
app.use(/* YOUR CODE HERE */);

// ─── Routers ─────────────────────────────────────────────────────────────────
// TODO 9: Mount booksRouter at /api/books and authorsRouter at /api/authors
app.use(/* YOUR CODE HERE */);
app.use(/* YOUR CODE HERE */);

// ─── 404 handler ─────────────────────────────────────────────────────────────
app.use((req, res) => {
  res.status(404).json({
    error: `${req.method} ${req.path} not found`,
    code: 'ROUTE_NOT_FOUND'
  });
});

// ─── Global error handler ────────────────────────────────────────────────────
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message || 'Internal server error',
    code: err.code || 'INTERNAL_ERROR'
  });
});

// ─── Start server ────────────────────────────────────────────────────────────
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

Install the cors package before running:

```bash
npm install cors
```

---

## Part 5: Test All Endpoints

### Step 6: Verify Books Routes

Using Thunder Client, test each books endpoint:

| Request | Expected Status | Notes |
|---|---|---|
| `GET /api/books` | 200 | Returns array of 3 books |
| `GET /api/books?author=Martin` | 200 | Returns 1 book (Clean Code) |
| `GET /api/books?year=1999` | 200 | Returns 1 book (Pragmatic Programmer) |
| `GET /api/books/1` | 200 | Returns single book |
| `GET /api/books/999` | 404 | Error object |
| `POST /api/books` (valid) | 201 | Location header present |
| `POST /api/books` (missing title) | 400 | details array with field name |
| `PUT /api/books/1` | 200 | Updated book |
| `DELETE /api/books/2` | 204 | Empty body |

### Step 7: Verify Authors Routes

| Request | Expected Status |
|---|---|
| `GET /api/authors` | 200 |
| `GET /api/authors/1` | 200 |
| `POST /api/authors` (valid) | 201 |
| `POST /api/authors` (missing name) | 400 |
| `DELETE /api/authors/3` | 204 |

### Step 8: Verify Middleware

Check the VS Code terminal after running the requests from Steps 6 and 7. Each request should produce a log line in this format:

```text
[2025-09-22T14:01:00.000Z] GET /api/books 200 8ms
[2025-09-22T14:01:03.452Z] POST /api/books 201 3ms
```

Screenshot the terminal showing at least five log entries with different methods and status codes.

---

## Deliverables

Submit to Canvas:

1. `index.js` — refactored orchestration file
2. `routes/books.js` — books router with TODOs completed
3. `routes/authors.js` — authors router
4. `middleware/logger.js` — completed logger
5. `middleware/validate.js` — completed validation factory
6. `package.json`
7. Screenshots from Thunder Client for books routes (all nine test cases)
8. Screenshots from Thunder Client for authors routes (all five test cases)
9. Screenshot of terminal showing middleware log output

---

## Grading Rubric

| Criterion | Points |
|---|---|
| `index.js` correctly mounts both routers with path prefixes | 10 |
| `index.js` registers CORS with origin restriction | 5 |
| `requestLogger` logs method, path, status code, and duration | 10 |
| `requireFields` factory returns correct 400 with details array | 15 |
| `GET /api/books` with `?author=` and `?year=` filters working | 10 |
| `GET /api/books/:id` returns correct 200 or 404 | 5 |
| `POST /api/books` returns 201 with Location header | 10 |
| `PUT /api/books/:id` replaces and returns 200 or 404 | 5 |
| `DELETE /api/books/:id` returns 204 or 404 | 5 |
| Authors router fully functional (all five endpoints) | 10 |
| Terminal screenshots showing logger output for 5+ requests | 5 |
| All fourteen Thunder Client screenshots captured | 5 |
| No verbs in URLs; correct status codes throughout | 5 |
| **Total** | **100** |
