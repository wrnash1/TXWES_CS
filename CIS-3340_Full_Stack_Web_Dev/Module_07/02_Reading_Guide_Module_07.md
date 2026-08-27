# Reading Guide: Module 07 - Node.js & Express Server

**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module introduces Node.js as a server-side JavaScript runtime and Express as the web framework used to build REST APIs. You will initialize a Node.js project, install dependencies, implement full CRUD routes, use middleware, and handle errors. These skills are directly applied in Module 08 (routing), Module 09 (PostgreSQL integration), and Module 14 (AWS deployment).

---

## 1. What is Node.js?

Node.js is a JavaScript runtime built on Chrome's V8 engine. It executes JavaScript outside the browser using an event-driven, non-blocking I/O model. Key characteristics:

- Single-threaded event loop handles concurrent connections without spawning threads
- Non-blocking I/O: file reads, database queries, and network calls do not block execution
- CommonJS module system: `require()` and `module.exports`
- Large ecosystem via npm (Node Package Manager)

Node.js powers everything from simple REST APIs to AWS Lambda functions. Every Lambda function written in JavaScript/TypeScript runs on Node.js.

---

## 2. Project Initialization

### npm init

```bash
mkdir my-api
cd my-api
npm init -y
```

The `-y` flag generates a default `package.json`. This file is the project manifest.

### package.json Structure

```json
{
  "name": "my-api",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
```

### Dependency Types

| Type | Flag | Purpose | Included in Production? |
|---|---|---|---|
| Dependency | `npm install` | Required at runtime | Yes |
| Dev dependency | `npm install --save-dev` | Development tools only | No |

AWS Lambda deployment packages include `dependencies` only. `devDependencies` are not bundled.

### nodemon

`nodemon` watches the project directory for file changes and restarts the Node.js process automatically. Use it during development.

```bash
npm install --save-dev nodemon
npm run dev    # uses nodemon via package.json script
```

---

## 3. Express Basics

### Installation

```bash
npm install express
```

### Minimal Server

```javascript
const express = require('express');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json()); // parse JSON request bodies

app.get('/', (req, res) => {
  res.json({ message: 'API is running' });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Express Application Methods

| Method | Purpose |
|---|---|
| `app.use(fn)` | Register middleware globally |
| `app.get(path, fn)` | Register GET route handler |
| `app.post(path, fn)` | Register POST route handler |
| `app.put(path, fn)` | Register PUT route handler |
| `app.patch(path, fn)` | Register PATCH route handler |
| `app.delete(path, fn)` | Register DELETE route handler |
| `app.listen(port, fn)` | Bind server to port and start listening |

---

## 4. Route Handlers

A route handler is a function that receives `(req, res)` and sends a response. Every handler must send exactly one response — calling `res.json()`, `res.send()`, or `res.status().send()`.

### Complete CRUD Example

```javascript
let items = [
  { id: 1, name: 'Widget A' },
  { id: 2, name: 'Widget B' }
];
let nextId = 3;

// GET /api/items — list all
app.get('/api/items', (req, res) => {
  res.status(200).json(items);
});

// GET /api/items/:id — get one
app.get('/api/items/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const item = items.find(i => i.id === id);
  if (!item) return res.status(404).json({ error: 'Not found', code: 'ITEM_NOT_FOUND' });
  res.status(200).json(item);
});

// POST /api/items — create
app.post('/api/items', (req, res) => {
  const { name } = req.body;
  if (!name) return res.status(400).json({ error: 'name is required' });
  const newItem = { id: nextId++, name };
  items.push(newItem);
  res.status(201).set('Location', `/api/items/${newItem.id}`).json(newItem);
});

// PUT /api/items/:id — replace
app.put('/api/items/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = items.findIndex(i => i.id === id);
  if (index === -1) return res.status(404).json({ error: 'Not found' });
  items[index] = { id, name: req.body.name };
  res.status(200).json(items[index]);
});

// DELETE /api/items/:id — remove
app.delete('/api/items/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = items.findIndex(i => i.id === id);
  if (index === -1) return res.status(404).json({ error: 'Not found' });
  items.splice(index, 1);
  res.status(204).send();
});
```

---

## 5. The Request Object (req)

| Property | Type | Description |
|---|---|---|
| `req.method` | string | HTTP method: `'GET'`, `'POST'`, etc. |
| `req.path` | string | URL path: `'/api/items/42'` |
| `req.params` | object | Path parameters: `{ id: '42' }` from `:id` |
| `req.query` | object | Query parameters: `{ sort: 'name' }` from `?sort=name` |
| `req.body` | object | Parsed JSON body (requires `express.json()`) |
| `req.headers` | object | All request headers |

```javascript
app.get('/api/items', (req, res) => {
  const { sort, page = 1, limit = 10 } = req.query;
  // GET /api/items?sort=name&page=2&limit=5
});
```

---

## 6. The Response Object (res)

```javascript
// Send JSON with status code
res.status(200).json({ data: items });

// Send with custom header
res.status(201).set('Location', '/api/items/5').json(newItem);

// Send empty body
res.status(204).send();

// Chaining: status() returns res, enabling method chaining
res.status(404).json({ error: 'Not found' });
```

### Common Response Patterns

| Operation | Status | Body |
|---|---|---|
| List resources | 200 | Array of objects |
| Get one resource | 200 | Single object |
| Create resource | 201 | Created object; include Location header |
| Replace resource | 200 | Updated object |
| Delete resource | 204 | Empty |
| Validation error | 400 | Error object with message |
| Not found | 404 | Error object with message |

---

## 7. Middleware

Middleware functions have the signature `(req, res, next)`. Call `next()` to pass control forward. Do not call `next()` if you send a response.

### Logging Middleware

```javascript
const requestLogger = (req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  next();
};

app.use(requestLogger); // register before routes
```

### Built-in Middleware

```javascript
app.use(express.json());          // parse application/json bodies
app.use(express.urlencoded({ extended: true })); // parse form data
app.use(express.static('public')); // serve static files
```

### Middleware Execution Order

Middleware runs in the order it is registered with `app.use()`. Always register body-parsing middleware before routes that read `req.body`.

```javascript
// CORRECT order
app.use(express.json());    // 1 — parse body
app.use(requestLogger);     // 2 — log request
app.get('/api/...', ...);   // 3 — handle route

// WRONG — body will be undefined in POST routes
app.post('/api/items', handler);
app.use(express.json());
```

---

## 8. Error Handling

### 404 Catch-All

Register after all routes. Catches any request that did not match a defined route:

```javascript
app.use((req, res) => {
  res.status(404).json({
    error: `${req.method} ${req.path} not found`,
    code: 'ROUTE_NOT_FOUND'
  });
});
```

### Global Error Handler

Four-parameter signature `(err, req, res, next)` — Express recognizes this as the error handler:

```javascript
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message || 'Internal server error',
    code: err.code || 'INTERNAL_ERROR'
  });
});
```

### Forwarding Errors

Call `next(err)` from any route or middleware to skip to the error handler:

```javascript
app.get('/api/items/:id', (req, res, next) => {
  try {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      const err = new Error('ID must be a number');
      err.status = 400;
      return next(err);
    }
    // ...
  } catch (err) {
    next(err);
  }
});
```

---

## 9. Environment Variables

Never hard-code configuration values (ports, database URLs, API keys). Use environment variables accessed via `process.env`.

```javascript
const PORT = process.env.PORT || 3000;
const DB_URL = process.env.DATABASE_URL;
```

Use a `.env` file locally with the `dotenv` package:

```bash
npm install dotenv
```

```javascript
// At the very top of index.js
require('dotenv').config();
```

Add `.env` to `.gitignore` — never commit secrets to version control. AWS Lambda reads environment variables set in the function configuration console — the same `process.env` interface.

---

## 10. Project File Structure

```text
express-server/
├── index.js           entry point — initializes app and calls app.listen()
├── package.json       project manifest and scripts
├── .env               local environment variables (not committed)
├── .gitignore         excludes node_modules and .env
├── routes/
│   └── books.js       route handlers grouped by resource (Module 08)
└── middleware/
    └── logger.js      reusable middleware functions
```

---

## 11. Exam and Interview Tips

1. `express()` is a factory function, not a class. Never use `new express()`.

2. `express.json()` must be registered before any route that reads `req.body`. A missing `app.use(express.json())` is the most common cause of `req.body === undefined`.

3. `req.params` contains path parameters (`:id`). `req.query` contains query string parameters (`?sort=name`). These are different objects.

4. `app.listen()` is called once at the end of the entry point file. Calling it multiple times binds multiple servers to the same port and throws an `EADDRINUSE` error.

5. `204 No Content` for DELETE means the response body must be empty. Call `res.status(204).send()` — not `res.status(204).json({})`.

6. The global error handler requires exactly four parameters `(err, req, res, next)`. With fewer parameters, Express does not recognize it as an error handler.

7. `process.env.PORT` is the correct way to read the port in AWS environments. Elastic Beanstalk sets PORT automatically.

8. In-memory arrays (as used in this module for simplicity) are reset on every server restart. In AWS Lambda, in-memory state is also reset on cold starts. Use a database for persistent data.

---

## 12. Study Checklist

- [ ] Initialize a Node.js project with `npm init` and install Express
- [ ] Understand the difference between dependencies and devDependencies
- [ ] Configure `package.json` scripts for `start` and `dev`
- [ ] Build a server with `app.listen()` reading port from `process.env.PORT`
- [ ] Implement GET, POST, PUT, and DELETE route handlers
- [ ] Use `req.params`, `req.query`, and `req.body` correctly
- [ ] Register `express.json()` middleware before routes
- [ ] Write a request logger middleware with `next()`
- [ ] Implement a 404 catch-all and global error handler
- [ ] Use environment variables with `dotenv` and never commit `.env`

---

## 13. Supplemental Resources

The following free, open-access resources go deeper on Module 07 topics:

**1. Node.js Official Documentation — Getting Started**
[https://nodejs.org/en/learn/getting-started/introduction-to-nodejs](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
The official Node.js introduction covering the event loop, non-blocking I/O, the V8 engine, and how Node.js differs from browser JavaScript — foundational reading before implementing Lambda functions in Module 14.

**2. Express.js Official Guide**
[https://expressjs.com/en/guide/routing.html](https://expressjs.com/en/guide/routing.html)
The authoritative Express routing guide covering route methods, path patterns, route parameters, middleware, and the `Router` object used in Module 08 — directly aligned to the Lab 07 CRUD implementation.

**3. MDN Web Docs — HTTP request methods**
[https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
Complete reference for all HTTP methods including safe and idempotent semantics — reinforces the REST principles applied in the Express route handlers built in this module.

**4. freeCodeCamp — Node.js and Express for Beginners**
[https://www.freecodecamp.org/news/free-8-hour-node-express-course/](https://www.freecodecamp.org/news/free-8-hour-node-express-course/)
A free video-based course covering project setup, middleware, routing, and error handling in Express — useful supplemental reference for students who prefer video walkthroughs alongside the reading guide and lab.
