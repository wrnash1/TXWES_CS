# Reading Guide: Module 08 - Lambda and Serverless Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 08 - Lambda and Serverless Architecture**! AWS Lambda allows you to run code without provisioning or managing servers. You upload your function code, configure triggers, and AWS handles everything else — scaling, patching, and availability. This module covers Lambda's execution model, event-driven triggers, concurrency limits, and how Lambda integrates with API Gateway, S3, DynamoDB Streams, SQS, and SNS to build fully serverless applications. Serverless architecture is one of the highest-growth areas on the SAA-C03 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AWS Lambda**: A serverless compute service that executes functions in response to events. Lambda functions run in isolated, ephemeral execution environments with configurable memory (128 MB to 10,240 MB), timeout (up to 15 minutes), and CPU (proportional to memory). Lambda scales automatically — each invocation runs in a separate environment, enabling virtually unlimited concurrency. You are billed only for the compute time consumed (in 1-ms increments), with a generous free tier.

*   **Lambda Event Sources and Triggers**: AWS services and resources that invoke Lambda functions. Synchronous invocations (Lambda waits and returns a response) include API Gateway, Application Load Balancer, and Cognito. Asynchronous invocations (Lambda receives and queues the event) include S3 Event Notifications, SNS, and EventBridge. Poll-based invocations (Lambda polls the source) include SQS, DynamoDB Streams, and Kinesis Data Streams. Understanding the invocation model matters for error handling and retry behavior.

*   **Lambda Concurrency and Cold Starts**: Concurrency is the number of function instances executing simultaneously. Lambda supports up to 1,000 concurrent executions per account per Region by default (can be increased). The first invocation of a Lambda function (or one after a period of inactivity) incurs a "cold start" — the time to initialize the execution environment, including loading the runtime and function code. Cold starts range from milliseconds to seconds depending on runtime and package size. Provisioned Concurrency pre-initializes execution environments to eliminate cold starts for latency-sensitive applications.

*   **API Gateway**: A fully managed service for creating, publishing, and securing REST, HTTP, and WebSocket APIs. API Gateway commonly acts as the front door for Lambda-based serverless applications — HTTP requests arrive at API Gateway, which invokes Lambda functions synchronously to handle business logic and return responses. API Gateway handles authentication (IAM, Cognito, Lambda authorizers), throttling, SSL, and request/response transformation.

*   **Lambda Layers**: A mechanism for packaging and sharing code, libraries, or data that multiple Lambda functions depend on. A Layer is a ZIP archive that Lambda extracts into `/opt` in the function's execution environment. Layers reduce function deployment package size, improve reuse across functions, and allow dependency updates without redeploying every function.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** Lambda/serverless content appears in Design High-Performing Architectures (24%) and Design Cost-Optimized Architectures (20%). "Most cost-effective compute for event-driven workloads" questions almost always point to Lambda.

*   **Lambda vs. EC2 vs. Fargate:** Lambda is the answer for short-duration, event-driven, stateless functions (under 15 minutes). EC2 is the answer for long-running processes, stateful applications, or workloads requiring OS-level access. Fargate is the answer for containerized applications that need more than 15 minutes or more than 10 GB of memory.

*   **Lambda Timeout Trap:** Lambda has a maximum execution timeout of 15 minutes. Any workload described as "processing jobs that run for multiple hours" cannot use Lambda — use EC2, ECS/Fargate, or AWS Batch instead.

*   **SQS + Lambda for Decoupling:** A very common SAA-C03 pattern is SQS → Lambda: SQS buffers messages (handles traffic spikes), and Lambda polls SQS to process messages asynchronously. This decouples the producer from the consumer and provides built-in retry with Dead Letter Queue (DLQ) support for failed messages.

*   **Lambda@Edge vs. CloudFront Functions:** Lambda@Edge runs Node.js or Python functions at CloudFront edge locations for request/response manipulation with up to 30 seconds timeout. CloudFront Functions run lightweight JavaScript at edge locations with sub-millisecond execution — suited for header manipulation and URL rewrites. The exam distinguishes these by execution time and complexity.

*   **Study Resource:** The Lambda Developer Guide covers the full execution model, event sources, and best practices: [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). The "Best practices for working with AWS Lambda functions" section is directly exam-relevant.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the Lambda chapter in the AWS Solutions Architect study materials. Review the [AWS Serverless Application Model (SAM) overview](https://aws.amazon.com/serverless/sam/) for how Lambda integrates with API Gateway, DynamoDB, and S3 in a complete serverless application. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Serverless Architectures with AWS Lambda" whitepaper — required reading for SAA-C03 serverless scenarios.

*   **Required Video:** Watch the Lambda and API Gateway module in the official course playlist, focusing on the invocation models (synchronous, asynchronous, poll-based), concurrency limits, and the canonical API Gateway → Lambda → DynamoDB serverless pattern: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create and invoke a Lambda function from S3:** Write a Python Lambda function that reads an uploaded S3 object, processes its content, and writes a result to DynamoDB. Configure an S3 Event Notification to invoke the function on `s3:ObjectCreated:*` events. Upload a test file and verify the DynamoDB entry.

*   **Build a serverless API with API Gateway and Lambda:** Create an HTTP API in API Gateway, create a Lambda integration for the GET /items route, and deploy the API. Test with curl or Postman that the Lambda function receives the request and returns a JSON response.

*   **Configure a Dead Letter Queue for Lambda:** Attach an SQS Dead Letter Queue to an async Lambda invocation configuration. Trigger a deliberate failure in the Lambda code and verify that after the configured retry count, the event lands in the DLQ for investigation.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Understand Lambda invocation models at [https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html).
- [ ] Review Lambda limits (timeout, memory, concurrency) at [https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
- [ ] Watch the Lambda/serverless video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab building a serverless application with S3 triggers, API Gateway, and DLQ.
- [ ] Proceed to the weekly quiz.
