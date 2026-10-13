# Lab 15: Real-Time Project Notifications with Socket.io

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90–120 minutes

---

## Objectives

By completing this lab you will:

- Add Socket.io to an Express server that already has REST routes and JWT auth
- Build a `NotificationPanel` React component that receives live push notifications
- Authenticate WebSocket connections using JWT in Socket.io middleware
- Use rooms to scope notifications to individual users
- Test real-time delivery by opening two browser windows simultaneously

---

## Prerequisites

- Lab 13 complete (Express API with JWT authentication)
- Module 15 video and reading guide complete
- Two terminal windows available (server + React dev server)

---

## Part 1: Install Socket.io (5 minutes)

### Step 1 — Install server package

In your `lab13-auth` directory (or a copy renamed `lab15-notifications`):

```bash
npm install socket.io
```

### Step 2 — Install client package

In your React project (the Vite frontend from Lab 13 or earlier):

```bash
npm install socket.io-client
```

---

## Part 2: Upgrade the Express Server (20 minutes)

### Step 3 — Wrap app in an http.Server

Open `server.js` (or `app.js` — whichever file calls `app.listen`).

Find this line:

```js
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

Replace it with:

```js
const http = require('http');
const { Server } = require('socket.io');

const server = http.createServer(app);

// TODO 1: Create the Socket.io Server instance.
// - Pass `server` as the first argument.
// - Configure cors with:
//     origin: process.env.FRONTEND_URL || 'http://localhost:5173'
//     methods: ['GET', 'POST']
// Assign the result to a variable named `io`.
const io = /* YOUR CODE HERE */;

server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### Step 4 — Add Socket.io authentication middleware

Below the `io` declaration, add:

```js
const jwt = require('jsonwebtoken');

// TODO 2: Add io.use() middleware to authenticate WebSocket connections.
// - Read the token from socket.handshake.auth.token
// - If no token is present, call next(new Error('Authentication required'))
// - Call jwt.verify(token, process.env.JWT_SECRET)
// - On success: assign the decoded payload to socket.data.user, then call next()
// - On failure (catch): call next(new Error('Invalid token'))
io.use((socket, next) => {
  /* YOUR CODE HERE */
});
```

### Step 5 — Add connection handler with user rooms

After the `io.use()` middleware:

```js
io.on('connection', (socket) => {
  const user = socket.data.user;
  console.log(`WS connected: ${user.email} (${socket.id})`);

  // TODO 3: Join a room named after the user's userId so that
  // notifications can be sent to a specific user.
  // Use socket.join() with a room name of `user:${user.userId}`.
  /* YOUR CODE HERE */

  socket.on('disconnect', () => {
    console.log(`WS disconnected: ${user.email}`);
  });
});
```

### Step 6 — Export `io` for use in route handlers

At the bottom of `server.js`, before `module.exports` (if you have one), add:

```js
module.exports = { app, server, io };
```

If `server.js` does not use `module.exports`, you will pass `io` differently in Step 8.

---

## Part 3: Emit Notifications from REST Routes (20 minutes)

### Step 7 — Update app.js to accept io

If your routes are in separate files, you need to pass `io` to the route that will emit notifications. The pattern is to attach `io` to the Express `app` object so any route can access it:

In `server.js`, after creating `io`:

```js
app.set('io', io);
```

In any route handler that needs to emit:

```js
const io = req.app.get('io');
```

### Step 8 — Emit a notification when a new project note is created

Open `routes/notes.js` (or your equivalent POST route for creating notes or action items).

Find the route handler for `POST /api/notes` (or equivalent). After saving the new item successfully, add:

```js
// TODO 4: Emit a real-time notification to the note's target user.
// - Get io: const io = req.app.get('io')
// - Emit to room `user:${targetUserId}` (use the userId of the note's owner)
// - Event name: 'new_notification'
// - Payload: { type: 'NOTE_CREATED', message: 'A new note was added to your project', projectId, createdAt: new Date().toISOString() }
/* YOUR CODE HERE */
```

If your API does not have a notes route, use the POST /api/students or POST /api/books route from a previous lab and emit a notification to the currently authenticated user (`req.user.userId`).

---

## Part 4: Create the Socket Singleton (10 minutes)

### Step 9 — Create src/socket.js in your React project

```js
// src/socket.js
import { io } from 'socket.io-client';

const SOCKET_URL = import.meta.env.VITE_SOCKET_URL || 'http://localhost:3000';

// TODO 5: Create the socket instance.
// - Call io(SOCKET_URL, { autoConnect: false })
// - This prevents a connection before the user logs in.
// Export the result as a named export `socket`.
export const socket = /* YOUR CODE HERE */;
```

### Step 10 — Update .env.development

Add to your Vite `.env.development` file:

```text
VITE_SOCKET_URL=http://localhost:3000
```

---

## Part 5: Build the NotificationPanel Component (25 minutes)

### Step 11 — Create src/components/NotificationPanel.jsx

```jsx
// src/components/NotificationPanel.jsx
import { useState, useEffect } from 'react';
import { socket } from '../socket';

// TODO 6: Complete the NotificationPanel component.
// Requirements:
// - Accept a `token` prop (the user's JWT from localStorage or auth context)
// - On mount:
//     a) Set socket.auth = { token } so the server can authenticate the connection
//     b) Call socket.connect()
//     c) Register a listener for 'new_notification' that prepends the new notification
//        to the notifications array using the functional updater form:
//        setNotifications(prev => [data, ...prev])
// - On unmount:
//     a) Call socket.off('new_notification')
//     b) Call socket.disconnect()
// - Render a list of notifications. Each item shows notification.message and notification.createdAt.
// - If notifications.length === 0, render <p>No notifications</p>

function NotificationPanel({ token }) {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    /* YOUR CODE HERE */
  }, [token]);

  return (
    <div className="notification-panel">
      <h3>Notifications</h3>
      {/* YOUR JSX HERE */}
    </div>
  );
}

export default NotificationPanel;
```

### Step 12 — Add connection status indicator

Extend `NotificationPanel` to track whether the socket is connected:

```jsx
// TODO 7: Add a connected state variable (useState(false)).
// - Register socket.on('connect', ...) to set connected to true
// - Register socket.on('disconnect', ...) to set connected to false
// - Register socket.on('connect_error', (err) => console.error('WS auth failed:', err.message))
// - Clean up all three listeners in the useEffect return function
// - Render a status badge: if connected show a green dot and "Live", else a grey dot and "Offline"
```

---

## Part 6: Wire NotificationPanel into the App (10 minutes)

### Step 13 — Add NotificationPanel to App.jsx

In your `App.jsx` (or wherever the authenticated layout lives):

```jsx
import NotificationPanel from './components/NotificationPanel';

// In your JSX, after the user is authenticated:
{user && <NotificationPanel token={localStorage.getItem('token')} />}
```

---

## Part 7: Testing (15 minutes)

### Step 14 — Manual test sequence

Start both servers:

```bash
# Terminal 1 — Express server
npm run dev

# Terminal 2 — React dev server
npm run dev
```

Open two browser windows. Log in as the same user in both windows. In one window, create a new note (or trigger the POST route from Step 8). Verify the notification appears in the `NotificationPanel` in **both** windows within 1–2 seconds without refreshing.

### Step 15 — Test authentication rejection

In the browser console of a logged-in window, run:

```js
socket.disconnect();
socket.auth = { token: 'invalid.token.here' };
socket.connect();
```

The `NotificationPanel` status badge should show "Offline" and the server console should log the rejected connection attempt.

### Expected Behavior

| Action | Expected result |
|---|---|
| User logs in, NotificationPanel mounts | Status badge shows "Live" (green) |
| POST request creates a note | `new_notification` event received; notification appears without refresh |
| Two windows open for same user | Both windows receive the notification |
| Invalid token used | `connect_error` logged; status shows "Offline" |
| Component unmounts (navigate away) | `socket.disconnect()` called; no active connection |

---

## Deliverables

Submit your project zip (excluding `node_modules`). Required files:

1. `server.js` — Socket.io Server creation, `io.use()` auth middleware, `connection` handler with room join (TODOs 1–3)
2. Route file with notification emit (TODO 4)
3. `src/socket.js` — singleton socket instance (TODO 5)
4. `src/components/NotificationPanel.jsx` — connection, listener, cleanup, status badge (TODOs 6–7)
5. Screenshot or screen recording showing a notification appearing in two browser windows simultaneously

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Socket.io Server created with CORS config and http.Server wrapping | 15 |
| `io.use()` middleware authenticates token and rejects invalid tokens | 20 |
| User joins personal room on connection | 10 |
| POST route emits `new_notification` to correct user room | 15 |
| `socket.js` singleton with `autoConnect: false` | 10 |
| `NotificationPanel` connects, listens, and cleans up correctly | 20 |
| Status badge reflects live/offline state | 5 |
| Two-window screenshot demonstrates real-time delivery | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Typing Indicators

Add a real-time "User is typing..." indicator to the notification panel, demonstrating bidirectional communication from client to server.

1. On the server, add two new event handlers inside `io.on('connection', ...)`:

```js
socket.on('typing_start', ({ roomId }) => {
  socket.to(roomId).emit('user_typing', {
    userId: socket.data.user.userId,
    email: socket.data.user.email,
  });
});

socket.on('typing_stop', ({ roomId }) => {
  socket.to(roomId).emit('user_stopped_typing', {
    userId: socket.data.user.userId,
  });
});
```

1. In the React `NotificationPanel` (or a new `TypingIndicator` component), add state and listeners:

```jsx
const [typingUsers, setTypingUsers] = useState([]);

// In useEffect, after socket.connect():
socket.on('user_typing', ({ userId, email }) => {
  setTypingUsers(prev =>
    prev.find(u => u.userId === userId) ? prev : [...prev, { userId, email }]
  );
});

socket.on('user_stopped_typing', ({ userId }) => {
  setTypingUsers(prev => prev.filter(u => u.userId !== userId));
});

// Clean up in return:
socket.off('user_typing');
socket.off('user_stopped_typing');
```

1. Add a text input with `onFocus` and `onBlur` handlers that emit `typing_start` and `typing_stop`:

```jsx
<input
  type="text"
  placeholder="Type a message..."
  onFocus={() => socket.emit('typing_start', { roomId: `project:${projectId}` })}
  onBlur={() => socket.emit('typing_stop', { roomId: `project:${projectId}` })}
/>
```

1. Open two browser windows. Click into the input in one window and verify the typing indicator appears in the other window within 500 ms. Click away and confirm the indicator disappears.

### Challenge 2: Unread Notification Badge with Acknowledgements

Track unread notifications with a badge count and mark them as read using Socket.io acknowledgements.

1. In `NotificationPanel`, add an `unreadCount` state variable. Increment it each time a `'new_notification'` event arrives. Render a badge next to the panel header:

```jsx
const [unreadCount, setUnreadCount] = useState(0);

// In the new_notification listener:
socket.on('new_notification', (data) => {
  setNotifications(prev => [data, ...prev]);
  setUnreadCount(prev => prev + 1);
});
```

1. Add a "Mark all read" button that emits a `mark_read` event with a Socket.io acknowledgement callback:

```jsx
<button onClick={() => {
  socket.emit('mark_read', {}, (response) => {
    if (response.ok) setUnreadCount(0);
  });
}}>
  Mark all read ({unreadCount})
</button>
```

1. On the server, handle the `mark_read` event with an acknowledgement:

```js
socket.on('mark_read', (data, callback) => {
  // In a real app, update the database here
  console.log(`${socket.data.user.email} marked notifications as read`);
  callback({ ok: true });
});
```

1. Test: receive 3 notifications (trigger 3 POST requests). Confirm the badge shows `3`. Click "Mark all read" and confirm the badge resets to `0` immediately — demonstrating the round-trip acknowledgement pattern.

### Reflection Questions

1. The typing indicator in Challenge 1 emits a separate `typing_stop` event when the user blurs the input. What problem would occur if the user closes the browser tab while typing (without blurring), and how would you add a timeout on the receiver side to auto-clear stale typing indicators?
1. Socket.io acknowledgements in Challenge 2 provide a request-response pattern over WebSocket. Compare this to a REST API call for the same "mark read" operation — list two scenarios where the Socket.io acknowledgement pattern is preferable and two where a REST call would be better.
