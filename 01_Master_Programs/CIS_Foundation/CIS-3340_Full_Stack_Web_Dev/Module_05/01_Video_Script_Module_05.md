# Video Script: Module 05 - Asynchronous JavaScript

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 23 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code and Chrome DevTools Network tab
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for Chrome
- Show the DevTools Network tab waterfall during fetch demonstrations
- Keep the Console panel open to show async execution order in real time

---

## Section 1: Introduction - Why Asynchronous Matters [00:00 - 04:00]

Welcome to Module 05. I am Professor Nash. Today we cover one of the most important concepts in JavaScript — asynchronous programming.

JavaScript is single-threaded. It has one call stack and processes one instruction at a time. This creates an obvious problem: what happens when we need to fetch data from a server? If JavaScript stopped and waited for the network response before doing anything else, the entire browser UI would freeze. Buttons would not work. Animations would pause. Pages would appear broken.

Asynchronous programming solves this. We initiate an operation — a network request, a timer, a file read — and provide a callback that executes when the operation completes. JavaScript keeps processing other instructions in the meantime.

This module covers the three generations of asynchronous JavaScript: callbacks (the original pattern), Promises (introduced in ES2015), and async/await (ES2017 syntax sugar over Promises). We will also cover the Fetch API, which is what you will use to communicate with AWS API Gateway endpoints from every front-end application in this course.

**AWS Exam Tip:** DVA-C02 scenarios frequently describe Lambda functions being triggered by events — S3 uploads, SQS messages, API Gateway requests. Each of these is an asynchronous operation from the perspective of the caller. Understanding async patterns helps you reason about retry logic, timeout handling, and CORS issues that appear in exam scenarios.

[SHOW BROWSER]

Let me demonstrate the execution order problem in the browser console.

---

## Section 2: The Event Loop and Call Stack [04:00 - 08:30]

[SHOW BROWSER]

Open Chrome DevTools Console. Type these three lines and observe the output order:

```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
console.log('C');
```

Output: A, C, B — not A, B, C. Even with a 0ms timeout, `setTimeout` is asynchronous. The callback is placed in the callback queue and only moves to the call stack after the synchronous code completes.

[SHOW CODE]

The JavaScript runtime has three components:

- Call stack: where synchronous code executes. LIFO — last in, first out.
- Web APIs: where async operations are handled (timers, network, DOM events) by the browser.
- Callback queue (task queue): where completed async callbacks wait to be executed.
- Microtask queue: where Promise callbacks wait — higher priority than the callback queue.

The event loop continuously checks: is the call stack empty? If yes, move the next task from the microtask queue (Promises) or callback queue (setTimeout) to the stack.

```javascript
console.log('1 — synchronous');

setTimeout(() => console.log('4 — setTimeout callback'), 0);

Promise.resolve().then(() => console.log('3 — Promise microtask'));

console.log('2 — synchronous');

// Output order: 1, 2, 3, 4
// Promise .then callbacks (microtasks) run before setTimeout callbacks (macrotasks)
```

---

## Section 3: Promises [08:30 - 14:00]

[SHOW CODE]

A Promise is an object that represents the eventual completion or failure of an asynchronous operation.

A Promise has three states:

- Pending — the operation has not completed yet
- Fulfilled — the operation succeeded, providing a value
- Rejected — the operation failed, providing a reason

```javascript
// Creating a Promise manually
const myPromise = new Promise(function(resolve, reject) {
  const success = true;
  if (success) {
    resolve('Operation succeeded!');  // transitions to Fulfilled
  } else {
    reject(new Error('Operation failed!')); // transitions to Rejected
  }
});

// Consuming a Promise with .then/.catch/.finally
myPromise
  .then(value => {
    console.log('Fulfilled:', value);  // 'Operation succeeded!'
    return value.toUpperCase();         // return passes to next .then
  })
  .then(upper => console.log('Chained:', upper))
  .catch(error => {
    console.error('Rejected:', error.message);
  })
  .finally(() => {
    console.log('Always runs — cleanup here');
  });
```

Promise.all — wait for multiple Promises simultaneously:

```javascript
const p1 = fetch('/api/programs');
const p2 = fetch('/api/faculty');
const p3 = fetch('/api/events');

Promise.all([p1, p2, p3])
  .then(([programsRes, facultyRes, eventsRes]) => {
    // all three fulfilled
    return Promise.all([programsRes.json(), facultyRes.json(), eventsRes.json()]);
  })
  .then(([programs, faculty, events]) => {
    renderPage(programs, faculty, events);
  })
  .catch(error => {
    // any ONE rejection triggers this
    console.error('One request failed:', error);
  });
```

**AWS Exam Tip:** AWS Lambda with Node.js runtime must return a Promise (or use async/await) for asynchronous handlers. If a Lambda handler initiates async work without returning the Promise, Lambda may time out or return before the work completes — a common exam scenario for Lambda timeout troubleshooting.

---

## Section 4: Async/Await and the Fetch API [14:00 - 19:30]

[SHOW CODE]

`async/await` is syntactic sugar over Promises. An `async` function always returns a Promise. `await` pauses execution inside the async function until the awaited Promise settles.

```javascript
// Promise chain — valid but harder to read
function fetchPrograms() {
  return fetch('/api/programs')
    .then(response => {
      if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
      return response.json();
    })
    .then(data => data)
    .catch(error => console.error('Fetch failed:', error));
}

// Async/await — same operation, easier to read
async function fetchPrograms() {
  try {
    const response = await fetch('/api/programs');
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch failed:', error);
  }
}
```

The Fetch API — making HTTP requests from the browser:

```javascript
// GET request
async function getPrograms() {
  const response = await fetch('https://api.example.com/programs');
  const programs = await response.json();
  return programs;
}

// POST request with JSON body
async function createEnrollment(programId, studentData) {
  const response = await fetch('https://api.example.com/enrollments', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    },
    body: JSON.stringify({ programId, ...studentData })
  });

  if (!response.ok) {
    throw new Error(`Enrollment failed: ${response.status}`);
  }

  return await response.json();
}

// DELETE request
async function deleteRecord(id) {
  const response = await fetch(`https://api.example.com/records/${id}`, {
    method: 'DELETE'
  });
  // 204 No Content — no body to parse
  if (!response.ok) throw new Error(`Delete failed: ${response.status}`);
}
```

[SHOW BROWSER]

Let me use the DevTools Network tab to show the fetch in action. Watch the request go out, the response come back, and the DOM update with the fetched data — all without a page reload.

---

## Section 5: Error Handling and Lab Preview [19:30 - 23:00]

[SHOW CODE]

Robust async error handling:

```javascript
async function loadPageData() {
  const loadingEl = document.querySelector('#loading');
  const errorEl   = document.querySelector('#error-msg');
  const contentEl = document.querySelector('#content');

  loadingEl.hidden = false;
  errorEl.hidden   = true;

  try {
    const [programs, events] = await Promise.all([
      fetchJSON('/api/programs'),
      fetchJSON('/api/events')
    ]);

    renderPrograms(programs);
    renderEvents(events);
    contentEl.hidden = false;

  } catch (error) {
    errorEl.textContent = `Failed to load content: ${error.message}`;
    errorEl.hidden      = false;
    console.error('loadPageData error:', error);

  } finally {
    loadingEl.hidden = true;
  }
}

async function fetchJSON(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
  return response.json();
}
```

In the lab this week you will call the public JSONPlaceholder API (`jsonplaceholder.typicode.com`), display the fetched posts in a card list, implement a loading state, handle errors gracefully, and add a retry button.

Thank you for watching. See you in Module 06 where we design the REST APIs that these fetch calls will consume.

---

## Additional Resources

- developer.mozilla.org — search "Using Fetch" and "async function" for complete API documentation
- aws.amazon.com/certification — review API Gateway and Lambda invocation model for async operation context
