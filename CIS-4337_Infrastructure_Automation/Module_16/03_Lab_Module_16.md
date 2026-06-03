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

End of Module 16 Capstone Lab
