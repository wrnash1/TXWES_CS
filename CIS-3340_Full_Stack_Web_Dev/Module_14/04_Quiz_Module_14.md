# Quiz: Module 14 — Cloud Deployment with AWS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

A developer deploys a React SPA to S3 with static website hosting enabled. The index document is set to `index.html`. When a user navigates directly to `https://bucket.s3-website.amazonaws.com/profile/settings`, they receive an S3 "Key not found" error. What is the root cause and what are two ways to fix it?

- A) S3 does not support React SPAs — move the application to EC2.
- B) S3 tries to find an object with the key `profile/settings` in the bucket. Since no such file exists, it returns an error. Fix 1: Set the S3 error document to `index.html` so all missing keys serve the React SPA. Fix 2: Create a CloudFront distribution with custom error responses mapping 403 and 404 back to `/index.html` with HTTP status 200.
- C) The URL must include a `.html` extension — React Router does not work without file extensions on S3.
- D) The S3 bucket policy is blocking the `/profile/settings` path specifically — add a separate policy statement for that path.

**Correct Answer:** B

**Explanation:** S3 serves files by exact key match. The path `/profile/settings` is a React Router route, not a file in S3. The error document setting tells S3 to serve `index.html` when a key is not found, letting React Router take over client-side. CloudFront custom error responses achieve the same result at the CDN layer — and are required when using S3 bucket origin with Origin Access Identity rather than the static website endpoint.

**Distractor Analysis:**

- Why A is incorrect: S3 static hosting is the standard deployment target for React SPAs.
- Why B is correct: The S3 error document and CloudFront custom error responses are the two correct fixes.
- Why C is incorrect: React Router handles routes without file extensions — the problem is not the URL format.
- Why D is incorrect: S3 bucket policies apply to objects, not URL paths. The issue is the missing object, not permissions.

---

## Question 2

A developer deploys a new version of the React application to S3. Users in Europe still see the previous version even after clearing their browser cache. What is the cause and the fix?

- A) S3 has a 24-hour replication delay to European regions — wait 24 hours.
- B) CloudFront edge caches in Europe are serving the previously cached version of the JavaScript bundle. Create a CloudFront cache invalidation for `/*` to force all edge locations to fetch fresh content from the S3 origin.
- C) The bucket policy must be updated to allow European IP addresses to access the new files.
- D) The React build must be run on a European EC2 instance to produce region-specific bundles.

**Correct Answer:** B

**Explanation:** CloudFront caches objects at edge locations based on their TTL. Uploading new files to S3 does not automatically evict the cached versions at CloudFront edges. A cache invalidation for `/*` instructs all edge locations to discard their cached copies and fetch fresh content from S3 on the next request. Clearing the browser cache only removes the local browser copy — it has no effect on CloudFront edge caches.

**Distractor Analysis:**

- Why A is incorrect: S3 is a global service with no propagation delay. File changes are immediately visible to CloudFront.
- Why B is correct: CloudFront cache invalidation is the required step after every deployment of new static assets.
- Why C is incorrect: CloudFront serves content to users regardless of their geographic location — IP-based policies are not relevant here.
- Why D is incorrect: React builds are region-agnostic — the same `dist/` folder is served globally through CloudFront.

---

## Question 3

An Express application is deployed to Elastic Beanstalk. The application starts but immediately crashes with `Error: Cannot find module 'dotenv'`. What is the most likely cause?

- A) Elastic Beanstalk does not support the `dotenv` npm package on Node.js.
- B) The deployment zip file includes a `node_modules/` folder from a different operating system — the native binaries are incompatible.
- C) The `dotenv` package is listed in `devDependencies` instead of `dependencies` in `package.json`. Elastic Beanstalk runs `npm install --production` which skips `devDependencies`. Moving `dotenv` to `dependencies` fixes the issue.
- D) `require('dotenv').config()` must be called inside the `app.listen()` callback, not at the top of the file.

**Correct Answer:** C

**Explanation:** Elastic Beanstalk installs dependencies using `npm install --omit=dev` (equivalent to `--production`), which skips packages listed in `devDependencies`. Packages required at runtime — including `dotenv`, `express`, `pg`, and `jsonwebtoken` — must be in `dependencies`. Only build tools and testing libraries (Jest, ESLint, nodemon) belong in `devDependencies`. That said, in production on Elastic Beanstalk, `dotenv` is often unnecessary since environment variables are set directly in the EB configuration — but if the code calls `require('dotenv')`, the package must be in `dependencies`.

**Distractor Analysis:**

- Why A is incorrect: Elastic Beanstalk supports all npm packages.
- Why B is incorrect: Elastic Beanstalk runs `npm install` on the deployment server, rebuilding native modules for the correct OS.
- Why C is correct: Runtime dependencies must be in `dependencies`, not `devDependencies`.
- Why D is incorrect: `dotenv.config()` placement does not affect whether the module is installed.

---

## Question 4

A developer places the RDS PostgreSQL instance with "Public access: Yes" and a security group allowing inbound port 5432 from `0.0.0.0/0`. The Elastic Beanstalk team lead immediately asks them to change this. Why?

- A) Public access increases RDS backup costs.
- B) Allowing `0.0.0.0/0` on port 5432 exposes the database to the entire internet. Any attacker who discovers the endpoint URL can attempt to connect and brute-force the database password. RDS should have no public access, with inbound port 5432 restricted to the Elastic Beanstalk security group — accessible only from within the VPC.
- C) RDS does not support connections from `0.0.0.0/0` — it blocks all external connections regardless of security group settings.
- D) Public access on RDS disables Multi-AZ failover.

**Correct Answer:** B

**Explanation:** A database exposed to the internet is one of the most serious cloud security misconfigurations. With `0.0.0.0/0` on port 5432, any host on the internet can attempt to connect to the PostgreSQL instance. Even with a strong password, this exposes the database to credential stuffing attacks, vulnerability exploits, and connection exhaustion. The correct configuration: no public access, security group allowing port 5432 only from the Elastic Beanstalk (or application) security group.

**Distractor Analysis:**

- Why A is incorrect: Public access does not affect backup pricing.
- Why B is correct: Internet-exposed databases are a critical security risk regardless of password strength.
- Why C is incorrect: RDS with public access and a permissive security group does accept external connections — the security group controls access, not a platform-level block.
- Why D is incorrect: Multi-AZ is independent of public access configuration.

---

## Question 5

A React application uses `const API_URL = import.meta.env.VITE_API_URL` in a fetch call. The developer adds `VITE_API_URL=https://api.example.com` to `.env.production` but the build still uses `http://localhost:3000`. What is the most likely cause?

- A) Vite does not read `.env.production` — all environment variables must be in `.env`.
- B) The developer ran `npm run dev` instead of `npm run build` — the development server reads `.env.development`, not `.env.production`. Running `npm run build` produces a bundle with the production URL.
- C) `import.meta.env` is not available in production builds — use `process.env` instead.
- D) The `VITE_` prefix is invalid in `.env.production` — use `REACT_APP_` instead.

**Correct Answer:** B

**Explanation:** Vite reads `.env.development` when running the dev server (`npm run dev`) and `.env.production` when building (`npm run build`). Running `npm run dev` in production configuration mode always uses development variables. The developer must run `npm run build` to produce a bundle that embeds the `.env.production` values. The resulting `dist/` folder then contains JavaScript with the production API URL baked in.

**Distractor Analysis:**

- Why A is incorrect: Vite explicitly reads `.env.production` during `npm run build`.
- Why B is correct: The dev server and build command read different env files.
- Why C is incorrect: `import.meta.env` is fully supported in Vite production builds — it is the official Vite API for environment variables.
- Why D is incorrect: `VITE_` is the correct Vite prefix. `REACT_APP_` is the Create React App (not Vite) prefix.

---

## Question 6

An Express application running on Elastic Beanstalk fails to connect to RDS PostgreSQL, logging `Error: SSL SYSCALL error: EOF detected`. What configuration change fixes this?

- A) Disable SSL in the RDS security group settings.
- B) Add `ssl: { rejectUnauthorized: false }` to the `pg` Pool configuration in the Express application.
- C) Upgrade the Node.js version on Elastic Beanstalk to enable native SSL support.
- D) Use the RDS instance's IP address instead of the endpoint hostname.

**Correct Answer:** B

**Explanation:** Amazon RDS for PostgreSQL requires SSL connections by default. The `pg` (node-postgres) driver needs SSL enabled and, because RDS uses a self-signed certificate not in the default CA bundle, `rejectUnauthorized: false` disables certificate chain verification. In production, the more secure approach is to download the AWS RDS CA certificate and use `ca: fs.readFileSync('rds-ca.pem')` — but `rejectUnauthorized: false` is acceptable for course labs.

**Distractor Analysis:**

- Why A is incorrect: SSL is not configured in the security group — it is a database engine parameter and the `pg` driver configuration.
- Why B is correct: `ssl: { rejectUnauthorized: false }` tells the `pg` driver to use SSL without validating the certificate chain.
- Why C is incorrect: SSL support is a `pg` driver configuration, not a Node.js version issue.
- Why D is incorrect: Using an IP address does not resolve the SSL handshake error.

---

## Question 7

A company wants to run a Node.js Express API on AWS without managing EC2 instances, auto-scaling groups, or operating system patches. They want to upload their code and have AWS run it. Which AWS service best fits this requirement?

- A) Amazon EC2 — launch an instance, SSH in, and run `node index.js` manually.
- B) AWS Elastic Beanstalk — upload a deployment zip and Elastic Beanstalk provisions and manages the EC2 infrastructure, load balancer, and auto-scaling automatically.
- C) Amazon S3 — upload the Node.js code as a static file.
- D) AWS CloudFormation — define the infrastructure as YAML and manage instances manually.

**Correct Answer:** B

**Explanation:** Elastic Beanstalk is a Platform as a Service (PaaS) that abstracts the underlying infrastructure. You upload application code (a zip file); Elastic Beanstalk handles EC2 provisioning, load balancer setup, auto-scaling configuration, rolling deployments, and health monitoring. You retain visibility and control through the console but do not manage servers directly.

**Distractor Analysis:**

- Why A is incorrect: EC2 provides the raw infrastructure — you must provision, configure, and patch it yourself.
- Why B is correct: Elastic Beanstalk is the AWS PaaS for web application deployment, designed exactly for this use case.
- Why C is incorrect: S3 stores static files — it cannot execute Node.js code.
- Why D is incorrect: CloudFormation is an infrastructure-as-code provisioning tool, not a deployment platform. It would provision EC2 but you still manage the instances.

---

## Question 8

A Lambda function connects to an RDS PostgreSQL database. Under a load test with 500 concurrent users, the RDS instance starts rejecting new connections with "FATAL: remaining connection slots are reserved." No application code changes are desired. Which AWS service solves this problem?

- A) Amazon ElastiCache — cache the most common database queries so fewer Lambda invocations reach RDS.
- B) Amazon RDS Proxy — maintains a persistent connection pool between Lambda and RDS, multiplexing hundreds of Lambda invocations through a smaller number of maintained database connections.
- C) AWS Auto Scaling — add more RDS instances to handle the connection load.
- D) AWS SQS — queue the Lambda invocations to serialize database access.

**Correct Answer:** B

**Explanation:** Lambda functions are stateless and create a new database connection on each invocation (unless connection reuse is implemented at the module level). At scale, hundreds of concurrent Lambda instances each create a connection, quickly exhausting PostgreSQL's connection limit. RDS Proxy maintains a persistent pool of connections to RDS and multiplexes many Lambda connections through it. No application code changes are required — simply point the Lambda's database host to the RDS Proxy endpoint instead of the RDS endpoint directly.

**Distractor Analysis:**

- Why A is incorrect: ElastiCache reduces read query load but does not solve connection count exhaustion.
- Why B is correct: RDS Proxy is the AWS-designed solution specifically for Lambda-to-RDS connection pooling.
- Why C is incorrect: RDS cannot horizontally scale read-write connections by adding instances — only read replicas scale reads, and they add more connection targets, not more capacity per target.
- Why D is incorrect: SQS serializes processing — it eliminates concurrency entirely, destroying Lambda's scalability advantage and introducing significant latency.

---

## Question 9

A development team stores database passwords and JWT secrets in `.env` files committed to their git repository. What is the primary risk and the correct AWS solution?

- A) Environment variable files slow down Elastic Beanstalk deployments — store them in S3 instead.
- B) Anyone with access to the git repository — including future contributors, CI/CD systems, and potentially public GitHub viewers — can read the secrets. The correct solution is to store secrets in AWS Secrets Manager or AWS Systems Manager Parameter Store, and retrieve them at runtime rather than embedding them in code or deployment packages.
- C) `.env` files are not supported by Node.js in production — use `config.json` instead.
- D) Committing `.env` files causes merge conflicts when multiple developers change configuration — use environment variables in the OS instead.

**Correct Answer:** B

**Explanation:** Secrets committed to version control are one of the most common and serious cloud security incidents. Once committed, secrets remain in git history even if deleted later. AWS Secrets Manager stores secrets encrypted at rest, enables rotation, and integrates with IAM for access control. AWS Systems Manager Parameter Store offers a similar capability with a free tier for standard parameters. For Elastic Beanstalk, environment properties in the EB console are a simpler alternative that avoids committing secrets to git.

**Distractor Analysis:**

- Why A is incorrect: File size has no meaningful effect on deployment speed, and S3 is not the recommended secrets store.
- Why B is correct: Secrets in version control is a critical vulnerability. Secrets Manager and Parameter Store are the AWS solutions.
- Why C is incorrect: Node.js supports `.env` files via `dotenv` — the issue is security, not compatibility.
- Why D is incorrect: Merge conflicts are a workflow problem, not a security concern. The primary risk is credential exposure.

---

## Question 10

A developer builds a React SPA that calls an API Gateway endpoint backed by Lambda and DynamoDB. The React build is hosted on S3 with CloudFront. What is the correct architectural reason that the React application does not embed AWS credentials (Access Key ID and Secret Access Key) in the JavaScript bundle?

- A) JavaScript cannot make HTTP requests to AWS services — only server-side languages can access AWS APIs.
- B) The React application calls API Gateway endpoints using `fetch()` — API Gateway is a public HTTPS endpoint that requires no AWS credentials. The Lambda function behind API Gateway uses an IAM execution role to access DynamoDB. AWS credentials never leave the server side.
- C) AWS Access Keys are automatically injected into the browser by CloudFront — no manual configuration is needed.
- D) React bundles are encrypted by Vite before deployment, so credentials in the bundle are safe.

**Correct Answer:** B

**Explanation:** The React application authenticates to API Gateway using a JWT (via a Lambda Authorizer) or an API key — not AWS IAM credentials. API Gateway is a public HTTPS endpoint. The Lambda function uses its IAM execution role (assigned via the Lambda configuration) to access DynamoDB — these role credentials are managed by AWS internally and never exposed to the client. Embedding IAM credentials in a JavaScript bundle is a critical security violation: any user can inspect the bundle source and extract the keys.

**Distractor Analysis:**

- Why A is incorrect: JavaScript absolutely can make HTTP requests to AWS services — but through public API endpoints, not with embedded IAM credentials.
- Why B is correct: This describes the correct separation: public API endpoint (no AWS credentials needed) + server-side IAM role (never exposed to client).
- Why C is incorrect: CloudFront does not inject AWS credentials into browser bundles.
- Why D is incorrect: Vite produces standard JavaScript bundles — they are not encrypted and are fully readable in browser DevTools.
