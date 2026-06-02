# CIS-4337 Infrastructure Automation

## Lab — Module 05: Modules — Creating and Using Reusable Modules

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Create a module directory with `main.tf`, `variables.tf`, and `outputs.tf`.
- Call a local module from a root configuration and pass variable values.
- Reference module output values in root-level resources and outputs.
- Inspect module resource addresses in state.
- Call a module from the public Terraform Registry.

---

## Prerequisites

- Terraform CLI 1.6.0 or later.
- AWS CLI configured with credentials (EC2 and VPC permissions).
- An AWS Free Tier account.

---

## Part 1: Create the VPC Module

### Step 1.1 — Create the directory structure

```bash
mkdir -p ~/tf-lab-05/modules/vpc
cd ~/tf-lab-05
```

### Step 1.2 — Create modules/vpc/variables.tf

```hcl
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}
```

### Step 1.3 — Create modules/vpc/main.tf

```hcl
resource "aws_vpc" "this" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name        = "${var.environment}-vpc"
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id

  tags = {
    Name = "${var.environment}-igw"
  }
}

resource "aws_subnet" "public" {
  count                   = length(var.public_subnet_cidrs)
  vpc_id                  = aws_vpc.this.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name        = "${var.environment}-public-${count.index + 1}"
    Environment = var.environment
  }
}
```

### Step 1.4 — Create modules/vpc/outputs.tf

```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.this.id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public[*].id
}

output "internet_gateway_id" {
  description = "ID of the internet gateway"
  value       = aws_internet_gateway.this.id
}
```

---

## Part 2: Call the Module from the Root Configuration

### Step 2.1 — Create root main.tf

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

module "network" {
  source = "./modules/vpc"

  vpc_cidr            = "10.0.0.0/16"
  environment         = var.environment
  public_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
}
```

### Step 2.2 — Create root variables.tf

```hcl
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "lab05"
}
```

### Step 2.3 — Create root outputs.tf

```hcl
output "vpc_id" {
  description = "VPC ID from the network module"
  value       = module.network.vpc_id
}

output "public_subnet_ids" {
  description = "Public subnet IDs from the network module"
  value       = module.network.public_subnet_ids
}
```

### Step 2.4 — Initialize and plan

```bash
terraform init
terraform plan
```

Record in `lab_notes.txt`:

1. How many resources does the plan show? Name each one.
2. What are the resource addresses in the plan output? Do they include the `module.network.` prefix?
3. What would happen if you ran `terraform plan` without running `terraform init` first?

### Step 2.5 — Apply

```bash
terraform apply -auto-approve
```

After apply, view the outputs:

```bash
terraform output
terraform output vpc_id
terraform output public_subnet_ids
```

Record the VPC ID and both subnet IDs in `lab_notes.txt`.

---

## Part 3: Inspect Module Resources in State

### Step 3.1 — List state

```bash
terraform state list
```

Record in `lab_notes.txt`:

1. What prefix appears before each resource created by the module?
2. How does the address of `aws_vpc.this` inside the module differ from a root-level `aws_vpc.main` resource?

### Step 3.2 — Show a module resource

```bash
terraform state show module.network.aws_vpc.this
```

Confirm the `id` matches the `vpc_id` output.

### Step 3.3 — Add a root-level resource using module output

Add the following to the root `main.tf`:

```hcl
resource "aws_security_group" "web" {
  name        = "${var.environment}-web-sg"
  description = "Security group for web servers"
  vpc_id      = module.network.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.environment}-web-sg"
  }
}
```

Add to `outputs.tf`:

```hcl
output "web_sg_id" {
  description = "Security group ID for web servers"
  value       = aws_security_group.web.id
}
```

Run `terraform plan` and confirm Terraform plans to create the security group inside the VPC created by the module.

```bash
terraform apply -auto-approve
```

---

## Part 4: Call a Registry Module

### Step 4.1 — Add a registry module call

Add the following to the root `main.tf` to use the community S3 bucket module:

```hcl
module "s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "~> 3.0"

  bucket = "cis4337-lab05-${var.environment}-data"
  acl    = "private"

  versioning = {
    enabled = true
  }

  tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
```

Add to `outputs.tf`:

```hcl
output "s3_bucket_name" {
  description = "S3 bucket name from registry module"
  value       = module.s3_bucket.s3_bucket_id
}
```

### Step 4.2 — Re-initialize to download the registry module

```bash
terraform init
```

Record: Where does Terraform store the downloaded registry module? Run `ls .terraform/modules/` to inspect.

### Step 4.3 — Plan and apply

```bash
terraform plan
terraform apply -auto-approve
```

---

## Part 5: Destroy All Resources

```bash
terraform destroy -auto-approve
```

Confirm all resources are removed:

```bash
terraform state list
```

---

## Deliverables

Submit to Canvas:

1. Screenshots of `modules/vpc/main.tf`, `modules/vpc/variables.tf`, and `modules/vpc/outputs.tf`.
2. Screenshot of `terraform plan` output showing module-prefixed resource addresses.
3. Screenshot of `terraform output` showing VPC ID and subnet IDs.
4. Screenshot of `terraform state list` showing module resource addresses.
5. Screenshot of `terraform init` after adding the registry module, showing the download.
6. Completed `lab_notes.txt` with all recorded answers.

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| VPC module created with correct three-file structure | 20 |
| Root configuration calls module with correct `source` and inputs | 15 |
| Module outputs referenced correctly in root resources and outputs | 15 |
| State addresses include `module.network.` prefix; confirmed with `state list` | 15 |
| Security group created using `module.network.vpc_id` reference | 15 |
| Registry module called with version constraint; `terraform init` re-run | 10 |
| All resources destroyed cleanly | 10 |

---

## Troubleshooting

**Error: Module not installed**
Run `terraform init`. You must re-run `init` every time you add or change a `module` block's `source` or `version`.

**Error: Unsupported argument**
The registry module you are calling does not accept the `acl` argument in newer versions. Remove the `acl` line and rely on the default bucket-owner-full-control ACL.

**The registry module download is slow**
Registry modules are downloaded from GitHub. If your network is slow, allow extra time. The module is cached after the first download.

---

Module 05 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
