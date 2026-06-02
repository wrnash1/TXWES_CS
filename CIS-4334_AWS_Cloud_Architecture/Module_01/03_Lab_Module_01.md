# Lab: Module 01 - AWS Global Infrastructure and Core Services Overview

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab develops hands-on familiarity with the AWS Global Infrastructure using the AWS CLI and the AWS Management Console. You will query Regions, Availability Zones, and service availability; analyze the Shared Responsibility Model against a reference architecture; and document an architecture deployment plan that satisfies a given availability requirement.

No resources are provisioned in this lab, so there are no charges. All commands are read-only describe and list operations.

---

## Prerequisites

- AWS account with IAM user or role that has at minimum the `ReadOnlyAccess` managed policy attached
- AWS CLI version 2 installed and configured (`aws configure` completed with Access Key, Secret Key, default Region `us-east-1`, output format `json`)
- Text editor or lab notebook for recording output

Verify your CLI is configured correctly before starting:

```bash
aws sts get-caller-identity
```

Expected output includes your AWS Account ID, IAM user or role ARN, and user ID. If this command returns an error, resolve your CLI configuration before proceeding.

---

## Part 1: Exploring AWS Regions (25 points)

### Task 1.1 — List All Available Regions

Run the following command to retrieve all Regions currently enabled for your account:

```bash
aws ec2 describe-regions \
  --query "Regions[*].{Name:RegionName,Endpoint:Endpoint}" \
  --output table
```

**Deliverable 1.1:** Record the complete output. Count the total number of Regions returned and note at least three Regions from different geographic areas (Americas, Europe, Asia Pacific).

### Task 1.2 — Identify Region Endpoints

Observe the endpoint pattern in your output. Each Region's EC2 endpoint follows the format `ec2.<region-name>.amazonaws.com`. This pattern is consistent across most AWS services and is how the AWS CLI routes API calls to the correct Region.

**Deliverable 1.2:** Write a one-paragraph explanation of why Region endpoints matter when designing a multi-region application. Consider: if your application makes API calls to EC2 in us-east-1 and eu-west-1 simultaneously, how does the CLI or SDK know which endpoint to target?

### Task 1.3 — Examine a Specific Region

Query detailed information about the us-east-1 Region:

```bash
aws ec2 describe-regions \
  --region-names us-east-1 \
  --output json
```

**Deliverable 1.3:** Record the output. Note the `OptInStatus` field. Explain the difference between opt-in Regions and default Regions and why this distinction matters for compliance-sensitive workloads.

---

## Part 2: Exploring Availability Zones (25 points)

### Task 2.1 — List AZs in us-east-1

```bash
aws ec2 describe-availability-zones \
  --region us-east-1 \
  --query "AvailabilityZones[*].{Name:ZoneName,ID:ZoneId,State:State,Type:ZoneType}" \
  --output table
```

**Deliverable 2.1:** Record the output table. How many AZs are available in us-east-1? List their names and AZ IDs.

### Task 2.2 — Compare AZs Across Two Regions

Run the same command against us-west-2:

```bash
aws ec2 describe-availability-zones \
  --region us-west-2 \
  --query "AvailabilityZones[*].{Name:ZoneName,ID:ZoneId,State:State,Type:ZoneType}" \
  --output table
```

**Deliverable 2.2:** Create a comparison table in your lab notebook with these columns: Region, AZ Name, AZ ID, State. Include all AZs from both Regions. Describe one scenario where knowing the AZ ID (rather than the AZ name) is necessary for correct cross-account resource planning.

### Task 2.3 — Identify Local Zones

```bash
aws ec2 describe-availability-zones \
  --region us-west-2 \
  --filters Name=zone-type,Values=local-zone \
  --query "AvailabilityZones[*].{Name:ZoneName,ID:ZoneId,State:State,GroupName:GroupName}" \
  --output table
```

**Deliverable 2.3:** Record the Local Zones available in us-west-2. For each Local Zone, identify the nearest major metropolitan area it serves. Explain the use case that would require a Local Zone rather than deploying directly in the parent Region.

---

## Part 3: Shared Responsibility Model Analysis (30 points)

This part is a conceptual architecture exercise. No CLI commands are required.

### Scenario

Your team is deploying the following architecture in us-east-1 across two Availability Zones:

```text
[Internet Gateway]
        |
[Application Load Balancer] (public subnet, AZ-a and AZ-b)
        |
[EC2 Auto Scaling Group] (private subnet, AZ-a and AZ-b)
  - Amazon Linux 2023 AMI
  - Custom web application (Python/Flask)
  - Nginx reverse proxy
        |
[Amazon RDS for PostgreSQL, Multi-AZ] (isolated subnet, AZ-a primary, AZ-b standby)
        |
[Amazon S3 bucket] (static assets and user-uploaded files)
```

### Task 3.1 — Responsibility Matrix

Create a responsibility matrix with three columns: Component, AWS Responsibility, Customer Responsibility. Complete the matrix for each component in the architecture: Internet Gateway, Application Load Balancer, EC2 instances (each layer), RDS for PostgreSQL, and S3 bucket.

**Deliverable 3.1:** Completed responsibility matrix (minimum 5 rows, one per component).

### Task 3.2 — Identify the Responsibility Boundary Shift

**Deliverable 3.2:** Write a paragraph (100-150 words) explaining how the customer's OS-level responsibility differs between the EC2 instances and the RDS for PostgreSQL instance. What specific actions must the customer take for EC2 that AWS handles for RDS? What responsibilities remain with the customer for RDS regardless of the managed service status?

### Task 3.3 — Compliance Implication

**Deliverable 3.3:** Your organization must achieve PCI DSS compliance for credit card processing in this architecture. Identify three specific customer-owned responsibilities in this architecture that directly affect PCI DSS compliance. For each, state what action the customer must take to satisfy the control.

---

## Part 4: Architecture Deployment Plan (20 points)

### Startup Launch Scenario

A startup is launching a new web application. Their requirements are:

- The application must remain available if any single data center fails
- Data must not leave the United States
- Response time for US users must be under 200 milliseconds for page loads
- The team has no compliance requirement beyond standard data privacy practices

### Task 4.1 — Region and AZ Selection

**Deliverable 4.1:** Select a primary AWS Region for this workload. Justify your selection using the four Region selection criteria from the reading guide (compliance, latency, service availability, cost). Name the specific AZs you would deploy across and explain why you chose at least two.

### Task 4.2 — High Availability vs. Disaster Recovery

**Deliverable 4.2:** The startup's CTO asks: "If we deploy across three AZs in one Region, are we protected against any outage scenario?" Write a 75-100 word response that accurately distinguishes between AZ-level failure protection and Region-level failure protection, and advises whether a multi-region strategy is warranted for this startup given their stated requirements.

---

## Submission Instructions

Compile all deliverables (1.1 through 4.2) into a single document. For CLI output deliverables, paste the actual terminal output verbatim. For written deliverables, use complete sentences and correct technical terminology.

Submit your completed lab document to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: Regions | 25 | Correct CLI output recorded; endpoint explanation accurate; opt-in vs. default correctly distinguished |
| Part 2: Availability Zones | 25 | AZ table complete and accurate; AZ ID vs. name distinction correctly explained; Local Zone use case correctly identified |
| Part 3: Shared Responsibility | 30 | Responsibility matrix complete and accurate; EC2 vs. RDS boundary correctly explained; PCI DSS actions specific and actionable |
| Part 4: Architecture Plan | 20 | Region selection justified using all four criteria; HA vs. DR distinction accurate and clearly stated |
| **Total** | **100** | |
