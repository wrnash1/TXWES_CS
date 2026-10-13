# Video Script: Module 07 — Terraform Variables, Outputs, and Locals

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: HashiCorp Terraform Associate (003)

---

## Introduction (0:00 – 1:30)

Welcome back to CIS-4337, Infrastructure Automation. I'm Professor Nash, and this is Module 07.

So far you've learned how to write Terraform configurations and manage providers. Today we tackle one of the most practical and exam-heavy topics in Terraform: variables, outputs, and locals.

By the end of this module you will be able to:

- Declare and use input variables with type constraints and validation rules
- Mark sensitive variables to protect secrets in output
- Define output values to expose data from your configuration
- Use local values to reduce repetition and improve readability
- Understand exactly how Terraform resolves variable precedence
- Load variables from `.tfvars` files and environment variables

Let's get started.

[PAUSE]

---

## Section 1: Input Variables (1:30 – 5:30)

Input variables are how you parameterize a Terraform configuration. Instead of hardcoding values, you declare a variable and pass in the value at apply time.

[SHOW TERMINAL]

Here is the simplest possible variable declaration:

```hcl
variable "region" {
  type        = string
  description = "The AWS region to deploy into"
  default     = "us-east-1"
}
```

You reference it in your configuration like this:

```hcl
provider "aws" {
  region = var.region
}
```

Notice the `var.` prefix — that is how you always access a variable's value in Terraform.

[PAUSE]

### Type Constraints

Terraform supports a rich type system. You can specify `string`, `number`, `bool`, or complex types like `list`, `map`, `set`, `object`, and `tuple`.

```hcl
variable "instance_count" {
  type        = number
  description = "Number of EC2 instances to create"
  default     = 2
}

variable "allowed_ports" {
  type        = list(number)
  description = "List of ports to open in security group"
  default     = [80, 443]
}

variable "tags" {
  type        = map(string)
  description = "Tags to apply to all resources"
  default = {
    Environment = "dev"
    Project     = "demo"
  }
}
```

When Terraform reads your configuration it enforces the type. If you pass a string where a number is expected, Terraform will attempt a conversion — and if that fails, it will error out with a clear message.

[PAUSE]

### Variable Validation

You can add a `validation` block to enforce business rules on your input variables.

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be one of: dev, staging, prod."
  }
}
```

The `condition` must evaluate to `true` for the plan to proceed. If it evaluates to `false`, Terraform prints your `error_message` and stops.

[SHOW TERMINAL]

Let's test this. If I run:

```bash
terraform plan -var="environment=qa"
```

Terraform returns:

```
Error: Invalid value for variable

  on variables.tf line 1:
   1: variable "environment" {

environment must be one of: dev, staging, prod.
```

Clean, informative, and it prevents misconfiguration before any infrastructure is touched.

[PAUSE]

---

## Section 2: Sensitive Variables (5:30 – 8:00)

Some variables hold secrets — database passwords, API keys, tokens. Terraform's `sensitive` argument tells Terraform to redact these values from terminal output and state display.

```hcl
variable "db_password" {
  type        = string
  description = "Database master password"
  sensitive   = true
}
```

When you reference a sensitive variable, Terraform marks any output that depends on it as sensitive too.

```hcl
output "connection_string" {
  value     = "postgres://admin:${var.db_password}@${aws_db_instance.main.endpoint}/app"
  sensitive = true
}
```

[SHOW TERMINAL]

During `terraform apply`, sensitive values appear as `(sensitive value)` in the plan output:

```
  + db_password = (sensitive value)
```

**Important exam note**: Sensitive values are still stored in `terraform.tfstate` in plain text. Marking a variable sensitive only affects console output, not state file storage. This is why state file security matters — which we cover in Module 08.

[PAUSE]

---

## Section 3: Output Values (8:00 – 11:00)

Outputs let you extract information from your Terraform configuration after apply. They are how you share data between modules, surface useful IDs, and expose values to automation pipelines.

```hcl
output "instance_public_ip" {
  description = "The public IP address of the web server"
  value       = aws_instance.web.public_ip
}

output "instance_id" {
  description = "The EC2 instance ID"
  value       = aws_instance.web.id
}
```

[SHOW TERMINAL]

After `terraform apply` completes, Terraform prints all outputs:

```
Outputs:

instance_id        = "i-0abc123def456789"
instance_public_ip = "54.234.12.45"
```

You can also query outputs at any time with:

```bash
terraform output
terraform output instance_public_ip
terraform output -json
```

The `-json` flag is especially useful in CI/CD pipelines where a script needs to consume the value programmatically.

[PAUSE]

### Output Dependencies

Outputs also create implicit dependencies. If an output references a resource attribute, Terraform knows that resource must be created first. This is the same dependency graph mechanism that governs resource ordering.

### Using Outputs Across Modules

When you call a child module, you access its outputs using module syntax:

```hcl
module "network" {
  source = "./modules/network"
}

resource "aws_instance" "web" {
  subnet_id = module.network.public_subnet_id
}
```

We will cover module composition in depth in Module 09, but this pattern is the foundation.

[PAUSE]

---

## Section 4: Local Values (11:00 – 14:00)

Local values — declared with the `locals` block — are named expressions you define once and reference throughout the configuration. They reduce repetition and make complex expressions readable.

```hcl
locals {
  common_tags = {
    Project     = "web-app"
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = "platform-team"
  }

  name_prefix = "${var.project}-${var.environment}"
  is_prod     = var.environment == "prod"
}
```

You reference locals with the `local.` prefix:

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = local.is_prod ? "t3.medium" : "t3.micro"
  tags          = local.common_tags
}

resource "aws_s3_bucket" "assets" {
  bucket = "${local.name_prefix}-assets"
  tags   = local.common_tags
}
```

[PAUSE]

### Locals vs Variables

This is a common point of confusion. Here is the key distinction:

- **Input variables** (`variable`) — values supplied by the caller (user, CI pipeline, `.tfvars` file)
- **Local values** (`locals`) — computed inside the configuration from other values; the caller cannot override them directly

Use locals when you have an expression that appears in multiple places, or when you want to name a derived value for clarity. Use variables when you need the caller to be able to supply or override the value.

[PAUSE]

---

## Section 5: Variable Precedence (14:00 – 17:00)

Terraform loads variable values from multiple sources. When the same variable is defined in more than one place, Terraform uses a strict precedence order — lowest to highest:

1. Default value in the `variable` block
2. `terraform.tfvars` file (auto-loaded)
3. `terraform.tfvars.json` file (auto-loaded)
4. `*.auto.tfvars` and `*.auto.tfvars.json` files (auto-loaded, alphabetical order)
5. `-var-file` flag on the command line
6. `-var` flag on the command line
7. `TF_VAR_name` environment variables

[SHOW TERMINAL]

Let me walk through an example. Given this variable:

```hcl
variable "region" {
  type    = string
  default = "us-east-1"
}
```

And a `terraform.tfvars` file containing:

```hcl
region = "us-west-2"
```

And an environment variable set:

```bash
export TF_VAR_region="eu-west-1"
```

If I then run:

```bash
terraform plan -var="region=ap-southeast-1"
```

The `-var` flag wins — Terraform uses `ap-southeast-1`.

The environment variable `TF_VAR_region` would beat the `.tfvars` file but loses to the explicit `-var` flag.

[PAUSE]

### tfvars Files

A `.tfvars` file is simply key-value pairs:

```hcl
region           = "us-west-2"
instance_count   = 3
environment      = "staging"
allowed_ports    = [80, 443, 8080]
```

You can have environment-specific files and load them explicitly:

```bash
terraform plan -var-file="prod.tfvars"
terraform plan -var-file="staging.tfvars"
```

This pattern — one `.tfvars` file per environment — is extremely common in real-world Terraform projects.

[PAUSE]

### Environment Variables

For every input variable `foo`, Terraform reads the environment variable `TF_VAR_foo`. This is the standard way to pass secrets into Terraform in CI/CD pipelines without writing them to disk.

```bash
export TF_VAR_db_password="SuperSecretPassword123"
terraform apply
```

The shell variable is consumed by Terraform and the value never appears in your version-controlled files.

[PAUSE]

---

## Section 6: Putting It All Together (17:00 – 20:00)

Let's look at a complete, realistic example that ties all these concepts together.

```hcl
# variables.tf
variable "project" {
  type        = string
  description = "Project name used in resource naming"
}

variable "environment" {
  type        = string
  description = "Deployment environment"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Must be dev, staging, or prod."
  }
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "db_password" {
  type      = string
  sensitive = true
}
```

```hcl
# locals.tf
locals {
  name_prefix = "${var.project}-${var.environment}"
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}
```

```hcl
# outputs.tf
output "web_public_ip" {
  description = "Public IP of the web server"
  value       = aws_instance.web.public_ip
}

output "db_endpoint" {
  description = "Database connection endpoint"
  value       = aws_db_instance.main.endpoint
  sensitive   = true
}
```

```hcl
# prod.tfvars
project       = "ecommerce"
environment   = "prod"
instance_type = "t3.medium"
```

[SHOW TERMINAL]

To deploy to production:

```bash
terraform apply -var-file="prod.tfvars"
```

To pass the database password securely from the pipeline:

```bash
export TF_VAR_db_password="$SECRET_FROM_VAULT"
terraform apply -var-file="prod.tfvars"
```

[PAUSE]

---

## Summary and Exam Tips (20:00 – 22:00)

Let's recap what we covered:

- Input variables parameterize configurations; use `type`, `default`, `description`, `validation`, and `sensitive`
- Output values expose resource attributes after apply; access with `terraform output`
- Local values are named expressions for internal use; use `local.` prefix
- Variable precedence order: default → tfvars → auto.tfvars → `-var-file` → `-var` → `TF_VAR_`
- Sensitive variables are redacted from console output but stored in state in plain text

**For the Terraform Associate exam**, pay attention to:

- The exact precedence order — it appears on the exam
- The difference between `variable` and `locals` — locals cannot be overridden by the caller
- `sensitive = true` does NOT encrypt the state file
- `terraform output -json` for programmatic consumption
- `TF_VAR_` prefix is case-sensitive and matches the variable name exactly

[PAUSE]

---

## Closing (22:00 – 23:00)

Excellent work getting through Module 07. Variables, outputs, and locals are things you will use in every single Terraform project for the rest of your career. The patterns we covered today — especially `.tfvars` per environment and `TF_VAR_` in pipelines — are industry standard.

In the lab you will build a parameterized configuration that uses all of these features together. Take your time, read the error messages carefully, and pay close attention to the precedence exercise.

Module 08 moves us into Terraform State Management — one of the most critical topics for operating Terraform in a team environment.

See you there.

[END OF SCRIPT]
