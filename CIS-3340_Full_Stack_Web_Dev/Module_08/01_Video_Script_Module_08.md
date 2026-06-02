# Video Script: Module 08 - Server-Side Routing & Middleware

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 21 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with multiple open files (routes/, middleware/ folders visible)
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for Postman/browser; [SHOW TERMINAL] for command-line output
- Demonstrate the refactor live — start with a single-file server and split it into the router structure during the recording

---

## Section 1: Introduction - From One File to Many [00:00 - 03:30]

Welcome to Module 08. I am Professor Nash. Last module you built a working Express server — all routes and middleware in a single `index.js` file. That works fine for five routes. It does not work for fifty.

This module is about organization. We will learn two things: how to use Express Router to split routes into separate files, and how to build reusable custom middleware. These are the patterns that production Node.js applications actually use.

[SHOW CODE]

Here is the `index.js` from Module 07. Five routes, two middleware functions, 80 lines. Now imagine this is a real API: users, products, orders, reviews, categories, shipping, payments. That is sixty or seventy routes in one file. Three developers editing it simultaneously produce merge conflicts. Someone adds a route for products in the users section. Nobody can find the authentication check. This is the monolith problem.

The solution is Express Router. Each resource gets its own file. `index.js` becomes an orchestration layer — it initializes the app, registers global middleware, and mounts the routers.

**AWS Exam Tip:** AWS Lambda functions follow the same single-responsibility principle that Express Router enforces. A Lambda function should do one thing well. A single Lambda handling sixty different operations is as problematic as a sixty-route `index.js`. In Module 14 when we deploy to API Gateway, each route group can optionally map to a separate Lambda — understanding Express Router now prepares you for that architecture decision.

---

## Section 2: Express Router [03:30 - 09:00]

[SHOW CODE]

`express.Router()` creates a mini-application capable of handling routes and middleware. Think of it as a sub-application that you mount at a path prefix.

Create a `routes/` folder. Inside it, create `books.js`:

```javascript
const express = require('express');
const router = express.Router();

let books = [
  { id: 1, title: 'Clean Code', author: 'Robert C. Martin', year: 2008 },
  { id: 2, title: 'The Pragmatic Programmer', author: 'Hunt & Thomas', year: 1999 }
];
let nextId = 3;

// GET /api/books
router.get('/', (req, res) => {
  res.status(200).json(books);
});

// GET /api/books/:id
router.get('/:id', (req, res) => {
  const book = books.find(b => b.id === parseInt(req.params.id));
  if (!book) return res.status(404).json({ error: 'Book not found', code: 'BOOK_NOT_FOUND' });
  res.status(200).json(book);
});

// POST /api/books
router.post('/', (req, res) => {
  const { title, author, year } = req.body;
  if (!title || !author) {
    return res.status(400).json({ error: 'title and author are required' });
  }
  const newBook = { id: nextId++, title, author, year };
  books.push(newBook);
  res.status(201).set('Location', `/api/books/${newBook.id}`).json(newBook);
});

// PUT /api/books/:id
router.put('/:id', (req, res) => {
  const index = books.findIndex(b => b.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'Book not found' });
  books[index] = { id: parseInt(req.params.id), ...req.body };
  res.status(200).json(books[index]);
});

// DELETE /api/books/:id
router.delete('/:id', (req, res) => {
  const index = books.findIndex(b => b.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'Book not found' });
  books.splice(index, 1);
  res.status(204).send();
});

module.exports = router;
```

Notice: the router uses `/` and `/:id` — not `/api/books` and `/api/books/:id`. The prefix is attached when you mount the router in `index.js`.

Now update `index.js`:

```javascript
const express = require('express');
const booksRouter = require('./routes/books');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Mount the books router at /api/books
app.use('/api/books', booksRouter);

// 404 and error handlers
app.use((req, res) => {
  res.status(404).json({ error: `${req.method} ${req.path} not found` });
});

app.use((err, req, res, next) => {
  res.status(err.status || 500).json({ error: err.message || 'Internal server error' });
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

`index.js` is now 22 lines. When you add a users resource, you create `routes/users.js` and add one line to `index.js`. The pattern scales without ever touching existing route files.

---

## Section 3: Custom Middleware [09:00 - 14:00]

[SHOW CODE]

Custom middleware functions are regular JavaScript functions registered with `app.use()`. They follow the three-parameter signature `(req, res, next)`.

Create a `middleware/` folder. Start with a request logger:

```javascript
// middleware/logger.js
const requestLogger = (req, res, next) => {
  const start = Date.now();
  const timestamp = new Date().toISOString();

  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`[${timestamp}] ${req.method} ${req.path} ${res.statusCode} ${duration}ms`);
  });

  next();
};

module.exports = requestLogger;
```

This version uses the `finish` event on the response to log the status code and duration after the response is sent — more informative than logging before the route handler runs.

Register it in `index.js`:

```javascript
const requestLogger = require('./middleware/logger');
app.use(requestLogger);
```

Now add a validation middleware factory — a function that returns a middleware function. This pattern creates reusable validators parameterized by field lists:

```javascript
// middleware/validate.js
const requireFields = (fields) => {
  return (req, res, next) => {
    const missing = fields.filter(f => !req.body[f]);
    if (missing.length > 0) {
      return res.status(400).json({
        error: 'Validation failed',
        code: 'MISSING_REQUIRED_FIELDS',
        details: missing.map(f => ({ field: f, message: `${f} is required` }))
      });
    }
    next();
  };
};

module.exports = { requireFields };
```

Use it in the books router:

```javascript
const { requireFields } = require('../middleware/validate');

router.post('/', requireFields(['title', 'author']), (req, res) => {
  // req.body.title and req.body.author are guaranteed to exist here
  const newBook = { id: nextId++, ...req.body };
  books.push(newBook);
  res.status(201).set('Location', `/api/books/${newBook.id}`).json(newBook);
});
```

By placing the validation middleware in the route definition as a second argument, the validation runs before the route handler. The route handler is only called if all required fields are present.

**AWS Exam Tip:** This middleware factory pattern is exactly how JWT authentication middleware works in Module 13. A single `authenticate` middleware function is applied to every protected route — and in AWS, it mirrors how a Lambda Authorizer works: a separate function that validates a token before the main Lambda executes.

---

## Section 4: CORS Middleware [14:00 - 17:30]

[SHOW BROWSER]

When your React front-end on `http://localhost:3000` sends a fetch request to your Express API on `http://localhost:5000`, the browser blocks it. This is the Same-Origin Policy — a browser security mechanism. The server must explicitly permit cross-origin requests by sending CORS headers.

[SHOW CODE]

Install the `cors` package:

```bash
npm install cors
```

The simplest configuration — allow all origins (use this only in development):

```javascript
const cors = require('cors');
app.use(cors());
```

This adds `Access-Control-Allow-Origin: *` to every response. For production, restrict this to your actual frontend origin:

```javascript
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:3000',
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

CORS must be registered before your route handlers — it is middleware that adds response headers. A common mistake is registering CORS after routes, which means some responses go out without the headers.

The preflight request: browsers send an `OPTIONS` request before a cross-origin POST, PUT, or DELETE to check if the server permits it. The `cors()` middleware handles OPTIONS requests automatically, responding with the correct headers.

**AWS Exam Tip:** AWS API Gateway has its own CORS configuration separate from your Lambda function. When you deploy to API Gateway in Module 14, you will configure CORS at the API Gateway level — not in Express. For local development, your Express CORS middleware handles it. Do not forget to configure both.

---

## Section 5: Route Parameters and Lab Preview [17:30 - 21:00]

[SHOW CODE]

A quick look at nested routes and query parameter filtering — two patterns the lab uses.

Nested resource: `GET /api/books/:bookId/reviews` — get all reviews for a specific book:

```javascript
// In routes/books.js
router.get('/:bookId/reviews', (req, res) => {
  const bookId = parseInt(req.params.bookId);
  const book = books.find(b => b.id === bookId);
  if (!book) return res.status(404).json({ error: 'Book not found' });

  const bookReviews = reviews.filter(r => r.bookId === bookId);
  res.status(200).json(bookReviews);
});
```

Query parameter filtering: `GET /api/books?author=Martin&year=2008`:

```javascript
router.get('/', (req, res) => {
  let result = [...books];
  const { author, year } = req.query;

  if (author) {
    result = result.filter(b =>
      b.author.toLowerCase().includes(author.toLowerCase())
    );
  }
  if (year) {
    result = result.filter(b => b.year === parseInt(year));
  }

  res.status(200).json(result);
});
```

In the lab this week you will refactor the Module 07 single-file server into the full router structure: move the books routes into `routes/books.js`, extract the logger into `middleware/logger.js`, create the `requireFields` validation middleware, add a `routes/authors.js` router, and configure CORS. This is the architecture you will use for every project from here forward.

Thank you for watching. See you in Module 09 where we replace the in-memory array with a real PostgreSQL database.

---

## Additional Resources

- developer.mozilla.org — search "Express routing" and "CORS" for the complete reference
- aws.amazon.com/certification — review API Gateway CORS configuration in the developer documentation
