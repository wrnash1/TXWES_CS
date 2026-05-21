# Online Course Map
## CIS-3340 – Full Stack Web Development
### 16-Week Schedule | Texas Wesleyan University

---

## Course Phases Overview

| Phase | Weeks | Focus Area | Core Technology |
|-------|-------|-----------|----------------|
| Phase 1: Web Foundations | 1–3 | HTML, CSS, Responsive Design | HTML5, CSS3, Flexbox/Grid |
| Phase 2: JavaScript & React | 4–5 | DOM, Async JS, React UI | JavaScript ES6+, React |
| Phase 3: Backend Development | 6–8 | REST APIs, Node.js, Databases | Node.js, Express, PostgreSQL |
| Phase 4: AWS Cloud Services | 9–12 | Cloud Fundamentals, Serverless | AWS EC2, S3, Lambda, DynamoDB |
| Phase 5: DevOps & Certification | 13–16 | CI/CD, Containers, Monitoring, Exam Prep | AWS CodePipeline, Docker, CloudWatch |

---

## Week-by-Week Schedule

---

### Phase 1 — Web Foundations (Weeks 1–3)

#### Week 1 | Module 01 — Web Development Overview: HTML5 Semantics & SEO
**Learning Objectives:**
- Explain the role of semantic HTML5 elements in document structure and SEO
- Apply WCAG accessibility guidelines to HTML markup
- Validate an HTML document using the W3C Nu HTML Checker

**Deliverables:**
- Quiz 01 (Canvas, due Sunday)
- Lab 01: Semantic HTML page with validated markup (GitHub URL, due Sunday)
- Discussion 01: What makes a website accessible? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** HTML5, VS Code, Git, W3C Validator

---

#### Week 2 | Module 02 — Modern CSS Layouts: Flexbox & Grid
**Learning Objectives:**
- Build one-dimensional layouts using CSS Flexbox
- Build two-dimensional layouts using CSS Grid
- Apply the CSS box model to control element sizing and spacing

**Deliverables:**
- Quiz 02 (Canvas, due Sunday)
- Lab 02: Flexbox card grid + CSS Grid dashboard layout (GitHub URL, due Sunday)

**Technologies Introduced:** CSS Flexbox, CSS Grid, Chrome DevTools Layout panel

---

#### Week 3 | Module 03 — Responsive Design
**Learning Objectives:**
- Implement a mobile-first responsive stylesheet using `@media` queries
- Configure the viewport meta tag for correct mobile rendering
- Use relative CSS units (`rem`, `vw`, `%`) for fluid layouts

**Deliverables:**
- Quiz 03 (Canvas, due Sunday)
- Lab 03: Mobile-first responsive landing page tested at 375px, 768px, 1280px (GitHub URL, due Sunday)
- Discussion 02: Mobile-first vs. desktop-first — which approach do you prefer and why? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** CSS Media Queries, Viewport Meta Tag, Chrome DevTools Device Toolbar

---

### Phase 2 — JavaScript & React (Weeks 4–5)

#### Week 4 | Module 04 — JavaScript for the Web: DOM and Events
**Learning Objectives:**
- Query and manipulate DOM nodes using `querySelector` and `querySelectorAll`
- Attach and remove event listeners for user interaction events
- Describe event bubbling and implement event delegation for dynamic lists

**Deliverables:**
- Quiz 04 (Canvas, due Sunday)
- Lab 04: Dynamic to-do list with DOM manipulation and event listeners (GitHub URL, due Sunday)

**Technologies Introduced:** Browser DOM API, JavaScript Event Model, Chrome DevTools Console

---

#### Week 5 | Module 05 — Asynchronous JavaScript
**Learning Objectives:**
- Explain the call stack, event loop, and callback queue model
- Write and consume Promises using `.then()` and `.catch()`
- Refactor Promise chains to `async`/`await` with `try`/`catch` error handling

**Deliverables:**
- Quiz 05 (Canvas, due Sunday)
- Lab 05: `fetch()` API client consuming a public REST API, rendered to the DOM with async/await (GitHub URL, due Sunday)
- Discussion 03: What is the difference between synchronous and asynchronous code? Describe a real-world scenario where this matters. (post by Wednesday, responses by Sunday)

**Technologies Introduced:** JavaScript Promises, Fetch API, async/await, try/catch

---

### Phase 3 — Backend Development (Weeks 6–8)

#### Week 6 | Module 06 — Node.js and Express: RESTful APIs
**Learning Objectives:**
- Map HTTP verbs to CRUD operations following REST conventions
- Identify the correct HTTP status codes for common API responses
- Design clean resource-oriented URL patterns for a REST API

**Deliverables:**
- Quiz 06 (Canvas, due Sunday)
- Lab 06: REST API route table for a `products` resource + Postman test screenshots (GitHub URL, due Sunday)

**Technologies Introduced:** REST Architecture, HTTP Status Codes, Postman

---

#### Week 7 | Module 07 — Node.js & Express Server
**Learning Objectives:**
- Initialize a Node.js project with `npm init` and install Express
- Define route handlers for GET and POST endpoints
- Configure body parsing middleware and environment variables

**Deliverables:**
- Quiz 07 (Canvas, due Sunday)
- Lab 07: Express server with at least 4 routes, nodemon dev setup, and PM2 production start (GitHub URL, due Sunday)
- Discussion 04: Compare a traditional server-hosted backend (Express on EC2) to serverless functions (AWS Lambda). When would you choose each? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** Node.js, Express.js, npm, nodemon, PM2

---

#### Week 8 | Module 08 — Databases: SQL with PostgreSQL
**Learning Objectives:**
- Design a relational database schema with PRIMARY KEY and FOREIGN KEY constraints
- Write SQL INSERT, SELECT, UPDATE, and DELETE statements
- Perform INNER JOIN queries to retrieve relational data across tables

**Deliverables:**
- Quiz 08 (Canvas, due Sunday)
- Lab 08: PostgreSQL schema with two related tables, seed data, and JOIN query results (GitHub URL, due Sunday)

**Technologies Introduced:** PostgreSQL, SQL DDL/DML, pgAdmin or psql CLI

---

### Phase 4 — AWS Cloud Services (Weeks 9–12)

#### Week 9 | Module 09 — NoSQL with MongoDB and Mongoose
**Learning Objectives:**
- Connect a Node.js application to MongoDB using Mongoose
- Define Mongoose schemas with validation rules and compile models
- Perform CRUD operations using Mongoose model methods

**Deliverables:**
- Quiz 09 (Canvas, due Sunday)
- Lab 09: Mongoose-connected Express API with User model CRUD endpoints (GitHub URL, due Sunday)
- Discussion 05: When would you choose MongoDB over PostgreSQL for a project? What are the trade-offs? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** MongoDB Atlas, Mongoose ODM, NoSQL document model

---

#### Week 10 | Module 10 — Authentication: JWT and OAuth 2.0
**Learning Objectives:**
- Hash passwords with bcrypt before database storage
- Generate and verify JSON Web Tokens using `jsonwebtoken`
- Configure CORS middleware in Express for cross-origin API access

**Deliverables:**
- Quiz 10 (Canvas, due Sunday)
- Lab 10: Express authentication API with `/register` (bcrypt), `/login` (JWT issue), and protected route (JWT verify middleware) (GitHub URL, due Sunday)

**Technologies Introduced:** bcrypt, jsonwebtoken, cors npm package, JWT.io

---

#### Week 11 | Module 11 — AWS Core Services: EC2, S3, IAM
**Learning Objectives:**
- Deploy a React production build to an S3 static website hosting bucket
- Launch an EC2 t2.micro instance and connect via SSH
- Configure security group inbound rules for HTTP and SSH access

**Deliverables:**
- Quiz 11 (Canvas, due Sunday)
- Lab 11: React app deployed to S3 (live URL) + Express app running on EC2 (public IP) (deployed URLs, due Sunday)
- Discussion 06: Describe the AWS Shared Responsibility Model. What is AWS responsible for vs. what is the developer responsible for? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** AWS S3, AWS EC2, AWS IAM, AWS CLI, CloudFront

---

#### Week 12 | Module 12 — AWS Lambda and Serverless Architecture
**Learning Objectives:**
- Write an AWS Lambda function handler in Node.js with correct event/context signatures
- Deploy a Lambda function manually via the console and via the AWS CLI
- Connect Lambda to API Gateway to serve HTTP requests without a traditional server

**Deliverables:**
- Quiz 12 (Canvas, due Sunday)
- Lab 12: Serverless REST API — 3 Lambda functions (GET list, GET by ID, POST create) connected to API Gateway endpoints (test URL, due Sunday)

**Technologies Introduced:** AWS Lambda, AWS API Gateway, AWS SAM (intro), serverless architecture

---

### Phase 5 — DevOps & Certification (Weeks 13–16)

#### Week 13 | Module 13 — AWS API Gateway and DynamoDB
**Learning Objectives:**
- Create a DynamoDB table with a partition key and perform CRUD via the AWS SDK v3
- Connect Lambda functions to DynamoDB using IAM execution roles
- Configure API Gateway CORS settings for a React front-end consumer

**Deliverables:**
- Quiz 13 (Canvas, due Sunday)
- Lab 13: Full serverless CRUD — React → API Gateway → Lambda → DynamoDB (deployed front-end URL, due Sunday)
- Discussion 07: Compare DynamoDB (key-value/document NoSQL) to PostgreSQL (relational SQL) for a high-traffic e-commerce product catalog. Which would you choose and why? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** AWS DynamoDB, AWS SDK v3 for JavaScript, AWS IAM execution roles

---

#### Week 14 | Module 14 — CI/CD with AWS CodePipeline and CodeBuild
**Learning Objectives:**
- Describe the stages of a CI/CD pipeline (Source → Build → Test → Deploy)
- Configure a CodePipeline that deploys on every GitHub push to main
- Differentiate blue/green, canary, and all-at-once deployment strategies

**Deliverables:**
- Quiz 14 (Canvas, due Sunday)
- Lab 14: CodePipeline connected to GitHub → CodeBuild → S3 deploy (screenshot of successful pipeline run, due Sunday)

**Technologies Introduced:** AWS CodePipeline, AWS CodeBuild, AWS CodeDeploy, GitHub integration

---

#### Week 15 | Module 15 — Containers: Docker and AWS ECS
**Learning Objectives:**
- Write a `Dockerfile` for a Node.js Express application
- Build and run a Docker image locally with `docker build` and `docker run`
- Push a container image to Amazon ECR and describe ECS task deployment

**Deliverables:**
- Quiz 15 (Canvas, due Sunday)
- Lab 15: Dockerized Express app with working `Dockerfile`, local `docker run` test, image pushed to ECR (GitHub URL + ECR image URI, due Sunday)
- Discussion 08: When would you use containers (ECS/Fargate) instead of serverless functions (Lambda) for a production application? (post by Wednesday, responses by Sunday)

**Technologies Introduced:** Docker, Dockerfile, Amazon ECR, Amazon ECS, AWS Fargate (overview)

---

#### Week 16 | Module 16 — Final Exam Prep & AWS Developer Associate Certification
**Learning Objectives:**
- Synthesize full-stack and AWS knowledge across all 15 modules
- Apply DVA-C02 exam strategies (process of elimination, scenario interpretation)
- Complete and submit the course portfolio of lab work

**Deliverables:**
- Quiz 16 (Canvas, due Wednesday — moved up to allow review time)
- **Final Exam** (Canvas, 65 questions, 130 minutes — opens Monday, closes Sunday at 11:59 PM)
- **Portfolio Submission** — GitHub profile link with all 15 lab repositories pinned (due Friday)

**Resources:** AWS Skill Builder practice exam, DVA-C02 Exam Guide PDF, Module 16 study checklist

---

## Summary: Assessment Due Dates Pattern

| Item | Due |
|------|-----|
| Weekly Quiz | Sunday 11:59 PM |
| Weekly Lab | Sunday 11:59 PM |
| Discussion Initial Post | Wednesday 11:59 PM |
| Discussion Peer Responses (×2) | Sunday 11:59 PM |
| Final Exam (Week 16) | Sunday 11:59 PM |
| Portfolio Submission (Week 16) | Friday 11:59 PM |

All times are Central Time (CT). Deadlines are enforced as posted in Canvas — the course schedule in Canvas is authoritative. This document is provided for planning purposes.
