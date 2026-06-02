# Lab: Module 03 - EC2: Instance Types, Auto Scaling, and Load Balancing

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab develops hands-on EC2 architecture skills through three exercises: selecting and justifying instance types for real-world workloads using the AWS CLI, analyzing Auto Scaling Group configuration for a given availability requirement, and designing a complete multi-AZ load-balanced auto-scaled architecture. These skills map directly to SAA-C03 scenario questions.

---

## Prerequisites

- AWS account with ReadOnlyAccess IAM policy and ec2:Describe* permissions
- AWS CLI v2 installed and configured
- Completed Module 03 video and reading guide

---

## Part 1: Instance Type Selection and Justification (30 points)

### Task 1.1 — Query Instance Type Details

Use the AWS CLI to retrieve information about available instance types. Run the following command to list instance types with their vCPU and memory details:

```bash
aws ec2 describe-instance-types \
  --filters Name=current-generation,Values=true \
  --query "InstanceTypes[*].{Type:InstanceType,vCPU:VCpuInfo.DefaultVCpus,MemMiB:MemoryInfo.SizeInMiB,Storage:InstanceStorageSupported}" \
  --output table \
  --region us-east-1
```

**Deliverable 1.1:** Record the first 20 rows of output. Identify at least one instance type from each of the following families in the output: M-family, C-family, R-family, and I-family.

### Task 1.2 — Instance Selection Scenarios

For each of the following five workload scenarios, identify the most appropriate EC2 instance family (not a specific type — the family), explain your reasoning in two to three sentences, and identify one purchasing model that best fits the described usage pattern.

**Scenario A:** A financial services company runs an in-memory trading analytics platform that loads 500 GB of market data into RAM at startup and processes it throughout the trading day. The workload runs from 6 AM to 8 PM EST weekdays only.

**Scenario B:** A media company encodes HD video files into multiple streaming formats. The encoding jobs run in parallel, each consuming 100% of available CPU cores for 10-30 minutes. The jobs arrive sporadically and losing a job mid-processing means simply restarting it.

**Scenario C:** A startup runs a new web application on EC2 that currently handles light traffic (under 10% CPU most of the time) but occasionally spikes to 80% CPU when a marketing email is sent. Budget is a primary concern.

**Scenario D:** A genomics research company runs large-scale distributed data processing using Apache Hadoop. The job reads and writes terabytes of data sequentially from local storage. Network bandwidth to shared storage is a bottleneck.

**Scenario E:** A game company is building a real-time multiplayer game server backend. The servers need consistent sub-2-millisecond response times, handle hundreds of thousands of concurrent UDP connections, and must be reachable via static IP addresses that clients have whitelisted in their firewalls.

**Deliverable 1.2:** For each of the five scenarios: instance family selected, reasoning (2-3 sentences), recommended purchasing model with justification.

### Task 1.3 — T-Series Credit Analysis

Research the AWS documentation for the T3 instance family. Identify the baseline CPU utilization percentage and credit accrual rate for the t3.medium instance.

**Deliverable 1.3:** Answer the following questions: (a) What is the baseline CPU utilization percentage for a t3.medium? (b) What happens to application performance when a t3.medium in Standard mode exhausts its CPU credit balance? (c) Under what specific circumstances would you choose t3.medium Unlimited mode over Standard mode, and what is the cost implication?

---

## Part 2: Auto Scaling Group Configuration Analysis (35 points)

### Architecture Scenario

A three-tier web application runs in us-east-1 with the following Auto Scaling Group configuration:

```text
ASG Name: WebAppASG
Launch Template: WebServer-LT-v3
  AMI: ami-0abcdef1234567890
  Instance Type: t3.medium
  IAM Instance Profile: WebServerRole
  Security Group: sg-webapp-web
  User Data: installs Nginx + app code from S3

Min Capacity: 1
Desired Capacity: 2
Max Capacity: 6
VPC Subnets: subnet-private-1a, subnet-private-1b
Health Check Type: EC2
Health Check Grace Period: 60 seconds
Scaling Policy: Target Tracking, metric=ASGAverageCPUUtilization, target=70%
```

### Task 2.1 — Identify Configuration Problems

Review the ASG configuration above and identify all configuration problems or risks. For each problem, state what the issue is and what the correct configuration should be.

**Deliverable 2.1:** List of identified problems with corrected values. You should find at least four distinct problems.

### Task 2.2 — Scaling Policy Evaluation

The current scaling policy targets 70% average CPU utilization.

**Deliverable 2.2:** Answer the following questions: (a) A traffic spike arrives and drives average CPU to 95%. The ASG is currently at desired=2. Describe what happens step by step — what does the scaling policy do, how quickly does new capacity become available, and what is the impact on users during the scale-out? (b) Would changing the target CPU to 50% improve or worsen the application's response to sudden traffic spikes? Explain why. (c) Given that this is a t3.medium instance fleet, identify one additional risk that the current CPU target tracking policy does not account for.

### Task 2.3 — Rewrite the Configuration

Rewrite the ASG configuration to address all problems you identified in Task 2.1. Present the corrected configuration in the same format as the original (not as a CLI command — as a specification document listing each parameter and its corrected value).

**Deliverable 2.3:** Corrected ASG configuration specification.

---

## Part 3: Multi-AZ Load Balanced Architecture Design (35 points)

### Design Scenario

A mid-size e-commerce company needs to redesign their web application architecture for their upcoming Black Friday sale. Requirements:

- Application must remain available if one Availability Zone fails
- Traffic peaks at 50x normal during the sale window (24 hours, then returns to normal)
- Application consists of a public-facing web tier and a private application API tier
- Session state must not be stored on EC2 instances (stateless design required)
- Database queries are the primary bottleneck during peak periods
- Company wants to minimize costs during the other 350 days of the year

### Task 3.1 — Load Balancer Design

Describe the load balancing architecture. Specify:

- Which load balancer type(s) you would use and at which tiers
- How many load balancer nodes are needed and in which AZs
- How traffic flows from the internet to the web tier and from the web tier to the API tier

**Deliverable 3.1:** Load balancer architecture description with tier-by-tier specification.

### Task 3.2 — Auto Scaling Configuration

For each tier (web and API), specify the Auto Scaling Group configuration including:

- Minimum, desired, and maximum capacity values with justification
- Instance family and purchasing model recommendation for the baseline vs. peak capacity
- Scaling policy type and metric target with justification
- Health check type and why

**Deliverable 3.2:** Two ASG specifications (web tier and API tier) with all parameters justified.

### Task 3.3 — Architecture Diagram Description

Draw or describe a complete architecture diagram showing all components. Include in your description:

- The VPC CIDR and subnet layout (public/private subnets across at least two AZs)
- All EC2 tiers and their subnets
- Load balancer placement
- Where the database tier sits and why
- How session state is handled without storing it on EC2

**Deliverable 3.3:** Architecture diagram or detailed textual description covering all components listed above.

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Submit to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: Instance Selection | 30 | Correct family for each scenario with sound reasoning; purchasing model matches usage pattern; T-series credit analysis accurate |
| Part 2: ASG Configuration | 35 | Minimum four problems identified with correct fixes; scaling policy analysis demonstrates understanding of target tracking behavior and T-series risks; corrected configuration is deployment-ready |
| Part 3: Architecture Design | 35 | Load balancer types correct and justified; ASG parameters appropriate for stated requirements; session state solution specified; architecture diagram is complete and correct |
| **Total** | **100** | |
