# Quiz: Module 14 - Deployment to AWS
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which AWS compute service provides resizable virtual machines for hosting a Node.js backend application?
*   A) Amazon S3
*   B) Amazon EC2
*   C) AWS Lambda
*   D) Amazon RDS
*   **Correct Answer:** B) Amazon EC2 (Elastic Compute Cloud) provides on-demand virtual machines called instances — you SSH in, install Node.js, and run your Express application just as you would on a physical server.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Amazon S3 is object storage for static files — it does not execute server-side application code.
    *   *Why B is correct:* EC2 instances are full virtual machines where you can install software, configure the OS, and run any application including Node.js servers.
    *   *Why C is incorrect:* AWS Lambda runs stateless functions in response to events without managing a server — it is not an always-on VM for hosting traditional Express servers.
    *   *Why D is incorrect:* Amazon RDS is a managed relational database service — not a compute service for running application code.

---

**Question 2**
Which of the following is the most accurate definition of **security groups** in AWS?
*   A) IAM policies attached to EC2 instances that grant or deny access to other AWS services such as S3 and DynamoDB.
*   B) Stateful virtual firewalls attached to AWS resources that control inbound and outbound network traffic using allow-rules for protocol, port range, and source/destination — blocking all inbound traffic by default.
*   C) AWS Shield configurations that protect EC2 instances from distributed denial-of-service (DDoS) attacks by rate-limiting inbound connections.
*   D) S3 bucket access control lists (ACLs) that restrict which IP addresses can download objects from a public bucket.
*   **Correct Answer:** B) Stateful virtual firewalls attached to AWS resources that control inbound and outbound network traffic using allow-rules for protocol, port range, and source/destination — blocking all inbound traffic by default.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IAM instance profiles attach IAM roles to EC2 instances for AWS service access — security groups control network-level traffic, not IAM permissions.
    *   *Why B is correct:* Security groups are the EC2 network access control mechanism — stateful, allow-only rules on inbound/outbound traffic.
    *   *Why C is incorrect:* AWS Shield is a DDoS protection service — security groups are network firewall rules, not DDoS mitigation.
    *   *Why D is incorrect:* S3 bucket ACLs and bucket policies control object access — security groups are EC2 network-level controls.

---

**Question 3**
A developer uploads a React production build to S3 with static website hosting enabled. The root URL loads correctly but `/about` returns "403 Forbidden." What is the most likely fix?
*   A) Upload a separate `about.html` file to the S3 bucket for each React Router route.
*   B) Configure the S3 static website error document to point to `index.html` — this redirects all unrecognized paths to the React application's entry point so React Router can handle the route client-side.
*   C) Add a security group inbound rule allowing HTTP on port 80 from `0.0.0.0/0` to the S3 bucket.
*   D) Switch from S3 static website hosting to an EC2 instance running a Node.js server — S3 cannot serve multi-route SPAs.
*   **Correct Answer:** B) Configure the S3 static website error document to point to `index.html` — this redirects unrecognized paths to the React entry point so React Router can handle the route client-side.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* React Router manages routes client-side from a single `index.html` — creating separate HTML files for each route breaks the SPA model.
    *   *Why B is correct:* Setting `index.html` as both the index document and the error document ensures all paths serve the React app, allowing React Router to handle routing.
    *   *Why C is incorrect:* Security groups do not apply to S3 — S3 access is controlled by bucket policies and ACLs.
    *   *Why D is incorrect:* S3 fully supports SPA hosting with the correct error document configuration — an EC2 server is not required.

---

**Question 4**
An EC2 instance running Node.js on port 3000 is accessible from within the VPC but not from the public internet. The application is running and listening correctly. What is the most likely cause?
*   A) Node.js requires a TLS certificate to accept connections from outside the VPC.
*   B) The EC2 instance's security group does not have an inbound rule allowing TCP port 3000 from `0.0.0.0/0` (or the client's IP range).
*   C) The EC2 instance does not have a public IPv4 address assigned — it was launched in a private subnet without an Elastic IP.
*   D) Both B and C are possible causes — missing security group rules and no public IP are the two most common reasons an EC2 instance is unreachable from the internet.
*   **Correct Answer:** D) Both B and C are possible causes — a missing security group inbound rule for port 3000 and the absence of a public IP address are the two most common reasons an EC2 instance is unreachable from the internet.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Node.js does not require TLS to accept connections from outside the VPC — TLS is optional and configured at the application or load balancer level.
    *   *Why B alone is insufficient:* Even with an open security group rule, the instance needs a public IP to be reachable from the internet.
    *   *Why C alone is insufficient:* Even with a public IP, the security group must allow inbound traffic on the listening port.
    *   *Why D is correct:* In practice, both conditions must be true: the instance must have a public IP (or Elastic IP) and the security group must allow inbound traffic on the relevant port.

---

**Question 5**
After deploying an update to a React app on S3 + CloudFront, users still see the old version. What must the developer do to serve the updated files?
*   A) Delete and recreate the S3 bucket — CloudFront caches bucket metadata permanently.
*   B) Create a CloudFront cache invalidation for `/*` to force CloudFront edge locations to fetch fresh files from S3 on the next request.
*   C) Re-upload the files with a different bucket name — CloudFront distributions cannot be updated after creation.
*   D) Disable the CloudFront distribution for 24 hours and re-enable it — this clears the edge cache automatically.
*   **Correct Answer:** B) Create a CloudFront cache invalidation for `/*` to force all CloudFront edge locations to discard their cached copies and fetch fresh files from the S3 origin on the next request.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Recreating the S3 bucket is destructive and unnecessary — cache invalidation is the correct mechanism.
    *   *Why B is correct:* CloudFront cache invalidation (`/*` for all files or specific paths) is the standard procedure for propagating deployments to edge caches. The AWS CLI command is `aws cloudfront create-invalidation --distribution-id <ID> --paths "/*"`.
    *   *Why C is incorrect:* CloudFront distributions can be updated after creation — the origin bucket, cache behaviors, and other settings are all editable.
    *   *Why D is incorrect:* Disabling and re-enabling a CloudFront distribution is destructive to availability and does not clear the edge cache the way an invalidation does.
