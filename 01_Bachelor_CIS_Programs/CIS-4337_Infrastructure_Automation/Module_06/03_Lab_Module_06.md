# CIS-4337 Infrastructure Automation

## Lab — Module 06: Data Sources and Terraform Functions

### Course Alignment: HashiCorp Terraform Associate 003

---

## Objectives

By the end of this lab you will be able to:

- Write `data` blocks to query AMIs, availability zones, and IAM policy documents.
- Reference data source attributes in resource blocks.
- Use `terraform console` to test built-in functions interactively.
- Apply for expressions to transform collections.
- Use `dynamic` blocks to generate variable-length nested blocks.

---

## Prerequisites

- Terraform CLI 1.6.0 or later.
- AWS CLI configured with credentials (EC2, IAM, and VPC read permissions).
- An AWS Free Tier account.

---

## Part 1: Use terraform console to Test Functions

Before writing any configuration, use the console to practice functions.

### Step 1.1 — Start the console

Navigate to any directory containing a `main.tf` with at least a `terraform {}` block (even an empty one), run `terraform init`, then:

```bash
terraform console
```

### Step 1.2 — Test string functions

Enter each expression and record the result in `lab_notes.txt`:

```text
upper("cis4337")
join("-", ["dev", "us-east-1", "web"])
split(",", "alice,bob,charlie")
replace("web-server-01", "-", "_")
format("instance-%03d", 7)
trimspace("  hello world  ")
```

### Step 1.3 — Test collection functions

```text
length(["a", "b", "c", "d"])
element(["alpha", "beta", "gamma"], 2)
merge({project = "lab06"}, {env = "dev"})
lookup({dev = "t3.micro", prod = "t3.large"}, "dev", "t3.micro")
lookup({dev = "t3.micro", prod = "t3.large"}, "staging", "t3.micro")
distinct(["a", "b", "a", "c", "b"])
flatten([["a", "b"], ["c"], ["d", "e"]])
```

Record the result of each. Note the difference between the two `lookup` calls.

### Step 1.4 — Test network functions

```text
cidrsubnet("10.0.0.0/16", 8, 0)
cidrsubnet("10.0.0.0/16", 8, 1)
cidrsubnet("10.0.0.0/16", 8, 5)
cidrhost("10.0.1.0/24", 10)
cidrhost("10.0.1.0/24", 100)
```

Record in `lab_notes.txt`: What pattern do you observe? How does the third argument to `cidrsubnet` affect the result?

Exit the console: type `exit` or press Ctrl+D.

---

## Part 2: Use Data Sources in a Configuration

### Step 2.1 — Create the working directory

```bash
mkdir ~/tf-lab-06
cd ~/tf-lab-06
```

### Step 2.2 — Create main.tf

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

# Data source: latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Data source: available availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# VPC for our resources
resource "aws_vpc" "lab" {
  cidr_block           = "10.6.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = { Name = "lab06-vpc" }
}

# Subnets using cidrsubnet function and availability zones data source
resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.lab.id
  cidr_block        = cidrsubnet("10.6.0.0/16", 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "lab06-public-${count.index + 1}"
  }
}

# EC2 instance using AMI from data source
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public[0].id

  tags = { Name = "lab06-web" }
}
```

### Step 2.3 — Create variables.tf

```hcl
variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}
```

### Step 2.4 — Create outputs.tf

```hcl
output "ami_id" {
  description = "AMI ID from data source"
  value       = data.aws_ami.amazon_linux.id
}

output "ami_name" {
  description = "AMI name from data source"
  value       = data.aws_ami.amazon_linux.name
}

output "availability_zones" {
  description = "Available AZs"
  value       = data.aws_availability_zones.available.names
}

output "subnet_cidrs" {
  description = "CIDR blocks of created subnets"
  value       = aws_subnet.public[*].cidr_block
}
```

### Step 2.5 — Apply and inspect outputs

```bash
terraform init
terraform apply -auto-approve
terraform output
```

Record in `lab_notes.txt`:

1. What AMI ID did the data source return?
2. What are the CIDR blocks of the two subnets? How were they calculated by `cidrsubnet`?
3. Which availability zones were returned by the data source?

---

## Part 3: IAM Policy Document Data Source

Add the following to `main.tf`:

```hcl
data "aws_iam_policy_document" "s3_read" {
  statement {
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:ListBucket"]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "s3_read" {
  name   = "lab06-s3-read"
  policy = data.aws_iam_policy_document.s3_read.json
}
```

Add to `outputs.tf`:

```hcl
output "iam_policy_json" {
  description = "JSON policy document generated by data source"
  value       = data.aws_iam_policy_document.s3_read.json
}
```

Run `terraform apply -auto-approve` and inspect the `iam_policy_json` output. Record: How does the `aws_iam_policy_document` data source simplify IAM policy management compared to writing raw JSON?

---

## Part 4: Dynamic Block

Add a security group using a dynamic block to `main.tf`:

```hcl
variable "ingress_ports" {
  type = list(number)
  default = [80, 443, 8080]
}

resource "aws_security_group" "web" {
  name   = "lab06-web-sg"
  vpc_id = aws_vpc.lab.id

  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = { Name = "lab06-web-sg" }
}
```

Run `terraform plan`. Record in `lab_notes.txt`:

1. How many `ingress` rules does the plan show?
2. What would happen if you added `8443` to `ingress_ports`?
3. How does this compare to writing three separate `ingress {}` blocks?

Run `terraform apply -auto-approve`.

---

## Part 5: Destroy All Resources

```bash
terraform destroy -auto-approve
```

---

## Deliverables

Submit to Canvas:

1. `lab_notes.txt` with all `terraform console` results and answers.
2. Screenshot of `terraform output` showing AMI ID, AZ list, and subnet CIDRs.
3. Screenshot of the `iam_policy_json` output.
4. Screenshot of `terraform plan` showing the dynamic ingress rules.
5. Final `main.tf` and `outputs.tf` files.

---

## Grading Rubric — 100 Points

| Criterion | Points |
|---|---|
| All `terraform console` function results recorded correctly | 20 |
| AMI data source used; correct reference syntax in resource | 15 |
| AZ data source used; subnets placed in correct AZs | 15 |
| `cidrsubnet` function used correctly; subnet CIDRs explained | 10 |
| IAM policy document data source used; JSON output captured | 15 |
| Dynamic block generates correct number of ingress rules | 15 |
| All resources destroyed cleanly | 10 |

---

## Troubleshooting

**console: No configuration files found**
Create a minimal `main.tf` with a `terraform {}` block and run `terraform init` before opening the console.

**Error: InvalidAMIID.NotFound**
The data source may return an AMI ID that is not yet fully available. Re-run `terraform apply`. If the issue persists, add a `filter` block to match a more specific AMI name.

**Error: with dynamic block — Invalid for_each argument**
Ensure `var.ingress_ports` is declared as `list(number)`. If you declared it as `list(string)`, the `from_port` and `to_port` will receive string values where numbers are expected.

---

## Part 9 — Challenge Exercise

### Challenge 1: Dynamic Security Group with Object Variable

Replace the simple `list(number)` ingress variable with a structured `list(object)` variable that carries port, protocol, and CIDR per rule. Use a dynamic block and a `for` expression together.

**Step A.** Replace `variable "ingress_ports"` with the following structured variable:

```hcl
variable "ingress_rules" {
  type = list(object({
    port     = number
    protocol = string
    cidr     = string
    description = string
  }))
  default = [
    { port = 80,  protocol = "tcp", cidr = "0.0.0.0/0",    description = "HTTP" },
    { port = 443, protocol = "tcp", cidr = "0.0.0.0/0",    description = "HTTPS" },
    { port = 22,  protocol = "tcp", cidr = "10.0.0.0/8",   description = "SSH internal" }
  ]
}
```

**Step B.** Update the `dynamic "ingress"` block to use `var.ingress_rules` as `for_each`, with `iterator = rule`, and reference `rule.value.port`, `rule.value.protocol`, `rule.value.cidr`, and `rule.value.description` inside the `content` block.

1. Run `terraform plan` and confirm three ingress rules appear with the correct ports and CIDRs.
2. Add a fourth rule for port `8443` with `cidr = "0.0.0.0/0"` to the default list and re-run `terraform plan`. Confirm Terraform plans an in-place update to the security group adding the new rule.
3. In `lab_notes.txt`, use a `for` expression in `terraform console` to extract just the `description` fields from `var.ingress_rules` as a list: `[for r in var.ingress_rules : r.description]`.

### Challenge 2: Data Source Chaining with `depends_on`

Demonstrate the scenario where a data source queries a resource being created in the same run, requiring explicit `depends_on`.

**Step A.** Add a second VPC resource to `main.tf` that is created with a specific `Name` tag, then add a data source that looks it up by that tag:

```hcl
resource "aws_vpc" "secondary" {
  cidr_block = "10.7.0.0/16"
  tags       = { Name = "lab06-secondary" }
}

data "aws_vpc" "secondary_lookup" {
  filter {
    name   = "tag:Name"
    values = ["lab06-secondary"]
  }
  depends_on = [aws_vpc.secondary]
}
```

1. Run `terraform plan` and observe the plan. Remove the `depends_on` line, run `terraform plan` again, and record what warning or error Terraform produces.
2. Restore `depends_on`, run `terraform apply -auto-approve`, and confirm the data source output matches the resource's VPC ID.
3. In `lab_notes.txt`, explain why `depends_on` is needed here even though the data source implicitly references no attribute of `aws_vpc.secondary`.

### Reflection Questions

1. You used both `aws_iam_policy_document` data source and `jsonencode()` to generate IAM policy JSON. In what situation would you prefer the data source approach over `jsonencode()`, and vice versa?
2. Dynamic blocks make configurations more flexible but can reduce readability. Describe a guideline for when to use a `dynamic` block versus writing static repeated nested blocks, and explain how documentation can compensate for reduced readability.

---

Module 06 Lab — CIS-4337 Infrastructure Automation — Texas Wesleyan University
