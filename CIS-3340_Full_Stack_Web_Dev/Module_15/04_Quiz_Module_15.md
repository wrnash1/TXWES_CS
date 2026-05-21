# Quiz: Module 15 - Web Sockets
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
What is the primary benefit of WebSockets over standard HTTP polling for real-time applications?
*   A) WebSockets automatically encrypt all data with TLS — HTTP polling sends data in plaintext.
*   B) WebSockets establish a persistent, full-duplex TCP connection — allowing the server to push data to the client at any time without the client initiating each exchange, eliminating per-message HTTP header overhead.
*   C) WebSockets bypass the browser's Same-Origin Policy — enabling cross-origin communication without CORS headers.
*   D) WebSockets execute 10x faster than HTTP because they bypass the JavaScript engine's event loop.
*   **Correct Answer:** B) WebSockets establish a persistent, full-duplex TCP connection — allowing the server to push data to clients without repeated HTTP request/response cycles, eliminating the latency and overhead of polling.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* WebSockets do not automatically encrypt data — WSS (WebSocket Secure) uses TLS, but plain WS does not. The same is true for HTTP vs. HTTPS.
    *   *Why B is correct:* The key advantage of WebSockets is server-initiated push over a persistent connection — HTTP polling requires the client to make repeated requests to check for new data.
    *   *Why C is incorrect:* WebSockets are still subject to the Same-Origin Policy — cross-origin WebSocket connections require the server to accept requests from non-matching origins.
    *   *Why D is incorrect:* WebSockets do not bypass the JavaScript event loop — they use the same asynchronous event-driven model as HTTP requests.

---

**Question 2**
Which of the following is the most accurate definition of **polling fallbacks** in the context of Socket.io?
*   A) The Socket.io feature that automatically retries a failed WebSocket connection up to five times before throwing an error.
*   B) Degraded transport mechanisms (HTTP long-polling or short-polling) that Socket.io uses when a WebSocket connection cannot be established — such as in corporate proxy environments that block WebSocket upgrades.
*   C) The browser's native `EventSource` API that provides one-way server-sent events as a fallback when the WebSocket handshake fails.
*   D) The AWS API Gateway feature that falls back to REST API routing when a WebSocket `$connect` route Lambda function times out.
*   **Correct Answer:** B) Degraded transport mechanisms (HTTP long-polling or short-polling) that Socket.io uses when a WebSocket connection cannot be established — such as in corporate proxy environments that block WebSocket upgrades.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Socket.io's reconnection logic — not polling fallbacks. Polling fallbacks are an alternative transport, not a retry mechanism.
    *   *Why B is correct:* Socket.io transparently negotiates the best available transport — starting with WebSockets and falling back to HTTP polling if the environment does not support WebSocket upgrades.
    *   *Why C is incorrect:* Server-Sent Events (SSE) via `EventSource` is a browser API for one-way push from server to client — it is a different technology from Socket.io's polling fallback mechanism.
    *   *Why D is incorrect:* AWS API Gateway WebSocket APIs do not fall back to REST routing on Lambda timeout — this is a made-up behavior.

---

**Question 3**
In Socket.io, what is the difference between `socket.emit()` and `io.emit()`?
*   A) `socket.emit()` sends events to all connected clients; `io.emit()` sends events only to the client represented by the `socket` object.
*   B) `socket.emit()` sends an event to the single client represented by that socket connection; `io.emit()` broadcasts the event to all currently connected clients.
*   C) `socket.emit()` emits events synchronously; `io.emit()` emits events asynchronously via a Promise.
*   D) `socket.emit()` is used on the server side; `io.emit()` is used on the browser client side.
*   **Correct Answer:** B) `socket.emit()` sends an event only to the specific client represented by that socket connection; `io.emit()` broadcasts the event to all currently connected clients.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the correct behavior — `io.emit()` broadcasts to all, `socket.emit()` targets one.
    *   *Why B is correct:* In Socket.io server-side code, `socket` refers to a single client connection — `socket.emit()` targets that client. `io` is the server instance — `io.emit()` broadcasts to every connected socket.
    *   *Why C is incorrect:* Both methods are event-driven and non-blocking — neither is synchronous in the traditional sense.
    *   *Why D is incorrect:* Both `socket.emit()` and `io.emit()` are server-side Socket.io methods. On the browser client side, the client socket also has its own `socket.emit()` for sending events to the server.

---

**Question 4**
On AWS, which service provides a managed WebSocket API that routes connections and messages to AWS Lambda functions without managing a WebSocket server?
*   A) Amazon EC2 with a Node.js Socket.io server running on port 443.
*   B) AWS API Gateway WebSocket API
*   C) Amazon SQS with long-polling enabled
*   D) AWS Elastic Load Balancer with sticky sessions
*   **Correct Answer:** B) AWS API Gateway WebSocket API provides a managed WebSocket endpoint — it routes `$connect`, `$disconnect`, and custom message routes to individual Lambda functions without any server management.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running Socket.io on EC2 is a valid option but requires server management — it is not a managed serverless WebSocket service.
    *   *Why B is correct:* API Gateway WebSocket APIs are the AWS-native managed solution for WebSocket connections backed by Lambda — a key DVA-C02 exam topic.
    *   *Why C is incorrect:* Amazon SQS with long-polling retrieves messages from a queue — it is a message queue service, not a real-time browser WebSocket service.
    *   *Why D is incorrect:* Elastic Load Balancers with sticky sessions route HTTP requests to consistent backend instances — they do not provide WebSocket API management with Lambda integration.

---

**Question 5**
A real-time collaborative whiteboard app uses Socket.io. When one user draws a shape, all other users in the same "room" should see it, but users in different rooms should not. Which Socket.io feature enables this targeted broadcasting?
*   A) `io.emit()` with a filter callback that checks each socket's session data before delivering the event.
*   B) Socket.io rooms — the server places each user's socket into a named room with `socket.join(roomId)` and broadcasts to room members only with `io.to(roomId).emit('draw', shape)`.
*   C) Socket.io namespaces — each whiteboard session connects to a separate namespace URL and broadcasts are scoped to the namespace.
*   D) WebSocket subprotocols — the server negotiates a unique subprotocol string per room during the handshake, and messages are automatically delivered only to sockets sharing the same subprotocol.
*   **Correct Answer:** B) Socket.io rooms — the server places each user's socket into a named room with `socket.join(roomId)` and broadcasts to that room with `io.to(roomId).emit('draw', shape)`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `io.emit()` broadcasts to all connected clients — there is no filter callback in the standard API. Implementing per-socket filtering manually is inefficient and error-prone.
    *   *Why B is correct:* Socket.io rooms are a lightweight grouping mechanism specifically designed for this use case — placing sockets in rooms and targeting `io.to(roomId).emit()` is the canonical pattern.
    *   *Why C is incorrect:* Namespaces are higher-level divisions of a Socket.io server (like separate endpoints) — they are appropriate for separating different application features, not individual whiteboard sessions with many room IDs.
    *   *Why D is incorrect:* WebSocket subprotocols are negotiated during the HTTP upgrade handshake for protocol identification — they do not provide room-based message routing.
