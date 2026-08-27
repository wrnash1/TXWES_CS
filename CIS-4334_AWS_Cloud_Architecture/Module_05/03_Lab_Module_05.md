# Lab: Module 05 - VPC: Subnets, Route Tables, Security Groups, NACLs

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab develops hands-on VPC architecture skills through the primary task specified for this module: designing complete VPC CIDR blocks for a three-tier architecture (public, private, database subnets) and configuring the associated security controls. You will produce a deployment-ready network specification and a working security group configuration.

---

## Prerequisites

- AWS account with VPC read permissions and the ability to create VPCs (or use the read-only describe commands to explore an existing VPC)
- AWS CLI v2 installed and configured
- Completed Module 05 video and reading guide

---

## Part 1: VPC CIDR Design for Three-Tier Architecture (40 points)

### Design Requirements

A financial services startup is launching a new payment processing platform on AWS. The architecture must support the following requirements:

- Three application tiers: public web tier, private application tier, isolated database tier
- Deployment across three Availability Zones in us-east-1 (us-east-1a, us-east-1b, us-east-1c)
- The VPC must accommodate at least 500 EC2 instances total across all tiers without exhausting the IP space
- The VPC CIDR must not overlap with the company's on-premises network: 192.168.0.0/16
- The design must leave at least 30% of the VPC CIDR space unallocated for future expansion
- Database subnet must have no route to the internet under any circumstances

### Task 1.1 — VPC CIDR Selection

Select an appropriate VPC CIDR block. Justify your selection by addressing:

- Why you chose this specific private RFC 1918 range
- How it avoids overlap with the on-premises network
- Total IP addresses in the VPC and calculation of how many are available for resources after AWS reservations

**Deliverable 1.1:** VPC CIDR block selected with written justification.

### Task 1.2 — Subnet CIDR Allocation

Design the complete subnet layout for all three tiers across all three AZs. For each subnet, specify:

- Subnet name and purpose
- CIDR block
- Availability Zone
- Subnet type (public, private, or isolated)
- Approximate usable IP addresses

Present your design as a table with nine subnet rows (three tiers × three AZs).

**Deliverable 1.2:** Complete nine-row subnet allocation table. Verify that all nine subnet CIDRs fit within the VPC CIDR without overlap. Show that at least 30% of the VPC CIDR space remains unallocated after the nine subnets.

### Task 1.3 — Route Table Design

Design the route tables for each subnet tier. For each route table, specify:

- Route table name
- Which subnets it is associated with
- All routes (destination CIDR and target)
- Justification for why the database tier route table has no internet route

**Deliverable 1.3:** Three route table specifications (one per tier). Include the specific route table entries with destinations and targets.

### Task 1.4 — CIDR Conflict Analysis

A senior engineer proposes adding a VPC peering connection to a partner company's VPC. The partner's VPC uses the CIDR block `10.0.0.0/8`. Evaluate whether this peering is feasible given your VPC design. If there is a conflict, explain specifically why it prevents peering and what the company would need to do to resolve it.

**Deliverable 1.4:** Conflict analysis with specific explanation and recommended resolution.

---

## Part 2: Security Group Configuration (35 points)

### Application Architecture

The payment processing platform uses this three-tier architecture:

- Public tier: Application Load Balancer accepting HTTPS (port 443) from the internet
- Application tier: EC2 instances running the payment API on port 8443 (HTTPS)
- Database tier: Amazon RDS for PostgreSQL on port 5432

The platform also requires:

- EC2 instances in the application tier need outbound access to port 443 (HTTPS) to call an external payment gateway API
- Database instances must not be accessible from the internet or the public subnet under any circumstances
- An operations team needs SSH access (port 22) to application tier EC2 instances from a specific office IP range: 198.51.100.0/27

### Task 2.1 — Security Group Specification

Design four security groups: SG-ALB, SG-AppServer, SG-Database, and SG-OpsBastion. For each security group, create a table with columns: Direction, Protocol, Port, Source/Destination, Description.

**Deliverable 2.1:** Four security group specifications in table format. Each table must include all required inbound and outbound rules. Use security group references (SG-ALB, SG-AppServer, etc.) rather than IP CIDR ranges where possible for east-west rules.

### Task 2.2 — Security Group Reference Justification

**Deliverable 2.2:** Write a paragraph (75-100 words) explaining why you used security group references (referencing another security group as the source) for east-west tier-to-tier rules rather than using IP CIDR ranges. What specific security benefit does this provide? What would happen if you used CIDR ranges from the subnet blocks instead?

### Task 2.3 — CLI Implementation

Using the AWS CLI, create the SG-Database security group in an existing VPC (use a test VPC in your account or the default VPC). Then add the inbound rule allowing PostgreSQL access only from SG-AppServer. Substitute real security group IDs for the placeholders.

```bash
aws ec2 create-security-group \
  --group-name SG-Database \
  --description "Database tier - RDS PostgreSQL" \
  --vpc-id vpc-xxxxxxxxxxxxxxxxx

aws ec2 authorize-security-group-ingress \
  --group-id sg-database-id \
  --protocol tcp \
  --port 5432 \
  --source-group sg-appserver-id
```

**Deliverable 2.3:** CLI output of both commands and a screenshot or text output showing the resulting security group rule.

---

## Part 3: Network ACL Design (25 points)

### Task 3.1 — NACL for the Public Subnet

Design a Network ACL for the public subnets (web tier) that:

- Allows inbound HTTPS (port 443) from anywhere
- Allows inbound HTTP (port 80) from anywhere for redirect purposes
- Allows inbound ephemeral ports (1024-65535) for return traffic from internet connections
- Explicitly blocks all inbound traffic from a known malicious IP range: 203.0.113.0/24
- Allows outbound HTTPS (port 443) to anywhere
- Allows outbound HTTP (port 80) to anywhere
- Allows outbound ephemeral ports (1024-65535) for response traffic

Present the NACL as a numbered table with columns: Rule Number, Direction, Type, Protocol, Port Range, Source/Destination, Action.

**Deliverable 3.1:** Complete NACL table for the public subnet with all rules in numeric order. The block rule for 203.0.113.0/24 must have a lower rule number than any allow rule that would otherwise permit traffic from that range.

### Task 3.2 — Stateless Behavior Explanation

A junior engineer argues that since the security group on the ALB already allows HTTPS traffic, the NACL rules are redundant. Write a response (75-100 words) explaining why both controls serve a distinct purpose and why the NACL outbound ephemeral port rule is specifically required even though the security group does not need an explicit outbound rule for the same scenario.

**Deliverable 3.2:** Written explanation of the complementary roles of Security Groups and NACLs, specifically addressing the stateless behavior difference.

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Include all tables, CLI output, and written responses. Submit to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: VPC CIDR Design | 40 | VPC CIDR avoids on-premises overlap; nine subnets fit within VPC without overlap; 30% unallocated; route tables correct for each tier; peering conflict analysis accurate |
| Part 2: Security Groups | 35 | All four SGs specify correct inbound and outbound rules; security group references used for east-west rules; CLI commands produce working SG rule; reference justification accurate |
| Part 3: Network ACLs | 25 | NACL rules numbered correctly; block rule has lower number than allow rules; ephemeral ports included for both inbound and outbound; stateless explanation correctly distinguishes SG and NACL behavior |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: VPC Flow Logs Analysis
Enable VPC Flow Logs on a subnet and analyze the captured traffic records to identify network behavior.
1. In the AWS Console, enable VPC Flow Logs on one of your VPC subnets, with destination set to CloudWatch Logs. Create a new log group named `/vpc/flowlogs/lab05`. Grant the VPC Flow Logs service the required IAM role permissions.
2. Generate traffic by running `aws s3 ls` from an EC2 instance in the logged subnet, and attempt an SSH connection from a disallowed source IP to test REJECT records.
3. After 5 minutes, open the CloudWatch log group and search for log records with `REJECT` in the Action field. Record the rejected traffic source, destination, and port.
4. Find a `ACCEPT` record for DNS traffic (UDP port 53) to the VPC DNS resolver (VPC CIDR + 2 address). Document the source and destination IP addresses.

### Challenge 2: VPC Gateway Endpoint for S3
Create a VPC Gateway Endpoint for S3 and verify that S3 traffic from a private subnet no longer routes through the NAT Gateway.
1. Create a VPC Gateway Endpoint for S3: navigate to VPC → Endpoints → Create Endpoint, select `com.amazonaws.<region>.s3`, choose your VPC, and select the private subnet route tables.
2. Verify the endpoint was added to the route table: `aws ec2 describe-route-tables --filters Name=association.subnet-id,Values=<private-subnet-id> --query "RouteTables[*].Routes"`. Confirm a route entry with Destination `pl-xxxxxxxx` (S3 managed prefix list) pointing to the endpoint.
3. From an EC2 instance in the private subnet, run `aws s3 ls --region <your-region>` and verify it succeeds without internet routing.
4. Check NAT Gateway CloudWatch metrics (`BytesOutToDestination`) before and after the endpoint creation to confirm S3 traffic is no longer flowing through the NAT Gateway.

### Reflection Questions
1. After completing Challenge 1, explain what information VPC Flow Logs do NOT capture that would be needed for a complete security audit. What additional AWS service would you enable to capture DNS query content, and what service captures application-layer HTTP request details?
2. How does the VPC Gateway Endpoint you created in Challenge 2 align with the AWS Well-Architected Framework Cost Optimization pillar? Calculate the approximate monthly NAT Gateway data processing cost savings if the endpoint redirects 1 TB of S3 traffic per month (NAT Gateway data processing rate: $0.045/GB).
