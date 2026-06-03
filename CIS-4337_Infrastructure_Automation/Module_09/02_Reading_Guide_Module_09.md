# Reading Guide: Module 09 — Terraform Modules

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Learning Objectives

After completing this reading guide you will be able to:

- Distinguish between root modules and child modules
- Call modules from all supported source types
- Apply version constraints to registry and Git-sourced modules
- Design clear module interfaces using variables and outputs
- Compose infrastructure from multiple modules
- Navigate and consume the Terraform Registry effectively

---

## 1. Module Fundamentals

### 1.1 Every Directory Is a Module

In Terraform, any directory containing at least one `.tf` file is a module. When you run Terraform commands in a directory, you are operating on the **root module**. Any module called by the root module (or by another module) is a **child module**.

The root module is the entry point. Child modules are reusable components.

### 1.2 Standard Module Structure

The conventional structure for a Terraform module:

```
module-name/
  main.tf        # Resource and data source definitions
  variables.tf   # Input variable declarations
  outputs.tf     # Output value declarations
  versions.tf    # Terraform and provider version constraints
  README.md      # Module documentation
```

These file names are conventions enforced by the Terraform Registry publication requirements. Terraform itself will load any `.tf` file regardless of name.

### 1.3 The Module Block

A parent module calls a child module using a `module` block:

```hcl
module "network" {
  source  = "./modules/network"
  version = "~> 2.0"

  # Module input variables
  environment = var.environment
  vpc_cidr    = "10.0.0.0/16"
}
```

Required arguments:

- `source` — where to find the module (required for all module blocks)

Optional arguments that are part of the module interface:

- `version` — version constraint (only for registry and registry-compatible sources)
- Any declared variable of the child module (e.g., `environment`, `vpc_cidr` above)

Meta-arguments supported by all module blocks:

- `count` — create multiple instances
- `for_each` — create an instance per map or set element
- `depends_on` — explicit dependency declaration
- `providers` — pass specific provider aliases

---

## 2. Module Sources

### 2.1 Local Paths

```hcl
module "vpc" {
  source = "./modules/vpc"
}

module "shared" {
  source = "../../shared/modules/logging"
}
```

Local paths must begin with `./` or `../`. Local modules are loaded directly from the filesystem; `terraform init` does not download them.

### 2.2 Terraform Registry

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

Format: `<NAMESPACE>/<MODULE>/<PROVIDER>`

- `NAMESPACE` — the organization or user on the Registry
- `MODULE` — the module name
- `PROVIDER` — the primary provider the module targets

### 2.3 Git Sources

```hcl
# HTTPS URL
module "vpc" {
  source = "git::https://github.com/acme/terraform-modules.git//modules/vpc"
}

# SSH URL
module "vpc" {
  source = "git::git@github.com:acme/terraform-modules.git//modules/vpc"
}

# Pin to a tag
module "vpc" {
  source = "git::https://github.com/acme/terraform-modules.git//modules/vpc?ref=v2.1.0"
}

# Pin to a commit hash
module "vpc" {
  source = "git::https://github.com/acme/terraform-modules.git//modules/vpc?ref=abc123f"
}
```

The `//` double-slash separator is important: it separates the repository root from the subdirectory containing the module. Without it, Terraform uses the repository root as the module.

### 2.4 GitHub and Bitbucket Shorthand

```hcl
module "vpc" {
  source = "github.com/acme/terraform-modules//modules/vpc"
}

module "vpc" {
  source = "bitbucket.org/acme/terraform-modules//modules/vpc"
}
```

These are shorthand for the full `git::https://` form.

### 2.5 Other Sources

| Source type | Example |
|---|---|
| S3 bucket | `s3::https://s3.amazonaws.com/my-bucket/module.zip` |
| GCS bucket | `gcs::https://www.googleapis.com/storage/v1/my-bucket/module.zip` |
| HTTP/HTTPS archive | `https://example.com/modules/vpc.zip` |

---

## 3. Module Versioning

### 3.1 Why Version Constraints Matter

Unpinned modules will fetch the latest available version on every `terraform init`. A new major version of a module may introduce breaking changes to input variable names, types, or resource structures — causing your next plan to propose destructive changes without any configuration changes on your part.

### 3.2 Version Constraint Syntax

| Constraint | Meaning |
|---|---|
| `= 5.1.2` | Exactly version 5.1.2 |
| `!= 5.0.0` | Any version except 5.0.0 |
| `>= 5.0` | Version 5.0 or higher |
| `< 6.0` | Any version below 6.0 |
| `~> 5.0` | >= 5.0.0, < 6.0.0 |
| `~> 5.1` | >= 5.1.0, < 6.0.0 |
| `~> 5.1.2` | >= 5.1.2, < 5.2.0 |

The pessimistic constraint operator `~>` is the most widely used. `~> 5.1` allows updates within the 5.x minor series. `~> 5.1.2` allows patch updates only.

### 3.3 Module Lock File

Terraform records the selected module versions in `.terraform.lock.hcl`. This file should be committed to version control to ensure consistent module versions across the team.

---

## 4. Module Inputs and Outputs

### 4.1 Designing the Input Interface

```hcl
# modules/network/variables.tf

variable "environment" {
  type        = string
  description = "Deployment environment (dev, staging, prod)"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging, or prod."
  }
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_count" {
  type        = number
  description = "Number of public subnets to create"
  default     = 2
}

variable "tags" {
  type        = map(string)
  description = "Additional tags for all resources"
  default     = {}
}
```

### 4.2 Designing the Output Interface

```hcl
# modules/network/outputs.tf

output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}
```

### 4.3 Calling the Module

```hcl
# root main.tf

module "network" {
  source = "./modules/network"

  environment         = var.environment
  vpc_cidr            = "10.10.0.0/16"
  public_subnet_count = 3
  tags = {
    Project = "ecommerce"
  }
}

# Consuming outputs
resource "aws_instance" "app" {
  subnet_id = module.network.private_subnet_ids[0]
}
```

---

## 5. Module Composition

### 5.1 Passing Module Outputs as Inputs

The primary pattern for composing modules is passing one module's outputs as another module's inputs:

```hcl
module "network" {
  source      = "./modules/network"
  environment = var.environment
}

module "compute" {
  source = "./modules/compute"

  environment = var.environment
  vpc_id      = module.network.vpc_id
  subnet_ids  = module.network.private_subnet_ids
}

module "database" {
  source = "./modules/database"

  environment = var.environment
  vpc_id      = module.network.vpc_id
  subnet_ids  = module.network.private_subnet_ids
  app_sg_id   = module.compute.security_group_id
}
```

Terraform builds the dependency graph automatically from these references: `network` is created first, then `compute` and `database` in parallel (since they both depend on `network` but not on each other).

### 5.2 count and for_each with Modules

```hcl
# Create one network module per environment
module "env_network" {
  for_each = toset(["dev", "staging", "prod"])
  source   = "./modules/network"

  environment = each.key
  vpc_cidr    = "10.${index(["dev", "staging", "prod"], each.key)}.0.0/16"
}

# Access outputs from for_each modules
output "all_vpc_ids" {
  value = { for env, mod in module.env_network : env => mod.vpc_id }
}
```

---

## 6. The Terraform Registry

### 6.1 Registry URL Structure

The public Terraform Registry is at `registry.terraform.io`. A module page URL follows this pattern:

`registry.terraform.io/modules/<namespace>/<module>/<provider>`

### 6.2 Verified vs. Community Modules

- **Verified modules** display a blue verified badge. They are maintained by technology partners (AWS, Microsoft, Google, HashiCorp) and meet quality standards.
- **Community modules** are published by the broader Terraform community. Review source code and version history before use in production.

### 6.3 Module Repository Naming Convention

For a module to be published to the public Registry, its GitHub repository must be named:

`terraform-<PROVIDER>-<MODULE_NAME>`

Examples:

- `terraform-aws-vpc`
- `terraform-azurerm-network`
- `terraform-google-kubernetes-engine`

### 6.4 terraform init and terraform get

```bash
# Initialize and download all modules and providers
terraform init

# Download modules only (no provider updates)
terraform get

# Download modules and update to latest matching versions
terraform get -update
```

---

## 7. Command Reference

| Command | Description |
|---|---|
| `terraform init` | Download and install modules and providers |
| `terraform get` | Download modules without updating providers |
| `terraform get -update` | Download and update modules to latest matching version |
| `terraform validate` | Check configuration syntax including module calls |
| `terraform graph` | Output dependency graph including module edges |

---

## 8. Exam Tips — Terraform Associate 003

1. **`terraform init` is required after adding new modules**: Terraform must download module code before it can plan or apply.

2. **Local modules are not downloaded**: Local path modules (`./` or `../`) are read from disk; `terraform init` does not copy them.

3. **The `//` separator in Git sources**: Separates the repository URL from the subdirectory path. Missing `//` means Terraform looks at the repository root.

4. **`module.<name>.<output>`**: The correct syntax for accessing child module outputs.

5. **`version` is only valid for registry sources**: You cannot use `version` with local path or generic Git URL sources.

6. **Module meta-arguments**: `count`, `for_each`, `depends_on`, and `providers` work the same as on resources but apply to entire module instances.

7. **Registry naming convention**: `terraform-<provider>-<name>` is required for publication; the reference in code is `<namespace>/<name>/<provider>`.

8. **Module hiding**: A child module cannot access the parent module's resources directly; communication is only through inputs (variables) and outputs.

---

## 9. Summary

Modules are the packaging and reuse mechanism for Terraform. A good module encapsulates a set of related resources, exposes a clear interface through variables and outputs, and hides implementation details from callers.

The ability to source modules from local paths, the Terraform Registry, and Git repositories enables teams to build internal module libraries and consume vetted public modules — both critical skills in production Terraform work.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
