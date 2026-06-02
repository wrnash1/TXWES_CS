# CIS-4337 Infrastructure Automation

## Discussion — Module 07: Terraform Workspaces and Environments

### Course Alignment: HashiCorp Terraform Associate 003

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two classmates by Sunday at 11:59 PM. Analyze each scenario using the specific workspace behavior and limitations covered in Module 07.

---

## Scenario A: The Workspace Accident

A DevOps team manages three environments — dev, staging, and prod — using three CLI workspaces within a single Terraform working directory. All workspaces use the same AWS account because the team never had time to set up separate accounts. One Friday afternoon, an engineer runs `terraform workspace select staging` to investigate a bug. After reviewing the state, they run `terraform destroy -auto-approve` to clean up a temporary test resource they thought they had deployed. Staging production infrastructure is destroyed within minutes.

For your initial post (175–225 words), address all three of the following points:

1. Explain the specific characteristics of CLI workspaces that allowed this accident to happen. Focus on what workspace isolation does and does not provide.
2. Compare the three-workspace approach to the recommended separate-directory pattern. Explain exactly what safeguard the separate-directory pattern provides that would have prevented this incident.
3. Propose a three-part remediation plan for this team: one structural change, one process change, and one technical safeguard. Be specific about Terraform features involved in each part.

---

## Scenario B: The Environment Variable Question

A junior engineer is building a Terraform configuration to deploy a web application across dev, staging, and prod. They want to use different instance sizes per environment. They are debating between two approaches:

Approach 1 — Workspaces with terraform.workspace:

```hcl
locals {
  sizes = {
    dev     = "t3.micro"
    staging = "t3.small"
    prod    = "t3.large"
  }
}

resource "aws_instance" "web" {
  instance_type = lookup(local.sizes, terraform.workspace, "t3.micro")
}
```

Approach 2 — Separate directories with a variable:

```hcl
variable "instance_type" {
  type    = string
  default = "t3.micro"
}

resource "aws_instance" "web" {
  instance_type = var.instance_type
}
```

For your initial post (175–225 words), address all three of the following points:

1. Describe the operational experience of each approach. How does an engineer deploy to each environment using Approach 1 versus Approach 2?
2. Identify one scenario where Approach 1 is superior and one scenario where Approach 2 is superior. Justify each recommendation with a specific technical reason.
3. Explain how you would extend Approach 1 to handle a new environment called `qa` without modifying the `resource` block. What must be added and where?

---

## Scenario C: The Workspace Naming Convention

An infrastructure team is designing a Terraform workspace strategy for a new SaaS product. The product will be deployed for multiple customers, each with their own isolated AWS environment. They are considering creating a workspace for each customer: `customer-acme`, `customer-globex`, `customer-initech`, etc. The senior engineer raises a concern.

For your initial post (175–225 words), address all three of the following points:

1. Explain the senior engineer's likely concern. Reference the specific CLI workspace limitations that make a large number of customer workspaces problematic in practice.
2. Compare the workspace-per-customer approach to an alternative architecture. Describe at least one alternative pattern and explain why it is better suited to per-customer isolation at scale.
3. Describe the role of `terraform.workspace` in naming uniqueness when the team uses workspaces for lightweight environment separation. Write an example resource block that embeds the workspace name and explain what happens if two different workspaces attempt to create a resource with the same global identifier (like an S3 bucket name).

---

## Peer Response Guidelines

When responding to classmates:

- Identify a workspace behavior or limitation they did not address.
- Offer a specific technical improvement or alternative architecture.
- Ask a follow-up question about a trade-off they made in their recommendation.

Each peer response must be at least 75 words and reference at least one specific `terraform workspace` command or `terraform.workspace` behavior by name.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all three prompt points with technical accuracy. Uses correct workspace terminology. Meets the 175–225 word count.
- 3–4 pts: Addresses most points but lacks precision in at least one area.
- 1–2 pts: Addresses fewer than two points or contains significant technical errors.
- 0 pts: No initial post submitted.

Peer Responses — 4 Points:

- 4 pts: Two substantive responses referencing specific workspace concepts. Each at least 75 words.
- 2 pts: One substantive response, or both lack technical depth.
- 0 pts: No peer responses submitted.

---

Professor Nash note: Scenario A describes a real class of Terraform incident. The workspace model provides convenience but no hard boundary between environments when all workspaces share credentials. Your post should reflect that you understand this trade-off at a production-system level, not just a definitional one.

---

Module 07 Discussion — CIS-4337 Infrastructure Automation — Texas Wesleyan University
