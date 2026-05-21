# Reading Guide: Module 10 - SQS, SNS, and Event-Driven Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 10 - SQS, SNS, and Event-Driven Architecture**! Decoupled, event-driven architectures are a central pattern for building scalable and resilient AWS applications. This module covers Amazon SQS (Simple Queue Service) for durable message buffering, Amazon SNS (Simple Notification Service) for pub/sub fan-out, and Amazon EventBridge for event-driven routing between services. Together, these services enable systems where producers and consumers are independent, traffic spikes are absorbed, and failures are isolated. Event-driven integration patterns are heavily tested on the SAA-C03 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Amazon SQS (Simple Queue Service)**: A fully managed message queuing service that decouples the components of a distributed application. Producers send messages to the queue; consumers poll the queue and process messages independently. SQS Standard Queues provide at-least-once delivery with best-effort ordering (high throughput, no ordering guarantees). SQS FIFO Queues guarantee exactly-once processing and strict first-in, first-out ordering (up to 300 TPS, or 3,000 TPS with batching). Messages are retained for up to 14 days and can be up to 256 KB.

*   **SQS Visibility Timeout**: The period after a consumer receives a message during which the message is invisible to other consumers. This prevents duplicate processing while a consumer is working on the message. If the consumer fails to delete the message before the timeout expires, the message becomes visible again for another consumer to process. Setting the visibility timeout too short relative to processing time causes duplicate processing; too long delays retry after consumer failure.

*   **Amazon SNS (Simple Notification Service)**: A fully managed pub/sub messaging service. Publishers send messages to an SNS Topic; subscribers (SQS queues, Lambda functions, HTTP endpoints, email, SMS, mobile push) receive a copy of each message. SNS is push-based — it delivers messages to all subscribers simultaneously. This fan-out pattern enables a single event (e.g., order placed) to trigger multiple downstream workflows (e.g., inventory deduction, email confirmation, analytics pipeline) in parallel.

*   **SNS + SQS Fan-Out Pattern**: A common architecture where an SNS Topic delivers to multiple SQS Queues as subscribers. Each queue feeds a different downstream consumer (e.g., Lambda function, EC2 worker). This enables parallel, independent processing of the same event by multiple consumers, with each consumer's SQS queue providing durable buffering and retry if the consumer is slow or temporarily unavailable.

*   **Amazon EventBridge**: A serverless event bus that routes events from AWS services, SaaS applications, and custom applications to targets (Lambda, Step Functions, SQS, SNS, etc.) based on event pattern rules. EventBridge replaces CloudWatch Events for custom event routing and provides schema registry, event replay, and cross-account/cross-Region event routing. EventBridge is the preferred decoupling mechanism for event-driven architectures that need flexible routing rules.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** SQS, SNS, and EventBridge appear in Design Resilient Architectures (26%) and Design High-Performing Architectures (24%). Decoupling and fan-out patterns appear in a large percentage of application architecture scenario questions.

*   **SQS Standard vs. FIFO Exam Selection:** The exam will describe a workload and ask which queue type to use. Exactly-once processing and ordering required → SQS FIFO. Maximum throughput, ordering not required → SQS Standard. FIFO is more expensive and has lower TPS limits, so do not over-specify it.

*   **SQS vs. SNS Exam Trap:** SQS = pull-based queue for one consumer (or competing consumers). SNS = push-based for fan-out to multiple subscribers simultaneously. The distinguishing factor: "fan out to multiple consumers in parallel" → SNS (or SNS+SQS). "Queue messages for a single processing pool" → SQS.

*   **Dead Letter Queue (DLQ):** When a message fails processing more than the configured maximum receive count, SQS moves it to a DLQ. This prevents poison pills (malformed messages) from blocking the queue indefinitely. Both Standard and FIFO queues support DLQs. Lambda also supports DLQ/failure destinations for async invocations.

*   **Long Polling vs. Short Polling:** SQS short polling (default) queries a subset of servers immediately and returns even if no messages are available, wasting API calls. Long polling waits up to 20 seconds for a message to arrive, reducing empty responses and costs. Always use long polling in production (`WaitTimeSeconds=20`).

*   **Study Resource:** The SQS and SNS developer guides cover all queue types, delivery models, and best practices: [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) and [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the SQS, SNS, and EventBridge chapters in the AWS Solutions Architect study materials. Review the [Amazon SQS FAQs page](https://aws.amazon.com/sqs/faqs/) for the Standard vs. FIFO comparison. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Implementing Microservices on AWS" whitepaper, which covers decoupled event-driven patterns extensively.

*   **Required Video:** Watch the SQS, SNS, and event-driven architecture module in the official course playlist, focusing on the SNS+SQS fan-out pattern and the DLQ configuration: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create an SQS Standard Queue and test message visibility:** Send 5 messages to the queue using the AWS CLI (`aws sqs send-message`). Receive one message (`aws sqs receive-message`), note the receipt handle, and observe that the message disappears from view during the visibility timeout. Verify it reappears after the timeout expires.

*   **Configure SNS fan-out with two SQS subscriber queues:** Create an SNS Topic, create two SQS queues as subscribers, and publish a test message to the SNS Topic. Verify that both SQS queues each receive a copy of the message independently.

*   **Configure a Dead Letter Queue for failed processing:** Create an SQS DLQ, configure the source queue to move messages to the DLQ after 3 receive attempts. Receive a message from the source queue without deleting it, repeat until the DLQ receives it, and verify the message payload in the DLQ.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Understand SQS Standard vs. FIFO at [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html).
- [ ] Review the SNS+SQS fan-out pattern at [https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html](https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html).
- [ ] Watch the SQS/SNS/event-driven architecture video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab with SQS queues, SNS fan-out, and DLQ configuration.
- [ ] Proceed to the weekly quiz.
