# Reading Guide: Module 16 — Terraform Associate 003 Exam Preparation and Capstone

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Overview

This reading guide is a comprehensive review of all nine Terraform Associate 003 exam objective domains. Use it as a study reference in the final weeks before your exam. Every section maps directly to an official exam objective. Concepts that appear most frequently on the exam are marked with the notation [HIGH FREQUENCY].

**Estimated reading time:** 90–120 minutes

---

## Domain 1: Understand Infrastructure as Code (IaC) Concepts

### 1.1 What IaC Is

Infrastructure as Code is the management of infrastructure — servers, networks, databases, load balancers — through version-controlled configuration files rather than through manual processes or interactive tools.

### 1.2 Benefits of IaC [HIGH FREQUENCY]

- **Automation**: reduces human error and eliminates manual steps
- **Consistency**: every environment is provisioned identically from the same code
- **Repeatability**: the same configuration deployed multiple times produces the same result
- **Version history**: infrastructure changes are tracked in git with author, timestamp, and rationale
- **Collaboration**: infrastructure changes go through code review
- **Documentation**: the configuration is self-documenting

### 1.3 Declarative vs. Imperative IaC [HIGH FREQUENCY]

Terraform is declarative — you define the desired end state and Terraform determines the steps to achieve it. You do not write `create_vpc()`, `create_subnet()`, `create_route_table()` in sequence. You declare `resource "aws_vpc"`, `resource "aws_subnet"`, `resource "aws_route_table"` and Terraform handles ordering.

Imperative tools like shell scripts or Ansible in procedural mode require you to specify each step. The operator manages ordering and idempotency manually.

### 1.4 Idempotency [HIGH FREQUENCY]

An operation is idempotent if applying it multiple times produces the same result as applying it once. `terraform apply` is idempotent — applying a configuration with no changes produces no changes. This is a core property of declarative IaC.

---

## Domain 2: Understand the Purpose of Terraform

### 2.1 Terraform vs. Other Tools [HIGH FREQUENCY]

| Tool | Type | Scope |
|------|------|-------|
| Terraform | Declarative IaC | Infrastructure provisioning (cloud, SaaS, network) |
| Ansible | Imperative/Declarative | Configuration management and some provisioning |
| Chef/Puppet | Declarative | Configuration management of server software |
| CloudFormation | Declarative IaC | AWS only |
| Pulumi | Imperative IaC (code) | Infrastructure provisioning (multi-cloud) |

### 2.2 Terraform's Multi-Provider Advantage

Terraform's provider ecosystem includes thousands of integrations. A single Terraform configuration can provision AWS VPCs, Azure DNS zones, Cloudflare CDN rules, PagerDuty escalation policies, and GitHub repository settings in one `terraform apply`.

### 2.3 The Role of State

Terraform uses state to track which resources it manages and their current attribute values. Without state, Terraform cannot calculate what needs to change. The state enables Terraform to:

- Detect resources that exist in the cloud but not in the configuration (candidates for deletion)
- Detect configuration changes that need to be applied to existing resources
- Provide dependency information for plan ordering

---

## Domain 3: Understand Terraform Basics

### 3.1 HCL Syntax

Terraform uses HashiCorp Configuration Language. Key syntax rules:

- Strings use double quotes: `"value"`
- Numbers are unquoted: `count = 3`
- Booleans are unquoted: `enabled = true`
- Heredoc strings use `<<EOF ... EOF` syntax
- Comments: `#`, `//` for single-line; `/* ... */` for multi-line

### 3.2 Resource Block [HIGH FREQUENCY]

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0abc123"
  instance_type = "t3.micro"
}
```

The resource type is `aws_instance`. The local name is `web`. Together they form the resource address `aws_instance.web`.

### 3.3 Data Source Block [HIGH FREQUENCY]

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-22.04-amd64-server-*"]
  }
}
```

Referenced as `data.aws_ami.ubuntu.id`. Data sources are read-only — they query existing infrastructure.

### 3.4 Variable Types [HIGH FREQUENCY]

- `string`: text value
- `number`: integer or float
- `bool`: true or false
- `list(type)`: ordered sequence, allows duplicates
- `set(type)`: unordered, no duplicates
- `map(type)`: key-value pairs, all values same type
- `object({attr = type})`: structured record with named attributes of different types
- `tuple([type, type])`: fixed-length sequence of mixed types
- `any`: accepts any type (use sparingly)

### 3.5 Functions [HIGH FREQUENCY]

Know these functions for the exam:

- `length(collection)` — count of elements
- `toset(list)` — convert list to set (deduplicates)
- `tolist(set)` — convert set to list
- `merge(map1, map2)` — combine maps, later maps override earlier
- `lookup(map, key, default)` — retrieve map value with default
- `contains(list, value)` — true if value is in list
- `flatten(list_of_lists)` — produce single flat list
- `zipmap(keys, values)` — create map from two lists
- `format(format_string, args...)` — string formatting
- `join(separator, list)` — join list elements into string
- `split(separator, string)` — split string into list
- `element(list, index)` — retrieve element by index (wraps around)
- `coalesce(val1, val2, ...)` — returns first non-null, non-empty value

---

## Domain 4: Use Terraform Outside of Core Workflow

### 4.1 terraform taint and untaint [HIGH FREQUENCY]

`terraform taint <resource_address>` marks a resource for forced replacement on the next apply. The resource is destroyed and recreated. Useful when a resource is in a bad state that Terraform cannot automatically correct.

`terraform untaint <resource_address>` removes the taint mark.

Note: In Terraform 1.0+, the preferred approach for forcing replacement is `terraform apply -replace=<resource_address>` rather than the two-step taint/apply process.

### 4.2 terraform import

Brings existing resources under Terraform management. The `terraform import` CLI command requires an existing resource block. The Terraform 1.5+ `import` block integrates import into the plan/apply cycle.

### 4.3 terraform state Subcommands

- `terraform state list` — list all resources in state
- `terraform state show <address>` — show all attributes of a specific resource
- `terraform state mv <source> <dest>` — move or rename resource in state
- `terraform state rm <address>` — remove resource from state without destroying it
- `terraform state pull` — download current remote state
- `terraform state push` — upload local state to remote backend (use with caution)

### 4.4 terraform workspace

Workspaces allow multiple state files from the same backend and configuration. Commands:

- `terraform workspace new <name>` — create a new workspace
- `terraform workspace select <name>` — switch to a workspace
- `terraform workspace list` — list all workspaces
- `terraform workspace show` — display current workspace name
- `terraform workspace delete <name>` — delete a workspace (must not be active)

Inside configuration, `terraform.workspace` is a string containing the current workspace name. This allows environment-specific configuration: `instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"`.

---

## Domain 5: Interact with Terraform Modules

### 5.1 Module Structure [HIGH FREQUENCY]

Standard published module structure:

```text
module-name/
  main.tf        (required)
  variables.tf   (required)
  outputs.tf     (required)
  README.md      (required for Registry)
  versions.tf    (recommended)
  examples/      (recommended)
    basic/
      main.tf
```

### 5.2 Module Sources [HIGH FREQUENCY]

- Local path: `source = "./modules/vpc"`
- Terraform Registry: `source = "hashicorp/consul/aws"` (namespace/module/provider)
- GitHub: `source = "github.com/hashicorp/example"`
- S3 archive: `source = "s3::https://s3.amazonaws.com/bucket/module.zip"`
- Generic HTTPS: `source = "https://example.com/module.zip"`

### 5.3 Module Versioning

When sourcing from the Terraform Registry or git, specify a version:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

Version constraints follow the same rules as provider version constraints.

### 5.4 Module Inputs and Outputs [HIGH FREQUENCY]

Inputs are variables in the child module. In the module block, you set them as arguments:

```hcl
module "my_module" {
  source    = "./modules/my_module"
  input_var = "value"
}
```

Outputs from the module are accessed as `module.my_module.output_name`.

---

## Domain 6: Navigate Terraform Workflow

### 6.1 CLI Commands and Flags [HIGH FREQUENCY]

Know every flag for every core command. The most tested:

`terraform init`:

- `-backend=false` — skip backend initialization (local state only)
- `-upgrade` — update provider versions to newest satisfying constraints
- `-reconfigure` — reconfigure backend without using existing state

`terraform plan`:

- `-out=FILE` — save plan to file
- `-var="key=val"` — set a variable
- `-var-file=FILE` — load variables from a file
- `-target=RESOURCE` — plan only a specific resource
- `-destroy` — plan a destroy
- `-refresh-only` — plan to update state without changes
- `-detailed-exitcode` — exit 0=no changes, 1=error, 2=changes

`terraform apply`:

- `-auto-approve` — skip interactive confirmation
- `PLANFILE` — apply a saved plan file
- `-replace=RESOURCE` — force replacement of a specific resource

`terraform destroy`:

- `-auto-approve` — skip confirmation
- `-target=RESOURCE` — destroy only a specific resource

### 6.2 Variable Precedence [HIGH FREQUENCY]

From lowest to highest precedence:

1. Default value in variable declaration
2. `terraform.tfvars` file (auto-loaded)
3. `terraform.tfvars.json` file (auto-loaded)
4. `*.auto.tfvars` files (auto-loaded, alphabetical order)
5. `-var-file` flag
6. `-var` flag
7. `TF_VAR_<name>` environment variable

Higher-precedence sources override lower-precedence sources for the same variable.

---

## Domain 7: Implement and Maintain State

### 7.1 State File Contents [HIGH FREQUENCY]

The state file (`terraform.tfstate`) contains:

- Terraform version
- Serial number (incremented on each update)
- All managed resources with their current attributes
- Output values
- Module structure

### 7.2 Backend Configuration [HIGH FREQUENCY]

Partial backend configuration allows backend settings to be split between the config file and init-time arguments:

```hcl
terraform {
  backend "s3" {
    bucket = "my-tfstate"
    key    = "prod/terraform.tfstate"
    region = "us-east-2"
  }
}
```

Sensitive backend values (credentials) can be passed via `-backend-config=key=value` at init time rather than stored in the configuration file.

### 7.3 State Locking [HIGH FREQUENCY]

State locking prevents concurrent operations. When locking fails (another operation holds the lock), Terraform displays a lock ID. Use `terraform force-unlock <lock-id>` only after confirming no other operation is active.

### 7.4 Sensitive State

Sensitive resource attributes are stored in plaintext in the state file. State file security requires: encrypted backend storage, restricted IAM access, and audit logging on state file access.

---

## Domain 8: Read and Use the Terraform Documentation

### 8.1 Registry Navigation

The Terraform Registry at registry.terraform.io is the primary source of provider and module documentation. For any provider resource, the documentation includes:

- Example usage
- Argument reference (all configurable attributes)
- Attribute reference (all computed attributes available after creation)
- Import section (the ID format for `terraform import`)
- Timeouts section (customizable operation timeouts)

### 8.2 Finding Import ID Formats

For the exam and in practice, always look up the import ID format in the provider documentation rather than guessing. The format is unique per resource type and often non-obvious.

---

## Domain 9: Understand Terraform Cloud Capabilities

### 9.1 HCP Terraform vs. Terraform CLI

HCP Terraform (formerly Terraform Cloud) adds to the open-source CLI:

- Remote state storage with encryption
- Remote execution (plans and applies run in the cloud)
- Team access controls with role-based permissions
- Run triggers (workspace B automatically plans when workspace A applies)
- Sentinel policy enforcement
- Private module registry
- SSO integration
- Audit logging

### 9.2 Sentinel Policy Framework [HIGH FREQUENCY]

Sentinel is a policy-as-code framework that evaluates Terraform plans before apply. Policies are written in the Sentinel language and can:

- Check that all EC2 instances are a specific instance type
- Require all resources to have specific tags
- Block creation of resources in prohibited regions
- Enforce naming conventions

Policy enforcement levels:

- **Advisory**: warns if violated but allows the run to proceed
- **Soft mandatory**: blocks the run but can be overridden by an authorized user
- **Hard mandatory**: blocks the run unconditionally

### 9.3 Terraform Enterprise vs. HCP Terraform

Terraform Enterprise is the self-hosted version. HCP Terraform is the SaaS version. Both provide the same feature set. The key difference is deployment model: Enterprise runs in your own infrastructure (for air-gapped or regulatory environments), HCP Terraform runs in HashiCorp's cloud.

---

## Exam Preparation Checklist

Use this checklist in the final week before your exam:

- [ ] I can describe the Terraform workflow: init, plan, apply
- [ ] I know every core CLI command and its most important flags
- [ ] I can explain the purpose of the state file and name its contents
- [ ] I can describe at least three remote backends and their locking mechanisms
- [ ] I understand variable precedence order from lowest to highest
- [ ] I can explain provider aliasing and when it is required
- [ ] I know the standard module directory structure
- [ ] I can write a dynamic block for a repeatable nested configuration block
- [ ] I understand the difference between for_each with maps vs. sets
- [ ] I can explain what a moved block does and why it was introduced
- [ ] I understand the import block vs. the CLI import command
- [ ] I know the Terraform Cloud organizational hierarchy: Organization > Workspace
- [ ] I can describe Sentinel policy enforcement levels
- [ ] I understand the difference between Terraform open-source, HCP Terraform, and Terraform Enterprise

---

## Key Terms Reference

- **IaC**: Infrastructure as Code — managing infrastructure through version-controlled configuration files
- **Idempotency**: applying an operation multiple times produces the same result as applying it once
- **Provider**: a plugin that implements resources for a specific platform or service
- **Resource**: a managed infrastructure object declared in a `resource` block
- **Data source**: a read-only query of existing infrastructure declared in a `data` block
- **State**: a record of which resources Terraform manages and their current attributes
- **Backend**: configuration for where and how state is stored
- **Workspace**: a named state file instance within a backend
- **Module**: a reusable collection of Terraform resources
- **Sentinel**: policy-as-code framework for HCP Terraform and Terraform Enterprise
- **for_each**: meta-argument creating one resource per element in a map or set
- **count**: meta-argument creating N indexed resource instances
- **moved block**: declares a resource address change without modifying infrastructure
- **import block**: integrates resource import into the plan/apply cycle (Terraform 1.5+)

---

## Supplemental Resources

**1. Terraform Associate 003 Exam Review Guide**
<https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003>
The official HashiCorp exam review guide for the Terraform Associate 003 certification. Maps every exam objective domain to specific tutorials, documentation pages, and hands-on exercises. Use this guide alongside Module 16 content in the final two weeks before the exam to identify any knowledge gaps and prioritize review areas. Includes the complete list of exam objectives with difficulty indicators.

**2. HashiCorp Learn — Terraform Tutorials**
<https://developer.hashicorp.com/terraform/tutorials>
The central index of all official Terraform tutorials organized by topic. Covers the full certification exam scope including core workflow, state management, module development, Terraform Cloud configuration, security, and advanced HCL patterns. Each tutorial includes a working code example, estimated completion time, and prerequisite list. Completing the tutorials tagged "Associate" provides practical experience with every exam domain.

**3. Terraform Associate 003 Sample Questions**
<https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-questions>
Official sample questions released by HashiCorp for the Terraform Associate 003 exam. Covers all nine objective domains with questions at representative difficulty levels. Use these questions to calibrate your readiness after completing the course review, identify domains where additional study is needed, and familiarize yourself with the question format and phrasing used on the actual exam.

---

End of Module 16 Reading Guide
