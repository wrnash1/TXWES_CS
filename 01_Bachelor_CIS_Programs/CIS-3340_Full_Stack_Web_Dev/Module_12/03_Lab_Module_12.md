# Lab 12: JWT Authentication for the Registrar API

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90–120 minutes

---

## Objectives

By completing this lab you will:

- Add JWT-based authentication to the Lab 11 Express API
- Hash passwords with bcrypt before storing them
- Issue signed JWTs on login and registration
- Write `requireAuth` and `requireRole` middleware
- Protect routes based on authentication and role
- Write a complete Postman test collection covering the auth flow

---

## Prerequisites

- Lab 11 complete (registrar API with students and courses routes)
- Module 12 video and reading guide complete
- Postman installed (desktop app or VS Code Thunder Client)

---

## Part 1: Install Dependencies and Update .env (10 minutes)

### Step 1 — Install packages

In your `lab11-registrar` directory (or a copy renamed `lab12-auth`):

```bash
npm install jsonwebtoken bcryptjs
```

### Step 2 — Update .env

Add `JWT_SECRET` to your `.env` file:

```text
NODE_ENV=development
PORT=3000
FRONTEND_URL=http://localhost:5173
JWT_SECRET=txwes-super-secret-dev-key-change-in-production
JWT_EXPIRES_IN=24h
```

**Security note**: In production, `JWT_SECRET` must be a randomly generated 256-bit string stored in AWS Secrets Manager or Systems Manager Parameter Store — never in code or committed `.env` files.

---

## Part 2: Custom Error Classes (5 minutes)

### Step 3 — Add UnauthorizedError and ForbiddenError to utils/errors.js

Open `utils/errors.js` and add two new classes below the existing ones:

```js
class UnauthorizedError extends AppError {
  constructor(message = 'Unauthorized') {
    super(message, 401, 'UNAUTHORIZED');
  }
}

class ForbiddenError extends AppError {
  constructor(message = 'Forbidden') {
    super(message, 403, 'FORBIDDEN');
  }
}

// Update module.exports
module.exports = { AppError, NotFoundError, ValidationError, UnauthorizedError, ForbiddenError };
```

---

## Part 3: User Store (10 minutes)

### Step 4 — Create data/users.js

```js
// data/users.js
const users = [];
let nextId = 1;

module.exports = {
  findByEmail: (email) =>
    users.find(u => u.email.toLowerCase() === email.toLowerCase()),
  findById: (id) => users.find(u => u.id === id),
  create: (data) => {
    const user = { id: nextId++, ...data, createdAt: new Date().toISOString() };
    users.push(user);
    return user;
  },
  // Never expose passwordHash in list results
  getAll: () => users.map(({ passwordHash, ...safe }) => safe),
};
```

---

## Part 4: Auth Middleware (15 minutes)

### Step 5 — Create middleware/auth.js

```js
// middleware/auth.js
const jwt = require('jsonwebtoken');
const { UnauthorizedError, ForbiddenError } = require('../utils/errors');

function requireAuth(req, res, next) {
  const header = req.headers.authorization;

  if (!header || !header.startsWith('Bearer ')) {
    return next(new UnauthorizedError('No token provided'));
  }

  const token = header.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return next(new UnauthorizedError('Token has expired — please log in again'));
    }
    next(new UnauthorizedError('Invalid token'));
  }
}

function requireRole(...allowedRoles) {
  return (req, res, next) => {
    if (!req.user) {
      return next(new UnauthorizedError('Authentication required'));
    }
    if (!allowedRoles.includes(req.user.role)) {
      return next(new ForbiddenError(
        `This action requires one of these roles: ${allowedRoles.join(', ')}`
      ));
    }
    next();
  };
}

module.exports = { requireAuth, requireRole };
```

---

## Part 5: Auth Routes (25 minutes)

### Step 6 — Create routes/auth.js

```js
// routes/auth.js
const { Router } = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const db = require('../data/users');
const { requireFields } = require('../middleware/validate');
const { ValidationError, UnauthorizedError } = require('../utils/errors');
const { requireAuth } = require('../middleware/auth');

const router = Router();

// POST /api/auth/register
router.post(
  '/register',
  requireFields(['name', 'email', 'password']),
  async (req, res, next) => {
    try {
      const { name, email, password } = req.body;

      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        return next(new ValidationError('Invalid email address format'));
      }
      if (password.length < 8) {
        return next(new ValidationError('Password must be at least 8 characters'));
      }
      if (db.findByEmail(email)) {
        return res.status(409).json({
          error: 'An account with that email already exists',
          code: 'EMAIL_EXISTS',
        });
      }

      const passwordHash = await bcrypt.hash(password, 12);
      const user = db.create({ name, email, passwordHash, role: 'student' });

      const token = jwt.sign(
        { userId: user.id, email: user.email, role: user.role },
        process.env.JWT_SECRET,
        { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
      );

      res.status(201).json({
        message: 'Registration successful',
        token,
        user: { id: user.id, name: user.name, email: user.email, role: user.role },
      });
    } catch (err) {
      next(err);
    }
  }
);

// POST /api/auth/login
router.post(
  '/login',
  requireFields(['email', 'password']),
  async (req, res, next) => {
    try {
      const { email, password } = req.body;

      // Generic error — do not reveal which field is wrong
      const genericError = new UnauthorizedError('Invalid email or password');

      const user = db.findByEmail(email);
      if (!user) return next(genericError);

      const valid = await bcrypt.compare(password, user.passwordHash);
      if (!valid) return next(genericError);

      const token = jwt.sign(
        { userId: user.id, email: user.email, role: user.role },
        process.env.JWT_SECRET,
        { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
      );

      res.status(200).json({
        token,
        user: { id: user.id, name: user.name, email: user.email, role: user.role },
      });
    } catch (err) {
      next(err);
    }
  }
);

// GET /api/auth/profile — protected; returns decoded JWT claims
router.get('/profile', requireAuth, (req, res) => {
  res.status(200).json({
    userId: req.user.userId,
    email: req.user.email,
    role: req.user.role,
    issuedAt: new Date(req.user.iat * 1000).toISOString(),
    expiresAt: new Date(req.user.exp * 1000).toISOString(),
  });
});

module.exports = router;
```

---

## Part 6: Protect the Students Routes (10 minutes)

### Step 7 — Add auth to routes/students.js

Add this import at the top of `routes/students.js`:

```js
const { requireAuth, requireRole } = require('../middleware/auth');
```

Then update the route definitions:

```js
// Public — anyone can view
router.get('/', (req, res) => { ... });

// Protected — must be logged in to view individual records
router.get('/:id', requireAuth, (req, res, next) => { ... });

// Protected — must be logged in to create
router.post('/', requireAuth, requireFields(['name', 'email', 'major']), (req, res, next) => { ... });

// Protected — logged in + role check
router.patch('/:id', requireAuth, requireRole('admin', 'staff', 'student'), (req, res, next) => { ... });

// Protected — admin only
router.delete('/:id', requireAuth, requireRole('admin'), (req, res, next) => { ... });
```

---

## Part 7: Mount Auth Routes in app.js (5 minutes)

### Step 8 — Update app.js

Add the auth router before the students and courses routes:

```js
app.use('/api/auth',     require('./routes/auth'));
app.use('/api/students', require('./routes/students'));
app.use('/api/courses',  require('./routes/courses'));
```

Start the server: `npm run dev`

---

## Part 8: Postman Testing (20 minutes)

### Step 9 — Create the collection

Create a new Postman collection "Lab 12 — Auth". Add a collection variable `token` with an empty initial value.

In the Login request Tests tab:

```js
const json = pm.response.json();
if (json.token) pm.collectionVariables.set('token', json.token);
```

In every protected request Authorization tab: Bearer Token → `{{token}}`.

### Step 10 — Execute the test sequence

| Step | Method | Endpoint | Notes | Expected Status |
|---|---|---|---|---|
| 1 | POST | /api/auth/register | Valid body | 201 |
| 2 | POST | /api/auth/register | Same email again | 409 |
| 3 | POST | /api/auth/register | Password less than 8 chars | 400 |
| 4 | POST | /api/auth/login | Correct credentials | 200 — saves token |
| 5 | POST | /api/auth/login | Wrong password | 401 |
| 6 | GET | /api/auth/profile | Valid Bearer token | 200 |
| 7 | GET | /api/auth/profile | No Authorization header | 401 |
| 8 | GET | /api/students | No token (public) | 200 |
| 9 | GET | /api/students/1 | Valid token | 200 |
| 10 | GET | /api/students/1 | No token | 401 |
| 11 | DELETE | /api/students/1 | Valid token (student role) | 403 |
| 12 | DELETE | /api/students/1 | Tampered token (change one char) | 401 |

---

## Expected Behavior Summary

- Registration hashes the password with bcrypt — the plaintext is never stored.
- Login uses `bcrypt.compare` — it never sees the stored hash as plaintext.
- Both endpoints issue a signed JWT valid for 24 hours.
- `GET /api/auth/profile` decodes and returns JWT claims without a database query.
- `DELETE /api/students/:id` returns 403 for student-role tokens.
- All 4xx responses include `error` and `code` fields.

---

## Deliverables

Submit your `lab12-auth` folder zipped (excluding `node_modules`). Required files:

1. `routes/auth.js` — register, login, profile endpoints
2. `middleware/auth.js` — `requireAuth` and `requireRole`
3. `data/users.js` — in-memory user store
4. `utils/errors.js` — updated with `UnauthorizedError` and `ForbiddenError`
5. `routes/students.js` — with auth applied to appropriate routes
6. Updated `app.js` with auth router mounted
7. Postman screenshot or collection export showing all 12 test steps

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Registration hashes password with bcrypt and issues JWT | 20 |
| Login verifies hash, uses generic error message, issues JWT | 15 |
| `requireAuth` reads Bearer token and sets `req.user` | 15 |
| `requireRole` returns 403 for insufficient role | 10 |
| `/api/auth/profile` returns decoded claims without DB lookup | 10 |
| Tampered token returns 401; no-token returns 401 | 10 |
| DELETE returns 403 for student role | 10 |
| Postman screenshot shows all 12 test cases with correct status codes | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Token Refresh Endpoint and Expiry Simulation

Add a `/api/auth/refresh` endpoint that issues a new token from a valid but potentially short-lived one, and test token expiry behavior.

1. Add a `POST /api/auth/refresh` route to `routes/auth.js`. The request must include a valid Bearer token. If the token is valid (not expired), issue a new token with a fresh `exp`:

```js
router.post('/refresh', requireAuth, (req, res) => {
  const { userId, email, role } = req.user;
  const token = jwt.sign(
    { userId, email, role },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
  );
  res.status(200).json({ token });
});
```

1. Add `JWT_SHORT_EXPIRES_IN=10s` to `.env`. Temporarily update `routes/auth.js` to use `process.env.JWT_SHORT_EXPIRES_IN` in the login response instead of `JWT_EXPIRES_IN`. Register, login, wait 11 seconds, then call `GET /api/auth/profile` — verify you receive `401` with `"Token has expired"`.
1. Call `POST /api/auth/refresh` with a valid (non-expired) token and confirm a new token is returned. Decode both the old and new tokens at `https://jwt.io` and verify the `iat` and `exp` claims differ.
1. Revert `JWT_EXPIRES_IN` back to `24h` for the remaining tests.

### Challenge 2: Promote-to-Admin Endpoint with Role Guard

Add an admin-only endpoint that promotes a user from `'student'` to `'staff'` role, and test the 403 behavior for non-admin tokens.

1. Add a `PATCH /api/users/:id/role` route to a new file `routes/users.js`:

```js
const { Router } = require('express');
const userDb = require('../data/users');
const { requireAuth, requireRole } = require('../middleware/auth');
const { NotFoundError, ValidationError } = require('../utils/errors');

const router = Router();

router.patch('/:id/role', requireAuth, requireRole('admin'), (req, res, next) => {
  const id = parseInt(req.params.id);
  if (isNaN(id)) return next(new ValidationError('id must be a number'));

  const { role } = req.body;
  const allowedRoles = ['student', 'staff', 'admin'];
  if (!role || !allowedRoles.includes(role)) {
    return next(new ValidationError(`role must be one of: ${allowedRoles.join(', ')}`));
  }

  const user = userDb.findById(id);
  if (!user) return next(new NotFoundError('User'));

  user.role = role;
  const { passwordHash, ...safe } = user;
  res.status(200).json(safe);
});

module.exports = router;
```

1. Mount the router in `app.js`: `app.use('/api/users', require('./routes/users'));`
1. In Postman, register two accounts. Use one account's token to attempt `PATCH /api/users/2/role` with `{ "role": "staff" }` — confirm `403 Forbidden` since neither account is admin.
1. Manually seed an admin user in `data/users.js` by pushing a pre-hashed record at startup, then log in as that admin and confirm the role promotion succeeds with `200` and the updated user object.

### Reflection Questions

1. The `POST /api/auth/refresh` endpoint in Challenge 1 requires a valid (non-expired) token to issue a new one. This means a user with an expired token cannot refresh — they must log in again. How does the OAuth 2.0 refresh token grant solve this problem, and why does it use a separate long-lived refresh token rather than the access token itself?
2. The in-memory user store loses all registered users when the server restarts. In a production system using PostgreSQL, what constraint would you add to the `users` table to enforce the "email must be unique" rule at the database level rather than relying solely on the application-level `findByEmail` check?
