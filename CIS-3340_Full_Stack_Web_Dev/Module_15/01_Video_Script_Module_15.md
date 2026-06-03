# Video Script: Module 15 — WebSockets and Real-Time Communication

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with Socket.io project, browser showing live chat demo
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for browser demo; [PAUSE] for slides
- Have `socket.io` installed on server, `socket.io-client` in React project
- Two browser windows open side-by-side to demonstrate real-time message delivery

---

## Section 1: Introduction — Why WebSockets? (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 15 — WebSockets and Real-Time Communication.

Every application we've built so far follows the same pattern: the browser sends a request, the server responds, the connection closes. That works perfectly for loading data. But what happens when the server has new information and needs to notify the client immediately — without the client asking first?

Think about a live notification badge that updates the moment a colleague assigns you a project. Or a chat message that appears instantly without refreshing the page. Or a dashboard that updates ticket counts in real time as data changes. HTTP's request-response cycle cannot do this efficiently. WebSockets can.

In this module we cover the WebSocket protocol and how it differs from HTTP, Socket.io as the standard Node.js WebSocket library, building a real-time feature in an Express plus React application, and AWS API Gateway WebSocket APIs for serverless real-time architectures.

[PAUSE — slide: Module 15 Learning Objectives]

---

## Section 2: The Problem with Polling (1:30 – 4:00)

Before WebSockets, developers used polling to simulate real-time behavior.

[PAUSE — slide: Three approaches — short polling, long polling, WebSockets]

**Short polling**: The client sends a new HTTP request every N seconds asking "is there anything new?" The server responds immediately with data or an empty response. Simple to implement but wasteful — the vast majority of requests return nothing, and every request carries the full HTTP header overhead.

**Long polling**: The client sends a request. The server holds the connection open until new data is available, then responds. The client immediately sends another request. Reduces wasted requests but holds server connections open for seconds at a time, which does not scale well.

**WebSockets**: The client and server complete a one-time HTTP handshake that upgrades the connection to the WebSocket protocol. After the upgrade, both sides can send messages at any time over a persistent TCP connection. No per-message headers. No request-response cycle. The connection stays open until one side closes it.

[PAUSE — slide: WebSocket upgrade handshake headers]

The upgrade handshake uses standard HTTP headers:

```http
GET /chat HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: <random-base64>
Sec-WebSocket-Version: 13
```

The server responds with `101 Switching Protocols`. From that point, the TCP connection carries WebSocket frames instead of HTTP messages.

---

## Section 3: Socket.io Architecture (4:00 – 7:00)

The native WebSocket API in the browser and Node.js is usable but low-level. Socket.io is the standard library that adds automatic reconnection, event naming, rooms and namespaces, and a fallback to HTTP long polling if WebSockets are blocked by a corporate proxy.

[SHOW CODE]

```bash
# Server
npm install socket.io

# Client (React with Vite)
npm install socket.io-client
```

[PAUSE — slide: Socket.io layered on top of WebSocket protocol]

Socket.io uses an event-driven model identical to Node.js EventEmitter. Both sides emit named events and register listeners for named events.

[SHOW CODE]

```js
// server — server.js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const cors = require('cors');

const app = express();
app.use(cors({ origin: process.env.FRONTEND_URL || 'http://localhost:5173' }));

const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: process.env.FRONTEND_URL || 'http://localhost:5173',
    methods: ['GET', 'POST'],
  },
});

io.on('connection', (socket) => {
  console.log(`Client connected: ${socket.id}`);

  socket.on('send_message', (data) => {
    // Broadcast to all connected clients
    io.emit('receive_message', data);
  });

  socket.on('disconnect', () => {
    console.log(`Client disconnected: ${socket.id}`);
  });
});

server.listen(3000, () => console.log('Server running on port 3000'));
```

Notice that Socket.io requires `http.createServer(app)` — you wrap the Express app in a plain HTTP server and pass that to Socket.io's `Server` constructor. This lets Socket.io intercept the WebSocket upgrade handshake on the same port as your HTTP routes.

[PAUSE — slide: io.emit vs socket.emit vs socket.to().emit]

Three emission targets:

- `io.emit('event', data)` — sends to ALL connected clients including the sender
- `socket.emit('event', data)` — sends only to the client that triggered this handler
- `socket.to('roomName').emit('event', data)` — sends to everyone in a room except the sender

---

## Section 4: React Client Integration (7:00 – 10:30)

[SHOW CODE]

```jsx
// src/socket.js — create a singleton socket instance
import { io } from 'socket.io-client';

const SOCKET_URL = import.meta.env.VITE_SOCKET_URL || 'http://localhost:3000';

export const socket = io(SOCKET_URL, {
  autoConnect: false, // connect manually when user enters the app
});
```

Creating the socket in a separate file prevents multiple connections when React re-renders the component.

[SHOW CODE]

```jsx
// src/components/Chat.jsx
import { useState, useEffect } from 'react';
import { socket } from '../socket';

function Chat({ username }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    // Connect when component mounts
    socket.connect();

    // Listen for incoming messages
    socket.on('receive_message', (data) => {
      setMessages((prev) => [...prev, data]);
    });

    // Cleanup: disconnect and remove listener on unmount
    return () => {
      socket.off('receive_message');
      socket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    if (!input.trim()) return;
    socket.emit('send_message', { username, text: input, timestamp: Date.now() });
    setInput('');
  };

  return (
    <div>
      <ul>
        {messages.map((msg, i) => (
          <li key={i}><strong>{msg.username}:</strong> {msg.text}</li>
        ))}
      </ul>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chat;
```

[PAUSE — slide: useEffect cleanup pattern — socket.off() and socket.disconnect()]

The cleanup function in `useEffect` is critical. Without `socket.off('receive_message')`, the listener accumulates on every re-render of the component, causing messages to appear multiple times. Without `socket.disconnect()`, the connection stays open after the user navigates away.

---

## Section 5: Rooms and Namespaces (10:30 – 13:00)

A chat application with one global broadcast is fine for a demo. Real applications need private channels — a chat room for each project, or a notification channel scoped to one user.

[SHOW CODE]

```js
// Server — room-based chat
io.on('connection', (socket) => {
  // Client requests to join a specific project room
  socket.on('join_room', (roomId) => {
    socket.join(roomId);
    socket.to(roomId).emit('user_joined', { socketId: socket.id });
  });

  socket.on('room_message', ({ roomId, message }) => {
    // Emit to everyone in the room including sender
    io.to(roomId).emit('room_message', message);
  });

  socket.on('leave_room', (roomId) => {
    socket.leave(roomId);
  });
});
```

[SHOW CODE]

```jsx
// Client — join a room when the component mounts
useEffect(() => {
  socket.connect();
  socket.emit('join_room', projectId);

  socket.on('room_message', (msg) => {
    setMessages((prev) => [...prev, msg]);
  });

  return () => {
    socket.emit('leave_room', projectId);
    socket.off('room_message');
    socket.disconnect();
  };
}, [projectId]);
```

[PAUSE — slide: Socket.io rooms vs namespaces]

Rooms are lightweight logical groupings within a single server. Namespaces are separate connection endpoints — `io.of('/admin')` creates a namespace that clients connect to with `io('/admin')`. Use rooms for dynamic groupings; use namespaces when you need different middleware or permissions on the connection itself.

---

## Section 6: Authentication on WebSocket Connections (13:00 – 15:30)

WebSocket connections run before the HTTP middleware chain. A client that sends a valid JWT in an HTTP request is not automatically authenticated on a Socket.io connection.

[SHOW CODE]

```js
// Server — authenticate WebSocket connections with JWT
const jwt = require('jsonwebtoken');

io.use((socket, next) => {
  const token = socket.handshake.auth.token;

  if (!token) {
    return next(new Error('Authentication required'));
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    socket.data.user = decoded;
    next();
  } catch (err) {
    next(new Error('Invalid token'));
  }
});

io.on('connection', (socket) => {
  // socket.data.user is available here
  const user = socket.data.user;
  console.log(`Authenticated connection from ${user.email}`);
});
```

[SHOW CODE]

```js
// Client — send token in handshake auth
const token = localStorage.getItem('token');

export const socket = io(SOCKET_URL, {
  autoConnect: false,
  auth: { token },
});
```

The Socket.io `io.use()` middleware intercepts every connection before the `connection` event fires. Calling `next(new Error(...))` rejects the connection and the client receives a `connect_error` event.

---

## Section 7: AWS API Gateway WebSocket APIs (15:30 – 19:30)

The Socket.io pattern we built requires a persistent server. In a serverless architecture, Lambda functions are stateless and ephemeral — they cannot hold WebSocket connections. AWS API Gateway WebSocket API solves this.

[PAUSE — slide: API Gateway WebSocket vs Socket.io — architecture comparison]

API Gateway WebSocket manages the persistent connections itself. When a client connects, disconnects, or sends a message, API Gateway invokes a Lambda function for the corresponding route.

Three built-in routes:

- `$connect` — invoked when a client establishes a WebSocket connection
- `$disconnect` — invoked when a client disconnects
- `$default` — invoked for every message that doesn't match a custom route

[SHOW CODE]

```js
// Lambda handler for $connect — stores connectionId in DynamoDB
const { DynamoDBClient, PutItemCommand } = require('@aws-sdk/client-dynamodb');
const client = new DynamoDBClient({});

exports.handler = async (event) => {
  const connectionId = event.requestContext.connectionId;

  await client.send(new PutItemCommand({
    TableName: process.env.CONNECTIONS_TABLE,
    Item: { connectionId: { S: connectionId } },
  }));

  return { statusCode: 200 };
};
```

[SHOW CODE]

```js
// Lambda handler for $default — broadcast message to all connections
const { DynamoDBClient, ScanCommand, DeleteItemCommand } = require('@aws-sdk/client-dynamodb');
const { ApiGatewayManagementApiClient, PostToConnectionCommand } = require('@aws-sdk/client-apigatewaymanagementapi');

const dynamo = new DynamoDBClient({});

exports.handler = async (event) => {
  const body = JSON.parse(event.body);
  const domain = event.requestContext.domainName;
  const stage = event.requestContext.stage;
  const endpoint = `https://${domain}/${stage}`;

  const apigw = new ApiGatewayManagementApiClient({ endpoint });

  // Get all connection IDs
  const { Items } = await dynamo.send(new ScanCommand({
    TableName: process.env.CONNECTIONS_TABLE,
  }));

  // Send to each connection; remove stale connections
  await Promise.all(Items.map(async ({ connectionId }) => {
    try {
      await apigw.send(new PostToConnectionCommand({
        ConnectionId: connectionId.S,
        Data: JSON.stringify(body),
      }));
    } catch (err) {
      if (err.statusCode === 410) {
        // Connection is stale — remove it
        await dynamo.send(new DeleteItemCommand({
          TableName: process.env.CONNECTIONS_TABLE,
          Key: { connectionId: { S: connectionId.S } },
        }));
      }
    }
  }));

  return { statusCode: 200 };
};
```

[PAUSE — slide: API Gateway WebSocket vs Socket.io decision matrix]

When to use each:

- Socket.io on a persistent server (EB, ECS): Requires a server that stays up. Simpler code. Better for high-message-rate applications. Supports rooms, namespaces, and reconnect natively.
- API Gateway WebSocket + Lambda + DynamoDB: Fully serverless. Scales to millions of concurrent connections with zero server management. Connection IDs must be stored externally (DynamoDB) for broadcast. More complex architecture.

---

## Section 8: React Integration with API Gateway WebSocket (19:30 – 21:30)

[SHOW CODE]

```jsx
// React — native WebSocket API (no Socket.io needed for API Gateway)
import { useState, useEffect, useRef } from 'react';

const WS_URL = import.meta.env.VITE_WS_URL;

function useWebSocket(url) {
  const [messages, setMessages] = useState([]);
  const wsRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);
    };

    ws.onerror = (err) => console.error('WebSocket error:', err);

    return () => ws.close();
  }, [url]);

  const send = (data) => {
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(data));
    }
  };

  return { messages, send };
}
```

The native WebSocket API uses `ws.onmessage`, `ws.onerror`, `ws.onopen`, and `ws.onclose` instead of Socket.io's event names. `ws.readyState === WebSocket.OPEN` guards against sending on a closed connection.

---

## Conclusion (21:30 – 23:00)

Summary of Module 15 — WebSockets and Real-Time Communication:

- HTTP polling is wasteful. WebSockets establish a persistent full-duplex TCP connection after a one-time upgrade handshake.
- Socket.io adds reconnection, event names, rooms, namespaces, and polling fallback to the WebSocket protocol.
- Create the socket instance in a separate module — not inside a React component — to prevent duplicate connections.
- The `useEffect` cleanup function must call `socket.off()` and `socket.disconnect()` to prevent listener accumulation.
- Rooms scope broadcasts to subsets of connected clients. Namespaces separate connection endpoints with different middleware.
- Authenticate WebSocket connections with `io.use()` middleware before the `connection` event fires.
- API Gateway WebSocket API manages persistent connections for serverless architectures. Lambda handles `$connect`, `$disconnect`, and `$default`. DynamoDB stores connection IDs for broadcast.
- For the AWS Developer Associate exam: know that API Gateway WebSocket requires storing `connectionId` in DynamoDB and sending responses via `ApiGatewayManagementApiClient`. Status `410 Gone` means the connection is stale.

Your lab this week builds a real-time project notification panel using Socket.io. See you in Module 16 — our final module and AWS Developer Associate exam prep.

[END OF SCRIPT]
