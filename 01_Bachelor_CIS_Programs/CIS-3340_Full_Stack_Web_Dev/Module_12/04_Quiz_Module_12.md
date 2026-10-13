# Quiz: Module 12 — React State Management & API Integration

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

A React developer writes this `useEffect`:

```jsx
useEffect(() => {
  fetch('/api/books')
    .then(res => res.json())
    .then(data => setBooks(data));
}, []);
```

The Express server returns a 500 error with the JSON body `{ "error": "Database connection failed" }`. What happens in the browser?

- A) `fetch` rejects with a network error and the `.catch()` handler fires.
- B) `fetch` resolves, `.json()` parses `{ "error": "Database connection failed" }`, and `setBooks` is called with an object instead of an array — likely causing a `.map()` crash on the next render.
- C) React automatically retries the fetch request when it receives a 500 status code.
- D) The browser blocks the request because 500 responses are not allowed by the CORS policy.

**Correct Answer:** B

**Explanation:** The `fetch` API only rejects on network failure. A 500 HTTP response is a successful network request — `fetch` resolves, `.json()` parses the error body, and `setBooks` receives an object. The next render calls `books.map()` on an object, which throws `TypeError: books.map is not a function`. Always check `res.ok` before calling `.json()`.

**Distractor Analysis:**

- Why A is incorrect: `fetch` does not reject on HTTP error status codes. Only network failure (no response at all) causes a rejection.
- Why B is correct: The server error body is valid JSON. `fetch` resolves and the error object replaces the expected array.
- Why C is incorrect: `fetch` has no built-in retry behavior. Retries must be implemented explicitly.
- Why D is incorrect: CORS has no concept of HTTP status codes blocking a response. It restricts which origins can make the request, not what status codes are returned.

---

## Question 2

A React component has this state:

```jsx
const [books, setBooks] = useState([]);
```

After a successful POST to the server (which returns the newly created book as JSON), which of the following correctly adds the new book to the state without mutating the existing array?

- A) `books.push(newBook); setBooks(books);`
- B) `setBooks([...books, newBook]);`
- C) `books[books.length] = newBook; setBooks(books);`
- D) `setBooks(books.concat);`

**Correct Answer:** B

**Explanation:** React requires a new array reference to detect the state change. `[...books, newBook]` creates a new array containing all existing books plus the new one, which is the correct immutable update pattern. The functional updater form `setBooks(prev => [...prev, newBook])` is preferred when there is any chance of stale closure issues.

**Distractor Analysis:**

- Why A is incorrect: `push` mutates the existing array in place. `setBooks(books)` then passes the same reference React already has, so React may skip the re-render.
- Why B is correct: Spread creates a new array reference, which triggers React's re-render cycle.
- Why C is incorrect: Direct index assignment also mutates the existing array — same problem as `push`.
- Why D is incorrect: `books.concat` without calling it is a function reference, not an array. This would set `books` state to a function.

---

## Question 3

A developer adds a delete button to each book card:

```jsx
<button onClick={handleDelete(book.id)}>Delete</button>
```

On page load, all books are immediately deleted from the server. What is the bug?

- A) `handleDelete` must be renamed to match the `onClick` prop convention.
- B) `handleDelete(book.id)` is called immediately during rendering — it executes once for each book card in the `.map()`. The fix is `onClick={() => handleDelete(book.id)}`.
- C) The `key` prop is missing from the button, causing React to call handlers on the wrong element.
- D) Arrow functions are not allowed in JSX event handler attributes.

**Correct Answer:** B

**Explanation:** `onClick={handleDelete(book.id)}` evaluates `handleDelete(book.id)` immediately during the render pass — once for every book in the array. The return value (likely `undefined`) is assigned to `onClick`, so the button click does nothing afterward. The fix is to wrap the call in an arrow function: `onClick={() => handleDelete(book.id)}`, which creates a function that only executes when the user clicks.

**Distractor Analysis:**

- Why A is incorrect: The prop name `onClick` is the event attribute — the handler name is irrelevant to this bug.
- Why B is correct: This is one of the most common React bugs — calling a function instead of referencing it in event handlers.
- Why C is incorrect: The `key` prop on a parent element affects reconciliation but has no effect on event handler timing.
- Why D is incorrect: Arrow functions are fully supported in JSX event handler attributes and are the recommended syntax.

---

## Question 4

A React application fetches data from `http://localhost:3000/api/books`. The browser console shows:

```text
Access to fetch at 'http://localhost:3000/api/books' from origin
'http://localhost:5173' has been blocked by CORS policy:
No 'Access-Control-Allow-Origin' header is present.
```

Where must the fix be applied, and what is the fix?

- A) In the React component — add `mode: 'no-cors'` to the `fetch` options.
- B) In the Express server — add `app.use(cors({ origin: 'http://localhost:5173' }))` before the route registrations.
- C) In the browser settings — disable the same-origin policy for localhost.
- D) In `vite.config.js` — add a `proxy` entry that rewrites the API origin.

**Correct Answer:** B

**Explanation:** CORS headers must come from the server. The Express server must respond with `Access-Control-Allow-Origin: http://localhost:5173` using the `cors` npm package. The `cors()` middleware must be registered before any route handlers so it applies to all requests.

**Distractor Analysis:**

- Why A is incorrect: `mode: 'no-cors'` makes an opaque request — the browser receives a response but JavaScript cannot read the body. It does not solve the CORS problem for data-fetching.
- Why B is correct: CORS is enforced by the browser based on response headers from the server. The server must explicitly permit the origin.
- Why C is incorrect: Disabling browser security is not a deployable solution and is dangerous. CORS exists for security reasons.
- Why D is incorrect: A Vite proxy would work in development by making the request appear same-origin, but it is a development tool only. The root cause — missing CORS headers on the Express server — remains.

---

## Question 5

A React component fetches a list of books and renders a count and a list as separate child components. A developer implements it this way:

```jsx
function BookCount() {
  const [books, setBooks] = useState([]);
  // fetch here
  return <p>{books.length} books</p>;
}

function BookList() {
  const [books, setBooks] = useState([]);
  // fetch here
  return <ul>{books.map(b => <li key={b.id}>{b.title}</li>)}</ul>;
}
```

What is the primary engineering problem with this approach?

- A) Two `useState` calls in sibling components is a React error — state can only be declared once per application.
- B) Each component fetches independently, resulting in two separate server requests. The two `books` arrays are separate state values — if one updates, the other does not, and the count and list can become inconsistent.
- C) The `key` prop on list items must be set to the array index, not `b.id`.
- D) `useEffect` is required when two components need to share state — the fetch must be inside a `useEffect` in both components simultaneously.

**Correct Answer:** B

**Explanation:** Each component maintains its own state. Two fetch calls to the same endpoint double the network load. More critically, if the data changes (a book is added or deleted in one component), the other component does not know — the count and list fall out of sync. The solution is to lift state up to a common ancestor (`App`) and pass the data as props.

**Distractor Analysis:**

- Why A is incorrect: React allows any number of `useState` calls across any number of components.
- Why B is correct: Duplicate fetch calls and desynchronized sibling state are the concrete engineering problems.
- Why C is incorrect: Stable unique IDs from the data are preferred for `key` — array indexes are a last resort.
- Why D is incorrect: `useEffect` is how you run the fetch — it does not solve the shared-state problem.

---

## Question 6

Which of the following correctly describes the purpose of a custom React hook?

- A) A custom hook is a React component that returns multiple JSX elements using a Fragment instead of a single root element.
- B) A custom hook is a JavaScript function whose name starts with `use`, which calls built-in React hooks internally and returns data and/or functions — allowing stateful logic to be reused across multiple components without copying code.
- C) A custom hook is a higher-order component (HOC) — a function that accepts a component and returns a new component with additional props.
- D) A custom hook is a lifecycle method available only in class-based React components, analogous to `componentDidMount`.

**Correct Answer:** B

**Explanation:** Custom hooks are plain JavaScript functions prefixed with `use` that encapsulate stateful logic using built-in hooks. They do not return JSX — they return state values, setters, or derived values. The `use` prefix is required so React's lint rules can enforce hook usage rules (no conditional calls, no calls inside loops).

**Distractor Analysis:**

- Why A is incorrect: A function returning JSX is a component, not a hook.
- Why B is correct: The `use` prefix, internal hook calls, and return of data/functions is the complete definition.
- Why C is incorrect: Higher-order components are a different pattern — a function that wraps a component.
- Why D is incorrect: Custom hooks exist only in functional React. Class components use lifecycle methods.

---

## Question 7

A developer wants to fetch a specific book when the `bookId` prop changes. Which `useEffect` dependency array is correct?

```jsx
function BookDetail({ bookId }) {
  const [book, setBook] = useState(null);

  useEffect(() => {
    fetch(`/api/books/${bookId}`)
      .then(res => res.json())
      .then(data => setBook(data));
  }, /* WHICH OF THESE? */);
}
```

- A) `[]` — run once on mount
- B) `[bookId]` — re-run whenever `bookId` changes
- C) No dependency array — run after every render
- D) `[book]` — re-run whenever the fetched book changes

**Correct Answer:** B

**Explanation:** `[bookId]` tells React to re-run the effect whenever `bookId` changes — which is exactly when a new book needs to be fetched. `[]` would only fetch once on mount, ignoring subsequent `bookId` prop changes. No dependency array runs after every render, causing infinite re-renders if `setBook` is called inside the effect.

**Distractor Analysis:**

- Why A is incorrect: `[]` fetches once — when `bookId` changes from the parent, the component does not re-fetch.
- Why B is correct: The effect depends on `bookId` — it should re-run when that value changes.
- Why C is incorrect: No array means every render triggers the effect. Since the effect calls `setBook`, which triggers a re-render, this creates an infinite loop.
- Why D is incorrect: `[book]` creates a circular dependency — fetching sets `book`, which re-runs the effect, which fetches again.

---

## Question 8

A React application is deployed to AWS S3 with CloudFront. The React app calls an API Gateway endpoint. A developer hardcodes the API URL as `https://abc123.execute-api.us-east-1.amazonaws.com/prod` in a `fetch` call. What is the production problem with this approach and what is the fix?

- A) API Gateway URLs must be called from the server — they cannot be called from browser JavaScript.
- B) The hardcoded URL works but is brittle — if the API stage or region changes, the source code must be rebuilt and redeployed. The fix is to store the URL in a Vite environment variable (`VITE_API_URL`) and access it via `import.meta.env.VITE_API_URL` in the component.
- C) AWS API Gateway blocks cross-origin requests from CloudFront distributions by default.
- D) The URL must be encrypted at rest using AWS KMS before it can be embedded in a React build.

**Correct Answer:** B

**Explanation:** Hardcoded URLs in React source code are an operational problem — any change to the API endpoint requires a code change, rebuild, and redeployment. Vite environment variables allow different values per environment (development, staging, production) without code changes. Variables prefixed with `VITE_` are embedded in the browser bundle at build time.

**Distractor Analysis:**

- Why A is incorrect: Browser JavaScript can call API Gateway endpoints — that is their primary use case.
- Why B is correct: Environment variables decouple configuration from source code — a best practice for all environments.
- Why C is incorrect: API Gateway supports CORS configuration. CloudFront does not inherently block API calls.
- Why D is incorrect: API Gateway URLs are not secret credentials and do not require encryption at rest.

---

## Question 9

A developer implements state deletion this way:

```jsx
const handleDelete = async (id) => {
  await fetch(`/api/books/${id}`, { method: 'DELETE' });
  books.splice(books.findIndex(b => b.id === id), 1);
  setBooks(books);
};
```

The book disappears from the UI inconsistently — sometimes it works, sometimes the book remains visible. What is the bug?

- A) `DELETE` requests require a `Content-Type: application/json` header.
- B) `books.splice()` mutates the original array. `setBooks(books)` then passes the same array reference React already has. React's shallow comparison detects no change and may skip the re-render.
- C) `await fetch(...)` must be wrapped in a `try/catch` block or the delete silently fails.
- D) `findIndex` returns `-1` when the item is not found, and `splice(-1, 1)` removes the last element instead.

**Correct Answer:** B

**Explanation:** `splice` mutates the `books` array in place, then `setBooks(books)` passes the same array reference. React uses shallow reference equality to detect state changes — if the reference is the same object, React may skip re-rendering. The correct approach is `setBooks(prev => prev.filter(b => b.id !== id))`, which creates a new array.

**Distractor Analysis:**

- Why A is incorrect: `DELETE` requests typically have no body, so `Content-Type` is not needed.
- Why B is correct: Array mutation + same reference = React may not re-render. This is the most common array state bug.
- Why C is incorrect: Missing `try/catch` causes unhandled rejections, but the inconsistency described is a re-render issue, not an error handling issue.
- Why D is incorrect: `findIndex` returning `-1` causes `splice(-1, 1)` to remove the last item — a real bug, but not the cause of the inconsistency described here.

---

## Question 10

A production React SPA deployed to S3 + CloudFront calls an API Gateway endpoint backed by a Lambda function. The Lambda function accesses an RDS PostgreSQL database. A developer observes that under load, the Lambda function receives many concurrent invocations and the database starts rejecting connections with "too many clients." What AWS service solves this problem and why?

- A) AWS ElastiCache — caches database query results so fewer SQL queries reach RDS.
- B) AWS RDS Proxy — maintains a persistent connection pool between Lambda and RDS, multiplexing many Lambda invocations through a smaller pool of database connections.
- C) AWS CloudFront — its edge caching reduces the number of requests that reach Lambda.
- D) AWS SQS — queues Lambda invocations so they run one at a time, preventing concurrent database connections.

**Correct Answer:** B

**Explanation:** Lambda functions create a new database connection on each cold start, and many concurrent Lambda invocations create many simultaneous connections. RDS has a fixed maximum connection limit. RDS Proxy sits between Lambda and RDS and maintains a pool of persistent connections, multiplexing many Lambda invocations through far fewer actual database connections. No application code changes are required.

**Distractor Analysis:**

- Why A is incorrect: ElastiCache reduces read load but does not solve the connection count problem.
- Why B is correct: RDS Proxy is the AWS-designed solution for Lambda-to-RDS connection exhaustion.
- Why C is incorrect: CloudFront caches static assets and API responses (when configured), but does not directly reduce Lambda concurrency for dynamic API calls.
- Why D is incorrect: SQS would serialize requests and eliminate concurrency entirely — destroying the scalability benefit of Lambda. It also introduces significant latency.

---

### Question 11 (5 points)

A developer stores a JWT in `localStorage` and reads it in a `fetch` call: `headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }`. A security auditor flags this as high-risk. Why?

- A) `localStorage` is synchronous, which blocks the main thread when reading large tokens.
- B) Any JavaScript running on the page — including injected code from an XSS attack — can read `localStorage`, stealing the JWT and allowing an attacker to impersonate the user until the token expires.
- C) `localStorage` tokens expire automatically after 30 minutes, making long-lived JWTs unusable.
- D) The `Authorization` header is not allowed in cross-origin requests — the token must be sent as a query parameter.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `localStorage` reads are synchronous but extremely fast — blocking is not the security concern.
  - Why B is correct: XSS (Cross-Site Scripting) attacks inject malicious JavaScript that reads `localStorage` and exfiltrates stored tokens. An HttpOnly cookie prevents this because JavaScript cannot access it at all.
  - Why C is incorrect: `localStorage` has no automatic expiration — items persist until explicitly deleted or the user clears browser storage.
  - Why D is incorrect: The `Authorization` header is permitted in cross-origin requests when the server includes `Access-Control-Allow-Headers: Authorization` in its CORS configuration.

---

### Question 12 (5 points)

A developer uses `bcrypt.compare(plaintext, storedHash)`. The stored hash was created with cost factor 10 but the application now uses cost factor 12. What happens when a user logs in?

- A) `bcrypt.compare` throws an error because the cost factors do not match.
- B) `bcrypt.compare` reads the cost factor embedded in the stored hash and uses it automatically — the comparison succeeds if the password is correct regardless of the current default cost factor.
- C) `bcrypt.compare` always rehashes the password with cost factor 12 before comparing, causing all old hashes to fail verification.
- D) The login returns `false` for all attempts until the user resets their password with the new cost factor.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `bcrypt.compare` does not throw when cost factors differ — it extracts the cost factor from the hash string itself.
  - Why B is correct: The bcrypt hash format encodes the algorithm, cost factor, and salt in the hash string (`$2b$12$...`). `bcrypt.compare` extracts these parameters from the stored hash and applies them — it does not use the application's current default.
  - Why C is incorrect: `bcrypt.compare` never modifies the stored hash — it only verifies the plaintext against it.
  - Why D is incorrect: Existing hashes remain valid after changing the default cost factor. New registrations will use the new factor; existing accounts use their original hash until they next change their password.

---

### Question 13 (5 points)

A JWT payload contains `{ "userId": 42, "role": "admin", "exp": 1735689600 }`. A developer decodes it with `jwt.decode(token)` instead of `jwt.verify(token, secret)` and uses `decoded.role` to authorize an admin action. What is the security vulnerability?

- A) `jwt.decode` returns `null` for tokens with an `exp` claim — the authorization check will always fail.
- B) `jwt.decode` does not verify the signature — an attacker can forge a token with `"role": "admin"` and gain unauthorized access because the signature is never checked.
- C) `jwt.decode` only returns the header, not the payload — `decoded.role` will be `undefined`.
- D) `jwt.decode` automatically refreshes expired tokens, potentially granting access after the token should have been invalid.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `jwt.decode` works with all valid base64url-encoded JWTs — the `exp` claim does not cause it to return `null`.
  - Why B is correct: `jwt.decode` is a base64url decode with no cryptographic verification. Anyone can construct a token with any payload and `jwt.decode` will return its contents as if it were legitimate. Always use `jwt.verify` for authorization decisions.
  - Why C is incorrect: `jwt.decode` returns the full decoded payload (and optionally the header with `{ complete: true }`) — not just the header.
  - Why D is incorrect: `jwt.decode` performs no expiration check and no token renewal — it simply decodes without validation.

---

### Question 14 (5 points)

The login endpoint returns the same error message `"Invalid email or password"` whether the email is not found or the password is wrong. Why is this intentional?

- A) It simplifies the code — only one error object needs to be created.
- B) Returning different messages for wrong email vs wrong password is a user enumeration vulnerability — an attacker could discover which email addresses have accounts by observing which error they receive.
- C) Express requires all `next(error)` calls to use the same error message to prevent duplicate error handler executions.
- D) bcrypt.compare cannot distinguish between a wrong password and a missing user, so the error message must be generic.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Code simplicity is a benefit but not the security reason. A developer could easily write two separate error objects.
  - Why B is correct: User enumeration allows an attacker to build a list of valid email addresses from the application, which can then be used for targeted phishing or credential stuffing. A generic error message prevents this.
  - Why C is incorrect: Express has no such restriction — multiple `next(err)` calls with different messages are perfectly valid.
  - Why D is incorrect: `bcrypt.compare` compares a plaintext password against a hash — it is only called after the user record is found. The generic message is a deliberate security choice, not a bcrypt limitation.

---

### Question 15 (5 points)

`requireAuth` middleware runs before `requireRole`. What happens if `requireRole` is applied without `requireAuth` before it?

- A) `requireRole` works correctly because it reads the `Authorization` header directly.
- B) `req.user` would be `undefined` because `requireAuth` is responsible for setting it. `requireRole` checks `if (!req.user)` and returns 401 or crashes if the null check is missing.
- C) Express automatically runs all middleware in alphabetical order, so `requireAuth` always runs before `requireRole`.
- D) `requireRole` only needs to run after `requireAuth` in production — in development, the order does not matter.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `requireRole` reads `req.user.role` — it does not read the `Authorization` header itself. Without `requireAuth`, `req.user` is never set.
  - Why B is correct: `requireAuth` decodes the JWT and sets `req.user`. `requireRole` depends on `req.user` existing. If `requireAuth` is skipped, `req.user` is `undefined` and accessing `req.user.role` throws a `TypeError`.
  - Why C is incorrect: Express runs middleware in registration order, not alphabetical order.
  - Why D is incorrect: The dependency between `requireAuth` and `requireRole` is a code logic requirement — it applies in all environments.

---

### Question 16 (5 points)

A `TokenExpiredError` is caught in `requireAuth`. What is the correct HTTP status code to return and why?

- A) `403 Forbidden` — the token exists but permission is denied.
- B) `401 Unauthorized` — the token was valid but is no longer a valid credential; the client must obtain a new token.
- C) `400 Bad Request` — an expired token is a malformed request.
- D) `200 OK` with an `expired: true` field — the client should check this flag.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `403` means authenticated but lacks permission. An expired token is an authentication failure — the user's identity cannot be confirmed, so `401` is correct.
  - Why B is correct: `401` signals that authentication is required or has failed. The client should re-authenticate (log in again to get a new token) and retry.
  - Why C is incorrect: `400` is for malformed requests such as invalid JSON or missing fields. An expired token is syntactically valid — it is semantically invalid from an authentication standpoint.
  - Why D is incorrect: Returning `200` for a failed authentication is a serious error — clients and intermediaries treat `200` as success. Security middleware at the API gateway level would not block the request if it received `200`.

---

### Question 17 (5 points)

AWS Cognito User Pools issue tokens after authentication. Which token should a React app send to API Gateway for identity verification, and what type is it?

- A) The refresh token — it has the longest validity and is used for all API calls.
- B) The ID token or access token — both are JWTs. The ID token contains user identity claims; the access token is used to authorize API calls. API Gateway Lambda Authorizers typically verify the access token.
- C) The client secret from the Cognito app client configuration — it is embedded in the request header.
- D) A session cookie set by Cognito's hosted UI — it is automatically included in all requests.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The refresh token is used to obtain new access/ID tokens — it is never sent to resource APIs.
  - Why B is correct: Cognito issues three tokens: ID token (user identity), access token (API authorization), and refresh token (token renewal). API calls use the access token in the `Authorization: Bearer` header. Lambda Authorizers verify it using the Cognito JWKS endpoint.
  - Why C is incorrect: The client secret is used in server-to-server OAuth flows — it is never embedded in client-side requests or sent to APIs.
  - Why D is incorrect: Cognito's hosted UI can set cookies for session management, but REST API calls use Bearer tokens in the `Authorization` header — not cookies.

---

### Question 18 (5 points)

A Postman collection variable `token` is set by a Tests script after the login request. What is the advantage of using `pm.collectionVariables.set('token', json.token)` compared to manually copying the token from the response?

- A) Collection variables are automatically encrypted at rest — manually copied tokens are stored in plain text.
- B) The script automatically updates the token in all protected requests whenever login is re-run, eliminating the manual copy-paste step and reducing the chance of testing with a stale or expired token.
- C) Collection variables bypass CORS restrictions that affect manually set headers.
- D) Postman requires collection variables for Bearer tokens — manually entered values are ignored.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Postman stores collection variables in plain text — there is no automatic encryption distinction between scripted and manual values.
  - Why B is correct: Automating token capture ensures that every test run uses the freshly issued token. This is especially important when the JWT expires between test sessions.
  - Why C is incorrect: CORS restrictions apply to browser-based requests — Postman makes direct HTTP requests and is not subject to browser CORS enforcement.
  - Why D is incorrect: Postman accepts manually entered Bearer tokens — scripted capture is a convenience, not a requirement.

---

### Question 19 (5 points)

A developer adds `const token = jwt.sign({ userId, email, role }, secret, { expiresIn: '24h' })`. The payload contains `role: 'student'`. An attacker intercepts the token, base64url-decodes the payload, changes `"role": "admin"`, and re-encodes it. What prevents this attack from succeeding?

- A) JWT payloads are encrypted — the attacker cannot read or modify them.
- B) The JWT signature is computed from both the header and the payload using the server's secret. Modifying the payload invalidates the signature, and `jwt.verify` will reject the tampered token with a `JsonWebTokenError`.
- C) JWTs contain a checksum field in the payload that detects modification.
- D) The `expiresIn` option locks the payload — any modification causes immediate expiry.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: JWT payloads are only base64url-encoded, not encrypted. The attacker can read and modify the bytes — but cannot produce a valid signature without the secret.
  - Why B is correct: The third section of a JWT (the signature) is `HMACSHA256(base64url(header) + '.' + base64url(payload), secret)`. Changing the payload changes the signature input, producing a mismatch that `jwt.verify` detects and rejects.
  - Why C is incorrect: JWTs have no checksum field — the signature is the integrity mechanism.
  - Why D is incorrect: `expiresIn` sets the `exp` claim — it has no relationship to payload immutability.

---

### Question 20 (5 points)

In the full-stack architecture (React → API Gateway → Lambda → RDS), where should the `JWT_SECRET` be stored in a production deployment?

- A) In the Vite `.env` file prefixed with `VITE_` so both the React app and Lambda can access it.
- B) Hardcoded in `middleware/auth.js` using a long random string literal so it cannot be changed accidentally.
- C) In AWS Secrets Manager or AWS Systems Manager Parameter Store, retrieved by the Lambda function at cold-start or via environment variable injection — never committed to source code.
- D) In the React app's `localStorage` so the frontend can verify tokens client-side without calling the backend.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `VITE_` variables are embedded in the client-side JavaScript bundle and are publicly visible — a JWT secret must never be in the client bundle.
  - Why B is incorrect: Hardcoded secrets in source code are exposed to anyone with repository access and cannot be rotated without a code change and redeployment.
  - Why C is correct: AWS Secrets Manager stores secrets encrypted at rest and in transit. Lambda retrieves the secret at runtime via the AWS SDK or environment variable injection. Secrets can be rotated without redeploying code.
  - Why D is incorrect: The JWT secret is used to sign and verify tokens — it must remain server-side only. Exposing it to the client would allow anyone to forge valid tokens.
