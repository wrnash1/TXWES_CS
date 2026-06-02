# CIS-4337 Infrastructure Automation

## Reading Guide — Module 06: Data Sources and Terraform Functions

### Course Alignment: HashiCorp Terraform Associate 003

---

## Overview

This module covers data sources, built-in functions, for expressions, and dynamic blocks. These tools are used in every non-trivial Terraform configuration and appear throughout the Associate 003 exam.

---

## 1. Core Vocabulary

**Data Source**
A `data` block that performs a read-only query against a provider API to fetch attributes of existing infrastructure. Data sources do not create, update, or destroy resources. Deleting a `data` block has no effect on real infrastructure.

**Data Source Reference**
The syntax `data.<type>.<name>.<attribute>` used to access a specific attribute returned by a data source.

**For Expression**
An HCL expression that transforms a list or map into a new list or map by applying a transformation and optional filter to each element. Syntax: `[for item in collection : expression]` or `{for k, v in map : key => value}`.

**Dynamic Block**
A block that generates one or more repeated nested blocks within a resource based on a collection variable. Used when a resource argument accepts a variable number of nested blocks.

**terraform console**
An interactive REPL command that evaluates HCL expressions against the current state and configuration. Used for testing functions and expressions without modifying configuration files.

**cidrsubnet**
A built-in function that calculates a subnet CIDR block from a parent CIDR block, an additional bit count, and a subnet number.

**lookup**
A built-in function that retrieves a value from a map by key, with a fallback default value if the key is not present.

**jsonencode / jsondecode**
Functions that convert between HCL values and JSON strings. Commonly used for IAM policies and user data scripts.

---

## 2. Data Source Syntax and Common Patterns

### Basic Data Source

```hcl
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
```

Reference: `data.aws_ami.amazon_linux.id`

### VPC Lookup by Tag

```hcl
data "aws_vpc" "prod" {
  filter {
    name   = "tag:Environment"
    values = ["prod"]
  }
}
```

Reference: `data.aws_vpc.prod.id`, `data.aws_vpc.prod.cidr_block`

### Availability Zones

```hcl
data "aws_availability_zones" "available" {
  state = "available"
}
```

Reference: `data.aws_availability_zones.available.names[0]`

### IAM Policy Document

```hcl
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}
```

Reference: `data.aws_iam_policy_document.assume_role.json`

### Data Source with depends_on

```hcl
data "aws_vpc" "newly_created" {
  filter {
    name   = "tag:Name"
    values = [aws_vpc.main.tags.Name]
  }

  depends_on = [aws_vpc.main]
}
```

Use `depends_on` when a data source queries infrastructure that Terraform is creating in the same run.

---

## 3. Built-in Functions Reference

### String Functions

| Function | Example | Result |
|---|---|---|
| `upper(s)` | `upper("hello")` | `"HELLO"` |
| `lower(s)` | `lower("WORLD")` | `"world"` |
| `trimspace(s)` | `trimspace(" hi ")` | `"hi"` |
| `replace(s,old,new)` | `replace("a-b","-","_")` | `"a_b"` |
| `join(sep,list)` | `join(",",["a","b"])` | `"a,b"` |
| `split(sep,s)` | `split(",","a,b")` | `["a","b"]` |
| `format(fmt,...)` | `format("%s-%d","x",1)` | `"x-1"` |
| `substr(s,off,len)` | `substr("hello",0,3)` | `"hel"` |
| `startswith(s,pfx)` | `startswith("hello","he")` | `true` |

### Collection Functions

| Function | Example | Result |
|---|---|---|
| `length(coll)` | `length(["a","b"])` | `2` |
| `element(list,idx)` | `element(["a","b"],1)` | `"b"` |
| `flatten(lists)` | `flatten([["a"],["b"]])` | `["a","b"]` |
| `distinct(list)` | `distinct(["a","a","b"])` | `["a","b"]` |
| `merge(maps...)` | `merge({a=1},{b=2})` | `{a=1,b=2}` |
| `lookup(map,key,def)` | `lookup({a="x"},"a","d")` | `"x"` |
| `keys(map)` | `keys({a=1,b=2})` | `["a","b"]` |
| `values(map)` | `values({a=1,b=2})` | `[1,2]` |
| `toset(list)` | `toset(["a","a","b"])` | Set of `["a","b"]` |
| `contains(list,val)` | `contains(["a","b"],"a")` | `true` |

### Numeric Functions

| Function | Example | Result |
|---|---|---|
| `max(nums...)` | `max(3,1,5)` | `5` |
| `min(nums...)` | `min(3,1,5)` | `1` |
| `ceil(n)` | `ceil(4.1)` | `5` |
| `floor(n)` | `floor(4.9)` | `4` |
| `abs(n)` | `abs(-3)` | `3` |

### Network Functions

| Function | Signature | Example | Result |
|---|---|---|---|
| `cidrsubnet` | `(prefix, newbits, netnum)` | `cidrsubnet("10.0.0.0/16",8,1)` | `"10.0.1.0/24"` |
| `cidrhost` | `(prefix, hostnum)` | `cidrhost("10.0.1.0/24",10)` | `"10.0.1.10"` |
| `cidrnetmask` | `(prefix)` | `cidrnetmask("10.0.0.0/16")` | `"255.255.0.0"` |

### Encoding Functions

| Function | Example |
|---|---|
| `base64encode(s)` | `base64encode("hello")` |
| `base64decode(s)` | `base64decode("aGVsbG8=")` |
| `jsonencode(val)` | `jsonencode({key="value"})` |
| `jsondecode(s)` | `jsondecode("{\"key\":\"val\"}")` |

---

## 4. For Expressions

```hcl
# List transformation
variable "names" {
  type    = list(string)
  default = ["alice", "bob", "charlie"]
}

locals {
  upper_names = [for name in var.names : upper(name)]
  # Result: ["ALICE", "BOB", "CHARLIE"]

  long_names = [for name in var.names : name if length(name) > 4]
  # Result: ["alice", "charlie"]

  name_lengths = {for name in var.names : name => length(name)}
  # Result: {"alice"=5, "bob"=3, "charlie"=7}
}
```

---

## 5. Dynamic Blocks

```hcl
variable "security_rules" {
  type = list(object({
    port     = number
    protocol = string
    cidr     = string
  }))
  default = [
    { port = 80,  protocol = "tcp", cidr = "0.0.0.0/0" },
    { port = 443, protocol = "tcp", cidr = "0.0.0.0/0" },
    { port = 22,  protocol = "tcp", cidr = "10.0.0.0/8" }
  ]
}

resource "aws_security_group" "app" {
  name   = "app-sg"
  vpc_id = aws_vpc.main.id

  dynamic "ingress" {
    for_each = var.security_rules
    iterator = rule
    content {
      from_port   = rule.value.port
      to_port     = rule.value.port
      protocol    = rule.value.protocol
      cidr_blocks = [rule.value.cidr]
    }
  }
}
```

---

## 6. Required Reading

- Read the data sources overview at developer.hashicorp.com/terraform/language/data-sources
- Read the built-in functions reference at developer.hashicorp.com/terraform/language/functions
- Read the for expressions reference at developer.hashicorp.com/terraform/language/expressions/for
- Read the dynamic blocks reference at developer.hashicorp.com/terraform/language/expressions/dynamic-blocks

---

## 7. Terraform Associate 003 Exam Tips

**Tip 1.** Data sources use `data.<type>.<name>.<attribute>`, not `resource.<type>.<name>.<attribute>`. The exam tests this distinction.

**Tip 2.** Removing a `data` block never destroys real infrastructure. Only removing a `resource` block causes a planned destroy.

**Tip 3.** `lookup(map, key, default)` is the safe map lookup function. Plain bracket notation `map["key"]` raises an error if the key is absent.

**Tip 4.** `cidrsubnet("10.0.0.0/16", 8, 1)` produces `"10.0.1.0/24"`. The second argument is the number of additional bits for the subnet prefix. The third is the subnet number. Know this function cold.

**Tip 5.** `terraform console` is the interactive expression evaluator. It is the correct tool for testing functions. The exam asks what `terraform console` is used for.

**Tip 6.** `dynamic` blocks use `for_each` (not `count`) to iterate. The `content` block defines the nested block body. The iterator defaults to the block label name but can be overridden with `iterator = <name>`.

**Tip 7.** `jsonencode` converts an HCL value to a JSON string. It is used for IAM policy arguments that expect a JSON string (`policy = jsonencode({...})`).

**Tip 8.** The `depends_on` meta-argument is valid inside `data` blocks as well as `resource` blocks. Use it when a data source must wait for a resource to be created in the same configuration.

---

## 8. Study Checklist

- [ ] Write a `data "aws_ami"` block with a filter from memory.
- [ ] Reference a data source attribute in a resource block using correct syntax.
- [ ] Use `lookup`, `length`, `element`, `merge`, `join`, `split`, `cidrsubnet`, and `jsonencode` in `terraform console`.
- [ ] Write a for expression that transforms a list of strings to uppercase.
- [ ] Write a `dynamic "ingress"` block that generates security group rules from a list variable.
- [ ] Explain when to use `depends_on` inside a `data` block.
- [ ] Read all four required documentation pages.
- [ ] Complete the Module 06 lab, quiz, and discussion post.

---

Module 06 Reading Guide — CIS-4337 Infrastructure Automation — Texas Wesleyan University
