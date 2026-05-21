# Reading Guide: Module 14 - Deployment to AWS
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 14 - Deployment to AWS**! This module covers the practical steps for deploying a full-stack web application to Amazon Web Services using core services tested on the AWS Certified Developer – Associate exam. You will learn how to host static React front-ends on Amazon S3, run Node.js backend servers on EC2 instances, configure security groups for network access control, and use the PM2 process manager to keep your Node.js application running in production. These are foundational AWS deployment skills that underpin the serverless and container architectures covered in subsequent modules.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **AWS S3**: Amazon Simple Storage Service; a highly durable, scalable object storage service. For full-stack deployments, S3 hosts static website assets (HTML, CSS, JavaScript bundles) from React production builds. A bucket is configured with static website hosting enabled, a public read bucket policy, and — when used with CloudFront — an Origin Access Control (OAC) so the bucket remains private except to CloudFront. S3 storage classes (Standard, Intelligent-Tiering, Glacier) and lifecycle rules are heavily tested on DVA-C02.
*   **EC2 hosting**: Amazon Elastic Compute Cloud; a service providing resizable virtual machines (instances) for running server-side application code. For a Node.js/Express backend, you launch an EC2 instance (commonly Amazon Linux 2 or Ubuntu), install Node.js, clone your repository, install dependencies, and start the application. EC2 instance types (`t2.micro`, `t3.small`, etc.), AMIs, key pairs for SSH access, and instance metadata are all DVA-C02 exam topics.
*   **Security groups**: Virtual stateful firewalls attached to EC2 instances (and other AWS resources like RDS, Lambda, ELB) that control inbound and outbound network traffic using allow-rules for protocol, port range, and source/destination. Security groups are stateful — allowing inbound traffic automatically allows the corresponding return traffic. By default, all inbound traffic is blocked and all outbound traffic is allowed. Common configurations: allow SSH (port 22) from your IP, allow HTTP (port 80) and HTTPS (port 443) from `0.0.0.0/0`.
*   **Public ports**: The TCP port numbers that an application listens on and that security group inbound rules must explicitly allow for external access. Port 22 (SSH), 80 (HTTP), 443 (HTTPS), and custom application ports (3000, 8080) are common. In production, a reverse proxy (Nginx or Apache) typically listens on port 80/443 and forwards to the application port — avoiding the need to run Node.js as root (which would be required to listen on ports below 1024).
*   **PM2 service manager**: A Node.js production process manager that keeps applications running after crashes, restarts on server reboot (`pm2 startup`), provides a cluster mode for multi-core CPU utilization, and offers built-in log management. Key commands: `pm2 start app.js`, `pm2 list`, `pm2 logs`, `pm2 restart`, `pm2 stop`. PM2 is the standard way to run Node.js applications on EC2 and is an exam-relevant tool for understanding production Node.js deployments.

---

### 2. Certification Exam Tips
*   **DVA-C02 Core AWS Services:** EC2, S3, and IAM are the foundational services covered in the very first domain of the DVA-C02 exam. For EC2: know instance families, AMIs, key pairs, user data scripts, Elastic IPs, and EBS volumes. For S3: know bucket policies, ACLs, versioning, lifecycle rules, presigned URLs, and transfer acceleration. For IAM: know users, roles, policies, and the principle of least privilege.
*   **S3 + CloudFront is the Standard Static Site Pattern:** The exam frequently tests the S3 + CloudFront architecture for serving static websites. Know that CloudFront distributions can cache S3 objects globally at edge locations, that cache invalidation (`/*`) is required after deployments, and that OAC/OAI restricts direct S3 access to CloudFront only.
*   **Study Resource:** The AWS Free Tier provides 750 hours/month of t2.micro EC2 and 5 GB of S3 storage — sufficient to complete all labs in this module at no cost. [AWS Free Tier](https://aws.amazon.com/free/) and the [AWS Management Console](https://console.aws.amazon.com/) are the primary hands-on resources for this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 3 covering **Deployment** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3) — this section covers deploying a Node.js backend and React frontend to various cloud platforms including AWS.
*   **Required Video:** Watch the AWS deployment section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering S3 static hosting, EC2 setup, and security group configuration.

---

### Lab & Command Integration
In this week's hands-on lab, you will deploy a full-stack application to AWS:
*   **Deploy static build files to AWS S3 bucket**: Run `npm run build` on your React application, create an S3 bucket with static website hosting enabled, and upload the `build/` directory using the AWS CLI (`aws s3 sync build/ s3://your-bucket-name --delete`) or the AWS Management Console.
*   **Launch a virtual Linux instance on AWS EC2**: Launch a `t2.micro` Amazon Linux 2 instance from the EC2 console, download the `.pem` key pair, and SSH in with `ssh -i key.pem ec2-user@<public-ip>`. Install Node.js using `nvm` and clone your Express API repository.
*   **Configure inbound security rules for HTTP/SSH ports**: In the EC2 Security Groups console, add an inbound rule allowing TCP port 22 from your current IP address and TCP port 3000 (or 80) from `0.0.0.0/0` — then verify connectivity with `curl http://<ec2-public-ip>:3000`.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 3 covering **Deployment** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part3).
- [ ] Watch the AWS deployment section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Create an [AWS Free Tier account](https://aws.amazon.com/free/) if you do not already have one — required for lab activities in this and subsequent modules.
- [ ] Proceed to the weekly hands-on lab activity.
