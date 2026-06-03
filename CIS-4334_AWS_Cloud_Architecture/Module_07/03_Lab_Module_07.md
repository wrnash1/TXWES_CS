# Lab: Module 07 — Amazon EC2 and Auto Scaling

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Total Points:** 100

---

## Lab Overview

This lab builds hands-on EC2 and Auto Scaling skills through three exercises: selecting and justifying EC2 instance types for real-world scenarios, configuring an Auto Scaling group with a launch template and Target Tracking policy using the AWS CLI, and designing a lifecycle hook architecture for a production workload.

---

## Prerequisites

- AWS Academy Learner Lab account or an AWS free-tier account
- AWS CLI v2 installed and configured with a named profile
- Completed Module 07 video and reading guide
- A default VPC with at least two subnets in different Availability Zones (present in all new AWS accounts)

---

## Part 1: Instance Type Selection and Justification (30 points)

For each of the following five workload scenarios, select the most cost-appropriate EC2 instance family and justify your choice. For each scenario also specify whether a placement group is required — and if so, which type.

### Scenario A

A startup is deploying a new customer-facing REST API. Traffic is expected to be low during the first three months while the product is in beta. The development team wants to minimize cost. The application has no GPU or special storage requirements.

**Deliverable 1A:** Instance family recommendation, size (small/medium/large), placement group decision, and 3-sentence justification.

### Scenario B

A pharmaceutical company runs molecular dynamics simulations. Each simulation job uses 32 vCPUs intensively for 8–12 hours with minimal memory requirements per vCPU. Jobs are submitted in batches and can be restarted from a saved state file if interrupted.

**Deliverable 1B:** Instance family recommendation, pricing model recommendation, placement group decision, and 4-sentence justification.

### Scenario C

A financial services firm is migrating SAP HANA to AWS. The SAP HANA instance requires 6 TB of RAM to hold the entire database in memory. Downtime is not acceptable during business hours.

**Deliverable 1C:** Instance family recommendation, placement group decision, and 3-sentence justification explaining why this family is the only correct choice.

### Scenario D

A video streaming platform runs a Cassandra NoSQL cluster with 12 nodes. They need rack-level fault isolation so that losing any single physical rack does not affect more than one Cassandra node group. The cluster must span three Availability Zones.

**Deliverable 1D:** Instance family recommendation and placement group type selection with explanation of why the chosen placement group type meets the requirement.

### Scenario E

An e-commerce company runs a steady-state web application tier behind an Application Load Balancer. The tier consistently uses 20 instances around the clock, 365 days a year. The instances are M6i.large. The company wants to maximize savings.

**Deliverable 1E:** Pricing model recommendation (be specific — which type of Savings Plan or Reserved Instance) and estimated discount range compared to On-Demand.

---

## Part 2: Auto Scaling Group Configuration with the AWS CLI (45 points)

In this part you will create a complete Auto Scaling group for a web application using the AWS CLI.

### Task 2.1 — Create a Launch Template

Create a launch template named `cis4334-web-template` using the following specification:

- AMI: Use the latest Amazon Linux 2023 AMI ID for your region (find it in the EC2 console under AMIs, or use the SSM public parameter)
- Instance type: t3.micro (free tier eligible)
- Security group: the default VPC security group
- User data: a bash script that installs and starts the Apache HTTP server (`httpd`)
- No key pair required for this lab

Write the complete AWS CLI command to create this launch template.

```bash
# Retrieve the latest Amazon Linux 2023 AMI ID via SSM
aws ssm get-parameter \
  --name "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64" \
  --query "Parameter.Value" \
  --output text
```

Store the returned AMI ID, then create the launch template:

```bash
aws ec2 create-launch-template \
  --launch-template-name cis4334-web-template \
  --version-description "Module07Lab-v1" \
  --launch-template-data '{
    "ImageId": "AMI_ID_FROM_ABOVE",
    "InstanceType": "t3.micro",
    "UserData": "IyEvYmluL2Jhc2gKeXVtIGluc3RhbGwgLXkgaHR0cGQKc3lzdGVtY3RsIHN0YXJ0IGh0dHBkCnN5c3RlbWN0bCBlbmFibGUgaHR0cGQ="
  }'
```

The UserData value above is base64-encoded. The plaintext it encodes is:

```bash
#!/bin/bash
yum install -y httpd
systemctl start httpd
systemctl enable httpd
```

**Deliverable 2.1:** The complete create-launch-template command with your actual AMI ID substituted, and a screenshot or copy of the CLI output showing the LaunchTemplateId.

### Task 2.2 — Create the Auto Scaling Group

Create an Auto Scaling group named `cis4334-web-asg` using the launch template from Task 2.1. The group should span two Availability Zones in your region. Use subnets from the default VPC.

First, list your default VPC subnets:

```bash
aws ec2 describe-subnets \
  --filters "Name=defaultForAz,Values=true" \
  --query "Subnets[*].{AZ:AvailabilityZone,SubnetId:SubnetId}" \
  --output table
```

Then create the ASG:

```bash
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name cis4334-web-asg \
  --launch-template "LaunchTemplateName=cis4334-web-template,Version=1" \
  --min-size 1 \
  --max-size 4 \
  --desired-capacity 2 \
  --vpc-zone-identifier "SUBNET_ID_AZ1,SUBNET_ID_AZ2" \
  --health-check-type EC2 \
  --health-check-grace-period 120 \
  --tags "Key=Environment,Value=lab,PropagateAtLaunch=true"
```

**Deliverable 2.2:** The complete create-auto-scaling-group command with your actual subnet IDs substituted. Paste the output of the following describe command to confirm the ASG was created:

```bash
aws autoscaling describe-auto-scaling-groups \
  --auto-scaling-group-names cis4334-web-asg \
  --query "AutoScalingGroups[0].{Name:AutoScalingGroupName,Min:MinSize,Max:MaxSize,Desired:DesiredCapacity,AZs:AvailabilityZones}"
```

### Task 2.3 — Attach a Target Tracking Scaling Policy

Attach a Target Tracking scaling policy that keeps average CPU utilization at 50%.

```bash
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name cis4334-web-asg \
  --policy-name cis4334-cpu-target-tracking \
  --policy-type TargetTrackingScaling \
  --target-tracking-configuration '{
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    },
    "TargetValue": 50.0,
    "DisableScaleIn": false
  }'
```

**Deliverable 2.3:** Paste the output of the above command showing the PolicyARN. Then answer: if the average CPU of the ASG rises to 80% and stays there for 3 minutes, what action will Auto Scaling take?

### Task 2.4 — Verify Instances Are Running

```bash
aws autoscaling describe-auto-scaling-instances \
  --query "AutoScalingInstances[?AutoScalingGroupName=='cis4334-web-asg'].{InstanceId:InstanceId,State:LifecycleState,Health:HealthStatus,AZ:AvailabilityZone}"
```

**Deliverable 2.4:** Paste the output showing your two running instances, confirming they are distributed across two Availability Zones.

### Task 2.5 — Clean Up

Terminate the ASG and launch template to avoid charges:

```bash
aws autoscaling delete-auto-scaling-group \
  --auto-scaling-group-name cis4334-web-asg \
  --force-delete

aws ec2 delete-launch-template \
  --launch-template-name cis4334-web-template
```

**Deliverable 2.5:** Confirm deletion by running describe commands and showing that both resources no longer exist.

---

## Part 3: Lifecycle Hook Architecture Design (25 points)

### Design Scenario

A company runs a stateful application on EC2 instances in an Auto Scaling group. When instances are terminated during scale-in, the application holds open database connections and has an in-memory write-ahead log that must be flushed to S3 before the instance shuts down. Loss of the in-memory log results in data corruption.

Additionally, when new instances launch, they must pull the latest application configuration from AWS Secrets Manager and register themselves with an internal service discovery system before accepting traffic.

### Task 3.1 — Design the Termination Hook

Describe the complete architecture for a termination lifecycle hook that ensures the in-memory log is flushed before instance termination. Your design must include:

- The lifecycle hook configuration (transition type, heartbeat timeout, default result)
- How the hook event is detected and acted upon (EventBridge + Lambda or SSM Run Command)
- What the automation logic does step by step
- How and when CompleteLifecycleAction is called
- What happens if the automation fails or exceeds the timeout

**Deliverable 3.1:** Architecture description covering all five points above. Minimum 200 words.

### Task 3.2 — Design the Launch Hook

Describe the complete architecture for a launch lifecycle hook that pulls configuration from Secrets Manager and registers the instance with service discovery before it enters InService.

**Deliverable 3.2:** Architecture description covering the same five structural points as Task 3.1. Minimum 150 words.

### Task 3.3 — Write the CLI Hook Creation Commands

Write the AWS CLI commands to create both lifecycle hooks on the `cis4334-web-asg` group.

```bash
# Termination hook
aws autoscaling put-lifecycle-hook \
  --auto-scaling-group-name cis4334-web-asg \
  --lifecycle-hook-name FlushLogBeforeTermination \
  --lifecycle-transition autoscaling:EC2_INSTANCE_TERMINATING \
  --heartbeat-timeout 300 \
  --default-result CONTINUE

# Launch hook
aws autoscaling put-lifecycle-hook \
  --auto-scaling-group-name cis4334-web-asg \
  --lifecycle-hook-name ConfigureBeforeLaunch \
  --lifecycle-transition autoscaling:EC2_INSTANCE_LAUNCHING \
  --heartbeat-timeout 180 \
  --default-result ABANDON
```

**Deliverable 3.3:** Explain why the termination hook uses `CONTINUE` as the default result but the launch hook uses `ABANDON`. What does each default result mean if the hook times out?

---

## Submission Instructions

Compile all deliverables into a single PDF or Word document labeled clearly by task number. Include all CLI commands exactly as written and all written responses. Submit through Canvas before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|------|--------|----------|
| Part 1: Instance Selection | 30 | Correct family for each scenario; pricing model justified; placement group decisions accurate |
| Part 2: ASG CLI Tasks 2.1–2.4 | 40 | Commands syntactically correct; deliverable outputs pasted; CPU question answered correctly |
| Part 2: Cleanup Task 2.5 | 5 | Both resources confirmed deleted |
| Part 3: Hook Design Tasks 3.1–3.2 | 15 | Both hook architectures include all five required elements; automation logic is specific and accurate |
| Part 3: CLI Commands Task 3.3 | 10 | Commands correct; CONTINUE vs ABANDON explained accurately |
| **Total** | **100** | |

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
