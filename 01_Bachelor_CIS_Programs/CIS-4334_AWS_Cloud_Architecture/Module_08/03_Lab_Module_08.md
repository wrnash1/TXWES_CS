# Lab: Module 08 — Amazon S3 and Storage Services

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Total Points:** 100

---

## Lab Overview

This lab builds hands-on S3 and storage skills through three exercises: creating and configuring an S3 bucket with versioning, lifecycle policies, and event notifications using the AWS CLI; practicing storage class selection for realistic scenarios; and designing an EBS storage solution for a database workload.

---

## Prerequisites

- AWS Academy Learner Lab account or AWS free-tier account
- AWS CLI v2 installed and configured
- A text editor for composing JSON configuration files
- Completed Module 08 video and reading guide

---

## Part 1: S3 Bucket Configuration with the AWS CLI (50 points)

### Task 1.1 — Create and Configure the Bucket

Create an S3 bucket for log storage. Bucket names must be globally unique — use your student ID or initials in the name.

```bash
# Create the bucket (replace REGION and YOUR_UNIQUE_NAME)
aws s3api create-bucket \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --region us-east-1

# Block all public access (security best practice)
aws s3api put-public-access-block \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --versioning-configuration Status=Enabled
```

**Deliverable 1.1:** Paste the output of the following verification command:

```bash
aws s3api get-bucket-versioning \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME
```

The output should show `{"Status": "Enabled"}`.

### Task 1.2 — Configure a Lifecycle Policy

Create a lifecycle configuration file named `lifecycle.json` with the following rules:

- Rule 1 (prefix `logs/`): transition to Standard-IA after 30 days, transition to Glacier Deep Archive after 365 days, expire after 2555 days
- Rule 2 (prefix `logs/`): expire noncurrent object versions after 90 days

Create the file `lifecycle.json` with this content:

```json
{
  "Rules": [
    {
      "ID": "log-tiering-and-expiration",
      "Status": "Enabled",
      "Filter": {"Prefix": "logs/"},
      "Transitions": [
        {"Days": 30, "StorageClass": "STANDARD_IA"},
        {"Days": 365, "StorageClass": "DEEP_ARCHIVE"}
      ],
      "Expiration": {"Days": 2555}
    },
    {
      "ID": "expire-noncurrent-versions",
      "Status": "Enabled",
      "Filter": {"Prefix": "logs/"},
      "NoncurrentVersionExpiration": {"NoncurrentDays": 90}
    }
  ]
}
```

Apply the lifecycle configuration:

```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --lifecycle-configuration file://lifecycle.json
```

**Deliverable 1.2:** Paste the output of the following verification command and explain in 2–3 sentences what will happen to an object uploaded to the `logs/` prefix on day 0, day 30, day 365, and day 2555:

```bash
aws s3api get-bucket-lifecycle-configuration \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME
```

### Task 1.3 — Upload Objects and Test Versioning

Upload a test file to the bucket and overwrite it to create multiple versions:

```bash
# Create a test file
echo "Log entry version 1" > testlog.txt

# Upload to the logs/ prefix
aws s3 cp testlog.txt s3://cis4334-logs-YOUR_UNIQUE_NAME/logs/testlog.txt

# Overwrite with version 2
echo "Log entry version 2" > testlog.txt
aws s3 cp testlog.txt s3://cis4334-logs-YOUR_UNIQUE_NAME/logs/testlog.txt

# List all versions of the object
aws s3api list-object-versions \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --prefix logs/testlog.txt
```

**Deliverable 1.3:** Paste the output of `list-object-versions` showing both versions with their version IDs. Then retrieve the first version using its version ID:

```bash
aws s3api get-object \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --key logs/testlog.txt \
  --version-id VERSION_ID_FROM_ABOVE \
  recovered_v1.txt

cat recovered_v1.txt
```

Paste the content of `recovered_v1.txt` to confirm you retrieved "Log entry version 1."

### Task 1.4 — Configure an Event Notification

Create an SQS queue to receive event notifications, then configure S3 to notify the queue when objects are created in the `uploads/` prefix with a `.jpg` suffix.

```bash
# Create SQS queue
aws sqs create-queue \
  --queue-name cis4334-s3-events \
  --query "QueueUrl" \
  --output text

# Get the queue ARN (replace ACCOUNT_ID and REGION)
aws sqs get-queue-attributes \
  --queue-url https://sqs.REGION.amazonaws.com/ACCOUNT_ID/cis4334-s3-events \
  --attribute-names QueueArn
```

Create the file `notification.json`:

```json
{
  "QueueConfigurations": [
    {
      "QueueArn": "arn:aws:sqs:REGION:ACCOUNT_ID:cis4334-s3-events",
      "Events": ["s3:ObjectCreated:*"],
      "Filter": {
        "Key": {
          "FilterRules": [
            {"Name": "prefix", "Value": "uploads/"},
            {"Name": "suffix", "Value": ".jpg"}
          ]
        }
      }
    }
  ]
}
```

Apply the notification configuration:

```bash
aws s3api put-bucket-notification-configuration \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME \
  --notification-configuration file://notification.json
```

**Deliverable 1.4:** Paste the output of the following command to confirm the notification configuration was applied:

```bash
aws s3api get-bucket-notification-configuration \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME
```

Then answer: if a file named `report.pdf` is uploaded to the `uploads/` prefix, will the SQS queue receive a notification? Explain why or why not.

### Task 1.5 — Clean Up

```bash
# Delete all object versions before deleting the bucket
aws s3 rm s3://cis4334-logs-YOUR_UNIQUE_NAME --recursive

aws s3api delete-bucket \
  --bucket cis4334-logs-YOUR_UNIQUE_NAME

aws sqs delete-queue \
  --queue-url https://sqs.REGION.amazonaws.com/ACCOUNT_ID/cis4334-s3-events
```

**Deliverable 1.5:** Confirm deletion with a brief statement that all resources were removed.

---

## Part 2: Storage Class Selection Analysis (25 points)

For each of the five storage scenarios below, select the most cost-appropriate S3 storage class and provide a 3–4 sentence justification. Your justification must reference the access frequency, minimum storage duration, retrieval time requirement, and redundancy requirement.

### Scenario A

A healthcare company generates patient imaging files. Each file is accessed multiple times per day for the first 90 days after creation. After 90 days, access drops to once per month. After 2 years, the files must be retained for 5 more years for regulatory compliance but are almost never accessed.

**Deliverable 2A:** Initial storage class, transition class(es), and estimated transition day(s) with justification.

### Scenario B

A DevOps team stores build artifacts in S3. The same artifact is downloaded dozens of times per day during active sprint cycles but access drops to zero between sprints. The team has no way to predict when the next spike will occur. The artifact must be immediately available when accessed.

**Deliverable 2B:** Storage class selection with justification for handling unpredictable access.

### Scenario C

An analytics company generates daily summary CSV files by processing raw data. The processed CSVs are accessed during the first week after creation but almost never after that. If an old CSV is ever lost, it can be regenerated from the raw data in under an hour. Cost reduction is the primary objective.

**Deliverable 2C:** Storage class selection and explanation of why the redundancy level chosen is appropriate for this specific scenario.

### Scenario D

A media company stores archived news footage. Each clip is accessed once or twice per year for licensing reviews. When accessed, retrieval must complete in under 5 minutes. The footage is irreplaceable.

**Deliverable 2D:** Storage class selection with justification referencing the retrieval time requirement and irreplaceable nature of the data.

### Scenario E

A financial services company must retain trade records for exactly 7 years per SEC regulations. Records are never accessed after the first week. The company needs to prove to auditors that records cannot be deleted or modified during the retention period.

**Deliverable 2E:** Storage class selection AND identify the additional S3 feature required to meet the immutability requirement.

---

## Part 3: EBS Volume Design (25 points)

### Design Scenario

A company is migrating the following workloads from on-premises to EC2 in us-east-1. Design the EBS volumes for each workload and justify every decision.

**Workload A:** A PostgreSQL production database on a single EC2 instance. The database requires 10,000 sustained IOPS and 200 MB/s throughput. The storage size needed is 500 GB. Database availability is critical and the team wants 99.999% EBS volume durability.

**Workload B:** A Hadoop data processing cluster with 6 EC2 worker nodes. Each node needs 2 TB of storage for HDFS block storage. Workloads are sequential reads and writes of large files. Cost efficiency is the top priority; IOPS performance is not critical.

**Workload C:** A development environment EC2 instance running a web application. The developer needs a 50 GB boot volume and a 100 GB data volume for test databases. Performance requirements are minimal.

### Task 3.1 — Volume Type Selection

For each workload, specify:

- EBS volume type
- Volume size
- IOPS setting (if applicable — gp3 and io2 allow independent IOPS specification)
- Whether the volume can be used as a boot volume
- Justification (3–4 sentences)

**Deliverable 3.1:** Volume specification table with justification for Workloads A, B, and C.

### Task 3.2 — AZ Constraint Analysis

A colleague suggests copying one of the Workload B Hadoop volumes to another AZ so it can be shared by multiple nodes. Explain whether this is possible, what the actual constraint is for EBS volumes and AZ placement, and what the correct architectural solution would be for shared storage across multiple EC2 instances in different AZs.

**Deliverable 3.2:** 150–200 word response explaining the AZ constraint and the correct architectural pattern for multi-instance shared storage.

### Task 3.3 — Write the CLI Volume Creation Commands

Write the AWS CLI commands to create the volumes for Workload A. You do not need to run these commands — write them correctly based on your specifications from Task 3.1.

```bash
# Create the Workload A production database volume
aws ec2 create-volume \
  --availability-zone us-east-1a \
  --volume-type TYPE_FROM_TASK_3_1 \
  --size SIZE_FROM_TASK_3_1 \
  --iops IOPS_FROM_TASK_3_1 \
  --encrypted \
  --tag-specifications 'ResourceType=volume,Tags=[{Key=Name,Value=postgres-prod-data},{Key=Environment,Value=production}]'
```

**Deliverable 3.3:** The complete CLI command with your actual volume type, size, and IOPS values from Task 3.1 substituted in. Explain why `--encrypted` is included and whether this incurs additional cost.

---

## Submission Instructions

Compile all deliverables into a single PDF or Word document labeled clearly by task number. Include all CLI commands exactly as written, all pasted command outputs, and all written responses. Submit through Canvas before the module deadline.

---

## Grading Rubric

| Part | Points | Criteria |
|------|--------|----------|
| Part 1: S3 CLI Tasks 1.1–1.3 | 30 | Commands correct; versioning output confirmed; both object versions visible in list-object-versions output; v1 content recovered correctly |
| Part 1: Event Notification Task 1.4 | 15 | Notification config applied; .pdf exclusion correctly explained |
| Part 1: Cleanup Task 1.5 | 5 | Resources confirmed deleted |
| Part 2: Storage Class Selection | 25 | Each scenario correct; justification references access frequency, minimum duration, retrieval time, and redundancy |
| Part 3: EBS Design Tasks 3.1–3.2 | 15 | Correct volume type for each workload; AZ constraint correctly explained; correct multi-instance solution identified |
| Part 3: CLI Command Task 3.3 | 10 | Command syntactically correct with actual values; encryption explanation accurate |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: S3 Replication Configuration
Configure S3 Same-Region Replication (SRR) between two buckets to practice replication setup and observe replication behavior.
1. Create a source bucket and a destination bucket (both in the same Region) with versioning enabled on both: `aws s3api create-bucket --bucket <source-name> --region us-east-1` and `aws s3api put-bucket-versioning --bucket <source-name> --versioning-configuration Status=Enabled`. Repeat for the destination.
2. Create an IAM role for S3 replication with a trust policy for s3.amazonaws.com and a permissions policy granting `s3:GetReplicationConfiguration`, `s3:ListBucket`, `s3:GetObjectVersion`, and `s3:ReplicateObject` on the source, and `s3:ReplicateObject` on the destination.
3. Configure replication on the source bucket: `aws s3api put-bucket-replication --bucket <source-name> --replication-configuration file://replication.json` (write the replication.json with the destination ARN and IAM role ARN).
4. Upload a test object to the source bucket and verify it appears in the destination within 60 seconds: `aws s3 ls s3://<destination-name>/`. Document whether pre-existing objects were replicated and why.

### Challenge 2: EBS Snapshot and AMI Creation
Create an EBS snapshot and build a custom AMI to understand the golden image workflow.
1. Create a gp3 EBS volume (1 GB is sufficient): `aws ec2 create-volume --size 1 --volume-type gp3 --availability-zone us-east-1a --encrypted`. Record the VolumeId.
2. Create a snapshot of the volume: `aws ec2 create-snapshot --volume-id <volume-id> --description "Lab08 challenge snapshot"`. Wait for the snapshot status to become `completed`: `aws ec2 describe-snapshots --snapshot-ids <snapshot-id> --query "Snapshots[*].State"`.
3. Register a new AMI from the snapshot: `aws ec2 register-image --name "lab08-custom-ami" --architecture x86_64 --root-device-name /dev/xvda --block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"SnapshotId":"<snapshot-id>","VolumeSize":1,"VolumeType":"gp3"}}]' --virtualization-type hvm`.
4. Describe the new AMI: `aws ec2 describe-images --image-ids <ami-id>`. Record the AMI ID and the block device mapping showing the snapshot association. Clean up: deregister the AMI and delete the snapshot and volume.

### Reflection Questions
1. After completing Challenge 1, explain why pre-existing objects in the source bucket are NOT automatically replicated when replication is first configured. What specific AWS feature must you use to replicate existing objects, and what does this tell you about how replication works at the S3 service level?
2. Based on Challenge 2, explain how EBS snapshots enable the "golden image" AMI pattern described in the Module 07 reading guide. How does the relationship between snapshots and AMIs support the AWS Well-Architected Framework Reliability pillar design principle of "use automation to make architectural experimentation easier"?

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
