# Quiz: Module 14 — Promises and Async/Await: Patterns in Practice

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

**Instructions:** Choose the single best answer for each question.

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
