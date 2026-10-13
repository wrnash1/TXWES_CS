# Video Script: Module 15 — Advanced Terraform Patterns

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Segment 1: Introduction (Lines 1–18)

Welcome back to CIS-4337. This is Module 15: Advanced Terraform Patterns.

In the earlier modules you learned the fundamentals: resources, providers, modules, state, and backends. Now we are going to go deeper into the language features that separate a Terraform practitioner from a Terraform expert.

These patterns appear frequently in the Terraform Associate 003 exam and are essential for writing production-quality configurations that are maintainable and DRY — Don't Repeat Yourself.

In this module we will cover:

- Dynamic blocks for generating nested configuration blocks programmatically
- `for_each` and `count` meta-arguments for creating multiple resource instances
- Conditional expressions for environment-specific configuration
- `moved` blocks for safe state refactoring
- `terraform import` for bringing existing resources under Terraform management
- Practical refactoring patterns

Let us start with dynamic blocks, which are one of the most misunderstood features in Terraform.

---

## Segment 2: Dynamic Blocks (Lines 19–52)

A dynamic block generates nested configuration blocks inside a resource based on a collection value. It solves a specific problem: some resource types have repeatable nested blocks — like `ingress` rules in a security group — and you need to generate a variable number of them based on input data.

Without dynamic blocks, you would have to hardcode each nested block separately. If you need three ingress rules, you write three `ingress {}` blocks. If you need ten, you write ten. This is not maintainable.

With a dynamic block, you provide a list or map of values and Terraform generates one block for each element.

The syntax is:

```hcl
resource "aws_security_group" "app" {
  name   = "app-sg"
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.ingress_rules

    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
      description = ingress.value.description
    }
  }
}
```

The variable `var.ingress_rules` is a list of objects. Each object in the list becomes one `ingress` block. Inside the `content` block, you reference the current element using `ingress.value` — that is, the iterator name (which matches the block type) followed by `.value`.

The iterator variable name defaults to the block type (`ingress` in this case), but you can override it with an `iterator` argument if the default name would conflict with something else in scope.

Dynamic blocks work for any repeatable nested block in any resource type. Common examples include `ingress` and `egress` in security groups, `rule` blocks in WAF configurations, `lifecycle_rule` blocks in S3 buckets, and `setting` blocks in Elastic Beanstalk configurations.

Do not overuse dynamic blocks. When the set of blocks is fixed and known, explicit blocks are more readable. Use dynamic blocks when the number of blocks is determined by input data.

---

## Segment 3: for_each and count (Lines 53–92)

`for_each` and `count` are meta-arguments that create multiple instances of a resource or module from a single block. They are the correct way to avoid copy-pasting resource blocks.

`count` creates N instances of a resource identified by an integer index. It is the simpler of the two but has a significant limitation: if you remove an element from the middle of the list, all resources with higher indices are renamed, which causes Terraform to destroy and recreate them.

```hcl
resource "aws_subnet" "public" {
  count             = length(var.public_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.public_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
}
```

`for_each` creates one instance per element in a map or set of strings, identified by a string key. It is the preferred approach for most use cases because adding or removing elements does not affect other instances.

```hcl
resource "aws_subnet" "public" {
  for_each = var.subnets

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value.cidr_block
  availability_zone = each.value.az

  tags = {
    Name = each.key
  }
}
```

With `for_each`, each instance is addressed as `aws_subnet.public["subnet-a"]` using the map key. You can reference the current key with `each.key` and the current value with `each.value`. If your collection is a set of strings, `each.key` and `each.value` are the same string.

When to use `count` versus `for_each`:

- Use `count` when you need a simple list of identical resources numbered sequentially — for example, three identical worker nodes where order matters
- Use `for_each` when resources have meaningful names or when you might need to add or remove individual instances without affecting others

A critical exam note: you cannot use both `count` and `for_each` on the same resource block. They are mutually exclusive.

`for_each` also works on modules. You can instantiate a module multiple times with different configurations by passing a map to `for_each` on the module block.

---

## Segment 4: Conditional Expressions (Lines 93–120)

Conditional expressions allow you to make configuration decisions based on variable values. The syntax is the ternary operator familiar from many programming languages: `condition ? true_value : false_value`.

The most common use is environment-specific sizing:

```hcl
resource "aws_instance" "app" {
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
  ami           = data.aws_ami.ubuntu.id
}
```

You can use conditionals in resource arguments, locals, and output values. They work with any type that Terraform supports.

A powerful pattern is conditional resource creation combined with `count`:

```hcl
resource "aws_cloudwatch_log_group" "app" {
  count = var.enable_logging ? 1 : 0
  name  = "/app/logs"
}
```

When `var.enable_logging` is true, count is 1 and the resource is created. When false, count is 0 and the resource does not exist. This is the standard pattern for optional resources in Terraform.

You can reference this resource in other places with a conditional to handle the case where count is 0:

```hcl
log_group_arn = var.enable_logging ? aws_cloudwatch_log_group.app[0].arn : ""
```

When using `for_each` for conditional resources, the pattern uses an empty map or a single-element map:

```hcl
resource "aws_cloudwatch_log_group" "app" {
  for_each = var.enable_logging ? { "enabled" = true } : {}
  name     = "/app/logs"
}
```

Conditionals can also appear in `locals` blocks to compute derived values:

```hcl
locals {
  db_instance_class = var.environment == "prod" ? "db.r6g.large" : "db.t3.micro"
  backup_retention  = var.environment == "prod" ? 7 : 1
}
```

Locals that compute conditional values keep your resource blocks clean — the logic lives in one place and resources just reference `local.db_instance_class`.

---

## Segment 5: Moved Blocks (Lines 121–150)

The `moved` block is a Terraform 1.1 feature that allows you to rename or move resources in your configuration without destroying and recreating them.

Before `moved` blocks existed, renaming a resource meant Terraform would plan to destroy the old resource and create a new one. This was dangerous for production resources — accidentally recreating a database because you renamed it in code was a serious operational risk.

With `moved` blocks, you tell Terraform explicitly that a resource has been renamed or moved to a module. Terraform updates the state file to reflect the new address without touching the underlying infrastructure.

The syntax is:

```hcl
moved {
  from = aws_s3_bucket.old_name
  to   = aws_s3_bucket.new_name
}
```

When you run `terraform plan` with a `moved` block, Terraform shows the move as a no-op operation in the plan output rather than as a destroy/create pair. The resource is not modified — only its state address changes.

`moved` blocks also handle moving resources into or out of modules:

```hcl
moved {
  from = aws_s3_bucket.my_bucket
  to   = module.storage.aws_s3_bucket.bucket
}
```

After the move is applied and the team has run `terraform apply`, you can delete the `moved` block from the configuration. Some teams choose to keep `moved` blocks permanently as documentation of the refactoring history.

`moved` blocks can be placed anywhere in your configuration — in the root module, in child modules, or in separate files. A common pattern is to maintain a `moves.tf` file that accumulates refactoring history.

---

## Segment 6: Importing Existing Resources (Lines 151–178)

`terraform import` brings existing cloud resources under Terraform management without destroying and recreating them. This is the essential tool for adopting Terraform in environments that already have manually provisioned infrastructure.

The classic workflow before Terraform 1.5 was:

1. Write the Terraform resource block for the existing resource
2. Run `terraform import <resource_address> <resource_id>` to read the current state of the resource into the state file
3. Run `terraform plan` and compare the configuration to the imported state
4. Adjust the configuration until `terraform plan` shows no changes

Terraform 1.5 introduced the `import` block, which integrates import into the standard plan/apply workflow:

```hcl
import {
  id = "i-0abc123def456789"
  to = aws_instance.existing_app
}

resource "aws_instance" "existing_app" {
  ami           = "ami-0123456789abcdef0"
  instance_type = "t3.medium"
}
```

With an `import` block in your configuration, `terraform plan` generates an import plan alongside any resource changes. `terraform apply` performs both the import and any changes in a single operation.

Terraform 1.5 also introduced `terraform plan -generate-config-out=generated.tf`. This command generates a starting-point Terraform configuration for an imported resource. The generated configuration is not always perfect — it may include computed attributes that cannot be specified in configuration — but it dramatically reduces the time required to write the initial resource block.

The resource ID format required for import differs by resource type. For AWS EC2 instances it is the instance ID. For S3 buckets it is the bucket name. For VPCs it is the VPC ID. Always check the provider documentation for the import ID format before running import.

---

## Segment 7: Refactoring Patterns (Lines 179–210)

Refactoring Terraform configurations is a regular maintenance activity. Modules become too large, resource names change, and configuration patterns improve over time. These are the most common refactoring scenarios.

The first is extracting a module. When a section of your root configuration grows to more than 20–30 resources, it is time to extract those resources into a reusable module. The process:

1. Create a new module directory with `main.tf`, `variables.tf`, and `outputs.tf`
2. Move the resource blocks into `main.tf`, replacing hardcoded values with variables
3. Add `moved` blocks from the old root resource addresses to the new module resource addresses
4. Call the module from the root configuration with the appropriate variable values
5. Run `terraform plan` to verify only moves are planned (no creates or destroys)
6. Apply the refactoring

The second pattern is splitting a workspace. When a single workspace manages too many resources, deployments become slow and the blast radius of an error is too large. Splitting into separate workspaces requires:

1. Identifying a logical boundary (e.g., network infrastructure vs. application infrastructure)
2. Moving state for the relevant resources to the new workspace using `terraform state mv`
3. Using data sources in the new workspace to reference outputs from the original workspace
4. Adding `removed` blocks in the original workspace to stop managing the moved resources

The `removed` block (introduced in Terraform 1.7) is the complement to `moved`. It tells Terraform to stop managing a resource without destroying it. This is useful during workspace splits.

Always run `terraform plan` after every refactoring step and verify the plan shows only moves — never unexpected destroys or creates.

In the next and final module we will review all Terraform Associate 003 exam objectives and work through practice questions.

See you there.

---

End of Module 15 Video Script
