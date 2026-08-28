# Reading Guide: Module 14 — Cloud Deployment with AWS

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3340 &BULL; FULL STACK WEB DEVELOPMENT</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-3340 Full Stack Web Development
**Certification Alignment:** AWS Certified Developer — Associate (DVA-C02)
**Texas Wesleyan University | Professor Nash**

---

## Introduction

This module covers deploying a full-stack application to AWS. You will serve the React frontend from S3 and CloudFront, run the Express API on Elastic Beanstalk, and connect to a managed PostgreSQL database on Amazon RDS. These are the core deployment services tested on the DVA-C02 exam and used in production full-stack applications.

---

## 1. Three-Tier AWS Architecture

### Service Roles

| Tier | Service | Role |
|---|---|---|
| Frontend | S3 + CloudFront | Host React static assets; serve from global edge locations |
| API | Elastic Beanstalk | Manage EC2 instances running Node.js/Express |
| Database | Amazon RDS | Managed PostgreSQL; automated backups and failover |

### Request Flow

```text
1. User browser → CloudFront edge (serves React SPA from cache)
2. React app → Elastic Beanstalk load balancer → EC2 (Express)
3. Express → RDS PostgreSQL (private VPC connection)
4. RDS → Express → browser (JSON response)
```

---

## 2. Amazon S3 for Static Website Hosting

### Setup Steps

1. Create S3 bucket — uncheck "Block all public access"
2. Enable static website hosting: index document = `index.html`, error document = `index.html`
3. Apply a bucket policy allowing public `s3:GetObject`
4. Upload the contents of the React `dist/` folder

### Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

### Why the Error Document Must Be index.html

S3 serves files by exact key match. A request for `/books/42` looks for an object named `books/42` — which does not exist. S3 returns its "error document." If the error document is `index.html`, the React SPA loads and React Router handles the `/books/42` route client-side.

Without this setting, direct navigation to any React route other than `/` returns an S3 error page.

---

## 3. Amazon CloudFront

### Purpose

CloudFront is a Content Delivery Network (CDN). It caches your S3 files at over 400 edge locations worldwide. Users receive files from the nearest edge, reducing latency significantly.

### Distribution Configuration

| Setting | Value |
|---|---|
| Origin domain | S3 static website endpoint (not bucket ARN) |
| Viewer protocol policy | Redirect HTTP to HTTPS |
| Default root object | `index.html` |

### Custom Error Responses (SPA Routing Fix)

| HTTP Error Code | Response Page Path | HTTP Response Code |
|---|---|---|
| `403` | `/index.html` | `200` |
| `404` | `/index.html` | `200` |

This is the CloudFront equivalent of the S3 error document setting. It returns `index.html` for any path that does not match a file in S3, letting React Router handle routing.

### Cache Invalidation

After uploading new files to S3, CloudFront edge caches may still serve the previous version until the TTL expires. Force immediate refresh:

```text
CloudFront Console → Distribution → Invalidations → Create → /*
```

Create an invalidation for `/*` after every production deployment.

### Content-Hash Filenames

Vite generates asset filenames with a content hash (e.g., `index-Bx3LvQ2C.js`). When code changes, the hash changes, and CloudFront caches the new file automatically because the filename is different. Only `index.html` needs to be invalidated — it does not have a hash.

---

## 4. Vite Environment Variables

```bash
# .env.development  (used by npm run dev)
VITE_API_URL=http://localhost:3000

# .env.production  (used by npm run build)
VITE_API_URL=https://your-eb-env.elasticbeanstalk.com
```

```javascript
// In React components
const API_URL = import.meta.env.VITE_API_URL;

fetch(`${API_URL}/api/books`)
```

### Rules

- Variables must be prefixed with `VITE_` to be included in the browser bundle
- Values are embedded at build time — changing them requires a rebuild
- Never put secrets (database passwords, JWT secret) in `VITE_` variables — they become part of the public JavaScript bundle

---

## 5. AWS Elastic Beanstalk

### What It Does

Elastic Beanstalk is a Platform as a Service (PaaS) that manages the infrastructure for running web applications. You provide application code; Elastic Beanstalk provisions:

- EC2 instances
- Load balancer
- Auto-scaling group
- Health monitoring and alerts
- Rolling deployments

### Deployment Package

Elastic Beanstalk expects a `.zip` file of your application code without `node_modules`. It runs `npm install` from your `package.json` during deployment.

```bash
# Create deployment zip (Mac/Linux)
zip -r app.zip . -x "node_modules/*" -x ".env" -x "*.git*"
```

Never include `.env` in the deployment zip. Set environment variables directly in the Elastic Beanstalk configuration.

### Required package.json Script

```json
{
  "scripts": {
    "start": "node index.js"
  }
}
```

Elastic Beanstalk for Node.js runs `npm start` to start the application.

### Environment Variables in Elastic Beanstalk

Set all secrets and configuration in the Elastic Beanstalk environment:

```text
EB Console → Environment → Configuration → Software → Environment properties
```

| Variable | Value |
|---|---|
| `NODE_ENV` | `production` |
| `PORT` | `8080` (EB default for Node.js) |
| `DB_HOST` | `your-db.abc123.us-east-1.rds.amazonaws.com` |
| `DB_PORT` | `5432` |
| `DB_NAME` | `bookstore` |
| `DB_USER` | `postgres` |
| `DB_PASSWORD` | (your RDS password) |
| `JWT_SECRET` | (your secret) |
| `ALLOWED_ORIGIN` | `https://your-cloudfront-domain.net` |

---

## 6. Amazon RDS for PostgreSQL

### What It Manages

| Feature | AWS Handles |
|---|---|
| Automated backups | Daily snapshots + transaction logs |
| Multi-AZ failover | Automatic standby in a second AZ |
| Patch management | OS and PostgreSQL version patches |
| Storage scaling | Auto-expand with Storage Autoscaling |

### Network Security

RDS should be in a **private subnet** — not accessible from the internet. Only resources inside the same VPC (like your Elastic Beanstalk EC2 instances) can connect.

```text
Public Internet → (blocked) → RDS
Elastic Beanstalk EC2 (same VPC) → (allowed) → RDS
```

Configure the RDS security group to allow inbound TCP on port 5432 only from the Elastic Beanstalk security group.

### Connection String

The RDS endpoint replaces `localhost` in your `pg` Pool configuration:

```javascript
const pool = new Pool({
  host:     process.env.DB_HOST,   // RDS endpoint
  port:     parseInt(process.env.DB_PORT) || 5432,
  database: process.env.DB_NAME,
  user:     process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  ssl:      { rejectUnauthorized: false } // required for RDS
});
```

The `ssl` option is required when connecting to RDS from Elastic Beanstalk.

### RDS Proxy

When Lambda functions scale to many concurrent instances, each creates a new database connection. RDS has a fixed maximum connection limit. RDS Proxy maintains a persistent connection pool between Lambda and RDS, multiplexing many Lambda invocations through fewer actual database connections. No application code changes required.

---

## 7. HTTPS and SSL/TLS

CloudFront provides HTTPS automatically using AWS Certificate Manager (ACM) SSL certificates. For a custom domain:

1. Request a certificate in ACM for `app.example.com`
2. Validate via DNS (add a CNAME record to your domain)
3. Attach the certificate to your CloudFront distribution
4. Create a Route 53 alias record pointing `app.example.com` to the CloudFront distribution

For the Elastic Beanstalk API endpoint, attach an ACM certificate to the load balancer and configure HTTPS on port 443.

---

## 8. Deployment Workflow Summary

```text
1. npm run build          → produces dist/ folder
2. Upload dist/ to S3     → overwrite existing files
3. Invalidate CloudFront  → /* invalidation
4. zip Express project    → exclude node_modules, .env
5. Deploy zip to EB       → EB runs npm install + npm start
6. Verify health          → EB console shows "OK" status
```

---

## 9. Exam and Interview Tips

1. S3 static website hosting requires the error document to be `index.html` for React SPAs — otherwise direct navigation to any non-root route returns an S3 error.

2. CloudFront custom error responses (403/404 → `/index.html` with 200) solve the SPA routing problem at the CDN level when the S3 origin is an OAI bucket (not a static website endpoint).

3. `VITE_` prefix is required for environment variables to appear in the browser bundle. Variables without the prefix are not included. Never put secrets in `VITE_` variables.

4. Elastic Beanstalk runs `npm start` — make sure your `package.json` has a `start` script pointing to `node index.js` or equivalent.

5. Never deploy `.env` to Elastic Beanstalk. Set environment variables through the EB console or `eb setenv`.

6. RDS should be in a private subnet with no public access. Allow inbound port 5432 only from the EB security group.

7. Add `ssl: { rejectUnauthorized: false }` to the `pg` Pool when connecting to RDS from Elastic Beanstalk.

8. CloudFront cache invalidation on `/*` is required after every deployment. Content-hash filenames (Vite default) only require invalidating `index.html` in production pipelines.

---

## 10. Study Checklist

- [ ] Create an S3 bucket with static website hosting enabled and error document set to `index.html`
- [ ] Apply a bucket policy that allows public `s3:GetObject`
- [ ] Create a CloudFront distribution with custom error responses for 403 and 404
- [ ] Build the React app with `npm run build` and upload `dist/` contents to S3
- [ ] Create a CloudFront cache invalidation after uploading new files
- [ ] Configure `VITE_API_URL` in `.env.production` and verify `import.meta.env.VITE_API_URL` is used in fetch calls
- [ ] Create an Elastic Beanstalk Node.js environment and deploy the Express application as a zip
- [ ] Set all environment variables in Elastic Beanstalk (never commit `.env`)
- [ ] Create an RDS PostgreSQL instance in the same VPC as Elastic Beanstalk with no public access
- [ ] Add `ssl: { rejectUnauthorized: false }` to the `pg` Pool for RDS connections
- [ ] Run the schema SQL on RDS and verify the Express API can query it
- [ ] Confirm the deployed full-stack app loads, authenticates, and persists data end-to-end

---

## 11. Supplemental Resources

The following free, open-access resources go deeper on Module 14 topics:

**1. AWS Documentation — Hosting a Static Website on Amazon S3**
[https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
The official AWS guide for S3 static website hosting covering bucket policy configuration, index and error document settings, and the difference between S3 REST endpoint and S3 website endpoint — directly aligned to Part 2 of Lab 14 and the SPA routing fix covered in Section 2 of this guide.

**2. AWS Documentation — Amazon CloudFront Developer Guide**
[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
The complete CloudFront reference covering distribution setup, custom error responses, cache behavior configuration, TTL settings, invalidation paths, and HTTPS with ACM — covers all CloudFront concepts in Section 3 of this guide and the CDN caching questions on the DVA-C02 exam.

**3. AWS Documentation — Elastic Beanstalk Node.js Platform**
[https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.html)
The official Elastic Beanstalk documentation for deploying Node.js applications — covers platform versions, `package.json` requirements, environment property configuration, deployment zip structure, and the Nginx reverse proxy configuration — directly aligned to Section 5 of this guide and Part 3 of Lab 14.

**4. AWS Documentation — Amazon RDS for PostgreSQL**
[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
The official RDS PostgreSQL documentation covering instance creation, VPC and security group configuration, Multi-AZ setup, automated backups, and SSL connection requirements — directly aligned to Section 6 of this guide, the `ssl: { rejectUnauthorized: false }` pattern, and the RDS security questions on the DVA-C02 exam.
