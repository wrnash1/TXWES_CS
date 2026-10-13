# Video Script: Module 09 — Terraform Modules

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Introduction (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 09 of CIS-4337, Infrastructure Automation.

In the previous two modules you mastered variables and state. Now we take the next big step: **Terraform modules**. Modules are the primary mechanism for organizing, reusing, and sharing Terraform code. They are to Terraform what functions and libraries are to general-purpose programming languages.

By the end of this module you will be able to:

- Explain the difference between the root module and child modules
- Create a reusable module with inputs and outputs
- Call modules from local directories, the Terraform Registry, and Git repositories
- Apply module versioning best practices
- Compose larger infrastructure from multiple modules

Let's get started.

[PAUSE]

---

## Section 1: What Is a Module (1:30 – 4:00)

In Terraform, every directory that contains `.tf` files is a module. When you run `terraform apply` in a directory, you are running the **root module** — the entry point for your configuration.

A **child module** is any module that is called by another module using a `module` block. The calling module is the **parent**.

Here is the simplest possible module call:

```hcl
module "network" {
  source = "./modules/network"
}
```

This tells Terraform: go into the `./modules/network` directory, process all the `.tf` files there, and treat them as a reusable component.

[PAUSE]

### Module Structure

A well-organized module typically has three files:

- `main.tf` — resource definitions
- `variables.tf` — input variable declarations
- `outputs.tf` — output value declarations

These are conventions, not requirements. All `.tf` files in a directory are loaded together regardless of their names.

```
modules/
  network/
    main.tf
    variables.tf
    outputs.tf
    README.md
```

A good module is like a well-designed function: it has a clear interface (inputs and outputs), does one thing well, and hides its implementation details.

[PAUSE]

---

## Section 2: Module Sources (4:00 – 8:00)

The `source` argument in a `module` block tells Terraform where to find the module code. There are five source types you need to know.

### Local Paths

```hcl
module "network" {
  source = "./modules/network"
}

module "shared_compute" {
  source = "../shared/compute"
}
```

Local paths always start with `./` or `../`. This is the most common source type during development.

[PAUSE]

### Terraform Registry

The public Terraform Registry at `registry.terraform.io` hosts thousands of community and verified modules.

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

The Registry source format is `<namespace>/<module>/<provider>`. The version constraint uses the same syntax as provider versions — we will cover this in a moment.

[PAUSE]

### Git Repositories

You can source a module directly from a Git repository:

```hcl
module "network" {
  source = "git::https://github.com/acme/terraform-modules.git//network"
}

# With a specific tag or branch
module "network" {
  source = "git::https://github.com/acme/terraform-modules.git//network?ref=v2.1.0"
}
```

The `//` double-slash separates the repository URL from the subdirectory path within the repo. The `?ref=` query parameter pins to a tag, branch, or commit hash.

[PAUSE]

### Other Sources

- **GitHub shorthand**: `source = "github.com/acme/terraform-modules//network"`
- **Bitbucket**: `source = "bitbucket.org/acme/terraform-modules//network"`
- **S3 bucket**: `source = "s3::https://s3.amazonaws.com/bucket/module.zip"`
- **HTTP URL**: `source = "https://example.com/modules/network.zip"`

[PAUSE]

---

## Section 3: Module Versioning (8:00 – 10:30)

When using the Terraform Registry or Git sources, you should always pin to a specific version. Unpinned modules will pull the latest version on every `terraform init`, which can introduce breaking changes.

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.1.2"      # exact version
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"    # >= 19.0, < 20.0 (compatible within major)
}

module "rds" {
  source  = "terraform-aws-modules/rds/aws"
  version = ">= 5.0, < 6.0"  # explicit range
}
```

[SHOW TERMINAL]

Version constraint operators:

- `= 1.0.0` — exact version only
- `!= 1.0.0` — exclude this version
- `> 1.0.0` — greater than
- `>= 1.0.0` — greater than or equal
- `< 2.0.0` — less than
- `~> 1.0` — compatible: >= 1.0, < 2.0
- `~> 1.0.0` — compatible: >= 1.0.0, < 1.1.0

The `~>` operator is the most commonly used in practice. It allows patch and minor updates within a major version, preventing breaking changes while allowing security fixes to flow through.

[PAUSE]

---

## Section 4: Module Inputs and Outputs (10:30 – 14:00)

The interface of a module is defined by its variable declarations (inputs) and output declarations (outputs).

### Module Inputs

In the child module's `variables.tf`:

```hcl
variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "environment" {
  type        = string
  description = "Deployment environment"
}

variable "availability_zones" {
  type        = list(string)
  description = "Availability zones to create subnets in"
}
```

In the parent module that calls it:

```hcl
module "network" {
  source = "./modules/network"

  vpc_cidr           = "10.10.0.0/16"
  environment        = var.environment
  availability_zones = ["us-east-1a", "us-east-1b"]
}
```

Notice that the parent passes values for the module's variables as arguments inside the `module` block.

[PAUSE]

### Module Outputs

In the child module's `outputs.tf`:

```hcl
output "vpc_id" {
  description = "The VPC ID"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = aws_subnet.public[*].id
}
```

In the parent module, consume them with `module.<name>.<output>`:

```hcl
resource "aws_instance" "app" {
  ami       = data.aws_ami.ubuntu.id
  subnet_id = module.network.private_subnet_ids[0]
}

output "vpc_id" {
  value = module.network.vpc_id
}
```

[PAUSE]

---

## Section 5: Module Composition (14:00 – 17:30)

Real-world Terraform configurations compose multiple modules together. This is where the power of modules becomes apparent.

[SHOW TERMINAL]

Here is a realistic root module that composes network, compute, and database modules:

```hcl
# root main.tf

module "network" {
  source = "./modules/network"

  environment        = var.environment
  vpc_cidr           = "10.0.0.0/16"
  availability_zones = data.aws_availability_zones.available.names
}

module "compute" {
  source = "./modules/compute"

  environment      = var.environment
  vpc_id           = module.network.vpc_id
  subnet_ids       = module.network.private_subnet_ids
  instance_type    = var.instance_type
}

module "database" {
  source = "./modules/database"

  environment     = var.environment
  vpc_id          = module.network.vpc_id
  subnet_ids      = module.network.private_subnet_ids
  app_sg_id       = module.compute.app_security_group_id
  db_password     = var.db_password
}
```

Notice how `module.network.vpc_id` flows into both `module.compute` and `module.database`. Terraform understands this dependency and will create the network resources before compute and database resources.

[PAUSE]

### Module Meta-Arguments

Module blocks support several meta-arguments:

- **`count`** — create multiple instances of a module
- **`for_each`** — create a module instance for each item in a map or set
- **`depends_on`** — explicit dependency when implicit ones are insufficient
- **`providers`** — pass specific provider configurations to a module

```hcl
module "per_region_network" {
  for_each = toset(["us-east-1", "us-west-2", "eu-west-1"])
  source   = "./modules/network"

  region      = each.value
  environment = var.environment
}
```

[PAUSE]

---

## Section 6: The Terraform Registry (17:30 – 20:00)

The public Terraform Registry at `registry.terraform.io` is the central repository for community and partner modules. Understanding how to use it is essential both for real-world work and for the exam.

[SHOW TERMINAL]

A Registry module URL looks like this: `registry.terraform.io/<NAMESPACE>/<MODULE>/<PROVIDER>`

For example:

- `terraform-aws-modules/vpc/aws` — The most popular AWS VPC module, maintained by the community
- `hashicorp/consul/aws` — HashiCorp's official Consul module for AWS
- `Azure/network/azurerm` — Microsoft's Azure network module

On the Registry website you will find:

- Module documentation (README)
- Input variable reference
- Output reference
- Version history
- Source code link
- Verified badge (for modules that pass HashiCorp's verification process)

[PAUSE]

### Creating a Publishable Module

To publish a module to the Registry, the GitHub repository must follow a specific naming convention: `terraform-<PROVIDER>-<MODULE>`. For example:

- `terraform-aws-vpc`
- `terraform-azurerm-network`
- `terraform-google-gke`

The module must also have a `README.md`, follow the standard file structure (`main.tf`, `variables.tf`, `outputs.tf`), and use semantic versioning via Git tags.

[PAUSE]

---

## Summary and Exam Tips (20:00 – 22:30)

Here is what we covered in Module 09:

- Every Terraform directory is a module; the entry point is the root module
- Child modules are called with `module` blocks and a `source` argument
- Source types: local paths, Terraform Registry, Git repos, GitHub/Bitbucket shorthand
- Always pin module versions in production; use `~>` for compatible releases
- Module inputs are variable arguments in the `module` block; outputs are accessed via `module.<name>.<output>`
- Modules compose by passing outputs of one module as inputs to another
- The Registry naming convention is `<namespace>/<module>/<provider>`

**For the Terraform Associate exam**, pay attention to:

- `terraform init` downloads modules from remote sources; local modules are used directly
- `terraform get` also downloads modules but does not re-download providers
- The `//` syntax in Git sources separates the repo URL from the subdirectory
- `module.<name>.<output>` is the correct reference syntax — no `var.` prefix
- Version constraints: know the meaning of `~>`, `>=`, and `!=`

[PAUSE]

---

## Closing (22:30 – 23:30)

Modules transform Terraform from a configuration language into an infrastructure programming system. Once you start thinking in modules, you stop copying and pasting resource blocks and start building reusable, testable components.

In the lab you will build two reusable modules and compose them from a root module. This is the closest lab to real-world Terraform work we have done so far.

Module 10 covers Terraform Workspaces — a mechanism for managing multiple environments from a single configuration.

See you there.

[END OF SCRIPT]
