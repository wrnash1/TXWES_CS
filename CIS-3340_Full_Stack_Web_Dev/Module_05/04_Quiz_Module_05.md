# Quiz: Module 05 - Asynchronous JavaScript

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

What state does a JavaScript Promise enter once it has completed successfully?

- A) Pending
- B) Fulfilled
- C) Rejected
- D) Resolved

**Correct Answer:** B

**Explanation:** A Promise transitions from Pending to Fulfilled when its asynchronous operation completes successfully, providing the resolved value to `.then()` handlers.

**Distractor Analysis:**

- Why A is incorrect: Pending is the initial state while the operation is still in progress — not a completion state.
- Why B is correct: Fulfilled is the specific terminal state for a successfully completed Promise.
- Why C is incorrect: Rejected is the terminal state for a failed Promise.
- Why D is incorrect: "Resolved" is an informal term for a Promise that has settled (either way), but it is not one of the three formal states defined in the specification.

---

## Question 2

Which of the following is the most accurate definition of the call stack in JavaScript?

- A) A browser security model that prevents scripts from one origin from making network requests to a different origin without explicit server permission.
- B) The LIFO data structure used by the JavaScript engine to track function execution contexts — each function call adds a frame, and each return removes one.
- C) The queue where resolved Promise callbacks wait before the event loop moves them onto the call stack for execution.
- D) A deployment pattern where two identical production environments alternate receiving live traffic to enable zero-downtime releases.

**Correct Answer:** B

**Explanation:** The call stack is the execution context tracker — JavaScript's single thread runs exactly what is on top of this stack. When a function is called, a frame is pushed; when it returns, the frame is popped.

**Distractor Analysis:**

- Why A is incorrect: This describes the Same-Origin Policy and CORS model — not the call stack.
- Why B is correct: The call stack is the LIFO execution context tracker for the JavaScript runtime.
- Why C is incorrect: This describes the microtask queue (Promise callbacks), not the call stack.
- Why D is incorrect: This describes a blue/green deployment strategy — a DevOps concept unrelated to JavaScript runtime.

---

## Question 3

A developer writes the following code but the console logs print in the wrong order. What is the root cause?

```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
console.log('C');
```

- A) `setTimeout` with 0ms delay executes synchronously before the next `console.log`.
- B) `setTimeout` callbacks are placed in the callback queue and only run after the call stack is fully empty — even a 0ms delay defers execution past synchronous code.
- C) `console.log` calls are asynchronous and execute in an unpredictable order.
- D) The JavaScript engine processes the last statement first (LIFO ordering) — `'C'` logs before `'A'`.

**Correct Answer:** B

**Explanation:** The event loop only moves the setTimeout callback from the queue to the stack after all synchronous statements finish, producing the output: A, C, B.

**Distractor Analysis:**

- Why A is incorrect: A 0ms delay does not mean synchronous execution — it means "run as soon as the call stack is empty."
- Why B is correct: The event loop moves callbacks only after the call stack is empty — synchronous code always runs first.
- Why C is incorrect: `console.log` is a synchronous call that executes immediately in order.
- Why D is incorrect: Sequential statements execute top-to-bottom, not in reverse.

---

## Question 4

An async function fetches data from an API but silently returns `undefined` instead of the expected data. What is the most likely cause?

- A) The `async` keyword was omitted from the function declaration.
- B) The developer forgot to use `await` before the `fetch()` call — the function returned before the Promise resolved, so the data was never captured.
- C) The Fetch API is not available inside async functions — `XMLHttpRequest` must be used instead.
- D) The `try/catch` block automatically returns `undefined` on success when no explicit `return` statement is present.

**Correct Answer:** B

**Explanation:** Without `await`, `fetch()` returns a Promise object immediately. The variable assigned to it holds an unresolved Promise, not the fetched data. The function returns `undefined` (or the unresolved Promise) before the network request completes.

**Distractor Analysis:**

- Why A is incorrect: If the `async` keyword were omitted, using `await` inside would throw a syntax error — not silently return `undefined`.
- Why B is correct: Missing `await` means the Promise is not unwrapped — the variable receives the Promise object, not its resolved value.
- Why C is incorrect: The Fetch API works perfectly inside async functions — that is the recommended pattern.
- Why D is incorrect: A `try/catch` block does not change return value behavior — if no error occurs, the `catch` block is skipped entirely.

---

## Question 5

When calling an AWS API Gateway endpoint from a browser front-end using `fetch()`, the request succeeds on the server but the browser blocks the response. What is the most likely cause and fix?

- A) The `fetch()` call used `async/await` instead of `.then()` — switching to `.then()` will resolve the block.
- B) The API Gateway endpoint is missing CORS headers in its response — the browser's Same-Origin Policy blocks the response until the server explicitly permits the cross-origin request.
- C) AWS Lambda functions written in Python automatically block browser responses — the function must be rewritten in Node.js.
- D) The browser blocks all HTTPS API responses unless the front-end is also served from HTTPS — switching both to HTTP will fix it.

**Correct Answer:** B

**Explanation:** Browsers enforce the Same-Origin Policy on responses. API Gateway must include `Access-Control-Allow-Origin` in its response headers. The request does reach the server (visible in CloudWatch logs), but the browser prevents JavaScript from reading the response without the permission header.

**Distractor Analysis:**

- Why A is incorrect: `async/await` and `.then()` are equivalent — syntax choice has no effect on CORS enforcement.
- Why B is correct: CORS is enforced at the browser level on the response. API Gateway's CORS configuration must include the correct `Access-Control-Allow-Origin` header.
- Why C is incorrect: Lambda runtime language does not affect CORS — the response headers matter, not the execution language.
- Why D is incorrect: This scenario describes a CORS block (successful server request, browser-side rejection), not a mixed-content protocol mismatch.

---

## Question 6

What does `Promise.allSettled([p1, p2, p3])` return when `p2` rejects and `p1` and `p3` fulfill?

- A) A rejected Promise containing only the error from `p2`.
- B) A fulfilled Promise containing an array where each element has `{ status: 'fulfilled', value: ... }` or `{ status: 'rejected', reason: ... }`.
- C) A fulfilled Promise containing only the results from `p1` and `p3`, skipping the rejected `p2`.
- D) Three separate Promises returned sequentially — `p1`, then an error, then `p3`.

**Correct Answer:** B

**Explanation:** `Promise.allSettled` always fulfills (never rejects) after all input Promises have settled. It returns an array of result objects where each object has a `status` field of either `'fulfilled'` (with a `value`) or `'rejected'` (with a `reason`). This allows the caller to handle each result independently.

**Distractor Analysis:**

- Why A is incorrect: `Promise.allSettled` never rejects — that is the key distinction from `Promise.all`.
- Why B is correct: `allSettled` reports every outcome regardless of individual failures.
- Why C is incorrect: All three results are returned — `allSettled` does not filter out rejections.
- Why D is incorrect: `Promise.allSettled` returns a single Promise that resolves with an array — not sequential Promises.

---

## Question 7

A developer writes an async function that makes two independent API calls:

```javascript
async function loadDashboard() {
  const users    = await fetchUsers();
  const products = await fetchProducts();
  render(users, products);
}
```

A performance review flags this as slow. What is the issue and the correct fix?

- A) `async` functions cannot contain more than one `await` — split each call into a separate function.
- B) The two `await` calls execute sequentially — `fetchProducts` does not start until `fetchUsers` completes. Fix: use `Promise.all([fetchUsers(), fetchProducts()])` to run both in parallel.
- C) `await` is only efficient with `fetch()` — custom async functions like `fetchUsers` must use `.then()` instead.
- D) The function is missing a `return` statement — without it, both Promises are cancelled before they resolve.

**Correct Answer:** B

**Explanation:** Sequential `await` statements execute one after the other — the second request waits for the first to complete before it starts. Since both requests are independent, starting them in parallel with `Promise.all` cuts the total wait time approximately in half.

**Distractor Analysis:**

- Why A is incorrect: `async` functions can contain any number of `await` statements.
- Why B is correct: `Promise.all([fetchUsers(), fetchProducts()])` starts both requests simultaneously and waits for both to settle.
- Why C is incorrect: `await` works with any Promise-returning function — there is no restriction to `fetch()`.
- Why D is incorrect: Missing `return` would cause the caller to receive `undefined`, but it does not cancel the internal Promises.

---

## Question 8

A developer uses the Fetch API and writes the following code. It runs without throwing an error, but the data displayed on the page is wrong.

```javascript
async function loadData() {
  const response = await fetch('/api/items');
  const data = response.json();
  renderItems(data);
}
```

What is the bug?

- A) `fetch` should be called without `await` — adding `await` breaks JSON parsing.
- B) `response.json()` returns a Promise — `await` is missing before it, so `data` receives an unresolved Promise object instead of the parsed JSON.
- C) `response.json()` can only be called once — the data was consumed by the `await fetch()` call.
- D) The function is missing a `try/catch` block, causing JSON parsing to fail silently.

**Correct Answer:** B

**Explanation:** `response.json()` is an asynchronous method that returns a Promise. Without `await`, `data` receives that unresolved Promise object rather than the actual JSON data. The fix is `const data = await response.json()`.

**Distractor Analysis:**

- Why A is incorrect: `await` before `fetch()` is correct and necessary — removing it would make `response` a Promise, not a Response object.
- Why B is correct: Both `fetch()` and `response.json()` return Promises that must be awaited.
- Why C is incorrect: `response.json()` can only be called once per response (the body stream can only be read once), but that is not what caused this bug.
- Why D is incorrect: A missing `try/catch` means errors are unhandled, but it does not cause `data` to receive the wrong type.

---

## Question 9

Which of the following correctly describes how to handle a `fetch()` request that receives an HTTP 404 status code?

- A) The `fetch()` Promise automatically rejects for 4xx status codes, so a `.catch()` handler is sufficient.
- B) The `fetch()` Promise fulfills for all HTTP responses including 4xx and 5xx — the developer must check `response.ok` or `response.status` manually and throw an error if appropriate.
- C) A 404 response causes `response.json()` to throw a `SyntaxError` because 404 responses have empty bodies.
- D) `fetch()` rejects for all non-200 status codes — only `response.ok === true` prevents the Promise from rejecting.

**Correct Answer:** B

**Explanation:** The Fetch API only rejects its Promise for network-level failures (no internet, DNS failure, request blocked by CORS). Any completed HTTP response — including 404, 500, and 401 — fulfills the Promise. Developers must manually check `response.ok` (true for 200-299) or `response.status` and throw an error if the status indicates failure.

**Distractor Analysis:**

- Why A is incorrect: The Fetch Promise does NOT reject for 4xx or 5xx responses — only for network failures.
- Why B is correct: `response.ok` is `false` for 404 responses, but the Promise still fulfills. Manual status checking is required.
- Why C is incorrect: 404 responses may or may not have a body — it depends on the server. The bug is not in `response.json()`.
- Why D is incorrect: `fetch()` never rejects based on HTTP status — only on network-level errors.

---

## Question 10

An AWS Lambda function with a Node.js runtime is configured as an API Gateway handler. The function makes a DynamoDB `getItem` call using the AWS SDK and should return the item in the response. A developer writes:

```javascript
exports.handler = async (event) => {
  const params = { TableName: 'Users', Key: { userId: { S: event.pathParameters.id } } };
  const result = dynamodb.getItem(params).promise();
  return { statusCode: 200, body: JSON.stringify(result.Item) };
};
```

Users receive `statusCode: 200` but the body is `undefined`. What is the bug?

- A) The `async` keyword is not needed on Lambda handlers — remove it to fix the response.
- B) `dynamodb.getItem(params).promise()` returns a Promise — `await` is missing, so `result` holds an unresolved Promise instead of the DynamoDB response object.
- C) Lambda handlers cannot use the AWS SDK — the handler must use `fetch()` to call the DynamoDB REST API instead.
- D) `JSON.stringify` cannot serialize DynamoDB response objects — use `JSON.stringify(result)` without `.Item` instead.

**Correct Answer:** B

**Explanation:** The AWS SDK v2 `.promise()` method returns a Promise. Without `await`, `result` holds an unresolved Promise object, not the DynamoDB data. `result.Item` on a Promise object is `undefined`. The fix is `const result = await dynamodb.getItem(params).promise()`.

**Distractor Analysis:**

- Why A is incorrect: The `async` keyword is correct and required here since the handler uses `await` (or should use it). Removing it would cause a syntax error.
- Why B is correct: Missing `await` before the DynamoDB Promise is the exact cause of the `undefined` body.
- Why C is incorrect: Lambda handlers can and should use the AWS SDK for DynamoDB access — that is the standard pattern.
- Why D is incorrect: `result.Item` is the correct property for a DynamoDB `getItem` response — but it is undefined because `result` is an unresolved Promise, not because `JSON.stringify` has a serialization issue.
