# Video Script: Module 14 — Cloud Deployment with AWS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**
**Estimated Duration:** 23–25 minutes
**Certification Alignment:** AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: AWS Console (us-east-1), VS Code, terminal
- Use [SHOW SCREEN] for AWS Console; [SHOW CODE] for VS Code; [PAUSE] for slide transitions
- Have AWS Free Tier account ready; Elastic Beanstalk, S3, RDS, CloudFront, Elastic Beanstalk CLI installed
- Pre-built React `dist/` folder and Express project from Lab 13 ready for deployment

---

## Section 1: Introduction — From Localhost to Production (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 14 — Cloud Deployment with AWS.

You have built a full-stack application: React frontend, Express API, PostgreSQL database, JWT authentication. It runs perfectly on your laptop. Today you deploy it to the cloud so the world can use it.

We will deploy the React SPA to S3 with CloudFront as the CDN, deploy the Express API to AWS Elastic Beanstalk, and connect it to an Amazon RDS PostgreSQL instance. This is the standard AWS three-tier deployment pattern, and it maps directly to what the DVA-C02 exam tests.

By the end of this module you will understand the role of each AWS service in a production deployment, know how environment variables work in both Elastic Beanstalk and Vite production builds, and be able to explain the end-to-end request flow from browser to database.

[PAUSE — slide: Module 14 Learning Objectives]

---

## Section 2: The Three-Tier AWS Architecture (1:30 – 5:00)

Let me orient you to the architecture before we touch the console.

[PAUSE — slide: Three-tier architecture diagram]

Tier one: the frontend. The React build output — `index.html`, JavaScript bundles, CSS — is a set of static files. We store them in an S3 bucket and serve them through CloudFront. CloudFront caches the files at edge locations around the world. When a user in Tokyo visits your app, they get the files from a server in Tokyo, not from your S3 bucket in Virginia.

Tier two: the API. The Express application runs on Elastic Beanstalk — AWS's managed platform for running web applications on EC2 instances. Elastic Beanstalk handles instance provisioning, load balancing, health monitoring, and rolling deployments. You upload a zip of your application code and Elastic Beanstalk takes care of the rest.

Tier three: the database. Amazon RDS for PostgreSQL is a managed relational database. AWS handles backups, patching, and failover. Your Express application connects to it exactly as it connects to a local PostgreSQL instance — same `pg` Pool, same connection string — just with an RDS endpoint URL.

[PAUSE — slide: Traffic flow — browser → CloudFront → S3 → Express EB → RDS]

The traffic flow:

1. Browser requests `https://app.example.com/` — CloudFront responds from its edge cache with `index.html` and JavaScript bundles.
2. React application loads in the browser.
3. React fetches `https://api.example.com/api/books` — this goes to the Elastic Beanstalk load balancer.
4. Load balancer routes the request to an EC2 instance running Express.
5. Express queries RDS PostgreSQL.
6. RDS returns the data, Express sends the JSON response, React renders it.

---

## Section 3: Deploying the React Frontend to S3 and CloudFront (5:00 – 11:00)

[SHOW SCREEN — AWS Console]

Step one: create an S3 bucket.

In the S3 console, click "Create bucket." Name it something like `lab14-bookstore-frontend`. Choose your region. Uncheck "Block all public access" — we need the files publicly readable. Confirm the warning. Create the bucket.

Under "Properties," scroll to "Static website hosting" and enable it. Set the index document to `index.html` and the error document to `index.html`. That second setting is critical — it makes React Router work for direct URL navigation.

[PAUSE — slide: Why error document must be index.html for SPAs]

Step two: upload the React build.

In VS Code, run:

[SHOW CODE]

```bash
# In the React project folder
npm run build
```

This produces the `dist/` folder. Back in the S3 console, upload the entire contents of `dist/` — not the `dist/` folder itself, but everything inside it. Set the storage class to "Standard."

Step three: set the bucket policy for public read access.

[SHOW CODE]

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::lab14-bookstore-frontend/*"
    }
  ]
}
```

Step four: create the CloudFront distribution.

In the CloudFront console, click "Create distribution." For the origin domain, use the S3 static website endpoint (not the bucket ARN — the website endpoint that ends in `.s3-website-us-east-1.amazonaws.com`).

Under "Default cache behavior," redirect HTTP to HTTPS. Under "Custom error responses," add two entries:

- HTTP error code `403` → Response page path `/index.html` → HTTP response code `200`
- HTTP error code `404` → Response page path `/index.html` → HTTP response code `200`

These two entries are what make direct navigation to `/books/42` work when deployed.

[PAUSE — slide: CloudFront custom error responses for SPA routing]

After the distribution deploys (about five minutes), visit the CloudFront domain. Your React app should load.

---

## Section 4: Deploying the Express API to Elastic Beanstalk (11:00 – 18:00)

[SHOW SCREEN — AWS Console]

Step one: prepare the application for Elastic Beanstalk.

Elastic Beanstalk expects a zip file containing your application code. Before zipping, make sure your `package.json` has a `start` script that runs your server with `node`:

[SHOW CODE]

```json
{
  "scripts": {
    "start": "node index.js"
  }
}
```

Remove `node_modules/` — Elastic Beanstalk runs `npm install` from your `package.json`. Zip the project:

[SHOW CODE]

```bash
# On Mac/Linux
zip -r lab14-api.zip . -x "node_modules/*" -x ".env"
```

Notice: exclude `.env`. You never deploy your secrets file — you set environment variables directly in Elastic Beanstalk.

Step two: create the Elastic Beanstalk application.

In the Elastic Beanstalk console, click "Create Application." Platform: Node.js. Upload your zip file.

Under "Configure more options," find "Software" and click "Edit." This is where you add environment variables: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `JWT_SECRET`, `JWT_EXPIRES_IN`, `ALLOWED_ORIGIN`. Set `NODE_ENV=production`.

[PAUSE — slide: Environment variables in Elastic Beanstalk — never commit secrets]

Step three: create the RDS instance.

In the RDS console, create a PostgreSQL database. Choose "Free tier" for the practice lab. Database identifier: `lab14-bookstore`. Set a master username and password — use the same values you will set in the Elastic Beanstalk `DB_USER` and `DB_PASSWORD` environment variables.

Under "Connectivity," place the RDS instance in the same VPC as the Elastic Beanstalk environment. Set "Public access" to "No" — the database should only be accessible from within the VPC, not from the internet.

The RDS endpoint will look like: `lab14-bookstore.abc123.us-east-1.rds.amazonaws.com`. Use this as your `DB_HOST` environment variable in Elastic Beanstalk.

[PAUSE — slide: VPC — why RDS should not be publicly accessible]

Step four: create the database schema.

To run the `CREATE TABLE` commands on RDS, you have two options: temporarily enable public access to run psql from your laptop, or SSH into the Elastic Beanstalk EC2 instance and run psql from there. For this lab, temporarily enable public access, run your schema, then disable it.

[SHOW CODE]

```bash
psql -h lab14-bookstore.abc123.us-east-1.rds.amazonaws.com \
     -U postgres -d bookstore
```

Run your `CREATE TABLE` statements for `users`, `authors`, and `books`.

Step five: update the CORS configuration.

The React app is now on CloudFront, not localhost. Update the Express `ALLOWED_ORIGIN` environment variable to your CloudFront domain: `https://d1abc123.cloudfront.net`.

[PAUSE — slide: Environment-based CORS origin configuration]

---

## Section 5: Connecting the Frontend to the Deployed API (18:00 – 23:00)

[SHOW CODE]

The React app currently fetches from `http://localhost:3000`. In production, it needs to fetch from the Elastic Beanstalk URL. Use Vite environment variables:

```text
# .env.development
VITE_API_URL=http://localhost:3000

# .env.production
VITE_API_URL=https://your-env.eba-abc123.us-east-1.elasticbeanstalk.com
```

In your React code:

```javascript
const API_URL = import.meta.env.VITE_API_URL;
fetch(`${API_URL}/api/books`);
```

Rebuild and re-upload to S3. Invalidate the CloudFront cache after uploading new files:

[SHOW SCREEN — AWS Console]

In CloudFront, select your distribution, go to "Invalidations," create an invalidation for `/*`. This forces all edge locations to fetch fresh files from S3. Without invalidation, users may see the old version for up to 24 hours.

[PAUSE — slide: CloudFront cache invalidation — required after every deployment]

[SHOW BROWSER]

Open the CloudFront URL. The React app loads. Log in. The books list loads from RDS via Elastic Beanstalk. Add a book — it persists in the cloud database. Refresh the page — the data is still there.

---

## Conclusion (23:00 – 25:00)

Summary of Module 14:

- S3 static website hosting stores React build files. The error document must be `index.html` for SPA routing.
- CloudFront serves the files globally from edge locations. Custom error responses for 403/404 return `index.html` for all routes.
- Elastic Beanstalk manages EC2 instances running Node.js. Never deploy `.env` — use EB environment variables.
- RDS PostgreSQL is the managed database. Place it in the same VPC as Elastic Beanstalk. Do not enable public access.
- Vite environment variables (`VITE_`) configure the API URL per environment. Rebuild after changing them.
- CloudFront cache invalidation on `/*` is required after every S3 deployment.

DVA-C02 exam focus: know which service plays which role — S3 for static assets, CloudFront for CDN, Elastic Beanstalk for managed EC2 web apps, RDS for relational data. The exam also tests that RDS should be in a private subnet (not publicly accessible) and that environment-specific configuration belongs in environment variables, not code.

Lab 14 deploys your Lab 13 full-stack application to AWS. See you there.

[END OF SCRIPT]
