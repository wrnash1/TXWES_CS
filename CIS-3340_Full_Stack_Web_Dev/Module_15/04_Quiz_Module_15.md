# Quiz: Module 15 — WebSockets and Real-Time Communication

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

A React component calls `io('http://localhost:3000')` inside the component function body (outside `useEffect`). What is the problem?

- A) `io()` must be called inside a `useEffect` hook or React will throw an error about side effects during rendering.
- B) Every time the component re-renders, `io()` creates a new WebSocket connection. The previous connections are never closed, resulting in duplicate connections accumulating over the lifetime of the component.
- C) Calling `io()` outside `useEffect` causes the connection to use HTTP polling instead of WebSockets because the DOM is not ready.
- D) Socket.io requires the connection to be created after the component mounts — calling it in the function body means the socket is created before the component's props are available.

**Correct Answer:** B

**Explanation:** `io()` immediately opens a WebSocket connection. When called in the component body rather than inside `useEffect`, it runs on every render — including re-renders triggered by state changes, parent re-renders, or React StrictMode's double-invocation. Each call creates a new connection that is never closed, because there is no cleanup function. The correct pattern is to create a singleton socket instance in a separate module (`src/socket.js`) and import it, so only one connection exists regardless of how many times the component renders.

**Distractor Analysis:**

- Why A is incorrect: React does not throw an error for calling `io()` in the component body. The problem is behavioral (duplicate connections), not a React error.
- Why B is correct: Multiple `io()` calls produce multiple connections. Without `socket.disconnect()` in a cleanup function, they accumulate.
- Why C is incorrect: `io()` uses WebSockets by default regardless of where it is called. The polling fallback is for environments where WebSockets are blocked, not for timing of the call.
- Why D is incorrect: `io()` does not require props. The issue is connection multiplicity, not prop availability.

---

## Question 2

A developer adds this `useEffect` to a chat component:

```jsx
useEffect(() => {
  socket.connect();
  socket.on('message', (msg) => {
    setMessages((prev) => [...prev, msg]);
  });
}, []);
```

After using the app for a few minutes, every new message appears three times. What is the most likely cause?

- A) `setMessages` with the functional updater form `prev => [...prev, msg]` appends the message three times when the component has three state variables.
- B) The `useEffect` runs three times because React StrictMode invokes effects twice in development, and the component re-renders once on mount — creating three `message` listeners that are never removed.
- C) Socket.io emits every event three times by default to ensure delivery — the developer must use `socket.once()` instead of `socket.on()`.
- D) The missing `socket.off('message')` in the cleanup function means each time the component re-renders or the effect re-runs, another listener is added. With three registrations, each incoming message triggers three `setMessages` calls.

**Correct Answer:** D

**Explanation:** Without `socket.off('message')` in the `useEffect` cleanup return function, every execution of the effect adds another listener to the `'message'` event. In React StrictMode, effects run twice in development (mount → unmount → remount), leaving two listeners. Additional re-renders add more. Three registrations cause each message to call `setMessages` three times, appending it three times. The fix is `return () => { socket.off('message'); socket.disconnect(); }`.

**Distractor Analysis:**

- Why A is incorrect: The functional updater form is correct. `prev => [...prev, msg]` always appends exactly one item regardless of other state variables.
- Why B is incorrect: React StrictMode does invoke effects twice in development, but the "three times" behavior persists in production too, indicating listener accumulation — not just a StrictMode artifact.
- Why C is incorrect: Socket.io does not retry event delivery by default. `socket.once()` would remove the listener after the first message, which is also wrong behavior for a chat.
- Why D is correct: Missing `socket.off()` in cleanup is the most common Socket.io bug in React. Each effect execution adds a new listener.

---

## Question 3

A Socket.io server has this code:

```js
io.on('connection', (socket) => {
  socket.on('join_room', (roomId) => {
    socket.join(roomId);
  });

  socket.on('send_to_room', ({ roomId, message }) => {
    socket.to(roomId).emit('new_message', message);
  });
});
```

User A and User B are both in room `'project-42'`. User A sends a message. Which clients receive the `'new_message'` event?

- A) All connected clients on the server, including User A.
- B) All clients in room `'project-42'`, including User A.
- C) All clients in room `'project-42'` except User A.
- D) Only User B, because `socket.to()` sends to exactly one other client.

**Correct Answer:** C

**Explanation:** `socket.to(roomId).emit(...)` broadcasts to all clients in the specified room **except the sender**. This is the standard broadcast-to-room pattern. If User A should also receive the message (for example, to confirm their own message appeared), use `io.to(roomId).emit(...)` instead, which includes the sender.

**Distractor Analysis:**

- Why A is incorrect: `socket.to(roomId)` scopes the emission to the room, not the entire server. `io.emit()` would reach all clients.
- Why B is incorrect: `socket.to(roomId)` excludes the sender. Only `io.to(roomId)` includes the sender.
- Why C is correct: `socket.to(room)` = everyone in the room except the socket that called it.
- Why D is incorrect: `socket.to(roomId)` sends to all clients in the room, not just one. `socket.to(socketId)` would send to exactly one client.

---

## Question 4

Where must Socket.io's CORS configuration be set, and why?

- A) In the React component's `fetch` options, using `mode: 'cors'`, because the WebSocket upgrade is a browser-initiated HTTP request.
- B) In the `Server` constructor passed to Socket.io — `new Server(server, { cors: { origin: '...' } })` — because the WebSocket upgrade handshake is an HTTP request that must include `Access-Control-Allow-Origin` in the server's response, and Socket.io handles that header independently of Express's `cors()` middleware.
- C) In Express's `app.use(cors(...))` middleware, because Socket.io routes all traffic through Express before upgrading the connection.
- D) CORS does not apply to WebSocket connections — only HTTP requests are subject to the browser's same-origin policy.

**Correct Answer:** B

**Explanation:** The WebSocket upgrade begins as an HTTP request. The browser enforces CORS on this request — if the server's response does not include `Access-Control-Allow-Origin`, the upgrade is blocked. Socket.io handles this handshake internally and does not route it through Express middleware. Therefore, CORS must be configured in the Socket.io `Server` constructor's `cors` option. Express's `app.use(cors(...))` only covers standard HTTP routes, not the Socket.io upgrade path.

**Distractor Analysis:**

- Why A is incorrect: `fetch` options do not affect WebSocket connections. WebSockets use the `WebSocket` constructor or `io()`, not `fetch`.
- Why B is correct: Socket.io intercepts the HTTP upgrade at the server level, bypassing Express middleware.
- Why C is incorrect: Express middleware does not intercept the WebSocket upgrade path. Testing confirms this — many developers discover the hard way that adding `cors()` to Express is not sufficient for Socket.io.
- Why D is incorrect: CORS does apply to WebSocket upgrades. The browser's same-origin policy checks the `Upgrade` request just like any cross-origin HTTP request.

---

## Question 5

A developer implements Socket.io authentication like this:

```js
io.on('connection', (socket) => {
  const token = socket.handshake.auth.token;
  if (!token) {
    socket.disconnect();
    return;
  }
  const decoded = jwt.verify(token, process.env.JWT_SECRET);
  socket.data.user = decoded;
});
```

What is the problem with this approach compared to using `io.use()` middleware?

- A) `socket.handshake.auth` is not available inside the `connection` handler — it is only accessible in `io.use()` middleware.
- B) The `connection` event fires and the client is considered connected before the token is checked. A brief window exists where the client is connected but not yet authenticated. Additionally, if `jwt.verify` throws, the unhandled exception crashes the server process.
- C) `socket.disconnect()` cannot be called from inside the `connection` handler — it must be called from `io.use()` middleware.
- D) This pattern is functionally identical to using `io.use()` — there is no meaningful difference.

**Correct Answer:** B

**Explanation:** When using `io.on('connection', ...)`, the client is already connected before the token is validated. Any events emitted by the client between connection and the check could be processed. More critically, `jwt.verify` throws on invalid or expired tokens — without a try/catch, this exception propagates up and can crash the Node.js process. The correct approach is `io.use((socket, next) => { ... })`, which runs before `connection` fires. Calling `next(new Error('...'))` rejects the connection before it is established.

**Distractor Analysis:**

- Why A is incorrect: `socket.handshake.auth` is accessible in both `io.use()` middleware and the `connection` handler.
- Why B is correct: Two problems — connected-before-authenticated window, and unhandled `jwt.verify` exception.
- Why C is incorrect: `socket.disconnect()` can be called from inside the `connection` handler.
- Why D is incorrect: The timing difference is meaningful for security. `io.use()` prevents the connection entirely; the `connection` handler validates after connection is established.

---

## Question 6

A team deploys their real-time application to AWS. They use an API Gateway WebSocket API with Lambda functions. After running for a week, the DynamoDB `connections` table has thousands of records for connections that no longer exist. What is the correct mechanism to clean up stale connections?

- A) Set a DynamoDB TTL attribute on each item when it is inserted — expired items are automatically deleted.
- B) Handle the `$disconnect` route to delete the connectionId from DynamoDB when a client disconnects. Additionally, when `PostToConnectionCommand` returns status `410 Gone`, delete that connectionId — `410` means the client dropped without triggering `$disconnect`.
- C) Run a scheduled Lambda that calls the API Gateway management API to list all connections and compare them against DynamoDB records.
- D) Enable DynamoDB Streams on the connections table and trigger a Lambda to validate each record as it is inserted.

**Correct Answer:** B

**Explanation:** There are two sources of stale connectionIds: clean disconnects (where `$disconnect` fires) and network drops (where `$disconnect` does not fire). The `$disconnect` Lambda handles clean disconnects. For network drops, when you attempt to send a message via `PostToConnectionCommand`, API Gateway returns HTTP `410 Gone` if the connection no longer exists. The broadcast Lambda should catch this status code and delete the stale record from DynamoDB. Both mechanisms together keep the table clean.

**Distractor Analysis:**

- Why A is incorrect: DynamoDB TTL is a valid supplementary cleanup mechanism, but it does not handle real-time cleanup at disconnect. TTL deletion can lag by up to 48 hours.
- Why B is correct: `$disconnect` + 410 handling is the complete solution designed into the API Gateway WebSocket architecture.
- Why C is incorrect: API Gateway does not expose a "list all active connections" API. The only source of truth is your DynamoDB table.
- Why D is incorrect: Validating on insert does not help with connections that become stale after insertion.

---

## Question 7

A developer wants to send a real-time notification to a specific user (not broadcast to all clients) using Socket.io rooms. Which server-side pattern correctly sends only to user ID 42?

- A) `socket.emit('notification', data)` — because `socket` always refers to the user with ID 42.
- B) On connect, the server calls `socket.join(`user:42`)`. Later, any route handler calls `io.to('user:42').emit('notification', data)`.
- C) `io.emit('notification', { targetUserId: 42, ...data })` — the client filters messages by `targetUserId`.
- D) `socket.broadcast.emit('notification', data)` — this sends to everyone except the current user, which is the correct pattern for server-initiated notifications.

**Correct Answer:** B

**Explanation:** The standard pattern for user-specific notifications is: on `connection`, the server joins the socket to a room named after the user's ID (e.g., `user:42`). From anywhere in the application — including REST route handlers that emit after a database write — `io.to('user:42').emit(...)` delivers the event to every socket that user has open (multiple tabs, devices). This is how the lab in this module is structured.

**Distractor Analysis:**

- Why A is incorrect: Inside `io.on('connection', socket => {...})`, `socket` refers to the currently connecting client — it changes with every connection. It cannot be referenced later in a route handler.
- Why B is correct: Room-per-user is the standard Socket.io pattern for user-scoped notifications.
- Why C is incorrect: Broadcasting to all clients and filtering client-side exposes all users' notifications to all clients. It is also inefficient for large numbers of connected users.
- Why D is incorrect: `socket.broadcast.emit()` sends to all clients except the current socket — it is used in event handlers triggered by that socket, not for targeted server-initiated notifications.

---

## Question 8

In an AWS API Gateway WebSocket API, a Lambda function for the `$connect` route receives an event with this structure:

```json
{
  "requestContext": {
    "connectionId": "abc123==",
    "routeKey": "$connect",
    "eventType": "CONNECT"
  },
  "queryStringParameters": {
    "token": "eyJhbGciOiJIUzI1NiJ9..."
  }
}
```

The Lambda must validate the JWT and reject unauthenticated connections. What HTTP status code should the Lambda return to reject the connection?

- A) `200` — API Gateway always accepts the connection regardless of the Lambda response.
- B) `401` — This signals to API Gateway that authentication failed and the connection should be refused.
- C) Any non-`2xx` status code (for example `401` or `403`) — API Gateway rejects the connection if `$connect` does not return a `2xx` response.
- D) `500` — The only way to reject a connection is to throw an unhandled exception in the Lambda.

**Correct Answer:** C

**Explanation:** API Gateway establishes the WebSocket connection only if the `$connect` Lambda returns a `2xx` status code. Returning any non-2xx response (401, 403, 400) causes API Gateway to reject the connection and the client receives a close event. The exact code in the `4xx` range is a matter of convention — `401` communicates "not authenticated" and `403` communicates "authenticated but not authorized." What matters is that the response is not `2xx`.

**Distractor Analysis:**

- Why A is incorrect: API Gateway does not ignore the Lambda return value. A non-2xx response from `$connect` rejects the connection.
- Why B is incorrect: `401` works, but the answer is too narrow — any non-2xx code rejects the connection.
- Why C is correct: The specification is non-2xx = rejected. `401` and `403` are both valid choices.
- Why D is incorrect: Throwing an unhandled exception causes a `500` response and the connection is rejected — but this is not the recommended pattern. Explicit status codes are clearer.

---

## Question 9

A developer is building a collaborative document editor. Multiple users can edit the same document simultaneously and see each other's cursor positions update in real time at 10 updates per second per user. The team is choosing between Socket.io on an Elastic Beanstalk server and an API Gateway WebSocket API with Lambda. Which architecture is more appropriate and why?

- A) API Gateway WebSocket + Lambda, because Lambda scales infinitely and can handle any message rate without configuration.
- B) Socket.io on Elastic Beanstalk, because high-frequency in-memory message routing (10 updates/second per user) is more efficient on a persistent server than routing every message through API Gateway → Lambda → DynamoDB → ApiGatewayManagementApi.
- C) Both architectures are equivalent for this use case — the choice is purely a matter of developer preference.
- D) API Gateway WebSocket + Lambda, because Socket.io does not support cursor position events.

**Correct Answer:** B

**Explanation:** At 10 cursor updates per second per user, a document with 10 simultaneous editors generates 100 messages per second. Every message in the API Gateway + Lambda architecture triggers a Lambda invocation, a DynamoDB scan to get all connectionIds, and N `PostToConnectionCommand` calls. This adds latency and cost at high message rates. Socket.io on a persistent server routes messages through in-memory data structures with microsecond latency. The API Gateway + Lambda pattern excels at scale-to-zero and massive concurrent connection counts — it is not optimized for high-frequency per-connection message routing.

**Distractor Analysis:**

- Why A is incorrect: Lambda concurrency scales, but each invocation involves external service calls (DynamoDB, ApiGatewayManagementApi) with non-trivial latency. High-frequency messages amplify this overhead.
- Why B is correct: In-memory routing on a persistent server is the right choice for high message rates with low latency requirements.
- Why C is incorrect: The architectures have meaningfully different performance and cost characteristics at high message rates.
- Why D is incorrect: Socket.io supports any named event, including cursor position events.

---

## Question 10

A developer deploys the real-time notification app from this module to production. The React app is on CloudFront (`https://d123.cloudfront.net`), the Express server is on Elastic Beanstalk (`https://api.myapp.com`). After deployment, the browser console shows:

```text
WebSocket connection to 'wss://api.myapp.com/socket.io/?...' failed:
Error during WebSocket handshake: Unexpected response code: 400
```

What is the most likely cause?

- A) CloudFront does not support WebSocket traffic — all WebSocket connections must go directly to the origin.
- B) The Socket.io server's CORS `origin` option is set to `http://localhost:5173` (the development value) instead of `https://d123.cloudfront.net`. The upgrade handshake fails the CORS check.
- C) Elastic Beanstalk blocks WebSocket connections by default — the developer must enable WebSocket support in the EB environment settings.
- D) The `wss://` protocol is not supported by Socket.io — the URL must use `ws://` without TLS.

**Correct Answer:** B

**Explanation:** Status `400` on a WebSocket handshake indicates the server rejected the upgrade request. The most common cause in this context is a CORS mismatch: the Socket.io server's `cors.origin` is still set to the development value (`http://localhost:5173`), while the production client connects from `https://d123.cloudfront.net`. The server rejects the handshake because the `Origin` header does not match. The fix is to set `FRONTEND_URL` as an Elastic Beanstalk environment property and use `origin: process.env.FRONTEND_URL` in the Socket.io `cors` config.

**Distractor Analysis:**

- Why A is incorrect: CloudFront supports WebSocket connections. It passes WebSocket upgrade requests to the origin by default.
- Why B is correct: CORS origin mismatch produces a 400 on the Socket.io handshake. This is the most common production deployment mistake for Socket.io apps.
- Why C is incorrect: Elastic Beanstalk does not block WebSocket connections by default. The load balancer must be configured for WebSocket support (which requires idle timeout settings), but the default configuration passes WebSocket traffic.
- Why D is incorrect: `wss://` is the TLS version of WebSocket (WebSocket Secure) and is fully supported by Socket.io. `wss://` is required in production — `ws://` over HTTP would be blocked by the browser's mixed content policy.

---

### Question 11 (5 points)

A Socket.io server broadcasts a message with `io.emit('announcement', data)`. Which clients receive this event?

- A) Only clients that have explicitly subscribed to the `'announcement'` event with `socket.on('announcement', ...)` on the server.
- B) Every connected client on the server, including the sender if the emit was triggered by a socket event handler.
- C) Only clients in the default room.
- D) Only the client whose event triggered the `io.emit()` call.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `io.emit()` is a server-side broadcast — it is not constrained by which server-side handlers are registered. All clients receive the event and each client decides whether to handle it based on their own `socket.on()` listeners.
  - Why B is correct: `io.emit()` broadcasts to every connected client including the sender. This is the widest possible broadcast scope in Socket.io.
  - Why C is incorrect: Socket.io does not have a "default room" that is distinct from the full client list. Every socket is automatically in a room named after its own `socket.id`, but `io.emit()` targets all clients regardless of rooms.
  - Why D is incorrect: `socket.emit()` (not `io.emit()`) sends to only the client associated with that socket instance.

---

### Question 12 (5 points)

A developer writes this React cleanup function:

```jsx
return () => {
  socket.disconnect();
};
```

The component re-mounts because the user navigates away and back. What happens to the `'new_notification'` listener?

- A) `socket.disconnect()` removes all event listeners including `'new_notification'`, so re-mounting creates exactly one listener.
- B) `socket.disconnect()` closes the connection but does not remove event listeners. On re-mount, the `useEffect` runs again and adds a second `'new_notification'` listener — each message triggers the handler twice.
- C) `socket.disconnect()` prevents the socket from reconnecting — the component shows "Offline" permanently after unmounting.
- D) Socket.io automatically removes all listeners on disconnect, so the behavior is the same as calling `socket.off('new_notification')`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `socket.disconnect()` closes the transport connection — it does not call `socket.removeAllListeners()`. Listeners remain registered.
  - Why B is correct: Without `socket.off('new_notification')`, each mount cycle adds another listener. After two mount/unmount cycles, three listeners exist, and each event fires three times.
  - Why C is incorrect: Socket.io's automatic reconnection re-establishes the connection when `socket.connect()` is called again (or if `autoConnect` is true and the socket was not manually disconnected). Manual disconnection with `socket.disconnect()` can be reversed by calling `socket.connect()` again.
  - Why D is incorrect: Socket.io does not remove application event listeners on disconnect. The `disconnect` event itself fires, but `on()` registrations persist.

---

### Question 13 (5 points)

A Socket.io server runs on three Elastic Beanstalk instances behind a load balancer. Users on Instance 1 emit events that users on Instance 2 never receive. What is the cause?

- A) Socket.io cannot run on Elastic Beanstalk — it requires a dedicated EC2 instance.
- B) Each server instance maintains its own in-memory set of connected clients. An event emitted on Instance 1 is only broadcast to clients connected to Instance 1 — clients on Instance 2 and 3 are invisible to it. The fix is to use Socket.io with a Redis adapter so all instances share a common pub/sub channel.
- C) The load balancer is blocking WebSocket traffic — enable WebSocket support in the EB load balancer settings.
- D) Socket.io rooms do not work across multiple server instances — use namespaces instead.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Elastic Beanstalk supports Socket.io applications. The problem is distributed state, not platform incompatibility.
  - Why B is correct: Socket.io's in-memory pub/sub only reaches clients connected to the same process. The `socket.io-adapter-redis` package (or the official `@socket.io/redis-adapter`) extends broadcasts across all server instances using Redis as a shared message bus.
  - Why C is incorrect: EB load balancer WebSocket support is a separate concern (sticky sessions and timeout settings) — it does not cause events to be missed on other instances.
  - Why D is incorrect: Namespaces also use in-memory state and have the same limitation across multiple instances.

---

### Question 14 (5 points)

In an API Gateway WebSocket API, a custom route `send_message` is configured. The client sends:

```json
{"action": "send_message", "content": "Hello everyone"}
```

Which Lambda is invoked?

- A) The `$connect` Lambda, because all WebSocket messages go through the connect handler first.
- B) The `$default` Lambda, because custom routes are aliases for `$default`.
- C) The Lambda associated with the `send_message` route, because API Gateway matches the `action` key to the configured route key.
- D) All three Lambdas in sequence: `$connect`, `send_message`, `$disconnect`.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `$connect` fires only when a new WebSocket connection is established, not for every message.
  - Why B is incorrect: Custom routes take precedence over `$default`. When the client sends a message with an `action` key matching a configured route, API Gateway invokes the route-specific Lambda.
  - Why C is correct: API Gateway WebSocket APIs use a route selection expression (typically `$request.body.action`) to match incoming messages to Lambda integrations. A message with `"action": "send_message"` invokes the Lambda attached to the `send_message` route.
  - Why D is incorrect: Lambda functions are invoked individually per event, not in sequence. `$disconnect` fires when the connection closes, not on every message.

---

### Question 15 (5 points)

A developer uses `socket.to(roomId).emit()` to send a project update. Users in the room report they do not see updates when they are the one who made the change. Why, and what is the fix?

- A) `socket.to(roomId).emit()` only works for users who joined the room using `socket.join()` — users who joined via the REST API are excluded.
- B) `socket.to(roomId)` excludes the sending socket. The user who triggered the event does not receive their own update. Use `io.to(roomId).emit()` to include the sender, or update the sender's state client-side optimistically before the emission.
- C) `socket.to(roomId)` has a bug in Socket.io version 4 — use `socket.broadcast.to(roomId)` instead.
- D) The room is empty because Socket.io clears all rooms when the emit is called.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `socket.to(room)` sends to all sockets in the room regardless of how they joined.
  - Why B is correct: The `socket.to()` API explicitly excludes the calling socket. This is by design for patterns like "notify everyone else." For collaborative features where the sender should also see updates, use `io.to(roomId).emit()` or apply the update to the sender's state directly on the client.
  - Why C is incorrect: `socket.to(room)` works correctly in Socket.io v4. `socket.broadcast.to(room)` is the same operation — both exclude the sender.
  - Why D is incorrect: Rooms are persistent for the duration of the connection. Emitting to a room does not clear it.

---

### Question 16 (5 points)

The `$disconnect` Lambda in an API Gateway WebSocket deployment does NOT always fire when a client disconnects. Under what condition does it fail to fire?

- A) When the client is using `wss://` (TLS) instead of `ws://`.
- B) When the connection is closed due to a network interruption or client crash rather than a clean `WebSocket.close()` call — the TCP connection drops without sending a close frame, so API Gateway cannot detect the disconnect immediately.
- C) When the `$disconnect` Lambda is in a different AWS region than the API Gateway.
- D) When the client reconnects within 30 seconds — API Gateway suppresses the disconnect event to avoid unnecessary Lambda invocations.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: TLS does not affect whether the close frame is sent. Both `wss://` and `ws://` use the same WebSocket close handshake.
  - Why B is correct: A clean disconnect sends a WebSocket close frame, which API Gateway catches and invokes `$disconnect`. A network drop — mobile switching networks, laptop lid close, browser crash — may leave the TCP connection half-open. API Gateway eventually detects it via timeout and may invoke `$disconnect`, but the timing is unreliable. This is why handling `410 Gone` from `PostToConnectionCommand` is essential for cleanup.
  - Why C is incorrect: Lambda and API Gateway are regional services — the Lambda is always in the same region as the API Gateway that invokes it.
  - Why D is incorrect: API Gateway has no such suppression logic. A disconnect followed by reconnect generates separate `$disconnect` and `$connect` events with different `connectionId` values.

---

### Question 17 (5 points)

A developer adds `socket.once('new_message', handler)` instead of `socket.on('new_message', handler)` in a chat component. What is the behavioral difference?

- A) `socket.once()` registers a listener that is automatically removed after the first event. The user will only see the first message — subsequent messages are silently dropped.
- B) `socket.once()` is identical to `socket.on()` in production but logs a deprecation warning in development.
- C) `socket.once()` queues all messages until the component re-renders, then delivers them all at once.
- D) `socket.once()` is required for React — `socket.on()` does not work with React's state updates.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: `socket.once()` is the standard Node.js `EventEmitter.once()` behavior — the listener fires exactly once, then is removed. In a chat component this means only the first incoming message is handled. All subsequent messages arrive with no listener registered and are discarded.
  - Why B is incorrect: `socket.once()` and `socket.on()` have different semantics. There is no deprecation warning.
  - Why C is incorrect: Socket.io does not buffer events per render cycle. Events are delivered immediately as they arrive from the server.
  - Why D is incorrect: `socket.on()` works correctly with React state updates when used in `useEffect`.

---

### Question 18 (5 points)

A developer deploys a Socket.io application to Elastic Beanstalk with multiple EC2 instances. Users report that real-time features work when they first connect, but after navigating for a few minutes, notifications stop arriving. What is the most likely cause?

- A) Socket.io connections time out after 5 minutes on Elastic Beanstalk.
- B) The Elastic Beanstalk load balancer is using round-robin routing, sending subsequent HTTP requests to different EC2 instances. The WebSocket connection stays on the original instance, but if that instance's Socket.io server emits to a room, only clients on that instance receive it. Additionally, if the load balancer routes a polling request to a different instance, Socket.io may lose the session.
- C) Socket.io requires sticky sessions to maintain WebSocket upgrades but the notifications stop because the Redis adapter is not configured.
- D) Elastic Beanstalk automatically terminates WebSocket connections after 60 seconds to free resources.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Socket.io does not have a hardcoded 5-minute timeout. Connections remain open as long as the underlying TCP connection is maintained and heartbeats succeed.
  - Why B is correct: Two distinct problems emerge with multiple EB instances: (1) WebSocket/polling transport affinity — without sticky sessions, polling requests can hit different instances and break session state; (2) in-memory pub/sub isolation — broadcasts only reach clients on the same instance. Both require fixes: sticky sessions (EB load balancer setting) and a Redis adapter.
  - Why C is incorrect: This is partially right but incomplete. Sticky sessions fix the transport problem; the Redis adapter fixes the broadcast problem. Both are needed — sticky sessions alone does not solve the notification delivery issue across instances.
  - Why D is incorrect: Elastic Beanstalk does not auto-terminate WebSocket connections at 60 seconds. The load balancer idle timeout can be configured and defaults to 60 seconds for HTTP — this must be increased for WebSocket connections, but it is a configuration step, not an automatic behavior.

---

### Question 19 (5 points)

Which Socket.io server code pattern correctly sends a real-time notification from inside an Express REST route handler (not from inside a socket event handler)?

- A) `socket.emit('notification', data)` — `socket` is available globally after any client connects.
- B) After attaching `io` to the Express app with `app.set('io', io)`, use `const io = req.app.get('io'); io.to('user:42').emit('notification', data)` inside the route handler.
- C) Import `io` directly from the Socket.io module using `const { io } = require('socket.io')`.
- D) Use `res.socket.emit('notification', data)` — `res.socket` is the Socket.io instance for the current request.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `socket` inside `io.on('connection')` is scoped to that specific connection callback. It cannot be accessed as a global variable from a separate route handler.
  - Why B is correct: `app.set('io', io)` stores the Socket.io server instance on the Express app object, making it accessible anywhere via `req.app.get('io')`. This is the standard pattern for emitting from REST route handlers.
  - Why C is incorrect: `require('socket.io')` exports the `Server` class, not an instance. The `io` instance is created by the application and must be passed explicitly.
  - Why D is incorrect: `res.socket` is a Node.js `net.Socket` (the raw TCP socket) — it has nothing to do with Socket.io. Calling `.emit()` on it would throw an error.

---

### Question 20 (5 points)

A developer is building a live sports score application that must push score updates to thousands of concurrent users every 5 seconds. They need to choose between Socket.io on Elastic Beanstalk and API Gateway WebSocket + Lambda. Which factors most favor the API Gateway + Lambda architecture for this use case?

- A) API Gateway WebSocket + Lambda is cheaper for high message frequency because Lambda invocations cost less than EC2 hours.
- B) The application has predictable bursty traffic (high during games, near-zero between games). API Gateway + Lambda scales to zero automatically between games — no EC2 instance is running or incurring cost. At peak, Lambda scales horizontally without manual auto-scaling configuration.
- C) API Gateway WebSocket + Lambda performs better than Socket.io for high-frequency broadcasts because DynamoDB scans are faster than in-memory operations.
- D) API Gateway WebSocket APIs support more concurrent connections than Socket.io because WebSocket is a protocol, not a library.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: For very high message frequency (thousands of users × many messages per second), Lambda invocation costs can exceed EC2 costs. The cost advantage of Lambda is at low or unpredictable traffic, not high sustained throughput.
  - Why B is correct: The scale-to-zero property is the primary advantage for bursty workloads. An EB environment running 24/7 incurs EC2 charges even between games. Lambda + API Gateway incurs costs only when connections are active and messages are flowing. For a sports app with clear game schedules, this is a significant cost advantage.
  - Why C is incorrect: In-memory operations are orders of magnitude faster than DynamoDB scans. DynamoDB adds latency to every broadcast — the API Gateway architecture is slower for high-frequency messages, not faster.
  - Why D is incorrect: Both Socket.io and API Gateway support large connection counts. The protocol (WebSocket) is the same underneath — the limiting factor is the infrastructure managing connections, not the library or service.
