# Quiz: Module 14 — Promises and Async/Await: Patterns in Practice

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question. Each question is worth 5 points (20 questions × 5 points = 100 points).

---

### Question 1

Three API requests are independent — none depends on the others' results. Which code retrieves all three most efficiently?

- A) Three sequential `await` calls, one per request
- B) `Promise.all` with all three `fetch` calls
- C) `setTimeout` to stagger the three requests
- D) A `for...of` loop with `await` inside

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Sequential `await` forces each request to wait for the previous one to complete. For three 200ms requests, total time would be ≈ 600ms. Since the requests are independent, this serialization is unnecessary.
- *Why B is correct:* `Promise.all` starts all three requests simultaneously. All three network calls are in-flight at the same time. Total wait time equals the slowest single response — approximately 200ms instead of 600ms. This is the correct pattern for independent parallel operations.
- *Why C is incorrect:* `setTimeout` adds artificial delay and does not coordinate results. It does not make requests parallel in any useful way.
- *Why D is incorrect:* `await` inside a `for...of` loop is sequential — each iteration waits for the previous `await` to resolve before starting the next. This has the same performance problem as option A.

---

### Question 2

What does `Promise.allSettled([p1, p2, p3])` return when `p2` rejects?

- A) A rejected Promise with `p2`'s reason
- B) A fulfilled Promise with only the two successful results
- C) A fulfilled Promise with an array of three result objects, each describing its outcome
- D) `undefined` — `allSettled` does not return a value

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.allSettled` never rejects. Unlike `Promise.all`, it does not fail fast. It waits for all Promises to settle and always fulfills.
- *Why B is incorrect:* `allSettled` includes all results — both fulfilled and rejected — not just the successful ones. Filtering is the caller's responsibility.
- *Why C is correct:* `Promise.allSettled` always fulfills with an array containing one result object per input Promise. Each object has `{ status: 'fulfilled', value: ... }` or `{ status: 'rejected', reason: ... }`. All three results are present regardless of which ones failed.
- *Why D is incorrect:* `allSettled` does return a value — a Promise that fulfills with the results array.

---

### Question 3

A developer uses `Promise.race` to implement a fetch timeout. The fetch takes 400ms and the timeout is set to 200ms. What is the outcome?

- A) The fetch result is returned after 400ms — `race` waits for all
- B) The race rejects with the timeout error after 200ms
- C) Both results are returned — whichever came first is used
- D) The fetch is cancelled and retried after 200ms

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.race` settles with the **first** Promise to settle — it does not wait for all. The timeout Promise settles at 200ms, before the fetch at 400ms.
- *Why B is correct:* The timeout Promise rejects at 200ms. Since that is before the fetch resolves at 400ms, `Promise.race` settles with the timeout rejection. The race rejects with the timeout error.
- *Why C is incorrect:* `Promise.race` returns a single value from the single first-settling Promise — not both. Once settled, the race is over.
- *Why D is incorrect:* `Promise.race` does not cancel or retry anything. The fetch continues in flight even after the race has settled — it simply has no handler anymore.

---

### Question 4

What does `JSON.stringify` do with a function property in an object?

```javascript
const obj = { name: 'Alice', greet: () => 'hello' };
console.log(JSON.stringify(obj));
```

- A) Throws a `TypeError` because functions cannot be serialized
- B) Converts the function to its source code string
- C) Omits the `greet` property entirely — output is `'{"name":"Alice"}'`
- D) Converts it to `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `JSON.stringify` does not throw for functions — it silently omits them. This silent omission is the behavior to know (and the potential bug to watch for).
- *Why B is incorrect:* JSON does not support functions. The property is not converted to a string representation of the source code — it is dropped entirely.
- *Why C is correct:* `JSON.stringify` silently omits any property whose value is a function, `undefined`, or a `Symbol`. The output is `'{"name":"Alice"}'` — `greet` is not present at all. This is defined behavior, not an error.
- *Why D is incorrect:* `null` replacement applies to values like `Infinity` and `NaN`. Functions are omitted (key and value removed), not replaced with `null`. The distinction matters: a `null` replacement keeps the key; omission removes it entirely.

---

### Question 5

After this round-trip, what is `back.created`?

```javascript
const obj = { created: new Date(2025, 0, 15) };
const back = JSON.parse(JSON.stringify(obj));
```

- A) A `Date` object equal to January 15, 2025
- B) `null`
- C) `undefined`
- D) An ISO 8601 date string like `'2025-01-15T...'`

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* `JSON.stringify` converts `Date` objects to ISO 8601 strings. `JSON.parse` has no special handling for date strings — it produces a plain string, not a `Date` object.
- *Why B is incorrect:* `null` would result from serializing `Infinity` or `NaN`. A `Date` object serializes to a string, not `null`.
- *Why C is incorrect:* `undefined` is not the result. The `created` key is present in the JSON — its value is a string.
- *Why D is correct:* `JSON.stringify` calls `.toISOString()` on `Date` objects, producing a string like `'2025-01-15T06:00:00.000Z'`. `JSON.parse` reads that string back as a plain JavaScript string, not a `Date`. To restore a `Date`, you must call `new Date(back.created)` explicitly.

---

### Question 6

A developer catches an error after using `AbortController`:

```javascript
controller.abort();
```

How should they distinguish an intentional abort from a real network error?

- A) Check `err.message === 'aborted'`
- B) Check `err.name === 'AbortError'`
- C) Check `err.code === 20`
- D) Aborted requests do not produce errors — they resolve with `null`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The message of an `AbortError` varies by browser and is not a reliable check. `err.name` is the stable, specified property to check.
- *Why B is correct:* When `controller.abort()` is called, the fetch Promise rejects with a `DOMException` (in browsers) or similar error object whose `name` property is `'AbortError'`. The standard pattern is `if (err.name === 'AbortError') { /* intentional cancel */ }`. This distinguishes it from network errors (e.g., `TypeError` for no connection).
- *Why C is incorrect:* `err.code` is an older API on `DOMException` objects and is not the recommended check. `err.name` is the standard approach.
- *Why D is incorrect:* Aborting a fetch causes the Promise to **reject**, not resolve. If the rejection is not caught, it becomes an unhandled rejection.

---

### Question 7

Which `Promise` combinator should be used when you want to display partial results even if some requests fail?

- A) `Promise.all`
- B) `Promise.race`
- C) `Promise.allSettled`
- D) `Promise.any`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.all` rejects immediately if any request fails — you lose all results, including the successful ones. This is the opposite of what is needed.
- *Why B is incorrect:* `Promise.race` settles with the first result only — it does not collect all results and does not wait for others.
- *Why C is correct:* `Promise.allSettled` waits for every Promise to settle and returns all results, both fulfilled and rejected. The caller inspects each result's `status` and handles successes and failures individually. This is the correct combinator when partial results are acceptable.
- *Why D is incorrect:* `Promise.any` fulfills with the first success and ignores the others. It does not collect all available results.

---

### Question 8

What is stored in `localStorage` by the following code?

```javascript
const prefs = { theme: 'dark', size: 14 };
localStorage.setItem('prefs', JSON.stringify(prefs));
```

- A) A JavaScript object `{ theme: 'dark', size: 14 }`
- B) The string `'{"theme":"dark","size":14}'`
- C) A reference to the `prefs` variable
- D) `undefined`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `localStorage` can only store strings. If you attempted to store an object directly (without `JSON.stringify`), it would be coerced to `'[object Object]'`. `JSON.stringify` converts the object to a JSON string first.
- *Why B is correct:* `JSON.stringify(prefs)` produces the string `'{"theme":"dark","size":14}'`. That string is what `setItem` stores. To retrieve the object, the caller must use `JSON.parse(localStorage.getItem('prefs'))`.
- *Why C is incorrect:* `localStorage` stores string values, not variable references. There is no concept of a reference to a JavaScript variable in `localStorage`.
- *Why D is incorrect:* `setItem` with a valid key and a JSON string stores that string successfully.

---

### Question 9

A developer writes an `async` function that loads data but forgets to handle errors. A fetch fails due to a network outage. What happens in a modern browser?

- A) The browser displays a built-in error page
- B) The `async` function returns `undefined` silently
- C) An unhandled Promise rejection is reported in the console
- D) The browser retries the fetch automatically

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The browser does not show an error page for JavaScript errors in running applications. That only happens for full navigation failures.
- *Why B is incorrect:* The `async` function does not silently return `undefined`. The unhandled rejection propagates and is reported.
- *Why C is correct:* When an `async` function throws (or `await`s a rejected Promise) and the rejection is not caught by `try/catch` or a `.catch` at the call site, the result is an unhandled Promise rejection. Modern browsers log an error to the console and fire an `unhandledrejection` event on `window`. Node.js logs a warning and may exit.
- *Why D is incorrect:* Browsers do not automatically retry failed fetch requests. Retry logic must be implemented manually.

---

### Question 10

A developer wants to load three pieces of data where the second and third are independent, but both depend on the first. What is the correct pattern?

- A) `Promise.all([fetch1, fetch2, fetch3])`
- B) Sequential `await` for all three
- C) `await` the first; then `Promise.all` for the other two
- D) `Promise.race([fetch1, fetch2, fetch3])`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* If fetch 2 and fetch 3 depend on data from fetch 1, they cannot start until fetch 1 completes. `Promise.all` starts all three simultaneously — fetches 2 and 3 would not have the first result yet.
- *Why B is incorrect:* Sequential `await` for all three forces fetch 3 to wait for fetch 2, even though they are independent of each other. This is unnecessarily slow.
- *Why C is correct:* `await` fetch 1 to get its result. Then use the result to build requests 2 and 3, and `Promise.all` to run them in parallel. Fetch 1 completes first (dependency honored); then 2 and 3 run concurrently (independence exploited). This is the optimal pattern.
- *Why D is incorrect:* `Promise.race` returns only the first result and discards the others. It does not collect all three results needed for the page.

---

### Question 11

What does `JSON.stringify({ a: undefined, b: 1, c: null })` produce?

- A) `'{"a":undefined,"b":1,"c":null}'`
- B) `'{"a":null,"b":1,"c":null}'`
- C) `'{"b":1,"c":null}'`
- D) `TypeError` because `undefined` cannot be serialized

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `undefined` is not a valid JSON value. `JSON.stringify` does not represent it as the literal text `undefined`.
- *Why B is incorrect:* `undefined` is not converted to `null` for object properties — it is omitted entirely. `null` conversion to `null` applies to array slots and the top-level value, not object property values of `undefined`.
- *Why C is correct:* `JSON.stringify` silently omits properties whose values are `undefined`, functions, or Symbols. Property `a` is dropped entirely. `null` is valid JSON and is preserved. The result is `'{"b":1,"c":null}'`.
- *Why D is incorrect:* No error is thrown. Omitting `undefined` properties is the specified, silent behavior of `JSON.stringify`.

---

### Question 12

A developer calls `controller.abort()` while a fetch is in flight. Which code correctly handles both the abort and real network errors?

```javascript
try {
  const res = await fetch(url, { signal: controller.signal });
  return await res.json();
} catch (err) {
  // ??? handle here
}
```

- A) `if (err.message === 'canceled') return;`
- B) `if (err.name === 'AbortError') return; throw err;`
- C) `if (err.status === 0) return;`
- D) `if (err instanceof DOMException) return;`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Error messages are not standardized across browsers. `err.message` may vary. `err.name` is the stable, specification-defined property to use for identifying `AbortError`.
- *Why B is correct:* Checking `err.name === 'AbortError'` identifies intentional cancellations. Returning silently (or swallowing the error) is the correct response — the abort was requested on purpose. Re-throwing with `throw err` ensures real network errors (e.g., `TypeError` for no connection) continue to propagate to the caller.
- *Why C is incorrect:* `err.status` is an HTTP status code from a `Response` object — it is not a property on thrown `Error` objects from a failed fetch.
- *Why D is incorrect:* While `AbortError` is an instance of `DOMException` in browsers, checking `instanceof DOMException` is too broad. Other `DOMException` types exist that should not be silently swallowed.

---

### Question 13

What does `Promise.any` return when given an array of three Promises that all reject?

- A) A fulfilled Promise with `undefined`
- B) A rejected Promise with the first rejection reason
- C) A rejected Promise with an `AggregateError` containing all three rejection reasons
- D) `null`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `Promise.any` does not fulfill when all Promises reject. When all reject, the result is itself a rejection.
- *Why B is incorrect:* `Promise.any` does not simply use the first rejection reason as its rejection value. The specification defines an `AggregateError` containing all rejection reasons, so callers can inspect every failure.
- *Why C is correct:* When every Promise in the array rejects, `Promise.any` rejects with an `AggregateError`. This special error type has an `.errors` array property containing the rejection reasons from all the Promises in order.
- *Why D is incorrect:* `Promise.any` never returns `null`. It returns a Promise that resolves or rejects.

---

### Question 14

Which statement about `await` inside a `for...of` loop is correct?

```javascript
async function loadItems(ids) {
  for (const id of ids) {
    const data = await fetchItem(id);
    console.log(data);
  }
}
```

- A) All `fetchItem` calls fire simultaneously and results are logged as they arrive
- B) Each `fetchItem` call waits for the previous one to complete before starting
- C) Using `await` inside a loop causes a `SyntaxError`
- D) The loop is skipped because `await` returns undefined inside a for loop

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `await` inside a `for...of` loop is sequential — each iteration pauses until the awaited Promise resolves before the loop advances to the next iteration. Use `map` + `Promise.all` for concurrent execution.
- *Why B is correct:* The `for...of` loop processes one item at a time. When `await fetchItem(id)` is encountered, the loop pauses until the Promise resolves, then continues to the next `id`. Total execution time equals the sum of all individual durations.
- *Why C is incorrect:* `await` inside a `for...of` loop is perfectly valid syntax within an `async` function. No error is thrown.
- *Why D is incorrect:* `await` returns the resolved value of the Promise — not `undefined`. The loop runs normally, just sequentially.

---

### Question 15

A developer wants to implement a 3-second timeout on a fetch request. Which code correctly uses `Promise.race` to achieve this?

- A) `fetch(url, { timeout: 3000 })`
- B) `setTimeout(() => fetch(url), 3000)`
- C) `Promise.race([fetch(url), new Promise((_, r) => setTimeout(() => r(new Error('Timeout')), 3000))])`
- D) `Promise.all([fetch(url), new Promise(resolve => setTimeout(resolve, 3000))])`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The `fetch` API does not accept a `timeout` option in the standard specification. This option would be silently ignored.
- *Why B is incorrect:* `setTimeout(() => fetch(url), 3000)` delays the start of the fetch by 3 seconds — it does not impose a timeout on the fetch itself.
- *Why C is correct:* `Promise.race` settles with whichever Promise settles first. The timeout Promise rejects after 3000ms. If the fetch takes longer than 3 seconds, the timeout wins and the race rejects. If the fetch resolves first, its result wins. This is the standard `Promise.race` timeout pattern.
- *Why D is incorrect:* `Promise.all` waits for both to fulfill. The timeout Promise resolves (not rejects) after 3 seconds — this would cause a 3-second delay to the result, not a timeout that cancels the fetch.

---

### Question 16

What value does `JSON.parse('null')` return?

- A) The string `'null'`
- B) `undefined`
- C) `null`
- D) `0`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `JSON.parse` parses the JSON string `'null'` as the JSON null literal, which maps to the JavaScript value `null` — not the string `'null'`.
- *Why B is incorrect:* `undefined` is not a valid JSON value and is not produced by `JSON.parse`. The JSON null literal maps to the JavaScript `null`, not `undefined`.
- *Why C is correct:* The JSON specification defines a `null` literal that corresponds to JavaScript's `null` value. `JSON.parse('null')` returns the JavaScript value `null`.
- *Why D is incorrect:* `0` is unrelated to `null`. JSON `null` maps to JavaScript `null`, not zero.

---

### Question 17

A developer reads from `localStorage` with `localStorage.getItem('missing-key')`. What is returned?

- A) `undefined`
- B) `null`
- C) An empty string `''`
- D) `0`

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* `getItem` returns `null` (not `undefined`) when the key does not exist. This distinction matters for type checks.
- *Why B is correct:* `localStorage.getItem(key)` returns `null` when the key has not been set. This is the specification-defined behavior. Always check `if (raw !== null)` before calling `JSON.parse` to avoid `JSON.parse(null)`, which returns `null` rather than your intended default.
- *Why C is incorrect:* An empty string would be returned if the key was explicitly set to an empty string: `localStorage.setItem('key', '')`. A missing key returns `null`, not `''`.
- *Why D is incorrect:* `0` would only be returned if the key was set to `'0'` and read back. A missing key always returns `null`.

---

### Question 18

The following code has a bug. What is it?

```javascript
async function loadDashboard() {
  const user = await apiFetch('/api/user');
  const posts = await apiFetch('/api/posts');
  const settings = await apiFetch('/api/settings');
  render(user, posts, settings);
}
```

- A) `apiFetch` cannot be called with `await` — use `.then` instead
- B) `render` is called before all three fetches complete
- C) All three fetches are sequential but they are independent — they should run in parallel with `Promise.all`
- D) `async` functions cannot contain more than one `await`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* `apiFetch` returns a Promise; using `await` on it is correct. `await` and `.then` are interchangeable approaches — one is not required over the other.
- *Why B is incorrect:* `render` is called after all three `await` calls have resolved — because each `await` pauses the function. `render` only runs after all three assignments complete.
- *Why C is correct:* The three fetches (`/api/user`, `/api/posts`, `/api/settings`) are independent — none needs the result of another to start. Running them sequentially wastes time. The fix is `const [user, posts, settings] = await Promise.all([apiFetch('/api/user'), apiFetch('/api/posts'), apiFetch('/api/settings')]);`.
- *Why D is incorrect:* `async` functions can have any number of `await` expressions. There is no limit.

---

### Question 19

What is the purpose of the second argument `null` in `JSON.stringify(obj, null, 2)`?

- A) It tells `JSON.stringify` to omit `null` values from the output
- B) It is a placeholder for the replacer argument; `null` means include all properties
- C) It sets the indent level to null (no indentation)
- D) It prevents circular reference errors

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The second argument does not filter `null` values. It is the replacer — a function or array that controls which properties are included. Passing `null` means no filtering: include everything.
- *Why B is correct:* `JSON.stringify(value, replacer, space)` — the second argument is the `replacer`. When `null`, no filtering occurs and all serializable properties are included. The third argument `2` sets the indentation to 2 spaces for pretty-printing.
- *Why C is incorrect:* The third argument controls indentation. The second argument `null` means no replacer is applied — it does not affect indentation.
- *Why D is incorrect:* `null` as the replacer does not provide circular reference protection. A circular reference in the object still throws a `TypeError`. Use a custom replacer function if you need to handle circular structures.

---

### Question 20

An async function makes several API calls. After the first `await`, the function throws an uncaught error. What happens?

```javascript
async function run() {
  const data = await fetchData();
  throw new Error('Something failed');   // no try/catch here
}

run();   // no .catch at the call site
```

- A) The error is silently discarded
- B) The program immediately crashes and stops
- C) `run()` returns a rejected Promise; browsers log an unhandled rejection warning
- D) The error is swallowed because it occurred after an `await`

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Errors thrown inside `async` functions are not silently discarded. They cause the function's returned Promise to reject.
- *Why B is incorrect:* In browsers, unhandled rejections do not stop the program immediately. The browser logs a warning to the console and fires an `unhandledrejection` event. Node.js may terminate the process depending on the version and configuration, but browsers do not crash.
- *Why C is correct:* A `throw` inside an `async` function causes its returned Promise to reject with the thrown error. Since `run()` is called without `.catch` and there is no `try/catch` around the call, the rejection is unhandled. Modern browsers and Node.js report this as an `UnhandledPromiseRejectionWarning` or `UnhandledRejectionError`.
- *Why D is incorrect:* Errors thrown after an `await` within an `async` function are not swallowed. They still reject the function's returned Promise, regardless of whether they occur before or after any `await`.
