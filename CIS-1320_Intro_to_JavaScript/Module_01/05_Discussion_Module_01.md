# Discussion Forum: Module 01 — JavaScript Introduction and Execution

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Background

You have now written your first JavaScript programs, connected them to HTML pages, and watched them execute in the browser. You have also experienced the script-placement problem first-hand — a `null` returned from `getElementById` when a script in `<head>` runs before the DOM exists — and fixed it with `defer`.

This discussion asks you to move beyond reproducing the lab steps and engage with the concepts behind what you did.

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Script Placement: The Real Consequence

You now know the rule: an undeferred `<script>` in `<head>` causes `getElementById` to return `null`. But why does that matter in a real website? `null` is just a value — what actually breaks?

In 175–225 words, respond to the following:

- Describe what happens in a browser when JavaScript code tries to call a method on `null`. For example, what does `null.textContent = 'Hello'` do — and why? Be specific about what error message appears and in what form the user sees it.
- Explain why this type of error is more dangerous in a production website than a development exercise. Consider who sees it, what it might break downstream, and whether the rest of the script continues executing.
- The reading guide presents two solutions: move the script to the bottom of `<body>`, or use `defer` in `<head>`. Identify one concrete reason why a developer might prefer `defer` over moving the tag, even though both fix the null problem.

Reference the lab activity in your response — describe what you observed in Part 4 when you introduced and then removed the null error.

---

### Scenario B — Three Methods, One Decision

The reading guide describes three ways to include JavaScript in a web page: inline event attributes, internal script blocks, and external `.js` files. Knowing all three methods is useful, but every day developers must choose which one to use for a given situation.

In 175–225 words, respond to the following:

- Describe a real-world scenario where an internal script block would be a reasonable choice. What characteristics of the project make it acceptable rather than just convenient? Give a concrete example — not just "a small project."
- Describe a real-world scenario where an external `.js` file is clearly the right choice. What specific advantage of external files makes it the correct decision in your example?
- The reading guide says inline JavaScript in event attributes is "poor practice." Some developers argue this is too absolute — that small `onclick` snippets on single-purpose buttons are harmless. Make an argument for or against this position based on the separation-of-concerns principle. You do not have to agree with the reading guide's position, but your argument must be specific.

---

### Scenario C — The Console as a Learning Tool

The browser DevTools Console is one of the most powerful tools available to a JavaScript developer. In this module you used it both as an output channel for `console.log()` and as an interactive REPL where you typed and evaluated expressions directly.

In 175–225 words, respond to the following:

- Describe two specific things you discovered — or confirmed — by typing expressions directly in the console during the lab. Do not just list the expressions; explain what you learned or were surprised by. For example, if you noticed something unexpected about how `+` behaves between different types, explain it.
- Explain the difference between `console.error()` and `console.log()` beyond the visual styling (the red color). What is the practical reason a developer would choose one over the other in their own code? Give a concrete example.
- Describe how you plan to use the console as a learning tool going forward in this course. What kinds of questions can you now answer just by typing in the console, without writing a full HTML page?

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top of your post
- Write in complete sentences — not bullet points
- Reference the Module 01 lab or reading guide at least once

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: share a related observation from your own lab, ask a specific follow-up question about their scenario, offer a counterargument to a position they took, or describe something from the reading guide that connects to their point

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | Scenario answered fully with specificity. At least one reference to the lab or reading guide. 175–225 words. Complete sentences. |
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

Module 01 is deceptively important. The concepts you practiced here — how JavaScript gets into a page, when it runs, and how to observe it — are the foundation for everything that follows. Students who skip the details in Module 01 often struggle in Module 10 when DOM manipulation becomes complex and script placement errors become invisible because they have been normalized.

Do not skip the discussion. The act of explaining what you observed to classmates — and reading how they interpreted the same concepts differently — is one of the highest-value activities in this course. I look forward to reading your posts.
