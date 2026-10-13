# Discussion Forum: Module 15 — Advanced Terraform Patterns

## Course: CIS-4337 Infrastructure Automation

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** HashiCorp Terraform Associate (003)

---

## Instructions

Choose one of the three scenarios below. Write an initial post of 175–225 words responding to the scenario prompt. Then write two peer responses of 75–100 words each that add substantive new information, ask a clarifying question, or respectfully challenge an assumption in the original post. Use the 10-point rubric at the bottom of this page to self-assess before submitting.

---

## Scenario A: The count Incident

A team manages 10 EC2 worker instances using `count = 10`. The list of configuration values for these workers is maintained in a variable. During a routine cleanup, a team member removes the configuration for worker 3 (index 2) from the list. They run `terraform plan`, see "3 to change, 1 to destroy," assume this is correct, and apply. Production monitoring immediately alerts: workers 3 through 10 are experiencing unexpected terminations and recreations because their index shifted.

Discuss: What caused this incident technically? How would migrating from `count` to `for_each` have prevented it? What process safeguards — beyond fixing the code pattern — would have caught this before the apply ran?

---

## Scenario B: The Legacy Import Project

Your company has 200 manually provisioned AWS resources across three accounts. Leadership wants all infrastructure managed by Terraform within 90 days. A junior engineer suggests running `terraform import` on every resource one by one. A senior engineer suggests a different approach using the `import` block and `-generate-config-out` for batches of similar resource types.

Discuss: Compare these two approaches in terms of speed, accuracy, and risk. What challenges arise when the generated configuration has attributes that differ from your team's standards? How would you organize the 90-day project to deliver manageable chunks of imported infrastructure without disrupting production?

---

## Scenario C: The Monolith Refactor

A root Terraform configuration has grown to 380 resources across 12 files. Engineers complain that `terraform plan` takes 8 minutes and `terraform apply` takes 45 minutes. Any change to any resource requires a full plan of all 380 resources. The team lead wants to split this into 6 smaller workspaces organized by service boundary.

Discuss: What is the correct technical approach to splitting the workspace without destroying any resources? Which Terraform features (`moved`, `removed`, `terraform state mv`, `data` sources) are involved and in what order? What risks must you manage during the transition period when resources exist in both old and new workspaces?

---

## Sample Peer Response Starters

- "Your count incident analysis is accurate. An additional safeguard I would add is..."
- "The two import approaches both have merit. I think the batch approach is superior because..."
- "Your workspace split plan is well sequenced. One risk during the transition period that you may have underweighted is..."

---

## Discussion Rubric — 10 Points Total

| Criterion | Points | Description |
|-----------|--------|-------------|
| Scenario accuracy | 2 | Initial post correctly identifies and addresses the core technical problem in the scenario |
| Depth of analysis | 2 | Post goes beyond surface-level description and explains trade-offs or consequences |
| Use of module concepts | 2 | Post accurately applies vocabulary and concepts from Module 15 (for_each, count, moved blocks, import, dynamic blocks, etc.) |
| Peer response 1 | 2 | First peer response adds new information, asks a clarifying question, or substantively engages with the original post |
| Peer response 2 | 2 | Second peer response meets the same standard and is not a simple agreement |

---

End of Module 15 Discussion
