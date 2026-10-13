# CIS-4337 Infrastructure Automation

## Discussion — Module 03: HCL Syntax — Providers, Resources, and Variables

### Course Alignment: HashiCorp Terraform Associate 003

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two classmates by Sunday at 11:59 PM. Use precise HCL terminology in your analysis.

---

## Scenario A: The Hardcoded Configuration

A development team is writing Terraform configurations for a new application. The junior engineer writes the following `main.tf`:

```hcl
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.large"

  tags = {
    Name = "production-app-server"
    Env  = "production"
  }
}
```

The engineer commits this file to a public GitHub repository.

For your initial post (175–225 words), address all three of the following points:

1. Identify all HCL anti-patterns in this configuration. There are at least three distinct problems. For each problem, name the specific HCL element involved and explain the risk.
2. Rewrite the `provider` block and `aws_instance` resource block header to correct all identified problems. Use `variable` blocks and environment variables as appropriate.
3. Explain the correct approach to supplying AWS credentials to Terraform in a team environment. Reference the variable precedence rules from the reading guide.

---

## Scenario B: The count vs. for_each Decision

A platform engineering team is writing a Terraform module to create EC2 instances for a set of microservices named `api`, `worker`, `scheduler`, and `cache`. A debate arises about whether to use `count` or `for_each`.

The first engineer proposes:

```hcl
resource "aws_instance" "service" {
  count         = 4
  ami           = var.ami_id
  instance_type = var.instance_type
  tags = { Name = "service-${count.index}" }
}
```

The second engineer proposes:

```hcl
resource "aws_instance" "service" {
  for_each      = toset(["api", "worker", "scheduler", "cache"])
  ami           = var.ami_id
  instance_type = var.instance_type
  tags = { Name = "service-${each.value}" }
}
```

For your initial post (175–225 words), address all three of the following points:

1. Explain the functional difference between these two approaches from Terraform's perspective. Focus on how resources are addressed in state and what happens when a service is removed from the list.
2. Recommend one approach over the other with a specific technical justification referencing the behavior Terraform exhibits when the list changes.
3. Explain how `each.key` and `each.value` differ when iterating over a `map` versus a `set`, and give one use case where a `map` would be more appropriate than a `set`.

---

## Scenario C: The lifecycle Dilemma

A production database is managed by Terraform with no `lifecycle` block. The security team requires that the database password be rotated by an automated secrets system outside of Terraform, without Terraform overwriting it on the next apply. The DBA requires that if the database must be replaced, the new database must be fully operational before the old one is deleted. After a near-miss incident, the team also wants a guard preventing accidental deletion.

For your initial post (175–225 words), address all three of the following points:

1. Write the complete `lifecycle` block that satisfies all three requirements using correct HCL syntax.
2. Explain what `ignore_changes = [password]` does and what it does not do. Clarify whether it prevents the password from being changed by Terraform in all scenarios.
3. Explain why `prevent_destroy = true` is not a permanent safeguard and describe the specific circumstance under which it fails to protect the resource.

---

## Peer Response Guidelines

When responding to classmates:

- Identify at least one detail they missed or stated imprecisely.
- Offer a corrected HCL snippet if their scenario involves a code error.
- Ask a follow-up question that would sharpen their technical analysis.

Each peer response must be at least 75 words and reference at least one specific HCL block type or meta-argument by name.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all three prompt points with technical accuracy. Uses correct HCL terminology. Meets the 175–225 word count. Code snippets are syntactically correct.
- 3–4 pts: Addresses most points but contains at least one HCL inaccuracy or imprecision.
- 1–2 pts: Addresses fewer than two prompt points or contains significant technical errors.
- 0 pts: No initial post submitted.

Peer Responses — 4 Points:

- 4 pts: Two substantive responses referencing specific HCL elements. Each at least 75 words.
- 2 pts: One substantive response, or both lack technical specificity.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Scenario A involves a real-world mistake that has resulted in compromised AWS accounts for many organizations. The habit of never hardcoding credentials is non-negotiable in professional practice. Make sure your post demonstrates that you understand not just what is wrong, but precisely why each problem is dangerous and how each is prevented.

---

Module 03 Discussion — CIS-4337 Infrastructure Automation — Texas Wesleyan University
