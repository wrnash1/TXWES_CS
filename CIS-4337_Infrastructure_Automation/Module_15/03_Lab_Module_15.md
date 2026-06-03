# Lab: Module 15 — Advanced Terraform Patterns

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will apply all five advanced Terraform patterns: dynamic blocks to generate security group rules from input data, for_each to deploy multiple subnets, conditional expressions for environment-specific sizing, a moved block to safely rename a resource, and the import block to bring an existing resource under Terraform management.

**Estimated time:** 100–130 minutes

**Prerequisites:**

- Terraform CLI v1.5+ installed
- AWS Free Tier account
- Remote state backend from Module 12 or Module 13 lab

---

## Part 1: Dynamic Blocks (25 minutes)

### Step 1.1 — Create the Lab Configuration

Create `module15-lab/main.tf`:

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
```

Create `module15-lab/variables.tf`:

```hcl
variable "aws_region" {
  type    = string
  default = "us-east-2"
}

variable "owner_tag" {
  type = string
}

variable "environment" {
  type    = string
  default = "dev"
  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "Environment must be dev or prod."
  }
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "security_group_rules" {
  description = "Map of ingress rules for the application security group"
  type = map(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))

  default = {
    "http" = {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTP from anywhere"
    }
    "https" = {
      from_port   = 443
      to_port     = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTPS from anywhere"
    }
    "ssh" = {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["10.0.0.0/8"]
      description = "SSH from internal network only"
    }
  }
}
```

### Step 1.2 — Write the Dynamic Block Security Group

Add to `main.tf`:

```hcl
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name      = "module15-vpc"
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

resource "aws_security_group" "app" {
  name        = "module15-app-sg"
  description = "Application security group with dynamic rules"
  vpc_id      = aws_vpc.main.id

  dynamic "ingress" {
    for_each = var.security_group_rules
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
    description = "Allow all outbound traffic"
  }

  tags = {
    Name      = "module15-app-sg"
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}
```

### Step 1.3 — Plan and Observe

```bash
terraform init
terraform plan -var="owner_tag=your-name"
```

Observe that the plan shows three ingress rules generated from the map. Add a fourth rule to `var.security_group_rules` in your `terraform.tfvars` file and rerun the plan to observe the fourth rule being added without affecting the others.

---

## Part 2: for_each Subnets (25 minutes)

### Step 2.1 — Add Subnet Variables

Add to `variables.tf`:

```hcl
variable "subnets" {
  description = "Map of subnet configurations"
  type = map(object({
    cidr_block        = string
    availability_zone = string
    public            = bool
  }))

  default = {
    "public-a" = {
      cidr_block        = "10.0.1.0/24"
      availability_zone = "us-east-2a"
      public            = true
    }
    "public-b" = {
      cidr_block        = "10.0.2.0/24"
      availability_zone = "us-east-2b"
      public            = true
    }
    "private-a" = {
      cidr_block        = "10.0.10.0/24"
      availability_zone = "us-east-2a"
      public            = false
    }
    "private-b" = {
      cidr_block        = "10.0.11.0/24"
      availability_zone = "us-east-2b"
      public            = false
    }
  }
}
```

### Step 2.2 — Add the for_each Subnet Resource

Add to `main.tf`:

```hcl
resource "aws_subnet" "app" {
  for_each = var.subnets

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value.cidr_block
  availability_zone       = each.value.availability_zone
  map_public_ip_on_launch = each.value.public

  tags = {
    Name      = "module15-${each.key}"
    Tier      = each.value.public ? "public" : "private"
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

output "subnet_ids" {
  description = "Map of subnet name to subnet ID"
  value       = { for k, v in aws_subnet.app : k => v.id }
}
```

### Step 2.3 — Apply and Test for_each Resilience

Apply the configuration:

```bash
terraform apply -var="owner_tag=your-name" -auto-approve
```

Now remove `"private-b"` from the subnets map in your `terraform.tfvars`. Run `terraform plan` and observe that only `aws_subnet.app["private-b"]` is planned for destruction. The other three subnets are unaffected.

This demonstrates the for_each advantage over count: removing one element does not affect other instances.

---

## Part 3: Conditional Expressions (20 minutes)

### Step 3.1 — Add Environment-Conditional Resources

Add to `main.tf`:

```hcl
locals {
  nat_gateway_count = var.environment == "prod" ? length([
    for k, v in var.subnets : k if v.public
  ]) : 1

  enable_flow_logs = var.environment == "prod"
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name      = "module15-igw"
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

resource "aws_flow_log" "vpc" {
  count = local.enable_flow_logs ? 1 : 0

  vpc_id          = aws_vpc.main.id
  traffic_type    = "ALL"
  iam_role_arn    = aws_iam_role.flow_log[0].arn
  log_destination = aws_cloudwatch_log_group.flow_log[0].arn

  tags = {
    Owner     = var.owner_tag
    ManagedBy = "Terraform"
  }
}

resource "aws_cloudwatch_log_group" "flow_log" {
  count             = local.enable_flow_logs ? 1 : 0
  name              = "/vpc/flow-logs/module15"
  retention_in_days = var.environment == "prod" ? 90 : 7
}

data "aws_iam_policy_document" "flow_log_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["vpc-flow-logs.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "flow_log" {
  count              = local.enable_flow_logs ? 1 : 0
  name               = "module15-flow-log-role"
  assume_role_policy = data.aws_iam_policy_document.flow_log_assume.json
}
```

### Step 3.2 — Compare dev vs prod Plans

Run with `environment=dev`:

```bash
terraform plan -var="owner_tag=your-name" -var="environment=dev"
```

Observe that `aws_flow_log.vpc`, `aws_cloudwatch_log_group.flow_log`, and `aws_iam_role.flow_log` are not in the plan (count=0).

Run with `environment=prod`:

```bash
terraform plan -var="owner_tag=your-name" -var="environment=prod"
```

Observe that all three resources appear in the plan. Document the difference in your submission.

---

## Part 4: Moved Blocks (15 minutes)

### Step 4.1 — Rename a Resource

You will rename `aws_internet_gateway.main` to `aws_internet_gateway.primary`. Without a `moved` block, this would show as a destroy and recreate.

Add to `main.tf`:

```hcl
moved {
  from = aws_internet_gateway.main
  to   = aws_internet_gateway.primary
}
```

Change the resource block name from `aws_internet_gateway.main` to `aws_internet_gateway.primary`.

Update any references to `aws_internet_gateway.main` (search your file for them).

### Step 4.2 — Verify the Move

After applying the dev configuration from Part 3, run:

```bash
terraform plan -var="owner_tag=your-name"
```

Observe the plan output. The internet gateway should show as a move operation — no destroy, no create. The line reads something like:

```text
# aws_internet_gateway.main has moved to aws_internet_gateway.primary
```

Apply to confirm the move completes without any infrastructure change.

---

## Part 5: Import Block (15 minutes)

### Step 5.1 — Identify an Existing Resource

In the AWS console, navigate to VPC and note the VPC ID of the VPC you created in Part 1 or any other existing VPC in your account.

### Step 5.2 — Write the Import Block

Create `import.tf`:

```hcl
import {
  id = "vpc-0xxxxxxxxxxxxxxxxx"
  to = aws_vpc.imported_vpc
}

resource "aws_vpc" "imported_vpc" {
  cidr_block = "10.99.0.0/16"
}
```

Replace the VPC ID with the actual ID. Use a VPC that is separate from the one you created in this lab to avoid conflicts.

### Step 5.3 — Generate Configuration

Run:

```bash
terraform plan -generate-config-out=generated_vpc.tf
```

Review `generated_vpc.tf`. Observe how Terraform populated all attributes from the actual VPC. Compare it to the minimal resource block you wrote in `import.tf`.

Run `terraform plan` without `-generate-config-out` and observe the import action in the plan output.

### Step 5.4 — Apply the Import

```bash
terraform apply -var="owner_tag=your-name" -auto-approve
```

Confirm the VPC is now in the state file with `terraform state list`.

---

## Lab Submission Requirements

Include in your submission document:

1. The `terraform plan` output showing three dynamic ingress rules generated from the map
2. The `terraform plan` output showing only `aws_subnet.app["private-b"]` planned for destruction after removing it from the map
3. Side-by-side comparison: the count of resources in the `dev` plan versus the `prod` plan from Part 3
4. The `terraform plan` output showing the moved block as a move operation rather than destroy/create
5. The first 30 lines of the generated `generated_vpc.tf` file
6. Answer: What is the risk of using `count` instead of `for_each` for the subnets in Part 2? Give a specific scenario where count would cause unintended infrastructure changes. (2–3 sentences)

---

## Cleanup

```bash
terraform destroy -var="owner_tag=your-name" -auto-approve
```

Remove `import.tf` before destroying if you imported a VPC you want to keep. Use `terraform state rm aws_vpc.imported_vpc` to remove it from state without destroying it.

---

End of Module 15 Lab
