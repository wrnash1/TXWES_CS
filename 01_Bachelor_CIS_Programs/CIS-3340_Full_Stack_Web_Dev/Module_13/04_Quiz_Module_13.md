# Quiz: Module 13 — Web Security: JWT Authentication & CORS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which section of a JSON Web Token contains the user claims such as `userId` and `email`, and can it be read without knowing the server's secret key?

- A) The signature section contains the user claims and can only be read with the server's secret key.
- B) The payload section contains the user claims. It is Base64Url-encoded — not encrypted — so anyone with the token can decode and read it without knowing the secret key.
- C) The header section contains the user claims. It is encrypted with AES-256 and requires the server's secret key to decrypt.
- D) All three sections are encrypted and cannot be read without the server's secret key.

**Correct Answer:** B

**Explanation:** The JWT payload is Base64Url-encoded JSON, not encrypted. Base64Url is a reversible encoding — any decoder can read it without any key. The signature proves the payload has not been tampered with, but it does not hide the payload contents. This is why sensitive data (passwords, credit card numbers) must never be placed in a JWT payload.

**Distractor Analysis:**

- Why A is incorrect: The signature does not contain user claims — it is an HMAC hash of the header and payload.
- Why B is correct: Base64Url encoding is not encryption. The payload is publicly readable.
- Why C is incorrect: The header contains algorithm metadata (`alg`, `typ`), not user claims.
- Why D is incorrect: None of the three sections are encrypted in a standard JWT using HS256.

---

## Question 2

A developer writes a login route that queries the database and returns:

- `"User not found"` when the email does not exist
- `"Wrong password"` when the email exists but the password is incorrect

Both return `401`. What security problem does this create?

- A) Returning `401` for both cases violates the HTTP specification — only `403` is correct for failed logins.
- B) Distinct error messages allow an attacker to enumerate registered email addresses — by sending login attempts and reading the error message, they learn which emails are registered without knowing any passwords.
- C) The error messages bypass bcrypt's timing attack protection.
- D) Returning different messages causes the browser to cache the 401 response incorrectly.

**Correct Answer:** B

**Explanation:** User enumeration allows attackers to build a list of confirmed registered accounts. With that list, they can target phishing attacks, credential stuffing, or brute-force attempts on known-good emails. The fix is to return the same message — typically "Invalid credentials" — regardless of which field was incorrect.

**Distractor Analysis:**

- Why A is incorrect: `401` is the correct HTTP status for failed authentication. `403` indicates an authenticated user lacking permission.
- Why B is correct: Different messages for "not found" vs "wrong password" leak whether the email is registered.
- Why C is incorrect: Distinct error messages are a separate issue from bcrypt timing — bcrypt.compare is already constant-time.
- Why D is incorrect: HTTP 401 responses are not cached by default.

---

## Question 3

A developer applies the `authenticate` middleware to every route in the Express application using `app.use(authenticate)` before all route registrations. What is the consequence?

- A) The middleware runs after all routes, so it has no effect.
- B) The `POST /api/auth/login` route is also protected by the middleware — a user cannot log in because they have no token yet. The login and register routes must be mounted before `app.use(authenticate)` or the middleware must be applied only to specific routers.
- C) The middleware causes a memory leak because it stores tokens in memory.
- D) Express throws an error because `app.use()` does not accept middleware functions — only router instances.

**Correct Answer:** B

**Explanation:** Express processes middleware and routes in registration order. If `app.use(authenticate)` is placed before the auth routes, every request — including `POST /api/auth/login` — will be checked for a valid token. Since login is the endpoint that issues tokens, requiring a token to log in creates a circular dependency. Auth routes must be registered before the authenticate middleware, or the middleware must be applied only to protected routers.

**Distractor Analysis:**

- Why A is incorrect: Middleware registered with `app.use()` runs before routes registered after it.
- Why B is correct: The ordering of middleware and routes in Express determines which requests the middleware intercepts.
- Why C is incorrect: The authenticate middleware does not store anything in memory — it only reads the Authorization header.
- Why D is incorrect: `app.use()` accepts any middleware function or router instance.

---

## Question 4

A React application sends `GET /api/books` with an `Authorization` header to an Express server on a different origin. The browser sends an `OPTIONS` request first and receives a `403` response. What is the most likely cause?

- A) GET requests with Authorization headers always require user confirmation in the browser before the request is sent.
- B) The Express CORS configuration is missing `Authorization` in the `allowedHeaders` list — the preflight fails, and the browser blocks the actual GET request.
- C) The `OPTIONS` HTTP method is not supported by Express — it must be handled by a custom route.
- D) The browser blocks all preflight requests to APIs that use JWTs for security reasons.

**Correct Answer:** B

**Explanation:** When a browser detects a custom request header like `Authorization`, it sends an `OPTIONS` preflight before the actual request. The server must respond with `Access-Control-Allow-Headers: Authorization` (among other required headers). If `Authorization` is not in the `allowedHeaders` CORS configuration, the preflight fails and the browser never sends the actual GET request.

**Distractor Analysis:**

- Why A is incorrect: Browsers do not prompt users for confirmation before sending requests — they enforce CORS automatically.
- Why B is correct: `allowedHeaders` must explicitly include `Authorization` for authenticated CORS requests to work.
- Why C is incorrect: Express handles `OPTIONS` automatically when the `cors()` middleware is used.
- Why D is incorrect: CORS is a browser security mechanism for cross-origin requests — it is not JWT-specific.

---

## Question 5

What is the purpose of the `exp` claim in a JWT payload, and what happens on the server when a token with an expired `exp` is received?

- A) `exp` is an optional label the client sets to describe the token. The server ignores it.
- B) `exp` is a Unix timestamp after which the token is invalid. When `jwt.verify()` processes an expired token, it throws `TokenExpiredError`. The server should catch this specifically and return `401`.
- C) `exp` tells the browser how long to cache the token in `localStorage` before deleting it automatically.
- D) `exp` defines the maximum number of times the token can be used before it expires.

**Correct Answer:** B

**Explanation:** The `exp` claim is a standard JWT claim containing a Unix timestamp. `jsonwebtoken`'s `jwt.verify()` automatically checks the current time against `exp`. If the token has expired, it throws `TokenExpiredError` — a subclass of `JsonWebTokenError`. Catching it separately allows the server to return a specific error message like "Token expired — please log in again" instead of a generic "Invalid token."

**Distractor Analysis:**

- Why A is incorrect: `exp` is a registered claim that `jwt.verify()` always checks automatically.
- Why B is correct: `TokenExpiredError` is distinct from other verification errors and enables user-friendly messaging.
- Why C is incorrect: `localStorage` has no native expiration mechanism — the browser does not delete items based on JWT claims.
- Why D is incorrect: JWTs are not counted — there is no built-in usage counter. Stateless tokens are valid until expired or until the signing secret is rotated.

---

## Question 6

An attacker intercepts a JWT from a user's `localStorage` (via an XSS vulnerability) and replaces the `userId` claim in the payload with a different user's ID. They then encode the modified payload and send the request. Will the server accept this modified token?

- A) Yes — the server only checks the `exp` claim, not the signature.
- B) No — the server recomputes the HMAC signature using its secret key and compares it to the signature in the token. The modified payload produces a different signature, so `jwt.verify()` throws `JsonWebTokenError`.
- C) Yes — Base64Url encoding is symmetric, so the attacker can re-encode the modified payload and produce a valid token.
- D) Yes — HMAC-SHA256 signatures are public key algorithms, so anyone can generate a valid signature.

**Correct Answer:** B

**Explanation:** The JWT signature is an HMAC-SHA256 hash of the header and payload using the server's secret key. When the attacker modifies the payload, the hash changes. The attacker cannot compute the correct new signature without knowing the secret key. `jwt.verify()` recomputes the expected signature and detects the mismatch, throwing `JsonWebTokenError`. This tamper detection is the core security property of JWTs.

**Distractor Analysis:**

- Why A is incorrect: `jwt.verify()` always checks both the signature and the `exp` claim.
- Why B is correct: Signature verification is what makes JWT claims trustworthy — even though the payload is visible.
- Why C is incorrect: Base64Url encoding is not the signature. Changing the payload invalidates the existing signature, which the attacker cannot regenerate.
- Why D is incorrect: HMAC-SHA256 is a symmetric algorithm requiring the secret key to both sign and verify — it is not a public key algorithm.

---

## Question 7

A developer stores the JWT in an `httpOnly` cookie instead of `localStorage`. What security benefit does this provide, and what new concern does it introduce?

- A) `httpOnly` cookies are encrypted at rest, preventing all forms of token theft.
- B) `httpOnly` cookies cannot be read by JavaScript — an XSS attack that injects malicious script into the page cannot steal the token. The new concern is Cross-Site Request Forgery (CSRF) — a malicious site can trigger requests that automatically include the cookie, so CSRF protection (a CSRF token or `SameSite` cookie attribute) is required for state-changing requests.
- C) `httpOnly` cookies eliminate the need for CORS headers because cookies are always same-origin.
- D) `httpOnly` cookies are automatically deleted when the user closes the browser, making logout unnecessary.

**Correct Answer:** B

**Explanation:** The `httpOnly` flag prevents client-side JavaScript from accessing the cookie. Even if an XSS payload executes in the browser, it cannot read the cookie value and exfiltrate the token. The trade-off is CSRF risk: a malicious site can embed a form or script that sends a cross-origin request, and the browser automatically includes cookies. Mitigations include `SameSite=Strict` or `SameSite=Lax` cookie attributes, or a separate CSRF token in a custom request header.

**Distractor Analysis:**

- Why A is incorrect: `httpOnly` prevents JavaScript access; it does not encrypt the cookie value at rest.
- Why B is correct: XSS resistance vs. CSRF risk is the exact trade-off between `httpOnly` cookies and `localStorage`.
- Why C is incorrect: CORS applies to requests from different origins regardless of whether credentials are in cookies or headers.
- Why D is incorrect: `httpOnly` has no effect on cookie expiration. Session cookies are cleared on browser close; persistent cookies with `Max-Age` or `Expires` are not.

---

## Question 8

In an AWS serverless architecture, a React SPA calls an API Gateway endpoint. The team wants to verify the caller's JWT before allowing the Lambda function to execute. Which AWS component performs this verification?

- A) Amazon Cognito User Pools built-in authorizer — it automatically validates JWTs without any custom code.
- B) A Lambda Authorizer — a separate Lambda function that API Gateway invokes before the backend Lambda, which verifies the JWT and returns an IAM policy document allowing or denying the request.
- C) AWS WAF (Web Application Firewall) — it inspects the Authorization header and validates the JWT signature.
- D) API Gateway resource policies — they contain a list of valid token values that API Gateway checks against the Authorization header.

**Correct Answer:** B

**Explanation:** A Lambda Authorizer (formerly Custom Authorizer) is a Lambda function that API Gateway invokes before the backend Lambda. It receives the request headers, extracts the JWT, verifies the signature and expiration, and returns an IAM policy document with `Effect: Allow` or `Effect: Deny`. API Gateway caches the policy by token value (configurable TTL) to avoid calling the authorizer on every request. This is a directly tested DVA-C02 pattern.

**Distractor Analysis:**

- Why A is incorrect: Cognito authorizers work automatically with Cognito-issued JWTs, but the question describes a custom JWT — not necessarily Cognito-issued. Lambda Authorizers support any JWT issuer.
- Why B is correct: Lambda Authorizers are the general-purpose custom auth mechanism for API Gateway.
- Why C is incorrect: AWS WAF inspects and blocks requests based on rules (rate limiting, IP blocking, SQL injection patterns) — it does not perform JWT cryptographic verification.
- Why D is incorrect: API Gateway resource policies control which AWS accounts or VPCs can call an API — they do not contain token lists.

---

## Question 9

A developer writes this authentication middleware:

```javascript
function authenticate(req, res, next) {
  const token = req.headers.authorization;
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  req.user = decoded;
  next();
}
```

A request arrives with `Authorization: Bearer eyJ...`. What happens?

- A) The middleware works correctly — `req.headers.authorization` contains the raw token value.
- B) `jwt.verify()` receives the full string `"Bearer eyJ..."` instead of just the token. This fails verification with `JsonWebTokenError: jwt malformed`. The fix is to split the header value and extract the second part.
- C) The middleware crashes with an unhandled exception on any invalid token because `jwt.verify()` throws but there is no `try/catch`.
- D) Both B and C are problems with this middleware.

**Correct Answer:** D

**Explanation:** There are two bugs. First, `req.headers.authorization` is `"Bearer eyJ..."` — the full header value including the scheme prefix. `jwt.verify()` expects only the token string, so passing the full value causes `JsonWebTokenError: jwt malformed`. Second, `jwt.verify()` throws on expired or invalid tokens, but there is no `try/catch` — the error propagates as an unhandled exception and Express's default error handler returns a 500 instead of a 401.

**Distractor Analysis:**

- Why A is incorrect: `req.headers.authorization` contains the full header value including `"Bearer "`.
- Why B is incorrect: While true, it is incomplete — the missing `try/catch` is an equally serious bug.
- Why C is incorrect: While true, it is incomplete — the unstripped prefix is an equally serious bug.
- Why D is correct: Both bugs must be fixed — strip the prefix and wrap `jwt.verify()` in `try/catch`.

---

## Question 10

A React application logs in successfully and receives a JWT. The token has `"exp": 1699900000` in the payload. Two hours later, the user tries to view their profile and the API returns `401 Token expired`. The React developer wants to automatically redirect the user to the login page when this happens. Where should this logic live in the React application?

- A) In a `useEffect` hook inside every component that fetches data — each component should check the `exp` claim locally by decoding the token on every render.
- B) In a centralized authenticated fetch helper or custom hook that checks the response status — if any API call returns `401`, clear the token from state and `localStorage` and redirect to the login form.
- C) In the Express server — the server should redirect to the login page when it returns `401`.
- D) In the JWT itself — set the `redirect_uri` claim to the login page URL so the browser automatically redirects.

**Correct Answer:** B

**Explanation:** A centralized auth fetch helper handles `401` responses in one place, keeping the logic DRY. When any API call returns `401`, the helper clears the stored token and triggers a state change that renders the `LoginForm`. This approach avoids duplicating expiration-check logic in every component. Checking the `exp` claim client-side is unreliable — only the server's `jwt.verify()` is authoritative.

**Distractor Analysis:**

- Why A is incorrect: Decoding and checking `exp` in every component is duplicated logic. Clock skew between client and server can also cause premature or late redirects. The server's `jwt.verify()` is authoritative.
- Why B is correct: A single centralized response handler is the correct pattern for authentication lifecycle management in React.
- Why C is incorrect: Express returns JSON responses, not browser redirects. The React SPA handles navigation — it does not follow HTTP 302 redirects from an API.
- Why D is incorrect: `redirect_uri` is an OAuth 2.0 parameter used during the authorization code flow — it is not a JWT claim and the browser does not act on JWT payload values.

---

### Question 11 (5 points)

A developer stores the JWT in `localStorage` and later discovers the app has an XSS vulnerability. Which statement best describes the resulting security risk?

- A) The XSS vulnerability is unrelated to token storage — tokens in `localStorage` are protected by the Same-Origin Policy.
- B) An attacker's injected script can call `localStorage.getItem('token')` and exfiltrate the token to a remote server, allowing the attacker to impersonate the user from any origin.
- C) Only server-side XSS vulnerabilities can steal tokens from `localStorage`.
- D) The JWT is already encrypted in `localStorage` by the browser, so exfiltration is harmless.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Same-Origin Policy governs cross-origin requests, not JavaScript access to `localStorage`. Any script running on the page — including injected scripts — can read `localStorage`.
  - Why B is correct: XSS gives the attacker arbitrary JavaScript execution. `localStorage` is fully accessible to JavaScript, so the attacker can read, copy, and send the token to a remote server where it can be replayed.
  - Why C is incorrect: XSS is a client-side vulnerability. An injected script runs in the browser with full access to `localStorage`, regardless of where the server is located.
  - Why D is incorrect: JWTs are base64url-encoded, not encrypted. `localStorage` also stores values as plain strings — the browser applies no encryption.

---

### Question 12 (5 points)

A React application sends authenticated requests using `fetch` with `credentials: 'include'`. The backend Express server uses the `cors` package with `origin: 'http://localhost:5173'`. Requests succeed in development, but the browser still blocks the preflight. Which additional option must be set on the server?

- A) `methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']`
- B) `credentials: true`
- C) `allowedHeaders: ['Content-Type', 'Authorization']`
- D) `exposedHeaders: ['Set-Cookie']`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Listing HTTP methods is not required for `credentials: 'include'` to work — the browser allows all standard methods unless the server restricts them.
  - Why B is correct: When the client sends `credentials: 'include'`, the server must respond with `Access-Control-Allow-Credentials: true`. The `cors` package sets this header when `credentials: true` is configured. Without it the browser rejects the response.
  - Why C is incorrect: `allowedHeaders` allows the `Authorization` header through preflight — it is good practice but is not the specific missing option that blocks `credentials: 'include'` requests.
  - Why D is incorrect: `exposedHeaders` controls which response headers JavaScript can read — it is unrelated to the `credentials` requirement.

---

### Question 13 (5 points)

Which hashing algorithm should NEVER be used for storing user passwords, and why?

- A) bcrypt — it is too slow and causes unacceptable login latency.
- B) Argon2 — it won a password hashing competition so it must have known weaknesses.
- C) SHA-256 — it is a fast general-purpose algorithm, which makes brute-force attacks using GPUs trivial.
- D) PBKDF2 — it uses HMAC internally, which is the same as signing a JWT.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: bcrypt's intentional slowness is a security feature, not a flaw. A cost factor of 12 takes roughly 250 ms per hash — negligible for login but enormously expensive for attackers.
  - Why B is incorrect: Argon2 won the Password Hashing Competition in 2015 specifically because of its strong security properties. It is the recommended algorithm for new systems.
  - Why C is correct: SHA-256 can compute billions of hashes per second on modern GPU hardware. An attacker with a stolen hash database can perform an offline brute-force attack and crack common passwords in minutes.
  - Why D is incorrect: PBKDF2 is a legitimate password hashing function. Its use of HMAC is irrelevant to JWT signing — the two use cases are entirely separate.

---

### Question 14 (5 points)

A JWT is issued with `{ "alg": "HS256", "typ": "JWT" }` in its header. An attacker intercepts the token and changes the header to `{ "alg": "none", "typ": "JWT" }`, removes the signature, and replays it. Which server-side behavior prevents this attack?

- A) The server checks that `alg` is not `"none"` before calling `jwt.verify()`.
- B) The `jsonwebtoken` library's `jwt.verify()` rejects `alg: none` tokens by default when a secret is provided.
- C) The payload is encrypted with the same secret, so altering the header invalidates decryption.
- D) The browser blocks requests containing `alg: none` tokens before they reach the server.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While adding an explicit check is a valid defense-in-depth measure, the primary protection comes from the library's default behavior, not from manual header inspection.
  - Why B is correct: The `jsonwebtoken` library requires a valid signature when a secret is provided to `jwt.verify()`. A token with `alg: none` has no signature — verification fails with `JsonWebTokenError`. The library explicitly rejects unsigned tokens unless `algorithms: ['none']` is explicitly allowed.
  - Why C is incorrect: JWT payloads are base64url-encoded, not encrypted. There is no encryption to invalidate.
  - Why D is incorrect: The browser has no knowledge of JWT contents — it transmits whatever the JavaScript sends in the `Authorization` header.

---

### Question 15 (5 points)

An Express API sets this CORS configuration: `cors({ origin: 'http://localhost:5173', credentials: true })`. A deployed React app at `https://app.example.com` sends a request with `credentials: 'include'`. What happens?

- A) The request succeeds because `credentials: true` overrides the origin restriction.
- B) The browser sends the request and the server responds, but the browser blocks the response because the `Access-Control-Allow-Origin` header does not match the request's origin.
- C) The server returns `403 Forbidden` because the origin does not match.
- D) The browser blocks the preflight request before it reaches the server because `https` and `http` are different schemes.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `credentials: true` enables the `Access-Control-Allow-Credentials: true` response header — it does not broaden the allowed origins.
  - Why B is correct: The server responds with `Access-Control-Allow-Origin: http://localhost:5173`. The browser compares this to the actual request origin `https://app.example.com` — they do not match, so the browser blocks JavaScript from reading the response (CORS error). The server itself never returns a CORS error — the enforcement is entirely in the browser.
  - Why C is incorrect: The CORS `origin` option in the `cors` middleware causes the server to omit or mismatch the `Access-Control-Allow-Origin` header — it does not return `403`.
  - Why D is incorrect: The browser does send the preflight — CORS enforcement happens at the response stage, not during the send stage.

---

### Question 16 (5 points)

The `Access-Control-Max-Age` response header returned during a CORS preflight controls which behavior?

- A) The maximum age of the JWT before the browser considers it expired.
- B) How long (in seconds) the browser may cache the preflight response, skipping subsequent `OPTIONS` requests for the same endpoint.
- C) The maximum time the server will wait for a request body before closing the connection.
- D) How long the `Set-Cookie` header's `Max-Age` attribute overrides `Access-Control-Max-Age`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: JWT expiration is controlled by the `exp` claim in the token payload and verified by `jwt.verify()` on the server — not by any HTTP header.
  - Why B is correct: `Access-Control-Max-Age` tells the browser how long to cache the preflight result. During that window, the browser skips the `OPTIONS` request and sends the actual request directly, reducing latency.
  - Why C is incorrect: Request body timeout is configured at the web server or framework level (e.g., Express `timeout` middleware) — not via a CORS header.
  - Why D is incorrect: Cookie `Max-Age` and `Access-Control-Max-Age` are entirely unrelated headers with no interaction.

---

### Question 17 (5 points)

RS256 (asymmetric) is used instead of HS256 (symmetric) to sign JWTs in a microservices architecture. What is the primary advantage?

- A) RS256 tokens are smaller because the signature uses fewer bytes than HS256.
- B) RS256 allows any service to verify tokens using only the public key — no service needs access to the private signing key, limiting the blast radius of a key compromise.
- C) RS256 tokens are impossible to decode because RSA encryption is applied to the payload.
- D) RS256 eliminates the need for an `exp` claim because RSA keys expire automatically.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: RSA signatures are larger than HMAC-SHA256 signatures. The RS256 token is bigger, not smaller.
  - Why B is correct: In RS256, only the Auth service holds the private key and signs tokens. All downstream services verify with the public key. A compromised downstream service cannot forge tokens — it cannot sign with the private key it never had.
  - Why C is incorrect: JWT payloads are base64url-encoded and always readable. RS256 is an asymmetric signing algorithm, not an encryption algorithm. For confidentiality use JWE.
  - Why D is incorrect: All JWTs should include an `exp` claim regardless of the signing algorithm. RSA keys do not expire automatically.

---

### Question 18 (5 points)

A JWT is compromised before it expires. The API uses stateless JWT verification and has no token blacklist. What is the most accurate statement about revoking the token?

- A) Delete the token from the user's `localStorage` — this revokes it server-side.
- B) The API can call `jwt.invalidate()` to mark the token as revoked in the `jsonwebtoken` library's internal store.
- C) True stateless JWT revocation is impossible before expiry without additional server-side state such as a token blacklist or short expiry combined with refresh tokens.
- D) Changing the JWT secret immediately revokes all existing tokens and is the standard revocation mechanism.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Deleting the token from `localStorage` removes it from the compromised client, but the attacker who stole it still holds a valid copy. The server has no record of which tokens have been issued and cannot distinguish the attacker's copy.
  - Why B is incorrect: `jsonwebtoken` does not have a `jwt.invalidate()` function — there is no built-in revocation store in the library.
  - Why C is correct: Stateless JWTs are self-contained. The server cannot revoke a specific token without maintaining server-side state (a blacklist). Practical mitigation strategies include short expiry plus refresh tokens, or a Redis-backed token blacklist.
  - Why D is incorrect: Changing the secret invalidates ALL tokens including legitimate ones — it is a last-resort emergency measure, not a targeted revocation mechanism.

---

### Question 19 (5 points)

An Express route applies `authenticate` middleware followed by `requireRole('admin')` middleware. A request arrives with a valid JWT for a user with `role: 'student'`. Which response does the client receive?

- A) `401 Unauthorized` — the token is valid but the role is wrong, so the user is considered unauthenticated.
- B) `403 Forbidden` — the user is authenticated but lacks the required role.
- C) `404 Not Found` — the admin route is hidden from non-admin users.
- D) `200 OK` — both middleware functions run, and the route handler ignores the role check.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `401` means "not authenticated" — the server cannot identify who the user is. A valid JWT proves identity. The correct code for "authenticated but unauthorized" is `403`.
  - Why B is correct: `requireRole` checks `req.user.role` after `authenticate` has already set it. The student role is not in the allowed list, so `requireRole` calls `next(new ForbiddenError(...))` and the global error handler returns `403`.
  - Why C is incorrect: HTTP route matching is independent of authorization — the route exists and is matched before middleware runs. Returning `404` for authorization failures would leak information about which routes exist.
  - Why D is incorrect: `requireRole` calls `next(err)` when the role check fails, bypassing the route handler entirely.

---

### Question 20 (5 points)

A developer adds `app.use(authenticate)` before all routes so every route is protected. The login and registration endpoints then start returning `401 Unauthorized` before the request body is even read. What is the correct fix?

- A) Move the auth middleware after the `express.json()` middleware so the body is parsed first.
- B) Mount the auth routes before `app.use(authenticate)`, or add a path check inside `authenticate` to skip unprotected paths.
- C) Add `if (req.path === '/login') next()` inside the route handler rather than the middleware.
- D) Disable the `authenticate` middleware for the entire application and protect routes individually using inline `if` checks in each handler.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The order of `express.json()` relative to `authenticate` is irrelevant to this problem. The issue is that `authenticate` runs before the request reaches the auth routes, not that the body is unparsed.
  - Why B is correct: Auth routes (`/api/auth/login`, `/api/auth/register`) must be reachable without a token. The cleanest pattern is to mount them before `app.use(authenticate)` so the global middleware never runs for those paths. Alternatively, `authenticate` can skip paths matching an allowlist.
  - Why C is incorrect: Placing path checks inside a route handler is wrong — the middleware has already run and rejected the request before the route handler is reached.
  - Why D is incorrect: Individual `if` checks in every handler are error-prone and do not scale. Middleware is the correct abstraction for cross-cutting concerns.
