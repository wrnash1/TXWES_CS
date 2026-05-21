# Reading Guide: Module 16 - Final Exam Prep & AWS Developer Associate Certification
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 16 - Final Exam Prep & AWS Developer Associate Certification**! This final module synthesizes everything you have built and studied across the course and prepares you specifically for the AWS Certified Developer – Associate (DVA-C02) examination. You will review the four exam domains, practice high-yield scenario questions, and solidify your understanding of how the full-stack skills from Modules 1–15 connect to AWS service architectures. This module also covers exam strategy, question interpretation techniques, and the hands-on lab portfolio review required for course completion.

---

### 1. High-Yield Glossary
Review these exam-focused definitions as final preparation:

*   **Core Operations (DVA-C02 Domain 1 — Development with AWS Services)**: The application-layer skills that make up the largest exam domain (~32%). Core operations include writing Lambda functions with correct handler signatures, building and consuming API Gateway REST/WebSocket APIs, reading and writing to DynamoDB using the AWS SDK v3, processing SQS and SNS messages, and using S3 presigned URLs for secure object access. Mastery of these operations directly determines exam performance.
*   **Best Practices (DVA-C02 Domain 2 — Security)**: Security best practices tested on the exam (~26%) include IAM least-privilege policies, using AWS Secrets Manager and Parameter Store for credential management, encrypting data at rest (KMS, S3 SSE) and in transit (HTTPS/TLS), using Cognito for user authentication, and implementing API Gateway authorizers (Cognito User Pool authorizers and Lambda authorizers). Never embed credentials in code — always use IAM roles for service-to-service authentication.
*   **System Configuration (DVA-C02 Domain 3 — Deployment)**: Deployment-related exam topics (~24%) include using AWS SAM (Serverless Application Model) and CloudFormation for infrastructure as code, deploying applications with AWS CodePipeline + CodeBuild + CodeDeploy (CI/CD), blue/green and canary deployment strategies, EC2 Auto Scaling and Elastic Beanstalk environment configuration, and Lambda deployment packages and layers. The exam tests both conceptual understanding and practical AWS console and CLI knowledge.

---

### 2. Certification Exam Tips
*   **Know the DVA-C02 Exam Structure:** The exam has 65 questions (50 scored + 15 unscored), a 130-minute time limit, and a passing score of 720/1000. Question types are multiple-choice (one correct answer) and multiple-response (two or more correct answers — the question specifies how many). Flag difficult questions and return to them — do not spend more than 2 minutes on any single question.
*   **Use the Process of Elimination:** For scenario questions, eliminate obviously wrong answers first. AWS exam distractors frequently include technically valid services used in the wrong context (e.g., using Kinesis when SQS is correct, or using EC2 when Lambda is more appropriate). Read each answer choice carefully and ask: "Does this answer directly solve the stated problem in the most operationally efficient way?"
*   **Study Resource:** AWS Skill Builder provides the official DVA-C02 exam guide, sample questions, and practice exams. [AWS Skill Builder — Developer Associate](https://explore.skillbuilder.aws/learn/course/external/view/elearning/9884/exam-prep-aws-certified-developer-associate) is the primary exam prep resource. The [DVA-C02 Exam Guide PDF](https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS-Certified-Developer-Associate_Exam-Guide.pdf) lists all tested services and tasks by domain.

---

### Required Readings & Videos
To prepare for the final exam and AWS certification, complete the following:
*   **Required Review:** Revisit the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/) — specifically Parts 3 (Node/Express/Deployment), 4 (Authentication), and any AWS-specific sections. Use the table of contents to identify and re-read any topics where you feel less confident.
*   **Required Video:** Watch the full-stack review and AWS certification section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — for a consolidated review of the course topics and deployment patterns tested on the exam.

---

### Lab & Command Integration
In this final module, you will complete a portfolio review and exam simulation:
*   **Portfolio review — verify all lab submissions**: Confirm that all 15 module labs have been completed and submitted. Each lab should be accessible via GitHub or a live deployment URL. Review the code for any lingering anti-patterns (hard-coded credentials, missing error handling, plaintext passwords) and fix them.
*   **AWS Architecture review**: Sketch the complete architecture of your course capstone project: React (S3 + CloudFront) → API Gateway → Lambda → DynamoDB. Label each component with its AWS service name, explain the security controls at each boundary (IAM roles, Cognito authorizer, KMS encryption), and document how the CI/CD pipeline deploys updates.
*   **Take a full DVA-C02 practice exam**: Complete the [AWS Skill Builder Official Practice Question Set](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13270/aws-certified-developer-associate-official-practice-question-set-dva-c02) under timed conditions — review every incorrect answer and identify the specific AWS documentation or course module that covers the tested concept.

---

### 3. Study Checklist
- [ ] Review all 15 module glossary terms — especially AWS service definitions from Modules 10–15.
- [ ] Complete the portfolio review and verify all lab submissions are accessible and correct.
- [ ] Take at least one full-length DVA-C02 practice exam at [AWS Skill Builder](https://explore.skillbuilder.aws/).
- [ ] Review the [DVA-C02 Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS-Certified-Developer-Associate_Exam-Guide.pdf) and confirm you can describe at least one use case for each listed service.
- [ ] Submit the final exam through Canvas — good luck!
