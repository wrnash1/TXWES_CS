# Lab Activity: Module 10 — SQS, SNS, and Event-Driven Architecture

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Time:** 60–75 minutes
**Instructor:** Professor Nash

---

## Objectives

By the end of this lab you will be able to:

- Create SQS Standard and FIFO queues and configure visibility timeout, long polling, and a Dead-Letter Queue
- Build an SNS topic and subscribe two SQS queues to demonstrate the fan-out pattern
- Observe message isolation between subscribers and DLQ redrive behavior
- Analyze architecture scenarios and select the correct messaging service for a given requirement

---

## Prerequisites

- AWS Management Console access with IAM permissions for SQS, SNS, and CloudWatch
- AWS CLI installed and configured (`aws configure`)
- A text editor for recording resource ARNs and queue URLs

---

## Part 1 — SQS Queue Configuration and Visibility Timeout

### Step 1.1 — Create the Source Queue

In the SQS console, create a Standard queue named `orders-processing`.

Set the following parameters:

- Visibility timeout: 30 seconds
- Message retention period: 4 days
- Receive message wait time: 20 seconds (enables long polling)

Record the queue URL. You will need it in subsequent steps.

### Step 1.2 — Create a Dead-Letter Queue

Create a second Standard queue named `orders-processing-dlq`. Use default settings — this queue requires no special configuration because it is the destination for failed messages.

Record the queue URL and ARN.

### Step 1.3 — Configure the Redrive Policy

Return to the `orders-processing` queue settings. In the Dead-letter queue section, enable the redrive policy:

- Set the DLQ to `orders-processing-dlq`
- Set `maxReceiveCount` to 3

This means: after a message has been received 3 times without being deleted, SQS moves it to the DLQ automatically.

### Step 1.4 — Send Test Messages via CLI

Send five messages to the source queue:

```bash
for i in 1 2 3 4 5; do
  aws sqs send-message \
    --queue-url <orders-processing-queue-url> \
    --message-body "{\"orderId\": \"ORD-00$i\", \"amount\": $((i * 25))}"
done
```

### Step 1.5 — Observe Visibility Timeout Behavior

Receive one message from the queue:

```bash
aws sqs receive-message \
  --queue-url <orders-processing-queue-url> \
  --wait-time-seconds 5
```

Record the `ReceiptHandle` from the response. Immediately attempt to receive another message from the same queue and observe that only 4 messages are visible — the received message is hidden during the visibility timeout.

Wait 35 seconds (longer than the 30-second visibility timeout) and receive again. Observe that the first message reappears, now with a new `ReceiptHandle`.

### Step 1.6 — Simulate DLQ Redrive

Receive the same message three more times without deleting it (the `ApproximateReceiveCount` attribute will increment with each receive). After the third receive, wait for the visibility timeout to expire.

Check the `orders-processing-dlq` queue for messages:

```bash
aws sqs receive-message \
  --queue-url <orders-processing-dlq-url> \
  --attribute-names All
```

Confirm the message has been moved to the DLQ and inspect its `ApproximateReceiveCount` attribute.

### Part 1 Analysis Questions

Answer these questions in your lab report:

1. What does the `ApproximateReceiveCount` attribute track and why is it the mechanism SQS uses to determine when to redirect to the DLQ?
2. A message processing function takes up to 8 minutes. The visibility timeout is set to 30 seconds. What problem does this cause and what is the correct configuration?
3. Why does SQS assign a new `ReceiptHandle` each time a message becomes visible and is received?

---

## Part 2 — SNS Fan-Out to SQS Queues

### Step 2.1 — Create Two Subscriber Queues

Create two Standard SQS queues:

- `inventory-service-queue`
- `analytics-service-queue`

Both should use default settings. Record both queue ARNs.

### Step 2.2 — Create an SNS Topic

In the SNS console, create a Standard topic named `order-events`.

Record the topic ARN.

### Step 2.3 — Subscribe Both Queues to the Topic

For each queue, create an SQS subscription on the `order-events` topic:

1. In the SNS console, choose Create subscription.
2. Set Protocol to Amazon SQS.
3. Enter the SQS queue ARN.
4. Leave the filter policy blank for now.

SNS will attempt to confirm the subscription. For SQS subscriptions, confirmation is automatic.

### Step 2.4 — Grant SNS Permission to Write to Each Queue

For each SQS queue, attach a queue policy that allows SNS to send messages. The policy must be added to the SQS queue's Access Policy, not the SNS topic policy.

The required statement for each queue:

```json
{
  "Effect": "Allow",
  "Principal": {
    "Service": "sns.amazonaws.com"
  },
  "Action": "sqs:SendMessage",
  "Resource": "<queue-arn>",
  "Condition": {
    "ArnEquals": {
      "aws:SourceArn": "<order-events-topic-arn>"
    }
  }
}
```

### Step 2.5 — Publish a Test Event to the SNS Topic

```bash
aws sns publish \
  --topic-arn <order-events-topic-arn> \
  --message '{"orderId": "ORD-0099", "customerId": "C-42", "amount": 199.99}' \
  --message-attributes '{"eventType": {"DataType": "String", "StringValue": "ORDER_PLACED"}}'
```

### Step 2.6 — Verify Fan-Out Delivery

Receive messages from both subscriber queues and verify that each received an identical copy of the order event:

```bash
aws sqs receive-message --queue-url <inventory-service-queue-url>
aws sqs receive-message --queue-url <analytics-service-queue-url>
```

Both queues should contain the same message body. This demonstrates the fan-out: one SNS publish resulted in two independent SQS deliveries.

### Step 2.7 — Add a Message Filter Policy

Return to the `analytics-service-queue` subscription in SNS. Add this filter policy:

```json
{
  "eventType": ["ORDER_PLACED"]
}
```

Publish a second message with `eventType = INVENTORY_UPDATED`:

```bash
aws sns publish \
  --topic-arn <order-events-topic-arn> \
  --message '{"itemSku": "SKU-888", "newQuantity": 50}' \
  --message-attributes '{"eventType": {"DataType": "String", "StringValue": "INVENTORY_UPDATED"}}'
```

Check both queues. The `inventory-service-queue` (no filter policy) receives the message. The `analytics-service-queue` (filter: `ORDER_PLACED` only) does not receive the `INVENTORY_UPDATED` message.

### Part 2 Analysis Questions

Answer these questions in your lab report:

1. You published one message to the SNS topic and both SQS queues each received a copy. Explain why this does not cause "duplicate processing" — how does each downstream service use its copy differently?
2. If the `analytics-service-queue` consumer is offline for 6 hours, what happens to the messages queued in `analytics-service-queue`? How does this differ from what would happen if the analytics service subscribed directly to the SNS topic without an SQS intermediary?
3. A new reporting service needs to receive all order events. Without SNS fan-out, what change would be required to the order-placement application code? With SNS fan-out, what is the only change required?

---

## Part 3 — Architecture Analysis

For each scenario below, identify the most appropriate AWS messaging service (SQS Standard, SQS FIFO, SNS, EventBridge, or Kinesis Data Streams) and justify your selection with specific service characteristics.

### Scenario A

A mobile game records player score events at a rate of 50,000 events per second. Three teams consume the data independently: the anti-cheat team, the leaderboard team, and the data science team. All three teams must be able to replay the last 7 days of events if they need to reprocess. No team's consumption affects the others.

Which service? ________________

Justification (write 3–5 sentences addressing throughput, multiple independent consumers, and replay capability):

### Scenario B

A bank processes wire transfers. Each transfer must be processed in exactly the order it was received per customer account. Duplicate processing of a single transfer is unacceptable — it would result in double-debiting customer accounts.

Which service? ________________

Justification (write 3–5 sentences addressing ordering requirements and duplicate prevention):

### Scenario C

An e-commerce platform needs to trigger five downstream services whenever a new order is placed: fraud detection, inventory reservation, shipment scheduling, customer notification, and revenue analytics. Each service needs durable, independent processing with automatic retry if it fails temporarily.

Which service? ________________

Justification (write 3–5 sentences addressing fan-out, durability, and consumer independence):

### Scenario D

An operations team wants to automatically remediate EC2 instances that transition to a stopped state unexpectedly. When any EC2 instance in the account changes state to "stopped," a Lambda function should immediately run a diagnostic and attempt restart.

Which service? ________________

Justification (write 3–5 sentences explaining why SNS or SQS cannot originate this trigger and what makes this service the correct choice):

---

## Deliverables

Submit to the Canvas assignment portal:

1. Screenshots of the SQS console showing the `orders-processing` queue configuration (visibility timeout, DLQ assignment, redrive policy).
2. CLI output showing the DLQ receiving the failed message from Step 1.6.
3. CLI output from Step 2.6 showing both queues receiving the fan-out message.
4. CLI output from Step 2.7 showing the filter policy preventing delivery to the analytics queue.
5. Written responses to all Part 1 and Part 2 analysis questions.
6. Architecture Analysis responses for Scenarios A through D (service selection and justification).

---

## Clean Up

To avoid ongoing charges, delete the following resources after completing the lab:

- SQS queues: `orders-processing`, `orders-processing-dlq`, `inventory-service-queue`, `analytics-service-queue`
- SNS topic: `order-events`
- SNS subscriptions (deleted automatically when topic is deleted)

---

## Part 9 — Challenge Exercise

### Challenge 1: Dead-Letter Queue Redrive and Poison Message Analysis
Practice identifying and recovering failed messages using DLQ redrive policies and the SQS console redrive feature.
1. Create a standard SQS queue named `challenge-processing` with a visibility timeout of 30 seconds and a maximum receive count of 2: `aws sqs create-queue --queue-name challenge-processing --attributes VisibilityTimeout=30,RedrivePolicy='{"deadLetterTargetArn":"<dlq-arn>","maxReceiveCount":"2"}'`. First create the DLQ: `aws sqs create-queue --queue-name challenge-dlq`.
2. Send three messages to `challenge-processing`: `aws sqs send-message --queue-url <url> --message-body "message-1"` (repeat for message-2 and message-3). Then receive and intentionally NOT delete two of the messages (let the visibility timeout expire twice) to simulate processing failures. After the second receive, verify both failed messages appear in the DLQ: `aws sqs get-queue-attributes --queue-url <dlq-url> --attribute-names ApproximateNumberOfMessages`.
3. Use the SQS console Redrive feature (or CLI: `aws sqs start-message-move-task --source-arn <dlq-arn> --destination-arn <source-queue-arn>`) to move the failed messages back to `challenge-processing` for reprocessing. Document the message move task ID and status.
4. Describe when you would NOT want to automatically redrive DLQ messages — identify at least two failure scenarios where redriving without investigation would cause repeated failures or data corruption.

### Challenge 2: SNS Message Filtering with Attribute-Based Routing
Configure SNS subscription filter policies to route messages to different SQS queues based on message attributes, simulating environment-specific or priority-based routing.
1. Create an SNS topic `challenge-events` and two SQS queues: `high-priority-queue` and `standard-queue`. Subscribe both queues to the SNS topic.
2. Apply a subscription filter policy to `high-priority-queue` that matches only messages where the `priority` attribute equals `HIGH`: `aws sns set-subscription-attributes --subscription-arn <arn> --attribute-name FilterPolicy --attribute-value '{"priority": ["HIGH"]}'`. Leave `standard-queue` with no filter policy (receives all messages).
3. Publish two test messages — one with `--message-attributes '{"priority":{"DataType":"String","StringValue":"HIGH"}}'` and one with `"StringValue":"NORMAL"`. Verify that `high-priority-queue` received only the HIGH message and `standard-queue` received both.
4. Research and document the difference between SNS subscription filter policies and EventBridge event patterns. In what scenario would you choose EventBridge rule filtering over SNS filter policies, even when both could technically route the same event?

### Reflection Questions
1. After completing Challenge 1, explain the relationship between the SQS visibility timeout, the maxReceiveCount redrive policy parameter, and message delivery guarantees. What happens to a message that reaches maxReceiveCount but has no DLQ configured — and what does this tell you about the importance of always configuring a DLQ in production?
2. Based on Challenge 2, how does SNS message filtering shift the routing responsibility from consumers to the messaging layer itself? Connect this to the AWS Well-Architected Framework's Operational Excellence pillar principle of "making frequent, small, reversible changes" — how does attribute-based routing make it easier to add new message consumers without modifying existing ones?

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
