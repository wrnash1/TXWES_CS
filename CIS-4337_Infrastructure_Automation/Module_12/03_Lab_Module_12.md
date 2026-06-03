# Lab: Module 12 — Terraform and CI/CD Pipelines

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will build a complete GitHub Actions CI/CD pipeline for a Terraform configuration that provisions an AWS S3 bucket. You will implement validate, security scan, plan, and apply jobs. You will also run tfsec locally and observe drift by making a manual change.

**Estimated time:** 90–120 minutes

**Prerequisites:**

- GitHub account with a repository created for this lab
- AWS Free Tier account
- Terraform CLI v1.5+ installed locally
- tfsec installed locally (`brew install tfsec` or download binary)
- Go 1.21+ installed (for the optional Terratest exercise)

---

## Part 1: Terraform Configuration (30 minutes)

### Step 1.1 — Create the Repository Structure

Create the following directory layout in your GitHub repository:

```text
terraform-cicd-lab/
  .github/
    workflows/
      terraform.yml
  main.tf
  variables.tf
  outputs.tf
  backend.tf
```

### Step 1.2 — Write the Terraform Configuration

Create `main.tf` with a versioned S3 bucket configuration:

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "lab" {
  bucket = "${var.bucket_prefix}-${random_id.bucket_suffix.hex}"

  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = var.owner_tag
  }
}

resource "aws_s3_bucket_versioning" "lab" {
  bucket = aws_s3_bucket.lab.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "lab" {
  bucket = aws_s3_bucket.lab.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "lab" {
  bucket = aws_s3_bucket.lab.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

Create `variables.tf`:

```hcl
variable "aws_region" {
  description = "AWS region for all resources"
  type        = string
  default     = "us-east-2"
}

variable "bucket_prefix" {
  description = "Prefix for the S3 bucket name"
  type        = string
  default     = "txwes-cicd-lab"
}

variable "environment" {
  description = "Environment tag value"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "owner_tag" {
  description = "Owner tag value for cost allocation"
  type        = string
}
```

Create `outputs.tf`:

```hcl
output "bucket_name" {
  description = "Name of the provisioned S3 bucket"
  value       = aws_s3_bucket.lab.id
}

output "bucket_arn" {
  description = "ARN of the provisioned S3 bucket"
  value       = aws_s3_bucket.lab.arn
}

output "bucket_region" {
  description = "Region of the provisioned S3 bucket"
  value       = aws_s3_bucket.lab.region
}
```

Create `backend.tf` using S3 backend (update bucket/key/region for your account):

```hcl
terraform {
  backend "s3" {
    bucket         = "your-tfstate-bucket"
    key            = "cicd-lab/terraform.tfstate"
    region         = "us-east-2"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

### Step 1.3 — Local Validation

Run these commands locally to confirm the configuration is valid:

```bash
terraform fmt
terraform init
terraform validate
```

All three must succeed before proceeding.

---

## Part 2: GitHub Actions Pipeline (40 minutes)

### Step 2.1 — Configure Repository Secrets

In your GitHub repository go to Settings > Secrets and variables > Actions. Add:

- `AWS_ACCESS_KEY_ID` — your AWS access key
- `AWS_SECRET_ACCESS_KEY` — your AWS secret key
- `TF_VAR_OWNER_TAG` — your name or email address

For a production setup you would use OIDC instead of static keys. This lab uses static keys for simplicity; the quiz and discussion will address the OIDC improvement.

### Step 2.2 — Write the Workflow File

Create `.github/workflows/terraform.yml`:

```yaml
name: Terraform CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

permissions:
  contents: read
  pull-requests: write

env:
  TF_VERSION: "1.6.6"
  AWS_DEFAULT_REGION: "us-east-2"

jobs:
  security-scan:
    name: Security Scan
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run tfsec
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          soft_fail: false
          minimum_severity: HIGH

      - name: Run Checkov
        uses: bridgecrewio/checkov-action@v12
        with:
          directory: .
          framework: terraform
          soft_fail: false

  validate:
    name: Validate
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Format Check
        run: terraform fmt -check -recursive

      - name: Terraform Init
        run: terraform init -backend=false

      - name: Terraform Validate
        run: terraform validate

  plan:
    name: Plan
    runs-on: ubuntu-latest
    needs: [security-scan, validate]
    if: github.event_name == 'pull_request'
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      TF_VAR_owner_tag: ${{ secrets.TF_VAR_OWNER_TAG }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        id: plan
        run: terraform plan -out=tfplan -no-color -input=false

      - name: Upload Plan Artifact
        uses: actions/upload-artifact@v4
        with:
          name: tfplan
          path: tfplan
          retention-days: 7

      - name: Post Plan to PR
        uses: actions/github-script@v7
        if: always()
        with:
          script: |
            const output = `#### Terraform Plan 📋
            \`\`\`
            ${{ steps.plan.outputs.stdout }}
            \`\`\`
            `;
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: output
            });

  apply:
    name: Apply
    runs-on: ubuntu-latest
    needs: [security-scan, validate]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      TF_VAR_owner_tag: ${{ secrets.TF_VAR_OWNER_TAG }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}

      - name: Terraform Init
        run: terraform init

      - name: Terraform Apply
        run: terraform apply -auto-approve -input=false
```

### Step 2.3 — Test the Pipeline

1. Create a feature branch: `git checkout -b feature/add-bucket`
2. Commit the Terraform files and push the branch
3. Open a pull request against main
4. Observe the pipeline jobs running in the Actions tab
5. Verify the plan comment appears on the PR
6. Merge the PR and observe the apply job running

Record the apply output in your lab submission document.

---

## Part 3: tfsec Local Scanning (15 minutes)

### Step 3.1 — Introduce a Security Finding

Temporarily modify `aws_s3_bucket_public_access_block.lab` to set `block_public_acls = false`. Save the file.

### Step 3.2 — Run tfsec

```bash
tfsec . --minimum-severity HIGH
```

Observe the finding. Note the check ID, the file and line number, and the remediation suggestion.

### Step 3.3 — Restore the Configuration

Set `block_public_acls = true` again. Run tfsec to confirm no findings remain.

Document in your lab submission: the check ID that fired, the severity level, and what the remediation guidance said.

---

## Part 4: Drift Detection (15 minutes)

### Step 4.1 — Observe Current State

After the apply job has run, go to the AWS console and note the bucket name from the Terraform output.

### Step 4.2 — Introduce Drift

In the AWS console, manually disable versioning on the bucket (set it to Suspended).

### Step 4.3 — Run Plan Locally

```bash
terraform plan -detailed-exitcode
echo "Exit code: $?"
```

Observe that Terraform detects the versioning configuration change and proposes to re-enable it. The exit code should be 2.

### Step 4.4 — Resolve the Drift

Run `terraform apply` to restore the bucket versioning to the Terraform-managed state.

---

## Part 5: Optional Terratest Exercise (20 minutes)

### Step 5.1 — Create the Test File

Create `test/bucket_test.go`:

```go
package test

import (
  "testing"

  "github.com/gruntwork-io/terratest/modules/aws"
  "github.com/gruntwork-io/terratest/modules/random"
  "github.com/gruntwork-io/terratest/modules/terraform"
  "github.com/stretchr/testify/assert"
)

func TestS3BucketProvisioning(t *testing.T) {
  t.Parallel()

  awsRegion := "us-east-2"
  uniqueID := random.UniqueId()

  terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
    TerraformDir: "../",
    Vars: map[string]interface{}{
      "bucket_prefix": "test-bucket-" + uniqueID,
      "owner_tag":     "terratest",
      "environment":   "dev",
    },
  })

  defer terraform.Destroy(t, terraformOptions)

  terraform.InitAndApply(t, terraformOptions)

  bucketName := terraform.Output(t, terraformOptions, "bucket_name")

  assert.NotEmpty(t, bucketName)

  versioningStatus := aws.GetS3BucketVersioning(t, awsRegion, bucketName)
  assert.Equal(t, "Enabled", versioningStatus)

  encryptionConfig := aws.GetS3BucketServerSideEncryptionConfiguration(t, awsRegion, bucketName)
  assert.NotNil(t, encryptionConfig)
}
```

### Step 5.2 — Initialize and Run

```bash
cd test
go mod init github.com/txwes/cicd-lab-test
go mod tidy
go test -v -timeout 30m
```

Observe the full test cycle: apply, assertions, destroy.

---

## Lab Submission Requirements

Include in your submission document:

1. Screenshot of the GitHub Actions pipeline showing all jobs passing
2. Screenshot of the plan comment on your pull request
3. The tfsec check ID that fired when public access was disabled and the remediation text
4. The exit code output from `terraform plan -detailed-exitcode` after introducing drift
5. Answer: What would you need to change in this pipeline to use OIDC instead of static AWS credentials? (2–3 sentences)

---

## Cleanup

After completing the lab, destroy your resources to avoid AWS charges:

```bash
terraform destroy -auto-approve
```

Also delete the S3 state bucket and DynamoDB lock table if you created them for this lab.

---

End of Module 12 Lab
