# CIS-4337 Infrastructure Automation

## Module 06: Data Sources and Terraform Functions

### Video Script — Estimated Runtime: 20–24 Minutes

---

## Section 1: Introduction — 0:00–1:30

Welcome back to CIS-4337. I am Professor Nash. In this module we cover two powerful capabilities that every production Terraform configuration uses: data sources and built-in functions.

By the end of this video you will be able to write `data` blocks to query existing infrastructure, understand how data source results are referenced, use the most important Terraform built-in functions, and use `terraform console` to test expressions interactively.

Data sources and functions appear throughout the Terraform Associate 003 exam, particularly in Domain 5 (Interact with Terraform Modules) and Domain 6 (Use the Core Terraform Workflow).

---

## Section 2: What Is a Data Source — 1:30–5:30

A data source allows Terraform to query external information and use it in your configuration. Unlike resources, data sources are read-only. They do not create, modify, or destroy anything.

Common use cases include:

- Finding the latest Amazon Machine Image (AMI) for a given filter criteria.
- Looking up an existing VPC by its tags so resources can be placed inside it.
- Reading an IAM policy document to attach to a role.
- Fetching an existing Route 53 zone ID for DNS record creation.

The block type is `data`. Like resources, data sources have a type (provided by the provider) and a local name.

**[SHOW CODE]**

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

This data source queries the AWS API for the most recent Amazon Linux 2 AMI matching the filter. The result is available as `data.aws_ami.amazon_linux`. To access a specific attribute:

**[SHOW CODE]**

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}
```

The reference syntax for data sources is `data.<type>.<name>.<attribute>`.

---

## Section 3: More Data Source Examples — 5:30–9:00

Let me walk through several data source patterns you will use regularly.

### Looking Up an Existing VPC

**[SHOW CODE]**

```hcl
data "aws_vpc" "existing" {
  filter {
    name   = "tag:Environment"
    values = ["prod"]
  }
}

resource "aws_subnet" "app" {
  vpc_id     = data.aws_vpc.existing.id
  cidr_block = "10.0.5.0/24"
}
```

### Reading Availability Zones

**[SHOW CODE]**

```hcl
data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_subnet" "public" {
  count             = 3
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
}
```

### Reading an IAM Policy Document

**[SHOW CODE]**

```hcl
data "aws_iam_policy_document" "s3_read" {
  statement {
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:ListBucket"]
    resources = ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"]
  }
}

resource "aws_iam_policy" "s3_read" {
  name   = "s3-read-policy"
  policy = data.aws_iam_policy_document.s3_read.json
}
```

The `aws_iam_policy_document` data source generates a properly formatted IAM policy JSON document, which is then passed to the resource as the `policy` argument.

### depends_on for Data Sources

If a data source depends on a resource that Terraform is creating in the same configuration, use `depends_on`:

**[SHOW CODE]**

```hcl
data "aws_vpc" "new" {
  filter {
    name   = "tag:Name"
    values = [aws_vpc.main.tags.Name]
  }

  depends_on = [aws_vpc.main]
}
```

Without `depends_on`, Terraform might attempt to query the VPC before it exists.

---

## Section 4: Terraform Built-in Functions — 9:00–16:00

Terraform has over 100 built-in functions organized into categories: string, numeric, collection, date/time, filesystem, hash/encoding, network, and type conversion. Let me cover the ones most tested on the exam.

### String Functions

**[SHOW CODE]**

```hcl
locals {
  upper_name  = upper("hello")           # "HELLO"
  lower_name  = lower("WORLD")           # "world"
  trimmed     = trimspace("  hello  ")   # "hello"
  replaced    = replace("foo-bar", "-", "_")  # "foo_bar"
  joined      = join("-", ["a", "b", "c"])    # "a-b-c"
  split_list  = split(",", "a,b,c")      # ["a", "b", "c"]
  formatted   = format("Hello, %s!", "World") # "Hello, World!"
}
```

### Collection Functions

**[SHOW CODE]**

```hcl
locals {
  list_len = length(["a", "b", "c"])          # 3
  first    = element(["a", "b", "c"], 0)      # "a"
  flattened = flatten([["a", "b"], ["c"]])    # ["a", "b", "c"]
  unique_list = distinct(["a", "b", "a"])     # ["a", "b"]
  to_set   = toset(["a", "b", "a"])          # toset(["a", "b"])
  merged   = merge({a = 1}, {b = 2})         # {a=1, b=2}
  looked_up = lookup({a = "x"}, "a", "def")  # "x"
  keys_list = keys({a = 1, b = 2})           # ["a", "b"]
  vals_list = values({a = 1, b = 2})         # [1, 2]
}
```

### Numeric Functions

**[SHOW CODE]**

```hcl
locals {
  maximum = max(3, 1, 4, 1, 5)   # 5
  minimum = min(3, 1, 4, 1, 5)   # 1
  ceiling = ceil(4.1)             # 5
  floor_v = floor(4.9)            # 4
}
```

### Encoding Functions

**[SHOW CODE]**

```hcl
locals {
  encoded = base64encode("hello world")       # "aGVsbG8gd29ybGQ="
  decoded = base64decode("aGVsbG8gd29ybGQ=")  # "hello world"
  jsoned  = jsonencode({key = "value"})       # "{\"key\":\"value\"}"
}
```

### Network Functions

**[SHOW CODE]**

```hcl
locals {
  # Generate subnet CIDRs from a VPC CIDR
  subnet_cidr = cidrsubnet("10.0.0.0/16", 8, 1)  # "10.0.1.0/24"
  host_addr   = cidrhost("10.0.1.0/24", 10)       # "10.0.1.10"
}
```

`cidrsubnet` is frequently tested. The arguments are: base CIDR, number of bits to extend the prefix, and the subnet number.

---

## Section 5: For Expressions and Dynamic Blocks — 16:00–19:30

### For Expressions

For expressions transform lists and maps inline:

**[SHOW CODE]**

```hcl
locals {
  # Transform a list
  upper_names = [for name in var.names : upper(name)]

  # Filter a list
  prod_instances = [for id in var.instance_ids : id if var.environment == "prod"]

  # Transform a map
  tag_map = {for k, v in var.tags : k => upper(v)}
}
```

### Dynamic Blocks

Dynamic blocks generate repeated nested blocks within a resource, avoiding copy-paste:

**[SHOW CODE]**

```hcl
variable "ingress_rules" {
  type = list(object({
    port        = number
    protocol    = string
    cidr_blocks = list(string)
  }))
  default = [
    { port = 80, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"] },
    { port = 443, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"] }
  ]
}

resource "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}
```

The iterator variable inside a `dynamic` block defaults to the block type name. You can override it with `iterator = rule` and then use `rule.value`.

---

## Section 6: terraform console — 19:30–21:00

`terraform console` opens an interactive REPL (Read-Eval-Print Loop) where you can evaluate HCL expressions against the current state and configuration. It is extremely useful for testing functions before putting them in your configuration.

**[SHOW CODE]**

```bash
terraform console
```

Inside the console:

```text
> upper("hello world")
"HELLO WORLD"
> cidrsubnet("10.0.0.0/16", 8, 3)
"10.0.3.0/24"
> length(["a", "b", "c"])
3
> lookup({a = "x", b = "y"}, "a", "default")
"x"
```

Type `exit` or press Ctrl+D to quit.

---

## Section 7: Closing — 21:00–22:00

Data sources are read-only queries against provider APIs. They use the `data` block type and are referenced as `data.<type>.<name>.<attribute>`. They never create or destroy infrastructure.

Key built-in functions to know: `upper`, `lower`, `join`, `split`, `length`, `element`, `flatten`, `merge`, `lookup`, `keys`, `values`, `cidrsubnet`, `jsonencode`. Use `terraform console` to test any function interactively.

For expressions transform collections inline. Dynamic blocks generate repeated nested blocks programmatically.

In Module 07 we cover Terraform workspaces. Complete the reading guide, lab, quiz, and discussion first.

See you in Module 07.

---

End of Script — Module 06
