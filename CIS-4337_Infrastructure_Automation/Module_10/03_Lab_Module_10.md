# Lab: Module 10 — Terraform Workspaces and Environments

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will work with Terraform workspaces to deploy environment-specific configurations to isolated state. You will use the `local` and `random` providers (no cloud credentials required) to simulate deploying an application to `dev`, `staging`, and `prod` environments from a single configuration. You will also build a directory-based structure to understand the alternative approach.

**Estimated time**: 75–90 minutes

**Prerequisites**:

- Terraform >= 1.5 installed
- A text editor
- A Unix/Linux terminal or Git Bash on Windows

---

## Part 1: Workspace Basics (15 minutes)

### Step 1.1 — Create Lab Directory

```bash
mkdir -p ~/tf-lab-10/workspace-demo
cd ~/tf-lab-10/workspace-demo
mkdir -p output
```

### Step 1.2 — Create main.tf

```hcl
# main.tf

terraform {
  required_version = ">= 1.5"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "local" {}
provider "random" {}

locals {
  workspace_config = {
    default = {
      replicas      = 1
      instance_size = "small"
      log_level     = "debug"
    }
    dev = {
      replicas      = 1
      instance_size = "small"
      log_level     = "debug"
    }
    staging = {
      replicas      = 2
      instance_size = "medium"
      log_level     = "info"
    }
    prod = {
      replicas      = 3
      instance_size = "large"
      log_level     = "warn"
    }
  }

  config = local.workspace_config[terraform.workspace]
}

resource "random_id" "deployment_id" {
  byte_length = 6
}

resource "local_file" "deployment_config" {
  filename = "${path.module}/output/${terraform.workspace}-deployment.json"
  content  = jsonencode({
    workspace     = terraform.workspace
    deployment_id = random_id.deployment_id.hex
    replicas      = local.config.replicas
    instance_size = local.config.instance_size
    log_level     = local.config.log_level
    timestamp     = "2026-06-02T00:00:00Z"
  })
  file_permission = "0644"
}

output "workspace" {
  value = terraform.workspace
}

output "deployment_id" {
  value = random_id.deployment_id.hex
}

output "replicas" {
  value = local.config.replicas
}

output "config_file" {
  value = local_file.deployment_config.filename
}
```

### Step 1.3 — Initialize

```bash
terraform init
```

### Step 1.4 — Check Current Workspace

```bash
terraform workspace show
# default

terraform workspace list
# * default
```

---

## Part 2: Deploy to Multiple Workspaces (20 minutes)

### Step 2.1 — Deploy to Default Workspace

```bash
terraform apply -auto-approve
terraform output
```

Note the `deployment_id` value and the `replicas` output (should be 1).

### Step 2.2 — Create and Deploy to Dev Workspace

```bash
terraform workspace new dev
terraform workspace show
# dev

terraform apply -auto-approve
terraform output
```

Note: The `deployment_id` will be DIFFERENT from the default workspace — each workspace has its own state.

### Step 2.3 — Create and Deploy to Staging Workspace

```bash
terraform workspace new staging
terraform apply -auto-approve
terraform output
```

Observe that `replicas` is now 2 (from the staging config).

### Step 2.4 — Create and Deploy to Prod Workspace

```bash
terraform workspace new prod
terraform apply -auto-approve
terraform output
```

Observe that `replicas` is now 3 and `instance_size` is `large`.

---

## Part 3: Inspect Workspace State Isolation (15 minutes)

### Step 3.1 — List All Workspaces

```bash
terraform workspace list
```

Expected output:

```
  default
  dev
  staging
* prod
```

### Step 3.2 — Inspect the State Directory Structure

```bash
ls terraform.tfstate.d/
ls terraform.tfstate.d/dev/
ls terraform.tfstate.d/staging/
ls terraform.tfstate.d/prod/
```

Confirm each workspace has its own `terraform.tfstate` file.

### Step 3.3 — Verify Isolation

Switch workspaces and compare `deployment_id` values:

```bash
terraform workspace select dev
terraform output deployment_id

terraform workspace select staging
terraform output deployment_id

terraform workspace select prod
terraform output deployment_id
```

Each value should be different — confirming complete state isolation between workspaces.

### Step 3.4 — Inspect Output Files

```bash
ls output/
cat output/dev-deployment.json
cat output/staging-deployment.json
cat output/prod-deployment.json
```

---

## Part 4: Modify and Re-apply to a Single Workspace (10 minutes)

### Step 4.1 — Switch to Dev and Modify

```bash
terraform workspace select dev
```

Add a new output to `main.tf`:

```hcl
output "environment_label" {
  value = "Deployed to workspace: ${terraform.workspace}"
}
```

### Step 4.2 — Plan and Apply

```bash
terraform plan
terraform apply -auto-approve
terraform output environment_label
```

Confirm that only the `dev` workspace state was modified. Switch to staging and verify it was not affected:

```bash
terraform workspace select staging
terraform output
# environment_label should not exist yet
```

---

## Part 5: Directory-Based Isolation (15 minutes)

### Step 5.1 — Create the Directory Structure

```bash
mkdir -p ~/tf-lab-10/dir-demo/{environments/{dev,staging,prod},modules/app}
cd ~/tf-lab-10/dir-demo
```

### Step 5.2 — Create the Shared Module

Create `modules/app/variables.tf`:

```hcl
variable "environment" {
  type = string
}

variable "replicas" {
  type    = number
  default = 1
}
```

Create `modules/app/main.tf`:

```hcl
terraform {
  required_providers {
    local  = { source = "hashicorp/local",  version = "~> 2.4" }
    random = { source = "hashicorp/random", version = "~> 3.5" }
  }
}

resource "random_id" "id" {
  byte_length = 4
}

resource "local_file" "config" {
  filename = "${path.root}/output/${var.environment}-app.json"
  content  = jsonencode({
    environment = var.environment
    replicas    = var.replicas
    app_id      = random_id.id.hex
  })
}
```

Create `modules/app/outputs.tf`:

```hcl
output "app_id" {
  value = random_id.id.hex
}
```

### Step 5.3 — Create dev Environment

Create `environments/dev/main.tf`:

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    local  = { source = "hashicorp/local",  version = "~> 2.4" }
    random = { source = "hashicorp/random", version = "~> 3.5" }
  }
}

provider "local"  {}
provider "random" {}

module "app" {
  source      = "../../modules/app"
  environment = "dev"
  replicas    = 1
}

output "app_id" {
  value = module.app.app_id
}
```

### Step 5.4 — Create prod Environment (Different Replica Count)

Create `environments/prod/main.tf` with `replicas = 3`.

### Step 5.5 — Deploy Each Environment Independently

```bash
mkdir -p ~/tf-lab-10/dir-demo/output

cd ~/tf-lab-10/dir-demo/environments/dev
terraform init
terraform apply -auto-approve

cd ~/tf-lab-10/dir-demo/environments/prod
terraform init
terraform apply -auto-approve
```

Observe: each environment has its own `.terraform/` directory and `terraform.tfstate`. There is no risk of one environment's operations affecting the other.

---

## Part 6: Workspace Deletion (5 minutes)

Return to the workspace demo:

```bash
cd ~/tf-lab-10/workspace-demo

# You cannot delete the currently selected workspace
# Select a different one first
terraform workspace select default

# Destroy prod resources
terraform workspace select prod
terraform destroy -auto-approve
terraform workspace select default
terraform workspace delete prod

# Verify
terraform workspace list
```

---

## Cleanup

```bash
# Clean up workspace demo
cd ~/tf-lab-10/workspace-demo
for ws in dev staging; do
  terraform workspace select $ws
  terraform destroy -auto-approve
done
terraform workspace select default
terraform destroy -auto-approve
for ws in dev staging; do
  terraform workspace delete $ws
done

# Clean up directory demo
cd ~/tf-lab-10/dir-demo/environments/dev && terraform destroy -auto-approve
cd ~/tf-lab-10/dir-demo/environments/prod && terraform destroy -auto-approve

rm -rf ~/tf-lab-10/
```

---

## Deliverables

1. Screenshot of `terraform workspace list` showing all 4 workspaces after Part 2
2. Screenshot showing different `deployment_id` values across workspaces (Part 3)
3. Screenshot of `terraform.tfstate.d/` directory listing
4. Screenshot of the `staging-deployment.json` file contents showing `replicas: 2`
5. Brief written answer (3–5 sentences): When would you choose workspaces over directory-based isolation, and vice versa?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| All 4 workspace environments deployed correctly | 25 |
| State isolation confirmed (different IDs per workspace) | 20 |
| Workspace list and state directory structure captured | 15 |
| Directory-based structure built and deployed | 25 |
| Workspace deletion completed correctly | 10 |
| Written comparison answer submitted | 5 |
| **Total** | **100** |

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
