# Lab: Module 06 - RDS and Aurora: Managed Relational Databases

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Points:** 100

---

## Lab Overview

This lab builds hands-on RDS and Aurora skills through three exercises: exploring RDS instance configuration using the AWS CLI, designing a high-availability database architecture for a given scenario, and analyzing backup and security configurations for production readiness. These skills map directly to SAA-C03 database design scenario questions.

---

## Prerequisites

- AWS account with RDS ReadOnly access (rds:Describe*)
- AWS CLI v2 installed and configured
- Completed Module 06 video and reading guide

---

## Part 1: RDS Architecture Design (40 points)

### Design Scenario

A mid-size e-commerce company is migrating their on-premises MySQL 8.0 database to AWS. Their requirements are:

- The database must remain available if a single AZ fails with automatic failover and no manual intervention
- The reporting team runs heavy SELECT queries that currently slow down the production database
- Maximum acceptable downtime during a failover: 2 minutes
- Data must be recoverable to any point in time within the last 14 days
- The database must not be accessible from the public internet
- All data at rest must be encrypted
- Database passwords must be automatically rotated every 30 days

### Task 1.1 — Engine and Deployment Selection

Select between RDS for MySQL and Aurora MySQL for this workload. Justify your selection by addressing:

- Which specific requirements favor your chosen engine
- Whether the 2-minute failover requirement is achievable with your choice
- The cost implication of your choice relative to the alternative

**Deliverable 1.1:** Engine selected with written justification (150-200 words).

### Task 1.2 — High Availability Architecture Specification

Design the complete database deployment specification. Specify:

- DB instance class recommendation (family and size) with justification
- Multi-AZ or Aurora Replica configuration
- Number of Read Replicas, their purpose, and which endpoint the reporting team should use
- Automated backup configuration (backup window, retention period)
- DB Subnet Group: which subnet tier from a three-tier VPC architecture, and why

**Deliverable 1.2:** Complete database architecture specification with all parameters listed and justified.

### Task 1.3 — Security Configuration Specification

Design the complete security configuration. Specify:

- Which IAM mechanism you would use to manage database credentials for the application
- How you would enforce encryption in transit (SSL requirement)
- Which AWS service handles the 30-day password rotation requirement and how it integrates with RDS
- Network access control: which security group rule is needed on the DB security group

**Deliverable 1.3:** Security configuration specification with specific service names and configuration details for each requirement.

---

## Part 2: CLI Exploration of Existing RDS Configuration (35 points)

### Task 2.1 — Describe RDS Instances

Run the following command to list RDS instances in your account (or the default Region):

```bash
aws rds describe-db-instances \
  --query "DBInstances[*].{ID:DBInstanceIdentifier,Engine:Engine,Version:EngineVersion,Class:DBInstanceClass,MultiAZ:MultiAZ,Encrypted:StorageEncrypted,PubliclyAccessible:PubliclyAccessible,Status:DBInstanceStatus}" \
  --output table
```

**Deliverable 2.1:** If your account has RDS instances, paste the output and identify any security concerns (unencrypted instances, publicly accessible instances, non-Multi-AZ production databases). If your account has no RDS instances, explain what each column in the query output represents and what value you would expect for a well-configured production database.

### Task 2.2 — Describe DB Snapshots

```bash
aws rds describe-db-snapshots \
  --query "DBSnapshots[*].{ID:DBSnapshotIdentifier,Type:SnapshotType,Status:Status,Engine:Engine,Encrypted:Encrypted}" \
  --output table
```

**Deliverable 2.2:** Record the output. Explain the difference between the snapshot types you see (automated vs. manual). If you were to restore from a snapshot from 3 days ago, would you also be able to recover to a specific point in time 3 days ago (to the minute) — why or why not?

### Task 2.3 — Explore Aurora Cluster Configuration

```bash
aws rds describe-db-clusters \
  --query "DBClusters[*].{ID:DBClusterIdentifier,Engine:Engine,Status:Status,MultiAZ:MultiAZ,ReaderEndpoint:ReaderEndpoint,Endpoint:Endpoint}" \
  --output table
```

**Deliverable 2.3:** Record the output. If no Aurora clusters exist, explain the purpose of the cluster endpoint vs. the reader endpoint and give a specific example of when an application should use each. Explain what happens to both endpoints during an Aurora failover event.

---

## Part 3: Backup and Recovery Analysis (25 points)

### Recovery Scenario

A production RDS for PostgreSQL database (Multi-AZ enabled, 14-day automated backup retention, daily snapshots at 2:00 AM UTC) experiences the following incident: at 3:45 PM on a Tuesday, a developer accidentally runs `DELETE FROM orders WHERE 1=1`, deleting all 2.3 million rows from the orders table. The error is discovered at 4:15 PM.

### Task 3.1 — Recovery Strategy

Describe the complete recovery process. Answer the following:

- Can you recover to the state of the database at exactly 3:44 PM (1 minute before the deletion)?
- What specific RDS recovery feature enables this and what are the limitations?
- Would the recovery use an automated backup or a manual snapshot?
- Where does the restored database appear — does it replace the existing database or create a new instance?
- What must the application team do after the restore completes?

**Deliverable 3.1:** Complete recovery strategy with step-by-step description and answers to each question above.

### Task 3.2 — Backup Configuration Improvement

Given the incident above, propose two improvements to the backup and recovery configuration that would reduce the time to discover and recover from similar incidents in the future. For each improvement, identify the specific AWS service or RDS feature involved and explain how it reduces either detection time or recovery time.

**Deliverable 3.2:** Two improvement proposals with specific AWS service or feature names and quantified impact on detection or recovery time.

---

## Submission Instructions

Compile all deliverables into a single document labeled clearly by task number. Include all CLI output verbatim and all written responses. Submit to the Canvas assignment portal before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|---|---|---|
| Part 1: Architecture Design | 40 | Engine selection justified against requirements; HA configuration correct; Read Replica endpoint guidance accurate; security configuration uses correct AWS services |
| Part 2: CLI Exploration | 35 | CLI output recorded or columns correctly explained; snapshot types distinguished accurately; Aurora endpoint behavior correct |
| Part 3: Backup and Recovery | 25 | Point-in-time recovery mechanics correctly described; restore creates new instance (not in-place); improvement proposals reference specific AWS services and realistic impact |
| **Total** | **100** | |
