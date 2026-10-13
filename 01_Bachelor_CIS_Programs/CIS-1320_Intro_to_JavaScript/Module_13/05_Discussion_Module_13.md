# Discussion Forum: Module 13 — Asynchronous JavaScript

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Background

Module 13 introduced asynchronous JavaScript: the event loop, `setTimeout`/`setInterval`, Promises, and `async/await`. These tools solve a fundamental problem — how to perform operations that take time (network requests, timers, file reads) without blocking the user interface. The module covered three layers of abstraction: the raw callback approach (`setTimeout`), the Promise object, and the `async/await` syntax that sits on top of Promises. This discussion asks you to reason about the tradeoffs between these approaches, the common mistakes they introduce, and the real-world patterns they enable.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — The Event Loop and Why Async Doesn't Mean Parallel

JavaScript is single-threaded, yet web pages respond to user input while waiting for a server response. The event loop is the mechanism that enables this — it processes callbacks from the event queue only when the call stack is empty. This means `setTimeout(..., 0)` does not run immediately; it runs after all current synchronous code finishes.

In 175–225 words, respond to the following:

- From the Module 13 lab (Part 1, Section 1.1), you confirmed that `setTimeout(..., 0)` logs after synchronous code. In your own words, explain exactly why — trace the execution step by step using the call stack, Web API, and event queue model from the reading guide.
- The reading guide states that `await` pauses the `async` function, not the entire JavaScript engine. Describe what this means in practical terms: if an `async` function is waiting on a slow network request, what is the rest of the page able to do in the meantime? Give a concrete example of something that would continue working.
- Some students expect `async/await` to make JavaScript multi-threaded — that two `async` functions would truly run simultaneously. Explain why this expectation is incorrect, and describe a specific case where `Promise.all` produces the performance improvement that students might incorrectly attribute to multi-threading.

Reference the lab or reading guide in your response.

---

### Scenario B — Promises: States, Chaining, and Error Handling

A Promise has exactly three states and can only transition in one direction. The `.then/.catch/.finally` chain is designed to handle the outcome of asynchronous operations cleanly — each `.then` receives the value from the previous one, and one `.catch` at the end handles any rejection in the chain. The reading guide notes that `fetch` does not reject on HTTP errors, which is a common source of bugs.

In 175–225 words, respond to the following:

- From the Module 13 lab (Part 2, Section 2.1), you created a Promise that could either fulfill or reject based on the input. Describe the two execution paths: what happens inside the Promise constructor for each, what does the calling code receive, and which `.then` or `.catch` block executes?
- The reading guide identifies a critical `fetch` behavior: a 404 or 500 HTTP response **resolves** the Promise rather than rejecting it. Describe a specific bug this could cause in a real application — one where an error response is silently treated as success — and explain how the `response.ok` check prevents it.
- The reading guide includes a table comparing `Promise.all`, `Promise.allSettled`, `Promise.race`, and `Promise.any`. Describe a real-world scenario where `Promise.allSettled` would be more appropriate than `Promise.all`, and explain what specific behavior of `Promise.all` makes it the wrong choice for that scenario.

Reference the lab or reading guide in your response.

---

### Scenario C — `async/await` vs Promise Chains: Readability and Tradeoffs

`async/await` is syntactic sugar — it compiles down to Promises. Everything you can write with `async/await` can be written with `.then/.catch` chains, and vice versa. The choice is primarily about readability and error-handling ergonomics. The reading guide presents both forms side by side so students can see the equivalence.

In 175–225 words, respond to the following:

- From the Module 13 lab (Part 3), you wrote both sequential `async/await` and `Promise.all` inside an `async` function. Describe specifically why the sequential `await` approach (Section 3.1) would be the wrong choice for Part 3, Section 3.4's three independent operations — even though both approaches are syntactically valid. What would the performance difference be?
- The reading guide's side-by-side comparison shows a `.then` chain and its equivalent `async/await` version. Describe a scenario where the `.then` chain form is actually clearer — for example, when there is only one async step, or when the operation is naturally a transformation pipeline.
- `async/await` error handling uses `try/catch`, which is familiar from synchronous code. But `try/catch` inside `async` functions has one behavior that surprises many students: forgetting to `await` a Promise inside the `try` block means `catch` will not catch its rejection. Describe why this happens, using what you know about when `try/catch` executes relative to when the Promise rejects.

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 13 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a concrete example they missed, challenge a position with a specific counter-case, describe a real production scenario that illustrates the concept, or ask a follow-up question that requires a technical answer

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | Scenario answered fully with specific examples. Reference to lab or reading guide. 175–225 words. Complete sentences. |
| 3–4 pts | Mostly addressed but vague or generic. Close to word count. |
| 1–2 pts | Significant parts missing or well below word count. |
| 0 pts | Not submitted. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 pts | Two responses to classmates with different scenarios. Each 60+ words and adds genuine value. |
| 2 pts | One peer response only, or responses lack substance. |
| 0 pts | No peer responses. |

---

## A Note from Professor Nash

Asynchronous JavaScript is the point where the language starts to feel genuinely different from what students often expect coming from other languages. The `response.ok` trap is one I see catch even experienced developers — not because they do not know it, but because they forget to check it when writing quickly. The event loop mental model, once it clicks, explains almost every "why did this run in the wrong order?" bug you will ever encounter. These concepts — Promises, `async/await`, the event loop — show up in every modern JavaScript project, every Node backend, and every front-end framework. Time spent here compounds. I look forward to your posts.
