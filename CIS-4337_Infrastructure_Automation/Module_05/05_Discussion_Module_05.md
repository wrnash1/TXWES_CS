# CIS-4337 Infrastructure Automation

## Discussion — Module 05: Modules — Creating and Using Reusable Modules

### Course Alignment: HashiCorp Terraform Associate 003

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two classmates by Sunday at 11:59 PM. Apply module design concepts from the Module 05 readings directly to the scenarios.

---

## Scenario A: The Copy-Paste Infrastructure

A startup has been operating for two years. Three developers have each written independent Terraform configurations to deploy a VPC, EC2 instances, and an RDS database for development, staging, and production. The three configurations started as copies of each other but have diverged significantly over time. Now, no two environments have the same security group rules, subnet structure, or tagging conventions. When the team tries to promote a change from development to staging, manual reconciliation is required every time.

For your initial post (175–225 words), address all three of the following points:

1. Explain how a properly designed Terraform module would have prevented this divergence. Reference the specific module design principles from the reading guide (single purpose, all inputs as variables, consistent structure).
2. Describe the refactoring process. How would the team consolidate the three configurations into one module called three times? What risks must they manage during the transition, specifically regarding the state addresses of existing resources?
3. Explain what input variables and output values the VPC module should expose to make it useful across all three environments. Give at least three specific variable names with their types and descriptions.

---

## Scenario B: The Unversioned Registry Module

A team's production Terraform configuration includes the following module call:

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "prod-vpc"
  cidr = "10.0.0.0/16"
  azs  = ["us-east-1a", "us-east-1b"]
}
```

On a Monday morning, the module's maintainers publish version 5.0.0, which introduces a breaking change: the output `vpc_id` is renamed to `id`. The team's CI/CD pipeline runs `terraform init -upgrade` at the start of every build. When the pipeline runs Monday morning, the apply fails because root-level resources referencing `module.vpc.vpc_id` cannot find that output.

For your initial post (175–225 words), address all three of the following points:

1. Identify the specific mistake in the module configuration that caused this incident. Write the corrected `module` block that would have prevented it.
2. Explain what `terraform init -upgrade` does and why running it automatically in every CI/CD build is risky when module version constraints are not pinned.
3. Describe the role of the `.terraform.lock.hcl` file in this scenario. Would committing the lock file to version control have prevented the incident even without a `version` constraint? Explain why or why not.

---

## Scenario C: The Module Interface Design Review

A senior engineer is reviewing a module written by a junior engineer. The module's purpose is to create an EC2 instance with an associated security group. The junior engineer's `variables.tf` contains only two variables:

```hcl
variable "ami_id" {
  type = string
}

variable "instance_type" {
  type = string
}
```

The `outputs.tf` is empty. Inside `main.tf`, the security group hardcodes `cidr_blocks = ["0.0.0.0/0"]` for all ingress rules, the instance type defaults to `t3.large` in the resource block (bypassing the variable), and there are no tags on any resource.

For your initial post (175–225 words), address all three of the following points:

1. List all the module design violations present in this code. Reference the specific best practices from the reading guide.
2. Write an improved `variables.tf` that addresses all the violations. Include at least five variables with correct `type`, `description`, and `default` values where appropriate.
3. Write an `outputs.tf` that exposes at least three values the calling configuration would reasonably need. For each output, explain why a caller would need that value.

---

## Peer Response Guidelines

When responding to classmates:

- Identify a module design issue or risk they did not mention.
- Offer a specific HCL improvement with a brief justification.
- Ask a follow-up question about a design tradeoff.

Each peer response must be at least 75 words and reference at least one specific module concept (source type, version constraint, variable, output, init behavior) by name.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all three prompt points with technical accuracy. Uses correct module terminology. Meets the 175–225 word count. Code snippets are syntactically correct.
- 3–4 pts: Addresses most points but contains at least one technical imprecision.
- 1–2 pts: Addresses fewer than two points or contains significant errors.
- 0 pts: No initial post submitted.

Peer Responses — 4 Points:

- 4 pts: Two substantive responses referencing specific module concepts. Each at least 75 words.
- 2 pts: One substantive response, or both lack technical depth.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Module design is a skill that separates junior Terraform users from engineers who can build maintainable infrastructure platforms. The scenarios in this module reflect real problems teams encounter at scale. When you write your post, think about what a future team member who inherits your code will need to understand and use it without asking you for help.

---

Module 05 Discussion — CIS-4337 Infrastructure Automation — Texas Wesleyan University
