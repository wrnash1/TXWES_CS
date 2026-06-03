# Discussion Forum: Module 15 — WebSockets and Real-Time Communication

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects WebSocket architecture decisions to real engineering trade-offs: protocol selection, scalability, security, and AWS service choices. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: Debugging a Socket.io Memory Leak

A developer builds a real-time dashboard. The React component that displays live data is:

```jsx
function LiveDashboard({ projectId }) {
  const [updates, setUpdates] = useState([]);

  useEffect(() => {
    const socket = io('http://localhost:3000');
    socket.emit('join_project', projectId);
    socket.on('project_update', (data) => {
      setUpdates((prev) => [...prev, data]);
    });
  }, [projectId]);

  return <ul>{updates.map((u, i) => <li key={i}>{u.message}</li>)}</ul>;
}
```

After a user navigates between projects (changing `projectId`) several times, they report two problems: the update list contains duplicates from previous projects, and the browser's memory usage climbs steadily.

Address all three of the following in your post:

1. Identify every bug in the `useEffect`. There are at least three. For each bug, explain exactly what happens at runtime because of it.
2. Rewrite the `useEffect` correctly. Your rewrite must fix all identified bugs and handle the case where `projectId` changes (the user navigates to a different project).
3. The developer proposes moving the `io()` call outside the component to a module-level variable (`const socket = io('...')`). Explain what problem this solves, what new problem it introduces if `autoConnect: false` is not set, and why `autoConnect: false` is the correct companion configuration.

Your initial post should be 175 to 225 words.

---

## Scenario B: Architecture Decision — Socket.io vs API Gateway WebSocket

A startup is building a project management tool. The product manager requests two real-time features:

- **Feature 1:** A notification badge that updates when a teammate assigns you a task. Expected frequency: 1–5 events per user per hour.
- **Feature 2:** A live cursor-sharing panel that shows where each team member's cursor is in a shared document. Expected frequency: up to 20 position updates per user per second while editing.

The engineering team is debating two architectures:

- **Option A:** Socket.io on an Elastic Beanstalk Node.js server
- **Option B:** AWS API Gateway WebSocket API + Lambda + DynamoDB

Address all three of the following in your post:

1. For Feature 1 (task assignment notifications), evaluate both architectures. Explain the specific DynamoDB operations that API Gateway + Lambda requires for each notification delivery, and whether that overhead is acceptable at the expected event frequency.
2. For Feature 2 (live cursor sharing), explain why the API Gateway + Lambda architecture creates a problem at 20 updates per second per user with 10 simultaneous editors. Calculate the approximate number of Lambda invocations per minute this generates, and what that means for cost and latency.
3. Propose a hybrid architecture: which feature belongs on which infrastructure, and why. Explain how the two systems would coexist in the same application from the client's perspective.

Your initial post should be 175 to 225 words.

---

## Scenario C: Securing WebSocket Connections

A team's real-time notification system has this authentication flow: users log in via `POST /api/auth/login`, receive a JWT stored in `localStorage`, and then connect to Socket.io. The current Socket.io server code has no authentication middleware — the `io.on('connection', ...)` handler processes all connections without checking identity. The team's security engineer flags two vulnerabilities.

Address all three of the following in your post:

1. Identify the two security vulnerabilities. The first is about what an unauthenticated client can do once connected. The second is about user-to-user data isolation — explain what happens if the server emits user-specific notifications to a room named `user:${userId}` but any client can join any room by emitting `join_room` with an arbitrary `userId`.
2. Describe the complete fix for both vulnerabilities: the `io.use()` middleware implementation that authenticates the connection before it is established, and the server-side room join logic that prevents a client from joining another user's room.
3. The security engineer also notes that storing the JWT in `localStorage` exposes it to XSS attacks. Describe the alternative storage approach using `httpOnly` cookies, explain why it is safer against XSS, and identify the trade-off it introduces for WebSocket authentication (since cookies are not sent in the WebSocket handshake by default).

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context or an architectural principle that strengthens the answer, or
- Present an alternative approach with trade-off analysis

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
| Initial post uses correct WebSocket and AWS terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

For Scenario A, posts that identify only one or two bugs will receive partial credit. The three bugs are distinct: creating a new `io()` connection inside `useEffect`, missing `socket.off()`, and missing `socket.disconnect()`. Each has a different consequence — duplicate connections, listener accumulation, and persistent connections after navigation. A strong post explains all three and shows the corrected code.

For Scenario B, I want to see actual numbers. "Lambda invocations per minute" is calculable — show the math. 20 updates per user per second, 10 users, 60 seconds = 12,000 Lambda invocations per minute, each requiring a DynamoDB scan and N `PostToConnectionCommand` calls. That number changes the architecture conversation from preference to engineering necessity.

For Scenario C, the JWT-in-cookie vs JWT-in-localStorage debate is not settled — both approaches have trade-offs. The strongest posts acknowledge that `httpOnly` cookies solve XSS but require `withCredentials: true` on the Socket.io client and `credentials: true` in the CORS config, and that the JWT still needs to be extracted from the cookie by the `io.use()` middleware via `socket.handshake.headers.cookie`. Understanding that nuance separates engineers who have actually deployed secure WebSocket applications from those who have only read about it.
