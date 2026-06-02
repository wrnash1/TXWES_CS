# CIS-4337 Infrastructure Automation

## Module 05: Modules — Creating and Using Reusable Modules

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337. I am Professor Nash. Modules are one of Terraform's most powerful features. They are also one of the most tested topics on the Associate 003 exam.

By the end of this video you will understand what a Terraform module is, why modules exist, how to create a module with the correct file structure, how to call a module from a root configuration, how module inputs and outputs work, and how to use modules from the public Terraform Registry.

We will build a complete VPC module with its own `main.tf`, `variables.tf`, and `outputs.tf`, then call it from a root configuration.

---

## Section 2: What Is a Module — 1:30–4:30

Every Terraform configuration is technically a module. The directory where you run Terraform commands is called the **root module**. Any other configuration directory referenced from the root with a `module` block is a **child module**.

Modules solve the problem of repetition. If you need to create a VPC with a standard set of subnets, route tables, and security groups in multiple environments or multiple regions, you should write that logic once and call it many times with different inputs. That is what modules are for.

Think of a module as a function in a programming language. It has:

- **Input variables** — the parameters the caller passes in.
- **Resources** — the internal implementation.
- **Output values** — what the module returns to the caller.

The caller does not need to know how the module works internally. It only needs to know what inputs to provide and what outputs are available.

---

## Section 3: Module File Structure — 4:30–7:30

The standard structure for a child module looks like this:

**[SHOW CODE]**

```text
modules/
└── vpc/
    ├── main.tf       # Resource declarations
    ├── variables.tf  # Input variable declarations
    ├── outputs.tf    # Output value declarations
    └── README.md     # Documentation (recommended)
```

Let me build each file.

First, `variables.tf` defines what the module accepts:

**[SHOW CODE]**

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
  description = "List of CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}
```

Next, `main.tf` contains the resources:

**[SHOW CODE]**

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

resource "aws_subnet" "public" {
  count             = length(var.public_subnet_cidrs)
  vpc_id            = aws_vpc.this.id
  cidr_block        = var.public_subnet_cidrs[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name        = "${var.environment}-public-${count.index + 1}"
    Environment = var.environment
  }
}

resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id

  tags = {
    Name = "${var.environment}-igw"
  }
}
```

Finally, `outputs.tf` exposes values the caller needs:

**[SHOW CODE]**

```hcl
output "vpc_id" {
  description = "ID of the created VPC"
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

## Section 4: Calling a Module — 7:30–11:00

With the module directory in place, the root configuration calls it with a `module` block.

**[SHOW CODE]**

```hcl
module "network" {
  source = "./modules/vpc"

  vpc_cidr            = "10.1.0.0/16"
  environment         = "prod"
  public_subnet_cidrs = ["10.1.1.0/24", "10.1.2.0/24", "10.1.3.0/24"]
}
```

The `source` argument is the only required argument. For a local module, it is a relative path. For a registry module, it is a registry address.

After adding a new module block, you must run `terraform init` before plan or apply. Terraform downloads the module code into `.terraform/modules/`. This is required even for local path modules — Terraform copies them into the cache during init.

To reference a module's output in the root configuration:

**[SHOW CODE]**

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  subnet_id     = module.network.public_subnet_ids[0]
}

output "vpc_id" {
  value = module.network.vpc_id
}
```

The syntax is `module.<module_name>.<output_name>`.

---

## Section 5: Module Sources — 11:00–14:30

Terraform supports multiple module source types.

**Local paths** reference a directory relative to the calling configuration. The path must begin with `./` or `../`:

**[SHOW CODE]**

```hcl
module "vpc" {
  source = "./modules/vpc"
}
```

**Terraform Registry** sources use a three-part address `<namespace>/<module>/<provider>`:

**[SHOW CODE]**

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

Always pin a version when using registry modules in production. Without a version constraint, Terraform will use the latest version, which can introduce breaking changes.

**Git sources** reference a repository URL:

**[SHOW CODE]**

```hcl
module "vpc" {
  source = "git::https://github.com/myorg/terraform-modules.git//vpc?ref=v1.2.0"
}
```

The `//` separates the repository URL from the subdirectory path within the repo. The `?ref=` parameter pins to a specific tag, branch, or commit.

**Other sources**: GitHub shorthand (`github.com/<org>/<repo>`), Bitbucket, S3, GCS, and HTTP archives are also supported.

---

## Section 6: Module Best Practices — 14:30–17:30

Let me walk through the practices that distinguish well-designed modules from poorly-designed ones.

**One purpose per module.** A module should do one thing well. A VPC module creates networking. An EC2 module creates compute. Avoid modules that do everything — they become impossible to reuse.

**All inputs as variables.** Never hardcode values inside a module that a caller might reasonably want to change. Every configurable value should be a variable with a sensible default.

**Document inputs and outputs.** Every variable and output block should have a `description` argument. This is the primary documentation for module consumers.

**Output everything useful.** If a resource inside the module has an ID or attribute that a calling configuration might need, expose it as an output. Under-output is one of the most common module design mistakes.

**Version-pin registry modules.** Use `version` with a pessimistic constraint (`~> 5.0`) or an exact pin for production. Never use a registry module without a version constraint.

**Use a consistent directory structure.** Every module should have `main.tf`, `variables.tf`, `outputs.tf`, and a `README.md`. Some teams add `versions.tf` for the `terraform {}` block and `locals.tf` for computed values.

---

## Section 7: The Terraform Registry — 17:30–20:00

The public Terraform Registry at registry.terraform.io hosts thousands of community and HashiCorp-maintained modules. The most widely used modules are:

- `terraform-aws-modules/vpc/aws` — AWS VPC with all standard components
- `terraform-aws-modules/eks/aws` — Amazon Elastic Kubernetes Service
- `terraform-aws-modules/rds/aws` — Amazon RDS with parameter groups and subnet groups
- `terraform-google-modules/network/google` — Google Cloud VPC

When you view a module in the registry, you see the required inputs, optional inputs with defaults, and outputs. The "Provision Instructions" tab shows you the exact `module` block to add to your configuration.

Verified modules display a verification badge. These are maintained by the technology partner (HashiCorp, AWS, Google, etc.) and have passed a quality review.

---

## Section 8: Closing — 20:00–21:00

Let me recap.

A module is a reusable directory of Terraform configuration. The root module is where you run Terraform. Child modules are called via `module` blocks.

The standard module structure has three files: `main.tf`, `variables.tf`, and `outputs.tf`. Inputs flow in through variables. Outputs flow out through output blocks. Module outputs are referenced as `module.<name>.<output>`.

Always run `terraform init` after adding or changing a module source. Pin versions for registry modules.

In Module 06 we cover data sources and Terraform built-in functions. Complete the reading guide, lab, quiz, and discussion first.

See you in Module 06.

---

End of Script — Module 05
