# CIS-4337 Infrastructure Automation

## Module 03: HCL Syntax — Providers, Resources, and Variables

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337. I am Professor Nash. In the first two modules we established what IaC is and how the Terraform workflow operates. In this module we go deep into the language itself: HashiCorp Configuration Language, or HCL.

By the end of this video you will understand every major HCL block type — `terraform`, `provider`, `resource`, `variable`, `output`, and `locals` — and how they work together. You will write a complete `main.tf` with an AWS provider, variable declarations, and an EC2 instance resource. You will also understand resource meta-arguments: `depends_on`, `count`, `for_each`, `provider`, and `lifecycle`.

HCL syntax questions appear throughout the Terraform Associate 003 exam. This module is foundational.

---

## Section 2: HCL Fundamentals — 1:30–4:30

HCL is a declarative, human-readable configuration language. Every Terraform configuration is a set of HCL blocks. A block has a type, optional labels, and a body enclosed in curly braces.

**[SHOW CODE]**

```hcl
block_type "label_one" "label_two" {
  argument_name = argument_value
}
```

For example, a resource block:

**[SHOW CODE]**

```hcl
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-2024"
}
```

Here, `resource` is the block type, `aws_s3_bucket` is the resource type (the first label), and `my_bucket` is the local name (the second label). Together, `aws_s3_bucket.my_bucket` is the address of this resource within the configuration.

HCL supports comments:

**[SHOW CODE]**

```hcl
# Single-line comment
// Also a single-line comment

/*
  Multi-line comment
*/
```

HCL is case-sensitive. `Region` and `region` are different argument names.

---

## Section 3: The terraform Block — 4:30–6:30

The `terraform` block configures Terraform's own behavior: the minimum required CLI version and the providers the configuration depends on.

**[SHOW CODE]**

```hcl
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

`required_version` prevents the configuration from running on an incompatible Terraform version. This protects against subtle behavior differences between versions.

`required_providers` declares each provider the configuration uses with its registry source path and version constraint. The source format is `<namespace>/<type>`. For HashiCorp-maintained providers, the namespace is `hashicorp`. For community providers, it might be the author's username or organization.

---

## Section 4: The provider Block — 6:30–9:00

The `provider` block configures a specific provider instance. It supplies authentication credentials, regional settings, and other platform-specific options.

**[SHOW CODE]**

```hcl
provider "aws" {
  region = "us-east-1"
}
```

Provider credentials should never be hardcoded in `.tf` files. Instead, use environment variables, IAM roles, or a credentials file. For AWS, the provider reads the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables automatically.

You can define multiple configurations of the same provider using the `alias` argument:

**[SHOW CODE]**

```hcl
provider "aws" {
  region = "us-east-1"
  alias  = "primary"
}

provider "aws" {
  region = "us-west-2"
  alias  = "secondary"
}
```

A resource uses a non-default provider configuration by specifying `provider = aws.secondary` in its block. This is the multi-region pattern and is tested on the exam.

---

## Section 5: The resource Block — 9:00–13:00

The `resource` block is the core building block of every Terraform configuration. It declares a real infrastructure object to be managed.

**[SHOW CODE]**

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  tags = {
    Name        = "web-server"
    Environment = var.environment
  }
}
```

The resource type `aws_instance` tells Terraform which provider resource type to manage. The local name `web` is used to reference this resource elsewhere in the configuration as `aws_instance.web`.

Notice that `instance_type` and `environment` use variable references. We will cover variables next.

### Resource Meta-Arguments

Meta-arguments are special arguments accepted by all resource types, regardless of provider. They control Terraform's behavior toward the resource rather than the resource's own configuration.

**`depends_on`** — Creates an explicit dependency when no implicit reference exists:

**[SHOW CODE]**

```hcl
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  depends_on = [aws_iam_role_policy_attachment.app_policy]
}
```

**`count`** — Creates multiple instances of the same resource:

**[SHOW CODE]**

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}
```

**`for_each`** — Creates one instance per item in a map or set:

**[SHOW CODE]**

```hcl
resource "aws_instance" "servers" {
  for_each      = toset(["web", "app", "db"])
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = each.value
  }
}
```

**`lifecycle`** — Controls replacement and deletion behavior:

**[SHOW CODE]**

```hcl
resource "aws_db_instance" "primary" {
  # ... other arguments ...

  lifecycle {
    prevent_destroy       = true
    create_before_destroy = true
    ignore_changes        = [password]
  }
}
```

- `prevent_destroy = true` blocks deletion even on `terraform destroy`.
- `create_before_destroy = true` creates the replacement resource before deleting the old one.
- `ignore_changes` tells Terraform to ignore changes to specific attributes that may be managed outside Terraform.

---

## Section 6: The variable Block — 13:00–16:30

Variables parameterize configurations, enabling the same code to deploy to different environments with different values.

**[SHOW CODE]**

```hcl
variable "instance_type" {
  description = "EC2 instance type for web servers"
  type        = string
  default     = "t3.micro"
}

variable "environment" {
  description = "Deployment environment"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging, or prod."
  }
}

variable "allowed_ports" {
  description = "List of ports to allow in the security group"
  type        = list(number)
  default     = [80, 443]
}
```

Variable types include `string`, `number`, `bool`, `list(<type>)`, `set(<type>)`, `map(<type>)`, `object({...})`, and `tuple([...])`. The exam tests type declarations frequently.

Variables are referenced as `var.<name>`:

**[SHOW CODE]**

```hcl
resource "aws_instance" "web" {
  instance_type = var.instance_type
}
```

Variable values are supplied through, in order of precedence from lowest to highest:

1. Default value in the variable block.
2. `terraform.tfvars` or `*.auto.tfvars` files.
3. `-var` flag on the CLI: `terraform apply -var="environment=prod"`.
4. `-var-file` flag on the CLI.
5. Environment variables named `TF_VAR_<name>`.

---

## Section 7: The output Block — 16:30–18:30

Output blocks expose values from a configuration after apply. They are used to display information to the operator or to pass values between modules.

**[SHOW CODE]**

```hcl
output "instance_public_ip" {
  description = "Public IP address of the web server"
  value       = aws_instance.web.public_ip
}

output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.web.id
  sensitive   = false
}
```

Mark outputs containing sensitive data with `sensitive = true` to prevent them from being displayed in CLI output:

**[SHOW CODE]**

```hcl
output "db_password" {
  value     = aws_db_instance.primary.password
  sensitive = true
}
```

---

## Section 8: Local Values — 18:30–20:00

`locals` blocks define computed or reused values within a configuration to avoid repetition:

**[SHOW CODE]**

```hcl
locals {
  common_tags = {
    Project     = "web-app"
    Environment = var.environment
    ManagedBy   = "terraform"
  }

  instance_name = "web-${var.environment}-01"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  tags = merge(local.common_tags, {
    Name = local.instance_name
  })
}
```

Local values are referenced as `local.<name>`. They cannot be overridden from outside the module — they are internal computed values, not inputs.

---

## Section 9: Putting It All Together — 20:00–22:00

Let me show you a complete, minimal `main.tf` that incorporates everything we covered: terraform block, provider, variables, a resource, and an output.

**[SHOW CODE]**

```hcl
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name      = "web-server"
    ManagedBy = "terraform"
  }
}

output "public_ip" {
  description = "Public IP of the web server"
  value       = aws_instance.web.public_ip
}
```

This is the pattern you will expand in the Module 03 lab and the Module 10 AWS lab.

---

## Section 10: Closing — 22:00–23:00

Let me recap.

HCL uses blocks with types and labels. The core block types are `terraform`, `provider`, `resource`, `variable`, `output`, and `locals`.

The `terraform` block declares required versions and providers. The `provider` block configures authentication and region. The `resource` block declares the infrastructure to manage. Variables parameterize the configuration. Outputs expose values after apply. Locals define reusable internal expressions.

Meta-arguments — `depends_on`, `count`, `for_each`, `lifecycle` — apply to all resource types.

In Module 04 we cover Terraform state in depth: how the state file works, remote backends, and state management commands. Complete the reading guide, lab, quiz, and discussion first.

See you in Module 04.

---

End of Script — Module 03
