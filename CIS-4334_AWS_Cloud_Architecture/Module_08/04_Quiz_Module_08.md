# Quiz: Module 08 - Lambda and Serverless Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A company needs to process images uploaded to S3 — generating thumbnails within seconds of upload. The processing job completes in under 2 minutes. Which compute solution is most operationally efficient and cost-effective?
*   A) A fleet of EC2 instances with Auto Scaling that poll S3 for new objects every 60 seconds.
*   B) An AWS Lambda function triggered by S3 Event Notifications (`s3:ObjectCreated:*`), processing each image in a separate Lambda invocation.
*   C) An Amazon ECS Fargate task running continuously that monitors an SQS queue for S3 object upload events.
*   D) An AWS Glue ETL job scheduled to run every 5 minutes to process any new S3 objects.
*   **Correct Answer:** B) Lambda with S3 Event Notifications provides immediate, per-object invocation without idle server costs — the canonical serverless event-driven pattern for S3 processing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A polling EC2 fleet introduces latency (up to 60 seconds before detection), wastes money on idle instances between uploads, and requires Auto Scaling configuration, patching, and management. Lambda's event-driven model is far simpler and more cost-effective for short-duration per-object processing.
    *   *Why B is correct:* S3 Event Notifications invoke Lambda automatically within milliseconds of an object upload. Each image is processed in an isolated Lambda invocation. You pay only for the compute time used. No servers to manage, no idle cost, no polling delay.
    *   *Why C is incorrect:* Fargate is appropriate for containerized workloads requiring more than Lambda's resource limits (>15 min, >10 GB memory). Running Fargate continuously for a 2-minute image processing job wastes compute and adds container orchestration overhead vs. the simpler Lambda approach.
    *   *Why D is incorrect:* AWS Glue is designed for large-scale ETL data transformation jobs, not real-time image processing. A 5-minute polling interval violates the "within seconds" requirement. Glue is also significantly more expensive for small, frequent jobs.

---

**Question 2**
Which of the following is the most accurate description of a **Lambda Cold Start**?
*   A) An error state where a Lambda function receives more requests than its configured concurrency limit and begins throttling new invocations.
*   B) The initialization latency that occurs when Lambda creates a new execution environment for a function — loading the runtime, code package, and initialization code — before the handler function can execute.
*   C) A billing model where Lambda charges a higher rate for the first 1 million invocations per month before applying the standard free-tier rate.
*   D) A Lambda deployment stage where the function code is validated and compiled before being made available for invocations.
*   **Correct Answer:** B) A cold start is the initialization overhead incurred when Lambda provisions a new execution environment — including runtime startup and function initialization code — before the actual handler is invoked.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Lambda throttling, which occurs when concurrent executions exceed the account/function limit. Throttled invocations receive a 429 error, not a cold start. These are distinct phenomena.
    *   *Why B is correct:* Cold starts are a key Lambda operational concern for the SAA-C03 exam. The duration depends on runtime (Java/C# have longer cold starts than Python/Node.js), package size, and VPC configuration (VPC Lambda has additional ENI attachment time). Provisioned Concurrency pre-initializes environments to eliminate cold starts for latency-sensitive applications.
    *   *Why C is incorrect:* Lambda pricing is based on invocation count and duration. The free tier covers 1 million invocations and 400,000 GB-seconds per month, but there is no "cold start billing rate" — cold starts are a latency issue, not a billing tier.
    *   *Why D is incorrect:* Lambda validates and packages function code at deployment time, but this is the deployment process, not a cold start. Cold starts happen at runtime invocation time, not at deployment.

---

**Question 3**
A company builds a serverless order processing system. Orders are placed at variable rates — quiet overnight, spiky during lunch and peak hours. The system must not lose orders during spikes and must process each order exactly once. Which architecture best satisfies these requirements?
*   A) API Gateway → Lambda directly. Lambda's auto-scaling handles any spike without message buffering.
*   B) API Gateway → SQS Standard Queue → Lambda (SQS as event source). SQS buffers orders during spikes, Lambda polls and processes them, and DLQ captures any failures.
*   C) API Gateway → SNS → Lambda. SNS fans out order events and Lambda processes each notification.
*   D) API Gateway → Kinesis Data Stream → Lambda. Kinesis provides ordered, replay-capable streaming with exactly-once semantics.
*   **Correct Answer:** B) SQS Standard Queue buffers orders during traffic spikes, Lambda processes them at a controlled rate, and the Dead Letter Queue captures failed processing attempts for investigation — providing durable, reliable order processing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Direct API Gateway → Lambda invocation without a queue means that if Lambda is throttled during a spike, orders are dropped. There is no durability or retry mechanism for the order messages themselves.
    *   *Why B is correct:* SQS + Lambda is the canonical decoupled, durable event processing pattern on SAA-C03. SQS retains messages for up to 14 days, automatically retries failed Lambda invocations, and routes persistently failing messages to a DLQ. SQS FIFO queues provide exactly-once processing if the ordering requirement is strict.
    *   *Why C is incorrect:* SNS is a push-based pub/sub service — it pushes notifications to subscribers with limited retry logic. If Lambda is throttled during a spike, SNS may drop messages. SNS is suited for fan-out notifications, not durable work queue processing.
    *   *Why D is incorrect:* Kinesis Data Streams provides ordered, replay-capable streaming, but exactly-once semantics in Kinesis require careful deduplication logic at the consumer. For simple order processing, SQS FIFO with Lambda is simpler and provides native exactly-once delivery. Kinesis is better suited for high-volume streaming analytics.

---

**Question 4**
A Lambda function is deployed inside a VPC to access a private RDS database. Operations staff report that the function takes 8–10 seconds on first invocation after periods of inactivity. Subsequent invocations in quick succession complete in under 100 milliseconds. What is the cause of the slow first invocations, and what is the recommended solution?
*   A) The RDS database has an idle connection timeout; increase the `max_allowed_packet` parameter in the RDS parameter group.
*   B) VPC-enabled Lambda functions experience longer cold starts due to ENI (Elastic Network Interface) attachment during environment initialization. Enable Provisioned Concurrency to pre-initialize the execution environment and eliminate cold start latency.
*   C) The Lambda function's memory allocation is too low, causing CPU throttling on first invocation. Increase memory to 3,008 MB.
*   D) The Lambda deployment package is too large; reduce the package size by removing unused libraries.
*   **Correct Answer:** B) VPC Lambda cold starts are longer than non-VPC Lambda because the execution environment must attach an ENI to the VPC before the function can run. Provisioned Concurrency pre-initializes the environment, eliminating the cold start delay.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* RDS connection timeouts affect established connections, not Lambda invocation latency. The symptom (slow only on first invocation, fast on subsequent) is the cold start pattern, not a database connection issue.
    *   *Why B is correct:* VPC Lambda historically had 10+ second cold starts due to ENI provisioning. AWS improved this with the "Hyperplane ENI" model, but VPC Lambda still has longer cold starts than non-VPC Lambda. Provisioned Concurrency is the AWS-recommended solution for latency-sensitive VPC Lambda functions, keeping environments warm and ready.
    *   *Why C is incorrect:* Lambda CPU is allocated proportionally to memory, so insufficient memory could slow execution, but it would not cause a specific pattern of slow first invocations followed by fast subsequent ones. That pattern is the cold start signature.
    *   *Why D is incorrect:* Package size contributes to cold start duration because Lambda must download and extract the package. However, the dominant factor for VPC Lambda cold starts is the ENI attachment, not package size. Reducing package size helps but does not eliminate VPC cold starts the way Provisioned Concurrency does.

---

**Question 5**
A Lambda function processes files uploaded to S3 but occasionally fails with transient errors (e.g., downstream API timeouts). Failed invocations should not be permanently lost, and engineers need to review and retry failed events manually. Which configuration achieves this with the least operational overhead?
*   A) Configure the Lambda function to write failed event data to a log file in the function's local `/tmp` storage for manual review.
*   B) Configure a Dead Letter Queue (DLQ) — either SQS or SNS — as the Lambda asynchronous invocation failure destination. Failed events are routed to the DLQ after the configured retry attempts, where they can be reviewed and replayed.
*   C) Increase the Lambda timeout to 15 minutes to allow sufficient time for the downstream API to recover.
*   D) Wrap the Lambda handler in a try/catch block and log errors to CloudWatch Logs; engineers can re-trigger failed invocations from CloudWatch.
*   **Correct Answer:** B) A Dead Letter Queue captures failed asynchronous Lambda invocations after all retries are exhausted, providing durable storage of the failed event payload for manual inspection and replay.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Lambda's local `/tmp` storage is ephemeral — it does not persist between invocations and is not accessible after the execution environment is recycled. Failed event data written to `/tmp` is permanently lost when the environment is destroyed.
    *   *Why B is correct:* The DLQ is the native Lambda mechanism for durably capturing failed asynchronous invocations. Asynchronous Lambda invocations (triggered by S3 Event Notifications) retry twice by default before routing to the DLQ. Engineers can inspect the SQS DLQ messages (which contain the original event payload) and redrive them after fixing the root cause.
    *   *Why C is incorrect:* Extending the timeout to 15 minutes for transient downstream API errors introduces unnecessary waiting and wastes Lambda compute time. Transient errors should be handled with retries and DLQ, not extended timeouts.
    *   *Why D is incorrect:* Logging errors to CloudWatch captures the error message but does not preserve the original event payload in a retrievable, replayable form. Engineers cannot easily "re-trigger" specific invocations from CloudWatch Logs — it is an observability tool, not a message queue.

