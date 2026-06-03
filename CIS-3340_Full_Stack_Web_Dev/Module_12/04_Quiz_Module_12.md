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
