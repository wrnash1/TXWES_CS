# Reading Guide: Module 15 — Advanced Terraform Patterns

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Overview

This reading guide covers the advanced HCL language features and operational patterns that experienced Terraform practitioners use daily. Understanding dynamic blocks, for_each, count, conditionals, moved blocks, and import is required for the Terraform Associate 003 exam and for maintaining production Terraform codebases.

**Estimated reading time:** 65–80 minutes

---

## Section 1: Dynamic Blocks

### 1.1 The Problem Dynamic Blocks Solve

Some Terraform resource types use nested blocks rather than arguments to configure repeatable settings. AWS security groups use `ingress {}` and `egress {}` blocks. Azure Network Security Groups use `security_rule {}` blocks. AWS WAF uses `rule {}` blocks.

When the number of these nested blocks is fixed, writing them explicitly is fine. When the number depends on input data — when a security group needs a variable number of rules based on the environment — explicit blocks cannot handle the variation. Dynamic blocks are the solution.

### 1.2 Dynamic Block Structure

```hcl
dynamic "<block_type>" {
  for_each = <collection>
  iterator = <optional_iterator_name>

  content {
    <argument> = <iterator_name>.value.<field>
  }
}
```

The `for_each` argument must be a map or a set/list. Each element in the collection generates one nested block. The `content` block defines what each generated block contains, using the iterator variable to access the current element.

### 1.3 Iterator Naming

The default iterator variable name is the same as the block type. In a `dynamic "ingress"` block, the iterator is `ingress`. If this name conflicts with something else in scope, use the `iterator` argument:

```hcl
dynamic "ingress" {
  for_each = var.ingress_rules
  iterator = rule

  content {
    from_port   = rule.value.from_port
    to_port     = rule.value.to_port
    protocol    = rule.value.protocol
    cidr_blocks = rule.value.cidr_blocks
  }
}
```

### 1.4 Nesting Dynamic Blocks

Dynamic blocks can be nested inside other dynamic blocks when the data structure requires it. However, deeply nested dynamic blocks become difficult to read and maintain. If you find yourself nesting dynamic blocks more than two levels deep, consider restructuring your data model.

### 1.5 When Not to Use Dynamic Blocks

Dynamic blocks are not appropriate when:

- The set of nested blocks is fixed and known at configuration write time — explicit blocks are clearer
- You are tempted to use them just to reduce lines of code in a situation where the explicit version is more readable
- The collection is large and the generated configuration would be unwieldy

---

## Section 2: for_each Meta-Argument

### 2.1 for_each with Maps

When `for_each` receives a map, each resource instance is identified by the map key. Inside the resource, `each.key` is the current key and `each.value` is the corresponding value.

```hcl
variable "subnets" {
  type = map(object({
    cidr_block        = string
    availability_zone = string
    public            = bool
  }))

  default = {
    "subnet-a" = {
      cidr_block        = "10.0.1.0/24"
      availability_zone = "us-east-2a"
      public            = true
    }
    "subnet-b" = {
      cidr_block        = "10.0.2.0/24"
      availability_zone = "us-east-2b"
      public            = false
    }
  }
}

resource "aws_subnet" "main" {
  for_each = var.subnets

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value.cidr_block
  availability_zone = each.value.availability_zone

  map_public_ip_on_launch = each.value.public

  tags = {
    Name = each.key
  }
}
```

Each subnet instance is addressed as `aws_subnet.main["subnet-a"]` and `aws_subnet.main["subnet-b"]`. Removing `"subnet-b"` from the map destroys only that subnet, leaving `"subnet-a"` unchanged.

### 2.2 for_each with Sets

When `for_each` receives a set of strings, each resource instance is identified by the string value, and `each.key == each.value`.

```hcl
variable "allowed_regions" {
  type    = set(string)
  default = ["us-east-2", "us-west-2"]
}

resource "aws_s3_bucket" "regional" {
  for_each = var.allowed_regions
  bucket   = "my-app-${each.value}"
  provider = aws # Would need aliased providers for real multi-region
}
```

### 2.3 Converting Lists to Sets for for_each

`for_each` does not accept lists directly — only maps and sets. If you have a list and want to use `for_each`, convert it with `toset()`:

```hcl
resource "aws_iam_user" "team" {
  for_each = toset(var.team_members)
  name     = each.value
}
```

This works when the list elements are unique. If the list may contain duplicates, `toset()` silently deduplicates — make sure this is the desired behavior.

### 2.4 for_each on Modules

`for_each` can be applied to module blocks to instantiate a module multiple times:

```hcl
module "environment" {
  for_each = var.environments

  source = "./modules/environment"

  name       = each.key
  cidr_block = each.value.cidr_block
  region     = each.value.region
}
```

Each module instance is addressed as `module.environment["dev"]`, `module.environment["staging"]`, etc.

---

## Section 3: count Meta-Argument

### 3.1 count Basics

`count` creates integer-indexed instances of a resource. It accepts any expression that evaluates to a non-negative integer.

```hcl
resource "aws_instance" "worker" {
  count         = var.worker_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "worker-${count.index}"
  }
}
```

Instances are addressed as `aws_instance.worker[0]`, `aws_instance.worker[1]`, etc.

### 3.2 The count Index Problem

The primary limitation of `count` is that indices are positional. If you have three worker instances at indices 0, 1, 2 and you remove the worker at position 1, Terraform renumbers the remaining workers. What was `worker[2]` becomes `worker[1]`. Terraform sees this as destroying and recreating the resource because its address changed.

This is safe for truly stateless, identical resources. It is dangerous for resources with state — databases, storage volumes, or any resource where the identity matters.

Rule of thumb: use `count` for resources where losing any specific instance is acceptable. Use `for_each` when each instance has a meaningful identity.

### 3.3 count for Optional Resources

The most robust use of `count` is the optional resource pattern:

```hcl
resource "aws_cloudwatch_metric_alarm" "cpu_high" {
  count = var.enable_monitoring ? 1 : 0

  alarm_name  = "cpu-high"
  metric_name = "CPUUtilization"
  threshold   = 80
}
```

When `var.enable_monitoring` is `false`, count is 0 and the alarm is not created. When `true`, count is 1 and the alarm exists. Referencing the resource elsewhere requires `aws_cloudwatch_metric_alarm.cpu_high[0]` when it exists.

---

## Section 4: Conditional Expressions

### 4.1 Ternary Syntax

The conditional expression syntax is `condition ? value_if_true : value_if_false`. The condition must evaluate to a boolean. Both branches must produce the same type — Terraform will raise an error if the types are incompatible.

```hcl
variable "is_production" {
  type    = bool
  default = false
}

locals {
  instance_type    = var.is_production ? "t3.large" : "t3.micro"
  retention_days   = var.is_production ? 90 : 7
  enable_multi_az  = var.is_production ? true : false
}
```

### 4.2 Conditionals in Resource Arguments

Conditionals can appear directly in resource arguments:

```hcl
resource "aws_db_instance" "main" {
  instance_class     = var.environment == "prod" ? "db.r6g.large" : "db.t3.micro"
  multi_az           = var.environment == "prod"
  deletion_protection = var.environment == "prod"
  backup_retention_period = var.environment == "prod" ? 7 : 1
}
```

### 4.3 Null Conditionals

Sometimes a conditional should produce `null` to omit an optional argument entirely:

```hcl
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  iam_instance_profile = var.enable_ssm ? aws_iam_instance_profile.ssm[0].name : null
}
```

When an argument is set to `null`, Terraform omits it from the API call, and the cloud provider uses its default value for that attribute.

---

## Section 5: Moved Blocks

### 5.1 Why moved Blocks Exist

Before moved blocks, any refactoring that changed a resource's address in the configuration caused Terraform to plan a destroy of the old address and create at the new address. For production resources — databases, load balancers, S3 buckets with data — this was a serious operational risk.

The `moved` block, introduced in Terraform 1.1, tells Terraform that a resource previously at one address is now at another address in the same state. No infrastructure changes occur.

### 5.2 Moving a Resource to a New Name

```hcl
moved {
  from = aws_s3_bucket.old_name
  to   = aws_s3_bucket.new_name
}

resource "aws_s3_bucket" "new_name" {
  bucket = "my-application-data"
}
```

After `terraform apply`, the state file records `aws_s3_bucket.new_name` at the same ARN as the old resource. The S3 bucket itself is unchanged.

### 5.3 Moving a Resource into a Module

```hcl
moved {
  from = aws_s3_bucket.app_data
  to   = module.storage.aws_s3_bucket.main
}
```

### 5.4 moved Block Lifecycle

After everyone on the team has applied the configuration containing the `moved` block, you can remove the block. Some teams keep `moved` blocks indefinitely as a refactoring audit trail. Others remove them after a sprint cycle. There is no functional difference — Terraform ignores `moved` blocks for states that have already been updated.

---

## Section 6: Importing Existing Resources

### 6.1 The CLI Import Command

The original import mechanism uses the CLI:

```bash
terraform import aws_s3_bucket.existing my-existing-bucket-name
```

This reads the current state of the S3 bucket from AWS and writes it to the state file under the address `aws_s3_bucket.existing`. The resource block must already exist in your configuration before running import.

After import, run `terraform plan`. The plan will almost always show differences because the default configuration values differ from the actual resource attributes. You must adjust your configuration until the plan shows no changes.

### 6.2 The import Block (Terraform 1.5+)

```hcl
import {
  id = "my-existing-bucket-name"
  to = aws_s3_bucket.existing
}

resource "aws_s3_bucket" "existing" {
  bucket = "my-existing-bucket-name"
}
```

The `import` block integrates the import into the plan/apply cycle. The plan shows the import action, and apply performs it. This is safer than the CLI command because the import is visible in the plan review.

### 6.3 Configuration Generation

Terraform 1.5+ can generate a starting-point configuration for imported resources:

```bash
terraform plan -generate-config-out=generated.tf
```

This produces a `generated.tf` file with a resource block populated from the actual resource attributes. Review and clean up the generated configuration — remove computed-only attributes, add variables where appropriate, and ensure the file follows your team's style conventions.

### 6.4 Import ID Formats

Every resource type has a specific import ID format. Examples:

| Resource | Import ID Format |
|----------|-----------------|
| `aws_instance` | EC2 instance ID: `i-0abc123def456789` |
| `aws_s3_bucket` | Bucket name: `my-bucket-name` |
| `aws_vpc` | VPC ID: `vpc-0abc123def456789` |
| `aws_iam_role` | Role name: `my-role-name` |
| `azurerm_resource_group` | Full resource ID: `/subscriptions/.../resourceGroups/name` |
| `google_compute_instance` | Project/zone/name: `project/zone/instance-name` |

Always check the "Import" section of the provider documentation for the specific resource type.

---

## Section 7: Refactoring Patterns

### 7.1 Extracting a Module

When a root configuration becomes too large, extract a logical group of resources into a child module:

1. Identify a cohesive group of resources (e.g., all networking resources)
2. Create `modules/networking/main.tf`, `variables.tf`, `outputs.tf`
3. Move the resource blocks to `modules/networking/main.tf`
4. Add `moved` blocks mapping old root addresses to new module addresses
5. Call the module from the root with the `module "networking" {}` block
6. Run `terraform plan` and verify only `move` operations are shown
7. Apply and then optionally remove the `moved` blocks

### 7.2 Splitting Workspaces

When a workspace manages too many resources, split it at a logical boundary:

1. Create a new Terraform workspace (new directory with its own backend configuration)
2. Use `terraform state mv` to move specific resources to the new workspace's state
3. In the new workspace, write resource blocks and mark them as imported rather than new
4. In the old workspace, use `removed` blocks or `terraform state rm` to stop managing the moved resources
5. Add `data` sources in the new workspace to reference outputs from the old workspace

### 7.3 Refactoring count to for_each

When resources were created with `count` and you want to switch to `for_each`:

```hcl
moved {
  from = aws_subnet.public[0]
  to   = aws_subnet.public["subnet-a"]
}

moved {
  from = aws_subnet.public[1]
  to   = aws_subnet.public["subnet-b"]
}
```

Each `moved` block maps one count-indexed instance to one for_each-keyed instance. After applying all moves, change the resource block from `count` to `for_each`. The subnets are unchanged in the cloud.

---

## Key Terms

- **Dynamic block**: generates repeatable nested configuration blocks from a collection
- **for_each**: meta-argument creating one resource instance per element in a map or set
- **count**: meta-argument creating integer-indexed resource instances
- **each.key / each.value**: references to the current element's key and value within a for_each block
- **count.index**: the zero-based integer index within a count block
- **Conditional expression**: ternary operator `condition ? true_val : false_val`
- **moved block**: declares that a resource's address has changed without modifying infrastructure
- **import block**: integrates resource import into the plan/apply cycle (Terraform 1.5+)
- **terraform import (CLI)**: command to read existing resource state into the state file
- **-generate-config-out**: plan flag that writes a generated resource configuration for imported resources

---

## Review Questions

1. What is the default iterator variable name in a dynamic block, and how do you override it?

2. Explain the count index problem. In what scenario is removing an element from a count-based resource list dangerous?

3. What is the difference between `for_each` receiving a map versus a set of strings in terms of how each.key and each.value behave?

4. What did teams have to do before `moved` blocks existed when they needed to rename a Terraform resource? What was the risk?

5. Describe the two import mechanisms available in Terraform 1.5+. What advantage does the `import` block have over the `terraform import` CLI command?

6. Write a conditional expression that evaluates to `"db.r6g.large"` when `var.environment == "prod"` and `"db.t3.micro"` otherwise.

---

## Supplemental Resources

**1. Terraform Dynamic Blocks**
<https://developer.hashicorp.com/terraform/language/expressions/dynamic-blocks>
The official HashiCorp reference for dynamic blocks, covering the `for_each`, `iterator`, and `content` arguments in detail. Includes guidance on when dynamic blocks are appropriate versus explicit nested blocks, how to nest dynamic blocks for complex resource types, and the performance and readability trade-offs of generating large numbers of nested blocks programmatically.

**2. Terraform Resource Addressing: count and for_each**
<https://developer.hashicorp.com/terraform/language/meta-arguments/for_each>
Comprehensive documentation for the `for_each` meta-argument including valid input types (maps and sets), the `each.key` and `each.value` references, how `for_each` instances are addressed in state and in cross-resource references, and the relationship between `for_each` on resource blocks versus `for_each` on module blocks. Covers the `toset()` conversion pattern and the behavior of removing keys from the collection.

**3. Terraform Refactoring: moved Blocks and Import**
<https://developer.hashicorp.com/terraform/language/modules/develop/refactoring>
The official guide to non-destructive Terraform refactoring using `moved` blocks, including moving resources between modules, renaming resources, and migrating from `count` to `for_each`. Also covers when moved blocks can be safely removed after all state files have been updated. Pairs with the `import` block documentation for a complete picture of bringing existing infrastructure under Terraform management without downtime.

---

End of Module 15 Reading Guide
