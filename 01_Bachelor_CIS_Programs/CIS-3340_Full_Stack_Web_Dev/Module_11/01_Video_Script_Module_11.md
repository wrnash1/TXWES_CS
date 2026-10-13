# Video Script: Module 11 — Node.js and Express

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with Node project open, Terminal for npm commands, Postman or Thunder Client for API testing
- Use [SHOW CODE] for VS Code; [SHOW TERMINAL] for terminal; [SHOW BROWSER] for Postman/Thunder Client
- Have Node.js 18+ installed; verify with `node --version`
- Pre-create a blank project folder before recording

---

## Section 1: Introduction — The Node.js Runtime (0:00 – 2:30)

Welcome back. I'm Professor Nash, and this is Module 11 — Node.js and Express.

Up to this point in the course we have focused on the frontend: HTML, CSS, vanilla JavaScript, and React. Starting now we move to the backend — the server that responds to requests from your browser or mobile app.

Node.js is a JavaScript runtime built on Chrome's V8 engine that allows you to run JavaScript outside the browser. Before Node.js, if you wanted to write a web server, you had to use a different language — PHP, Python, Ruby, Java. Node.js changed that. Now you can use JavaScript for both the frontend and the backend, sharing code and skills across your full stack.

Node.js is non-blocking and event-driven. Instead of waiting for one operation to complete before starting the next — like reading a file or querying a database — Node.js uses callbacks, Promises, and async/await to handle many operations concurrently in a single thread. This makes it extremely efficient for I/O-heavy workloads like web APIs.

[PAUSE — slide: Node.js event loop diagram]

AWS Lambda functions can run Node.js. When you deploy a serverless API on AWS, the code you write in this module is exactly the kind of code that runs inside a Lambda function.

---

## Section 2: Node.js Core Modules (2:30 – 5:00)

Node.js ships with built-in core modules. You don't install them — you just require them.

[SHOW CODE]

```js
// http — create a basic web server without Express
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello from Node.js!');
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

Run this with `node server.js`. Visit `localhost:3000` and you see your response. This is raw Node.js — no framework.

The `http` module is powerful but verbose. You have to parse URL parameters manually, handle content types yourself, and write a lot of boilerplate for anything beyond the simplest responses. That is why Express exists.

Other commonly used core modules:

[SHOW CODE]

```js
// path — manipulate file paths cross-platform
const path = require('path');
const fullPath = path.join(__dirname, 'public', 'index.html');

// fs — read and write files
const fs = require('fs');
fs.readFile('./data.json', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(JSON.parse(data));
});

// fs/promises — same thing with async/await
const { readFile } = require('fs/promises');
const data = await readFile('./data.json', 'utf8');

// os — system information
const os = require('os');
console.log(os.platform(), os.cpus().length);
```

[PAUSE — slide: Node.js core modules overview]

---

## Section 3: npm and Package Management (5:00 – 6:30)

npm is Node's package manager. It ships with Node.js. Every Node project starts with `npm init`, which creates a `package.json` file.

[SHOW TERMINAL]

```bash
mkdir my-server && cd my-server
npm init -y
npm install express dotenv
npm install --save-dev nodemon
```

`package.json` is the manifest of your project — its name, version, scripts, and dependencies. `node_modules` contains the installed packages. Never commit `node_modules` to git.

Set up a `.gitignore`:

```
node_modules/
.env
```

Add a dev script in `package.json`:

[SHOW CODE]

```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  }
}
```

`nodemon` watches for file changes and automatically restarts the server during development. Use `npm run dev` during development, `npm start` in production.

[PAUSE — slide: package.json anatomy]

---

## Section 4: Express — First Server (6:30 – 9:30)

Express is a minimal, flexible web framework for Node.js. It adds routing, middleware, and a clean request/response API on top of Node's `http` module.

[SHOW CODE]

```js
// server.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware — parse JSON request bodies
app.use(express.json());

// Route — GET /
app.get('/', (req, res) => {
  res.status(200).json({ message: 'Hello from Express!' });
});

// Route — GET /health
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Every route takes three pieces: the HTTP method (`get`, `post`, `put`, `delete`), the path, and a handler function. The handler receives the `req` (request) object and `res` (response) object.

[PAUSE — slide: Express route anatomy]

The request object carries everything the client sent: `req.params` for URL parameters, `req.query` for query string parameters, `req.body` for the JSON body, and `req.headers` for HTTP headers.

[SHOW CODE]

```js
// URL params: GET /api/users/42
app.get('/api/users/:id', (req, res) => {
  console.log(req.params.id);   // '42' (string)
  console.log(req.params);      // { id: '42' }
});

// Query params: GET /api/users?page=2&limit=10
app.get('/api/users', (req, res) => {
  console.log(req.query.page);  // '2'
  console.log(req.query.limit); // '10'
});

// Body: POST /api/users with JSON body
app.post('/api/users', (req, res) => {
  console.log(req.body); // { name: 'Alice', email: 'alice@example.com' }
});
```

---

## Section 5: Routing (9:30 – 12:00)

As your application grows, keeping all routes in `server.js` becomes unwieldy. Express Router lets you organize routes into separate files.

[SHOW CODE]

```js
// routes/users.js
const { Router } = require('express');
const router = Router();

// In-memory data for now
let users = [
  { id: 1, name: 'Alice Johnson', email: 'alice@txwes.edu' },
  { id: 2, name: 'Bob Martinez', email: 'bob@txwes.edu' },
];

router.get('/', (req, res) => {
  res.status(200).json(users);
});

router.get('/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.status(200).json(user);
});

router.post('/', (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) return res.status(400).json({ error: 'name and email required' });

  const newUser = { id: Date.now(), name, email };
  users.push(newUser);
  res.status(201)
    .set('Location', `/api/users/${newUser.id}`)
    .json(newUser);
});

router.delete('/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = users.findIndex(u => u.id === id);
  if (index === -1) return res.status(404).json({ error: 'User not found' });
  users.splice(index, 1);
  res.status(204).send();
});

module.exports = router;
```

Mount the router in `server.js`:

[SHOW CODE]

```js
// server.js
const usersRouter = require('./routes/users');
app.use('/api/users', usersRouter);
```

Now GET `/api/users` hits the router's `get('/')` handler, and GET `/api/users/42` hits `get('/:id')`.

[PAUSE — slide: Router file structure diagram]

---

## Section 6: Middleware (12:00 – 15:30)

Middleware is a function with signature `(req, res, next)` that runs before your route handler. Middleware can read and modify `req` and `res`, execute any code, end the response, or call `next()` to pass control to the next middleware in the chain.

[PAUSE — slide: Middleware pipeline diagram]

[SHOW CODE]

```js
// Custom request logger middleware
function requestLogger(req, res, next) {
  const start = Date.now();
  res.on('finish', () => {
    console.log(`${req.method} ${req.path} ${res.statusCode} ${Date.now() - start}ms`);
  });
  next();
}

app.use(requestLogger);
```

`app.use(fn)` registers middleware that runs for every request. The order you register middleware matters — it runs top to bottom.

[SHOW CODE]

```js
// app.use order matters
app.use(express.json());      // 1. Parse JSON body
app.use(requestLogger);        // 2. Log the request
app.use('/api', apiRouter);    // 3. Route to handlers
app.use(notFoundHandler);      // 4. 404 for unmatched routes
app.use(errorHandler);         // 5. Catch errors
```

Route-level middleware runs only for specific routes:

[SHOW CODE]

```js
// requireAuth runs only before these specific routes
app.get('/api/profile', requireAuth, (req, res) => {
  res.json(req.user);
});

// Or apply to all routes in a router
router.use(requireAuth);
```

Third-party middleware packages extend Express significantly.

[SHOW CODE]

```bash
npm install cors helmet morgan
```

[SHOW CODE]

```js
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

app.use(helmet());              // Security headers
app.use(cors({ origin: 'http://localhost:5173' })); // Allow React dev server
app.use(morgan('dev'));         // HTTP request logging
```

[PAUSE — slide: Commonly used Express middleware]

---

## Section 7: Request/Response Cycle (15:30 – 17:30)

Let me trace exactly what happens from the moment a browser sends a request to when it receives a response.

[PAUSE — slide: Request/response cycle diagram — numbered steps]

Step one: the client sends an HTTP request — method, URL, headers, optional body.

Step two: Express matches the method and path against registered routes. Middleware registered with `app.use` runs first, in order.

Step three: the matching route handler runs. It accesses `req.body`, `req.params`, `req.query`.

Step four: the handler builds a response and calls `res.json()`, `res.send()`, or `res.status().json()`.

Step five: Express serializes the response and sends it back to the client with the appropriate status code and headers.

[SHOW CODE]

```js
// A complete round-trip example
router.post('/', async (req, res, next) => {
  try {
    // Validate
    const { name, email } = req.body;
    if (!name || !email) {
      return res.status(400).json({
        error: 'Validation failed',
        details: { name: !name ? 'required' : null, email: !email ? 'required' : null },
      });
    }

    // Process (in real apps: query database)
    const newUser = { id: Date.now(), name, email, createdAt: new Date().toISOString() };

    // Respond
    res.status(201)
      .set('Location', `/api/users/${newUser.id}`)
      .json(newUser);
  } catch (err) {
    next(err); // Forward to error-handling middleware
  }
});
```

---

## Section 8: Error Handling (17:30 – 20:30)

Express has a special error-handling middleware with four parameters: `(err, req, res, next)`. Register it last in your middleware chain.

[SHOW CODE]

```js
// 404 handler — catches requests that matched no route
app.use((req, res) => {
  res.status(404).json({
    error: 'Not found',
    path: req.path,
    method: req.method,
  });
});

// Error handler — catches errors forwarded with next(err)
app.use((err, req, res, next) => {
  const status = err.status || err.statusCode || 500;
  const message = status < 500 ? err.message : 'Internal Server Error';

  console.error(`[ERROR] ${req.method} ${req.path} — ${err.message}`);
  if (status === 500) console.error(err.stack);

  res.status(status).json({
    error: message,
    code: err.code || 'SERVER_ERROR',
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack }),
  });
});
```

Define custom error classes for clean error propagation:

[SHOW CODE]

```js
// utils/errors.js
class AppError extends Error {
  constructor(message, status, code) {
    super(message);
    this.status = status;
    this.code = code;
  }
}

class NotFoundError extends AppError {
  constructor(resource) {
    super(`${resource} not found`, 404, 'NOT_FOUND');
  }
}

class ValidationError extends AppError {
  constructor(message) {
    super(message, 400, 'VALIDATION_ERROR');
  }
}

module.exports = { AppError, NotFoundError, ValidationError };
```

[SHOW CODE]

```js
// Route using custom errors
const { NotFoundError, ValidationError } = require('../utils/errors');

router.get('/:id', async (req, res, next) => {
  try {
    const user = await db.findById(req.params.id);
    if (!user) throw new NotFoundError('User');
    res.json(user);
  } catch (err) {
    next(err);
  }
});
```

The error flows through `next(err)` to the error handler, which sets the appropriate status code and sends a consistent JSON error response.

[PAUSE — slide: Error handling middleware chain]

---

## Section 9: REST API Structure (20:30 – 22:30)

A well-structured Express project follows these conventions.

[PAUSE — slide: Project folder structure]

```
my-api/
├── server.js          ← App entry point; listen only
├── app.js             ← Express app setup; middleware; routes
├── routes/
│   ├── users.js
│   └── products.js
├── controllers/       ← Handler logic (for larger apps)
│   └── usersController.js
├── middleware/
│   ├── auth.js
│   └── validate.js
├── utils/
│   └── errors.js
├── .env
├── .gitignore
└── package.json
```

Separating `app.js` from `server.js` is important for testing — your test suite can import `app.js` without starting a real server.

[SHOW CODE]

```js
// app.js — configure app, do not call listen()
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const usersRouter = require('./routes/users');

const app = express();
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use('/api/users', usersRouter);
app.use((req, res) => res.status(404).json({ error: 'Not found' }));
app.use((err, req, res, next) => { /* error handler */ });

module.exports = app;

// server.js — only starts the server
const app = require('./app');
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on ${PORT}`));
```

---

## Conclusion (22:30 – 24:00)

Here is the summary for Module 11.

- Node.js runs JavaScript on the server using the V8 engine and a non-blocking event loop.
- Core modules like `http`, `path`, and `fs` are available without installing anything.
- npm manages packages — `package.json` is the manifest, `node_modules` is never committed.
- Express adds routing and middleware on top of Node's `http` module.
- `req.params`, `req.query`, and `req.body` carry client data to handlers.
- Middleware runs in order — parse body, log, auth, route, 404, error handler.
- Error-handling middleware has four parameters `(err, req, res, next)` and is registered last.
- Separate `app.js` from `server.js` for testability.

For the AWS Developer Associate exam, Lambda functions running Node.js use the same async/await patterns and handler signature you are learning here. The exam tests how to configure Lambda's environment variables, memory, timeout, and trigger events — all concepts that build on understanding the Node.js runtime.

Your lab this week builds a complete Express REST API for a university registrar system. See you in Module 12 where we add authentication with JWT and bcrypt.

[END OF SCRIPT]
