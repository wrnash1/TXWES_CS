# Discussion Forum: Module 15 — Error Handling & Debugging

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Background

Module 15 covers two foundational professional skills: writing code that handles errors deliberately, and using tools to diagnose problems in running code. The module introduced JavaScript's six built-in error types, the `try/catch/finally` construct, the `throw` statement, custom error classes built with `extends Error`, `console` debugging methods (`table`, `group`, `time`, `assert`), and Chrome DevTools breakpoints. These are not advanced topics — they are baseline practices in every production codebase. This discussion asks you to reason about the design decisions behind error handling and debugging: when to catch and recover versus rethrow, how custom errors improve code clarity, and what makes a debugging session efficient versus frustrating.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Catching vs. Rethrowing: When Each Is Correct

A common mistake when learning `try/catch` is catching every error and either ignoring it silently or logging it and continuing, regardless of whether the error is actually understood or recoverable. The reading guide presents a clear rule: catch errors you can specifically handle; rethrow everything else.

In 175–225 words, respond to the following:

- From the Module 15 lab (Part 1, Sections 1.2 and 1.4), you practiced catching specific error types with `instanceof` and rethrowing unexpected ones. Describe the behavior you observed — what happened when the function received a `TypeError` versus a `RangeError`, and what would happen if the `throw err` line were removed?
- The reading guide explains that silently catching every error hides bugs. Give a concrete example of a bug that would be permanently invisible if every error were swallowed in a blanket `catch (err) { }` block. Describe what the user or developer would see (or fail to see), and why.
- Describe a realistic scenario where catching an error and recovering gracefully is the correct choice — where the error is expected, understood, and has a sensible default. Contrast it with a case where the same error type would need to be rethrown because the caller must handle it.

Reference the lab or reading guide in your response.

---

### Scenario B — Custom Error Classes: Design and Value

The built-in error types (`TypeError`, `RangeError`, etc.) describe what went wrong mechanically. Custom error classes let you describe what went wrong in your application's terms. The difference matters when a `catch` block needs to respond differently to a user input problem versus a system failure.

In 175–225 words, respond to the following:

- From the Module 15 lab (Part 2), you implemented `ValidationError`, `NotFoundError`, and `PermissionError` classes. Describe what you had to do to make them work correctly — specifically, why `super(message)` and `this.name` are both required. What does each one do, and what breaks if either is omitted?
- The reading guide's custom error example includes extra properties on the class (`field` on `ValidationError`, `resource` and `id` on `NotFoundError`). Explain how these extra properties improve a `catch` block compared to catching a plain `Error` — what can the catch block do with them that it could not do otherwise?
- Describe a web application feature — something with user interaction — where you would define at least two custom error classes to distinguish different failure modes. Name the classes, describe what each represents, and explain how the `catch` block would respond differently to each.

Reference the lab or reading guide in your response.

---

### Scenario C — Debugging Strategy: Tools and Approach

A developer who only uses `console.log` for debugging can eventually find most bugs, but it is inefficient. The Sources panel in DevTools, breakpoints, and `console` methods like `table`, `group`, and `time` reduce the time from "something is wrong" to "I found it and fixed it." The choice of tool shapes how quickly a bug can be isolated.

In 175–225 words, respond to the following:

- From the Module 15 lab (Part 3, Section 3.4), you used a `debugger` statement and then a manual breakpoint to pause execution inside `calculateOrderTotal`. Describe what you were able to see in the Scope panel and Call Stack panel that you could not easily see from `console.log` output alone. What specific information was available?
- The reading guide explains that `debugger` must be removed before deploying to production. Describe precisely what would happen to a user who opens a page with a `debugger` statement left in the code and who also happens to have Chrome DevTools open. Why is this a real problem and not just a theoretical concern?
- Describe a type of bug — a real category of programming mistake — that is difficult to find with `console.log` but easy to find with a breakpoint in the Sources panel. Explain why the breakpoint makes the difference.

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 15 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: add a concrete example they missed, challenge a position with a specific counter-case, describe a real application pattern that illustrates the concept, or ask a follow-up question that requires a technical answer

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

Error handling and debugging are skills that separate developers who can build working software from those who can only build software that works when nothing goes wrong. The `try/catch` construct is not just syntax — it is a design decision about what your code is responsible for handling and what it passes to its caller. Custom errors are not just classes — they are contracts that let different parts of your code communicate precisely about what failed and why. And debugging tools are not a crutch — they are how professionals diagnose the subtle, non-obvious bugs that no amount of `console.log` would easily find. I look forward to your posts.
