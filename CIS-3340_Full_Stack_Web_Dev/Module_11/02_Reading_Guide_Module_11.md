# Reading Guide: Module 11 — Node.js and Express

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Overview

This guide covers the Node.js runtime, npm, and the Express framework in depth. Work through every code section in VS Code. By the end, you should be able to build a structured Express REST API with proper routing, middleware, and error handling.

---

## 1. The Node.js Runtime

### 1.1 How Node.js Works

Node.js is single-threaded but uses an event loop to handle concurrent operations without blocking. When Node.js encounters an I/O operation — a file read, database query, or network request — it delegates the work to the OS and registers a callback. While waiting, the event loop processes other requests. When the OS finishes, the callback is added to the event queue and executed.

This model is called non-blocking I/O. It makes Node.js efficient for API servers where most work is I/O rather than CPU computation.

### 1.2 CommonJS vs ES Modules

Node.js has two module systems.

| Feature | CommonJS | ES Modules |
|---|---|---|
| Import syntax | `const x = require('./x')` | `import x from './x.js'` |
| Export syntax | `module.exports = x` | `export default x` |
| File extension | `.js` | `.mjs` or `.js` with `"type":"module"` |
| `__dirname` available | Yes | No — use `import.meta.url` |
| Top-level `await` | No | Yes |
| Default in Node.js | Yes | Opt-in |

In this course we use CommonJS (`require`/`module.exports`) for Node projects. It is still the default and is used in most existing codebases.

### 1.3 The Node.js Event Loop Phases

Understanding the event loop helps you debug timing issues.

1. **Timers** — executes `setTimeout` and `setInterval` callbacks that are ready
2. **I/O callbacks** — handles I/O errors and other deferred callbacks
3. **Idle/prepare** — internal use only
4. **Poll** — retrieves new I/O events; blocks here if nothing is queued
5. **Check** — `setImmediate` callbacks
6. **Close callbacks** — close event handlers (e.g., socket close)

`process.nextTick` callbacks execute before the next event loop phase — use it sparingly.

---

## 2. Core Module Reference

### 2.1 path Module

```js
const path = require('path');

path.join('/users', 'alice', 'docs');   // '/users/alice/docs'
path.resolve('./routes', 'users.js');   // absolute path from cwd
path.dirname('/users/alice/file.js');   // '/users/alice'
path.basename('/users/alice/file.js');  // 'file.js'
path.extname('photo.jpeg');             // '.jpeg'
path.join(__dirname, 'public');         // safe cross-platform path
```

Always use `path.join` instead of string concatenation for file paths. Windows uses `\`; Linux/Mac uses `/`. `path.join` handles both.

### 2.2 fs Module (Async/Promises)

```js
const { readFile, writeFile, unlink, mkdir } = require('fs/promises');

// Read a file
const raw = await readFile('./data/students.json', 'utf8');
const students = JSON.parse(raw);

// Write a file
await writeFile('./data/students.json', JSON.stringify(students, null, 2));

// Check if file exists
const { access, constants } = require('fs/promises');
try {
  await access('./data.json', constants.R_OK);
  console.log('File exists and is readable');
} catch {
  console.log('File not found');
}
```

Always use `fs/promises` (async) over the callback-based `fs`. Mixing callbacks and async/await leads to confusing code.

### 2.3 process Object

```js
process.env.PORT        // environment variable
process.env.NODE_ENV    // 'development', 'test', or 'production'
process.cwd()           // current working directory
process.exit(1)         // exit with error code
process.argv            // command-line arguments array
```

`process.env` is the standard way to read configuration in Node.js. Never hard-code API keys, database URLs, or port numbers. Use `.env` files with the `dotenv` package in development and AWS environment variables or AWS Secrets Manager in production.

---

## 3. Express Framework Reference

### 3.1 Application Setup

```js
// app.js — standard Express setup
const express = require('express');
const cors    = require('cors');
const helmet  = require('helmet');
const morgan  = require('morgan');
require('dotenv').config();

const app = express();

// Middleware stack — ORDER MATTERS
app.use(helmet());
app.use(cors({ origin: process.env.FRONTEND_URL || 'http://localhost:5173' }));
app.use(morgan(process.env.NODE_ENV === 'production' ? 'combined' : 'dev'));
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/users',    require('./routes/users'));
app.use('/api/courses',  require('./routes/courses'));

// Error handling — always last
app.use(require('./middleware/notFound'));
app.use(require('./middleware/errorHandler'));

module.exports = app;
```

### 3.2 Route Methods and Path Patterns

| Method | Typical Use | Success Status |
|---|---|---|
| `GET` | Retrieve resource | 200 |
| `POST` | Create resource | 201 + Location header |
| `PUT` | Replace resource entirely | 200 |
| `PATCH` | Update resource partially | 200 |
| `DELETE` | Remove resource | 204 (no body) |

```js
// Path pattern examples
router.get('/users',        handler); // exact match
router.get('/users/:id',    handler); // named param — req.params.id
router.get('/files/*',      handler); // wildcard
router.get('/a|b',          handler); // regex-like alternatives
```

### 3.3 Request Object Cheat Sheet

```js
req.params      // { id: '42' } — URL path parameters
req.query       // { page: '1', limit: '20' } — query string
req.body        // { name: 'Alice' } — parsed JSON/form body
req.headers     // { 'content-type': 'application/json', ... }
req.method      // 'GET', 'POST', etc.
req.path        // '/api/users'
req.originalUrl // '/api/users?page=1'
req.ip          // client IP address
req.get('Authorization')  // read a specific header
```

### 3.4 Response Object Cheat Sheet

```js
res.status(200)                              // set status code
res.json({ key: 'value' })                  // send JSON + Content-Type header
res.send('plain text')                      // send text
res.status(201).json(newResource)           // chain status + json
res.set('Location', '/api/users/42')        // set a header
res.set('X-Custom', 'value')                // set custom header
res.status(204).send()                      // no-content response
res.redirect(301, '/new-path')              // redirect
res.sendFile(path.join(__dirname, 'index.html'))  // serve a file
```

---

## 4. Middleware Deep Dive

### 4.1 Writing Middleware

```js
// Request timing middleware
function timing(req, res, next) {
  req._start = Date.now();
  res.on('finish', () => {
    const ms = Date.now() - req._start;
    console.log(`${req.method} ${req.path} — ${ms}ms`);
  });
  next();  // always call next() or send a response — never both
}

// Attaching data to req for downstream use
function attachRequestId(req, res, next) {
  req.requestId = `req-${Date.now()}-${Math.random().toString(36).slice(2)}`;
  res.set('X-Request-Id', req.requestId);
  next();
}
```

### 4.2 Validation Middleware Factory

```js
// middleware/validate.js
function requireFields(fields) {
  return (req, res, next) => {
    const missing = fields.filter(f => !req.body[f]);
    if (missing.length > 0) {
      return res.status(400).json({
        error: 'Missing required fields',
        fields: missing,
      });
    }
    next();
  };
}

// Usage
router.post('/', requireFields(['name', 'email']), async (req, res, next) => {
  // req.body.name and req.body.email are guaranteed to exist here
});
```

### 4.3 Middleware Execution Order

```text
Request arrives
     |
     v
app.use(helmet())          <- Security headers added to res
     |
     v
app.use(cors())            <- CORS headers added
     |
     v
app.use(express.json())    <- req.body populated
     |
     v
app.use('/api', router)    <- route matched; handler runs
     |
     v
app.use(notFound)          <- runs if no route matched
     |
     v
app.use(errorHandler)      <- runs if any middleware called next(err)
```

---

## 5. Error Handling Patterns

### 5.1 Custom Error Classes

```js
// utils/errors.js
class AppError extends Error {
  constructor(message, status, code) {
    super(message);
    this.name = this.constructor.name;
    this.status = status;
    this.code = code;
    Error.captureStackTrace(this, this.constructor);
  }
}

class NotFoundError extends AppError {
  constructor(resource = 'Resource') {
    super(`${resource} not found`, 404, 'NOT_FOUND');
  }
}

class ValidationError extends AppError {
  constructor(message, fields = null) {
    super(message, 400, 'VALIDATION_ERROR');
    this.fields = fields;
  }
}

class UnauthorizedError extends AppError {
  constructor(message = 'Unauthorized') {
    super(message, 401, 'UNAUTHORIZED');
  }
}

module.exports = { AppError, NotFoundError, ValidationError, UnauthorizedError };
```

### 5.2 Global Error Handler

```js
// middleware/errorHandler.js
module.exports = function errorHandler(err, req, res, next) {
  const status = err.status || 500;
  const isDev = process.env.NODE_ENV === 'development';

  // Log 5xx errors with stack trace
  if (status >= 500) {
    console.error(`[${new Date().toISOString()}] ERROR:`, err.stack);
  }

  res.status(status).json({
    error:   status < 500 ? err.message : 'Internal Server Error',
    code:    err.code || 'SERVER_ERROR',
    ...(err.fields && { fields: err.fields }),
    ...(isDev && status >= 500 && { stack: err.stack }),
  });
};
```

### 5.3 Async Error Wrapper

Repeating `try/catch/next(err)` in every route is verbose. Use a wrapper:

```js
// utils/asyncHandler.js
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

module.exports = asyncHandler;

// Usage — no try/catch needed
const asyncHandler = require('../utils/asyncHandler');

router.get('/:id', asyncHandler(async (req, res) => {
  const user = await db.findById(req.params.id);
  if (!user) throw new NotFoundError('User');
  res.json(user);
}));
```

---

## 6. Project Structure Best Practices

### 6.1 Recommended Folder Layout

```text
project-root/
├── app.js              <- Express setup; export app; no listen()
├── server.js           <- require('./app').listen(PORT)
├── routes/             <- Router files; define route handlers
├── controllers/        <- Handler logic (optional for larger apps)
├── middleware/         <- Custom middleware functions
├── utils/              <- Shared utilities; error classes; async wrapper
├── models/             <- Database interaction layer
├── tests/              <- API and unit tests
├── .env                <- Local config; never commit
├── .env.example        <- Template with placeholder values; commit this
├── .gitignore
└── package.json
```

### 6.2 Environment Variables Convention

```bash
# .env
NODE_ENV=development
PORT=3000
DB_HOST=localhost
DB_NAME=registrar
DB_USER=postgres
DB_PASSWORD=devpassword
JWT_SECRET=change-this-in-production
FRONTEND_URL=http://localhost:5173
```

```bash
# .env.example  (commit this file)
NODE_ENV=development
PORT=3000
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
JWT_SECRET=
FRONTEND_URL=
```

---

## 7. AWS Lambda Connection

A Lambda function handler is essentially a single Express route handler:

```js
// Lambda handler signature
exports.handler = async (event, context) => {
  const body = JSON.parse(event.body || '{}');
  const { id } = event.pathParameters || {};

  // Same logic you would write in an Express handler
  const user = await db.findById(id);
  if (!user) return { statusCode: 404, body: JSON.stringify({ error: 'Not found' }) };

  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(user),
  };
};
```

`event.body`, `event.pathParameters`, and `event.queryStringParameters` map directly to Express's `req.body`, `req.params`, and `req.query`. Understanding Express makes Lambda much easier to learn.

### 7.1 AWS Exam Tips

- Lambda environment variables are configured in the function configuration, not in `.env` files.
- Lambda has a maximum timeout of 15 minutes. Long-running operations should use Step Functions or SQS.
- Lambda cold starts occur when a new execution environment is initialized. Minimize package size and avoid global database connections for cold-start-sensitive functions.
- API Gateway `proxy integration` passes the full HTTP request to Lambda as the `event` object.
- `process.env.NODE_ENV` in Lambda is typically set to `production` in the function configuration.

---

## 8. Study Checklist

- [ ] Create a Node.js project with `npm init -y` and install `express`, `dotenv`, `nodemon`
- [ ] Write a basic Express server with at least one GET and one POST route
- [ ] Use `express.Router()` to split routes into separate files
- [ ] Use `req.params`, `req.query`, and `req.body` correctly in handlers
- [ ] Write and apply custom middleware (`app.use(fn)` and route-level `router.use(fn)`)
- [ ] Return appropriate status codes (200, 201, 204, 400, 404, 500)
- [ ] Write a global error handler with four parameters `(err, req, res, next)`
- [ ] Use `next(err)` to forward errors to the error handler
- [ ] Create custom `AppError`, `NotFoundError`, and `ValidationError` classes
- [ ] Separate `app.js` (setup) from `server.js` (listen)
- [ ] Configure `cors`, `helmet`, and `morgan` middleware
- [ ] Explain the relationship between Express route handlers and AWS Lambda handlers

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 11 topics:

**1. Node.js Official Documentation — `path` module**
[https://nodejs.org/api/path.html](https://nodejs.org/api/path.html)
The complete `path` module API reference covering `path.join`, `path.resolve`, `path.dirname`, `path.basename`, and cross-platform path separator handling — directly aligned to the `path.join(__dirname, ...)` pattern used throughout Lab 11.

**2. Express.js Official Guide — Error Handling**
[https://expressjs.com/en/guide/error-handling.html](https://expressjs.com/en/guide/error-handling.html)
The authoritative Express documentation on writing error-handling middleware, the four-parameter `(err, req, res, next)` signature, forwarding errors with `next(err)`, and the async error handling pattern — covers all concepts in Section 5 of this guide.

**3. npm — helmet documentation**
[https://www.npmjs.com/package/helmet](https://www.npmjs.com/package/helmet)
The official `helmet` package documentation listing all security headers it sets by default and the configuration options for each — directly relevant to the `app.use(helmet())` call in `app.js` and the security header concepts tested in the quiz.

**4. npm — morgan documentation**
[https://www.npmjs.com/package/morgan](https://www.npmjs.com/package/morgan)
The official `morgan` HTTP request logger documentation covering predefined formats (`dev`, `combined`, `tiny`), custom token definitions, and writing to a file stream — aligns to the `morgan(process.env.NODE_ENV === 'production' ? 'combined' : 'dev')` pattern in the lab.
