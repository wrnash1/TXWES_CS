# Reading Guide: Module 08 - Server-Side Routing & Middleware

**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers two foundational Express patterns used in every production Node.js application: Express Router for organizing routes into separate files, and custom middleware for reusable request-processing logic. You will also configure CORS, build a validation middleware factory, and implement route-level middleware. These patterns apply directly to Module 09 (database integration), Module 13 (JWT authentication middleware), and Module 14 (AWS deployment).

---

## 1. The Problem with Single-File Servers

A single `index.js` with all routes becomes unmanageable as an API grows. Common symptoms:

- Merge conflicts when multiple developers edit the same file
- Difficulty locating specific endpoint code
- Duplicated validation logic across routes
- No clear boundary between resources (users, products, orders)

Express Router solves the first problem. Custom middleware solves the last two.

---

## 2. Express Router

`express.Router()` creates a modular route handler. Each router instance is a complete mini-application with its own middleware stack and route definitions.

### Creating a Router

```javascript
// routes/books.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.status(200).json(books);
});

router.get('/:id', (req, res) => {
  // ...
});

router.post('/', (req, res) => {
  // ...
});

module.exports = router;
```

### Mounting a Router

```javascript
// index.js
const booksRouter = require('./routes/books');
app.use('/api/books', booksRouter);
```

The mount path `/api/books` is prepended to every path defined in the router. A router route of `/` becomes `/api/books`. A router route of `/:id` becomes `/api/books/:id`.

### File Structure

```text
project/
├── index.js            app initialization, global middleware, router mounts
├── package.json
├── routes/
│   ├── books.js        book resource routes
│   ├── authors.js      author resource routes
│   └── users.js        user resource routes
└── middleware/
    ├── logger.js        request logging
    └── validate.js      input validation factory
```

---

## 3. Middleware Patterns

### Standard Middleware Signature

```javascript
const myMiddleware = (req, res, next) => {
  // modify req or res
  next(); // MUST call next() or send a response
};

app.use(myMiddleware);           // applies to all routes
app.get('/path', myMiddleware, handler); // applies to one route
```

### Route-Level Middleware

Middleware can be scoped to a single route by passing it as an additional argument before the handler:

```javascript
router.post('/', validateInput, authenticate, (req, res) => {
  // only runs if validateInput and authenticate both call next()
});
```

### Middleware Factory

A function that returns a middleware function, parameterized by arguments:

```javascript
// middleware/validate.js
const requireFields = (fields) => {
  return (req, res, next) => {
    const missing = fields.filter(f => req.body[f] === undefined || req.body[f] === '');
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

Usage:

```javascript
const { requireFields } = require('../middleware/validate');

router.post('/', requireFields(['title', 'author', 'year']), (req, res) => {
  // all three fields are guaranteed to be present
});
```

### Request Logger with Timing

```javascript
// middleware/logger.js
const requestLogger = (req, res, next) => {
  const start = Date.now();
  const ts = new Date().toISOString();

  res.on('finish', () => {
    const ms = Date.now() - start;
    console.log(`[${ts}] ${req.method} ${req.path} ${res.statusCode} ${ms}ms`);
  });

  next();
};

module.exports = requestLogger;
```

The `res.on('finish', ...)` event fires after the response is sent — this allows logging the actual status code and response time.

---

## 4. Middleware Execution Order

Order matters. Middleware runs in registration order.

```javascript
// CORRECT
app.use(express.json());           // 1 — parse body
app.use(cors());                   // 2 — add CORS headers
app.use(requestLogger);            // 3 — log request
app.use('/api/books', booksRouter); // 4 — handle routes
app.use(notFoundHandler);          // 5 — 404 catch-all
app.use(errorHandler);             // 6 — error handler (4 params)
```

A middleware registered after the route will never run for requests handled by that route — the response has already been sent.

---

## 5. Error Handling Middleware

### 404 Catch-All

Registered after all routes. Catches requests that matched no route:

```javascript
app.use((req, res) => {
  res.status(404).json({
    error: `${req.method} ${req.path} not found`,
    code: 'ROUTE_NOT_FOUND'
  });
});
```

### Global Error Handler

Four-parameter signature — Express recognizes this as the error handler. Register last:

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

From any route or middleware, call `next(err)` to skip to the error handler:

```javascript
router.get('/:id', (req, res, next) => {
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

## 6. CORS Configuration

The Same-Origin Policy blocks browser-side requests to different origins (different scheme, host, or port). The server resolves this by sending CORS response headers.

### Installation

```bash
npm install cors
```

### Basic Configuration (Development)

```javascript
const cors = require('cors');
app.use(cors()); // Access-Control-Allow-Origin: *
```

### Restricted Configuration (Production)

```javascript
app.use(cors({
  origin: process.env.FRONTEND_URL,
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true  // required when sending cookies or Authorization headers
}));
```

### CORS Headers Reference

| Header | Purpose |
|---|---|
| `Access-Control-Allow-Origin` | Which origins may access this resource |
| `Access-Control-Allow-Methods` | Which HTTP methods are permitted |
| `Access-Control-Allow-Headers` | Which request headers are permitted |
| `Access-Control-Allow-Credentials` | Whether cookies/auth headers may be sent |

### Preflight Requests

Browsers send an `OPTIONS` request before cross-origin POST, PUT, DELETE to verify the server's CORS policy. The `cors()` middleware handles OPTIONS automatically.

---

## 7. Query Parameters and Filtering

```javascript
// GET /api/books?author=Martin&year=2008&sort=title
router.get('/', (req, res) => {
  let result = [...books];
  const { author, year, sort } = req.query;

  if (author) {
    result = result.filter(b => b.author.toLowerCase().includes(author.toLowerCase()));
  }
  if (year) {
    result = result.filter(b => b.year === parseInt(year));
  }
  if (sort === 'title') {
    result.sort((a, b) => a.title.localeCompare(b.title));
  }

  res.status(200).json(result);
});
```

All query parameter values are strings. Convert to the appropriate type (`parseInt`, `parseFloat`, comparison to `'true'`) before use.

---

## 8. Router-Level Middleware

A router can have its own middleware stack applied to all routes within it:

```javascript
// routes/admin.js — all admin routes require authentication
const router = express.Router();

router.use(authenticate); // applied to all routes in this router

router.get('/users', (req, res) => { /* ... */ });
router.delete('/users/:id', (req, res) => { /* ... */ });

module.exports = router;
```

This is cleaner than adding the `authenticate` middleware to every individual route.

---

## 9. Exam and Interview Tips

1. `express.Router()` routes use paths relative to the mount point. A router mounted at `/api/books` with a route `'/:id'` handles `GET /api/books/42` — not `GET /api/books/:id`.

2. The 404 catch-all must be registered after all route definitions, not before. If registered before, it intercepts all requests.

3. The global error handler requires exactly four parameters `(err, req, res, next)`. Any other arity causes Express to treat it as regular middleware.

4. CORS middleware must be registered before routes. A response sent without CORS headers causes a browser-side CORS error even if the server processes the request correctly.

5. `cors({ credentials: true })` requires a specific `origin` — `origin: '*'` with `credentials: true` is rejected by browsers.

6. Middleware factories (functions that return middleware) are the standard pattern for authentication checks, role-based access control, and field validation.

7. `next()` passes to the next middleware. `next(err)` skips all regular middleware and routes and jumps to the error handler.

8. AWS Lambda Authorizers work like authentication middleware: a separate function validates the request before the main handler runs. Understanding Express route-level middleware directly prepares you for Lambda Authorizer architecture.

---

## 10. Study Checklist

- [ ] Split a single-file Express server into `routes/` and `middleware/` folders
- [ ] Create an `express.Router()`, define routes on it, and mount it with a path prefix
- [ ] Write a custom middleware function with `(req, res, next)` signature
- [ ] Build a middleware factory that returns a validation function
- [ ] Register a request logger that logs method, path, status, and duration
- [ ] Configure `cors()` for development (all origins) and production (specific origin)
- [ ] Implement a 404 catch-all handler after all routes
- [ ] Implement a four-parameter global error handler
- [ ] Forward errors to the error handler using `next(err)`
- [ ] Filter query parameters with `req.query` and handle type conversion

---

## 11. Supplemental Resources

The following free, open-access resources go deeper on Module 08 topics:

**1. Express.js Official Guide — Using Middleware**
[https://expressjs.com/en/guide/using-middleware.html](https://expressjs.com/en/guide/using-middleware.html)
The authoritative Express documentation covering application-level middleware, router-level middleware, error-handling middleware, and built-in middleware — directly aligned to the middleware pipeline and factory patterns built in Lab 08.

**2. Express.js Official Guide — Router**
[https://expressjs.com/en/4x/api.html#router](https://expressjs.com/en/4x/api.html#router)
The full API reference for `express.Router()` including `router.param()`, `router.route()`, `router.use()`, and mounting behavior — essential for understanding how the books and authors routers in Lab 08 interact with the main app.

**3. MDN Web Docs — Cross-Origin Resource Sharing (CORS)**
[https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
A comprehensive reference explaining the browser CORS mechanism, preflight requests, credentialed requests, and the response headers (`Access-Control-Allow-Origin`, etc.) that the `cors()` middleware sets — foundational for debugging CORS errors in Module 08 and AWS API Gateway in Module 14.

**4. npm — cors package documentation**
[https://www.npmjs.com/package/cors](https://www.npmjs.com/package/cors)
The official documentation for the `cors` npm package covering configuration options (`origin`, `methods`, `credentials`, `allowedHeaders`), per-route usage, and preflight handling — the exact package configured in the Lab 08 `index.js` refactor.
