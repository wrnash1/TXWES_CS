# Reading Guide: Module 10 — Terraform Workspaces and Environments

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


## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Learning Objectives

After completing this reading guide you will be able to:

- Create, select, list, and delete Terraform workspaces
- Use `terraform.workspace` to write environment-aware configurations
- Explain how workspace state is stored with local and remote backends
- Describe the limitations of workspaces for production multi-environment management
- Design a directory-based environment isolation structure
- Apply the hybrid workspace-directory pattern in appropriate contexts

---

## 1. Terraform Workspaces

### 1.1 Concept

A Terraform workspace is a named, isolated instance of state within a single backend and configuration. Every Terraform configuration starts with one workspace: `default`. Additional workspaces can be created and switched between at will.

Workspaces share:

- The same `.tf` configuration files
- The same backend (S3 bucket, Azure container, etc.)
- The same provider configuration

Workspaces do NOT share:

- State (`terraform.tfstate`) — each workspace has its own

### 1.2 Workspace Commands

| Command | Description |
|---|---|
| `terraform workspace list` | List all workspaces; `*` marks current |
| `terraform workspace show` | Print the name of the current workspace |
| `terraform workspace new <name>` | Create a workspace and switch to it |
| `terraform workspace select <name>` | Switch to an existing workspace |
| `terraform workspace delete <name>` | Delete a workspace (must not be selected) |

```bash
# Full workflow example
terraform workspace new dev
terraform apply -var-file="dev.tfvars"

terraform workspace new staging
terraform apply -var-file="staging.tfvars"

terraform workspace list
#   default
#   dev
# * staging

terraform workspace select dev
terraform workspace show
# dev
```

### 1.3 Workspace State Storage

**Local backend**: State is stored in `terraform.tfstate.d/<workspace>/terraform.tfstate`. The `default` workspace uses the root `terraform.tfstate` as usual.

```text
project/
  terraform.tfstate              # default workspace
  terraform.tfstate.d/
    dev/
      terraform.tfstate
    staging/
      terraform.tfstate
```

**S3 backend**: Each workspace is stored at a separate key:

- `default` workspace: the `key` argument value (e.g., `prod/app/terraform.tfstate`)
- Other workspaces: `env:/<workspace>/prod/app/terraform.tfstate`

**Azure Blob**: Each workspace is a separate blob named `<key>.<workspace>`.

**GCS**: Each workspace is stored at `<prefix>/<workspace>.tfstate`.

### 1.4 The default Workspace

- Always exists; is created automatically on `terraform init`
- Cannot be deleted
- Is selected by default when no other workspace is active
- Stores state in the root `terraform.tfstate` (local) or at the configured `key` (remote)

---

## 2. Using terraform.workspace

### 2.1 Built-in Value

`terraform.workspace` is a built-in string value that returns the name of the currently selected workspace. It is not a variable and requires no declaration.

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "acme-logs-${terraform.workspace}"
}
```

### 2.2 Conditional Configuration

```hcl
locals {
  is_prod = terraform.workspace == "prod"

  instance_type = local.is_prod ? "t3.medium" : "t3.micro"
  replica_count = local.is_prod ? 3 : 1
}
```

### 2.3 Lookup Maps

A more scalable pattern uses a map keyed by workspace name:

```hcl
locals {
  workspace_settings = {
    default = {
      instance_type    = "t3.micro"
      min_size         = 1
      max_size         = 2
      enable_logging   = false
    }
    dev = {
      instance_type    = "t3.micro"
      min_size         = 1
      max_size         = 2
      enable_logging   = true
    }
    staging = {
      instance_type    = "t3.small"
      min_size         = 2
      max_size         = 4
      enable_logging   = true
    }
    prod = {
      instance_type    = "t3.medium"
      min_size         = 3
      max_size         = 10
      enable_logging   = true
    }
  }

  settings = local.workspace_settings[terraform.workspace]
}
```

This approach centralizes all environment-specific values and makes the differences explicit and reviewable.

### 2.4 Resource Naming Convention

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name        = "vpc-${terraform.workspace}"
    Environment = terraform.workspace
    ManagedBy   = "Terraform"
  }
}
```

---

## 3. Workspace Limitations

Understanding the limitations of workspaces is as important as knowing how to use them. These limitations are frequently tested on the Terraform Associate exam.

### 3.1 Shared Backend Configuration

All workspaces in a configuration use the same backend. This means:

- `dev` and `prod` share the same S3 bucket (different keys, but same bucket and AWS account)
- IAM permissions that allow `terraform apply` for `dev` also apply to `prod`
- A misconfigured backend change affects all workspaces simultaneously

### 3.2 Shared Provider Configuration

All workspaces use the same `provider` block configuration. You cannot natively configure different AWS accounts, Azure subscriptions, or GCP projects per workspace.

To use separate cloud accounts per environment, you must use the directory structure approach or use `providers` meta-argument with aliased providers.

### 3.3 Implicit Selection Risk

The active workspace is a CLI-level setting stored in `.terraform/environment`. There is no way to tell which workspace will be used by reading the `.tf` files alone. An operator must run `terraform workspace show` before every operation to avoid accidentally applying to the wrong environment.

### 3.4 Code Complexity

As environments diverge in architecture, the `terraform.workspace` conditional logic grows increasingly complex. A `prod` environment requiring a multi-AZ RDS cluster while `dev` uses a single-AZ instance is still manageable. But if `prod` requires a completely different networking topology, the shared configuration becomes unmanageable.

---

## 4. Directory-Based Environment Isolation

### 4.1 Structure

The directory-based approach uses a separate directory per environment, each with its own configuration, backend, and variable files:

```text
infrastructure/
  environments/
    dev/
      main.tf          # Calls shared modules
      variables.tf
      terraform.tfvars
      backend.tf       # Points to dev S3 bucket
    staging/
      main.tf
      variables.tf
      terraform.tfvars
      backend.tf       # Points to staging S3 bucket
    prod/
      main.tf
      variables.tf
      terraform.tfvars
      backend.tf       # Points to prod S3 bucket
  modules/
    network/
    compute/
    database/
```

### 4.2 Shared Module Pattern

Each environment directory calls shared modules with environment-specific inputs:

```hcl
# environments/prod/main.tf

module "network" {
  source = "../../modules/network"

  environment  = "prod"
  vpc_cidr     = var.vpc_cidr
  az_count     = 3
}

module "compute" {
  source = "../../modules/compute"

  environment   = "prod"
  vpc_id        = module.network.vpc_id
  instance_type = var.instance_type
  min_size      = var.min_size
  max_size      = var.max_size
}
```

```hcl
# environments/prod/terraform.tfvars

vpc_cidr      = "10.0.0.0/16"
instance_type = "t3.medium"
min_size      = 3
max_size      = 10
```

### 4.3 Benefits vs. Workspaces

| Concern | Workspaces | Directory Isolation |
|---|---|---|
| State separation | Yes — separate state per workspace | Yes — separate backend per directory |
| Credential separation | No — shared provider config | Yes — different provider config per dir |
| Architecture differences | Limited — shared code | Full — each dir is independent |
| Clarity | Low — workspace is implicit | High — explicit directory structure |
| CI/CD integration | Medium — must pass workspace name | High — run from environment directory |
| Blast radius | Medium — wrong workspace risk | Low — physically separate configurations |

---

## 5. Comparison: Workspaces vs. Directory Structure

| When to use workspaces | When to use directory structure |
|---|---|
| Ephemeral test environments | Production environments |
| Feature branch isolation | Different cloud accounts per env |
| Single-person projects | Strict separation required by compliance |
| Low-risk short-lived environments | Architecturally different environments |
| CI/CD per-PR environments | Long-lived, regulated infrastructure |

---

## 6. Exam Tips — Terraform Associate 003

1. **`default` workspace cannot be deleted**: It always exists and is the starting workspace.

2. **`terraform workspace new` both creates and selects**: After `new`, the CLI is in the new workspace.

3. **`terraform workspace delete` has requirements**: The workspace must not currently be selected, and it must have no managed resources (empty state).

4. **`terraform.workspace` is a built-in value**: Not a variable; no `var.` prefix needed.

5. **Local state path**: `terraform.tfstate.d/<workspace>/terraform.tfstate` for all non-default workspaces.

6. **S3 state path**: `env:/<workspace>/<key>` for non-default workspaces.

7. **Workspaces are NOT the recommended solution for separate credentials**: HashiCorp explicitly recommends directory-based isolation when different cloud accounts or credentials are required per environment.

8. **Workspaces are well-suited for ephemeral environments**: Feature branches, PR-based environments, and short-lived test instances are the canonical workspace use cases.

---

## 7. Summary

Terraform workspaces provide lightweight state isolation within a shared configuration. They are best suited for ephemeral environments and feature-branch testing. For production-grade multi-environment infrastructure, the directory-based isolation pattern provides stronger guarantees: separate state, separate credentials, explicit architecture differences, and lower blast radius.

The two approaches are complementary rather than mutually exclusive — many teams use directory isolation for their major environment tiers and workspaces for ephemeral sub-environments within a tier.

---

## 8. Supplemental Resources

**1. Terraform Workspaces — Language Reference**
<https://developer.hashicorp.com/terraform/language/state/workspaces>
The official documentation for Terraform workspaces covering the `terraform.workspace` built-in value, workspace state storage paths for local and remote backends, the use cases where workspaces are appropriate, and the explicit guidance on when directory-based isolation is preferred.

**2. Terraform Workspace CLI Commands**
<https://developer.hashicorp.com/terraform/cli/commands/workspace>
Complete CLI reference for all `terraform workspace` subcommands: `list`, `show`, `new`, `select`, and `delete`. Includes behavioral notes such as the requirement that a workspace must have empty state before deletion.

**3. Terraform Recommended Practices — Workspace Usage**
<https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices/part1>
HashiCorp's recommended practices guide for structuring Terraform configurations across environments and teams. Covers when to use workspaces versus separate configurations, and how to organize state for multiple environments in a way that scales to large organizations.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
