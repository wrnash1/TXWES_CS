# Reading Guide: Module 15 — WebSockets and Real-Time Communication

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

---

## Overview

This module covers the WebSocket protocol, Socket.io, and AWS API Gateway WebSocket APIs. By the end of this guide you will understand how persistent TCP connections differ from HTTP, how to build a real-time feature in a full-stack Express plus React application, and how the serverless equivalent works on AWS.

---

## 1. HTTP vs WebSockets

Every HTTP request follows the same lifecycle: the client opens a TCP connection, sends a request, receives a response, and the connection closes (or is reused briefly with HTTP keep-alive). The server can never initiate a message to the client — it can only respond.

WebSockets change this. A WebSocket connection starts with a standard HTTP request that asks the server to upgrade the protocol:

```http
GET /notifications HTTP/1.1
Host: api.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13
```

The server accepts:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

After `101 Switching Protocols`, the TCP connection carries WebSocket frames. Both sides can send messages at any time. The connection stays open until one side sends a close frame.

| Feature | HTTP Request-Response | WebSocket |
|---|---|---|
| Direction | Client → Server only | Full-duplex (both directions) |
| Connection lifecycle | One request, one response | Persistent until closed |
| Server push | Not possible | Yes — server sends anytime |
| Per-message overhead | Full HTTP headers (~500 bytes) | 2–10 byte WebSocket frame |
| Use case | Load page, fetch data | Chat, live notifications, dashboards |

---

## 2. Socket.io

The native WebSocket API (available in both browsers and Node.js) is functional but minimal. Socket.io is the standard library for WebSocket applications in Node.js. It adds:

- **Named events** — emit `'send_message'` and listen for `'send_message'`, instead of parsing raw message bytes
- **Automatic reconnection** — if the connection drops, the client reconnects and re-joins rooms automatically
- **Rooms** — logical groupings that scope broadcasts to subsets of clients
- **Namespaces** — separate connection endpoints with independent middleware chains
- **Polling fallback** — if WebSockets are blocked by a corporate proxy, Socket.io falls back to HTTP long polling transparently

### Installation

```bash
# Express server
npm install socket.io

# React client (Vite project)
npm install socket.io-client
```

### Server Setup

Socket.io wraps an `http.Server` instance, not the Express `app` directly. This lets Socket.io intercept the WebSocket upgrade handshake on the same port as your REST routes.

```js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: process.env.FRONTEND_URL,
    methods: ['GET', 'POST'],
  },
});

io.on('connection', (socket) => {
  console.log(`Connected: ${socket.id}`);

  socket.on('send_message', (data) => {
    io.emit('receive_message', data);
  });

  socket.on('disconnect', () => {
    console.log(`Disconnected: ${socket.id}`);
  });
});

server.listen(3000);
```

Key points:

- `io.on('connection', callback)` fires for every new client
- Each client gets a unique `socket.id`
- Events on the server's `socket` object are scoped to that one client
- `io.emit(...)` broadcasts to all clients; `socket.emit(...)` sends only to the calling client

### Emission Targets

| Method | Recipients |
|---|---|
| `io.emit('event', data)` | All connected clients (including sender) |
| `socket.emit('event', data)` | Only the client whose handler is executing |
| `socket.to('roomId').emit('event', data)` | All clients in the room except sender |
| `io.to('roomId').emit('event', data)` | All clients in the room including sender |

---

## 3. Singleton Socket in React

Create the Socket.io client instance in a separate module, not inside a component. If you call `io(url)` inside a component, each render creates a new connection.

```js
// src/socket.js
import { io } from 'socket.io-client';

export const socket = io(import.meta.env.VITE_SOCKET_URL, {
  autoConnect: false,
});
```

`autoConnect: false` prevents the connection from opening before the user authenticates. Call `socket.connect()` manually when appropriate.

### Connecting in a Component

```jsx
import { useEffect, useState } from 'react';
import { socket } from '../socket';

function NotificationPanel() {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    socket.connect();

    socket.on('new_notification', (data) => {
      setNotifications((prev) => [...prev, data]);
    });

    return () => {
      socket.off('new_notification');
      socket.disconnect();
    };
  }, []);

  return (
    <ul>
      {notifications.map((n, i) => <li key={i}>{n.message}</li>)}
    </ul>
  );
}
```

The cleanup function must:

1. Call `socket.off('event_name')` — removes the listener to prevent duplicate handlers across re-renders
2. Call `socket.disconnect()` — closes the connection when the component unmounts

Without `socket.off()`, every render that runs `useEffect` adds another `'new_notification'` listener, causing each message to appear N times where N is the re-render count.

---

## 4. Rooms

Rooms group connections so that broadcasts reach only relevant clients.

```js
// Server
io.on('connection', (socket) => {
  socket.on('join_project', (projectId) => {
    socket.join(`project:${projectId}`);
  });

  socket.on('project_update', ({ projectId, update }) => {
    io.to(`project:${projectId}`).emit('project_update', update);
  });

  socket.on('leave_project', (projectId) => {
    socket.leave(`project:${projectId}`);
  });
});
```

```jsx
// Client
useEffect(() => {
  socket.connect();
  socket.emit('join_project', projectId);

  socket.on('project_update', (update) => {
    setProject((prev) => ({ ...prev, ...update }));
  });

  return () => {
    socket.emit('leave_project', projectId);
    socket.off('project_update');
    socket.disconnect();
  };
}, [projectId]);
```

A client can be in multiple rooms simultaneously. Room membership is server-side only — clients do not know which rooms other clients are in.

---

## 5. Authenticating WebSocket Connections

Socket.io connections bypass Express middleware. A JWT verified in `requireAuth` middleware does not apply to WebSocket connections. Authenticate on the connection itself using `io.use()`.

```js
const jwt = require('jsonwebtoken');

io.use((socket, next) => {
  const token = socket.handshake.auth.token;

  if (!token) return next(new Error('Authentication required'));

  try {
    socket.data.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch {
    next(new Error('Invalid token'));
  }
});
```

```js
// Client — send token in connection handshake
const socket = io(SOCKET_URL, {
  auth: { token: localStorage.getItem('token') },
});
```

`io.use()` middleware runs before `connection` fires. Calling `next(new Error(...))` rejects the connection. The client receives a `connect_error` event with the error message.

---

## 6. AWS API Gateway WebSocket API

Socket.io requires a persistent server. For serverless architectures, AWS API Gateway WebSocket API manages the TCP connections and invokes Lambda functions for each event.

### Architecture

```text
Browser ←──WebSocket──→ API Gateway ──→ Lambda ($connect)
                                    ──→ Lambda ($default — message)
                                    ──→ Lambda ($disconnect)

Lambda ──→ DynamoDB (store/retrieve connectionIds)
Lambda ──→ ApiGatewayManagementApi (send message to specific connectionId)
```

### Built-in Routes

| Route | When invoked |
|---|---|
| `$connect` | Client establishes WebSocket connection |
| `$disconnect` | Client disconnects (cleanly or drops) |
| `$default` | Any message that does not match a custom route |

### $connect Lambda — Store Connection ID

```js
const { DynamoDBClient, PutItemCommand } = require('@aws-sdk/client-dynamodb');
const client = new DynamoDBClient({});

exports.handler = async (event) => {
  const { connectionId } = event.requestContext;

  await client.send(new PutItemCommand({
    TableName: process.env.CONNECTIONS_TABLE,
    Item: {
      connectionId: { S: connectionId },
      connectedAt: { S: new Date().toISOString() },
    },
  }));

  return { statusCode: 200 };
};
```

### $default Lambda — Broadcast to All Connections

```js
const { DynamoDBClient, ScanCommand, DeleteItemCommand } = require('@aws-sdk/client-dynamodb');
const { ApiGatewayManagementApiClient, PostToConnectionCommand } = require('@aws-sdk/client-apigatewaymanagementapi');

exports.handler = async (event) => {
  const body = JSON.parse(event.body);
  const { domainName, stage } = event.requestContext;
  const endpoint = `https://${domainName}/${stage}`;

  const dynamo = new DynamoDBClient({});
  const apigw = new ApiGatewayManagementApiClient({ endpoint });

  const { Items } = await dynamo.send(new ScanCommand({
    TableName: process.env.CONNECTIONS_TABLE,
  }));

  await Promise.all(Items.map(async ({ connectionId }) => {
    try {
      await apigw.send(new PostToConnectionCommand({
        ConnectionId: connectionId.S,
        Data: Buffer.from(JSON.stringify(body)),
      }));
    } catch (err) {
      if (err.$metadata?.httpStatusCode === 410) {
        // Stale connection — remove from DynamoDB
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

Status `410 Gone` means the client disconnected without triggering `$disconnect` (network drop). Delete the stale record to prevent accumulation.

### React Client with Native WebSocket

API Gateway WebSocket APIs use the native `WebSocket` browser API — no Socket.io client needed.

```js
// src/useWebSocket.js
import { useEffect, useRef, useState } from 'react';

export function useWebSocket(url) {
  const [messages, setMessages] = useState([]);
  const wsRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onmessage = (event) => {
      setMessages((prev) => [...prev, JSON.parse(event.data)]);
    };

    ws.onerror = (err) => console.error('WebSocket error:', err);

    return () => ws.close();
  }, [url]);

  const send = (data) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(data));
    }
  };

  return { messages, send };
}
```

---

## 7. Socket.io vs API Gateway WebSocket — Decision Guide

| Factor | Socket.io (persistent server) | API Gateway WebSocket + Lambda |
|---|---|---|
| Server required | Yes (EB, ECS, EC2) | No |
| Scalability | Limited by server count | Unlimited (AWS managed) |
| Reconnection | Built-in | Must implement client-side |
| Rooms/namespaces | Built-in | Must implement with DynamoDB |
| Message rate | High (in-memory routing) | Moderate (DynamoDB read on each message) |
| Cost model | Fixed server cost | Pay per connection-minute + message |
| Development complexity | Lower | Higher (three Lambda functions + DynamoDB) |

---

## 8. Exam and Interview Tips

1. **WebSocket upgrade uses HTTP 101** — The `101 Switching Protocols` status code is the upgrade acknowledgment. This is the only use of 101 in modern web development.

2. **Socket.io is not WebSocket** — Socket.io is a library built on top of WebSocket. A native WebSocket client cannot connect to a Socket.io server without the Socket.io protocol layer.

3. **`socket.off()` before disconnect** — Failing to remove event listeners is one of the most common Socket.io bugs. Always call `socket.off('eventName')` in the `useEffect` cleanup.

4. **API Gateway WebSocket `$connect` must return 200** — If the `$connect` Lambda returns any non-2xx status, the connection is refused. Do not throw uncaught errors in `$connect`.

5. **Status 410 Gone** — When `PostToConnectionCommand` returns 410, the client disconnected without triggering `$disconnect`. Delete the connectionId from DynamoDB.

6. **connectionId is ephemeral** — API Gateway generates a new `connectionId` for every connection. You cannot predict or reuse them. Always store in DynamoDB on `$connect` and remove on `$disconnect`.

7. **CORS applies to the WebSocket handshake** — Socket.io's `cors` option configures the HTTP handshake origin check. Omitting it causes the upgrade request to be blocked by the browser's CORS policy.

8. **`io.use()` runs before `connection`** — Middleware registered with `io.use()` is the correct place to authenticate WebSocket connections. Express `app.use()` middleware does not apply.

---

## 9. Study Checklist

Before moving to the lab, confirm you can answer yes to each item:

- [ ] I can explain the WebSocket upgrade handshake and what `101 Switching Protocols` means
- [ ] I know the difference between `io.emit()`, `socket.emit()`, and `socket.to(room).emit()`
- [ ] I know why the socket instance should be created in a separate module, not inside a React component
- [ ] I know what `socket.off()` does and why it must be called in `useEffect` cleanup
- [ ] I can describe what Socket.io rooms are and how to join and leave them
- [ ] I know how to authenticate a Socket.io connection using `io.use()` and `socket.handshake.auth`
- [ ] I can describe the three built-in API Gateway WebSocket routes and what each Lambda does
- [ ] I know why `410 Gone` from `PostToConnectionCommand` means the connectionId should be deleted
- [ ] I can explain when to choose Socket.io vs API Gateway WebSocket API

---

## 10. Supplemental Resources

The following free, open-access resources go deeper on Module 15 topics:

**1. Socket.io Official Documentation — Getting Started**
[https://socket.io/docs/v4/](https://socket.io/docs/v4/)
The official Socket.io v4 documentation covering server setup, client installation, event emission targets (`io.emit`, `socket.to`, `socket.broadcast`), rooms, namespaces, middleware, and the `io.use()` authentication pattern — the primary reference for all Socket.io patterns in Lab 15.

**2. MDN Web Docs — The WebSocket API**
[https://developer.mozilla.org/en-US/docs/Web/API/WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
The complete browser WebSocket API reference covering the `WebSocket` constructor, `readyState` values (`CONNECTING`, `OPEN`, `CLOSING`, `CLOSED`), `onmessage`, `onerror`, `onclose` handlers, and the `101 Switching Protocols` handshake — directly aligned to Section 1 of this guide and the native WebSocket client used with API Gateway.

**3. AWS Documentation — API Gateway WebSocket APIs**
[https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)
The official AWS reference for API Gateway WebSocket APIs covering the `$connect`, `$disconnect`, and `$default` routes, route selection expressions, Lambda integration, the `ApiGatewayManagementApi` for sending messages back to clients, connection management, and the `410 Gone` status code — covers all Section 6 concepts and the DVA-C02 WebSocket exam topics.

**4. Socket.io Documentation — Rooms**
[https://socket.io/docs/v4/rooms/](https://socket.io/docs/v4/rooms/)
The Socket.io official reference for rooms covering `socket.join()`, `socket.leave()`, `io.to(room).emit()`, `socket.to(room).emit()`, auto-generated socket ID rooms, and the difference between the sender-inclusive and sender-exclusive broadcast variants — directly reinforces Section 4 of this guide and the user-room notification pattern in Lab 15.
