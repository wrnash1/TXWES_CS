# Reading Guide: Module 12 — RESTful API Design and Authentication

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Overview

This guide covers REST architectural principles, HTTP conventions, password hashing with bcrypt, JWT authentication, protected routes, and API testing with Postman. These concepts are foundational for building secure production APIs and for the AWS Developer Associate exam.

---

## 1. REST Architectural Constraints

### 1.1 The Six Constraints

REST (Representational State Transfer) is defined by six architectural constraints. An API that satisfies all six is called RESTful.

| Constraint | Description | Practical Impact |
|---|---|---|
| **Client-Server** | Client and server are decoupled; communicate through a uniform interface | Frontend and backend can evolve independently |
| **Stateless** | No session state on the server; each request is self-contained | Enables horizontal scaling; any server can handle any request |
| **Cacheable** | Responses explicitly declare whether they can be cached | Reduces server load; requires correct `Cache-Control` headers |
| **Uniform Interface** | Resource identification in URLs; manipulation via representations | Predictable, self-documenting API surface |
| **Layered System** | Client cannot distinguish direct server connection from intermediary | Enables load balancers, CDNs, API gateways |
| **Code on Demand** | Server can send executable code (optional) | Rarely used in modern APIs |

### 1.2 Statelessness Is Not Optional

The stateless constraint is the most important for scaling. It means the server never stores session state between requests. Authentication state must be carried by the client in every request — typically as a JWT in the `Authorization` header. This allows any node in a cluster to serve any request without consulting a central session store.

Contrast with session-based auth: the server stores a session ID → user mapping in memory or Redis. Every request must hit the same server (sticky sessions) or all servers must share the session store. JWT eliminates this coordination problem.

---

## 2. HTTP Conventions Reference

### 2.1 HTTP Verb Semantics

| Verb | Semantics | Idempotent | Safe | Body |
|---|---|---|---|---|
| GET | Read resource | Yes | Yes | No |
| POST | Create resource | No | No | Yes |
| PUT | Replace resource entirely | Yes | No | Yes |
| PATCH | Update resource partially | No | No | Yes |
| DELETE | Remove resource | Yes | No | No |

**Idempotent**: repeating the same request has the same effect as calling it once.
**Safe**: the request does not modify server state.

### 2.2 Status Code Reference

```text
1xx — Informational
  100 Continue

2xx — Success
  200 OK
  201 Created              -> POST success; include Location: /api/resource/id header
  204 No Content           -> DELETE success; no response body

3xx — Redirection
  301 Moved Permanently
  304 Not Modified         -> cached response still valid

4xx — Client Error
  400 Bad Request          -> invalid JSON, missing fields, malformed input
  401 Unauthorized         -> not authenticated
  403 Forbidden            -> authenticated but lacks permission
  404 Not Found            -> resource does not exist
  405 Method Not Allowed   -> wrong HTTP verb for this endpoint
  409 Conflict             -> duplicate resource (e.g., email already exists)
  422 Unprocessable Entity -> valid syntax but semantic validation failed
  429 Too Many Requests    -> rate limiting

5xx — Server Error
  500 Internal Server Error -> unhandled exception
  502 Bad Gateway          -> upstream server error
  503 Service Unavailable  -> temporarily down
  504 Gateway Timeout      -> upstream timeout
```

### 2.3 401 vs 403 — Critical Distinction

This distinction is tested on DVA-C02.

- **401 Unauthorized**: The request lacks valid authentication credentials. The client should obtain credentials and retry. Common error message: "No token provided" or "Token expired."
- **403 Forbidden**: The client is authenticated but does not have permission for the requested resource. Retry with different credentials will not help. Common error message: "Insufficient permissions."

---

## 3. URL Design Reference

### 3.1 Resource Naming Rules

```text
# Nouns for resources, HTTP verb for actions
GET    /api/students          # list
POST   /api/students          # create
GET    /api/students/42       # single item
PUT    /api/students/42       # full replace
PATCH  /api/students/42       # partial update
DELETE /api/students/42       # delete

# Plural nouns consistently
/api/students  not /api/student
/api/courses   not /api/course

# Hyphens for multi-word, all lowercase
/api/course-enrollments
/api/grade-reports

# Nested resources for relationships
GET  /api/students/42/courses         # enrollments for student 42
POST /api/students/42/courses         # enroll student 42
```

### 3.2 Query Parameters for Filtering

```text
# Filtering
GET /api/students?major=CS&gpa_min=3.5

# Sorting
GET /api/courses?sort=title&order=asc

# Pagination
GET /api/students?page=2&limit=20

# Sparse fieldsets
GET /api/students?fields=id,name,email
```

### 3.3 Versioning

```text
# Version in URL path (most common)
/api/v1/students
/api/v2/students

# Version in header (RFC standard but harder to test)
Accept: application/vnd.txwes.v2+json
```

---

## 4. bcrypt Reference

### 4.1 How bcrypt Works

bcrypt is an adaptive password hashing algorithm designed to be slow. The cost factor (also called salt rounds or work factor) controls the number of iterations: `iterations = 2^costFactor`. A cost factor of 12 means 4,096 iterations. As hardware gets faster, you increase the cost factor to maintain the same elapsed time.

The bcrypt hash format:

```text
$2b$12$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
 ^^ ^^  ^                22 chars                 ^ 31 chars
 |  |   |                 salt                        hash
 |  |   cost factor (12)
 |  algorithm identifier (2b = bcrypt)
 version prefix
```

### 4.2 bcrypt Code Patterns

```js
const bcrypt = require('bcryptjs');

// Registration — hash before storing
async function hashPassword(plaintext) {
  return bcrypt.hash(plaintext, 12);
}

// Login — compare plaintext against stored hash
async function checkPassword(plaintext, storedHash) {
  return bcrypt.compare(plaintext, storedHash);
}

// Example usage
const hash = await hashPassword('myPassword123!');
console.log(hash); // $2b$12$...

const valid = await checkPassword('myPassword123!', hash);  // true
const wrong = await checkPassword('wrongPassword', hash);    // false
```

### 4.3 bcrypt Security Properties

- The salt is randomly generated and embedded in the hash — no separate salt storage needed.
- Two hashes of the same password are different (different random salts) — rainbow table attacks are defeated.
- `bcrypt.compare` is timing-safe — it does not short-circuit on the first mismatched character, preventing timing attacks.
- Never use MD5, SHA-1, or SHA-256 for passwords — they are fast, which makes brute force trivial.

---

## 5. JWT Reference

### 5.1 JWT Structure

A JWT is three base64url-encoded JSON objects separated by dots:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9        <- header
.eyJ1c2VySWQiOjQyLCJyb2xlIjoic3R1ZGVudCJ9   <- payload
.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c <- signature
```

**Header** (decoded):

```json
{ "alg": "HS256", "typ": "JWT" }
```

**Payload** (decoded) — standard claims:

| Claim | Name | Description |
|---|---|---|
| `iss` | Issuer | Who issued the token |
| `sub` | Subject | Who the token is about (user ID) |
| `exp` | Expiration | Unix timestamp after which the token is invalid |
| `iat` | Issued At | Unix timestamp when the token was issued |
| `nbf` | Not Before | Token not valid before this time |

Custom claims go in the payload alongside standard claims. Keep the payload small — it is base64url-encoded, not encrypted.

### 5.2 JWT is Not Encrypted

JWT payloads are only base64url-encoded — any party with the token can read the claims. Never put sensitive data (passwords, SSNs, credit card numbers) in a JWT payload. JWTs are signed (tamper-evident) but not confidential. Use JWE (JSON Web Encryption) if you need encrypted tokens.

### 5.3 JWT Code Patterns

```js
const jwt = require('jsonwebtoken');

// Sign — create a token
const token = jwt.sign(
  { userId: 42, email: 'alice@txwes.edu', role: 'student' },  // payload
  process.env.JWT_SECRET,                                       // secret
  { expiresIn: '24h', issuer: 'txwes-registrar' }              // options
);

// Verify — validate and decode
try {
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  // decoded = { userId: 42, email: '...', role: '...', iat: ..., exp: ... }
} catch (err) {
  if (err.name === 'TokenExpiredError') {
    // handle expired token
  }
  if (err.name === 'JsonWebTokenError') {
    // handle invalid signature or malformed token
  }
}

// Decode without verification (use for debugging only)
const unverified = jwt.decode(token);
```

### 5.4 JWT Storage — Security Tradeoffs

| Storage Location | XSS Risk | CSRF Risk | Notes |
|---|---|---|---|
| `localStorage` | High | Low | JS-accessible; XSS attack can steal tokens |
| `sessionStorage` | High | Low | Same as localStorage; cleared on tab close |
| HttpOnly Cookie | Low | High | JS cannot read; requires CSRF protection |
| Memory (variable) | Low | Low | Lost on page refresh; best for sensitive apps |

For this course, store JWTs in memory (a React state variable) for simplicity. For production, use HttpOnly cookies with CSRF protection or a specialized auth library.

---

## 6. Auth Middleware Implementation

### 6.1 requireAuth Middleware

```js
// middleware/auth.js
const jwt = require('jsonwebtoken');

function requireAuth(req, res, next) {
  const header = req.headers.authorization;
  if (!header?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided', code: 'UNAUTHORIZED' });
  }

  const token = header.split(' ')[1];
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (err) {
    const message = err.name === 'TokenExpiredError' ? 'Token expired' : 'Invalid token';
    res.status(401).json({ error: message, code: 'UNAUTHORIZED' });
  }
}

module.exports = { requireAuth };
```

### 6.2 Role-Based Access Control

```js
function requireRole(...allowedRoles) {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Not authenticated' });
    }
    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Insufficient permissions', code: 'FORBIDDEN' });
    }
    next();
  };
}

// Usage
router.delete('/:id', requireAuth, requireRole('admin', 'staff'), handler);
```

---

## 7. Postman Testing Guide

### 7.1 Setting Up a Collection

Create a new Postman collection called "TxWes Registrar API". Add a collection-level variable `baseUrl = http://localhost:3000` and `token` with an empty initial value.

### 7.2 Auto-Save Token from Login Response

In the login request's Tests tab, add this script:

```js
const json = pm.response.json();
if (json.token) {
  pm.collectionVariables.set('token', json.token);
}
```

### 7.3 Use Token in Protected Requests

In each protected request's Authorization tab, select "Bearer Token" and enter `{{token}}`.

### 7.4 Complete Test Sequence

| Step | Request | Expected Status |
|---|---|---|
| 1 | POST /api/auth/register | 201 |
| 2 | POST /api/auth/register (same email) | 409 |
| 3 | POST /api/auth/login (wrong password) | 401 |
| 4 | POST /api/auth/login (correct) | 200 — save token |
| 5 | GET /api/students (no token) | 401 |
| 6 | GET /api/students (valid token) | 200 |
| 7 | DELETE /api/students/1 (student role) | 403 |
| 8 | GET /api/auth/profile | 200 — shows decoded user |

---

## 8. AWS DVA-C02 Exam Connections

- **API Gateway + REST**: API Gateway natively implements REST routing. It maps HTTP methods and URL paths to Lambda functions or other integrations. Understanding REST conventions is prerequisite knowledge.
- **Amazon Cognito**: Managed JWT issuance, token refresh, user pools, and identity pools. Cognito's access tokens and ID tokens are JWTs. DVA-C02 tests when to use Cognito vs rolling your own auth.
- **JWT verification on Lambda**: A Lambda authorizer (formerly custom authorizer) verifies a JWT and returns an IAM policy allowing or denying the request. The mechanism is identical to your `requireAuth` middleware.
- **Secrets Manager**: `process.env.JWT_SECRET` in production should come from AWS Secrets Manager or Systems Manager Parameter Store, not a `.env` file or Lambda environment variable (for the most sensitive secrets).
- **401 vs 403**: API Gateway returns 401 for missing or expired tokens and 403 for policy denials. This distinction is tested.

---

## 9. Study Checklist

- [ ] Explain the six REST constraints; identify which two are most important for scalability
- [ ] Match HTTP verbs to their semantics and correct status codes
- [ ] Explain the difference between 401 and 403
- [ ] Design a URL structure for a resource with nested sub-resources
- [ ] Hash a password with bcrypt using a cost factor of 12
- [ ] Compare a password attempt against a stored bcrypt hash
- [ ] Sign a JWT with `jsonwebtoken` including `exp` claim
- [ ] Verify a JWT and handle `TokenExpiredError` and `JsonWebTokenError` separately
- [ ] Write `requireAuth` middleware that reads the Bearer token and attaches `req.user`
- [ ] Write `requireRole` middleware that checks `req.user.role`
- [ ] Explain why login error messages should be generic (same message for wrong email vs wrong password)
- [ ] Set up a Postman collection with auto-save token and collection variable auth
- [ ] Explain the relationship between JWT auth middleware and AWS Lambda authorizers

---

## 10. Supplemental Resources

The following free, open-access resources go deeper on Module 12 topics:

**1. JWT.io — JSON Web Token Introduction**
[https://jwt.io/introduction](https://jwt.io/introduction)
The official JWT.io introduction covering the three-part structure (header, payload, signature), standard claims, signing algorithms (HS256 vs RS256), and the security properties of signed tokens — directly aligned to Section 5 of this guide and the JWT patterns in Lab 12.

**2. OWASP — Password Storage Cheat Sheet**
[https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
The OWASP authoritative guide on password hashing, bcrypt cost factor selection, why fast hashing algorithms (MD5, SHA-256) must never be used for passwords, and migration strategies for upgrading hash algorithms — directly reinforces Section 4 of this guide.

**3. MDN Web Docs — HTTP authentication**
[https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)
Complete reference for HTTP authentication schemes including Bearer tokens and the `Authorization` header format used by `requireAuth` middleware — covers the `401 Unauthorized` and `403 Forbidden` distinction tested in the quiz and the DVA-C02 exam.

**4. AWS Documentation — Amazon Cognito — User Pools**
[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
The official AWS Cognito documentation covering user pool setup, token types (ID token, access token, refresh token), Lambda authorizer integration, and the hosted UI — the production equivalent of the `bcrypt + JWT` auth system built in Lab 12 and a key DVA-C02 exam topic.
