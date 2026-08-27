# Lab 13: JWT Authentication for the Bookstore API

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**
**Estimated Time:** 90–120 minutes
**Total Points:** 100

---

## Overview

In this lab you will add JWT-based authentication to the Express bookstore API from Lab 12. You will create a user registration and login endpoint, write authentication middleware, protect the book routes, and update the React frontend to log in, store the token, and send it with every API request.

---

## Prerequisites

- Node.js 18+ and PostgreSQL running locally
- Lab 12 Express API and React frontend both working
- Postman or curl for testing

---

## Part 1: Database Setup (10 minutes)

### Step 1 — Create the users table

Connect to your bookstore database in psql and run:

```sql
CREATE TABLE users (
  id            SERIAL PRIMARY KEY,
  email         VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at    TIMESTAMPTZ DEFAULT NOW()
);
```

Screenshot: psql confirming `CREATE TABLE`.

---

## Part 2: Install Packages and Configure Environment (10 minutes)

### Step 2 — Install dependencies

In your Express project folder:

```bash
npm install jsonwebtoken bcrypt
```

### Step 3 — Add environment variables

Open `.env` and add:

```text
JWT_SECRET=replace-this-with-a-random-32-character-string
JWT_EXPIRES_IN=1h
```

Generate a real secret with:

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

Paste the output as your `JWT_SECRET` value.

---

## Part 3: Registration and Login Routes (25 minutes)

### Step 4 — Create routes/auth.js

Create a new file `routes/auth.js`:

```javascript
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const pool = require('../db');

const router = express.Router();
const SALT_ROUNDS = 10;

// POST /api/auth/register
router.post('/register', async (req, res, next) => {
  try {
    const { email, password } = req.body;

    // TODO 1: Validate that email and password are present.
    // Return 400 with { error: 'Email and password required' } if either is missing.

    // TODO 2: Check whether the email already exists in the users table.
    // Use a parameterized query: SELECT id FROM users WHERE email = $1
    // If a row is returned, respond with 409 and { error: 'Email already registered' }

    // TODO 3: Hash the password with bcrypt using SALT_ROUNDS.
    // Insert the new user: INSERT INTO users (email, password_hash) VALUES ($1, $2) RETURNING id, email
    // Respond with 201 and { id, email } from the returned row.

    /* YOUR CODE HERE */
  } catch (err) {
    next(err);
  }
});

// POST /api/auth/login
router.post('/login', async (req, res, next) => {
  try {
    const { email, password } = req.body;

    // TODO 4: Validate that email and password are present. Return 400 if missing.

    // TODO 5: Query the users table for the email.
    // SELECT id, email, password_hash FROM users WHERE email = $1
    // If no row is found, respond with 401 and { error: 'Invalid credentials' }

    // TODO 6: Use bcrypt.compare to check the password against password_hash.
    // If invalid, respond with 401 and { error: 'Invalid credentials' }
    // Use the SAME error message whether the email was not found or the password was wrong.

    // TODO 7: Sign a JWT using process.env.JWT_SECRET and process.env.JWT_EXPIRES_IN.
    // Include { userId: user.id, email: user.email } as the payload.
    // Respond with 200 and { token }.

    /* YOUR CODE HERE */
  } catch (err) {
    next(err);
  }
});

module.exports = router;
```

Complete TODOs 1 through 7.

### Step 5 — Mount the auth router

In `index.js`, register the auth routes before any authenticated routes:

```javascript
// TODO 8: Mount the auth router at /api/auth
// app.use('/api/auth', require('./routes/auth'));
/* YOUR CODE HERE */
```

Complete TODO 8.

### Step 6 — Test registration and login

Start the server and test with curl or Postman:

```bash
# Register a new user
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"password123"}'
# Expected: 201 { "id": 1, "email": "alice@example.com" }

# Login
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"password123"}'
# Expected: 200 { "token": "eyJ..." }

# Wrong password
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"wrong"}'
# Expected: 401 { "error": "Invalid credentials" }
```

Screenshot: all three responses.

---

## Part 4: Authentication Middleware (15 minutes)

### Step 7 — Create middleware/authenticate.js

Create a new file `middleware/authenticate.js`:

```javascript
const jwt = require('jsonwebtoken');

function authenticate(req, res, next) {
  // TODO 9: Read req.headers.authorization.
  // If missing or does not start with 'Bearer ', return 401 { error: 'Authorization header required' }

  // TODO 10: Extract the token from the header (split on space, take index 1).
  // Call jwt.verify(token, process.env.JWT_SECRET) inside a try/catch.
  // On success: set req.user = decoded payload, call next()
  // On TokenExpiredError: return 401 { error: 'Token expired' }
  // On any other error: return 401 { error: 'Invalid token' }

  /* YOUR CODE HERE */
}

module.exports = authenticate;
```

Complete TODOs 9 and 10.

### Step 8 — Protect the book routes

In `index.js`, apply the authenticate middleware to the books router:

```javascript
const authenticate = require('./middleware/authenticate');

// TODO 11: Change the books route registration to require authentication.
// Before: app.use('/api/books', require('./routes/books'));
// After:  app.use('/api/books', authenticate, require('./routes/books'));
/* YOUR CODE HERE */
```

Complete TODO 11.

### Step 9 — Test protected routes

```bash
# No token — should fail
curl http://localhost:3000/api/books
# Expected: 401 { "error": "Authorization header required" }

# With valid token (replace TOKEN with the value from login)
curl -H "Authorization: Bearer TOKEN" http://localhost:3000/api/books
# Expected: 200 JSON array of books
```

Screenshot: both responses showing the 401 and then the 200 with the token.

---

## Part 5: React Authentication (25 minutes)

### Step 10 — Update CORS configuration

In the Express `index.js`, update the CORS configuration to allow the `Authorization` header:

```javascript
app.use(cors({
  origin: 'http://localhost:5173',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  // TODO 12: Add allowedHeaders: ['Content-Type', 'Authorization']
  /* YOUR CODE HERE */
}));
```

Complete TODO 12.

### Step 11 — Create the useAuth hook

In the React project, create `src/hooks/useAuth.js`:

```javascript
import { useState } from 'react';

const API_URL = 'http://localhost:3000';

export function useAuth() {
  const [token, setToken] = useState(
    () => localStorage.getItem('token')
  );

  const login = async (email, password) => {
    // TODO 13: POST to /api/auth/login with { email, password }
    // Check res.ok — throw an Error with a message if login fails
    // On success: extract token from JSON, store in localStorage, call setToken(token)

    /* YOUR CODE HERE */
  };

  const logout = () => {
    // TODO 14: Remove 'token' from localStorage and call setToken(null)
    /* YOUR CODE HERE */
  };

  return { token, login, logout };
}
```

Complete TODOs 13 and 14.

### Step 12 — Create the LoginForm component

Create `src/components/LoginForm.jsx`:

```jsx
import { useState } from 'react';

function LoginForm({ onLogin }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      await onLogin(email, password);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 400, margin: '40px auto' }}>
      <h2>Sign In</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        style={{ display: 'block', width: '100%', padding: '8px', marginBottom: '8px' }}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        style={{ display: 'block', width: '100%', padding: '8px', marginBottom: '8px' }}
      />
      <button type="submit" style={{ padding: '8px 20px' }}>Log In</button>
    </form>
  );
}

export default LoginForm;
```

### Step 13 — Update App.jsx to gate on authentication

Update `src/App.jsx`:

```jsx
import { useAuth } from './hooks/useAuth';
import { useBooks } from './hooks/useBooks';
import LoginForm from './components/LoginForm';
import AddBookForm from './components/AddBookForm';

function App() {
  const { token, login, logout } = useAuth();

  // TODO 15: If token is null, render <LoginForm onLogin={login} /> instead of the dashboard.

  // TODO 16: Update the useBooks hook (or its internal fetch calls) to pass the token
  // in the Authorization header. Pass token as a parameter or via context.
  // Hint: add a `token` parameter to useBooks() and include it in the fetch headers.

  // ... rest of App component (books list, add form, delete buttons)
  /* YOUR CODE HERE */
}

export default App;
```

Complete TODOs 15 and 16. For TODO 16, update `src/hooks/useBooks.js` to accept a `token` argument and pass it as `Authorization: Bearer ${token}` in the fetch options.

### Step 14 — Test the full flow

1. Open `http://localhost:5173`. You should see the login form (no token in localStorage).
2. Enter `alice@example.com` / `password123`. The dashboard should load with the book list.
3. Open DevTools → Application → Local Storage. Verify the token is stored.
4. Paste the token into jwt.io and confirm the `userId` and `email` claims.
5. Click Logout. The login form should reappear and the token should be removed from localStorage.
6. Reload the page after logging in — the token should be restored from localStorage and the dashboard should load without re-entering credentials.

Screenshot: each of the six steps above.

---

## Expected Final Output

- `POST /api/auth/register` creates a user with a bcrypt-hashed password
- `POST /api/auth/login` returns a signed JWT on success; `401` on wrong credentials
- `GET /api/books` without a token returns `401`
- `GET /api/books` with a valid `Authorization: Bearer` header returns book data
- React shows the login form when unauthenticated and the dashboard when authenticated
- The token persists across page reloads via `localStorage`

---

## Deliverables

Submit a zip of your Express project folder (excluding `node_modules`) and a zip of your React project folder (excluding `node_modules`). Your submission must include:

1. `routes/auth.js` — register and login endpoints
2. `middleware/authenticate.js` — Bearer token verification
3. `index.js` — updated with auth routes and protected books route
4. React `src/hooks/useAuth.js`
5. React `src/components/LoginForm.jsx`
6. React `src/App.jsx` — gated on authentication

---

## Grading Rubric

| Criterion | Points |
|---|---|
| `users` table created; register endpoint hashes password with bcrypt | 15 |
| Login returns JWT; same error message for missing user and wrong password | 15 |
| Authenticate middleware extracts and verifies Bearer token | 15 |
| Protected books route returns 401 without token, 200 with valid token | 15 |
| CORS `allowedHeaders` includes `Authorization` — preflight succeeds | 10 |
| React shows login form when unauthenticated | 10 |
| React sends `Authorization: Bearer` header on all book API calls | 10 |
| Token persists across page reload; logout clears localStorage | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Token Refresh and Expiry Simulation

Add a `/api/auth/refresh` endpoint and test token expiry behavior end-to-end.

1. Add `JWT_EXPIRES_IN=24h` and `JWT_SHORT_EXPIRES_IN=10s` to your `.env` file.

1. Add a `POST /api/auth/refresh` route to `routes/auth.js`. It must require a valid Bearer token (reuse the `authenticate` middleware) and issue a new token:

```javascript
router.post('/refresh', authenticate, (req, res) => {
  const { userId, email } = req.user;
  const token = jwt.sign(
    { userId, email },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
  );
  res.json({ token });
});
```

1. Temporarily change the `expiresIn` value in your login route to `process.env.JWT_SHORT_EXPIRES_IN`. Register a new user, log in, and copy the token. Wait 11 seconds, then run:

```bash
curl -H "Authorization: Bearer TOKEN" http://localhost:3000/api/books
# Expected: 401 { "error": "Token expired" }
```

1. Before the token expires, call `POST /api/auth/refresh` with the valid token in the header. Paste both the original and refreshed tokens into `https://jwt.io` and confirm the `iat` and `exp` claims differ. Revert the login route back to `JWT_EXPIRES_IN` when done.

### Challenge 2: Role-Based Access Control

Add a `role` column to the database and an admin-only delete endpoint.

1. Add a `role` column to the `users` table and update the register route:

```sql
ALTER TABLE users ADD COLUMN role VARCHAR(50) DEFAULT 'user' NOT NULL;
```

Update `routes/auth.js` — include `role` in the JWT payload when signing:

```javascript
const token = jwt.sign(
  { userId: user.id, email: user.email, role: user.role },
  process.env.JWT_SECRET,
  { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
);
```

1. Create `middleware/requireRole.js`:

```javascript
const { ForbiddenError } = require('../utils/errors');

function requireRole(...allowedRoles) {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Not authenticated' });
    }
    if (!allowedRoles.includes(req.user.role)) {
      return next(new ForbiddenError(
        `Requires one of: ${allowedRoles.join(', ')}`
      ));
    }
    next();
  };
}

module.exports = requireRole;
```

1. In `routes/books.js`, protect the DELETE endpoint with both `authenticate` and `requireRole('admin')`:

```javascript
const authenticate  = require('../middleware/authenticate');
const requireRole   = require('../middleware/requireRole');

// DELETE /api/books/:id — admin only
router.delete(
  '/:id',
  authenticate,
  requireRole('admin'),
  async (req, res, next) => {
    // existing delete handler
  }
);
```

1. In psql, manually set one user to `admin`:

```sql
UPDATE users SET role = 'admin' WHERE email = 'alice@example.com';
```

Log in as Alice and confirm `DELETE /api/books/1` returns `200`. Log in as a regular user and confirm `DELETE /api/books/1` returns `403 Forbidden`.

### Reflection Questions

1. The refresh endpoint in Challenge 1 requires a valid (non-expired) token to issue a new one. This means a user with an expired token must log in again. The OAuth 2.0 specification solves this with a separate long-lived refresh token that is never used for API calls. Why is it safer to use a dedicated refresh token rather than accepting expired access tokens for refresh?
1. Challenge 2 embeds the user's `role` directly in the JWT payload. If an admin demotes a user in the database, the user's token still carries `role: 'admin'` until it expires. Describe two strategies that mitigate this stale-role problem — one that keeps JWTs fully stateless and one that introduces a small amount of server-side state.
