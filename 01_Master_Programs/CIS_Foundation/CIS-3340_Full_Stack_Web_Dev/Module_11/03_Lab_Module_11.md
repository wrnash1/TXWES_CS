# Lab 11: University Registrar REST API with Express

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90–120 minutes

---

## Objectives

By completing this lab you will:

- Build a structured Express REST API from scratch
- Organize routes using `express.Router()`
- Write custom middleware for logging and validation
- Implement proper HTTP status codes and response shapes
- Write a global error handler with custom error classes
- Test all endpoints with Postman or Thunder Client

---

## Prerequisites

- Node.js 18+ installed (`node --version` to verify)
- Module 11 video and reading guide complete
- Postman or Thunder Client VS Code extension installed

---

## Part 1: Project Setup (15 minutes)

### Step 1 — Initialize the project

```bash
mkdir lab11-registrar && cd lab11-registrar
npm init -y
npm install express dotenv cors helmet morgan
npm install --save-dev nodemon
```

### Step 2 — Configure package.json scripts

Open `package.json` and replace the `"scripts"` section:

```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  }
}
```

### Step 3 — Create the .env file

Create `.env` in the project root:

```text
NODE_ENV=development
PORT=3000
FRONTEND_URL=http://localhost:5173
```

Create `.gitignore`:

```text
node_modules/
.env
```

### Step 4 — Create the folder structure

```bash
mkdir routes middleware utils
```

Your structure should look like:

```text
lab11-registrar/
├── app.js
├── server.js
├── routes/
│   ├── students.js
│   └── courses.js
├── middleware/
│   ├── validate.js
│   └── errorHandler.js
├── utils/
│   └── errors.js
├── .env
├── .gitignore
└── package.json
```

---

## Part 2: Custom Error Classes (10 minutes)

### Step 5 — Create utils/errors.js

```js
// utils/errors.js
class AppError extends Error {
  constructor(message, status, code) {
    super(message);
    this.name = this.constructor.name;
    this.status = status;
    this.code = code;
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

module.exports = { AppError, NotFoundError, ValidationError };
```

---

## Part 3: Middleware (15 minutes)

### Step 6 — Create middleware/validate.js

```js
// middleware/validate.js
function requireFields(fields) {
  return (req, res, next) => {
    const missing = fields.filter(f => {
      const val = req.body[f];
      return val === undefined || val === null || val === '';
    });

    if (missing.length > 0) {
      return res.status(400).json({
        error: 'Missing required fields',
        code: 'VALIDATION_ERROR',
        fields: missing,
      });
    }

    next();
  };
}

module.exports = { requireFields };
```

### Step 7 — Create middleware/errorHandler.js

```js
// middleware/errorHandler.js

// 404 handler — no route matched
function notFound(req, res) {
  res.status(404).json({
    error: `Cannot ${req.method} ${req.path}`,
    code: 'NOT_FOUND',
  });
}

// Global error handler — called when next(err) is used
function errorHandler(err, req, res, next) {
  const status = err.status || 500;
  const isDev = process.env.NODE_ENV === 'development';

  if (status >= 500) {
    console.error(`[ERROR] ${new Date().toISOString()} ${req.method} ${req.path}`);
    console.error(err.stack);
  }

  res.status(status).json({
    error: status < 500 ? err.message : 'Internal Server Error',
    code: err.code || 'SERVER_ERROR',
    ...(err.fields && { fields: err.fields }),
    ...(isDev && status >= 500 && { stack: err.stack }),
  });
}

module.exports = { notFound, errorHandler };
```

---

## Part 4: Routes (30 minutes)

### Step 8 — Create in-memory data

Create `data/students.js` (first create the `data/` directory):

```bash
mkdir data
```

```js
// data/students.js
let students = [
  { id: 1, name: 'Alice Johnson', email: 'alice@txwes.edu', major: 'Computer Science', gpa: 3.8, enrolledYear: 2022 },
  { id: 2, name: 'Bob Martinez', email: 'bob@txwes.edu', major: 'Information Systems', gpa: 2.9, enrolledYear: 2021 },
  { id: 3, name: 'Carol Chen', email: 'carol@txwes.edu', major: 'Computer Science', gpa: 3.5, enrolledYear: 2023 },
];
let nextId = 4;

module.exports = {
  getAll: () => students,
  getById: (id) => students.find(s => s.id === id),
  create: (data) => {
    const student = { id: nextId++, ...data, gpa: data.gpa || 0.0 };
    students.push(student);
    return student;
  },
  update: (id, data) => {
    const index = students.findIndex(s => s.id === id);
    if (index === -1) return null;
    students[index] = { ...students[index], ...data };
    return students[index];
  },
  remove: (id) => {
    const index = students.findIndex(s => s.id === id);
    if (index === -1) return false;
    students.splice(index, 1);
    return true;
  },
};
```

### Step 9 — Create routes/students.js

```js
// routes/students.js
const { Router } = require('express');
const db = require('../data/students');
const { requireFields } = require('../middleware/validate');
const { NotFoundError, ValidationError } = require('../utils/errors');

const router = Router();

// GET /api/students — list all, with optional ?major= filter
router.get('/', (req, res) => {
  let result = db.getAll();
  if (req.query.major) {
    result = result.filter(s =>
      s.major.toLowerCase().includes(req.query.major.toLowerCase())
    );
  }
  res.status(200).json({ count: result.length, data: result });
});

// GET /api/students/:id
router.get('/:id', (req, res, next) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) return next(new ValidationError('id must be a number'));

  const student = db.getById(id);
  if (!student) return next(new NotFoundError('Student'));
  res.status(200).json(student);
});

// POST /api/students
router.post(
  '/',
  requireFields(['name', 'email', 'major']),
  (req, res, next) => {
    const { name, email, major, gpa, enrolledYear } = req.body;

    // Basic email validation
    if (!email.includes('@')) return next(new ValidationError('Invalid email address'));

    const student = db.create({ name, email, major, gpa, enrolledYear });
    res.status(201)
      .set('Location', `/api/students/${student.id}`)
      .json(student);
  }
);

// PATCH /api/students/:id — partial update
router.patch('/:id', (req, res, next) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) return next(new ValidationError('id must be a number'));

  const updated = db.update(id, req.body);
  if (!updated) return next(new NotFoundError('Student'));
  res.status(200).json(updated);
});

// DELETE /api/students/:id
router.delete('/:id', (req, res, next) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) return next(new ValidationError('id must be a number'));

  const deleted = db.remove(id);
  if (!deleted) return next(new NotFoundError('Student'));
  res.status(204).send();
});

module.exports = router;
```

### Step 10 — Create routes/courses.js

```js
// routes/courses.js
const { Router } = require('express');
const { requireFields } = require('../middleware/validate');
const { NotFoundError } = require('../utils/errors');

const router = Router();

let courses = [
  { id: 'CIS-3340', title: 'Full Stack Web Development', credits: 3, instructor: 'Prof. Nash' },
  { id: 'CIS-3350', title: 'Database Management', credits: 3, instructor: 'Prof. Smith' },
  { id: 'CIS-4410', title: 'Cloud Computing', credits: 3, instructor: 'Prof. Johnson' },
];

router.get('/', (req, res) => {
  res.status(200).json({ count: courses.length, data: courses });
});

router.get('/:id', (req, res, next) => {
  const course = courses.find(c => c.id === req.params.id.toUpperCase());
  if (!course) return next(new NotFoundError('Course'));
  res.status(200).json(course);
});

router.post('/', requireFields(['id', 'title', 'credits']), (req, res) => {
  const course = { ...req.body, id: req.body.id.toUpperCase() };
  courses.push(course);
  res.status(201).set('Location', `/api/courses/${course.id}`).json(course);
});

module.exports = router;
```

---

## Part 5: App and Server Files (10 minutes)

### Step 11 — Create app.js

```js
// app.js
const express = require('express');
const cors    = require('cors');
const helmet  = require('helmet');
const morgan  = require('morgan');
require('dotenv').config();

const { notFound, errorHandler } = require('./middleware/errorHandler');

const app = express();

app.use(helmet());
app.use(cors({ origin: process.env.FRONTEND_URL }));
app.use(morgan(process.env.NODE_ENV === 'production' ? 'combined' : 'dev'));
app.use(express.json());

// Health check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', env: process.env.NODE_ENV, timestamp: new Date().toISOString() });
});

// Routes
app.use('/api/students', require('./routes/students'));
app.use('/api/courses',  require('./routes/courses'));

// Error handling — always last
app.use(notFound);
app.use(errorHandler);

module.exports = app;
```

### Step 12 — Create server.js

```js
// server.js
const app = require('./app');
const PORT = parseInt(process.env.PORT) || 3000;

app.listen(PORT, () => {
  console.log(`Registrar API running on http://localhost:${PORT}`);
  console.log(`Environment: ${process.env.NODE_ENV}`);
});
```

---

## Part 6: Testing with Postman / Thunder Client (15 minutes)

Start the server: `npm run dev`

Test each endpoint and verify the response:

| Request | Expected Status | Expected Body |
|---|---|---|
| `GET /health` | 200 | `{ status: 'ok' }` |
| `GET /api/students` | 200 | Array of 3 students |
| `GET /api/students?major=computer` | 200 | Array of 2 students |
| `GET /api/students/1` | 200 | Alice's record |
| `GET /api/students/999` | 404 | `{ error: 'Student not found' }` |
| `POST /api/students` (valid body) | 201 | New student + Location header |
| `POST /api/students` (missing name) | 400 | `{ fields: ['name'] }` |
| `PATCH /api/students/1` body: `{"gpa":4.0}` | 200 | Updated student |
| `DELETE /api/students/2` | 204 | Empty body |
| `GET /api/students/2` (after delete) | 404 | Not found error |
| `GET /api/noroute` | 404 | Cannot GET /api/noroute |

---

## Deliverables

Submit your `lab11-registrar` folder zipped (excluding `node_modules`). Required files:

1. `app.js` and `server.js`
2. `routes/students.js` — all 5 CRUD endpoints
3. `routes/courses.js` — GET all, GET by ID, POST
4. `middleware/validate.js` — `requireFields` factory
5. `middleware/errorHandler.js` — `notFound` and `errorHandler`
6. `utils/errors.js` — `AppError`, `NotFoundError`, `ValidationError`
7. `data/students.js` — in-memory data layer
8. A screenshot or export of your Postman/Thunder Client test results

---

## Grading Rubric

| Criterion | Points |
|---|---|
| All 5 student CRUD endpoints return correct status codes and response shapes | 25 |
| `requireFields` middleware blocks invalid POST requests with 400 | 15 |
| `NotFoundError` and `ValidationError` reach the global error handler | 15 |
| `GET /api/students?major=` filter returns correct subset | 10 |
| `errorHandler` returns `stack` only in development mode | 10 |
| `app.js` and `server.js` separated correctly | 10 |
| `helmet`, `cors`, `morgan` configured correctly | 10 |
| Testing screenshot shows all 11 test cases with expected results | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: asyncHandler Wrapper and Custom Error Classes

Refactor all async route handlers to use the `asyncHandler` utility and add an `UnauthorizedError` class for a protected endpoint.

1. Create `utils/asyncHandler.js`:

```js
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

module.exports = asyncHandler;
```

1. Add `UnauthorizedError` to `utils/errors.js`:

```js
class UnauthorizedError extends AppError {
  constructor(message = 'Unauthorized') {
    super(message, 401, 'UNAUTHORIZED');
  }
}

module.exports = { AppError, NotFoundError, ValidationError, UnauthorizedError };
```

1. Refactor `routes/students.js` to wrap every async handler with `asyncHandler` and remove all `try/catch` blocks. Import it at the top: `const asyncHandler = require('../utils/asyncHandler');`. Then change each route handler signature from `async (req, res, next)` to `asyncHandler(async (req, res, next))`.

1. Add a protected `GET /api/students/export` route that requires an `X-Admin-Key` header matching the value of `process.env.ADMIN_KEY`. If the header is missing or wrong, `throw new UnauthorizedError('Admin key required')`. If correct, respond with the full student array as CSV text (`Content-Type: text/csv`). Add `ADMIN_KEY=txwes-secret` to `.env` and test the endpoint with and without the correct header.

### Challenge 2: Rate Limiting and Request ID Middleware

Add per-IP rate limiting and a request ID header to every response.

1. Install the rate limiting package:

```bash
npm install express-rate-limit
```

1. Create `middleware/requestId.js` that attaches a unique request ID to both `req` and the response header:

```js
const { randomUUID } = require('crypto');

function requestId(req, res, next) {
  req.requestId = randomUUID();
  res.set('X-Request-Id', req.requestId);
  next();
}

module.exports = requestId;
```

1. In `app.js`, register the rate limiter and request ID middleware before routes:

```js
const rateLimit = require('express-rate-limit');
const requestId = require('./middleware/requestId');

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 30,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Too many requests', code: 'RATE_LIMITED' }
});

app.use(requestId);
app.use(limiter);
```

1. Test that every response includes an `X-Request-Id` header (visible in Thunder Client's response headers panel). To trigger the rate limit, send more than 30 requests within one minute and verify the `429` response with `{ "error": "Too many requests", "code": "RATE_LIMITED" }`.

### Reflection Questions

1. The `asyncHandler` wrapper catches rejected promises and calls `next(err)`. Without it, an unhandled rejection in an `async` route function in older versions of Express (before Express 5) would cause the Node.js process to crash or hang. How does Express 5 change this behavior, and why is `asyncHandler` still considered a best practice even with Express 5?
2. The rate limiter stores request counts in memory by default. If the API is deployed across multiple Lambda instances or multiple Node.js processes, why does an in-memory rate limiter fail to enforce the limit accurately, and what storage backend would you use instead?
