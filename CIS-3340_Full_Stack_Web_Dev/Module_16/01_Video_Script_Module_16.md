# Video Script: Module 16 — Final Exam Prep & AWS Developer Associate Certification

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen throughout — no screen capture needed for this module
- Use [PAUSE] for slides; [SHOW CODE] only for the brief code review segments
- Slide deck: exam domain breakdown, service mapping table, rapid-fire review cards
- Have DVA-C02 exam guide PDF on screen for domain breakdown section

---

## Section 1: Introduction — The Finish Line (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 16 — the final module of CIS-3340 Full Stack Web Development.

Over the past fifteen weeks you built a real, production-capable full-stack application. You wrote HTML, CSS, and JavaScript from scratch. You built a REST API in Express with authentication, authorization, and proper error handling. You deployed a React frontend to AWS S3 and CloudFront, an Express backend to Elastic Beanstalk, and a PostgreSQL database to RDS. You added real-time features with WebSockets. That is a complete, professional software stack.

This final module has two goals: prepare you to pass the AWS Certified Developer — Associate exam, and help you see how every lab you completed maps directly to something on that exam.

[PAUSE — slide: Module 16 objectives — exam domains and lab-to-exam mapping]

---

## Section 2: The DVA-C02 Exam — What You Need to Know (1:30 – 4:30)

The AWS Certified Developer — Associate exam (DVA-C02) has 65 questions, a 130-minute time limit, and a passing score of approximately 720 out of 1000. Questions are multiple-choice (one correct answer) and multiple-response (two or more correct answers, stated in the question).

[PAUSE — slide: DVA-C02 exam domains and percentages]

The exam is divided into four domains:

**Domain 1 — Development with AWS Services: 32%**

This is the largest domain. It covers Lambda functions (handler signatures, event objects, environment variables, layers), API Gateway (REST APIs, request/response mapping, Lambda integration, usage plans), DynamoDB (data modeling, `GetItem`, `PutItem`, `Query`, `Scan`, expressions), SQS and SNS (message processing, fan-out patterns), S3 (presigned URLs, lifecycle policies, event notifications), and the AWS SDK for JavaScript v3.

**Domain 2 — Security: 26%**

IAM roles, policies, and least-privilege design. AWS Secrets Manager and Systems Manager Parameter Store for secrets. KMS encryption (SSE-S3, SSE-KMS). Cognito User Pools and Identity Pools. API Gateway authorizers — Cognito User Pool authorizers and Lambda authorizers. Never embed credentials in code.

**Domain 3 — Deployment: 24%**

CloudFormation and AWS SAM for infrastructure as code. CodePipeline, CodeBuild, CodeDeploy for CI/CD. Deployment strategies — in-place, blue/green, canary (Lambda weighted aliases, CodeDeploy AppSpec). Elastic Beanstalk configuration, deployment package contents, environment properties. Lambda deployment packages, layers, and versioning.

**Domain 4 — Troubleshooting and Optimization: 18%**

CloudWatch Logs and Metrics — querying logs, creating alarms. X-Ray tracing — service maps, traces, sampling. Lambda performance — cold starts, memory allocation, concurrency. DynamoDB performance — hot partitions, capacity modes, DAX. SQS visibility timeout and dead-letter queues.

[PAUSE — slide: Domain percentages as a bar chart]

---

## Section 3: Lab-to-Exam Mapping (4:30 – 8:00)

Every lab you completed in this course maps directly to a DVA-C02 domain. Let me show you the connection.

[PAUSE — slide: Lab-to-exam mapping table]

Lab 1 through 3 — HTML, CSS, JavaScript fundamentals. This maps to Domain 1. The exam tests JavaScript knowledge needed to write Lambda functions and use the AWS SDK.

Labs 4 and 5 — Node.js and npm. Lambda functions run on Node.js. Understanding `require`, `module.exports`, `async/await`, and `package.json` is prerequisite knowledge for every Lambda question.

Labs 6 and 7 — Express routing, middleware, and error handling. API Gateway Lambda integration passes an `event` object to your handler. The `event.body`, `event.pathParameters`, `event.queryStringParameters`, and `event.headers` structure mirrors what Express receives from `req`.

Lab 8 — PostgreSQL and SQL. RDS is a managed relational database. The exam tests connection string configuration, security group setup, and the RDS Proxy pattern for Lambda-to-RDS connections — all covered in Lab 14.

Labs 12 and 13 — JWT authentication, bcrypt, protected routes. This maps directly to Domain 2. Cognito User Pools issue JWTs. Lambda authorizers verify JWTs using the exact same logic as your `requireAuth` middleware. The `401 Unauthorized` vs `403 Forbidden` distinction is explicitly tested.

Lab 14 — S3, CloudFront, Elastic Beanstalk, RDS. This is Domain 3. Deploying to EB, configuring environment variables instead of committed `.env` files, setting up RDS in a private subnet — all exam content.

Lab 15 — WebSockets. API Gateway WebSocket APIs are in Domain 1. The `$connect`, `$disconnect`, `$default` routes, connectionId storage in DynamoDB, and `PostToConnectionCommand` — all exam-eligible content.

[PAUSE — slide: Lab-to-exam mapping continued]

---

## Section 4: High-Yield Domain 1 Topics (8:00 – 12:00)

Let me walk through the topics that appear most frequently on Domain 1.

[PAUSE — slide: Lambda function handler signature]

Lambda handler signature for Node.js:

[SHOW CODE]

```js
exports.handler = async (event, context) => {
  // event — the trigger payload (API Gateway event, S3 event, SQS message, etc.)
  // context — runtime information (function name, memory limit, request ID)
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: 'OK' }),
  };
};
```

For API Gateway proxy integration, the response must have `statusCode`, `headers`, and `body` (as a string). Forgetting `JSON.stringify(body)` is a common bug — API Gateway requires `body` to be a string, not an object.

[PAUSE — slide: DynamoDB key concepts]

DynamoDB high-yield topics:

- **Partition key** — determines which partition stores the item. High-cardinality values prevent hot partitions.
- **Sort key** — enables range queries within a partition. `Query` requires a partition key; `Scan` reads the entire table.
- **GSI (Global Secondary Index)** — allows querying by non-key attributes. Creates a separate partition.
- **Capacity modes** — On-Demand scales automatically; Provisioned requires capacity planning with auto-scaling.
- **Condition expressions** — `ConditionExpression: 'attribute_not_exists(pk)'` prevents overwriting existing items.

[PAUSE — slide: SQS visibility timeout and DLQ]

SQS patterns:

- **Visibility timeout** — when a consumer receives a message, it becomes invisible for N seconds. If not deleted within the timeout, it reappears. Set the timeout longer than your Lambda function's maximum processing time.
- **Dead-letter queue (DLQ)** — after `maxReceiveCount` failed processing attempts, the message moves to the DLQ. The DLQ is a separate SQS queue used for analysis and alerting.
- **`maxReceiveCount`** — controls how many times a message can be received before going to the DLQ.

---

## Section 5: High-Yield Domain 2 Topics — Security (12:00 – 15:00)

Security questions on the DVA-C02 exam follow predictable patterns. The answers almost always involve IAM roles, Secrets Manager, or Cognito.

[PAUSE — slide: IAM least privilege — never use AdministratorAccess for Lambda]

**Rule 1: Lambda functions use IAM execution roles, never access keys in code.**

If an exam question asks how a Lambda function should access DynamoDB, the answer is an IAM execution role with `dynamodb:PutItem` permission on the specific table ARN — never `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in environment variables.

**Rule 2: Secrets Manager for secrets, Parameter Store for configuration.**

Secrets Manager rotates secrets automatically (database passwords, API keys). Parameter Store stores configuration values with optional encryption using SecureString. Both are accessed from Lambda via the AWS SDK — no credentials in code.

**Rule 3: Cognito User Pool authorizer vs Lambda authorizer.**

Cognito User Pool authorizer: validates JWTs issued by the same Cognito User Pool. Zero code required. Use this when your users authenticate with Cognito.

Lambda authorizer: custom code that validates any JWT (including third-party providers). Returns an IAM policy document. API Gateway caches the policy for up to 3,600 seconds. Use this when you need custom validation logic — exactly like your `requireAuth` middleware.

[PAUSE — slide: Lambda authorizer policy document structure]

[SHOW CODE]

```js
// Lambda authorizer return value
return {
  principalId: decoded.userId,
  policyDocument: {
    Version: '2012-10-17',
    Statement: [{
      Action: 'execute-api:Invoke',
      Effect: 'Allow', // or 'Deny'
      Resource: event.methodArn,
    }],
  },
  context: {
    userId: decoded.userId,
    role: decoded.role,
  },
};
```

The `context` object values are passed to the Lambda integration as `$context.authorizer.userId` — accessible in your route handler Lambda.

---

## Section 6: High-Yield Domain 3 Topics — Deployment (15:00 – 18:00)

[PAUSE — slide: SAM template structure]

AWS SAM (Serverless Application Model) is CloudFormation with a simplified syntax for Lambda, API Gateway, and DynamoDB.

[SHOW CODE]

```yaml
# template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  BooksFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/books.handler
      Runtime: nodejs20.x
      Environment:
        Variables:
          TABLE_NAME: !Ref BooksTable
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref BooksTable
      Events:
        GetBooks:
          Type: Api
          Properties:
            Path: /books
            Method: get

  BooksTable:
    Type: AWS::Serverless::SimpleTable
    Properties:
      PrimaryKey:
        Name: id
        Type: String
```

SAM CLI commands: `sam build` compiles the application, `sam deploy --guided` deploys to CloudFormation.

[PAUSE — slide: Blue/green vs canary deployment strategies]

Deployment strategies:

- **In-place**: replace the current version. If something breaks, rollback requires redeployment. Risk: brief downtime.
- **Blue/green**: deploy new version alongside old version. Switch traffic all at once. Rollback is instant (switch back). EB supports this natively.
- **Canary**: shift a small percentage of traffic (5%, 10%) to the new version, monitor metrics, then shift 100%. Lambda uses weighted aliases. CodeDeploy `Linear10PercentEvery1Minute` is an example canary strategy.

The exam tests which strategy is appropriate for which requirement. Zero-downtime + instant rollback = blue/green. Gradual validation = canary.

---

## Section 7: High-Yield Domain 4 Topics — Troubleshooting (18:00 – 20:30)

[PAUSE — slide: CloudWatch Logs structure — log groups, log streams, log events]

CloudWatch Logs: every Lambda function writes to a log group named `/aws/lambda/FunctionName`. Each execution instance writes to a separate log stream. Use CloudWatch Logs Insights to query across log streams with a SQL-like syntax.

X-Ray: tracing service that shows the full request path across Lambda, API Gateway, DynamoDB, and other AWS services. Enable X-Ray on Lambda with `TracingConfig: Active` in SAM/CloudFormation. The X-Ray service map shows where latency is concentrated.

Lambda cold starts: when a Lambda function has not been invoked recently, AWS must initialize the execution environment. Cold starts add 100ms–1000ms of latency. Mitigation options: provisioned concurrency (keeps instances warm), Lambda SnapStart (for Java), or reducing package size and initialization code.

[PAUSE — slide: Lambda cold start mitigation options]

---

## Section 8: Exam Strategy (20:30 – 22:30)

Fifteen minutes of strategy that can be worth ten questions:

[PAUSE — slide: Exam strategy — five rules]

**Rule 1: Eliminate answers that embed credentials in code.** Any answer that puts access keys in Lambda environment variables or in source code is wrong. Every time.

**Rule 2: "Least privilege" means the minimum permissions for the job.** If an answer grants `*` on `*`, it is wrong. Look for the answer that names a specific service and specific action.

**Rule 3: Managed services beat custom code.** If you can use Cognito User Pool authorizer instead of a custom Lambda authorizer, the exam prefers it. If you can use SQS DLQ instead of custom retry logic, SQS DLQ is correct.

**Rule 4: Read "multiple response" questions carefully.** The question will tell you exactly how many answers to select — "Select TWO." Select exactly that many. Selecting fewer or more gets zero credit.

**Rule 5: Flag and return.** Mark difficult questions and continue. You have 130 minutes for 65 questions — about 2 minutes per question. Do not lose 5 minutes on one question when you could answer three others in that time.

---

## Conclusion (22:30 – 24:00)

This is the end of CIS-3340 Full Stack Web Development.

You started with an empty `index.html` and ended with a deployed, authenticated, real-time full-stack application running on AWS infrastructure. That is not a toy project — that is the foundation of every production web application you will ever build.

The AWS Developer Associate exam tests whether you can reason about these same concepts at the service level rather than the code level. The translation is direct: your `requireAuth` middleware is a Lambda authorizer. Your `.env` variables are Secrets Manager. Your `app.listen(3000)` is an EB environment. Your `socket.io` server is API Gateway WebSocket. You already know this material. The exam is asking you to recognize it by AWS service name.

Good luck on the exam. You have earned it.

[END OF SCRIPT]
