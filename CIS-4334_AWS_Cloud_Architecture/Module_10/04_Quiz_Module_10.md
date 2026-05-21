# Quiz: Module 10 - SQS, SNS, and Event-Driven Architecture
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A company processes customer orders. When an order is placed, it must trigger three independent workflows simultaneously: deduct inventory, send a confirmation email, and publish an analytics event. Which AWS architecture pattern best implements this?
*   A) Send the order event to a single SQS Standard Queue; three separate Lambda functions poll the same queue and each process the order.
*   B) Publish the order event to an SNS Topic with three SQS Queues as subscribers; each queue feeds an independent consumer for inventory, email, and analytics.
*   C) Write the order to an RDS database and have three scheduled Lambda functions query for new records every 60 seconds.
*   D) Use Amazon EventBridge to send the order event directly to three Lambda functions using a single rule that targets all three functions simultaneously.
*   **Correct Answer:** B) The SNS-to-SQS fan-out pattern delivers a copy of the order event to each SQS queue, allowing three independent, isolated processing pipelines to run in parallel with durable buffering.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single SQS queue with competing consumers means each message is received by only ONE consumer (the first to receive it). Inventory, email, and analytics cannot all receive the same message from the same SQS queue — each message is consumed by exactly one consumer in a competing-consumer model.
    *   *Why B is correct:* This is the canonical SNS fan-out pattern. SNS delivers a copy of each message to every subscribed SQS queue. Each queue provides independent, durable buffering for its downstream consumer. If the email service is slow, its queue grows while inventory and analytics proceed unaffected — true decoupling.
    *   *Why C is incorrect:* Polling a relational database every 60 seconds introduces up to 60 seconds of processing latency and creates database load from three polling processes. This is a database anti-pattern for event-driven workflows and violates the real-time processing expectation.
    *   *Why D is incorrect:* EventBridge rules can target multiple targets simultaneously, which is a valid fan-out pattern. However, EventBridge does not provide durable message buffering — if a Lambda function is throttled or fails, the event is not retried with the same durability guarantees as SQS. For durable decoupling, SNS+SQS is the more reliable answer for this scenario.

---

**Question 2**
Which of the following is the most accurate description of the difference between **SQS Standard Queues** and **SQS FIFO Queues**?
*   A) Standard Queues guarantee strict message ordering and exactly-once delivery; FIFO Queues provide best-effort ordering and at-least-once delivery for higher throughput.
*   B) Standard Queues offer maximum throughput with best-effort ordering and at-least-once delivery; FIFO Queues guarantee strict message ordering and exactly-once processing, at lower maximum throughput.
*   C) Standard Queues support only a single consumer; FIFO Queues support multiple competing consumers processing messages in parallel.
*   D) Standard Queues and FIFO Queues are functionally identical; the difference is that FIFO Queues charge a higher per-message rate.
*   **Correct Answer:** B) Standard Queues maximize throughput with at-least-once delivery and best-effort ordering; FIFO Queues guarantee exactly-once processing and strict FIFO order at lower TPS limits.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the definitions. Standard Queues have at-least-once delivery and best-effort ordering. FIFO Queues have exactly-once and strict ordering. The real descriptions are the opposite of this answer.
    *   *Why B is correct:* This is the exact SAA-C03 distinction. Standard Queues are nearly unlimited throughput, suitable for workloads where duplicate processing can be handled idempotently. FIFO Queues (up to 300 TPS, 3,000 with batching) are for workloads that absolutely cannot tolerate duplicates or out-of-order processing, such as financial transactions.
    *   *Why C is incorrect:* Both Standard and FIFO Queues support multiple consumers. FIFO Queues use message groups to enable parallelism while maintaining order within each group.
    *   *Why D is incorrect:* While FIFO Queues do cost more per request, the functional differences (ordering guarantees, exactly-once delivery, TPS limits) are fundamental, not cosmetic. They are designed for different use cases.

---

**Question 3**
A payment processing application sends payment commands to an SQS queue. The processing Lambda function fails on some messages due to malformed payment data. These failed messages keep reappearing in the queue and blocking healthy messages. Which SQS configuration prevents poison pill messages from indefinitely blocking the queue?
*   A) Set the SQS message retention period to 1 hour so failed messages expire quickly.
*   B) Configure a Dead Letter Queue (DLQ) with a maximum receive count; messages exceeding the retry limit are moved to the DLQ for investigation.
*   C) Enable SQS Long Polling to reduce the frequency at which failed messages are received.
*   D) Increase the SQS visibility timeout to 24 hours to give the Lambda function more time to process difficult messages.
*   **Correct Answer:** B) A Dead Letter Queue with a configured maximum receive count automatically moves messages that repeatedly fail processing to the DLQ, isolating poison pills without blocking healthy messages.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Reducing the retention period causes failed messages to expire (be deleted) before they can be investigated and corrected. This destroys data rather than isolating it for diagnosis.
    *   *Why B is correct:* The DLQ is the standard SQS poison pill solution. After a message is received more than the `maxReceiveCount` times without successful deletion (indicating repeated processing failure), SQS moves it to the DLQ. Engineers can inspect the DLQ to diagnose the malformed data and re-process corrected messages without disrupting the main queue.
    *   *Why C is incorrect:* Long Polling reduces empty receive calls (no messages available) to save API costs. It does not change retry behavior for failed messages — a poison pill message with a short visibility timeout still reappears repeatedly regardless of polling mode.
    *   *Why D is incorrect:* Increasing visibility timeout to 24 hours means a failed message is invisible to other consumers for 24 hours. If the Lambda function crashes, the message is stuck for 24 hours before becoming processable again — worsening the blocking problem, not solving it.

---

**Question 4**
A company uses SQS to buffer messages from an e-commerce application to a warehouse inventory system. During a flash sale, 50,000 orders arrive within 2 minutes, but the warehouse system can only process 200 orders per minute. How does SQS help this architecture remain resilient during the spike?
*   A) SQS automatically scales the warehouse processing Lambda to match the incoming order volume.
*   B) SQS absorbs the burst by retaining up to 120,000 messages in the queue; the warehouse system processes at its own rate (200/min) until the queue drains, with messages retained for up to 14 days.
*   C) SQS rejects messages once the queue depth exceeds a defined threshold, preventing the warehouse system from being overloaded.
*   D) SQS immediately forwards all 50,000 messages to the warehouse system simultaneously, relying on the system's internal rate limiting to drop excess messages.
*   **Correct Answer:** B) SQS acts as an elastic buffer — it durably stores all incoming messages and allows the downstream consumer to process them at its own sustainable rate, completely decoupling the producer's write throughput from the consumer's read throughput.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SQS does not scale Lambda or any downstream compute service. SQS stores messages; a separate Auto Scaling or concurrency configuration handles scaling the consumers. When Lambda polls SQS, Lambda's concurrent executions scale based on queue depth, but this is Lambda Auto Scaling — not SQS Auto Scaling.
    *   *Why B is correct:* This is the fundamental value proposition of SQS for spiky workloads. The queue absorbs the burst (50,000 messages) and holds them durably while the warehouse system processes at its capacity (200/min). The 50,000 messages will be processed in approximately 250 minutes — no messages are lost, and the warehouse system is never overwhelmed.
    *   *Why C is incorrect:* SQS does not reject messages based on queue depth (within normal limits). The standard queue can hold up to 120,000 in-flight messages plus unlimited visible messages. Message rejection would cause data loss — the opposite of what SQS is designed to do.
    *   *Why D is incorrect:* SQS is a pull-based service — consumers poll for messages at their own rate. SQS does not push all messages simultaneously to the consumer. There is no "forward all at once" behavior in SQS.

---

**Question 5**
A data pipeline publishes events to an SNS Topic whenever a new analytics report is generated. Three teams subscribe to receive the events: Team A using Lambda, Team B using SQS, and Team C using an HTTPS endpoint. Team C's HTTPS endpoint is down for maintenance for 2 hours. What happens to Team C's events during the outage?
*   A) SNS retries delivery to Team C's HTTPS endpoint for up to 23 days using exponential backoff; events that cannot be delivered after the retry period are discarded or sent to an SNS DLQ if configured.
*   B) SNS pauses delivery to all subscribers until Team C's endpoint recovers to maintain event order consistency.
*   C) SNS automatically buffers undeliverable events for Team C in an internal queue and delivers them in bulk when the endpoint recovers.
*   D) SNS switches Team C to email delivery automatically when HTTPS delivery fails, ensuring events are not lost.
*   **Correct Answer:** A) SNS retries HTTP/HTTPS endpoint delivery with exponential backoff for an extended period. Events that exhaust the retry policy are discarded unless an SNS Dead Letter Queue is configured for the subscription.
*   **Distractor Analysis:**
    *   *Why A is correct:* SNS has a built-in retry policy for HTTP/HTTPS subscriptions with multiple phases: immediate retries, pre-backoff, backoff, and post-backoff phases totaling up to 23 days of delivery attempts with exponential backoff. For guaranteed durability, a DLQ should be attached to the subscription. Note that Team A (Lambda) and Team B (SQS) are unaffected by Team C's outage — SNS fan-out is independent per subscriber.
    *   *Why B is incorrect:* SNS delivers to each subscriber independently. An unhealthy subscriber does not pause or affect delivery to other subscribers. Team A and Team B receive their events immediately regardless of Team C's status.
    *   *Why C is incorrect:* SNS does not buffer failed delivery in an internal persistent queue. It retries using its retry policy, but without a configured DLQ, events that exhaust all retries are permanently lost. SNS is not designed as a durable queue (that is SQS's role) — SNS+SQS fan-out solves this by giving each subscriber its own SQS queue.
    *   *Why D is incorrect:* SNS does not automatically switch delivery protocols for failed subscriptions. If the HTTPS endpoint fails, SNS retries HTTPS delivery according to the retry policy. It does not fall back to email or any other protocol without explicit configuration.

