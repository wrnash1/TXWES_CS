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

---

### Question 11 (5 points)

What is the output order of the following code?

```javascript
console.log('A');
Promise.resolve().then(() => console.log('B'));
setTimeout(() => console.log('C'), 0);
console.log('D');
```

- A) A, B, C, D
- B) A, D, C, B
- C) A, D, B, C
- D) A, B, D, C

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Promise microtasks do not run before synchronous code — `D` must print before `B`.
  - Why B is incorrect: Microtasks (Promise `.then`) drain before macrotasks (`setTimeout`), so `B` runs before `C`.
  - Why C is correct: Synchronous code runs first (A, D), then the microtask queue drains (B), then the macrotask queue (C).
  - Why D is incorrect: `D` is synchronous and prints before `B` which is a microtask queued after `D`.

---

### Question 12 (5 points)

Which `Promise.all` behavior distinguishes it from `Promise.allSettled`?

- A) `Promise.all` runs Promises sequentially; `Promise.allSettled` runs them in parallel.
- B) `Promise.all` rejects immediately if any input Promise rejects; `Promise.allSettled` waits for all Promises to settle and always fulfills.
- C) `Promise.all` only accepts an array of two Promises; `Promise.allSettled` accepts any number.
- D) `Promise.all` returns values in the order they resolve; `Promise.allSettled` returns them in input order.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Both methods start all Promises simultaneously — neither runs them sequentially.
  - Why B is correct: `Promise.all` short-circuits and rejects as soon as any Promise rejects. `Promise.allSettled` always waits for every Promise and returns an array describing each outcome.
  - Why C is incorrect: Both methods accept an iterable of any length.
  - Why D is incorrect: Both methods return results in input array order, not in resolution order.

---

### Question 13 (5 points)

A developer wants to send a POST request with a JSON body using `fetch()`. Which header is required for the server to correctly parse the body?

- A) `Accept: application/json`
- B) `Authorization: Bearer token`
- C) `Content-Type: application/json`
- D) `X-Requested-With: fetch`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `Accept: application/json` tells the server what response format the client wants — it does not describe the request body format.
  - Why B is incorrect: `Authorization` carries authentication credentials — it does not tell the server how to parse the body.
  - Why C is correct: `Content-Type: application/json` informs the server that the request body is JSON-encoded, enabling it to parse the body correctly.
  - Why D is incorrect: `X-Requested-With` is a non-standard legacy header sometimes added by older AJAX libraries — it is not required for JSON body parsing.

---

### Question 14 (5 points)

An `async` function has no explicit `return` statement. What does it return?

- A) `null`
- B) `undefined` wrapped in a resolved Promise
- C) An empty object `{}`
- D) A rejected Promise

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A function without a return statement produces `undefined`, not `null`.
  - Why B is correct: `async` functions always return a Promise. When the function body completes without an explicit `return`, the returned Promise resolves with `undefined`.
  - Why C is incorrect: An `async` function without a return statement never produces an empty object.
  - Why D is incorrect: The returned Promise is fulfilled, not rejected, when there is no explicit `throw` or rejected `await`.

---

### Question 15 (5 points)

A developer needs to abort a `fetch()` request if it takes longer than 5 seconds. Which built-in browser API enables this?

- A) `clearTimeout(fetchPromise)`
- B) `fetch(url, { timeout: 5000 })`
- C) `AbortController` — create a controller, pass `signal` to fetch, and call `controller.abort()` after a timeout
- D) `Promise.race([fetch(url), Promise.reject('timeout')])`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `clearTimeout` cancels a `setTimeout` callback — it cannot cancel a `fetch()` Promise.
  - Why B is incorrect: The Fetch API does not accept a `timeout` option — there is no built-in timeout parameter.
  - Why C is correct: `AbortController` is the standard mechanism for cancelling fetch requests. Pass `{ signal: controller.signal }` to `fetch()`, then call `controller.abort()` when the timeout fires.
  - Why D is incorrect: `Promise.race` with a rejecting Promise causes the caller to receive the rejection, but the underlying network request continues running in the background, consuming resources.

---

### Question 16 (5 points)

When a `fetch()` call succeeds but the server returns a 500 status code, what happens to the returned Promise?

- A) It rejects with a `TypeError: Failed to fetch` error.
- B) It fulfills with a `Response` object where `response.ok` is `false` and `response.status` is `500`.
- C) It rejects with an `HttpError` containing the status code.
- D) It fulfills with `null` because 500 responses have no body.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `TypeError: Failed to fetch` occurs for network-level failures — not for HTTP error responses.
  - Why B is correct: The Fetch API only rejects for network failures. Any HTTP response, including 5xx errors, fulfills the Promise. The developer must check `response.ok` or `response.status`.
  - Why C is incorrect: There is no built-in `HttpError` type in the Fetch API — developers typically throw their own errors after checking `response.ok`.
  - Why D is incorrect: 500 responses can and do have a body. The Promise fulfills with the `Response` regardless of body content.

---

### Question 17 (5 points)

What is "callback hell" and how do Promises solve it?

- A) Callback hell refers to excessive use of `requestAnimationFrame` callbacks; Promises replace them with `async` animation loops.
- B) Callback hell is deeply nested async callbacks where error handling is duplicated at each level and control flow is hard to follow; Promises flatten the structure into a chain with a single centralized `.catch()`.
- C) Callback hell describes browser compatibility issues with older `addEventListener` syntax; Promises are a modern cross-browser replacement.
- D) Callback hell refers to attaching too many listeners to the same element; Promises provide a one-time subscription model.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `requestAnimationFrame` is used for animation timing — it is unrelated to callback hell.
  - Why B is correct: Callback hell (the "pyramid of doom") is deeply nested error-first callbacks. Promise chaining flattens this into a linear sequence with a single `.catch()` for all errors.
  - Why C is incorrect: Callback hell is about code structure and readability, not browser compatibility.
  - Why D is incorrect: Too many event listeners is a different problem managed via event delegation, not callback hell.

---

### Question 18 (5 points)

A Lambda function's `fetch()` call to a downstream API takes 5 seconds. The Lambda timeout is configured to 3 seconds. What is the result?

- A) Lambda automatically retries the request three times before returning an error.
- B) Lambda terminates the function at 3 seconds and returns a 504 Gateway Timeout to API Gateway.
- C) The Lambda timeout does not affect in-flight `fetch()` requests — the downstream API response arrives after 5 seconds.
- D) API Gateway automatically increases the Lambda timeout to match the downstream API response time.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Lambda does not automatically retry on timeout — retry logic must be explicitly implemented.
  - Why B is correct: When a Lambda function's configured timeout (3s) is shorter than the downstream operation's duration (5s), Lambda kills the function and the caller receives a 504 error.
  - Why C is incorrect: Lambda's timeout terminates the entire function execution, including all in-flight async operations.
  - Why D is incorrect: API Gateway and Lambda timeouts are independent settings that must be configured separately.

---

### Question 19 (5 points)

A developer wraps an async function call in `try/catch` but omits `await`. What happens when the async function throws?

```javascript
function handleClick() {
  try {
    loadData(); // async function — await omitted
  } catch (error) {
    showError(error);
  }
}
```

- A) The `catch` block catches the error and calls `showError` as expected.
- B) The error is caught but silently swallowed — `showError` is never called.
- C) The `catch` block is never triggered because the error occurs inside a Promise — it becomes an unhandled rejection.
- D) The code throws a `SyntaxError` at parse time because `await` is required inside `try/catch`.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Without `await`, the `try/catch` block completes synchronously before the async function rejects.
  - Why B is incorrect: The error is not silently swallowed — it becomes an unhandled Promise rejection logged in the console.
  - Why C is correct: Without `await`, `try/catch` only catches synchronous errors before `loadData()` returns its Promise. Errors inside the async function occur after the `catch` block has already exited.
  - Why D is incorrect: Omitting `await` is a logic error, not a syntax error — the code parses and runs without issue.

---

### Question 20 (5 points)

What does `response.headers.get('Content-Type')` return when the server sends `Content-Type: application/json; charset=utf-8`?

- A) `{ type: 'application/json', charset: 'utf-8' }`
- B) `'application/json'` with the charset parameter stripped
- C) `'application/json; charset=utf-8'` — the full header value as a string
- D) `true` indicating JSON content type is present

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `headers.get()` returns a raw string — it does not parse headers into structured objects.
  - Why B is incorrect: `headers.get()` returns the full header value including all parameters — it does not strip the charset.
  - Why C is correct: `Headers.get()` returns the complete header value string exactly as sent by the server, including semicolon-separated parameters.
  - Why D is incorrect: `headers.get()` returns a string or `null` — never a boolean.
