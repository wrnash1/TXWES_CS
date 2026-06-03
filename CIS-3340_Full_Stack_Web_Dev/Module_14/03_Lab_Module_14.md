# Lab 14: Deploying the Full-Stack Bookstore to AWS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**
**Estimated Time:** 120–150 minutes
**Total Points:** 100

---

## Overview

In this lab you will deploy the full-stack bookstore application from Lab 13 to AWS. The React frontend will be served from S3 and CloudFront. The Express API will run on Elastic Beanstalk. The PostgreSQL database will be hosted on Amazon RDS. By the end of the lab your application will be live on a public URL, accessible from any browser in the world.

---

## Prerequisites

- AWS Free Tier account
- AWS CLI installed and configured (`aws configure`)
- Lab 13 Express API and React projects working locally
- Node.js 18+ installed
- A working local PostgreSQL database with the `bookstore` schema

---

## Part 1: Prepare the React Frontend (15 minutes)

### Step 1 — Configure production environment variables

In the React project root, create `.env.production`:

```text
# TODO 1: Set VITE_API_URL to your future Elastic Beanstalk endpoint URL.
# You can use a placeholder now (e.g., https://PLACEHOLDER.elasticbeanstalk.com)
# and update it after deploying the API. You will rebuild and re-upload.
VITE_API_URL=https://PLACEHOLDER.elasticbeanstalk.com
```

Verify that every `fetch` call in your React code uses `import.meta.env.VITE_API_URL`:

```javascript
// TODO 2: Search your codebase for any hardcoded 'http://localhost:3000' URLs.
// Replace each one with:
const API_URL = import.meta.env.VITE_API_URL;
fetch(`${API_URL}/api/books`)
```

### Step 2 — Build the production bundle

```bash
npm run build
```

Open the `dist/` folder in VS Code. Verify it contains:

- `index.html`
- `assets/` folder with content-hashed `.js` and `.css` files

Screenshot: the `dist/` folder structure.

---

## Part 2: Deploy the Frontend to S3 and CloudFront (25 minutes)

### Step 3 — Create the S3 bucket

In the AWS Console (S3):

1. Create bucket — name: `lab14-bookstore-<your-initials>` (must be globally unique)
2. Region: `us-east-1`
3. Uncheck "Block all public access" — acknowledge the warning
4. Leave all other settings as defaults — Create bucket

### Step 4 — Enable static website hosting

In the bucket → Properties → Static website hosting:

- Enable
- Index document: `index.html`
- Error document: `index.html`
- Save

Screenshot: the static website hosting settings showing both documents set to `index.html`.

### Step 5 — Apply the bucket policy

In the bucket → Permissions → Bucket policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::lab14-bookstore-<your-initials>/*"
    }
  ]
}
```

Replace `<your-initials>` with your actual initials. Save.

### Step 6 — Upload the build files

In the bucket → Objects → Upload:

- Click "Add files" and select everything inside `dist/` (not the `dist/` folder itself)
- Also add the `assets/` folder using "Add folder"
- Upload

### Step 7 — Create the CloudFront distribution

In CloudFront console → Create distribution:

- Origin domain: use the S3 **static website endpoint** (shown in S3 → Properties → Static website hosting). It looks like `lab14-bookstore-<initials>.s3-website-us-east-1.amazonaws.com`
- Viewer protocol policy: Redirect HTTP to HTTPS

Under "Custom error responses," add:

| HTTP error code | Response page path | HTTP response code |
|---|---|---|
| 403 | /index.html | 200 |
| 404 | /index.html | 200 |

Create distribution. Wait approximately 5 minutes for the distribution to deploy (Status changes from "Deploying" to the distribution ID).

Screenshot: the CloudFront distribution showing Status as deployed and the Distribution domain name.

### Step 8 — Test the frontend

Visit the CloudFront distribution domain (e.g., `https://d1abc123.cloudfront.net`). You should see the bookstore login form.

Attempt to navigate directly to `https://d1abc123.cloudfront.net/books` — it should load the React app (redirected to login if not authenticated), not a 403 error.

Screenshot: browser showing the bookstore at the CloudFront URL.

---

## Part 3: Deploy the Express API to Elastic Beanstalk (35 minutes)

### Step 9 — Prepare the Express project

In the Express project, verify `package.json` has a `start` script:

```json
{
  "scripts": {
    "start": "node index.js"
  }
}
```

Add the `ssl` option to your `db.js` connection pool for RDS compatibility:

```javascript
// TODO 3: In db.js, add ssl: { rejectUnauthorized: false } to the Pool config.
// Wrap it in a conditional so SSL is only used in production:
const pool = new Pool({
  host:     process.env.DB_HOST,
  port:     parseInt(process.env.DB_PORT) || 5432,
  database: process.env.DB_NAME,
  user:     process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  ssl: process.env.NODE_ENV === 'production'
    ? { rejectUnauthorized: false }
    : false
});
```

Complete TODO 3.

### Step 10 — Create the deployment zip

```bash
# From the Express project root
zip -r lab14-api.zip . \
  -x "node_modules/*" \
  -x ".env" \
  -x "*.git*" \
  -x ".gitignore"
```

Verify the zip does not contain `.env` or `node_modules/`.

### Step 11 — Create the Elastic Beanstalk application

In the Elastic Beanstalk console → Create application:

- Application name: `lab14-bookstore-api`
- Platform: Node.js — Platform branch: Node.js 18 running on 64bit Amazon Linux 2023
- Upload your code: select `lab14-api.zip`

Before creating the environment, configure environment properties. In "Configure more options" → Software → Edit:

| Key | Value |
|---|---|
| `NODE_ENV` | `production` |
| `PORT` | `8080` |
| `JWT_SECRET` | (your secret from Lab 13) |
| `JWT_EXPIRES_IN` | `1h` |
| `ALLOWED_ORIGIN` | (your CloudFront URL, e.g., `https://d1abc123.cloudfront.net`) |

Leave DB variables blank for now — you will add them after creating RDS.

Create the environment. Wait 5–10 minutes for provisioning.

Screenshot: Elastic Beanstalk environment showing "Health: Ok" status.

---

## Part 4: Create the RDS Database (25 minutes)

### Step 12 — Create the RDS PostgreSQL instance

In the RDS console → Create database:

- Engine: PostgreSQL
- Template: Free tier
- DB instance identifier: `lab14-bookstore-db`
- Master username: `postgres`
- Master password: (create a strong password — save it)
- DB instance class: `db.t3.micro`
- Storage: 20 GiB gp2
- Connectivity: same VPC as your Elastic Beanstalk environment
- Public access: No
- VPC security group: Create new — name it `lab14-rds-sg`

Create database. Wait 5–10 minutes.

After creation, note the **Endpoint** (e.g., `lab14-bookstore-db.abc123.us-east-1.rds.amazonaws.com`).

### Step 13 — Configure RDS security group

The RDS security group must allow inbound PostgreSQL connections from the Elastic Beanstalk EC2 security group.

In EC2 → Security Groups, find the security group assigned to your Elastic Beanstalk environment (named something like `awseb-...`). Copy its Group ID.

In the `lab14-rds-sg` security group → Inbound rules → Edit:

- Add rule: Type = PostgreSQL, Source = Custom, enter the EB security group ID

Save.

### Step 14 — Add database environment variables to Elastic Beanstalk

Back in Elastic Beanstalk → Environment → Configuration → Software → Edit:

Add the remaining environment variables:

| Key | Value |
|---|---|
| `DB_HOST` | (your RDS endpoint) |
| `DB_PORT` | `5432` |
| `DB_NAME` | `postgres` |
| `DB_USER` | `postgres` |
| `DB_PASSWORD` | (your RDS master password) |

Apply. Elastic Beanstalk will restart the application with the new variables.

### Step 15 — Run the database schema

Temporarily enable public access on the RDS instance to run schema commands from your laptop:

In RDS → DB instance → Modify → Connectivity → Public access: Yes → Apply immediately.

Connect and run your schema:

```bash
psql -h <your-rds-endpoint> -U postgres -d postgres
```

```sql
CREATE TABLE users (
  id            SERIAL PRIMARY KEY,
  email         VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at    TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE authors (
  id         SERIAL PRIMARY KEY,
  name       VARCHAR(255) NOT NULL,
  country    VARCHAR(100),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE books (
  id         SERIAL PRIMARY KEY,
  title      VARCHAR(255) NOT NULL,
  author_id  INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
  year       INTEGER CHECK (year BETWEEN 1000 AND 2100),
  genre      VARCHAR(100),
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

After running the schema, disable public access again:

In RDS → Modify → Public access: No → Apply immediately.

Screenshot: psql confirming all three tables created on RDS.

---

## Part 5: Wire Everything Together (10 minutes)

### Step 16 — Update the React VITE_API_URL

Now that you have the Elastic Beanstalk URL (visible in the EB console as the "Environment URL"), update `.env.production`:

```text
VITE_API_URL=https://lab14-bookstore-api.us-east-1.elasticbeanstalk.com
```

Rebuild:

```bash
npm run build
```

Re-upload the contents of `dist/` to S3 (delete the existing files first, then upload the new ones).

Create a CloudFront cache invalidation for `/*`.

### Step 17 — End-to-end test

1. Visit your CloudFront URL in the browser.
2. Register a new user account.
3. Log in — the JWT should be issued by the Elastic Beanstalk Express API.
4. Add a book — it should persist in RDS.
5. Reload the page — the book should still be there.
6. Log out and log back in — the data should persist.

Screenshot: the completed bookstore showing at least one book loaded from RDS via Elastic Beanstalk, accessed through the CloudFront URL.

---

## Deliverables

Submit to Canvas:

1. Screenshot: S3 bucket static website hosting settings (index.html for both documents)
2. Screenshot: CloudFront distribution deployed with your domain name visible
3. Screenshot: Elastic Beanstalk environment showing "Health: Ok"
4. Screenshot: RDS instance showing "Available" status
5. Screenshot: psql output confirming all three tables created on RDS
6. Screenshot: deployed application at the CloudFront URL showing a book loaded from RDS
7. The updated `db.js` with SSL configuration
8. The updated `.env.production` (with the real EB URL — no secrets in this file)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| S3 bucket with static hosting and correct error document — screenshot | 10 |
| CloudFront distribution deployed with SPA routing working — screenshot | 15 |
| Elastic Beanstalk environment healthy — screenshot | 20 |
| RDS instance created with no public access; schema created — screenshot | 20 |
| `db.js` updated with production SSL option | 10 |
| `VITE_API_URL` in `.env.production` (no localhost) | 5 |
| End-to-end screenshot: book visible at CloudFront URL, loaded from RDS | 20 |
| **Total** | **100** |

---

## Cleanup Note

AWS Free Tier provides 12 months of limited free usage. To avoid charges after this lab:

- Elastic Beanstalk: Terminate the environment (does not delete the application)
- RDS: Stop the instance (it auto-restarts after 7 days — delete it to prevent charges)
- CloudFront: Disable the distribution (distributions are free while disabled)
- S3: The first 5 GB of storage is free — no action needed for the lab data
