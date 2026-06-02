# CIS-4337 Infrastructure Automation

## Reading Guide — Module 03: HCL Syntax — Providers, Resources, and Variables

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This module covers the complete HCL block vocabulary used in Terraform configurations. Every concept here is tested on the Terraform Associate 003 exam and used in every subsequent lab. Read this guide in full before beginning the lab.

---

## 1. Core Vocabulary

**Block**
The fundamental syntactic unit of HCL. A block has a type keyword, zero or more string labels, and a body enclosed in `{}`. Example: `resource "aws_instance" "web" { ... }`.

**Block Type**
The first keyword of a block that determines its purpose. Core block types: `terraform`, `provider`, `resource`, `data`, `variable`, `output`, `locals`, `module`.

**Resource Type**
The first label of a `resource` block that identifies which provider resource is being managed (e.g., `aws_instance`, `aws_s3_bucket`). The format is `<provider>_<resource>`.

**Local Name**
The second label of a `resource` or `data` block. Used to reference the resource within the configuration. The full resource address is `<resource_type>.<local_name>`.

**Meta-Argument**
A special argument accepted by all resource blocks regardless of provider. Controls Terraform behavior toward the resource. Meta-arguments: `depends_on`, `count`, `for_each`, `provider`, `lifecycle`.

**Implicit Dependency**
A dependency created automatically when one resource references an attribute of another. Terraform detects these references and orders resource creation accordingly.

**Explicit Dependency**
A dependency created with `depends_on` when no attribute reference exists but one resource must be fully created before another can begin.

**Variable Type Constraint**
A type declaration in a `variable` block that restricts what values are accepted. Types include `string`, `number`, `bool`, `list(T)`, `set(T)`, `map(T)`, `object({...})`, `tuple([...])`, and `any`.

**Sensitive Value**
A value marked with `sensitive = true` in a variable or output block. Terraform suppresses display of sensitive values in plan and apply output. The value is still stored in state.

**Local Value**
An expression defined in a `locals` block and referenced as `local.<name>`. Used to avoid repetition. Cannot be overridden from outside the module.

---

## 2. HCL Block Types — Complete Reference

### terraform Block

```hcl
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "my-tfstate-bucket"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

The `terraform` block may appear only once per configuration. The `backend` block inside it configures remote state storage (covered in Module 04).

### provider Block

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}
```

A resource selects a non-default provider with `provider = aws.west` inside its block body. Provider configurations should never contain hardcoded credentials.

### resource Block

```hcl
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "main-vpc"
  }
}
```

### data Block

Data sources read existing infrastructure that Terraform does not manage:

```hcl
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
```

Referenced as `data.<type>.<name>.<attribute>`: `data.aws_ami.amazon_linux.id`.

### variable Block

```hcl
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"

  validation {
    condition     = contains(["t3.micro", "t3.small", "t3.medium"], var.instance_type)
    error_message = "Must be t3.micro, t3.small, or t3.medium."
  }
}
```

### output Block

```hcl
output "vpc_id" {
  description = "ID of the main VPC"
  value       = aws_vpc.main.id
}

output "db_password" {
  value     = aws_db_instance.primary.password
  sensitive = true
}
```

### locals Block

```hcl
locals {
  env_prefix = "${var.environment}-${var.project}"

  common_tags = {
    Environment = var.environment
    Project     = var.project
    ManagedBy   = "terraform"
  }
}
```

Referenced as `local.env_prefix`, `local.common_tags`.

---

## 3. Resource Meta-Arguments

### depends_on

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  depends_on = [aws_iam_role_policy_attachment.app_policy]
}
```

Use when: resource B depends on resource A but B does not reference any of A's attributes.

### count

```hcl
resource "aws_subnet" "public" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
}
```

Access individual instances with `aws_subnet.public[0]`, `aws_subnet.public[1]`, etc.

### for_each

```hcl
variable "buckets" {
  type    = map(string)
  default = {
    logs    = "us-east-1"
    backups = "us-west-2"
  }
}

resource "aws_s3_bucket" "storage" {
  for_each = var.buckets
  bucket   = "myapp-${each.key}-bucket"
  region   = each.value
}
```

Access instances with `aws_s3_bucket.storage["logs"]`. Preferred over `count` when resources have meaningful names because it avoids index renumbering.

### lifecycle

```hcl
resource "aws_db_instance" "primary" {
  # database configuration ...

  lifecycle {
    prevent_destroy       = true
    create_before_destroy = false
    ignore_changes        = [engine_version, snapshot_identifier]
  }
}
```

| Argument | Effect |
|---|---|
| `prevent_destroy = true` | Blocks deletion; raises error on destroy |
| `create_before_destroy = true` | Creates replacement before deleting original |
| `ignore_changes = [list]` | Ignores drift on specified attributes |
| `replace_triggered_by` | Forces replacement when referenced resources change |

---

## 4. Variable Type System

| Type | Example Value | Declaration |
|---|---|---|
| `string` | `"us-east-1"` | `type = string` |
| `number` | `3` | `type = number` |
| `bool` | `true` | `type = bool` |
| `list(string)` | `["a","b","c"]` | `type = list(string)` |
| `set(string)` | `["a","b"]` (no duplicates) | `type = set(string)` |
| `map(string)` | `{key = "value"}` | `type = map(string)` |
| `object({...})` | `{name="x",port=80}` | `type = object({name=string,port=number})` |
| `tuple([...])` | `["x",80,true]` | `type = tuple([string,number,bool])` |
| `any` | Accepts any type | `type = any` |

---

## 5. Variable Value Precedence

From lowest to highest priority:

1. Default value declared in the `variable` block.
2. `terraform.tfvars` file in the working directory.
3. `*.auto.tfvars` files (loaded alphabetically).
4. `-var-file="filename.tfvars"` CLI flag.
5. `-var="name=value"` CLI flag.
6. `TF_VAR_<name>` environment variables.

The highest-priority source wins. Knowing this order is directly tested on the exam.

---

## 6. String Interpolation and Expressions

```hcl
locals {
  # String interpolation
  bucket_name = "app-${var.environment}-data"

  # Conditional expression
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"

  # Function call
  name_upper = upper(var.project_name)
}
```

Terraform expressions support:

- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logic: `&&`, `||`, `!`
- Conditional: `condition ? true_val : false_val`
- Function calls: `length(list)`, `merge(map1, map2)`, `toset(list)`
- For expressions: `[for s in var.names : upper(s)]`

---

## 7. Complete Example: AWS Provider + Variable + EC2 Resource

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

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

locals {
  common_tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  tags          = merge(local.common_tags, { Name = "web-${var.environment}" })
}

output "web_public_ip" {
  description = "Public IP of the web instance"
  value       = aws_instance.web.public_ip
}
```

---

## 8. Required Reading

- Read the HCL syntax overview at developer.hashicorp.com/terraform/language/syntax/configuration
- Read the resource blocks reference at developer.hashicorp.com/terraform/language/resources
- Read the variables reference at developer.hashicorp.com/terraform/language/values/variables
- Read the meta-arguments reference at developer.hashicorp.com/terraform/language/meta-arguments/depends_on

---

## 9. Terraform Associate 003 Exam Tips

**Tip 1.** The exam distinguishes between `count` and `for_each`. Use `count` when creating N identical resources. Use `for_each` when each resource needs a unique name derived from the collection key. Changing a `count`-based resource's index causes unintended destroy-and-recreate operations if items are reordered.

**Tip 2.** `prevent_destroy = true` does not survive if you remove the `lifecycle` block from the configuration and run apply. The protection only exists as long as the `lifecycle` block is present.

**Tip 3.** `ignore_changes` takes a list of attribute names without quotes: `ignore_changes = [tags, user_data]`. It does not prevent the resource from being replaced if a non-ignored immutable attribute changes.

**Tip 4.** Provider `alias` is required for multi-region or multi-account deployments within one configuration. The unaliased provider is the default. Resources must explicitly reference aliased providers with `provider = <type>.<alias>`.

**Tip 5.** Variable validation blocks (`validation {}`) run before plan. If a supplied value fails validation, Terraform errors out before querying any provider APIs.

**Tip 6.** `sensitive = true` in a variable or output block only hides values from CLI output. The value is still stored in plain text in the state file unless the backend encrypts state at rest.

**Tip 7.** Know the difference between `local` (computed expression, not overridable) and `variable` (input parameter, overridable). They serve different purposes and the exam tests both.

**Tip 8.** The exam tests the order of variable value precedence. Environment variables (`TF_VAR_*`) have higher priority than `.tfvars` files but lower priority than CLI `-var` flags.

---

## 10. Study Checklist

- [ ] Write a `terraform {}` block with a `required_version` and one `required_providers` entry from memory.
- [ ] Write a `provider "aws" {}` block with a region variable and an aliased second region.
- [ ] Write a `resource "aws_instance"` block using `var.` references for at least two attributes.
- [ ] Write a `variable` block with `type`, `description`, `default`, and a `validation` block.
- [ ] Write an `output` block with `sensitive = true`.
- [ ] Write a `locals` block and reference a local value inside a resource tag.
- [ ] Explain all four resource meta-arguments without notes.
- [ ] Explain the difference between `count` and `for_each`.
- [ ] List variable value precedence from lowest to highest.
- [ ] Complete the Module 03 lab, quiz, and discussion post.

---

Module 03 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
