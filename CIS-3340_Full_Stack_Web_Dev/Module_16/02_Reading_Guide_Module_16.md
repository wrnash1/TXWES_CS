# Reading Guide: Module 16 — Final Exam Prep & AWS Developer Associate Certification

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3340 &BULL; FULL STACK WEB DEVELOPMENT</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

---

## Overview

This final reading guide synthesizes the AWS services and full-stack patterns from all fifteen modules and prepares you for the AWS Certified Developer — Associate exam (DVA-C02). Use this as a structured review document — each section maps course labs to exam domains.

---

## 1. Exam Structure

| Item | Detail |
|---|---|
| Exam code | DVA-C02 |
| Number of questions | 65 (50 scored, 15 unscored) |
| Time limit | 130 minutes |
| Passing score | ~720 out of 1000 |
| Question types | Multiple-choice (one answer), Multiple-response (two or more, count stated) |
| Exam domains | 4 domains (see below) |

---

## 2. DVA-C02 Exam Domains

### Domain 1 — Development with AWS Services (32%)

The largest domain. Core topics:

- **AWS Lambda** — handler signature (`exports.handler = async (event, context) => {}`), event object structure for API Gateway, S3, SQS triggers, environment variables, layers, versioning, aliases
- **Amazon API Gateway** — REST APIs, Lambda proxy integration, request/response mapping, usage plans, throttling, Cognito User Pool authorizers, Lambda authorizers
- **Amazon DynamoDB** — partition key vs sort key, `GetItem`, `PutItem`, `UpdateItem`, `DeleteItem`, `Query` (requires partition key), `Scan` (full table), GSI, LSI, on-demand vs provisioned capacity, expressions
- **Amazon SQS** — standard vs FIFO queues, visibility timeout, `maxReceiveCount`, DLQ, long polling
- **Amazon SNS** — topics, subscriptions, fan-out pattern (SNS → multiple SQS queues)
- **Amazon S3** — `GetObject`, `PutObject`, presigned URLs, lifecycle policies, S3 Event Notifications
- **AWS SDK v3** — modular imports (`@aws-sdk/client-dynamodb`), `await client.send(new Command(input))`

### Domain 2 — Security (26%)

- **IAM** — least-privilege roles for Lambda, resource-based policies, never embed access keys in code
- **AWS Secrets Manager** — store and rotate database passwords and API keys, Lambda reads at runtime via SDK
- **AWS Systems Manager Parameter Store** — SecureString for sensitive config, String/StringList for non-sensitive config
- **AWS KMS** — SSE-KMS for S3 and DynamoDB, envelope encryption
- **Amazon Cognito** — User Pools (authentication, JWT issuance), Identity Pools (federated AWS credentials)
- **API Gateway authorizers** — Cognito User Pool authorizer (validates Cognito JWTs, zero code), Lambda authorizer (custom validation, returns IAM policy, cacheable)

### Domain 3 — Deployment (24%)

- **AWS SAM** — CloudFormation extension for serverless; `AWS::Serverless::Function`, `AWS::Serverless::Api`, `AWS::Serverless::SimpleTable`; `sam build` + `sam deploy --guided`
- **AWS CodePipeline + CodeBuild + CodeDeploy** — CI/CD pipeline stages: Source → Build → Deploy
- **Deployment strategies** — In-place (highest risk), Blue/Green (instant rollback, parallel environments), Canary (gradual traffic shift, Lambda weighted aliases)
- **AWS Elastic Beanstalk** — platform-managed deployment, `package.json` must have `start` script, secrets in environment properties (not `.env`)
- **Lambda deployment packages** — zip files uploaded directly or via S3; layers for shared dependencies

### Domain 4 — Troubleshooting and Optimization (18%)

- **Amazon CloudWatch** — log groups (`/aws/lambda/FunctionName`), metrics, alarms, Logs Insights
- **AWS X-Ray** — distributed tracing, service maps, `TracingConfig: Active` in SAM
- **Lambda performance** — memory allocation (also determines CPU), cold starts, provisioned concurrency
- **DynamoDB performance** — hot partitions, DAX (in-memory cache), read/write capacity
- **SQS troubleshooting** — visibility timeout mismatch, DLQ for unprocessable messages

---

## 3. Lab-to-Exam Mapping

| Lab | Topic | DVA-C02 Domain |
|---|---|---|
| 1–3 | HTML, CSS, JavaScript | Domain 1 — JS fundamentals for Lambda |
| 4–5 | Node.js, npm, modules | Domain 1 — Lambda runtime, `require`, `async/await` |
| 6–7 | Express routing, middleware, error handling | Domain 1 — API Gateway Lambda integration event structure |
| 8 | PostgreSQL, SQL queries | Domain 1 — RDS with Lambda (connection via RDS Proxy) |
| 9–10 | React components, state, `useEffect` | Domain 1 — DynamoDB SDK patterns mirror React async patterns |
| 11 | Express middleware, error handling | Domain 4 — Structured error logging in CloudWatch |
| 12 | React state management, CORS | Domain 2 — CORS = security boundary at API Gateway |
| 13 | JWT auth, bcrypt, middleware | Domain 2 — Lambda authorizers, Cognito JWT structure |
| 14 | S3, CloudFront, EB, RDS | Domain 3 — Full deployment pipeline |
| 15 | WebSockets, Socket.io, API Gateway WS | Domain 1 — API Gateway WebSocket API |

---

## 4. High-Yield Service Patterns

### Lambda + API Gateway (REST)

The Lambda proxy integration passes the full HTTP request as an `event` object:

```js
exports.handler = async (event) => {
  const { httpMethod, path, pathParameters, queryStringParameters, headers, body } = event;

  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: 'OK' }),  // body MUST be a string
  };
};
```

Common bug: forgetting `JSON.stringify()` on the body. API Gateway requires the body to be a string.

### Lambda Authorizer

```js
exports.handler = async (event) => {
  const token = event.authorizationToken?.replace('Bearer ', '');

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    return {
      principalId: decoded.userId,
      policyDocument: {
        Version: '2012-10-17',
        Statement: [{ Action: 'execute-api:Invoke', Effect: 'Allow', Resource: event.methodArn }],
      },
      context: { userId: decoded.userId, role: decoded.role },
    };
  } catch {
    throw new Error('Unauthorized');
  }
};
```

The `context` values are accessible in the downstream Lambda as `$context.authorizer.userId`.

### DynamoDB — SDK v3 Patterns

```js
const { DynamoDBClient, GetItemCommand, PutItemCommand, QueryCommand } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand, PutCommand } = require('@aws-sdk/lib-dynamodb');

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);  // simplifies marshaling

// Get item
const { Item } = await docClient.send(new GetCommand({
  TableName: 'Orders',
  Key: { orderId: '12345' },
}));

// Put item with condition (prevent overwrite)
await docClient.send(new PutCommand({
  TableName: 'Orders',
  Item: { orderId: '12345', status: 'pending', createdAt: new Date().toISOString() },
  ConditionExpression: 'attribute_not_exists(orderId)',
}));

// Query by partition key
const { Items } = await docClient.send(new QueryCommand({
  TableName: 'Orders',
  KeyConditionExpression: 'customerId = :cid',
  ExpressionAttributeValues: { ':cid': 'user-99' },
}));
```

Use `DynamoDBDocumentClient` to avoid manual marshaling/unmarshaling of DynamoDB type descriptors (`{ S: 'value' }`).

### SQS Processing Lambda

```js
exports.handler = async (event) => {
  const results = await Promise.allSettled(
    event.Records.map(async (record) => {
      const body = JSON.parse(record.body);
      await processOrder(body);
    })
  );

  // Report batch item failures for partial success
  const failures = results
    .map((r, i) => r.status === 'rejected' ? { itemIdentifier: event.Records[i].messageId } : null)
    .filter(Boolean);

  return { batchItemFailures: failures };
};
```

Return `batchItemFailures` to prevent successfully processed messages from being retried while only retrying failed ones (requires SQS Lambda trigger with `ReportBatchItemFailures`).

### AWS SAM Template Essentials

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Runtime: nodejs20.x
    Timeout: 30
    Environment:
      Variables:
        TABLE_NAME: !Ref OrdersTable

Resources:
  OrdersFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/orders.handler
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref OrdersTable
      Events:
        GetOrders:
          Type: Api
          Properties:
            Path: /orders
            Method: get

  OrdersTable:
    Type: AWS::Serverless::SimpleTable
    Properties:
      PrimaryKey:
        Name: orderId
        Type: String
```

`DynamoDBCrudPolicy` is a SAM policy template that grants `GetItem`, `PutItem`, `UpdateItem`, `DeleteItem`, `Query`, `Scan` on the specified table.

---

## 5. Security Patterns — Exam Rules

These rules eliminate wrong answers:

1. **Never embed credentials in code** — Lambda uses IAM execution roles for AWS service access. Access keys in code or environment variables are always wrong.

2. **Secrets Manager for secrets, Parameter Store for config** — Secrets Manager supports automatic rotation (critical for RDS passwords). Parameter Store is cheaper and stores config values. Both accessed via SDK at runtime.

3. **Least privilege** — Grant only the permissions the function needs. `Resource: "*"` with `Action: "*"` is never correct.

4. **Cognito for user auth** — User Pools handle registration, login, MFA, and JWT issuance. Identity Pools vend temporary AWS credentials for direct AWS service access (S3, DynamoDB).

5. **HTTPS everywhere** — S3 bucket policies can enforce HTTPS with `aws:SecureTransport`. API Gateway always uses HTTPS. Never use HTTP for API endpoints.

---

## 6. Deployment Strategies Comparison

| Strategy | Traffic shift | Rollback | AWS services |
|---|---|---|---|
| In-place | All at once, same instances | Redeploy | CodeDeploy, EB |
| Blue/Green | All at once, new environment | Switch traffic back instantly | EB swap URLs, CodeDeploy |
| Canary | Gradual (e.g., 10% then 100%) | Rollback while majority on old version | Lambda aliases, CodeDeploy |
| Linear | Equal steps at set intervals | Same as canary | Lambda aliases, CodeDeploy |

---

## 7. Troubleshooting Patterns

| Symptom | Root cause | Fix |
|---|---|---|
| Lambda timeout | Insufficient memory / slow external call | Increase memory; add X-Ray to find bottleneck |
| Cold start latency | New execution environment initialization | Provisioned concurrency; reduce package size |
| DynamoDB `ProvisionedThroughputExceededException` | Hot partition or insufficient RCU/WCU | Increase capacity; use exponential backoff |
| SQS messages disappear on failure | No DLQ configured | Add DLQ with `maxReceiveCount` |
| Lambda "too many connections" on RDS | Lambda creates new connection per invocation | Add RDS Proxy |
| API Gateway 502 Bad Gateway | Lambda returned malformed response | Ensure `body` is a string and `statusCode` is present |
| CloudFront serves stale content | Cache not invalidated after deploy | Create invalidation on `/*` after S3 upload |
| S3 SPA routing 403/404 on direct URL | No error document configured | Set error document to `index.html`; add CloudFront custom error response |

---

## 8. Exam Tips and Interview Preparation

1. **Know `401` vs `403`** — `401 Unauthorized` means not authenticated (no or invalid credentials). `403 Forbidden` means authenticated but not permitted. API Gateway returns `401` when no authorizer token is present; `403` when the Lambda authorizer returns `Deny`.

2. **`Scan` vs `Query`** — `Query` requires a partition key and is efficient. `Scan` reads every item and is expensive. Exam questions that describe "reads the entire table" are describing a `Scan` — usually the wrong choice.

3. **SQS vs SNS** — SQS is a queue (pull-based, one consumer processes each message). SNS is a pub/sub topic (push-based, all subscribers receive each message). SNS + SQS fan-out means one SNS message goes to multiple SQS queues.

4. **S3 presigned URL** — grants time-limited access to a private object without making the bucket public. Generated server-side with `GetObjectCommand` and the presigner. The `expiresIn` parameter (seconds) controls lifetime.

5. **Lambda layers** — a zip file containing shared libraries or dependencies that is mounted at `/opt/` in the Lambda execution environment. Reduces deployment package size and enables sharing code across functions.

6. **CloudWatch Logs Insights** — use `fields`, `filter`, `stats`, and `sort` to query structured logs across all Lambda invocations. Essential for debugging intermittent errors at scale.

7. **X-Ray service map** — visual diagram of all services in a request path with latency distribution. Identifies the slowest segment without reading individual traces.

8. **`attribute_not_exists(pk)` condition expression** — the most reliable idempotency check for DynamoDB `PutItem`. Ensures the item is not inserted if it already exists.

---

## 9. Study Checklist

Before the exam, confirm you can answer yes to each item:

- [ ] I can write a Lambda handler that returns the correct API Gateway proxy response format
- [ ] I can describe the difference between a Cognito User Pool authorizer and a Lambda authorizer, and when to use each
- [ ] I know which AWS service stores and rotates database passwords (Secrets Manager) vs configuration values (Parameter Store)
- [ ] I can explain what the SQS visibility timeout is and what happens when it expires before the message is deleted
- [ ] I can describe the three DynamoDB operations that require a partition key (GetItem, PutItem, UpdateItem) vs the one that scans without a key (Scan)
- [ ] I can explain the Lambda cold start problem and name two mitigation options
- [ ] I can write a SAM template defining a Lambda function with a DynamoDB table and the correct managed policy
- [ ] I know the difference between blue/green, canary, and in-place deployment strategies
- [ ] I can explain why `Action: "*", Resource: "*"` is always the wrong IAM policy for a Lambda execution role
- [ ] I can describe how CloudFront custom error responses solve the S3 SPA routing problem

---

## 10. Supplemental Resources

The following free, open-access resources go deeper on Module 16 topics and directly support DVA-C02 exam preparation:

**1. AWS Lambda Developer Guide**
[https://docs.aws.amazon.com/lambda/latest/dg/welcome.html](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
The official AWS Lambda reference covering the handler signature, event and context objects, environment variables, layers, versioning, aliases, provisioned concurrency, cold start mitigation, and the execution environment lifecycle — the primary reference for Domain 1 and Domain 4 Lambda topics on the DVA-C02 exam.

**2. Amazon DynamoDB Developer Guide**
[https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
The official DynamoDB reference covering partition keys, sort keys, `GetItem`, `PutItem`, `Query`, `Scan`, GSI, LSI, on-demand vs provisioned capacity, condition expressions, `attribute_not_exists`, DAX, and DynamoDB Streams — covers all DynamoDB patterns in Section 4 of this guide and the high-frequency DynamoDB questions in Domain 1.

**3. AWS Serverless Application Model (SAM) Developer Guide**
[https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
The official SAM reference covering the `Transform` declaration, `AWS::Serverless::Function`, `AWS::Serverless::Api`, `AWS::Serverless::SimpleTable`, SAM policy templates (`DynamoDBCrudPolicy`, `SQSPollerPolicy`), `Globals`, `sam build`, and `sam deploy --guided` — directly supports the SAM template pattern in Section 4 and deployment domain questions.

**4. AWS CodePipeline User Guide**
[https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
The official CodePipeline reference covering pipeline stages (Source, Build, Deploy), integration with CodeBuild for build specs and test reports, CodeDeploy deployment strategies (in-place, blue/green, canary, linear), Lambda weighted aliases for canary deployments, and AppSpec file structure — covers the CI/CD patterns in Domain 3 and the deployment strategy comparison in Section 6.
