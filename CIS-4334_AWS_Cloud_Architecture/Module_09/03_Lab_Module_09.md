# Lab: Module 09 — AWS Databases

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Total Points:** 100

---

## Lab Overview

This lab builds hands-on database skills through three exercises: creating and querying a DynamoDB table with indexes using the AWS CLI (the most accessible database service for free-tier labs), analyzing RDS Multi-AZ and Read Replica configurations, and designing a complete database architecture for a multi-tier application scenario.

---

## Prerequisites

- AWS Academy Learner Lab account or AWS free-tier account
- AWS CLI v2 installed and configured
- Completed Module 09 video and reading guide
- Familiarity with JSON syntax for DynamoDB CLI commands

---

## Part 1: DynamoDB Table Design and Operations (50 points)

### Task 1.1 — Create a Table with a Composite Primary Key

You are building a data model for an order management system. The access patterns are:

1. Get all orders for a specific customer (query by CustomerId)
2. Get a specific order for a customer (query by CustomerId + OrderId)
3. Get all orders for a specific product regardless of customer (requires a GSI)

Create a DynamoDB table named `cis4334-orders` with a composite primary key:

```bash
aws dynamodb create-table \
  --table-name cis4334-orders \
  --attribute-definitions \
    AttributeName=CustomerId,AttributeType=S \
    AttributeName=OrderId,AttributeType=S \
    AttributeName=ProductId,AttributeType=S \
  --key-schema \
    AttributeName=CustomerId,KeyType=HASH \
    AttributeName=OrderId,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST \
  --global-secondary-indexes '[
    {
      "IndexName": "ProductId-index",
      "KeySchema": [
        {"AttributeName": "ProductId", "KeyType": "HASH"},
        {"AttributeName": "OrderId", "KeyType": "RANGE"}
      ],
      "Projection": {"ProjectionType": "ALL"}
    }
  ]'
```

Wait for the table to become ACTIVE:

```bash
aws dynamodb wait table-exists --table-name cis4334-orders

aws dynamodb describe-table \
  --table-name cis4334-orders \
  --query "Table.{Status:TableStatus,Keys:KeySchema,GSIs:GlobalSecondaryIndexes[*].IndexName}"
```

**Deliverable 1.1:** Paste the output of the describe-table command. Identify in 2–3 sentences which access pattern is served by the base table and which access pattern requires the GSI.

### Task 1.2 — Write Items

Write the following four orders to the table using `put-item`:

Order 1: CustomerId=C001, OrderId=ORD-001, ProductId=P-LAPTOP, OrderDate=2024-11-01, Total=1299.99, Status=SHIPPED

Order 2: CustomerId=C001, OrderId=ORD-002, ProductId=P-MOUSE, OrderDate=2024-11-15, Total=39.99, Status=DELIVERED

Order 3: CustomerId=C002, OrderId=ORD-003, ProductId=P-LAPTOP, OrderDate=2024-11-20, Total=1299.99, Status=PROCESSING

Order 4: CustomerId=C002, OrderId=ORD-004, ProductId=P-KEYBOARD, OrderDate=2024-12-01, Total=79.99, Status=SHIPPED

Write the `put-item` command for Order 1 and run all four:

```bash
aws dynamodb put-item \
  --table-name cis4334-orders \
  --item '{
    "CustomerId": {"S": "C001"},
    "OrderId": {"S": "ORD-001"},
    "ProductId": {"S": "P-LAPTOP"},
    "OrderDate": {"S": "2024-11-01"},
    "Total": {"N": "1299.99"},
    "Status": {"S": "SHIPPED"}
  }'
```

**Deliverable 1.2:** Write the complete `put-item` commands for Orders 2, 3, and 4 following the same pattern. Include the correct DynamoDB attribute type notation (S for string, N for number) for every attribute.

### Task 1.3 — Query by Partition Key

Query all orders for customer C001 using the primary key:

```bash
aws dynamodb query \
  --table-name cis4334-orders \
  --key-condition-expression "CustomerId = :cid" \
  --expression-attribute-values '{":cid": {"S": "C001"}}'
```

**Deliverable 1.3:** Paste the query output. Then write a second query that retrieves only orders for C001 with Status=SHIPPED. Note: Status is not a key attribute, so you must use a FilterExpression, not a KeyConditionExpression. Write the complete command including `--filter-expression` and the corresponding entry in `--expression-attribute-values`. Explain in 1–2 sentences the difference between a KeyConditionExpression and a FilterExpression in DynamoDB.

### Task 1.4 — Query Using the GSI

Query all orders for product P-LAPTOP using the GSI:

```bash
aws dynamodb query \
  --table-name cis4334-orders \
  --index-name ProductId-index \
  --key-condition-expression "ProductId = :pid" \
  --expression-attribute-values '{":pid": {"S": "P-LAPTOP"}}'
```

**Deliverable 1.4:** Paste the query output showing both laptop orders from different customers (C001 and C002). Then answer: why is this query impossible to perform efficiently on the base table without the GSI? What operation would you be forced to use instead, and what is the performance and cost implication of that operation?

### Task 1.5 — Conditional Write and Error Handling

Attempt to write an item that prevents duplicate orders using a condition expression:

```bash
# This should succeed (ORD-005 does not exist)
aws dynamodb put-item \
  --table-name cis4334-orders \
  --item '{
    "CustomerId": {"S": "C001"},
    "OrderId": {"S": "ORD-005"},
    "ProductId": {"S": "P-MONITOR"},
    "Total": {"N": "299.99"},
    "Status": {"S": "PROCESSING"}
  }' \
  --condition-expression "attribute_not_exists(CustomerId) AND attribute_not_exists(OrderId)"

# This should FAIL (ORD-001 already exists)
aws dynamodb put-item \
  --table-name cis4334-orders \
  --item '{
    "CustomerId": {"S": "C001"},
    "OrderId": {"S": "ORD-001"},
    "ProductId": {"S": "P-LAPTOP"},
    "Total": {"N": "999.99"},
    "Status": {"S": "PROCESSING"}
  }' \
  --condition-expression "attribute_not_exists(CustomerId) AND attribute_not_exists(OrderId)"
```

**Deliverable 1.5:** Paste the output of both commands. The first should succeed (no output). The second should produce a ConditionalCheckFailedException error. Explain in 2–3 sentences what this pattern prevents in a production application and why DynamoDB's conditional writes are important for data integrity.

### Task 1.6 — Clean Up

```bash
aws dynamodb delete-table --table-name cis4334-orders
```

**Deliverable 1.6:** Paste the delete-table output confirming deletion.

---

## Part 2: RDS Architecture Analysis (25 points)

Answer the following questions in writing. No AWS console access is required — this is an analytical exercise based on the module content.

### Task 2.1 — Multi-AZ Failover Scenario

A production RDS MySQL instance is running in us-east-1a with Multi-AZ enabled (standby in us-east-1b). The application uses the RDS endpoint `mydb.abcdefghijkl.us-east-1.rds.amazonaws.com`. At 2:00 AM, the primary instance fails due to a hardware issue.

Answer all four questions:

a) How does the application reconnect to the database after failover? Does it need a new connection string?

b) What is the approximate failover duration, and what happens to in-flight transactions during the failover window?

c) The standby instance was not serving any traffic before the failover. Why was it still valuable?

d) After the failover completes, where is the new standby deployed? Is Multi-AZ still in effect?

**Deliverable 2.1:** 4-part answer, 2–3 sentences per question.

### Task 2.2 — Read Replica Architecture

The same application team now wants to add a reporting feature. Business analysts run complex SQL aggregation queries on the production database, and these queries are causing performance problems for the application. Describe the architecture change needed.

Answer all three questions:

a) What RDS feature should the team implement and how should the application be updated to use it?

b) The team lead asks: "Can't we just use the Multi-AZ standby for the reporting queries to avoid maintaining a separate instance?" Explain why this is or is not possible.

c) One analyst suggests running reports against a cross-region Read Replica in us-west-2. Beyond read scaling, what additional benefit does this provide?

**Deliverable 2.2:** 3-part answer, 3–4 sentences per question.

### Task 2.3 — RDS vs. Aurora Decision

A startup is building a new SaaS application. They need MySQL compatibility, expect traffic to grow from 100 to 100,000 active users over 18 months, and need their database to survive AZ failures automatically. A junior developer says they should use RDS MySQL. The lead architect recommends Aurora MySQL. Make the case for Aurora.

**Deliverable 2.3:** 150–200 word argument for Aurora, covering storage scaling, read replica capacity, failover speed, and performance characteristics compared to RDS MySQL.

---

## Part 3: Database Architecture Design (25 points)

### Design Scenario

You are designing the data layer for a social media analytics platform with these requirements:

- **User profiles**: 10 million users; profile reads at millions per second; profile data accessed by user ID; eventual consistency is acceptable for most reads
- **Post activity feed**: Users see a feed of posts from people they follow; feed queries involve traversing follower relationships
- **Analytics dashboard**: Marketing team runs daily reports aggregating post counts, engagement metrics, and user growth by month over the past 3 years; queries scan billions of rows
- **Session management**: User sessions stored with a 30-minute expiration; must handle 500,000 concurrent sessions; session data must survive an AZ failure

### Task 3.1 — Database Selection

For each of the four requirements above, select the most appropriate AWS database service and explain your choice in 3–5 sentences. Your explanation must reference the specific access pattern, scale requirement, and the AWS feature that makes your chosen service the right fit.

**Deliverable 3.1:** Four database selections with justifications.

### Task 3.2 — Architecture Diagram Description

Describe the complete data architecture as a text diagram showing all four database services, how the application tier connects to each, and any caching or acceleration layers you would add.

```
Application Tier (EC2 / Lambda)
    |
    ├── User Profile Service → [YOUR ANSWER]
    |       └── [Caching layer? Which service?]
    |
    ├── Social Graph Service → [YOUR ANSWER]
    |
    ├── Analytics Service → [YOUR ANSWER]
    |
    └── Session Management Service → [YOUR ANSWER]
                └── [Configuration: engine, HA mode?]
```

**Deliverable 3.2:** Fill in the architecture diagram with your selected services and any configuration details that matter (e.g., Aurora with 3 read replicas, ElastiCache Redis with Multi-AZ).

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Include all CLI commands and outputs, all written responses, and the completed architecture diagram. Submit through Canvas before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|------|--------|----------|
| Part 1: DynamoDB Tasks 1.1–1.4 | 30 | Table created with correct GSI; put-item commands use correct type notation; query vs. filter explained correctly; GSI query returns results from multiple customers |
| Part 1: Conditional Write Task 1.5 | 10 | Both commands run; ConditionalCheckFailedException produced; purpose of conditional writes explained |
| Part 1: Cleanup Task 1.6 | 5 | Deletion confirmed |
| Part 2: RDS Analysis Task 2.1 | 10 | All four failover questions answered correctly (DNS endpoint, failover time, standby value, post-failover Multi-AZ) |
| Part 2: RDS Analysis Task 2.2 | 10 | Read Replica use correctly described; standby limitation explained; cross-region DR benefit identified |
| Part 2: RDS vs. Aurora Task 2.3 | 5 | Aurora argument covers all four specified characteristics |
| Part 3: DB Selection and Architecture | 25 | All four services correctly selected with appropriate justifications; architecture diagram complete |
| **Total** | **100** | |

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
