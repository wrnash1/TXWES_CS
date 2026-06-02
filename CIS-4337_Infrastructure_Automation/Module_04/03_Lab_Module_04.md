# CIS-4337 Infrastructure Automation

## Lab — Module 04: Terraform State — Local and Remote Backends

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Inspect local state file structure after an apply.
- Use all major `terraform state` subcommands.
- Configure an S3 remote backend with DynamoDB locking.
- Migrate local state to a remote backend.
- Simulate a locked state and release the lock.

---

## Prerequisites

- Terraform CLI 1.6.0 or later.
- AWS CLI configured with credentials that have S3 and DynamoDB permissions.
- An AWS Free Tier account.

---

## Part 1: Examine Local State

### Step 1.1 — Create the working directory and configuration

```bash
mkdir ~/tf-lab-04
cd ~/tf-lab-04
```

Create `main.tf`:

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "lab_bucket" {
  bucket = "cis4337-lab04-state-demo-${random_id.suffix.hex}"

  tags = {
    Name      = "lab04-bucket"
    ManagedBy = "terraform"
  }
}

resource "random_id" "suffix" {
  byte_length = 4
}
```

Update `main.tf` to add the random provider:

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}
```

### Step 1.2 — Initialize and apply

```bash
terraform init
terraform apply -auto-approve
```

### Step 1.3 — Inspect the state file

```bash
cat terraform.tfstate
```

Record in `lab_notes.txt`:

1. What is the `serial` value in the state file?
2. How many resources are listed in the `resources` array?
3. What is the `id` of the `aws_s3_bucket.lab_bucket` resource?
4. Are any sensitive values visible in plaintext?

### Step 1.4 — Use terraform state list

```bash
terraform state list
```

Record the output. How does the address format match the resource type and local name in your HCL?

### Step 1.5 — Use terraform state show

```bash
terraform state show aws_s3_bucket.lab_bucket
```

Record three attributes that appear in the output that are not in your HCL configuration (these are computed attributes assigned by AWS).

---

## Part 2: Practice State Subcommands

### Step 2.1 — Move a resource in state

Use `terraform state mv` to rename the bucket resource in state:

```bash
terraform state mv aws_s3_bucket.lab_bucket aws_s3_bucket.main_bucket
```

Run `terraform state list` to confirm the rename. Then update the resource name in `main.tf` to match:

```hcl
resource "aws_s3_bucket" "main_bucket" {
  # ... same content ...
}
```

Run `terraform plan`. Confirm the plan shows no changes (state and config now agree).

### Step 2.2 — Remove a resource from state

Run `terraform state rm aws_s3_bucket.main_bucket`. Then run:

```bash
terraform plan
```

Record: What does the plan propose now that the bucket is no longer tracked in state? (The bucket still exists in AWS, but Terraform no longer knows about it.)

### Step 2.3 — Re-import the resource

First, find the bucket name from the state list output or the AWS console. Then re-import it:

```bash
terraform import aws_s3_bucket.main_bucket <your-bucket-name>
```

Run `terraform plan` to confirm no changes remain.

---

## Part 3: Configure the S3 Remote Backend

### Step 3.1 — Create the S3 state bucket

Using the AWS console or CLI, create an S3 bucket for Terraform state. The bucket name must be globally unique. Enable versioning.

```bash
aws s3api create-bucket \
  --bucket cis4337-tfstate-$(whoami) \
  --region us-east-1

aws s3api put-bucket-versioning \
  --bucket cis4337-tfstate-$(whoami) \
  --versioning-configuration Status=Enabled
```

### Step 3.2 — Create the DynamoDB locking table

```bash
aws dynamodb create-table \
  --table-name terraform-state-lock \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

Record in `lab_notes.txt`:

1. What is the exact attribute name required by the S3 backend for locking?
2. What is the attribute type?
3. Why does Terraform not create this table automatically?

### Step 3.3 — Add the backend configuration

Add a `backend "s3"` block to the `terraform {}` block in `main.tf`:

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }

  backend "s3" {
    bucket         = "cis4337-tfstate-YOUR_USERNAME"
    key            = "lab04/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

Replace `YOUR_USERNAME` with the actual bucket name you created.

### Step 3.4 — Migrate state to the remote backend

```bash
terraform init -migrate-state
```

When prompted "Do you want to copy existing state to the new backend?" type `yes`.

Record in `lab_notes.txt`:

1. Where is the state file now stored?
2. What happened to the local `terraform.tfstate` file?

### Step 3.5 — Verify remote state

```bash
terraform state list
terraform plan
```

Confirm both commands work against the remote backend. Run:

```bash
aws s3 ls s3://cis4337-tfstate-YOUR_USERNAME/lab04/
```

Confirm `terraform.tfstate` appears in the S3 bucket.

---

## Part 4: Destroy and Clean Up

```bash
terraform destroy -auto-approve
```

After destroy, check whether the S3 state bucket and DynamoDB table still exist (they should — Terraform does not manage infrastructure it was not configured to manage).

Clean up the state infrastructure manually:

```bash
aws s3 rb s3://cis4337-tfstate-YOUR_USERNAME --force
aws dynamodb delete-table --table-name terraform-state-lock --region us-east-1
```

---

## Deliverables

Submit to Canvas:

1. Screenshot of local `terraform.tfstate` contents showing at least two resources.
2. Screenshot of `terraform state list` output.
3. Screenshot of `terraform state show aws_s3_bucket.main_bucket` output.
4. Screenshot of `terraform init -migrate-state` showing the migration prompt and confirmation.
5. Screenshot of `aws s3 ls` confirming state file in the S3 bucket.
6. Completed `lab_notes.txt` with all recorded answers.

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| Local state inspected; serial, resource count, and ID recorded | 15 |
| `terraform state mv` executed; plan shows no changes after config update | 15 |
| `terraform state rm` and `terraform import` completed successfully | 20 |
| DynamoDB table created with correct `LockID` attribute | 15 |
| Backend migration completed; state in S3 confirmed | 25 |
| Resources destroyed; cleanup completed | 10 |

---

## Troubleshooting

**Error: NoSuchBucket during backend init**
The S3 bucket must exist before running `terraform init`. Create the bucket first using the AWS CLI or console.

**Error: ResourceNotFoundException during locking**
The DynamoDB table does not exist or the name in the backend config does not match. Verify the table name with `aws dynamodb list-tables`.

**Error: AccessDeniedException**
Your AWS credentials lack permission to access S3 or DynamoDB. Ensure your IAM user has `AmazonS3FullAccess` and `AmazonDynamoDBFullAccess` or equivalent policies.

---

Module 04 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
