# CIS-4337 Infrastructure Automation

## Reading Guide — Module 05: Modules — Creating and Using Reusable Modules

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

Modules are the primary mechanism for code reuse in Terraform. This module covers module structure, module calls, input and output flow, source types, and registry usage. These topics appear throughout the Terraform Associate 003 exam.

---

## 1. Core Vocabulary

**Root Module**
The configuration directory where you run Terraform commands. Every Terraform project has exactly one root module per working directory.

**Child Module**
A configuration directory called from the root module (or another child module) via a `module` block. Child modules encapsulate infrastructure logic and expose an interface through variables and outputs.

**Module Source**
The `source` argument in a `module` block that tells Terraform where to find the module code. Can be a local path, registry address, Git URL, or other supported source type.

**module Block**
The HCL block in a calling configuration that invokes a child module. The `source` argument is the only required argument.

**Module Input Variable**
A `variable` block declared inside a module that defines the parameters the caller must or may supply. These are the module's public interface for inputs.

**Module Output Value**
An `output` block declared inside a module that exposes a computed value to the caller. Referenced in the calling configuration as `module.<name>.<output_name>`.

**Terraform Registry**
The public module and provider registry at registry.terraform.io. Hosts community and HashiCorp-verified modules for all major cloud providers.

**Verified Module**
A registry module that has passed a quality review by the technology partner. Displayed with a verification badge.

**Module Composition**
The practice of calling multiple modules from the root (or from each other) to compose complex infrastructure from smaller, focused components.

---

## 2. Standard Module File Structure

```text
modules/
└── vpc/
    ├── main.tf        # Resource declarations
    ├── variables.tf   # Input variable declarations
    ├── outputs.tf     # Output value declarations
    ├── versions.tf    # terraform{} block (optional but recommended)
    └── README.md      # Usage documentation
```

The root configuration that calls the module:

```text
project/
├── main.tf            # module blocks and root resources
├── variables.tf       # root-level variables
├── outputs.tf         # root-level outputs
├── terraform.tfvars   # variable values
└── modules/
    └── vpc/           # child module
```

---

## 3. Complete VPC Module Example

### modules/vpc/variables.tf

```hcl
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
  default     = ["10.0.11.0/24", "10.0.12.0/24"]
}
```

### modules/vpc/main.tf

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
    Name = "${var.environment}-public-${count.index + 1}"
  }
}

resource "aws_subnet" "private" {
  count      = length(var.private_subnet_cidrs)
  vpc_id     = aws_vpc.this.id
  cidr_block = var.private_subnet_cidrs[count.index]

  tags = {
    Name = "${var.environment}-private-${count.index + 1}"
  }
}
```

### modules/vpc/outputs.tf

```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.this.id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value       = aws_subnet.private[*].id
}

output "internet_gateway_id" {
  description = "ID of the internet gateway"
  value       = aws_internet_gateway.this.id
}
```

---

## 4. Calling the VPC Module from Root

```hcl
module "network" {
  source = "./modules/vpc"

  vpc_cidr             = "10.1.0.0/16"
  environment          = var.environment
  public_subnet_cidrs  = ["10.1.1.0/24", "10.1.2.0/24"]
  private_subnet_cidrs = ["10.1.11.0/24", "10.1.12.0/24"]
}

# Using module outputs in another resource
resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  subnet_id     = module.network.public_subnet_ids[0]

  tags = {
    Name = "app-server"
  }
}

# Exposing module output at root level
output "vpc_id" {
  description = "VPC ID from the network module"
  value       = module.network.vpc_id
}
```

---

## 5. Module Source Types

| Source Type | Example | Version Argument |
|---|---|---|
| Local path | `source = "./modules/vpc"` | Not supported |
| Terraform Registry | `source = "terraform-aws-modules/vpc/aws"` | Required for production |
| GitHub shorthand | `source = "github.com/org/repo"` | Use `?ref=tag` |
| Git HTTPS | `source = "git::https://github.com/org/repo.git//subdir"` | Use `?ref=tag` |
| S3 bucket | `source = "s3::https://bucket.s3.amazonaws.com/module.zip"` | Not supported |

---

## 6. Registry Module Call Syntax

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}
```

Registry modules use a three-part address: `<NAMESPACE>/<MODULE>/<PROVIDER>`.

---

## 7. Module Workflow

After adding or modifying a `module` block in your configuration:

1. Run `terraform init` — downloads module code into `.terraform/modules/`.
2. Run `terraform plan` — shows all resources the module will create.
3. Run `terraform apply` — creates resources in the correct dependency order.

Module resources appear in state with addresses like `module.network.aws_vpc.this`. They are managed exactly like root-level resources.

---

## 8. Required Reading

- Read the modules overview at developer.hashicorp.com/terraform/language/modules
- Read the module sources reference at developer.hashicorp.com/terraform/language/modules/sources
- Read the module composition guide at developer.hashicorp.com/terraform/language/modules/develop/composition
- Browse the public module registry at registry.terraform.io

---

## 9. Terraform Associate 003 Exam Tips

**Tip 1.** The only required argument in a `module` block is `source`. All other arguments are optional or are variable inputs.

**Tip 2.** `terraform init` must be run after adding or changing a `module` block. Without it, Terraform errors with "module not installed."

**Tip 3.** Module outputs are referenced as `module.<name>.<output_name>`. The exam tests this syntax. Do not confuse it with `var.<name>` (variable) or `local.<name>` (local value).

**Tip 4.** Local path sources start with `./` or `../`. Registry sources use a three-part address. The `version` argument is only valid for registry and Git sources — it is invalid for local paths.

**Tip 5.** A module resource's state address includes the module path: `module.network.aws_vpc.this`. When using `terraform state` commands, always use the full module-qualified address.

**Tip 6.** Modules do not have separate state files. All resources across all modules in a configuration are tracked in the same `terraform.tfstate` file.

**Tip 7.** When a calling module passes a `providers` argument to a child module, it overrides the default provider for that module. This is used for multi-account deployments.

**Tip 8.** Published registry modules expose a `version` constraint. The `~> 5.0` pessimistic constraint allows any 5.x version. The exam tests version constraint interpretation.

---

## 10. Study Checklist

- [ ] Describe the difference between root module and child module.
- [ ] Write a module directory with `main.tf`, `variables.tf`, and `outputs.tf` from memory.
- [ ] Write a `module` block calling a local path module with variable inputs.
- [ ] Write a `module` block calling a registry module with a version constraint.
- [ ] Explain the reference syntax for accessing a module output.
- [ ] List the five module source types and when each is appropriate.
- [ ] Explain why `terraform init` is required after adding a module block.
- [ ] Read all four required documentation pages.
- [ ] Complete the Module 05 lab, quiz, and discussion post.

---

## 11. Supplemental Resources

**1. Terraform Modules Overview**
<https://developer.hashicorp.com/terraform/language/modules>
The primary documentation for writing, calling, and publishing Terraform modules. Covers child module structure, the `module` block syntax, output references, and provider inheritance.

**2. Terraform Module Sources Reference**
<https://developer.hashicorp.com/terraform/language/modules/sources>
Documents all supported module source types: local paths, Terraform Registry, GitHub, Bitbucket, S3, and more. Includes the correct syntax for each and the rules around the `version` argument.

**3. Terraform Registry Module Browser**
<https://registry.terraform.io/browse/modules>
The public module registry. Browse community and verified modules for AWS, Azure, GCP, and other providers. Each module page displays inputs, outputs, version history, and usage examples — the same format you will encounter on the Terraform Associate exam.

---

Module 05 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
