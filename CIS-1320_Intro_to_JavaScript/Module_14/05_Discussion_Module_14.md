# Discussion Forum: Module 14 — Promises and Async/Await: Patterns in Practice

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Background

Module 14 deepened the async patterns introduced in Module 13. The core themes were performance (sequential vs parallel execution), robustness (`Promise.allSettled` for partial results, `AbortController` for cancellation, structured error handling), and data handling (JSON serialization and `localStorage`). These patterns are not advanced features reserved for complex applications — they are the baseline of competent async code. This discussion asks you to reason about the design choices involved: when to choose one combinator over another, what silent failures look like and why they happen, and how async patterns shape user experience.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Sequential vs Parallel: When Each is Correct

The reading guide presents a clear rule: use `Promise.all` for independent operations; use sequential `await` for dependent ones. The performance difference can be dramatic — three 200ms requests take 600ms sequentially but 200ms in parallel. Yet many developers default to sequential `await` for all async code because it reads naturally, and never notice the performance cost.

In 175–225 words, respond to the following:

- From the Module 14 lab (Part 1, Sections 1.2–1.3), you measured the elapsed time for sequential and parallel execution of three independent delays. Describe what you observed — what were the approximate times, and what does that difference represent in a real web application with multiple API calls?
- The reading guide includes an example where sequential `await` is the correct choice: loading a token, then using it to load a user profile, then using that to load settings. Explain precisely why `Promise.all` would be wrong for that workflow, even though the three requests are all asynchronous.
- Describe a realistic dashboard page that loads several independent data sources. Name the sources (e.g., user profile, recent orders, notifications), explain why they are independent, and describe what the user experience difference would be between sequential and parallel loading.

Reference the lab or reading guide in your response.

---

### Scenario B — `Promise.allSettled` and Graceful Degradation

`Promise.all` is fail-fast: one rejection aborts everything. `Promise.allSettled` waits for all outcomes and hands you every result to inspect individually. The choice between them reflects a design decision about how your application handles partial failure — should one failed component abort the whole page, or should the rest of the page display despite the failure?

In 175–225 words, respond to the following:

- From the Module 14 lab (Part 2, Sections 2.1–2.2), you observed both combinators on the same set of mixed-outcome Promises. Describe the precise difference in behavior you observed — what did `Promise.all` do versus `Promise.allSettled` when `p2` rejected?
- The reading guide's `initDashboard` example uses `Promise.all` for critical data and `Promise.allSettled` for non-critical data. Describe the design reasoning behind this split: why would you want critical data to fail the whole operation, but non-critical data to degrade gracefully?
- Describe a specific web application feature where using `Promise.all` instead of `Promise.allSettled` would cause a poor user experience — a case where a minor, unrelated failure would unnecessarily block the user from seeing important content. What would the user see, and why is it the wrong behavior?

Reference the lab or reading guide in your response.

---

### Scenario C — JSON Serialization: What Gets Preserved and What Gets Lost

`JSON.stringify` and `JSON.parse` are simple in appearance but have specific rules about what JavaScript values they can represent. Functions are silently dropped, `Date` objects become strings, `Infinity` becomes `null`. These are not bugs — they are defined behavior. But they become bugs when a developer does not expect them.

In 175–225 words, respond to the following:

- From the Module 14 lab (Part 3, Section 3.2), you observed what `JSON.stringify` does with functions, `undefined`, `Date` objects, and `Infinity`. Describe two specific cases from that section — not just what the output was, but why the JSON specification cannot represent these JavaScript values.
- The lab used a simulated `localStorage` pattern: serialize with `JSON.stringify` before storing, deserialize with `JSON.parse` after reading. Describe a specific bug a developer could introduce by storing a `Date` object, retrieving it later, and treating the retrieved value as a `Date` without checking its type. What operation would fail, and why?
- `AbortController` is a tool for managing fetch cancellation. Describe a specific user-facing scenario — something a real user would do — where failing to cancel in-flight requests would produce incorrect or confusing behavior in the UI. Then describe how `AbortController` solves the problem.

Reference the lab or reading guide in your response.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 14 lab or reading guide at least once

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

The patterns in this module — parallel loading, graceful degradation, request cancellation, JSON persistence — are not special cases. They are how professional async JavaScript is written every day. The search page in the lab with debounce and `AbortController` is a stripped-down version of the search bar on every major web application you use. The `Promise.allSettled` pattern is how dashboards stay usable even when one of six API calls fails. These things feel advanced when you are learning them, but they quickly become automatic. I look forward to your posts.
