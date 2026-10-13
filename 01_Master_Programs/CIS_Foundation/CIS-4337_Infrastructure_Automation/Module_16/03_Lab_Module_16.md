# Lab: Module 16 — Terraform Associate 003 Capstone Project

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Lab Overview

This capstone lab integrates the skills from all 15 previous modules into a single production-grade Terraform configuration. You will deploy a three-tier web application infrastructure on AWS incorporating: a VPC with multi-AZ subnets, security groups with dynamic rules, an application load balancer, auto-scaling EC2 instances, an RDS database, encrypted S3 state backend, sensitive variable handling, and a CI/CD-ready structure. You will then run a security scan, simulate drift, and complete a self-assessment against all exam objective domains.

**Estimated time:** 3–4 hours

**Prerequisites:**

- All previous lab exercises completed or concepts understood
- Terraform CLI v1.5+ installed
- AWS Free Tier account (note: this lab deploys an ALB and RDS instance which incur small charges — destroy immediately after completing)
- Checkov installed

---

## Part 1: Project Structure (20 minutes)

### Step 1.1 — Create the Directory Layout

```text
capstone/
  modules/
    networking/
      main.tf
      variables.tf
      outputs.tf
    compute/
      main.tf
      variables.tf
      outputs.tf
    database/
      main.tf
      variables.tf
      outputs.tf
  main.tf
  variables.tf
  outputs.tf
  backend.tf
  versions.tf
  terraform.tfvars.example
```

### Step 1.2 — Write versions.tf

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
```

---

## Part 2: Networking Module (35 minutes)

### Step 2.1 — Networking Module Variables

Create `modules/networking/variables.tf`:

```hcl
variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
}

variable "environment" {
  type        = string
  description = "Environment name"
}

variable "owner_tag" {
  type        = string
  description = "Owner tag for cost allocation"
}

variable "public_subnets" {
  type = map(object({
    cidr_block        = string
    availability_zone = string
  }))
  description = "Map of public subnet configurations"
}

variable "private_subnets" {
  type = map(object({
    cidr_block        = string
    availability_zone = string
  }))
  description = "Map of private subnet configurations"
}

variable "alb_ingress_rules" {
  type = map(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))
  description = "Map of ALB security group ingress rules"
}
```

### Step 2.2 — Networking Module Main

Create `modules/networking/main.tf`:

```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "${var.environment}-vpc"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name        = "${var.environment}-igw"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_subnet" "public" {
  for_each = var.public_subnets

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value.cidr_block
  availability_zone       = each.value.availability_zone
  map_public_ip_on_launch = true

  tags = {
    Name        = "${var.environment}-public-${each.key}"
    Tier        = "public"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_subnet" "private" {
  for_each = var.private_subnets

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value.cidr_block
  availability_zone       = each.value.availability_zone
  map_public_ip_on_launch = false

  tags = {
    Name        = "${var.environment}-private-${each.key}"
    Tier        = "private"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_security_group" "alb" {
  name        = "${var.environment}-alb-sg"
  description = "Security group for application load balancer"
  vpc_id      = aws_vpc.main.id

  dynamic "ingress" {
    for_each = var.alb_ingress_rules
    iterator = rule

    content {
      from_port   = rule.value.from_port
      to_port     = rule.value.to_port
      protocol    = rule.value.protocol
      cidr_blocks = rule.value.cidr_blocks
      description = rule.value.description
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound"
  }

  tags = {
    Name        = "${var.environment}-alb-sg"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_security_group" "app" {
  name        = "${var.environment}-app-sg"
  description = "Security group for application instances"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.alb.id]
    description     = "Allow traffic from ALB only"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound"
  }

  tags = {
    Name        = "${var.environment}-app-sg"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_security_group" "db" {
  name        = "${var.environment}-db-sg"
  description = "Security group for RDS database"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.app.id]
    description     = "Allow PostgreSQL from app tier only"
  }

  tags = {
    Name        = "${var.environment}-db-sg"
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}
```

### Step 2.3 — Networking Module Outputs

Create `modules/networking/outputs.tf`:

```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = { for k, v in aws_subnet.public : k => v.id }
}

output "private_subnet_ids" {
  value = { for k, v in aws_subnet.private : k => v.id }
}

output "alb_security_group_id" {
  value = aws_security_group.alb.id
}

output "app_security_group_id" {
  value = aws_security_group.app.id
}

output "db_security_group_id" {
  value = aws_security_group.db.id
}
```

---

## Part 3: Database Module (25 minutes)

Create `modules/database/variables.tf`:

```hcl
variable "environment" { type = string }
variable "owner_tag" { type = string }
variable "vpc_id" { type = string }
variable "subnet_ids" { type = map(string) }
variable "db_security_group_id" { type = string }
variable "db_username" {
  type      = string
  sensitive = true
}
variable "db_password" {
  type      = string
  sensitive = true
}
variable "instance_class" {
  type    = string
  default = "db.t3.micro"
}
```

Create `modules/database/main.tf`:

```hcl
resource "aws_db_subnet_group" "main" {
  name       = "${var.environment}-db-subnet-group"
  subnet_ids = values(var.subnet_ids)

  tags = {
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}

resource "aws_db_instance" "main" {
  identifier             = "${var.environment}-app-db"
  engine                 = "postgres"
  engine_version         = "15.4"
  instance_class         = var.instance_class
  allocated_storage      = 20
  storage_encrypted      = true
  username               = var.db_username
  password               = var.db_password
  db_name                = "appdb"
  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [var.db_security_group_id]
  skip_final_snapshot    = true
  publicly_accessible    = false
  deletion_protection    = false
  backup_retention_period = var.environment == "prod" ? 7 : 1
  multi_az               = var.environment == "prod"

  tags = {
    Environment = var.environment
    Owner       = var.owner_tag
    ManagedBy   = "Terraform"
  }
}
```

Create `modules/database/outputs.tf`:

```hcl
output "db_endpoint" {
  value = aws_db_instance.main.endpoint
}

output "db_name" {
  value = aws_db_instance.main.db_name
}
```

---

## Part 4: Root Module and Apply (30 minutes)

### Step 4.1 — Root variables.tf

```hcl
variable "environment" {
  type    = string
  default = "dev"
}

variable "aws_region" {
  type    = string
  default = "us-east-2"
}

variable "owner_tag" { type = string }

variable "db_username" {
  type      = string
  sensitive = true
}

variable "db_password" {
  type      = string
  sensitive = true
}
```

### Step 4.2 — Root main.tf

```hcl
provider "aws" {
  region = var.aws_region
}

module "networking" {
  source      = "./modules/networking"
  vpc_cidr    = "10.0.0.0/16"
  environment = var.environment
  owner_tag   = var.owner_tag

  public_subnets = {
    "a" = { cidr_block = "10.0.1.0/24", availability_zone = "${var.aws_region}a" }
    "b" = { cidr_block = "10.0.2.0/24", availability_zone = "${var.aws_region}b" }
  }

  private_subnets = {
    "a" = { cidr_block = "10.0.10.0/24", availability_zone = "${var.aws_region}a" }
    "b" = { cidr_block = "10.0.11.0/24", availability_zone = "${var.aws_region}b" }
  }

  alb_ingress_rules = {
    "http"  = { from_port = 80,  to_port = 80,  protocol = "tcp", cidr_blocks = ["0.0.0.0/0"], description = "HTTP" }
    "https" = { from_port = 443, to_port = 443, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"], description = "HTTPS" }
  }
}

module "database" {
  source               = "./modules/database"
  environment          = var.environment
  owner_tag            = var.owner_tag
  vpc_id               = module.networking.vpc_id
  subnet_ids           = module.networking.private_subnet_ids
  db_security_group_id = module.networking.db_security_group_id
  db_username          = var.db_username
  db_password          = var.db_password
  instance_class       = var.environment == "prod" ? "db.r6g.large" : "db.t3.micro"
}
```

### Step 4.3 — Pass Secrets via Environment Variables

```bash
export TF_VAR_db_username="capstoneadmin"
export TF_VAR_db_password="CapstoneLabPassword2024!"
export TF_VAR_owner_tag="your-name"
```

### Step 4.4 — Initialize, Scan, and Plan

```bash
terraform init
checkov -d . --framework terraform --output cli
terraform plan
```

Review the plan. Verify the resource count and check that sensitive values are redacted in the output.

---

## Part 5: Security Scan and Exam Self-Assessment (30 minutes)

### Step 5.1 — Checkov Scan

Run a full Checkov scan and identify any findings. For each finding, look up the CIS control it maps to and write a one-sentence remediation note.

### Step 5.2 — Exam Domain Self-Assessment

Rate your confidence in each domain from 1 (need more study) to 5 (exam-ready):

| Domain | Topic | Confidence (1–5) |
|--------|-------|-----------------|
| 1 | IaC concepts, declarative vs. imperative | |
| 2 | Terraform's purpose, comparison to other tools | |
| 3 | HCL syntax, variable types, functions | |
| 4 | terraform import, taint, state subcommands, workspaces | |
| 5 | Module structure, sources, versioning, inputs/outputs | |
| 6 | Core workflow commands and all flags | |
| 7 | State file, remote backends, locking, workspaces | |
| 8 | Reading provider documentation, import ID formats | |
| 9 | Terraform Cloud, Sentinel, HCP vs. Enterprise | |

Study any domain where your confidence is below 4 before scheduling your exam.

---

## Lab Submission Requirements

Include in your submission document:

1. Screenshot of `terraform plan` showing resource counts per module
2. Screenshot of at least one `(sensitive value)` redaction in the plan output
3. Checkov scan output with any findings and your one-sentence remediation note for each
4. Your completed Exam Domain Self-Assessment table
5. A brief reflection (150–200 words): What concept from this course was most challenging for you, and how has your understanding changed from Module 1 to Module 16?

---

## Cleanup

```bash
terraform destroy -auto-approve
```

This destroy may take 10–15 minutes due to the RDS instance deletion. Verify all resources are removed in the AWS console after destroy completes.

---

## Part 9 — Challenge Exercise

### Challenge 1: Capstone CI/CD Pipeline with Drift Alerting

Connect the capstone project to a GitHub Actions pipeline that includes security scanning, planning on pull requests, applying on merge, and nightly drift detection with automatic GitHub Issue creation.

**Step A.** Initialize a Git repository in the `capstone/` directory and push it to GitHub. Add a `.gitignore` file before the first commit:

```text
.terraform/
terraform.tfstate
terraform.tfstate.backup
*.tfstate
*.tfvars
.terraform.lock.hcl
```

Note: in production, you commit `.terraform.lock.hcl` — it is excluded here only because the lab does not have a stable provider version to lock to. In real projects, commit the lock file.

**Step B.** Create `.github/workflows/capstone-ci.yml`:

```yaml
name: Capstone CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 7 * * *'
  workflow_dispatch:

permissions:
  contents: read
  pull-requests: write
  issues: write
  id-token: write

env:
  TF_VERSION: "1.6.6"
  AWS_DEFAULT_REGION: "us-east-2"

jobs:
  security:
    name: Security Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Checkov
        uses: bridgecrewio/checkov-action@v12
        with:
          directory: .
          framework: terraform
          soft_fail: true

  validate:
    name: Validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      - run: terraform fmt -check -recursive
      - run: terraform init -backend=false
      - run: terraform validate

  plan:
    name: Plan
    runs-on: ubuntu-latest
    needs: [security, validate]
    if: github.event_name == 'pull_request'
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      TF_VAR_db_username: ${{ secrets.TF_VAR_DB_USERNAME }}
      TF_VAR_db_password: ${{ secrets.TF_VAR_DB_PASSWORD }}
      TF_VAR_owner_tag: ${{ secrets.TF_VAR_OWNER_TAG }}
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      - run: terraform init
      - id: plan
        run: terraform plan -no-color -input=false
      - uses: actions/github-script@v7
        if: always()
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '#### Capstone Plan\n```\n${{ steps.plan.outputs.stdout }}\n```'
            });

  drift:
    name: Drift Detection
    runs-on: ubuntu-latest
    if: github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      TF_VAR_db_username: ${{ secrets.TF_VAR_DB_USERNAME }}
      TF_VAR_db_password: ${{ secrets.TF_VAR_DB_PASSWORD }}
      TF_VAR_owner_tag: ${{ secrets.TF_VAR_OWNER_TAG }}
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      - run: terraform init
      - id: drift
        run: |
          terraform plan -detailed-exitcode -no-color 2>&1 | tee plan.txt
          echo "code=${PIPESTATUS[0]}" >> "$GITHUB_OUTPUT"
      - uses: actions/github-script@v7
        if: steps.drift.outputs.code == '2'
        with:
          script: |
            const plan = require('fs').readFileSync('plan.txt','utf8');
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Capstone Drift — ' + new Date().toISOString().split('T')[0],
              body: '## Drift Detected\n\n```\n' + plan.slice(0,4000) + '\n```',
              labels: ['infrastructure','drift']
            });
```

1. Commit the workflow file and push. Use `workflow_dispatch` to trigger the drift detection job manually. Confirm it runs without errors when no drift is present (exit code 0, no issue created).
2. Manually change one tag on the VPC in the AWS console. Re-trigger the drift job and confirm it creates a GitHub Issue with the plan output.
3. Run `terraform apply` to resolve the drift, then trigger the workflow again to confirm the issue is no longer created (exit code 0).
4. Document in `lab_notes.txt`: the pipeline uses static AWS credentials stored as GitHub secrets. List three specific security improvements you would make to this pipeline for a production deployment at a financial services company, and explain the threat each improvement addresses.

### Challenge 2: Full Exam Domain Review Sprint

Complete a timed self-assessment covering all nine exam domains using only the course materials and your own notes — no external resources.

**Step A.** Set a 90-minute timer. Without opening any HashiCorp documentation, answer the following in `exam_sprint.txt`:

```text
Domain 1 — IaC Concepts:
1. Name three benefits of IaC over manual provisioning.
2. What is the difference between declarative and imperative IaC? Give one example of each.
3. Define idempotency in the context of Terraform.

Domain 2 — Terraform Purpose:
4. Name two cloud providers Terraform supports and the environment variable convention each uses for authentication.
5. What does Terraform use state for? Name three things the state file contains.

Domain 3 — Terraform Basics:
6. Write the HCL syntax for a resource block creating an S3 bucket named "my-bucket" with an Owner tag.
7. Name five Terraform built-in functions and describe what each does.
8. What is the difference between list(string), set(string), and map(string)?

Domain 4 — Outside Core Workflow:
9. What is the difference between terraform taint and terraform apply -replace?
10. Name all six terraform state subcommands and describe each.

Domain 5 — Modules:
11. What are the three required files for a Terraform Registry module?
12. Write the module source string format for a module from the public registry.
13. How do you reference an output named "vpc_id" from a module named "networking"?

Domain 6 — Core Workflow:
14. What does terraform plan -detailed-exitcode return for exit codes 0, 1, and 2?
15. List all variable precedence sources from lowest to highest.
16. What does -backend=false do on terraform init?

Domain 7 — State:
17. Describe what state locking does and how the S3 backend implements it.
18. What is partial backend configuration and why is it useful?
19. What command releases a stuck state lock and when should you use it?

Domain 8 — Documentation:
20. Where in provider documentation do you find the import ID format for a resource?

Domain 9 — Terraform Cloud:
21. Name all three Sentinel policy enforcement levels and describe each.
22. What is the difference between Terraform Enterprise and HCP Terraform?
23. What is a run trigger in Terraform Cloud?
```

**Step B.** After the timer ends, compare your answers to the reading guides and quizzes from Modules 01–16. For any answer you were unable to complete or got wrong, mark the corresponding domain in your self-assessment table from Part 5 with a lower confidence score and schedule an additional 30-minute review session for that domain before your exam.

1. Record in `exam_sprint.txt` your overall score (number of questions answered correctly out of 23) and the two domains where you had the most difficulty.
2. If any domain scored below 70%, re-read the corresponding section of this module's reading guide and re-attempt those domain questions from memory.
3. Schedule your Terraform Associate 003 certification exam once you can consistently score 85% or higher on timed domain reviews. The exam contains 57 questions with a 60-minute time limit.

### Reflection Questions

1. The capstone project uses three separate modules (networking, compute, database) that communicate through outputs and inputs. Describe the dependency chain from the database module's perspective: what outputs does it consume from the networking module, and what would happen to the database resources in Terraform's plan if the networking module were removed from the root configuration without first destroying the database module? Explain the specific error Terraform would encounter and how you would safely decommission the full stack.
2. Looking back across all 16 modules of this course, identify the single Terraform concept you believe poses the greatest operational risk in a production environment if misunderstood or misapplied. Explain the specific failure scenario, identify which module covered this concept, and describe the defense-in-depth controls (tooling, process, policy) you would put in place to prevent the failure from reaching production infrastructure.

---

End of Module 16 Capstone Lab
