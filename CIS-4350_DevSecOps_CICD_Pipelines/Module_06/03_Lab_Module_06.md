# Lab 06 — IaC Security: Scanning Terraform with tfsec, checkov, and Conftest

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Texas Wesleyan University | Professor Nash

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Lab Overview

In this lab you will write intentionally insecure Terraform configurations, scan them with tfsec and checkov to identify misconfigurations, write a custom OPA Rego policy and test it with Conftest, remediate the findings, and integrate the scanning pipeline into GitHub Actions.

**Estimated Time:** 90–120 minutes

**Difficulty:** Intermediate

---

## Prerequisites

- Terraform CLI installed (`terraform version`)
- Docker (for tfsec and checkov via container)
- Python 3.8+ for checkov CLI installation
- Git and GitHub account
- An AWS or Azure account is NOT required — all scanning is static analysis

---

## Part 1 — Insecure Terraform Configuration (15 minutes)

### Part 1 Objective

Create a Terraform module with multiple security misconfigurations that scanners will detect.

### Step 1.1 — Initialize the Project

```bash
mkdir ~/lab06-iac-security && cd ~/lab06-iac-security
git init && git checkout -b main
mkdir infra policies
```

### Step 1.2 — Write Insecure Terraform

Create `infra/main.tf`:

```hcl
terraform {
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

# MISCONFIGURATION 1: S3 bucket with public access
resource "aws_s3_bucket" "app_data" {
  bucket = "my-app-data-bucket-lab06"
}

resource "aws_s3_bucket_acl" "app_data_acl" {
  bucket = aws_s3_bucket.app_data.id
  acl    = "public-read"
}

# MISCONFIGURATION 2: No encryption at rest
# (no aws_s3_bucket_server_side_encryption_configuration)

# MISCONFIGURATION 3: Security group open to world on port 22
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Web server security group"
  vpc_id      = "vpc-00000000"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "SSH from anywhere"
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTP from anywhere"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "All outbound traffic"
  }
}

# MISCONFIGURATION 4: RDS instance publicly accessible
resource "aws_db_instance" "app_db" {
  identifier        = "lab06-db"
  engine            = "mysql"
  engine_version    = "8.0"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  db_name           = "appdb"
  username          = "admin"
  password          = "SuperSecret123!"  # MISCONFIGURATION 5: Hardcoded password
  publicly_accessible    = true
  skip_final_snapshot    = true
  storage_encrypted      = false  # MISCONFIGURATION 6: Unencrypted RDS
  deletion_protection    = false
  backup_retention_period = 0     # MISCONFIGURATION 7: No backups
}
```

---

## Part 2 — Scan with tfsec (20 minutes)

### Part 2 Objective

Run tfsec and interpret the findings against the insecure Terraform configuration.

### Step 2.1 — Run tfsec via Docker

```bash
docker run --rm \
  -v "$(pwd)/infra:/terraform" \
  aquasec/tfsec:latest /terraform \
  --format lovely \
  2>&1 | tee tfsec-results.txt
```

### Step 2.2 — Run tfsec with SARIF Output

```bash
docker run --rm \
  -v "$(pwd)/infra:/terraform" \
  -v "$(pwd):/output" \
  aquasec/tfsec:latest /terraform \
  --format sarif \
  --out /output/tfsec-results.sarif
```

### Step 2.3 — Record Findings

In your lab report, create a table listing every finding tfsec reports with:

- Rule ID (e.g., `aws-s3-no-public-buckets`)
- Severity
- Affected resource
- Brief description of the issue

You should find at least 6 distinct findings.

---

## Part 3 — Scan with checkov (20 minutes)

### Part 3 Objective

Run checkov against the same Terraform configuration and compare findings to tfsec.

### Step 3.1 — Install and Run checkov

```bash
pip install checkov

checkov -d infra/ \
  --framework terraform \
  --output cli \
  2>&1 | tee checkov-results.txt
```

### Step 3.2 — Run checkov with SARIF Output

```bash
checkov -d infra/ \
  --framework terraform \
  --output sarif \
  --output-file-path ./ \
  --soft-fail
```

### Step 3.3 — Compare tfsec and checkov Findings

Create a comparison table in your lab report:

| Finding | Found by tfsec | Found by checkov |
|---|---|---|
| Public S3 bucket | | |
| No S3 encryption | | |
| SSH open to 0.0.0.0/0 | | |
| RDS publicly accessible | | |
| RDS storage not encrypted | | |
| Hardcoded RDS password | | |
| No RDS backup retention | | |

Which tool found more issues? Were there findings unique to one tool?

---

## Part 4 — Write a Custom OPA Policy with Conftest (20 minutes)

### Part 4 Objective

Write a Rego policy that enforces an organization-specific rule: all RDS instances must have `deletion_protection = true`.

### Step 4.1 — Install Conftest

```bash
# On Linux/macOS
wget https://github.com/open-policy-agent/conftest/releases/download/v0.50.0/conftest_0.50.0_linux_amd64.tar.gz
tar xzf conftest_*.tar.gz
sudo mv conftest /usr/local/bin/

# Verify
conftest --version
```

### Step 4.2 — Generate a Terraform Plan JSON

```bash
cd infra/
terraform init -backend=false
terraform plan -out=tfplan.binary 2>/dev/null || true
terraform show -json tfplan.binary > ../tfplan.json 2>/dev/null || \
  echo '{"resource_changes": []}' > ../tfplan.json
cd ..
```

If you do not have AWS credentials, create a mock plan JSON for policy testing:

```bash
cat > tfplan.json << 'EOF'
{
  "resource_changes": [
    {
      "address": "aws_db_instance.app_db",
      "type": "aws_db_instance",
      "change": {
        "actions": ["create"],
        "after": {
          "deletion_protection": false,
          "storage_encrypted": false,
          "publicly_accessible": true,
          "backup_retention_period": 0
        }
      }
    }
  ]
}
EOF
```

### Step 4.3 — Write Rego Policies

Create `policies/terraform/rds_security.rego`:

```rego
package main

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_db_instance"
  resource.change.actions[_] == "create"
  resource.change.after.deletion_protection == false
  msg := sprintf(
    "RDS instance '%s' must have deletion_protection = true",
    [resource.address]
  )
}

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_db_instance"
  resource.change.actions[_] == "create"
  resource.change.after.storage_encrypted == false
  msg := sprintf(
    "RDS instance '%s' must have storage_encrypted = true",
    [resource.address]
  )
}

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_db_instance"
  resource.change.actions[_] == "create"
  resource.change.after.publicly_accessible == true
  msg := sprintf(
    "RDS instance '%s' must not be publicly_accessible",
    [resource.address]
  )
}
```

### Step 4.4 — Run Conftest

```bash
conftest test tfplan.json --policy policies/terraform/
```

All three policies should produce `FAIL` messages. Record the output.

### Step 4.5 — Remediate One Policy and Re-test

Update `tfplan.json` to set `deletion_protection: true` only, then re-run Conftest. Confirm the deletion protection check now passes while the other two still fail. Record both outputs.

---

## Part 5 — Remediate and Integrate into GitHub Actions (15 minutes)

### Part 5 Objective

Fix the Terraform misconfigurations and write the CI pipeline.

### Step 5.1 — Create the Secure Terraform File

Create `infra/main_secure.tf` (keep `main.tf` for comparison):

```hcl
# infra/main_secure.tf — remediated configuration

resource "aws_s3_bucket" "app_data_secure" {
  bucket = "company-app-data-lab06-secure"
}

resource "aws_s3_bucket_public_access_block" "app_data_secure" {
  bucket                  = aws_s3_bucket.app_data_secure.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "app_data_secure" {
  bucket = aws_s3_bucket.app_data_secure.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_versioning" "app_data_secure" {
  bucket = aws_s3_bucket.app_data_secure.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

### Step 5.2 — Write the IaC Security Pipeline

Create `.github/workflows/iac-security.yml`:

```yaml
name: IaC Security Pipeline

on:
  pull_request:
    paths:
      - infra/**
      - policies/**

permissions:
  contents: read
  security-events: write

jobs:
  terraform-validate:
    name: Terraform Validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.7.0
      - run: terraform -chdir=infra/ init -backend=false
      - run: terraform -chdir=infra/ validate
      - run: terraform -chdir=infra/ fmt -check -recursive

  tfsec:
    name: tfsec Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aquasecurity/tfsec-action@v1.0.0
        with:
          working_directory: infra/
          soft_fail: false
          format: sarif
          sarif_file: tfsec.sarif
      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: tfsec.sarif

  checkov:
    name: checkov Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: bridgecrewio/checkov-action@master
        with:
          directory: infra/
          framework: terraform
          soft_fail: false
          output_format: sarif
          output_file_path: checkov.sarif
      - uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: checkov.sarif

  conftest:
    name: OPA Policy Validation
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install conftest
        run: |
          wget -q https://github.com/open-policy-agent/conftest/releases/download/v0.50.0/conftest_0.50.0_linux_amd64.tar.gz
          tar xzf conftest_*.tar.gz && sudo mv conftest /usr/local/bin/
      - name: Run Conftest
        run: conftest test tfplan.json --policy policies/terraform/
```

---

## Deliverables

Submit the following on Canvas:

1. `tfsec-results.txt` and `checkov-results.txt` (Parts 2 and 3)
2. Comparison table showing which tool detected which finding (Part 3, Step 3.3)
3. `policies/terraform/rds_security.rego` — completed Rego policy file (Part 4)
4. Screenshot of Conftest reporting three FAIL findings (Part 4, Step 4.4)
5. Screenshot of Conftest with deletion_protection passing (Part 4, Step 4.5)
6. Completed `.github/workflows/iac-security.yml` (Part 5)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| tfsec and checkov output files — 6+ findings identified | 20 |
| Comparison table — accurate, complete | 15 |
| Rego policy — syntactically correct, 3 deny rules | 25 |
| Conftest FAIL screenshot (all 3 findings) | 15 |
| Conftest partial pass screenshot | 10 |
| GitHub Actions workflow — syntactically correct, 4 jobs | 15 |
| Total | 100 |

---

Lab 06 | CIS-4350 | Texas Wesleyan University | Professor Nash
