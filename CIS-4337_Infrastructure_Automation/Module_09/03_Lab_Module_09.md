# Lab: Module 09 — Terraform Modules

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will build two reusable local modules — `app_config` and `environment_info` — and compose them from a root module. You will practice defining module inputs and outputs, consuming module outputs in other resources, and using `for_each` to create multiple module instances. No cloud credentials are required; the lab uses the `local` and `random` providers.

**Estimated time**: 75–90 minutes

**Prerequisites**:

- Terraform >= 1.5 installed
- A text editor
- A Unix/Linux terminal or Git Bash on Windows

---

## Part 1: Project Structure (10 minutes)

### Step 1.1 — Create Directory Structure

```bash
mkdir -p ~/tf-lab-09/{modules/app_config,modules/environment_info,output}
cd ~/tf-lab-09
```

Your structure should look like:

```
tf-lab-09/
  modules/
    app_config/
    environment_info/
  output/
```

---

## Part 2: Build the app_config Module (20 minutes)

### Step 2.1 — Create modules/app_config/variables.tf

```hcl
# modules/app_config/variables.tf

variable "app_name" {
  type        = string
  description = "Name of the application"

  validation {
    condition     = length(var.app_name) >= 2
    error_message = "app_name must be at least 2 characters."
  }
}

variable "environment" {
  type        = string
  description = "Deployment environment"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging, or prod."
  }
}

variable "port" {
  type        = number
  description = "Application port"
  default     = 8080
}

variable "replicas" {
  type        = number
  description = "Number of application replicas"
  default     = 1
}

variable "extra_env_vars" {
  type        = map(string)
  description = "Additional environment variables"
  default     = {}
}
```

### Step 2.2 — Create modules/app_config/main.tf

```hcl
# modules/app_config/main.tf

terraform {
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

resource "random_id" "app_id" {
  byte_length = 4
}

locals {
  name_prefix = "${var.app_name}-${var.environment}"
  base_env_vars = {
    APP_NAME    = var.app_name
    ENVIRONMENT = var.environment
    PORT        = tostring(var.port)
    REPLICAS    = tostring(var.replicas)
    APP_ID      = random_id.app_id.hex
  }
  all_env_vars = merge(local.base_env_vars, var.extra_env_vars)
}

resource "local_file" "config" {
  filename = "${path.root}/output/${local.name_prefix}-config.json"
  content  = jsonencode({
    app_name    = var.app_name
    environment = var.environment
    port        = var.port
    replicas    = var.replicas
    app_id      = random_id.app_id.hex
    env_vars    = local.all_env_vars
  })
  file_permission = "0644"
}
```

### Step 2.3 — Create modules/app_config/outputs.tf

```hcl
# modules/app_config/outputs.tf

output "app_id" {
  description = "Unique ID for this application instance"
  value       = random_id.app_id.hex
}

output "name_prefix" {
  description = "Name prefix used for all resources"
  value       = local.name_prefix
}

output "config_file_path" {
  description = "Absolute path to the generated config file"
  value       = local_file.config.filename
}

output "env_vars" {
  description = "All environment variables for this application"
  value       = local.all_env_vars
}
```

---

## Part 3: Build the environment_info Module (15 minutes)

### Step 3.1 — Create modules/environment_info/variables.tf

```hcl
# modules/environment_info/variables.tf

variable "environment" {
  type        = string
  description = "The deployment environment"
}

variable "apps" {
  type = list(object({
    name    = string
    app_id  = string
    port    = number
  }))
  description = "List of deployed application objects"
  default     = []
}
```

### Step 3.2 — Create modules/environment_info/main.tf

```hcl
# modules/environment_info/main.tf

terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

locals {
  summary = {
    environment = var.environment
    app_count   = length(var.apps)
    apps        = var.apps
    generated   = timestamp()
  }
}

resource "local_file" "summary" {
  filename        = "${path.root}/output/${var.environment}-summary.json"
  content         = jsonencode(local.summary)
  file_permission = "0644"
}
```

### Step 3.3 — Create modules/environment_info/outputs.tf

```hcl
# modules/environment_info/outputs.tf

output "summary_file_path" {
  description = "Path to the environment summary file"
  value       = local_file.summary.filename
}

output "app_count" {
  description = "Number of applications in this environment"
  value       = length(var.apps)
}
```

---

## Part 4: Build the Root Module (20 minutes)

### Step 4.1 — Create root variables.tf

```hcl
# variables.tf (root)

variable "environment" {
  type    = string
  default = "dev"
}
```

### Step 4.2 — Create root main.tf

```hcl
# main.tf (root)

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

# Call app_config module for the API service
module "api" {
  source = "./modules/app_config"

  app_name    = "api-service"
  environment = var.environment
  port        = 3000
  replicas    = 2
  extra_env_vars = {
    LOG_LEVEL   = "info"
    DB_HOST     = "localhost"
  }
}

# Call app_config module for the worker service
module "worker" {
  source = "./modules/app_config"

  app_name    = "worker-service"
  environment = var.environment
  port        = 4000
  replicas    = 3
  extra_env_vars = {
    LOG_LEVEL   = "warn"
    QUEUE_URL   = "amqp://localhost"
  }
}

# Compose outputs from both modules to feed into environment_info
module "env_info" {
  source = "./modules/environment_info"

  environment = var.environment
  apps = [
    {
      name   = module.api.name_prefix
      app_id = module.api.app_id
      port   = 3000
    },
    {
      name   = module.worker.name_prefix
      app_id = module.worker.app_id
      port   = 4000
    }
  ]
}
```

### Step 4.3 — Create root outputs.tf

```hcl
# outputs.tf (root)

output "api_app_id" {
  description = "Unique ID for the API service"
  value       = module.api.app_id
}

output "worker_app_id" {
  description = "Unique ID for the worker service"
  value       = module.worker.app_id
}

output "api_config_path" {
  value = module.api.config_file_path
}

output "worker_config_path" {
  value = module.worker.config_file_path
}

output "environment_summary_path" {
  value = module.env_info.summary_file_path
}

output "total_apps" {
  value = module.env_info.app_count
}
```

---

## Part 5: Initialize, Plan, and Apply (10 minutes)

### Step 5.1 — Initialize

```bash
terraform init
```

Observe that Terraform detects the three module sources. Local modules are used directly; `terraform init` does not download them.

### Step 5.2 — Validate

```bash
terraform validate
```

### Step 5.3 — Plan

```bash
terraform plan
```

Review the plan. Identify which resources are being created by which modules (look for `module.api.*`, `module.worker.*`, `module.env_info.*` prefixes).

### Step 5.4 — Apply

```bash
terraform apply -auto-approve
```

### Step 5.5 — Inspect Outputs

```bash
terraform output
terraform output -json
cat output/api-service-dev-config.json
cat output/worker-service-dev-config.json
cat output/dev-summary.json
```

---

## Part 6: for_each Module Instantiation (10 minutes)

### Step 6.1 — Modify root main.tf

Replace the `module "api"` and `module "worker"` blocks with a `for_each` approach:

```hcl
locals {
  services = {
    api = {
      port     = 3000
      replicas = 2
      extra_env_vars = {
        LOG_LEVEL = "info"
      }
    }
    worker = {
      port     = 4000
      replicas = 3
      extra_env_vars = {
        LOG_LEVEL = "warn"
      }
    }
    scheduler = {
      port     = 5000
      replicas = 1
      extra_env_vars = {
        LOG_LEVEL = "debug"
      }
    }
  }
}

module "services" {
  for_each = local.services
  source   = "./modules/app_config"

  app_name       = "${each.key}-service"
  environment    = var.environment
  port           = each.value.port
  replicas       = each.value.replicas
  extra_env_vars = each.value.extra_env_vars
}
```

Update the `module "env_info"` block to reference the new `for_each` module:

```hcl
module "env_info" {
  source = "./modules/environment_info"

  environment = var.environment
  apps = [
    for svc_key, svc_mod in module.services : {
      name   = svc_mod.name_prefix
      app_id = svc_mod.app_id
      port   = local.services[svc_key].port
    }
  ]
}
```

Remove the old individual module outputs and replace with:

```hcl
output "all_app_ids" {
  value = { for k, v in module.services : k => v.app_id }
}
```

### Step 6.2 — Apply the Changes

```bash
terraform init
terraform apply -auto-approve
```

Note: Terraform will ask you to confirm destroying the old module resources and creating new ones under the `for_each` addresses.

```bash
terraform output all_app_ids
ls output/
```

---

## Cleanup

```bash
terraform destroy -auto-approve
rm -rf output/ .terraform/
```

---

## Deliverables

1. All module file contents: `modules/app_config/*.tf` and `modules/environment_info/*.tf`
2. Root `main.tf`, `variables.tf`, and `outputs.tf` showing the `for_each` approach
3. Screenshot of `terraform output -json` after the final apply
4. Screenshot of `terraform plan` output showing module-prefixed resource addresses

---

## Grading Rubric

| Criterion | Points |
|---|---|
| `app_config` module with correct variables, resources, and outputs | 25 |
| `environment_info` module with correct interface | 15 |
| Root module correctly calls and composes both modules | 20 |
| Module outputs consumed correctly in root outputs | 15 |
| `for_each` module instantiation implemented correctly | 20 |
| Clean destroy with no errors | 5 |
| **Total** | **100** |

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
