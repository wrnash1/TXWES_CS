# Video Script: Module 12 — RESTful API Design and Authentication

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with Express project open, Postman for API testing
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for Postman; [PAUSE] for slides
- Have `jsonwebtoken` and `bcryptjs` installed in the demo project
- Postman collection pre-loaded with auth flow requests

---

## Section 1: Introduction — Why REST and Why Auth? (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 12 — RESTful API Design and Authentication.

In Module 11 you built an Express server with routes, middleware, and error handling. The API you built was open — anyone who knew the URL could read and modify data. Real applications need two more things: a consistent, predictable API design that clients can trust, and an authentication system that ensures only authorized users can access protected resources.

In this module we cover REST principles and HTTP conventions that make APIs intuitive to use, JSON Web Tokens for stateless authentication, bcrypt for password hashing, protected route middleware, and Postman for testing the full auth flow.

These skills connect directly to the AWS Developer Associate exam — API Gateway and Cognito test many of these same concepts at scale.

[PAUSE — slide: Module 12 Learning Objectives]

---

## Section 2: REST Principles (1:30 – 4:30)

REST — Representational State Transfer — is an architectural style for distributed systems defined by Roy Fielding in his 2000 doctoral dissertation. A REST API is not a standard you install; it is a set of design constraints that, when followed, produce APIs that are consistent, scalable, and easy to use.

Six REST constraints:

[PAUSE — slide: Six REST Constraints]

One: **Client-Server** — the client and server are separate and communicate only through a well-defined interface.

Two: **Stateless** — each request contains all information needed to process it. The server holds no session state between requests. This is critical for scaling — any server in a cluster can handle any request.

Three: **Cacheable** — responses can be cached by clients and intermediaries. Proper use of HTTP cache headers reduces load on the server.

Four: **Uniform Interface** — resource identification in URLs, manipulation through representations, self-descriptive messages.

Five: **Layered System** — the client cannot tell whether it is connected directly to the server or through an intermediary like a load balancer or CDN.

Six: **Code on Demand** (optional) — servers can send executable code to clients.

The two most important for this course are **stateless** and **uniform interface**.

[PAUSE — slide: REST constraints summary]

---

## Section 3: HTTP Verbs and Status Codes (4:30 – 7:30)

REST APIs use HTTP verbs to express intent. The verb tells the server what operation to perform; the URL identifies the resource.

[SHOW CODE]

```
GET    /api/courses          → list all courses
GET    /api/courses/CIS-3340 → get one course
POST   /api/courses          → create a course
PUT    /api/courses/CIS-3340 → replace the course entirely
PATCH  /api/courses/CIS-3340 → update partial fields
DELETE /api/courses/CIS-3340 → delete the course
```

POST creates — the server assigns the ID. PUT replaces everything. PATCH updates only provided fields. GET and DELETE have no body.

HTTP status codes communicate the outcome. Know these cold.

[PAUSE — slide: HTTP status codes by class]

```
2xx — Success
  200 OK           → successful GET, PUT, PATCH
  201 Created      → successful POST; include Location header
  204 No Content   → successful DELETE; no response body

4xx — Client Error
  400 Bad Request  → invalid input, missing fields, malformed JSON
  401 Unauthorized → not authenticated
  403 Forbidden    → authenticated but not authorized for this resource
  404 Not Found    → resource does not exist
  409 Conflict     → duplicate; e.g., email already registered

5xx — Server Error
  500 Internal Server Error → unhandled exception
```

The `401` vs `403` distinction is frequently tested on the AWS Developer Associate exam. 401 means "I do not know who you are — please authenticate." 403 means "I know who you are, but you are not allowed to do this."

[PAUSE — slide: 401 vs 403 side-by-side comparison]

---

## Section 4: URL Design Best Practices (7:30 – 9:30)

Good URL design makes APIs self-documenting.

Use nouns for resources, not verbs. The verb is the HTTP method.

[SHOW CODE]

```
GOOD — nouns and HTTP verbs
GET    /api/students
POST   /api/students
GET    /api/students/42
DELETE /api/students/42

BAD — verbs in URLs
GET  /api/getStudents
POST /api/createStudent
POST /api/deleteStudent/42
```

Use plural nouns consistently. Use hyphens for multi-word paths, not camelCase.

Nest resources to express relationships.

[SHOW CODE]

```
GET  /api/students/42/courses          → enrollments for student 42
POST /api/students/42/courses          → enroll student 42
GET  /api/students/42/courses/CIS-3340 → specific enrollment record
```

Use query parameters for filtering, sorting, and pagination.

[SHOW CODE]

```
GET /api/students?major=CS&gpa_min=3.5
GET /api/courses?sort=title&order=asc
GET /api/students?page=2&limit=20
```

[PAUSE — slide: URL design — good vs bad examples]

---

## Section 5: Password Hashing with bcrypt (9:30 – 12:00)

Never store plain-text passwords. If your database is compromised, plain-text passwords expose every user's credentials immediately. Bcrypt is the standard password hashing algorithm for Node.js.

[SHOW CODE]

```bash
npm install bcryptjs
```

[SHOW CODE]

```js
const bcrypt = require('bcryptjs');

// Hashing — cost factor 12 means 2^12 = 4096 iterations
async function hashPassword(plaintext) {
  return bcrypt.hash(plaintext, 12);
}

// Comparing — timing-safe comparison
async function verifyPassword(plaintext, hash) {
  return bcrypt.compare(plaintext, hash);
}

// Registration
const hash = await hashPassword('mySecurePassword!');
// Store hash in database — never the plaintext

// Login
const isValid = await verifyPassword('mySecurePassword!', storedHash);
// true if correct, false if wrong
```

A higher cost factor makes the hash slower to compute — that is intentional. Cost factor 12 takes about 300ms on modern hardware, which is imperceptible to users but makes brute-force attacks impractical.

Bcrypt automatically generates a random salt embedded in the hash string. You never manage salts manually. Two hashes of the same password are always different because each has a unique random salt — this defeats rainbow table attacks.

[PAUSE — slide: bcrypt hash format with labeled components]

---

## Section 6: JSON Web Tokens (12:00 – 16:00)

JSON Web Tokens are the standard mechanism for stateless authentication in REST APIs. A JWT is a compact, URL-safe token encoding signed claims about a user.

[PAUSE — slide: JWT structure — header dot payload dot signature]

A JWT has three base64url-encoded parts separated by dots. The header specifies the algorithm. The payload carries claims: user ID, role, expiration. The signature is HMAC-SHA256 of header.payload using a secret key known only to the server.

[SHOW CODE]

```bash
npm install jsonwebtoken
```

[SHOW CODE]

```js
const jwt = require('jsonwebtoken');

const JWT_SECRET = process.env.JWT_SECRET; // Never hard-code this

// Sign a token after successful login
function signToken(payload) {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: '24h' });
}

// Verify a token in auth middleware
function verifyToken(token) {
  return jwt.verify(token, JWT_SECRET); // throws if invalid or expired
}

// Usage
const token = signToken({ userId: 42, email: 'alice@txwes.edu', role: 'student' });

const decoded = verifyToken(token);
// { userId: 42, email: 'alice@txwes.edu', role: 'student', iat: ..., exp: ... }
```

[PAUSE — slide: JWT authentication flow — three steps]

The auth flow: Step one — user submits email and password. Step two — server verifies credentials, issues JWT, sends it to the client. Step three — on subsequent requests, client includes the JWT in the `Authorization: Bearer <token>` header. Server verifies the signature and extracts the user's identity — no database lookup needed for each request.

JWT authentication is stateless. Any server in the cluster can verify the token because verification only requires the secret key, not a shared session store.

Important: JWT payloads are base64url-encoded, not encrypted. Anyone with the token can decode the payload. Never put passwords, SSNs, or credit card numbers in a JWT payload.

---

## Section 7: Auth Middleware and Protected Routes (16:00 – 19:00)

Every protected route needs middleware that reads the token from the header, verifies it, and attaches the user to `req.user`.

[SHOW CODE]

```js
// middleware/auth.js
const jwt = require('jsonwebtoken');
const { UnauthorizedError } = require('../utils/errors');

function requireAuth(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return next(new UnauthorizedError('No token provided'));
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded; // attach decoded payload to req
    next();
  } catch (err) {
    if (err.name === 'TokenExpiredError') {
      return next(new UnauthorizedError('Token expired'));
    }
    next(new UnauthorizedError('Invalid token'));
  }
}

function requireRole(...allowedRoles) {
  return (req, res, next) => {
    if (!req.user || !allowedRoles.includes(req.user.role)) {
      return next(new ForbiddenError('Insufficient permissions'));
    }
    next();
  };
}

module.exports = { requireAuth, requireRole };
```

[SHOW CODE]

```js
// Applying auth to routes
router.get('/profile', requireAuth, (req, res) => {
  res.json({ user: req.user }); // req.user = decoded JWT claims
});

router.delete('/:id', requireAuth, requireRole('admin'), async (req, res, next) => {
  // Only admin role reaches here
});
```

[PAUSE — slide: Auth middleware pipeline diagram]

---

## Section 8: Registration and Login Routes (19:00 – 21:30)

[SHOW CODE]

```js
// POST /api/auth/register
router.post('/register', requireFields(['name', 'email', 'password']), async (req, res, next) => {
  try {
    const { name, email, password } = req.body;

    if (users.find(u => u.email === email)) {
      return res.status(409).json({ error: 'Email already registered', code: 'EMAIL_EXISTS' });
    }
    if (password.length < 8) {
      return next(new ValidationError('Password must be at least 8 characters'));
    }

    const passwordHash = await bcrypt.hash(password, 12);
    const user = { id: Date.now(), name, email, passwordHash, role: 'student' };
    users.push(user);

    const token = jwt.sign(
      { userId: user.id, email: user.email, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: '24h' }
    );

    res.status(201).json({
      token,
      user: { id: user.id, name: user.name, email: user.email, role: user.role },
    });
  } catch (err) { next(err); }
});

// POST /api/auth/login
router.post('/login', requireFields(['email', 'password']), async (req, res, next) => {
  try {
    const { email, password } = req.body;

    // Generic error — never reveal which field is wrong
    const genericError = new UnauthorizedError('Invalid email or password');

    const user = users.find(u => u.email === email);
    if (!user) return next(genericError);

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) return next(genericError);

    const token = jwt.sign(
      { userId: user.id, email: user.email, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: '24h' }
    );

    res.status(200).json({ token, user: { id: user.id, name: user.name, email: user.email } });
  } catch (err) { next(err); }
});
```

The login error message is identical for "email not found" and "wrong password." This is intentional security design — different messages would tell an attacker whether a particular email is registered in your system.

[PAUSE — slide: Security — generic auth error messages explained]

---

## Section 9: Postman Testing (21:30 – 23:00)

Postman is the standard tool for testing REST APIs. The complete auth flow test sequence:

1. `POST /api/auth/register` — register a user, copy the `token` from the response.
2. Set Authorization tab to Bearer Token, paste the token.
3. `GET /api/auth/profile` — should return decoded user claims without a database query.
4. `POST /api/auth/register` same email — should return 409 Conflict.
5. `POST /api/auth/login` with wrong password — should return 401.
6. `GET /api/students/1` with no Authorization header — should return 401.
7. Modify one character in the token — should return 401 Invalid token.
8. `DELETE /api/students/1` with student-role token — should return 403.

[PAUSE — slide: Postman test sequence with expected status codes]

---

## Conclusion (23:00 – 24:00)

Summary of Module 12 — RESTful API Design and Authentication:

- REST constraints: stateless and uniform interface are the most important. Each request is self-contained.
- HTTP verbs express intent; status codes communicate outcome. Know the 2xx, 4xx, 5xx classes.
- URL design: nouns for resources, HTTP verbs for actions, nested paths for relationships, query params for filtering.
- bcrypt hashes passwords with a random salt and a cost factor — never store plaintext.
- JWT encodes signed claims; the server verifies the signature without a database lookup on every request.
- Auth middleware reads the `Authorization: Bearer` header, verifies the token, attaches claims to `req.user`.
- 401 means not authenticated. 403 means authenticated but not authorized.
- Use a single generic error message for login — never reveal which field is wrong.

For the AWS Developer Associate exam: API Gateway implements REST natively. Amazon Cognito provides managed JWT issuance and verification at scale. Lambda authorizers verify JWTs using the exact same logic as your `requireAuth` middleware. Know when to use Cognito versus a custom JWT implementation.

Your lab this week adds this complete auth system to the Lab 11 registrar API. See you in Module 13.

[END OF SCRIPT]
