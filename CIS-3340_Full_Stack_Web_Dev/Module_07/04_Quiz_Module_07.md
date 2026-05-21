# Quiz: Module 07 - Node.js & Express Server
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which code snippet correctly initializes a basic Express application instance?
*   A) `const app = express()`
*   B) `const app = new express.App()`
*   C) `const app = require('express').start()`
*   D) `const app = Express.init()`
*   **Correct Answer:** A) `const express = require('express'); const app = express();` — calling the required `express` module as a function returns a new application instance.
*   **Distractor Analysis:**
    *   *Why A is correct:* The `express` module exports a factory function — invoking it with `express()` creates and returns the application object.
    *   *Why B is incorrect:* `express.App` is not a class — Express does not use `new` for instantiation.
    *   *Why C is incorrect:* The Express module does not expose a `.start()` method — calling an Express app as a function is the correct pattern.
    *   *Why D is incorrect:* `Express.init()` is not a valid Express API — `express` is lowercase and called as a function, not a static initializer.

---

**Question 2**
Which of the following is the most accurate definition of **server setup** in an Express application?
*   A) The process of provisioning an AWS EC2 instance, attaching an Elastic IP address, and configuring SSH key pairs for remote access.
*   B) Initializing an Express application, configuring global middleware (such as body parsing and CORS), defining route handlers, and calling `app.listen()` to bind the server to a network port.
*   C) The process of containerizing a Node.js application with Docker, building an image, and pushing it to Amazon ECR for deployment to ECS.
*   D) The configuration of IAM roles and security groups that control which AWS services an EC2 instance can access at runtime.
*   **Correct Answer:** B) Initializing an Express application, configuring global middleware (such as body parsing and CORS), defining route handlers, and calling `app.listen()` to bind the server to a network port.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes EC2 instance provisioning — an AWS infrastructure task, not Express server setup.
    *   *Why B is correct:* Server setup in Express involves the code-level steps of creating the app, registering middleware, defining routes, and starting the listener.
    *   *Why C is incorrect:* This describes Docker containerization and ECR deployment — a CI/CD and container concept, not Express server setup.
    *   *Why D is incorrect:* This describes AWS IAM and security group configuration — cloud access control, not application-level server setup.

---

**Question 3**
A developer needs to start an Express server so it automatically restarts whenever a source file is saved during development. Which command enables this behavior?
*   A) `node index.js`
*   B) `nodemon index.js`
*   C) `npm start --watch`
*   D) `pm2 start index.js`
*   **Correct Answer:** B) `nodemon index.js` — `nodemon` is a development tool that monitors the project directory for file changes and automatically restarts the Node.js process, eliminating the need to manually stop and restart during development.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `node index.js` starts the server once but does not watch for file changes — the server must be manually restarted after each edit.
    *   *Why B is correct:* `nodemon` is the standard development-time auto-restart tool for Node.js applications (installed with `npm install -g nodemon`).
    *   *Why C is incorrect:* `npm start --watch` is not a standard npm CLI flag — `--watch` support depends on the specific script defined in `package.json`.
    *   *Why D is incorrect:* `pm2` is a production process manager that provides clustering and persistence — it is not intended for development-time file watching.

---

**Question 4**
An Express server running on an EC2 instance is unreachable from the internet even though the application is listening on port 3000. What is the most likely cause?
*   A) Node.js cannot listen on ports above 1024 without superuser privileges.
*   B) The EC2 instance's security group does not have an inbound rule allowing TCP traffic on port 3000 from the internet.
*   C) Express requires a valid SSL certificate before it will accept inbound connections.
*   D) `app.listen()` must be called with `'0.0.0.0'` as the host to accept external connections — using no host argument only binds to `127.0.0.1`.
*   **Correct Answer:** B) The EC2 instance's security group does not have an inbound rule allowing TCP traffic on port 3000 from the internet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Node.js can listen on any port above 1024 without elevated privileges — ports below 1024 require root on Linux, but 3000 does not.
    *   *Why B is correct:* AWS security groups act as instance-level firewalls. A new EC2 instance blocks all inbound traffic by default — port 3000 must be explicitly allowed in the inbound rules.
    *   *Why C is incorrect:* Express does not require SSL to accept connections — HTTPS is optional and configured separately.
    *   *Why D is incorrect:* When `app.listen(3000)` is called without a host, Node.js binds to all available network interfaces (`0.0.0.0`) by default — this is not the cause of the connection failure.

---

**Question 5**
A Node.js/Express API processes incoming POST requests but the `req.body` object is always `undefined`. What is the most likely fix?
*   A) Add `Content-Type: text/plain` as a request header instead of `application/json`.
*   B) Register the `express.json()` middleware before the route handlers — without it, Express does not parse incoming JSON request bodies.
*   C) Change the route from `app.post()` to `app.get()` since `req.body` is only populated on GET requests.
*   D) Set `app.enable('body-parser')` in the Express configuration to activate the built-in body parsing feature.
*   **Correct Answer:** B) Register the `express.json()` middleware before the route handlers — without it, Express does not parse incoming JSON request bodies.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Changing to `text/plain` would make the body a raw string, not a parsed object — and `req.body` would still be undefined without body-parsing middleware.
    *   *Why B is correct:* `app.use(express.json())` registers the built-in JSON body parser as global middleware. Without it, Express passes the raw request stream to route handlers and `req.body` remains `undefined`.
    *   *Why C is incorrect:* `req.body` is populated for POST, PUT, and PATCH requests — not GET requests, which have no body.
    *   *Why D is incorrect:* `app.enable('body-parser')` is not a valid Express configuration option — body parsing middleware must be explicitly registered with `app.use()`.
