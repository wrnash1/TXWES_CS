# Reading Guide: Module 07 — Terraform Variables, Outputs, and Locals

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

- Write input variable declarations with all supported arguments
- Apply type constraints and validation blocks to enforce configuration rules
- Define output values and consume them programmatically
- Create local values to simplify complex expressions
- Predict which variable value Terraform will use given multiple sources
- Construct `.tfvars` files for environment-specific deployments

---

## 1. Input Variables

### 1.1 Variable Block Syntax

The `variable` block is the mechanism for accepting external input into a Terraform configuration. Every argument inside the block is optional, but well-written configurations include all of them.

```hcl
variable "instance_type" {
  type        = string
  description = "EC2 instance type for the web server"
  default     = "t3.micro"
  sensitive   = false

  validation {
    condition     = can(regex("^t[23]\\.", var.instance_type))
    error_message = "instance_type must be a t2 or t3 family type."
  }
}
```

| Argument | Required | Purpose |
|---|---|---|
| `type` | No | Enforces a data type on the value |
| `description` | No | Documents the purpose of the variable |
| `default` | No | Provides a fallback value; omit to require caller input |
| `sensitive` | No | Redacts value from console output and plan display |
| `validation` | No | One or more blocks that enforce custom conditions |
| `nullable` | No | If `false`, null cannot be assigned; defaults to `true` |

### 1.2 Type System

Terraform's type system has two categories: **primitive types** and **complex types**.

**Primitive types:**

- `string` — a sequence of Unicode characters
- `number` — an integer or floating-point value
- `bool` — `true` or `false`

**Complex types:**

- `list(type)` — ordered sequence, zero-indexed
- `set(type)` — unordered collection of unique values
- `map(type)` — key-value pairs with string keys
- `object({ key = type, ... })` — a fixed-shape map with named attributes
- `tuple([type, type, ...])` — a fixed-length ordered sequence of potentially different types

```hcl
variable "vpc_config" {
  type = object({
    cidr_block           = string
    enable_dns_hostnames = bool
    az_count             = number
  })
  default = {
    cidr_block           = "10.0.0.0/16"
    enable_dns_hostnames = true
    az_count             = 2
  }
}
```

Using `object` types enforces the shape of complex inputs and makes the interface of a module self-documenting.

### 1.3 Validation Blocks

A `validation` block consists of two required arguments: `condition` and `error_message`.

```hcl
variable "port" {
  type = number

  validation {
    condition     = var.port >= 1 && var.port <= 65535
    error_message = "port must be between 1 and 65535 inclusive."
  }
}
```

Rules for validation blocks:

- The `condition` expression must return `bool`
- You may only reference the current variable in the condition — not other variables
- Multiple `validation` blocks are allowed; all must pass
- Use `can()` to test whether an expression produces an error (useful for regex and parsing)

### 1.4 Sensitive Variables

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}
```

When `sensitive = true`:

- The value is replaced with `(sensitive value)` in plan and apply output
- Any output that references this variable is automatically treated as sensitive
- The value is **still stored in plaintext** inside `terraform.tfstate`

---

## 2. Output Values

### 2.1 Output Block Syntax

```hcl
output "vpc_id" {
  description = "The ID of the created VPC"
  value       = aws_vpc.main.id
}
```

| Argument | Required | Purpose |
|---|---|---|
| `value` | Yes | The expression to expose |
| `description` | No | Documents the output's purpose |
| `sensitive` | No | Redacts from display; still in state |
| `depends_on` | No | Explicit dependency to ensure ordering |
| `precondition` | No | Asserts a condition before outputting (Terraform 1.2+) |

### 2.2 Querying Outputs

After `terraform apply` you can retrieve output values at any time:

```bash
# Show all outputs
terraform output

# Show a single output value
terraform output vpc_id

# Show all outputs as JSON (for scripting)
terraform output -json

# Show raw value without quotes (useful in shell scripts)
terraform output -raw vpc_id
```

### 2.3 Outputs in Module Composition

When a root module calls a child module, child module outputs become accessible as `module.<name>.<output>`:

```hcl
module "vpc" {
  source     = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = module.vpc.vpc_id
  cidr_block = "10.0.1.0/24"
}
```

The child module's `outputs.tf` must declare the output for it to be accessible:

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  value = aws_vpc.main.id
}
```

---

## 3. Local Values

### 3.1 Locals Block Syntax

Local values are declared with a `locals` block (note the plural). Each entry is a name-expression pair.

```hcl
locals {
  environment  = var.environment
  name_prefix  = "${var.project}-${var.environment}"
  is_prod      = var.environment == "prod"
  web_port     = 443
  common_tags  = merge(var.tags, {
    ManagedBy   = "Terraform"
    Environment = var.environment
  })
}
```

Reference locals using the `local.` prefix (note: singular):

```hcl
resource "aws_security_group" "web" {
  name = "${local.name_prefix}-sg"
  tags = local.common_tags
}
```

### 3.2 When to Use Locals

| Use case | Best choice |
|---|---|
| Value supplied by the caller | `variable` |
| Value derived from other values | `locals` |
| Repeated complex expression | `locals` |
| Conditional logic shared across resources | `locals` |
| Secret or sensitive input | `variable` with `sensitive = true` |

### 3.3 Locals Cannot Reference Each Other Circularly

Terraform evaluates locals in dependency order. A local can reference another local, but circular dependencies will cause an error during the configuration load phase.

```hcl
locals {
  base  = "my-app"
  full  = "${local.base}-${var.environment}"   # valid — base is defined above
}
```

---

## 4. Variable Precedence

Terraform evaluates variables from multiple sources. When the same variable appears in more than one source, the **higher-precedence source wins**.

### 4.1 Precedence Order (Lowest to Highest)

| Priority | Source |
|---|---|
| 1 (lowest) | `default` value in `variable` block |
| 2 | `terraform.tfvars` file (auto-loaded if present) |
| 3 | `terraform.tfvars.json` file (auto-loaded if present) |
| 4 | `*.auto.tfvars` files (auto-loaded, alphabetical) |
| 5 | `*.auto.tfvars.json` files (auto-loaded, alphabetical) |
| 6 | `-var-file` flag on CLI |
| 7 | `-var` flag on CLI |
| 8 (highest) | `TF_VAR_name` environment variable |

**Exam tip**: Environment variables (`TF_VAR_`) have the highest precedence. The `-var` flag has second-highest. This is the most commonly tested aspect of variable precedence.

### 4.2 tfvars File Syntax

```hcl
# terraform.tfvars
region         = "us-west-2"
instance_count = 3
environment    = "staging"

allowed_cidrs = [
  "10.0.0.0/8",
  "172.16.0.0/12",
]

tags = {
  Project = "my-app"
  Team    = "platform"
}
```

### 4.3 Auto-loaded Files

Terraform automatically loads these file names without any flags:

- `terraform.tfvars`
- `terraform.tfvars.json`
- Any file ending in `.auto.tfvars`
- Any file ending in `.auto.tfvars.json`

All other `.tfvars` files must be specified with `-var-file`.

### 4.4 TF_VAR_ Environment Variables

```bash
# Set before running Terraform
export TF_VAR_region="us-east-2"
export TF_VAR_db_password="$VAULT_SECRET"
export TF_VAR_instance_count="5"

terraform plan
```

The environment variable name is `TF_VAR_` followed by the exact variable name. The prefix and name are case-sensitive.

---

## 5. Command Reference

| Command | Description |
|---|---|
| `terraform plan -var="key=value"` | Pass a single variable on CLI |
| `terraform plan -var-file="file.tfvars"` | Load variables from a specific file |
| `terraform output` | List all output values |
| `terraform output <name>` | Show a single output value |
| `terraform output -json` | Show all outputs as JSON |
| `terraform output -raw <name>` | Show raw string value (no quotes) |
| `terraform console` | Interactive REPL for testing expressions |

---

## 6. Exam Tips — Terraform Associate 003

The following points are high-frequency exam topics for this module:

1. **Precedence order is exact**: Know the 8-level precedence from `default` up to `TF_VAR_`. It is tested directly.

2. **`sensitive = true` does not encrypt state**: The state file still holds the value in plaintext. Encryption must be handled at the backend level.

3. **Locals vs. variables**: Locals are internal computations. Variables accept external input. A caller cannot pass a value for a `locals` entry.

4. **`terraform output -raw`**: Returns an unquoted string — used in shell scripts that consume output values.

5. **Auto-loaded files**: `terraform.tfvars` and `*.auto.tfvars` load automatically. Any other `.tfvars` file requires `-var-file`.

6. **`can()` function in validation**: `can(regex("pattern", var.value))` returns `true` if the regex matches and `false` if it fails, rather than throwing an error.

7. **`nullable = false`**: Prevents a variable from being set to `null`. If omitted, `nullable` defaults to `true`.

8. **Type `any`**: Terraform also accepts `type = any`, which disables type checking. Avoid in production but be able to recognize it on the exam.

---

## 7. Summary

This module covered the three mechanisms Terraform provides for managing values inside a configuration:

- **Input variables** define the interface of your configuration; they accept external input with full type safety and validation
- **Output values** expose resource attributes for consumption by operators, pipelines, and other modules
- **Local values** reduce repetition and improve readability by naming derived expressions

Mastery of variable precedence and the distinction between sensitive storage vs. display suppression are essential for both the exam and real-world practice.

---

## 8. Supplemental Resources

**1. Terraform Input Variables Reference**
<https://developer.hashicorp.com/terraform/language/values/variables>
Complete reference for all variable block arguments including `nullable`, `sensitive`, and `validation`. Includes the full variable value precedence table and examples for each source type.

**2. Terraform Output Values Reference**
<https://developer.hashicorp.com/terraform/language/values/outputs>
Documents all output block arguments, how sensitive outputs behave in CLI and state, and how outputs are consumed across module boundaries. Covers the `precondition` argument added in Terraform 1.2.

**3. Terraform Local Values Reference**
<https://developer.hashicorp.com/terraform/language/values/locals>
Explains the `locals` block syntax, when locals are evaluated in the dependency graph, and guidance on avoiding over-use of locals that reduces configuration clarity.

---

*Texas Wesleyan University — CIS-4337 Infrastructure Automation*
*Proprietary and Confidential. Not for disclosure outside of authorized course participants.*
