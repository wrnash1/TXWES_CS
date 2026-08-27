# Lab: Module 07 — Terraform Variables, Outputs, and Locals

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Lab Overview

In this lab you will build a fully parameterized Terraform configuration that provisions a simulated web application environment using the `local` provider (no cloud credentials required). You will practice declaring typed variables with validation, using `.tfvars` files, setting environment variables, working with local values, and querying outputs.

**Estimated time**: 60–75 minutes

**Prerequisites**:

- Terraform >= 1.5 installed and on your PATH
- A text editor (VS Code recommended)
- A Unix/Linux shell or Git Bash on Windows

---

## Part 1: Project Setup (10 minutes)

### Step 1.1 — Create the Lab Directory

```bash
mkdir -p ~/tf-lab-07 && cd ~/tf-lab-07
```

### Step 1.2 — Create the Provider Configuration

Create `main.tf`:

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}
```

Initialize the configuration:

```bash
terraform init
```

Expected output includes: `Terraform has been successfully initialized!`

---

## Part 2: Declare Input Variables (15 minutes)

### Step 2.1 — Create variables.tf

```hcl
# variables.tf

variable "app_name" {
  type        = string
  description = "Name of the application"

  validation {
    condition     = length(var.app_name) >= 3 && length(var.app_name) <= 20
    error_message = "app_name must be between 3 and 20 characters."
  }
}

variable "environment" {
  type        = string
  description = "Deployment environment"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be one of: dev, staging, prod."
  }
}

variable "port" {
  type        = number
  description = "Application listening port"
  default     = 8080

  validation {
    condition     = var.port >= 1024 && var.port <= 65535
    error_message = "port must be between 1024 and 65535."
  }
}

variable "enable_https" {
  type        = bool
  description = "Enable HTTPS configuration"
  default     = false
}

variable "allowed_origins" {
  type        = list(string)
  description = "List of allowed CORS origins"
  default     = ["https://example.com"]
}

variable "app_config" {
  type = object({
    max_connections = number
    log_level       = string
    debug_mode      = bool
  })
  description = "Application configuration object"
  default = {
    max_connections = 100
    log_level       = "info"
    debug_mode      = false
  }
}

variable "secret_api_key" {
  type        = string
  description = "API key for external service"
  sensitive   = true
  default     = "placeholder-not-real"
}
```

### Step 2.2 — Test Validation

Run a plan with an invalid environment value:

```bash
terraform plan -var="app_name=myapp" -var="environment=qa"
```

Confirm that Terraform rejects the value with the custom error message.

Now test with a valid value:

```bash
terraform plan -var="app_name=myapp" -var="environment=dev"
```

---

## Part 3: Define Local Values (10 minutes)

### Step 3.1 — Create locals.tf

```hcl
# locals.tf

locals {
  name_prefix = "${var.app_name}-${var.environment}"

  config_filename = "${local.name_prefix}-config.json"

  protocol = var.enable_https ? "https" : "http"

  base_url = "${local.protocol}://localhost:${var.port}"

  app_metadata = {
    name        = var.app_name
    environment = var.environment
    version     = "1.0.0"
    managed_by  = "Terraform"
    base_url    = local.base_url
  }
}
```

---

## Part 4: Create Resources Using Variables and Locals (15 minutes)

### Step 4.1 — Add Resources to main.tf

Append the following to `main.tf`:

```hcl
resource "local_file" "app_config" {
  filename = "${path.module}/output/${local.config_filename}"
  content  = jsonencode({
    app_name        = var.app_name
    environment     = var.environment
    port            = var.port
    enable_https    = var.enable_https
    base_url        = local.base_url
    allowed_origins = var.allowed_origins
    max_connections = var.app_config.max_connections
    log_level       = var.app_config.log_level
    debug_mode      = var.app_config.debug_mode
  })
  file_permission = "0644"
}

resource "local_file" "env_file" {
  filename = "${path.module}/output/${local.name_prefix}.env"
  content  = <<-EOT
    APP_NAME=${var.app_name}
    ENVIRONMENT=${var.environment}
    PORT=${var.port}
    ENABLE_HTTPS=${var.enable_https}
    BASE_URL=${local.base_url}
    LOG_LEVEL=${var.app_config.log_level}
  EOT
  file_permission = "0600"
}
```

### Step 4.2 — Create the Output Directory

```bash
mkdir -p output
```

---

## Part 5: Define Outputs (10 minutes)

### Step 5.1 — Create outputs.tf

```hcl
# outputs.tf

output "app_name" {
  description = "The application name"
  value       = var.app_name
}

output "environment" {
  description = "The deployment environment"
  value       = var.environment
}

output "base_url" {
  description = "The application base URL"
  value       = local.base_url
}

output "config_file_path" {
  description = "Path to the generated configuration file"
  value       = local_file.app_config.filename
}

output "env_file_path" {
  description = "Path to the generated environment file"
  value       = local_file.env_file.filename
}

output "app_metadata" {
  description = "Full application metadata map"
  value       = local.app_metadata
}

output "api_key_length" {
  description = "Length of the API key (sensitive value masked)"
  value       = length(var.secret_api_key)
}
```

---

## Part 6: Create tfvars Files (10 minutes)

### Step 6.1 — Create dev.tfvars

```hcl
# dev.tfvars
app_name     = "webapp"
environment  = "dev"
port         = 3000
enable_https = false

allowed_origins = [
  "http://localhost:3000",
  "http://localhost:8080",
]

app_config = {
  max_connections = 50
  log_level       = "debug"
  debug_mode      = true
}
```

### Step 6.2 — Create prod.tfvars

```hcl
# prod.tfvars
app_name     = "webapp"
environment  = "prod"
port         = 443
enable_https = true

allowed_origins = [
  "https://webapp.example.com",
  "https://api.example.com",
]

app_config = {
  max_connections = 500
  log_level       = "warn"
  debug_mode      = false
}
```

### Step 6.3 — Apply the Dev Configuration

```bash
terraform apply -var-file="dev.tfvars" -auto-approve
```

Verify the output files were created:

```bash
ls output/
cat output/webapp-dev-config.json
```

---

## Part 7: Variable Precedence Exercise (10 minutes)

### Step 7.1 — Test Environment Variable Override

Set an environment variable and observe it overrides the tfvars value:

```bash
export TF_VAR_port=9090
terraform plan -var-file="dev.tfvars"
```

Look at the plan output — `port` should show `9090` rather than `3000` from `dev.tfvars`.

### Step 7.2 — Test CLI Override

The `-var` flag overrides even `TF_VAR_`:

```bash
terraform plan -var-file="dev.tfvars" -var="port=7777"
```

Verify that `port` is `7777`.

### Step 7.3 — Clean Up Environment Variable

```bash
unset TF_VAR_port
```

### Step 7.4 — Apply Prod Configuration

```bash
terraform apply -var-file="prod.tfvars" -auto-approve
```

Inspect the new output files:

```bash
cat output/webapp-prod-config.json
cat output/webapp-prod.env
```

---

## Part 8: Query Outputs (5 minutes)

```bash
# List all outputs
terraform output

# Query a single output
terraform output base_url

# Get raw value for use in a shell script
terraform output -raw base_url

# Get all outputs as JSON
terraform output -json
```

---

## Cleanup

```bash
terraform destroy -var-file="prod.tfvars" -auto-approve
rm -rf output/
```

---

## Deliverables

Submit the following to the course LMS:

1. `variables.tf` — complete with all variable declarations
2. `locals.tf` — with all local value definitions
3. `outputs.tf` — with all output declarations
4. `dev.tfvars` and `prod.tfvars`
5. A screenshot of `terraform output -json` after applying `prod.tfvars`
6. A screenshot showing the validation error when `environment=qa` is passed

---

## Grading Rubric

| Criterion | Points |
|---|---|
| All variables declared with correct types | 20 |
| Validation blocks function correctly | 20 |
| Locals defined and referenced properly | 15 |
| Outputs defined and queryable | 15 |
| Both `.tfvars` files produce correct output files | 15 |
| Precedence exercise completed correctly | 10 |
| Clean destroy with no errors | 5 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Structured Object Variable with Conditional Local

Extend the configuration with a structured `server_config` variable using `type = object` that drives multiple resource behaviors through conditional local values.

**Step A.** Add the following variable to `variables.tf`:

```hcl
variable "server_config" {
  type = object({
    tier         = string
    replica_count = number
    cache_enabled = bool
  })
  default = {
    tier          = "standard"
    replica_count = 1
    cache_enabled = false
  }

  validation {
    condition     = contains(["basic", "standard", "premium"], var.server_config.tier)
    error_message = "tier must be basic, standard, or premium."
  }
}
```

**Step B.** Add the following locals to `locals.tf`:

```hcl
  max_workers   = var.server_config.tier == "premium" ? 16 : (var.server_config.tier == "standard" ? 4 : 1)
  cache_ttl     = var.server_config.cache_enabled ? 3600 : 0
  tier_label    = upper(var.server_config.tier)
```

1. Add a `local_file` resource named `server_spec` that writes a JSON file combining `local.max_workers`, `local.cache_ttl`, `local.tier_label`, and `var.server_config.replica_count` using `jsonencode()`.
2. Add an output `server_spec_summary` that exposes `{ tier = local.tier_label, workers = local.max_workers, cache_ttl = local.cache_ttl }`.
3. Apply with `-var='server_config={"tier":"premium","replica_count":3,"cache_enabled":true}'` and verify the generated file and output values.

### Challenge 2: Variable Precedence Race

Demonstrate all levels of variable precedence by configuring the same variable `app_name` from five different sources simultaneously.

1. Ensure `app_name` has a default of `"default-app"` in `variables.tf`.
2. Set `app_name = "tfvars-app"` in `terraform.tfvars` and `app_name = "auto-app"` in a new file `override.auto.tfvars`.
3. Export `TF_VAR_app_name=env-app` in the shell.
4. Run `terraform plan -var-file="dev.tfvars" -var="app_name=cli-app"` and record which value wins.
5. Remove the `-var="app_name=cli-app"` flag and re-run. Record which value now wins and explain the precedence chain in `lab_notes.txt` from lowest to highest for all five sources you configured.

### Reflection Questions

1. The lab used `sensitive = true` on `var.secret_api_key` to hide it from CLI output. Given that the value is still stored in plaintext in `terraform.tfstate`, describe two additional controls you would implement in a production environment to protect secrets flowing through Terraform.
2. You built separate `dev.tfvars` and `prod.tfvars` files to drive different configurations from one codebase. Compare this pattern to using Terraform workspaces for environment separation. What are the advantages and disadvantages of each approach?

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
