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

---

### Question 11 (5 points)

A developer deploys a new `index-NewHash.js` bundle to S3 but does not create a CloudFront cache invalidation. Which behavior will most users experience after deployment?

- A) All users will immediately receive the new bundle because S3 notifies CloudFront of changes.
- B) Users will continue to receive the old `index.html` (and therefore load the old JS bundle) from CloudFront edge caches until the cache TTL expires or an invalidation is created.
- C) CloudFront automatically invalidates its cache whenever an S3 object is overwritten.
- D) Content-hashed filenames eliminate the need for cache invalidations — only `index.html` needs updating.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: S3 has no mechanism to push change notifications to CloudFront edges. CloudFront fetches from origin only when the cached TTL expires or an invalidation is requested.
  - Why B is correct: CloudFront edges serve their cached copy until the TTL expires. The new bundle exists in S3, but existing edge-cached responses are unaffected until invalidated.
  - Why C is incorrect: CloudFront does not monitor S3 for changes. Invalidation is always a manual or automated (CI/CD) action.
  - Why D is correct as far as it goes, but B is the best answer to the question asked. Content-hashed filenames (`index-NewHash.js`) do mean the new file is never stale because it has a new name. However, `index.html` still points to the old bundle name until it is also updated and the CloudFront cache for `index.html` is invalidated. Without invalidating `index.html`, users get the old entry point.

---

### Question 12 (5 points)

An Elastic Beanstalk Node.js application fails health checks and shows "Degraded" status. The EB logs show `Error: listen EADDRINUSE :::3000`. What is the most likely cause?

- A) Port 3000 is blocked by the EB security group inbound rules.
- B) The application is trying to listen on port 3000, but Elastic Beanstalk routes traffic through its Nginx proxy on port 8080 by default. The application must listen on `process.env.PORT` (which EB sets to `8080`) rather than a hardcoded port.
- C) Another EB application is already running on port 3000 in the same region.
- D) Node.js 18 does not support port numbers below 4000.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Security group rules control external access — they do not cause `EADDRINUSE` errors inside the instance.
  - Why B is correct: Elastic Beanstalk sets `PORT=8080` as an environment variable and configures Nginx to proxy to it. If the application ignores `process.env.PORT` and hardcodes `3000`, Nginx cannot route traffic to it, causing health check failures. Reading `process.env.PORT` is essential.
  - Why C is incorrect: Each EB environment runs on its own EC2 instance — there is no port conflict between environments.
  - Why D is incorrect: Node.js has no minimum port restriction for application code (only ports below 1024 require root privileges on Linux).

---

### Question 13 (5 points)

A developer sets `VITE_DB_PASSWORD=mysecretpassword` in `.env.production` and uses it in a React component. What is the security consequence?

- A) Vite strips variables not prefixed with `VITE_` from the bundle, so database passwords are automatically protected.
- B) The `VITE_DB_PASSWORD` value is embedded in the JavaScript bundle at build time and shipped to every browser that loads the application. Anyone can open DevTools or inspect the bundle source to read it.
- C) Environment variables in `.env.production` are encrypted by Vite before being embedded in the bundle.
- D) The password is only accessible server-side because React runs on the server with SSR.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This is precisely backwards. The `VITE_` prefix is required for a variable to appear in the bundle. Variables WITHOUT the prefix are excluded. Adding the prefix ensures the value is included — which is dangerous for secrets.
  - Why B is correct: Any variable with the `VITE_` prefix is inlined into the JavaScript bundle as plain text. `VITE_DB_PASSWORD` would literally appear as the string `mysecretpassword` in the minified output.
  - Why C is incorrect: Vite performs no encryption on environment variable values — they are substituted as plain strings.
  - Why D is incorrect: A standard Vite React application is a client-side SPA — React runs entirely in the browser, not on the server.

---

### Question 14 (5 points)

A developer runs `npm run build` and the `dist/index.html` still contains `http://localhost:3000` in the compiled JavaScript. `VITE_API_URL` is correctly set in `.env.production`. What is the most likely mistake?

- A) The code uses `process.env.VITE_API_URL` instead of `import.meta.env.VITE_API_URL`.
- B) The `.env.production` file was committed to `.gitignore`.
- C) `npm run build` must be run from the React `src/` directory, not the project root.
- D) Vite only reads `.env` — `.env.production` is not a supported file name.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: Vite exposes environment variables via `import.meta.env`, not `process.env`. Using `process.env.VITE_API_URL` returns `undefined` in the browser at runtime, causing the code to fall back to a hardcoded default or produce `undefined` in the URL string. The build succeeds without errors because `process.env` is a valid expression.
  - Why B is incorrect: `.gitignore` affects git tracking, not Vite's ability to read the file during the local build process.
  - Why C is incorrect: `npm run build` must be run from the project root where `package.json` lives — not from `src/`.
  - Why D is incorrect: Vite supports `.env`, `.env.local`, `.env.development`, `.env.production`, and their `.local` variants.

---

### Question 15 (5 points)

Which of the following correctly describes how Amazon RDS Multi-AZ failover works?

- A) Multi-AZ creates read replicas in multiple regions that applications load-balance across.
- B) Multi-AZ maintains a synchronous standby replica in a second Availability Zone. If the primary instance fails, RDS automatically updates the DNS endpoint to point to the standby within 60–120 seconds — no application code changes required.
- C) Multi-AZ requires the application to detect the primary failure and reconnect to a hardcoded standby endpoint.
- D) Multi-AZ is only available for MySQL — PostgreSQL uses a different high-availability mechanism.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Multi-AZ describes synchronous replication within a region for high availability, not read replicas across regions. Read replicas are a separate, asynchronous feature for scaling reads.
  - Why B is correct: RDS Multi-AZ is a transparent HA mechanism. The application always connects to the same RDS endpoint — AWS handles the failover DNS switch automatically.
  - Why C is incorrect: The failover is automatic and transparent. The application does not need to detect failure or change connection strings.
  - Why D is incorrect: Multi-AZ is available for all major RDS database engines including PostgreSQL, MySQL, MariaDB, Oracle, and SQL Server.

---

### Question 16 (5 points)

An Express API deployed to Elastic Beanstalk uses `cors({ origin: 'http://localhost:5173' })`. After deploying the React app to CloudFront, all API calls from the browser fail with CORS errors. What is the fix?

- A) Disable CORS entirely on the EB environment — Elastic Beanstalk handles CORS at the load balancer level.
- B) Update the `ALLOWED_ORIGIN` environment variable in Elastic Beanstalk to the CloudFront domain, and update the Express CORS configuration to use `origin: process.env.ALLOWED_ORIGIN`.
- C) Re-deploy the React app to S3 using the same domain as the Elastic Beanstalk environment.
- D) CORS only applies to local development — production deployments do not enforce CORS.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The load balancer does not handle application-level CORS headers. The Express application must set the correct `Access-Control-Allow-Origin` header.
  - Why B is correct: The `origin` option must match the actual domain making requests. After deploying to CloudFront, requests come from the CloudFront domain. Hardcoding `localhost:5173` in production breaks all browser requests. Reading the origin from an environment variable allows it to be set per environment without code changes.
  - Why C is incorrect: Hosting React on the same domain as the API would technically eliminate the cross-origin issue, but this conflates the two deployment targets and is not the intended architecture.
  - Why D is incorrect: Browsers enforce CORS on all cross-origin requests regardless of environment. There is no production exemption.

---

### Question 17 (5 points)

A developer connects to an RDS PostgreSQL instance with `psql` to run the schema, then sets `Public access: No`. What does `Public access: No` prevent?

- A) It prevents Elastic Beanstalk EC2 instances from connecting to the database.
- B) It removes the public IP address from the RDS instance and blocks all connections from outside the VPC — the database can only be reached from resources within the same VPC.
- C) It blocks all connections including from the same VPC until explicitly re-enabled.
- D) It applies to reads only — writes still require public access.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: EB EC2 instances are inside the same VPC as the RDS instance. Private VPC traffic is allowed by the security group rule, which is independent of the public access setting.
  - Why B is correct: Setting public access to No removes the publicly routable DNS entry for the instance. The instance remains accessible from within the VPC via its private endpoint. Security groups provide an additional layer of access control.
  - Why C is incorrect: Connections from within the same VPC are controlled by security groups, not the public access setting. VPC-internal traffic is unaffected.
  - Why D is incorrect: Public access is an all-or-nothing network exposure setting — it does not differentiate between read and write operations.

---

### Question 18 (5 points)

A developer wants to automate the deployment of the React frontend so that running a single command builds, uploads to S3, and invalidates CloudFront. Which AWS CLI sequence accomplishes this?

- A) `aws s3 sync dist/ s3://bucket-name --delete && aws cloudfront create-invalidation --distribution-id ABCDEF --paths "/*"`
- B) `aws ec2 deploy dist/ && aws cloudfront invalidate`
- C) `aws s3 push dist/ s3://bucket-name && aws cloudfront flush`
- D) `aws s3 copy dist/ s3://bucket-name --region us-east-1 && aws cloudfront purge --all`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: `aws s3 sync` uploads all changed files from `dist/` to the S3 bucket and removes files that no longer exist locally (`--delete`). `aws cloudfront create-invalidation` forces all edge locations to discard cached copies. Both commands use correct CLI syntax.
  - Why B is incorrect: `aws ec2 deploy` is not a valid command. EC2 deployment uses CodeDeploy, not a direct S3-style sync.
  - Why C is incorrect: `aws s3 push` and `aws cloudfront flush` are not valid AWS CLI commands.
  - Why D is incorrect: `aws s3 copy` copies a single object — it does not sync a folder. `aws cloudfront purge` is not a valid command.

---

### Question 19 (5 points)

An Express application stores its database connection pool as a module-level variable: `const pool = new Pool(config)`. On Elastic Beanstalk, the application reconnects to RDS successfully after deployment. Why is this pattern correct for EB but potentially problematic for Lambda?

- A) Elastic Beanstalk EC2 instances have persistent processes — the module is loaded once and the pool is reused across requests. Lambda functions may spin up new execution environments, each creating a new `Pool` and connection. At high concurrency, this exhausts RDS connections.
- B) Elastic Beanstalk uses Node.js, which supports module-level variables. Lambda uses Python, which does not.
- C) Lambda destroys the connection pool after each invocation — a new pool is created for every single request.
- D) Elastic Beanstalk connections are encrypted automatically; Lambda connections require explicit SSL configuration.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: EB runs a persistent Node.js process. The pool initializes once at startup and reuses connections across HTTP requests — exactly as designed. Lambda execution environments are ephemeral. Each new execution environment creates a new `Pool`. At scale, many environments run simultaneously, each holding connections, quickly reaching RDS limits. RDS Proxy solves this.
  - Why B is incorrect: Lambda supports Node.js — the language is not the distinction.
  - Why C is incorrect: Lambda does not destroy module-level state after each invocation — a warm execution environment reuses module-level variables across invocations. The problem is the number of concurrent environments, each with its own pool.
  - Why D is incorrect: SSL configuration is independent of the connection pool pattern and applies equally to both platforms.

---

### Question 20 (5 points)

After deploying the full-stack application, the developer needs to test the end-to-end auth flow on the live URL. Which sequence is correct?

- A) Register → Login → confirm JWT in browser DevTools → add a book → reload → verify book persists → logout → verify redirect to login.
- B) Login → Register → confirm JWT → reload.
- C) Deploy CloudFront → Run `npm run dev` locally → test via localhost → upload to S3.
- D) Run all tests locally with `npm test` — no end-to-end verification is needed after cloud deployment.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why A is correct: This sequence exercises every layer of the deployed system — registration (RDS write), login (JWT issuance from EB), JWT storage (browser), data persistence (RDS), session restore from `localStorage` (React), and logout (token removal). Each step validates a different component.
  - Why B is incorrect: A user must register before they can log in — logging in first will fail because no account exists yet. The order matters.
  - Why C is incorrect: Testing against localhost after cloud deployment validates the local build, not the deployed system. The point of end-to-end testing is to verify the live CloudFront → EB → RDS path.
  - Why D is incorrect: Unit and integration tests run locally against a local or test database. They do not verify that EB environment variables are correct, that the RDS security group allows connections, or that CloudFront routes requests correctly.
