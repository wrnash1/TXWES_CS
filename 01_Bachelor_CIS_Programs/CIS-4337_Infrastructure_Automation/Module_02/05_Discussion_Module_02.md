# CIS-4337 Infrastructure Automation

## Discussion — Module 02: Terraform Workflow

### Course Alignment: HashiCorp Terraform Associate 003

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two classmates by Sunday at 11:59 PM. Ground your analysis in specific Terraform CLI behavior from the Module 02 readings and lab.

---

## Scenario A: The Missing Init

A junior engineer clones a Terraform repository from GitHub to set up a new staging environment. The repository contains a fully written `main.tf`, `variables.tf`, and `outputs.tf`. Excited to get started, the engineer runs `terraform plan` immediately without running any other commands first. Terraform returns an error and nothing happens.

For your initial post (175–225 words), address all three of the following points:

1. Explain precisely why `terraform plan` failed. Identify which workflow step was skipped and what that step is responsible for providing.
2. Describe what the engineer should have done instead, including the correct command sequence and what each command prepares for the next.
3. Explain what the `.terraform.lock.hcl` file in the repository provides and why the engineer still needed to run `terraform init` even though provider version constraints were already recorded in that file.

---

## Scenario B: The Production Apply Surprise

A DevOps engineer has been making incremental changes to a Terraform configuration over several days. On Friday afternoon they run `terraform plan` and verify that only two small changes are planned. They approve the changes and note to themselves to run `terraform apply` Monday morning. Over the weekend, another team member merges a separate branch that adds three new resources to the same configuration. Monday morning, the engineer runs `terraform apply` — without running plan first — and approves the changes. The apply creates five resources instead of the expected two.

For your initial post (175–225 words), address all three of the following points:

1. Identify the workflow mistake the engineer made and explain which Terraform pattern would have prevented the unintended extra resources from being applied.
2. Describe the `terraform plan -out=tfplan` and `terraform apply tfplan` pattern and explain exactly why it prevents this class of problem.
3. Reflect on how this scenario illustrates the relationship between the plan and apply steps in the Terraform workflow. What is the key principle violated when plan and apply are not treated as a pair?

---

## Scenario C: The Forced Replacement Incident

An operations team manages a production web application using Terraform. A change request arrives to update the application server's Amazon Machine Image (AMI) to a newer version for security patching. An engineer updates the `ami` attribute in `main.tf` and runs `terraform plan`. The plan shows `-/+` next to the `aws_instance` resource and lists the action as "must be replaced." The engineer is surprised because they expected a simple in-place update.

For your initial post (175–225 words), address all three of the following points:

1. Explain why changing an `ami` attribute triggers forced replacement rather than an in-place update, and describe what `-/+` means in the plan output.
2. Discuss the operational impact of a forced replacement on a production web server. What happens to the existing instance and its data during the apply?
3. Propose a strategy to minimize or eliminate downtime when a forced replacement is required. Your answer should reference infrastructure patterns rather than Terraform-specific workarounds.

---

## Peer Response Guidelines

When responding to classmates:

- Identify a risk or edge case they did not mention.
- Offer a specific alternative approach with technical justification.
- Connect their scenario to another Terraform concept from Module 02.
- Ask a follow-up question that would advance the technical discussion.

Each peer response must be at least 75 words and reference at least one specific Terraform CLI command or concept by name.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all three prompt points with technical accuracy. Uses correct terminology (init, plan, apply, forced replacement, saved plan, lock file, etc.). Meets the 175–225 word count.
- 3–4 pts: Addresses most points but lacks technical precision in at least one area.
- 1–2 pts: Addresses fewer than two points or contains significant technical errors.
- 0 pts: No initial post submitted.

Peer Responses — 4 Points:

- 4 pts: Two substantive responses, each at least 75 words, each referencing specific Terraform concepts.
- 2 pts: One substantive response, or both responses lack technical content.
- 0 pts: No peer responses submitted.

---

Professor Nash note: The scenarios in this module test whether you understand the workflow at a practical level, not just a definitional one. Your post should read like an explanation you would give to a colleague on a real team, not a recitation of definitions from the reading guide.

---

Module 02 Discussion — CIS-4337 Infrastructure Automation — Texas Wesleyan University
