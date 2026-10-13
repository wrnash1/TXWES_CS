# CIS-4337 Infrastructure Automation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4337 &BULL; INFRASTRUCTURE AUTOMATION & CONFIGURATION MANAGEMENT</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

## 11. Supplemental Resources

**1. Terraform Resource Blocks Reference**
<https://developer.hashicorp.com/terraform/language/resources/syntax>
Complete reference for resource block syntax, meta-arguments (`count`, `for_each`, `depends_on`, `lifecycle`, `provider`), and resource addressing. Essential for Module 03 lab exercises involving `count` vs `for_each`.

**2. Terraform Input Variables Reference**
<https://developer.hashicorp.com/terraform/language/values/variables>
Covers all variable block arguments, type constraints, validation blocks, sensitive values, and the full variable value precedence order. Maps directly to exam questions on variable assignment priority.

**3. Terraform Local Values Reference**
<https://developer.hashicorp.com/terraform/language/values/locals>
Explains when to use `locals` versus `variables`, how to compose local expressions, and best practices for avoiding over-use of locals that reduces configuration readability.

---

Module 03 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
