# Lab 07: Building a Node.js & Express REST API

**Course:** CIS-3340 Full Stack Web Development
**Module:** 07 - Node.js & Express Server
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will build a complete REST API for a bookstore application using Node.js and Express. You will initialize a project, install dependencies, implement all CRUD endpoints, add middleware, and test every route with Thunder Client or Postman. This is the implementation of the API you designed in Module 06.

---

## Prerequisites

- Node.js installed (version 18 or higher — run `node --version` to verify)
- VS Code with the Thunder Client extension, or Postman
- Completion of Module 06 Lab (API design document)

---

## Part 1: Project Setup

### Step 1: Initialize the Project

Open a terminal in VS Code. Create a new project folder and initialize it:

```bash
mkdir lab07-express
cd lab07-express
npm init -y
```

Verify that `package.json` was created. Then install dependencies:

```bash
npm install express
npm install --save-dev nodemon
```

Open `package.json` and update the `scripts` section to match this exactly:

```json
{
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  }
}
```

Create a `.gitignore` file in the project root with this content:

```text
node_modules/
.env
```

### Step 2: Create the Entry Point

Create `index.js` in the project root. This is the complete file — read through every section before running it:

```javascript
const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

// ─── Middleware ──────────────────────────────────────────────────────────────
app.use(express.json());

// Request logger — logs method, path, and timestamp for every request
const requestLogger = (req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
};
app.use(requestLogger);

// ─── In-memory data store ────────────────────────────────────────────────────
let books = [
  { id: 1, title: 'Clean Code', author: 'Robert C. Martin', year: 2008 },
  { id: 2, title: 'The Pragmatic Programmer', author: 'Hunt & Thomas', year: 1999 },
  { id: 3, title: "You Don't Know JS", author: 'Kyle Simpson', year: 2015 }
];
let nextId = 4;

// ─── Routes ──────────────────────────────────────────────────────────────────

// TODO 1: GET /api/books — return all books with status 200
// Replace this placeholder with your implementation
app.get('/api/books', (req, res) => {
  // YOUR CODE HERE
});

// TODO 2: GET /api/books/:id — return one book or 404
app.get('/api/books/:id', (req, res) => {
  // YOUR CODE HERE
});

// TODO 3: POST /api/books — create a book; validate title and author
// Return 400 if missing, 201 with Location header if successful
app.post('/api/books', (req, res) => {
  // YOUR CODE HERE
});

// TODO 4: PUT /api/books/:id — replace a book entirely or 404
app.put('/api/books/:id', (req, res) => {
  // YOUR CODE HERE
});

// TODO 5: DELETE /api/books/:id — remove a book; return 204 or 404
app.delete('/api/books/:id', (req, res) => {
  // YOUR CODE HERE
});

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
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Run the server:

```bash
npm run dev
```

The terminal should print `Server running on port 3000`. If you see `EADDRINUSE`, port 3000 is already in use — change the port in the URL for testing: `http://localhost:3001`.

---

## Part 2: Implement the Routes

### Step 3: GET /api/books (All Books)

Replace `TODO 1` with the implementation:

```javascript
app.get('/api/books', (req, res) => {
  res.status(200).json(books);
});
```

Test in Thunder Client: `GET http://localhost:3000/api/books`

Expected result:

- Status: `200 OK`
- Body: JSON array with three book objects

Screenshot the response panel.

### Step 4: GET /api/books/:id (Single Book)

Replace `TODO 2`:

```javascript
app.get('/api/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const book = books.find(b => b.id === id);

  if (!book) {
    return res.status(404).json({
      error: 'Book not found',
      code: 'BOOK_NOT_FOUND'
    });
  }

  res.status(200).json(book);
});
```

Test these two requests:

| Request | Expected Status |
|---|---|
| `GET /api/books/1` | 200 with book object |
| `GET /api/books/999` | 404 with error object |

Screenshot both responses.

### Step 5: POST /api/books (Create a Book)

Replace `TODO 3`:

```javascript
app.post('/api/books', (req, res) => {
  const { title, author, year } = req.body;

  if (!title || !author) {
    return res.status(400).json({
      error: 'title and author are required',
      code: 'MISSING_REQUIRED_FIELDS'
    });
  }

  const newBook = { id: nextId++, title, author, year: year || null };
  books.push(newBook);

  res.status(201)
    .set('Location', `/api/books/${newBook.id}`)
    .json(newBook);
});
```

Test with Thunder Client:

- Method: POST
- URL: `http://localhost:3000/api/books`
- Header: `Content-Type: application/json`
- Body:

```json
{
  "title": "Eloquent JavaScript",
  "author": "Marijn Haverbeke",
  "year": 2018
}
```

Expected result:

- Status: `201 Created`
- Response body includes the new book with an `id` of 4
- Response headers include `Location: /api/books/4`

Screenshot the response showing both the status code and the Location header.

Also test the validation case — send a POST body with no `title` field. Verify status is `400`.

### Step 6: PUT /api/books/:id (Replace a Book)

Replace `TODO 4`:

```javascript
app.put('/api/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = books.findIndex(b => b.id === id);

  if (index === -1) {
    return res.status(404).json({
      error: 'Book not found',
      code: 'BOOK_NOT_FOUND'
    });
  }

  const { title, author, year } = req.body;
  books[index] = { id, title, author, year };
  res.status(200).json(books[index]);
});
```

Test with Thunder Client:

- Method: PUT
- URL: `http://localhost:3000/api/books/1`
- Body:

```json
{
  "title": "Clean Code (2nd Edition)",
  "author": "Robert C. Martin",
  "year": 2024
}
```

Expected: status `200` and the updated book in the response body.

After the PUT, send `GET /api/books/1` and verify the title has changed.

### Step 7: DELETE /api/books/:id (Remove a Book)

Replace `TODO 5`:

```javascript
app.delete('/api/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = books.findIndex(b => b.id === id);

  if (index === -1) {
    return res.status(404).json({
      error: 'Book not found',
      code: 'BOOK_NOT_FOUND'
    });
  }

  books.splice(index, 1);
  res.status(204).send();
});
```

Test:

1. `DELETE /api/books/2` — expected status `204` with no response body
2. `DELETE /api/books/2` again — expected status `404` (already deleted)
3. `GET /api/books` — verify book with id 2 is gone

Screenshot each response.

---

## Part 3: Verify Middleware and Error Handling

### Step 8: Verify the Request Logger

While Thunder Client sends requests, watch the VS Code terminal. Every request should produce a log line like:

```text
[2025-09-15T14:23:01.443Z] GET /api/books
[2025-09-15T14:23:05.112Z] POST /api/books
```

Screenshot the terminal showing at least three log entries.

### Step 9: Test the 404 Catch-All

Send a request to a route that does not exist:

- `GET http://localhost:3000/api/nonexistent`

Expected: status `404` and body `{ "error": "GET /api/nonexistent not found", "code": "ROUTE_NOT_FOUND" }`.

Screenshot the response.

### Step 10: Final Verification

Send the following sequence of requests and capture the results in a summary table:

| Request | Expected Status | Verified |
|---|---|---|
| `GET /api/books` | 200 | |
| `GET /api/books/1` | 200 | |
| `GET /api/books/999` | 404 | |
| `POST /api/books` (valid body) | 201 | |
| `POST /api/books` (missing title) | 400 | |
| `PUT /api/books/1` | 200 | |
| `DELETE /api/books/3` | 204 | |
| `DELETE /api/books/3` (again) | 404 | |
| `GET /api/nonexistent` | 404 | |

---

## Deliverables

Submit to Canvas:

1. `index.js` — your complete implemented server file
2. `package.json` — showing correct scripts and dependencies
3. Screenshot: `GET /api/books` response (200, JSON array)
4. Screenshot: `GET /api/books/999` response (404)
5. Screenshot: `POST /api/books` response (201 with Location header visible)
6. Screenshot: `POST /api/books` validation failure (400)
7. Screenshot: `DELETE /api/books/:id` response (204 empty body)
8. Screenshot: terminal showing request logger output (3+ entries)
9. Screenshot: 404 catch-all response for unknown route

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Project initializes with correct `package.json` scripts | 5 |
| `express.json()` middleware registered before routes | 5 |
| `GET /api/books` returns 200 with full array | 10 |
| `GET /api/books/:id` returns 200 or 404 correctly | 10 |
| `POST /api/books` returns 201 with Location header | 15 |
| `POST /api/books` returns 400 when required fields missing | 10 |
| `PUT /api/books/:id` replaces and returns 200 or 404 | 10 |
| `DELETE /api/books/:id` returns 204 (or 404 if not found) | 10 |
| Request logger middleware logs all requests to console | 10 |
| 404 catch-all returns correct error JSON | 5 |
| All nine test cases verified (screenshot table) | 5 |
| Code uses consistent REST conventions (status codes, no verbs in URLs) | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: PATCH Endpoint and Input Sanitization

Add a PATCH endpoint that partially updates a book's fields, and add input sanitization to all write endpoints.

1. Add a PATCH route after the PUT route in `index.js`:

```javascript
app.patch('/api/books/:id', (req, res) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) return res.status(400).json({ error: 'ID must be a number' });
  const index = books.findIndex(b => b.id === id);
  if (index === -1) return res.status(404).json({ error: 'Book not found', code: 'BOOK_NOT_FOUND' });
  const { title, author, year } = req.body;
  if (title !== undefined) books[index].title = title;
  if (author !== undefined) books[index].author = author;
  if (year !== undefined) books[index].year = year;
  res.status(200).json(books[index]);
});
```

1. Add a sanitization helper at the top of `index.js` that trims and truncates string fields to prevent abnormally long inputs:

```javascript
function sanitizeBook({ title, author, year }) {
  return {
    title:  typeof title  === 'string' ? title.trim().slice(0, 200)  : title,
    author: typeof author === 'string' ? author.trim().slice(0, 100) : author,
    year:   year != null ? parseInt(year) : null
  };
}
```

1. Apply `sanitizeBook(req.body)` inside your POST and PUT handlers before creating or replacing a book.
1. Test the PATCH endpoint in Thunder Client: send `PATCH /api/books/1` with only `{ "year": 2024 }` and verify the title and author are unchanged while the year updates.

### Challenge 2: Request Timing Middleware and Structured Logging

Replace the simple console.log logger with a structured JSON logger that records request duration.

1. Replace the `requestLogger` middleware with a version that captures the response finish time:

```javascript
const requestLogger = (req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(JSON.stringify({
      ts: new Date().toISOString(),
      method: req.method,
      path: req.path,
      status: res.statusCode,
      ms: duration
    }));
  });
  next();
};
```

1. Restart the server with `npm run dev` and make five requests through Thunder Client.
1. Copy the JSON log lines from the terminal and paste them into a new file called `sample-logs.json` (as a JSON array by wrapping them in `[...]` with commas between entries).
1. Open `sample-logs.json` in VS Code and verify it is valid JSON using the built-in JSON formatter (Shift+Alt+F).

### Reflection Questions

1. The structured JSON logger emits one log line per request as a complete JSON object. Why is this format preferred over plain text log lines when logs are collected by a service like AWS CloudWatch Logs Insights?
2. The PATCH implementation only updates fields that are explicitly present in `req.body`. What would happen if you used `||` instead of `!== undefined` to check for field presence — and which book field would be impossible to set to a falsy value like `0` or `""`?
