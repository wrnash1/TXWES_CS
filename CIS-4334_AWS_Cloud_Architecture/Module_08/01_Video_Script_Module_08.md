# Video Script: Module 08 - Lambda and Serverless Architecture

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 08: Lambda and Serverless Architecture.

AWS Lambda is the foundational service of the AWS serverless computing model. It is tested heavily on the SAA-C03 exam because it represents a fundamentally different approach to running application code — no servers to manage, automatic scaling, and pay-per-execution pricing. Understanding Lambda, how it integrates with other AWS services, and when to choose it over EC2 is essential exam knowledge.

By the end of this module you will be able to:

- Explain the Lambda execution model including invocation types, execution environment lifecycle, and cold start behavior
- Identify the event sources that can trigger Lambda functions and their invocation types
- Configure Lambda with appropriate memory, timeout, and concurrency settings
- Integrate Lambda with S3, API Gateway, DynamoDB Streams, SQS, and SNS
- Explain the serverless application pattern using Lambda, API Gateway, and DynamoDB together
- Identify when Lambda is the right compute choice versus EC2 or containers
- Describe Lambda@Edge and its use in CloudFront-integrated architectures

---

## [01:30 - 06:00] Lambda Execution Model

[SHOW DIAGRAM]

AWS Lambda runs code in response to events. You upload your function code, configure the runtime, and Lambda handles all the underlying compute infrastructure — provisioning servers, scaling, patching, and availability.

The core execution model has several key components.

A Lambda function is a piece of code packaged with its dependencies and configuration. The function has a runtime (Python, Node.js, Java, Go, .NET, Ruby, or a custom runtime), a handler (the entry point function that Lambda calls), and configuration for memory, timeout, and environment variables.

When an event triggers the function, Lambda creates an execution environment — a secure, isolated container running on AWS-managed infrastructure. The execution environment initializes the runtime, loads the function code, and calls the handler with the event object. This initialization phase is called the cold start, and it typically adds 100 milliseconds to several seconds of latency depending on the runtime and the size of the deployment package.

After the handler returns, the execution environment is not immediately destroyed. Lambda may reuse it for subsequent invocations — this is called a warm start and has no initialization overhead. Any objects initialized outside the handler function (database connections, SDK clients, configuration values) persist across warm invocations within the same execution environment.

[SHOW DIAGRAM]

Lambda function configuration options:

Memory: from 128 MB to 10,240 MB in 1 MB increments. CPU allocation scales proportionally with memory — there is no separate CPU setting. A function with 1,769 MB of memory receives one full vCPU. A function that is CPU-bound benefits from increasing memory even if it does not need the extra RAM.

Timeout: from 1 second to 15 minutes maximum. Lambda is not designed for long-running processes. If your workload runs longer than 15 minutes, it should use EC2, ECS/Fargate, or AWS Batch instead.

Concurrency: Lambda scales by running multiple execution environments simultaneously. Reserved concurrency caps a function's maximum concurrent invocations. Provisioned concurrency pre-warms a specified number of execution environments, eliminating cold starts for latency-sensitive applications.

---

## [06:00 - 10:30] Invocation Types and Event Sources

[SHOW DIAGRAM]

Lambda functions are invoked in one of three ways:

Synchronous invocation: the caller waits for the function to complete and receives the response. API Gateway, Application Load Balancer, and direct SDK invocations use synchronous invocation. Error handling is the caller's responsibility.

Asynchronous invocation: the caller sends the event and Lambda returns immediately without waiting for the function to finish. S3 event notifications, SNS, and EventBridge use asynchronous invocation. Lambda retries failed asynchronous invocations up to two additional times. After all retries are exhausted, the event can be sent to a Dead Letter Queue (SQS or SNS) for investigation.

Event source mapping (stream and queue polling): Lambda polls the event source and processes batches of records. DynamoDB Streams, Kinesis Data Streams, and SQS queues use event source mapping. Failures with SQS return messages to the queue and eventually to the SQS DLQ.

[SHOW DIAGRAM]

Common event sources and their invocation types:

Amazon S3 triggers Lambda asynchronously. When an object is created, deleted, or modified, S3 publishes an event notification to Lambda. The event contains the bucket name, object key, and event type. Always URL-decode the object key in your function — S3 encodes special characters in keys.

Amazon API Gateway triggers Lambda synchronously. API Gateway routes HTTP requests to Lambda functions. Each route maps to a Lambda handler. API Gateway manages authentication, throttling, SSL, and request transformation. This is the serverless REST API pattern.

DynamoDB Streams uses event source mapping. Lambda polls the stream and processes batches of item change records. Used for real-time downstream processing of database changes.

SQS uses event source mapping. Lambda polls the queue and processes batches of messages. When processing fails, messages return to the queue and eventually go to the SQS DLQ.

SNS triggers Lambda asynchronously. SNS pushes notification events directly to Lambda. Used for fan-out patterns where one message triggers multiple Lambda functions.

---

## [10:30 - 14:30] Serverless Application Patterns

[SHOW DIAGRAM]

The classic serverless web application pattern combines three services: API Gateway, Lambda, and DynamoDB.

A client sends an HTTP request to an API Gateway endpoint. API Gateway authenticates the request, then routes it to the appropriate Lambda function. The Lambda function processes the request — reading from or writing to a DynamoDB table — and returns a response to API Gateway, which formats and sends the HTTP response back to the client.

This architecture is entirely serverless: no EC2 instances to manage, no fixed capacity to provision, scales automatically from zero to millions of requests, and you pay only for actual invocations.

[SHOW DIAGRAM]

A second common pattern is event-driven file processing:

A user uploads a file to an S3 bucket. S3 publishes an event notification to a Lambda function. The Lambda function processes the file — resizing an image, parsing a CSV, extracting metadata — and stores the result in S3, DynamoDB, or another service. The original file upload triggers the entire pipeline without any polling or scheduling.

[SHOW DIAGRAM]

A third pattern is queue-based decoupling with SQS and Lambda:

An application writes messages to an SQS queue instead of directly calling a processing Lambda. Lambda polls the queue and processes messages in batches. This decouples the message producer from the processor, handles traffic spikes gracefully (messages queue up rather than throttle), and provides automatic retry and DLQ support for failed processing.

---

## [14:30 - 18:30] Lambda Permissions and Security

[SHOW DIAGRAM]

Lambda security has two sides: what can invoke the function, and what the function can do.

Execution role: every Lambda function has an IAM execution role. When the function runs, it assumes this role and uses its permissions to make AWS API calls. The execution role must grant only the permissions the function needs — least privilege applies. A function that reads from S3 and writes to DynamoDB needs s3:GetObject and dynamodb:PutItem permissions, not s3:* or AdministratorAccess.

Resource-based policy: Lambda functions have a resource-based policy that controls which AWS services and accounts are allowed to invoke the function. When you configure an S3 bucket to send events to Lambda, the function policy grants s3.amazonaws.com the lambda:InvokeFunction action, scoped to the specific bucket ARN.

[SHOW DIAGRAM]

VPC integration: by default, Lambda functions run in a Lambda-managed VPC with internet access. If a function must access resources inside a customer VPC — an RDS database, an ElastiCache cluster, an internal API — configure the function with a VPC, subnets, and a security group. Lambda creates an elastic network interface in the specified subnet.

Be aware that Lambda in a VPC loses its default internet access. If the function also needs internet access, add a NAT Gateway to the VPC and route the private subnet's 0.0.0.0/0 traffic through it. Placing Lambda in a public subnet does not restore internet access — Lambda ENIs do not receive public IP addresses.

---

## [18:30 - 22:00] Lambda@Edge and Container Images

Lambda@Edge runs Lambda functions at CloudFront edge locations. Instead of running in a single region, the function executes at the edge location closest to the user. Lambda@Edge can be triggered at four points in the CloudFront request lifecycle: viewer request, origin request, origin response, and viewer response.

Use cases for Lambda@Edge include URL rewriting, security header injection, A/B testing, and lightweight authentication at the edge. Lambda@Edge functions have stricter limits: maximum 5 seconds for viewer triggers, 30 seconds for origin triggers, and no VPC access.

Lambda also supports deploying functions as container images up to 10 GB in size. The container image must implement the Lambda Runtime Interface. This allows teams to use existing Docker-based build pipelines and deploy larger dependency packages that exceed the 50 MB zip deployment limit.

---

## [22:00 - 24:00] Module Summary

AWS Lambda is a serverless compute service that runs code in response to events without requiring infrastructure management. Execution environments have a lifecycle: cold start initialization and warm reuse. Memory and CPU scale together, and the maximum function timeout is 15 minutes.

Invocation types: synchronous (API Gateway, ALB), asynchronous (S3, SNS, EventBridge with automatic retry and DLQ), and event source mapping (SQS, DynamoDB Streams, Kinesis with batch processing).

Key patterns: serverless API (API Gateway + Lambda + DynamoDB), event-driven file processing (S3 + Lambda), queue-based decoupling (SQS + Lambda).

Security: execution role defines what the function can do; resource-based policy defines who can invoke the function. Lambda in a VPC loses internet access and requires a NAT Gateway for outbound connectivity.

Lambda@Edge runs functions at CloudFront edge locations for geographically distributed request processing.

For your certification study: <aws.amazon.com/certification>

---

End of Module 08 Video Script
