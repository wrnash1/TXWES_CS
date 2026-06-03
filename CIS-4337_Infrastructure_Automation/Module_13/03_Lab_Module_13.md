# Lab: Module 13 — Terraform Security Best Practices

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will apply Terraform security best practices across four exercises: sensitive variable handling, S3 backend encryption, least-privilege IAM policy construction, and Checkov compliance scanning with CIS benchmark mapping.

**Estimated time:** 90–120 minutes

**Prerequisites:**

- Terraform CLI v1.5+ installed locally
- AWS Free Tier account
- Checkov installed (`pip install checkov` or `brew install checkov`)
- Access to an S3 bucket and DynamoDB table for remote state (from Module 12 lab, or create new)

---

## Part 1: Sensitive Variable Handling (25 minutes)

### Step 1.1 — Create the Configuration

Create a new directory `module13-lab/` and add `main.tf`:

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  type    = string
  default = "us-east-2"
}

variable "db_username" {
  description = "RDS master username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "RDS master password"
  type        = string
  sensitive   = true

  validation {
    condition     = length(var.db_password) >= 16
    error_message = "Password must be at least 16 characters."
  }
}

variable "owner_tag" {
  description = "Owner tag for cost allocation"
  type        = string
}

resource "aws_db_instance" "lab" {
  identifier           = "module13-lab-db"
  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  storage_encrypted    = true
  username             = var.db_username
  password             = var.db_password
  db_name              = "labdb"
  skip_final_snapshot  = true
  publicly_accessible  = false
  deletion_protection  = false

  tags = {
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

output "db_endpoint" {
  description = "RDS endpoint"
  value       = aws_db_instance.lab.endpoint
  sensitive   = false
}

output "db_connection_string" {
  description = "Full connection string including credentials"
  value       = "postgresql://${var.db_username}:${var.db_password}@${aws_db_instance.lab.endpoint}/labdb"
  sensitive   = true
}
```

### Step 1.2 — Pass Secrets via Environment Variables

Do not create a `terraform.tfvars` file. Instead, export the sensitive values as environment variables:

```bash
export TF_VAR_db_username="labadmin"
export TF_VAR_db_password="SecureLabPassword2024!"
export TF_VAR_owner_tag="your-name"
```

### Step 1.3 — Observe Sensitive Redaction

Run `terraform init` (with `-backend=false` to skip backend for this test), then:

```bash
terraform plan -backend=false
```

Observe: the plan output shows `(sensitive value)` for `db_username` and `db_password` wherever those values would appear. The output `db_connection_string` is also flagged as sensitive.

Run:

```bash
terraform output db_connection_string
```

Observe the output shows `(sensitive value)`. Now run:

```bash
terraform output -raw db_connection_string
```

Observe that the actual connection string is displayed when explicitly requested with `-raw`. Document this behavior in your lab submission — it demonstrates that `sensitive = true` is a display control, not an access control.

---

## Part 2: Encrypted Remote Backend (25 minutes)

### Step 2.1 — Create KMS Key for State Encryption

```hcl
resource "aws_kms_key" "tfstate" {
  description             = "KMS key for Terraform state encryption"
  deletion_window_in_days = 7
  enable_key_rotation     = true

  tags = {
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
    Purpose   = "terraform-state-encryption"
  }
}

resource "aws_kms_alias" "tfstate" {
  name          = "alias/module13-tfstate"
  target_key_id = aws_kms_key.tfstate.key_id
}
```

Add this to `main.tf`. Apply it with your current local backend to create the KMS key first.

### Step 2.2 — Configure Encrypted S3 Backend

Add `backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket         = "your-tfstate-bucket"
    key            = "module13-lab/terraform.tfstate"
    region         = "us-east-2"
    encrypt        = true
    kms_key_id     = "alias/module13-tfstate"
    dynamodb_table = "terraform-state-lock"
  }
}
```

Run `terraform init` to migrate state to the encrypted backend. Confirm the migration prompt. After migration, verify in the AWS console that the S3 object is encrypted with the KMS key by inspecting the object properties.

### Step 2.3 — Verify Lock Table Behavior

Open a second terminal and attempt to run `terraform plan` while the first terminal is mid-apply. Observe the lock error message — it should reference the DynamoDB table and include a lock ID. This confirms state locking is working.

---

## Part 3: Least-Privilege IAM Policy (20 minutes)

### Step 3.1 — Analyze Resource Requirements

Review your `main.tf`. List every resource type and the IAM actions required:

| Resource | Required IAM Actions |
|----------|---------------------|
| `aws_db_instance` | `rds:CreateDBInstance`, `rds:DescribeDBInstances`, `rds:ModifyDBInstance`, `rds:DeleteDBInstance`, `rds:AddTagsToResource` |
| `aws_kms_key` | `kms:CreateKey`, `kms:DescribeKey`, `kms:EnableKeyRotation`, `kms:TagResource`, `kms:ScheduleKeyDeletion` |
| `aws_kms_alias` | `kms:CreateAlias`, `kms:DeleteAlias` |

### Step 3.2 — Write the Least-Privilege Policy

Create `iam_policy.tf`:

```hcl
data "aws_iam_policy_document" "terraform_executor" {
  statement {
    sid    = "RDSManagement"
    effect = "Allow"

    actions = [
      "rds:CreateDBInstance",
      "rds:DescribeDBInstances",
      "rds:DescribeDBSubnetGroups",
      "rds:ModifyDBInstance",
      "rds:DeleteDBInstance",
      "rds:AddTagsToResource",
      "rds:ListTagsForResource",
    ]

    resources = ["*"]
  }

  statement {
    sid    = "KMSKeyManagement"
    effect = "Allow"

    actions = [
      "kms:CreateKey",
      "kms:DescribeKey",
      "kms:EnableKeyRotation",
      "kms:GetKeyPolicy",
      "kms:GetKeyRotationStatus",
      "kms:ListAliases",
      "kms:ListKeys",
      "kms:TagResource",
      "kms:ScheduleKeyDeletion",
      "kms:CreateAlias",
      "kms:DeleteAlias",
    ]

    resources = ["*"]
  }

  statement {
    sid    = "StateBackendAccess"
    effect = "Allow"

    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject",
      "s3:ListBucket",
    ]

    resources = [
      "arn:aws:s3:::your-tfstate-bucket",
      "arn:aws:s3:::your-tfstate-bucket/*",
    ]
  }

  statement {
    sid    = "StateLocking"
    effect = "Allow"

    actions = [
      "dynamodb:GetItem",
      "dynamodb:PutItem",
      "dynamodb:DeleteItem",
    ]

    resources = ["arn:aws:dynamodb:us-east-2:*:table/terraform-state-lock"]
  }
}

resource "aws_iam_policy" "terraform_executor" {
  name        = "TerraformExecutorModule13"
  description = "Least-privilege policy for Module 13 Terraform execution"
  policy      = data.aws_iam_policy_document.terraform_executor.json
}
```

Review the generated policy JSON with `terraform plan`. Verify it contains only the actions listed and no wildcards on sensitive services.

---

## Part 4: Checkov CIS Compliance Scan (20 minutes)

### Step 4.1 — Introduce a CIS Finding

Temporarily modify the `aws_db_instance` resource to set `publicly_accessible = true` and `storage_encrypted = false`. Save the file.

### Step 4.2 — Run Checkov

```bash
checkov -d . --framework terraform --output cli
```

Observe the findings. Note:

- The check ID (e.g., `CKV_AWS_17` for publicly accessible RDS)
- The CIS control it maps to
- The file name and line number
- The remediation suggestion

### Step 4.3 — Map to CIS Controls

Run Checkov with the compliance framework flag:

```bash
checkov -d . --framework terraform --compliance cis_aws_v3
```

Review the compliance report. Identify which CIS Level 1 and Level 2 controls are violated.

### Step 4.4 — Restore and Verify

Revert `publicly_accessible = true` to `false` and `storage_encrypted = false` to `true`. Run Checkov again to confirm zero findings remain for these controls.

---

## Lab Submission Requirements

Include in your submission document:

1. Screenshot of `terraform plan` output showing `(sensitive value)` for the database credentials
2. Screenshot of the S3 object properties in the AWS console showing SSE-KMS encryption with your key alias
3. The completed IAM policy JSON (copy from `terraform plan` output for the `aws_iam_policy` resource)
4. The Checkov output from Step 4.2 listing at least two findings, with the check IDs and CIS control numbers
5. Answer: What is the difference between `sensitive = true` on a variable and state file encryption? Why are both needed? (2–3 sentences)

---

## Cleanup

Destroy all resources after completing the lab:

```bash
terraform destroy -auto-approve
```

Also delete the KMS key alias and schedule the KMS key for deletion (minimum 7-day waiting period in AWS).

---

End of Module 13 Lab
