# CIS-4337 Infrastructure Automation

## Lab — Module 03: HCL Syntax — Providers, Resources, and Variables

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Write a complete `main.tf` with an AWS provider block, variable declarations, and an `aws_instance` resource.
- Use variable references, local values, and output blocks.
- Apply `count` and `for_each` meta-arguments.
- Use the `lifecycle` block with `prevent_destroy` and `ignore_changes`.
- Interpret plan output for resources created with `count` and `for_each`.

---

## Prerequisites

- Terraform CLI 1.6.0 or later.
- AWS CLI configured with credentials (access key + secret key, or IAM role).
- An AWS Free Tier account. The resources in this lab qualify for Free Tier usage.
- VS Code or another text editor.

If you do not yet have AWS credentials configured, run:

```bash
aws configure
```

Enter your Access Key ID, Secret Access Key, default region (`us-east-1`), and output format (`json`).

---

## Part 1: Write a Complete main.tf with AWS Provider and EC2 Instance

### Step 1.1 — Create the working directory

```bash
mkdir ~/tf-lab-03
cd ~/tf-lab-03
```

### Step 1.2 — Create variables.tf

```hcl
variable "aws_region" {
  description = "AWS region for all resources"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance (Amazon Linux 2 in us-east-1)"
  type        = string
  default     = "ami-0c55b159cbfafe1f0"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"

  validation {
    condition     = contains(["t2.micro", "t3.micro"], var.instance_type)
    error_message = "instance_type must be t2.micro or t3.micro."
  }
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging, or prod."
  }
}

variable "project_name" {
  description = "Project name used in resource tags"
  type        = string
  default     = "cis4337-lab03"
}
```

### Step 1.3 — Create main.tf

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
  region = var.aws_region
}

locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "terraform"
  }
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  tags          = merge(local.common_tags, { Name = "${var.project_name}-web" })
}
```

### Step 1.4 — Create outputs.tf

```hcl
output "web_instance_id" {
  description = "ID of the web EC2 instance"
  value       = aws_instance.web.id
}

output "web_public_ip" {
  description = "Public IP address of the web EC2 instance"
  value       = aws_instance.web.public_ip
}

output "web_instance_state" {
  description = "Current state of the web instance"
  value       = aws_instance.web.instance_state
}
```

### Step 1.5 — Run init and plan

```bash
terraform init
terraform plan
```

Record in `lab_notes.txt`:

1. How many resources does the plan show?
2. What are the `ami` and `instance_type` values shown in the plan?
3. What symbol precedes `aws_instance.web`?

### Step 1.6 — Apply and capture outputs

```bash
terraform apply -auto-approve
```

After apply completes, note the output values printed to the terminal. Then run:

```bash
terraform output
terraform output web_public_ip
```

Record both the instance ID and the public IP in `lab_notes.txt`.

---

## Part 2: Add a count-Based Resource

### Step 2.1 — Add a second EC2 resource using count

Add the following block to `main.tf`:

```hcl
resource "aws_instance" "worker" {
  count         = 2
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = merge(local.common_tags, {
    Name = "${var.project_name}-worker-${count.index}"
  })
}
```

Add the following to `outputs.tf`:

```hcl
output "worker_instance_ids" {
  description = "IDs of the worker instances"
  value       = aws_instance.worker[*].id
}
```

### Step 2.2 — Plan and apply

```bash
terraform plan
terraform apply -auto-approve
```

Record in `lab_notes.txt`:

1. How are the two worker instances addressed in the plan output?
2. What names appear in the `tags` output for each worker?
3. What is the value of `aws_instance.worker[0].id` after apply?

---

## Part 3: Replace count with for_each

### Step 3.1 — Replace the worker resource

Replace the `aws_instance.worker` block in `main.tf` with:

```hcl
variable "worker_names" {
  description = "Names for worker instances"
  type        = set(string)
  default     = ["worker-a", "worker-b"]
}

resource "aws_instance" "worker" {
  for_each      = var.worker_names
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = merge(local.common_tags, {
    Name = "${var.project_name}-${each.value}"
  })
}
```

Update `outputs.tf` to replace the worker output:

```hcl
output "worker_instance_ids" {
  description = "IDs of the worker instances keyed by name"
  value       = { for k, v in aws_instance.worker : k => v.id }
}
```

### Step 3.2 — Plan and observe the change

```bash
terraform plan
```

Record in `lab_notes.txt`:

1. Does the plan show a destroy-and-recreate for the worker instances? Why?
2. How are the `for_each` instances addressed in the plan (e.g., `aws_instance.worker["worker-a"]`)?
3. What is the difference between how `count` and `for_each` address resources?

### Step 3.3 — Apply

```bash
terraform apply -auto-approve
```

---

## Part 4: Use the lifecycle Block

### Step 4.1 — Add lifecycle to the web instance

Add a `lifecycle` block to `aws_instance.web` in `main.tf`:

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  tags          = merge(local.common_tags, { Name = "${var.project_name}-web" })

  lifecycle {
    prevent_destroy = true
    ignore_changes  = [tags]
  }
}
```

### Step 4.2 — Attempt to destroy

```bash
terraform destroy -target=aws_instance.web
```

Terraform should produce an error similar to:

```text
Error: Instance cannot be destroyed
```

Record in `lab_notes.txt`:

1. What exact error message did Terraform produce?
2. What would you need to do to allow deletion of this resource?

### Step 4.3 — Remove prevent_destroy for cleanup

Change `prevent_destroy = true` to `prevent_destroy = false` to allow the destroy in the next step.

---

## Part 5: Destroy All Resources

```bash
terraform destroy -auto-approve
```

Verify that all resources are removed:

```bash
terraform state list
```

Expected: no output (empty state).

---

## Deliverables

Submit the following to Canvas:

1. Final `main.tf` file (after all modifications).
2. Final `variables.tf` file.
3. Final `outputs.tf` file.
4. Screenshot of `terraform apply` completion showing instance creation.
5. Screenshot of `terraform output` showing instance IDs.
6. Screenshot of the `prevent_destroy` error from Part 4.
7. Completed `lab_notes.txt` with all recorded answers.

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| `main.tf` uses correct terraform, provider, locals, and resource blocks | 20 |
| `variables.tf` has correct type constraints and validation blocks | 15 |
| `outputs.tf` correctly references resource attributes | 10 |
| `count`-based resource created; instances addressed by index | 15 |
| `for_each` resource created; instances addressed by key | 20 |
| `lifecycle` block applied; `prevent_destroy` error captured | 10 |
| All resources destroyed cleanly; empty state confirmed | 10 |

---

## Troubleshooting

**Error: InvalidAMIID.NotFound**
The default AMI ID may not be valid in your region. Find the correct Amazon Linux 2 AMI for your region at console.aws.amazon.com by navigating to EC2 > AMIs and searching for "amzn2-ami-hvm".

**Error: UnauthorizedOperation**
Your AWS credentials do not have permission to create EC2 instances. Ensure your IAM user or role has `AmazonEC2FullAccess` or an equivalent policy attached.

**The for_each plan shows destroy-and-recreate for existing workers**
This is expected. Changing from `count` to `for_each` changes the resource address schema, requiring Terraform to destroy the `count`-indexed resources and create `for_each`-keyed ones.

---

Module 03 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
