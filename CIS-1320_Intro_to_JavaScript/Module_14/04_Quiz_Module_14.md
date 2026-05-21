# Quiz: Module 14 - Promises & Async/Await
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

**Question 1**
What does a function declared with the 'async' keyword always return?
*   A) An array of values
*   B) A Promise
*   C) A boolean representing success or failure
*   D) The direct return value without wrapping
*   **Correct Answer:** B) An async function always returns a Promise. If the function returns a value, the Promise is resolved with that value.
*   **Distractor Analysis:**
    *   *Why correct:* An async function always returns a Promise. If the function returns a value, the Promise is resolved with that value.
    *   The other options are incorrect.

---

**Question 2**
Which of the following most accurately describes the **`await` expression** in JavaScript?
*   A) A keyword that pauses the entire JavaScript runtime until a Promise settles, blocking all other code
*   B) An operator used inside an `async` function that pauses only that function's execution until the awaited Promise resolves, then resumes with the resolved value
*   C) A method available on Promise objects that is equivalent to calling `.then()` on the Promise
*   D) A declaration keyword used to create a new asynchronous variable that updates automatically when a Promise resolves
*   **Correct Answer:** B) An operator used inside an `async` function that pauses only that function's execution until the awaited Promise resolves, then resumes with the resolved value.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `await` suspends only the enclosing `async` function, not the whole runtime; the event loop continues processing other tasks while waiting.
    *   *Why B is correct:* `await promiseValue` yields control back to the event loop and resumes the `async` function once the Promise settles, making asynchronous code appear synchronous in structure.
    *   *Why C is incorrect:* `await` is a language operator, not a method on Promise; it is syntactic sugar for consuming a Promise, but is not the same as calling `.then()`.
    *   *Why D is incorrect:* There are no "asynchronous variables" in JavaScript; `await` is used in expressions to obtain the resolved value, not to declare special variable types.

---

**Question 3**
What is the resolved value of the following Promise chain?
```javascript
Promise.resolve(5)
  .then(n => n * 2)
  .then(n => n + 1);
```
*   A) `5`
*   B) `10`
*   C) `11`
*   D) A rejected Promise because arithmetic inside `.then()` is not allowed
*   **Correct Answer:** C) `11`
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The first `.then` transforms `5` to `10`; `5` is the starting value, not the final result.
    *   *Why B is incorrect:* `10` is the intermediate result after the first `.then`; the second `.then` adds 1 to produce `11`.
    *   *Why C is correct:* `Promise.resolve(5)` resolves with `5`; the first `.then` doubles it to `10`; the second `.then` adds 1 for a final resolved value of `11`.
    *   *Why D is incorrect:* Returning a plain value from a `.then()` callback resolves the next Promise in the chain with that value; no error occurs.

---

**Question 4**
While working on **Promises & Async/Await**, a developer writes:
```javascript
async function getData() {
  const response = await fetch("https://api.example.com/data");
  const json = await response.json();
  return json;
}
```
If the network request fails (e.g., server unreachable), what happens?
*   A) `fetch()` returns `null`, which is passed to `response.json()`, causing no error.
*   B) The `await fetch(...)` expression throws an error, and without a `try/catch`, the returned Promise is rejected.
*   C) The function automatically retries the request three times before rejecting.
*   D) JavaScript suppresses network errors in `async` functions to prevent crashes.
*   **Correct Answer:** B) The `await fetch(...)` expression throws an error, and without a `try/catch`, the returned Promise is rejected.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A network failure rejects the Promise returned by `fetch()`; `await` re-throws the rejection as an error, not `null`.
    *   *Why B is correct:* When `await` is applied to a rejected Promise, it throws the rejection reason as an exception; without `try/catch`, the `async` function's returned Promise is rejected with that error.
    *   *Why C is incorrect:* JavaScript has no built-in retry mechanism; retrying must be implemented explicitly.
    *   *Why D is incorrect:* JavaScript does not suppress errors; unhandled rejections in `async` functions propagate as rejected Promises.

---

**Question 5**
Which of the following correctly handles both a resolved and rejected Promise using async/await?
*   A) `async function go() { const data = await fetch(url).catch(handleError); }`
*   B) `async function go() { try { const r = await fetch(url); return await r.json(); } catch (err) { console.error(err); } }`
*   C) `async function go() { const data = await fetch(url); } go().catch(console.error);`
*   D) Both B and C are valid approaches
*   **Correct Answer:** D) Both B and C are valid approaches.
*   **Distractor Analysis:**
    *   *Why A alone is not fully correct:* Chaining `.catch()` on `fetch()` before `await` catches only the fetch error but not errors from `r.json()` or later steps; it is partial error handling.
    *   *Why B is correct:* `try/catch` inside the `async` function is the standard pattern; it catches errors from both `await fetch()` and `await r.json()`.
    *   *Why C is correct:* Catching on the returned Promise at the call site (`go().catch(...)`) is equally valid; unhandled rejections inside `getData()` propagate to the call site's `.catch()`.
    *   *Why D is correct:* Both B and C are recognized, valid patterns for handling async errors. The choice depends on whether you want to handle errors inside or outside the async function.
