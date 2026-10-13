# Video Script: Module 13 — Web Security: JWT Authentication & CORS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**
**Estimated Duration:** 23–25 minutes
**Certification Alignment:** AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with Express project, Postman or curl, jwt.io in browser
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for browser/Postman; [PAUSE] for slide transitions
- Have jwt.io open in one browser tab, Postman open, and the Express project from Module 08 ready
- Demonstrate token inspection on jwt.io during Section 3

---

## Section 1: Introduction — Why Authentication Matters (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 13 — Web Security: JWT Authentication and CORS.

So far you have built APIs that respond to any request from any caller. That works for public data, but most real applications have private data. A user should only see their own orders, their own account, their own projects — not everyone else's.

Today you will implement stateless authentication using JSON Web Tokens. You will build a login endpoint that issues a token, protect routes with middleware that verifies the token, and connect the React frontend to send the token on every authenticated request. You will also complete your understanding of CORS — specifically the preflight OPTIONS request, which becomes critical when your React app sends custom headers.

For the AWS DVA-C02 exam: JWT is the mechanism behind API Gateway Lambda Authorizers. Understanding JWT structure and validation is directly tested.

[PAUSE — slide: Module 13 Learning Objectives]

---

## Section 2: What Is a JSON Web Token? (1:30 – 5:00)

A JSON Web Token is a compact, self-contained string that carries claims — statements about the user. It has three parts separated by dots: a header, a payload, and a signature.

[SHOW BROWSER — jwt.io]

Paste this token into jwt.io and I'll walk you through it:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsImVtYWlsIjoiYWxpY2VAZXhhbXBsZS5jb20iLCJpYXQiOjE2OTk5MDAwMDAsImV4cCI6MTY5OTkwMzYwMH0.abc123signature
```

The header is Base64Url-encoded JSON: `{ "alg": "HS256", "typ": "JWT" }`. It tells you which signing algorithm was used.

The payload is also Base64Url-encoded JSON. In this token it contains: `userId`, `email`, `iat` (issued at timestamp), and `exp` (expiration timestamp).

The signature is an HMAC-SHA256 hash of the header and payload using a secret key known only to the server. The server recomputes this hash on every request. If the result matches the signature in the token, the token has not been tampered with.

[PAUSE — slide: JWT structure diagram — header.payload.signature]

Three critical things about JWT:

First: the payload is Base64Url-encoded, not encrypted. Anyone who has the token can read the claims. Never put passwords, credit card numbers, or sensitive data in a JWT payload.

Second: the signature is what makes the token trustworthy. An attacker cannot change the `userId` in the payload without invalidating the signature — and they cannot recompute a valid signature without the secret key.

Third: JWTs are stateless. The server does not store sessions. Every request carries a self-contained proof of identity that the server can verify with one cryptographic operation.

[PAUSE — slide: JWT — what it is and what it is not]

---

## Section 3: Building Login and Protected Routes (5:00 – 13:00)

Let me build this step by step. First, install the required packages.

[SHOW CODE]

```bash
npm install jsonwebtoken bcrypt dotenv
```

`jsonwebtoken` creates and verifies JWTs. `bcrypt` hashes passwords. Never store plaintext passwords.

Add your JWT secret to `.env`:

```text
JWT_SECRET=a-very-long-random-string-at-least-32-characters
JWT_EXPIRES_IN=1h
```

Now the login route. For this demonstration I am using an in-memory user record — in production this would query your database:

[SHOW CODE]

```javascript
// routes/auth.js
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const router = express.Router();

// In production: query the database for the user
const USERS = [
  {
    id: 1,
    email: 'alice@example.com',
    // bcrypt hash of 'password123'
    passwordHash: '$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy'
  }
];

router.post('/login', async (req, res, next) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password required' });
    }

    const user = USERS.find(u => u.email === email);
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign(
      { userId: user.id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN }
    );

    res.status(200).json({ token });
  } catch (err) {
    next(err);
  }
});

module.exports = router;
```

Notice: I return the same error message for both "user not found" and "wrong password". This prevents attackers from knowing whether an email address is registered.

Now the authentication middleware:

[SHOW CODE]

```javascript
// middleware/authenticate.js
const jwt = require('jsonwebtoken');

function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing or invalid Authorization header' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded; // { userId, email, iat, exp }
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return res.status(401).json({ error: 'Token expired' });
    }
    return res.status(401).json({ error: 'Invalid token' });
  }
}

module.exports = authenticate;
```

The `Authorization: Bearer <token>` header is the standard format for sending JWTs. The middleware strips the `Bearer` prefix and trailing space, verifies the token, and attaches the decoded payload to `req.user`. Every protected route handler can then access `req.user.userId` and `req.user.email`.

Apply the middleware to protected routes:

[SHOW CODE]

```javascript
// index.js
const authenticate = require('./middleware/authenticate');

// Public routes — no authentication
app.use('/api/auth', require('./routes/auth'));

// Protected routes — authentication required
app.use('/api/books', authenticate, require('./routes/books'));
```

[SHOW BROWSER — Postman]

Send `POST /api/auth/login` with `{ "email": "alice@example.com", "password": "password123" }`. You get back a token.

Now send `GET /api/books` with no token — you get `401 Missing or invalid Authorization header`.

Add the `Authorization: Bearer <token>` header and try again — you get the book list.

[PAUSE — slide: Login → token → protected request flow diagram]

---

## Section 4: Sending JWT from React (13:00 – 18:00)

Now on the React side. The login form sends credentials to the API, stores the token, and attaches it to subsequent requests.

[SHOW CODE]

```jsx
// src/hooks/useAuth.js
import { useState } from 'react';

export function useAuth() {
  const [token, setToken] = useState(
    () => localStorage.getItem('token') // restore on reload
  );

  const login = async (email, password) => {
    const res = await fetch('http://localhost:3000/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    if (!res.ok) throw new Error('Login failed');
    const { token } = await res.json();
    localStorage.setItem('token', token);
    setToken(token);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  return { token, login, logout };
}
```

Using the token in a fetch call:

[SHOW CODE]

```jsx
// Authenticated fetch helper
const authFetch = (url, options = {}) => {
  return fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  });
};

// Example usage
const res = await authFetch('http://localhost:3000/api/books');
```

I am storing the token in `localStorage` here because it is simple to demonstrate. In production, `httpOnly` cookies are more secure against XSS attacks — the browser cannot read them with JavaScript, so a malicious script cannot steal the token. We cover that trade-off in detail in the reading guide.

[PAUSE — slide: localStorage vs httpOnly cookie trade-offs]

---

## Section 5: CORS Preflight for Authenticated Requests (18:00 – 23:00)

When the React app sends a request with the `Authorization` header, the browser sends a CORS preflight first — an `OPTIONS` request to check whether the server permits the custom header.

[SHOW CODE]

```text
OPTIONS /api/books HTTP/1.1
Origin: http://localhost:5173
Access-Control-Request-Method: GET
Access-Control-Request-Headers: Authorization, Content-Type
```

The Express `cors()` middleware handles this automatically if configured correctly:

[SHOW CODE]

```javascript
app.use(cors({
  origin: 'http://localhost:5173',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

The `allowedHeaders` property is critical. If `Authorization` is not listed, the browser will block the actual request after the preflight fails.

[SHOW BROWSER — Network tab]

Open the React app, log in, and navigate to the books page. In the Network tab you will see two requests to `GET /api/books` — the first is the `OPTIONS` preflight, which returns `204 No Content`. The second is the actual `GET` with the `Authorization` header.

[PAUSE — slide: CORS preflight — why it exists and what it checks]

For the AWS exam: API Gateway has its own CORS configuration. You must enable CORS on each API Gateway resource and specify the allowed headers. When using a Lambda Authorizer, the authorizer receives the `Authorization` header, verifies the JWT, and returns an IAM policy telling API Gateway whether to allow or deny the request. API Gateway then calls the Lambda function only if the policy allows it.

[PAUSE — slide: API Gateway + Lambda Authorizer flow]

---

## Conclusion (23:00 – 25:00)

Summary of Module 13:

- A JWT has three parts: header, Base64Url payload, and HMAC signature. The payload is readable — never put secrets in it.
- The signature proves the token has not been tampered with. The server recomputes it on every request.
- JWTs are stateless — no session storage on the server.
- Login endpoint: verify email and password, sign a JWT with `jwt.sign()`, return the token.
- Authentication middleware: extract `Bearer <token>` from the `Authorization` header, verify with `jwt.verify()`, attach decoded payload to `req.user`.
- `TokenExpiredError` and general errors return `401`. Protected routes return `403` when the identity is valid but access is denied.
- React stores the token in `localStorage` or `httpOnly` cookies. Attaches it as `Authorization: Bearer <token>` on every authenticated fetch.
- CORS preflight: `OPTIONS` request checks permitted headers. `Authorization` must be in `allowedHeaders`.
- AWS: Lambda Authorizers verify JWTs before API Gateway calls the Lambda function. This is the standard DVA-C02 pattern.

Lab 13 adds authentication to the full-stack bookstore from Lab 12. See you there.

[END OF SCRIPT]
