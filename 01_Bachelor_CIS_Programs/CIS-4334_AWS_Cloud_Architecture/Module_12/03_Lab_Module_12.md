# Lab: Module 12 — Serverless Order Processing Pipeline

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Lab Overview

In this lab you build a complete serverless order processing pipeline on AWS. An API Gateway HTTP API endpoint accepts order submissions. A Lambda function validates and persists orders to DynamoDB. DynamoDB Streams triggers a fulfillment Lambda. A Step Functions state machine orchestrates the multi-step fulfillment workflow. An SNS topic fans out a completion event to an SQS queue and an email subscriber.

**Estimated Time:** 90 minutes

**AWS Services Used:** Lambda, API Gateway (HTTP API), DynamoDB, DynamoDB Streams, Step Functions, SNS, SQS, IAM, CloudWatch

**Cost Estimate:** Under $1.00 for lab completion. All services used fall within or near Free Tier limits.

---

## Prerequisites

- AWS account with console access
- Modules 1–11 completed
- Basic Python familiarity for reading the function code

---

## Architecture

```text
Client (curl / Postman)
        |
        v
API Gateway HTTP API  POST /orders
        |
        v
Lambda: order-intake-fn
  Validates payload, writes to DynamoDB
        |
        v
DynamoDB: Orders table  (Streams: NEW_IMAGE)
        |
        v
Lambda: order-stream-fn
  Reads stream record, starts Step Functions
        |
        v
Step Functions: OrderFulfillmentStateMachine
  CheckInventory -> ProcessPayment -> ScheduleShipping
        |
        v
SNS: order-completion-topic
  --> SQS: order-archive-queue
  --> Email subscriber
```

---

## Part 1: Create the DynamoDB Table

### Step 1.1

Open the DynamoDB console and choose **Create table**.

- Table name: `Orders`
- Partition key: `orderId` (String)
- Billing mode: On-Demand (default)

Choose **Create table**.

### Step 1.2 — Enable Streams

1. Open the `Orders` table.
2. Choose the **Exports and streams** tab.
3. Under **DynamoDB stream details**, choose **Enable**.
4. View type: **New image**.
5. Choose **Enable stream**.
6. Copy the **Stream ARN** for later use.

---

## Part 2: Create IAM Roles

### Step 2.1 — Lambda Execution Role

1. Open IAM → **Roles → Create role**.
2. Trusted entity: **AWS service → Lambda**.
3. Attach:

   - `AWSLambdaBasicExecutionRole`
   - `AmazonDynamoDBFullAccess`
   - `AmazonSNSFullAccess`
   - `AWSStepFunctionsFullAccess`

4. Role name: `lab12-lambda-role`

### Step 2.2 — Step Functions Execution Role

1. Create another role.
2. Trusted entity: **AWS service → Step Functions**.
3. Attach `AWSLambdaRole` and `AmazonSNSFullAccess`.
4. Role name: `lab12-sfn-role`

---

## Part 3: Lambda Functions

### Step 3.1 — order-intake-fn

Create a Lambda function:

- Name: `order-intake-fn`
- Runtime: Python 3.12
- Existing role: `lab12-lambda-role`

Replace the default code:

```python
import json
import boto3
import uuid
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    for field in ['customerId', 'items', 'totalAmount']:
        if field not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'Missing field: {field}'})
            }
    order_id = str(uuid.uuid4())
    table.put_item(Item={
        'orderId': order_id,
        'customerId': body['customerId'],
        'items': body['items'],
        'totalAmount': str(body['totalAmount']),
        'status': 'RECEIVED',
        'createdAt': int(time.time())
    })
    return {
        'statusCode': 201,
        'body': json.dumps({'orderId': order_id, 'status': 'RECEIVED'})
    }
```

Choose **Deploy**.

### Step 3.2 — Stub Functions for Step Functions

Create three more Lambda functions (same runtime and role). Use these code bodies:

**check-inventory-fn:**

```python
def lambda_handler(event, context):
    print(f"Inventory check: {event.get('orderId')}")
    return {**event, 'inventoryStatus': 'AVAILABLE'}
```

**process-payment-fn:**

```python
def lambda_handler(event, context):
    print(f"Payment processing: {event.get('orderId')}")
    return {**event, 'paymentStatus': 'APPROVED'}
```

**schedule-shipping-fn:**

```python
def lambda_handler(event, context):
    print(f"Shipping scheduled: {event.get('orderId')}")
    return {**event, 'trackingNumber': 'TRACK-12345'}
```

Deploy each function.

---

## Part 4: SNS and SQS Setup

### Step 4.1 — SNS Topic

1. Open SNS → **Create topic → Standard**.
2. Name: `order-completion-topic`
3. Create and copy the **Topic ARN**.

### Step 4.2 — SQS Queue

1. Open SQS → **Create queue → Standard**.
2. Name: `order-archive-queue`
3. Create and copy the **Queue ARN**.

### Step 4.3 — SNS → SQS Subscription

1. In SQS, open `order-archive-queue`.
2. Choose **SNS subscriptions → Subscribe to Amazon SNS topic**.
3. Select `order-completion-topic` and confirm.

### Step 4.4 — Email Subscription

1. In SNS, open `order-completion-topic`.
2. Create subscription: Protocol = Email, your address.
3. Confirm via the confirmation email.

---

## Part 5: Step Functions State Machine

1. Open Step Functions → **Create state machine → Write your workflow in code**.
2. Type: **Standard**.
3. Paste the following ASL (replace `REGION` and `ACCOUNT_ID` with your values):

```json
{
  "Comment": "Order fulfillment workflow",
  "StartAt": "CheckInventory",
  "States": {
    "CheckInventory": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "check-inventory-fn",
        "Payload.$": "$"
      },
      "ResultPath": "$.checkResult",
      "Next": "ProcessPayment",
      "Catch": [{"ErrorEquals": ["States.ALL"], "Next": "OrderFailed"}]
    },
    "ProcessPayment": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "process-payment-fn",
        "Payload.$": "$"
      },
      "ResultPath": "$.paymentResult",
      "Next": "ScheduleShipping",
      "Catch": [{"ErrorEquals": ["States.ALL"], "Next": "OrderFailed"}]
    },
    "ScheduleShipping": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
        "FunctionName": "schedule-shipping-fn",
        "Payload.$": "$"
      },
      "ResultPath": "$.shippingResult",
      "Next": "OrderComplete"
    },
    "OrderComplete": {"Type": "Succeed"},
    "OrderFailed": {
      "Type": "Fail",
      "Error": "FulfillmentFailed",
      "Cause": "A fulfillment step failed"
    }
  }
}
```

1. Name: `OrderFulfillmentStateMachine`
2. Permissions: existing role → `lab12-sfn-role`
3. Create. Copy the **State Machine ARN**.

---

## Part 6: Stream Trigger Lambda

### Step 6.1 — order-stream-fn

Create a Lambda function named `order-stream-fn` (Python 3.12, `lab12-lambda-role`).

```python
import json
import boto3
import os

sfn = boto3.client('stepfunctions')
STATE_MACHINE_ARN = os.environ['STATE_MACHINE_ARN']

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] in ('INSERT', 'MODIFY'):
            new_image = record['dynamodb'].get('NewImage', {})
            order_id = new_image.get('orderId', {}).get('S', 'unknown')
            sfn.start_execution(
                stateMachineArn=STATE_MACHINE_ARN,
                name=f'order-{order_id}',
                input=json.dumps({'orderId': order_id})
            )
            print(f"Started execution for {order_id}")
```

Under **Configuration → Environment variables**, add:

- Key: `STATE_MACHINE_ARN` | Value: your state machine ARN

Deploy.

### Step 6.2 — Add DynamoDB Trigger

1. In `order-stream-fn`, choose **+ Add trigger → DynamoDB**.
2. Select the `Orders` table stream.
3. Batch size: `10`
4. Starting position: **Latest**
5. Add.

---

## Part 7: API Gateway

1. Open API Gateway → **Create API → HTTP API → Build**.
2. Add integration: **Lambda → order-intake-fn**.
3. API name: `OrdersAPI`
4. Route: `POST /orders` → `order-intake-fn`
5. Stage: `$default`
6. Create. Copy the **Invoke URL**.

---

## Part 8: Test the Pipeline

### Test 8.1 — Submit an Order

```bash
curl -X POST https://<INVOKE_URL>/orders \
  -H "Content-Type: application/json" \
  -d '{"customerId":"cust-001","items":["widget-A"],"totalAmount":29.99}'
```

Expected: `{"orderId": "...", "status": "RECEIVED"}`

### Test 8.2 — DynamoDB Verification

Open DynamoDB → `Orders` → **Explore table items**. Confirm the record is present with `status: RECEIVED`.

### Test 8.3 — Step Functions Verification

Open Step Functions → `OrderFulfillmentStateMachine` → **Executions**. Confirm the execution completed successfully. Inspect each state's input and output.

### Test 8.4 — SQS Verification

Open SQS → `order-archive-queue` → **Send and receive messages → Poll for messages**. Confirm the SNS notification message is present.

---

## Reflection Questions

Provide written answers in your lab submission document:

1. What happens to an API Gateway HTTP API request if `order-intake-fn` throws an unhandled exception? Which service does NOT buffer or retry the request, and how should you handle this?

2. Describe the impact of the DynamoDB Streams `NEW_IMAGE` setting on `order-stream-fn`. If you needed to detect what fields changed on an update, which stream view type would you use instead?

3. In the Step Functions state machine, `ProcessPayment` has a `Catch` block routing to `OrderFailed`. What real-world compensating transaction logic should run in `OrderFailed` to maintain data consistency?

4. You need to add an email notification whenever an order is placed, in addition to the existing completion notification. Identify exactly where in the current architecture you would add this without modifying `order-intake-fn`.

---

## Cleanup

Delete resources in this order to avoid dependency errors:

1. API Gateway HTTP API: `OrdersAPI`
2. Lambda functions: `order-intake-fn`, `order-stream-fn`, `check-inventory-fn`, `process-payment-fn`, `schedule-shipping-fn`
3. Step Functions state machine: `OrderFulfillmentStateMachine`
4. SNS topic: `order-completion-topic` (deletes subscriptions)
5. SQS queue: `order-archive-queue`
6. DynamoDB table: `Orders`
7. IAM roles: `lab12-lambda-role`, `lab12-sfn-role`

---

## Submission Checklist

- Screenshot of successful `curl` response showing `orderId` and `status: RECEIVED`
- Screenshot of DynamoDB `Orders` item
- Screenshot of completed Step Functions execution with all states green
- Screenshot of SQS message in `order-archive-queue`
- Written answers to all four reflection questions

---

## Part 9 — Challenge Exercise

### Challenge 1: Lambda Concurrency Behavior Under Load
Observe Lambda throttling and Reserved Concurrency limits using concurrent invocations.
1. Deploy a simple Lambda function that sleeps for 5 seconds and returns a timestamp: use the inline code `import time; def handler(e,c): time.sleep(5); return {"statusCode":200,"body":"ok"}`. Set a low Reserved Concurrency of 3: `aws lambda put-function-concurrency --function-name <fn-name> --reserved-concurrent-executions 3`.
2. Invoke the function 10 times nearly simultaneously using a loop: `for i in $(seq 1 10); do aws lambda invoke --function-name <fn-name> --invocation-type Event /dev/null & done; wait`. Check the function's CloudWatch metrics for `Throttles` within 2 minutes: `aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Throttles --dimensions Name=FunctionName,Value=<fn-name> --start-time $(date -u -d '5 minutes ago' +%Y-%m-%dT%H:%M:%SZ) --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) --period 60 --statistics Sum`.
3. Remove the Reserved Concurrency cap: `aws lambda delete-function-concurrency --function-name <fn-name>`. Repeat the 10 concurrent invocations and compare the Throttles metric. Document the difference in behavior.
4. Calculate: if this function averages 5 seconds per invocation and the business requires processing 600 orders per minute with zero throttling, what minimum Reserved Concurrency is needed? Show your calculation.

### Challenge 2: Step Functions Error Handling with Catch and Retry
Add resilient error handling to a Step Functions state machine using Catch and Retry configurations.
1. Create a Lambda function named `flaky-fn` that randomly fails 50% of the time: `import random; def handler(e,c): if random.random() < 0.5: raise Exception("Random failure"); return {"result": "success"}`.
2. Create a Step Functions state machine with a single Task state calling `flaky-fn`. Add a Retry configuration: `"Retry": [{"ErrorEquals": ["States.ALL"], "IntervalSeconds": 2, "MaxAttempts": 3, "BackoffRate": 2}]`. Execute the state machine 5 times and record how many succeed on the first attempt versus requiring retries: `aws stepfunctions start-execution --state-machine-arn <arn> --name test-$(date +%s)`.
3. Add a Catch configuration to the Task state that routes failures after all retries to a fallback Pass state returning `{"result": "fallback triggered"}`. Re-execute and verify that no execution fails — either the Task succeeds or the Catch handles the failure gracefully.
4. Examine the execution history of one run that triggered retries: `aws stepfunctions get-execution-history --execution-arn <arn>`. Identify the event types that appear for each retry attempt and explain what the `TaskScheduled`, `TaskFailed`, and `TaskSucceeded` events represent in the execution timeline.

### Reflection Questions
1. After completing Challenge 1, explain the difference between Reserved Concurrency and Provisioned Concurrency in terms of what problem each solves. A Lambda function serves a latency-sensitive customer-facing API — which type of concurrency configuration would you apply and why? Reference the AWS Well-Architected Framework Performance Efficiency pillar in your answer.
2. Based on Challenge 2, explain how Step Functions Retry with exponential backoff implements the Reliability pillar principle of "design for failure." Compare this approach to implementing retry logic inside the Lambda function itself — what does Step Functions provide that application-level retry code cannot, particularly in the context of idempotency and workflow visibility?
