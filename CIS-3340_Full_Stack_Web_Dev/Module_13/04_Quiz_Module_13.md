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
