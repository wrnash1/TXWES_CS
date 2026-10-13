# Reading Guide: Module 13 — Web Security: JWT Authentication & CORS

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3340 &BULL; FULL STACK WEB DEVELOPMENT</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer — Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers the two most important security topics for full-stack web developers: JSON Web Token (JWT) authentication and Cross-Origin Resource Sharing (CORS). You will implement stateless authentication in Express, protect routes with middleware, and connect a React frontend to send authenticated requests. These patterns map directly to the API Gateway Lambda Authorizer pattern tested on the DVA-C02 exam.

---

## 1. JSON Web Tokens

### Structure

A JWT is a dot-separated string with three Base64Url-encoded sections:

```text
header.payload.signature
```

| Section | Content | Encoding |
|---|---|---|
| Header | `{ "alg": "HS256", "typ": "JWT" }` | Base64Url |
| Payload | Claims: `userId`, `email`, `iat`, `exp` | Base64Url |
| Signature | HMAC-SHA256(header + "." + payload, secret) | Binary → Base64Url |

### Claims

| Claim | Meaning |
|---|---|
| `iat` | Issued at (Unix timestamp) |
| `exp` | Expiration (Unix timestamp) |
| `sub` | Subject — typically the user ID |
| Custom | Any application-defined field (`userId`, `email`, `role`) |

### What JWTs Are Not

The payload is Base64Url-encoded, not encrypted. Anyone who possesses the token can decode and read the payload without knowing the secret key. Never include passwords, credit card numbers, or any sensitive data in a JWT payload.

The signature guarantees integrity — the server can detect if the payload was modified — but not confidentiality.

### Signing and Verifying

```javascript
const jwt = require('jsonwebtoken');

// Sign — called at login
const token = jwt.sign(
  { userId: 1, email: 'alice@example.com' },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// Verify — called on every protected request
try {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  // decoded = { userId: 1, email: 'alice@example.com', iat: ..., exp: ... }
} catch (err) {
  if (err.name === 'TokenExpiredError') { /* 401 token expired */ }
  else { /* 401 invalid token */ }
}
```

---

## 2. Password Hashing with bcrypt

Never store plaintext passwords. Use bcrypt to hash before storing and to compare during login.

```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 10;

// At registration — hash before saving to database
const hash = await bcrypt.hash(plaintext, SALT_ROUNDS);

// At login — compare plaintext against stored hash
const valid = await bcrypt.compare(plaintext, storedHash);
// valid is true or false
```

`bcrypt.compare` is resistant to timing attacks — it always takes approximately the same time regardless of whether the match succeeds.

**Authentication error messages:** Return the same message (`Invalid credentials`) whether the email is not found or the password is wrong. Distinct messages reveal which half of the credentials is incorrect.

---

## 3. Login Endpoint

```javascript
// routes/auth.js
router.post('/login', async (req, res, next) => {
  try {
    const { email, password } = req.body;
    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password required' });
    }

    // In production: query the database
    const user = await db.query(
      'SELECT * FROM users WHERE email = $1',
      [email]
    );
    if (!user.rows[0]) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const valid = await bcrypt.compare(password, user.rows[0].password_hash);
    if (!valid) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign(
      { userId: user.rows[0].id, email: user.rows[0].email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN || '1h' }
    );

    res.status(200).json({ token });
  } catch (err) {
    next(err);
  }
});
```

---

## 4. Authentication Middleware

```javascript
// middleware/authenticate.js
const jwt = require('jsonwebtoken');

function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Authorization header required' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
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

### Applying Middleware

```javascript
// Public routes
app.use('/api/auth', require('./routes/auth'));

// Protected routes — authenticate runs before the route handler
app.use('/api/books', authenticate, require('./routes/books'));

// Route-level application (single route)
router.delete('/:id', authenticate, async (req, res, next) => { /* ... */ });
```

### 401 vs 403

| Status | Meaning |
|---|---|
| `401 Unauthorized` | No valid credentials provided (missing/expired/invalid token) |
| `403 Forbidden` | Valid credentials but insufficient permissions (e.g., deleting another user's resource) |

---

## 5. Token Storage Trade-offs

| Location | XSS Risk | CSRF Risk | Notes |
|---|---|---|---|
| `localStorage` | High — JS can read it | None | Simple to implement; avoid for sensitive apps |
| `sessionStorage` | High — JS can read it | None | Cleared when tab closes |
| `httpOnly` Cookie | None — JS cannot read it | Medium | More secure; requires CSRF protection on mutating requests |

For course labs, `localStorage` is acceptable. In production, prefer `httpOnly` cookies with `SameSite=Strict` or CSRF tokens.

---

## 6. Sending JWT from React

```javascript
// Helper — attaches Authorization header to every request
const authFetch = (token) => (url, options = {}) =>
  fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
      ...options.headers
    }
  });

// Usage
const res = await authFetch(token)('/api/books');
```

### Persisting the Token Across Page Reloads

```javascript
// On login — store
localStorage.setItem('token', token);

// On app load — restore
const token = localStorage.getItem('token') ?? null;

// On logout — remove
localStorage.removeItem('token');
```

### Conditional Rendering Based on Auth State

```jsx
function App() {
  const [token, setToken] = useState(
    () => localStorage.getItem('token')
  );

  if (!token) return <LoginForm onLogin={setToken} />;
  return <Dashboard token={token} onLogout={() => { localStorage.removeItem('token'); setToken(null); }} />;
}
```

---

## 7. CORS Preflight for Authenticated Requests

When a browser sends a cross-origin request with custom headers (like `Authorization`), it first sends an HTTP `OPTIONS` preflight request to ask whether the server allows it.

### Preflight Request

```text
OPTIONS /api/books HTTP/1.1
Origin: http://localhost:5173
Access-Control-Request-Method: GET
Access-Control-Request-Headers: Authorization, Content-Type
```

### Required Express Configuration

```javascript
app.use(cors({
  origin: process.env.ALLOWED_ORIGIN || 'http://localhost:5173',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true  // required if using cookies
}));
```

`Authorization` must appear in `allowedHeaders`. If it is missing, the browser blocks the actual request after the preflight fails.

### When Preflight Is Triggered

A CORS preflight occurs when:

- The request method is not `GET`, `POST`, or `HEAD`
- The request includes custom headers (including `Authorization`)
- The `Content-Type` is not `application/x-www-form-urlencoded`, `multipart/form-data`, or `text/plain`

---

## 8. AWS Lambda Authorizer Pattern

In AWS, a Lambda Authorizer sits in front of API Gateway and verifies JWTs before the backend Lambda function is invoked.

```text
Client → API Gateway → Lambda Authorizer → IAM Policy
                              ↓
                    (if Allow) → Lambda function → RDS/DynamoDB
```

The Lambda Authorizer:

1. Receives the `Authorization` header from the API Gateway event
2. Extracts and verifies the JWT
3. Returns an IAM policy document: `{ "Effect": "Allow" or "Deny", "Resource": "arn:aws:..." }`
4. API Gateway caches the policy by token to avoid calling the authorizer on every request

This pattern is tested directly on the DVA-C02 exam.

---

## 9. Exam and Interview Tips

1. The JWT payload is Base64Url-encoded, not encrypted. Never put secret data in it.

2. `jwt.verify()` throws `TokenExpiredError` for expired tokens and `JsonWebTokenError` for tampered tokens. Catch both and return `401`.

3. Return `401` when credentials are absent or invalid. Return `403` when credentials are valid but the user lacks permission for the specific resource.

4. The `bcrypt.compare` function always takes the same amount of time — it is safe against timing attacks that try to determine whether an email is registered.

5. CORS preflight (`OPTIONS`) is triggered by custom headers. `Authorization` must be listed in `allowedHeaders`. Missing it silently blocks authenticated requests.

6. `credentials: true` in the CORS configuration is required when the browser sends cookies. The client must also set `credentials: 'include'` in the fetch call.

7. A Lambda Authorizer verifies a JWT and returns an IAM policy to API Gateway. API Gateway caches the policy by the token value (configurable TTL). This is the standard DVA-C02 auth pattern for serverless APIs.

8. Storing tokens in `localStorage` is simple but vulnerable to XSS. `httpOnly` cookies cannot be read by JavaScript — they are more secure but require CSRF protection on write operations.

---

## 10. Study Checklist

- [ ] Explain the three parts of a JWT and what each part contains
- [ ] Sign a JWT with `jwt.sign()` including `userId` and an expiration
- [ ] Verify a JWT with `jwt.verify()` and handle `TokenExpiredError`
- [ ] Hash a password with bcrypt before storing it
- [ ] Compare a login password against a bcrypt hash
- [ ] Write an `authenticate` middleware that extracts and verifies a Bearer token
- [ ] Return the same error message for "user not found" and "wrong password"
- [ ] Apply authentication middleware to specific Express routes
- [ ] Configure Express CORS to allow the `Authorization` header in `allowedHeaders`
- [ ] Send the JWT from React using the `Authorization: Bearer` header pattern
- [ ] Explain the difference between 401 and 403 HTTP status codes
- [ ] Describe the AWS Lambda Authorizer flow and why API Gateway caches the policy

---

## 11. Supplemental Resources

The following free, open-access resources go deeper on Module 13 topics:

**1. OWASP — JSON Web Token Security Cheat Sheet**
[https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)
The OWASP authoritative reference covering JWT attack vectors — `alg: none` bypass, weak secret brute force, claim confusion — and the corresponding defenses including algorithm pinning, secret entropy requirements, and token revocation strategies. Directly reinforces the security concepts in Sections 1 and 5 of this guide.

**2. MDN Web Docs — Cross-Origin Resource Sharing (CORS)**
[https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
Complete reference for the CORS protocol including preflight mechanics, `Access-Control-Allow-Headers`, `Access-Control-Allow-Credentials`, and the browser same-origin enforcement model — directly aligned to Section 7 (CORS for authenticated requests) and the `allowedHeaders: ['Authorization']` pattern in Lab 13.

**3. npm — jsonwebtoken package documentation**
[https://www.npmjs.com/package/jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)
The official `jsonwebtoken` package documentation covering `jwt.sign()` options (`expiresIn`, `issuer`, `audience`), `jwt.verify()` error types (`TokenExpiredError`, `JsonWebTokenError`, `NotBeforeError`), algorithm options, and security considerations — the primary reference for all JWT code patterns in this module.

**4. AWS Documentation — API Gateway Lambda Authorizer**
[https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
The official AWS documentation for Lambda authorizers covering token-based vs request-based authorizers, IAM policy output format, TTL caching of authorization decisions, and the relationship between the authorizer function and the backend Lambda — the production-scale equivalent of the `authenticate` middleware built in Lab 13.
