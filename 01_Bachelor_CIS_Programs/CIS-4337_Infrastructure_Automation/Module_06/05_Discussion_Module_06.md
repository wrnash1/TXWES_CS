# CIS-4337 Infrastructure Automation

## Discussion — Module 06: Data Sources and Terraform Functions

### Course Alignment: HashiCorp Terraform Associate 003

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two classmates by Sunday at 11:59 PM. Apply data source and function concepts from Module 06 directly to each scenario.

---

## Scenario A: The Hardcoded AMI Problem

A team manages hundreds of EC2 instances across three AWS regions using Terraform. Their configurations hardcode AMI IDs directly in resource blocks:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}
```

Every quarter, when AWS releases updated Amazon Linux 2 AMIs with security patches, an engineer must manually find the new AMI ID for each region, update every `.tf` file, and test before deploying. Last quarter, two regions were missed, leaving them running outdated AMIs for 45 days.

For your initial post (175–225 words), address all three of the following points:

1. Explain how a `data "aws_ami"` block would solve this problem. Write the specific data source block and resource reference that would replace the hardcoded AMI ID, including the necessary `filter` arguments to select Amazon Linux 2.
2. Explain how this approach handles the multi-region problem. If the same module is deployed in three regions, how does the data source ensure the correct AMI for each region is used?
3. Discuss one risk of always using `most_recent = true` in a data source. When might a team want to pin a specific AMI ID instead of always using the latest?

---

## Scenario B: The Security Group Explosion

A network security engineer is tasked with creating security groups for six different application tiers. Each tier requires a different set of ingress ports. The current approach uses six separate `aws_security_group` resources, each with its ingress rules hardcoded as individual blocks. The total configuration is over 400 lines, and adding a new tier requires copying an existing resource block and manually editing every attribute.

The engineer's manager asks for a redesign that can add a new tier by modifying only a variable value.

For your initial post (175–225 words), address all three of the following points:

1. Design a `variable` block that can represent all six application tiers and their port requirements. Choose the most appropriate HCL type and provide a complete variable declaration with an example default value for at least two tiers.
2. Write the `dynamic "ingress"` block structure that would iterate over the variable to generate ingress rules. Show how `ingress.value` is used to access port and protocol.
3. Explain what happens to the plan when a new tier is added to the variable value. How does this compare to the current approach of copying resource blocks?

---

## Scenario C: The CIDR Calculation Challenge

A cloud architect needs to build a Terraform module that provisions VPCs across multiple environments. The requirements are:

- Each environment gets a `/16` VPC CIDR.
- Each VPC must be divided into six `/24` subnets.
- Subnets must be placed in three availability zones (two subnets per AZ).
- The subnet CIDRs must be calculated programmatically so the module works for any parent CIDR.

The architect wants to use the `cidrsubnet` function and the `aws_availability_zones` data source rather than hardcoding any CIDR or AZ values.

For your initial post (175–225 words), address all three of the following points:

1. Explain how `cidrsubnet("10.0.0.0/16", 8, 0)` through `cidrsubnet("10.0.0.0/16", 8, 5)` produces six `/24` subnets. Show all six results.
2. Write the `resource "aws_subnet"` block using `count`, `cidrsubnet`, and a reference to `data.aws_availability_zones.available.names` that creates all six subnets. Show how the AZ is selected to distribute two subnets per AZ.
3. Explain why using `data "aws_availability_zones"` is better than hardcoding availability zone names. Reference a specific scenario where hardcoded AZ names would cause a deployment to fail.

---

## Peer Response Guidelines

When responding to classmates:

- Identify a function or data source they did not mention that would enhance their solution.
- Offer a specific correction or improvement to their HCL code.
- Ask a follow-up question about an edge case in their design.

Each peer response must be at least 75 words and reference at least one specific built-in function or `data` block type by name.

---

## Grading Rubric — 10 Points Total

Initial Post — 6 Points:

- 5–6 pts: Addresses all three prompt points with technical accuracy. Uses correct HCL and function syntax. Meets the 175–225 word count.
- 3–4 pts: Addresses most points but contains at least one technical imprecision or syntax error.
- 1–2 pts: Addresses fewer than two points or contains significant errors.
- 0 pts: No initial post submitted.

Peer Responses — 4 Points:

- 4 pts: Two substantive responses referencing specific functions or data source concepts. Each at least 75 words.
- 2 pts: One substantive response, or both lack technical specificity.
- 0 pts: No peer responses submitted.

---

Professor Nash note: The ability to avoid hardcoded values is what separates a maintainable Terraform configuration from one that requires constant manual updates. When you review your classmates' posts in Scenario A and C, consider the operational cost of their approach at scale — dozens of regions, hundreds of modules, and quarterly patch cycles.

---

Module 06 Discussion — CIS-4337 Infrastructure Automation — Texas Wesleyan University
