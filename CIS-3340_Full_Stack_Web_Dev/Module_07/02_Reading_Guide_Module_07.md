# Reading Guide: Module 07 - Node.js & Express Server
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 07 - Node.js & Express Server**! This module introduces Node.js — the JavaScript runtime that allows you to run JavaScript outside the browser as a server-side platform — and Express.js, the minimal web framework used to build RESTful APIs on top of Node. You will learn how Node's event loop enables non-blocking I/O, how npm manages dependencies, and how to build a basic HTTP server with routing. The patterns you learn here apply directly to AWS Lambda (which runs Node.js functions), Elastic Beanstalk deployments, and EC2-hosted Express applications.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Node event loop**: Node.js's concurrency model that allows a single-threaded JavaScript process to handle thousands of simultaneous I/O operations (file reads, database queries, HTTP requests) without blocking. When an async operation is initiated (e.g., reading a file), Node registers a callback and continues processing other requests. The event loop continuously checks the callback queue and executes callbacks when the call stack is empty — enabling high throughput without threads.
*   **Package manager (npm)**: The Node Package Manager; the default registry and CLI tool for managing JavaScript packages and project dependencies. `npm init` creates a `package.json` manifest; `npm install <package>` downloads and registers a dependency; `npm run <script>` executes scripts defined in `package.json`. npm is also used to install global tools like `nodemon` (auto-restart on file change) and `pm2` (production process manager).
*   **Express framework**: A minimal, unopinionated Node.js web framework that wraps Node's built-in `http` module and adds routing, middleware support, request/response helpers, and error handling. An Express application is created with `const app = express()`, routes are defined with `app.get()`, `app.post()`, etc., and the server starts listening with `app.listen(port)`.
*   **Server setup**: The process of initializing an Express application, configuring global middleware (body parsing, CORS, logging), defining route handlers, and calling `app.listen(PORT)` to bind the server to a TCP port. Best practices include loading the port from environment variables (`process.env.PORT`), gracefully handling uncaught exceptions, and separating route definitions from the main application entry point.
*   **Listening sockets**: The TCP socket connections maintained by a Node.js HTTP server via `server.listen(port, host)`. When a client connects on the specified port, Node accepts the connection and processes the HTTP request. Understanding ports is essential for AWS deployments — EC2 security groups must allow inbound traffic on the application's listening port (commonly 3000, 8080, or 443).

---

### 2. Certification Exam Tips
*   **DVA-C02 Tests Node.js Lambda Handlers:** AWS Lambda natively supports Node.js runtimes (Node 18.x, 20.x). The exam tests the structure of a Lambda handler — `exports.handler = async (event, context) => { ... }` — and how the `event` object carries the API Gateway request payload. Understanding how Express route handlers process `req`/`res` objects directly translates to understanding Lambda event handling.
*   **Environment Variables on AWS:** Node.js reads environment variables via `process.env.VARIABLE_NAME`. On AWS Lambda, environment variables are set in the function configuration; on EC2 and Elastic Beanstalk, they are set in the instance or environment configuration. Never hard-code credentials or configuration values in source code — always use `process.env` and AWS Secrets Manager or Parameter Store.
*   **Study Resource:** The official Node.js documentation and the Express.js getting-started guide are the authoritative references. [Full Stack Open — Part 3: Node.js and Express](https://fullstackopen.com/en/part3) walks through building a REST API backend step-by-step and is directly relevant to this module's lab.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 3 covering **Node.js and Express** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3) — this section builds a fully functional REST API backend.
*   **Required Video:** Watch the Node.js and Express section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering server initialization, routing, and middleware.

---

### Lab & Command Integration
In this week's hands-on lab, you will build a basic Express server from scratch:
*   **Initialize npm package settings**: Run `npm init -y` in your project directory to create a `package.json` file, then install Express with `npm install express`.
*   **Create base Express routing script file**: Create an `index.js` file, require Express, define at least two routes (`GET /` and `GET /api/items`), and return JSON responses using `res.json()`.
*   **Listen to connections on port 3000**: Call `app.listen(3000, () => console.log('Server running on port 3000'))` and verify the server responds correctly by opening `http://localhost:3000` in the browser or using `curl http://localhost:3000`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 3 covering **Node.js and Express** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3).
- [ ] Watch the Node.js and Express section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Install Node.js LTS from [nodejs.org](https://nodejs.org/) if not already installed — verify with `node -v` and `npm -v` in your terminal.
- [ ] Proceed to the weekly hands-on lab activity.
