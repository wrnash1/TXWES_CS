# Lab Activity: Module 02 - Azure Physical Architecture

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 60-75 minutes
**Submission:** Canvas LMS — Module 02 Lab Assignment
**Prerequisite:** Azure for Students subscription (free — activate at azure.microsoft.com/en-us/free/students/)

---

## Learning Objectives

By completing this lab you will be able to:

- Use Azure CLI to list and explore Azure regions and their Availability Zone support
- Create and inspect resource groups using both the Azure Portal and Azure CLI
- Map an organizational management hierarchy onto Azure subscriptions and management groups
- Explain region selection trade-offs using real latency and compliance criteria

---

## Prerequisites

- Azure for Students subscription activated (or free trial at portal.azure.com)
- Azure CLI installed and authenticated (`az login` completed)
- A modern web browser with access to portal.azure.com

To verify your CLI setup, run:

```bash
az account show
```

The output should display your subscription name, subscription ID, and tenant ID. If you receive an error, run `az login` and follow the browser authentication prompt.

---

## Part A: Explore Azure Regions Using the CLI (20 Points)

### Part A Instructions

Use Azure CLI commands to explore available regions. Do not use the Portal for this part — all work must be done via CLI and documented with terminal output.

### Step 1: List All Available Regions (5 Points)

Run the following command and capture the output:

```bash
az account list-locations --output table
```

In your submission document, include the full terminal output and answer these questions:

1. How many total regions are listed?
2. Identify three regions located in the United States. List their Name (the CLI identifier) and DisplayName.
3. What is the CLI region name for the region geographically closest to Fort Worth, Texas?

### Step 2: Find Regions with Availability Zone Support (10 Points)

Run this query to filter regions that support Availability Zones:

```bash
az account list-locations \
  --query "[?availabilityZoneMappings != null].{Name:name, Display:displayName}" \
  --output table
```

In your submission document:

1. List five regions that appear in this filtered output.
2. Compare the output from Step 1 to Step 2. Are all regions in Step 1 also in Step 2? What does this tell you about Availability Zone availability?
3. Does `southcentralus` (South Central US) appear in the Availability Zone-supported list? Why does this matter for Texas-based deployments?

### Step 3: Inspect a Specific Region (5 Points)

Run the following command to get detailed information about East US:

```bash
az account list-locations --query "[?name=='eastus']" --output json
```

In your submission document, include the JSON output and identify:

1. The `availabilityZoneMappings` array — how many zones are listed for East US?
2. The `metadata.latitude` and `metadata.longitude` values — what US city is nearest to these coordinates?

---

## Part B: Create and Manage Resource Groups (30 Points)

### Part B CLI Instructions

In this part you will create resource groups using both the Azure Portal and Azure CLI, then explore their properties.

### Step 1: Create a Resource Group via Azure CLI (10 Points)

Run the following command to create a resource group. Replace `[your-initials]` with your actual initials (e.g., `jdn`):

```bash
az group create \
  --name "cis4331-lab02-[your-initials]-rg" \
  --location "southcentralus" \
  --tags "course=CIS4331" "module=02" "purpose=lab"
```

Document the following:

1. Include the full JSON output returned by the command.
2. What is the value of the `"provisioningState"` field in the output?
3. What does the `--tags` parameter accomplish? Why might tagging be important in a real organization?

### Step 2: Verify the Resource Group in the Azure Portal (5 Points)

**[SHOW PORTAL — Navigate to portal.azure.com > Resource Groups]**

Navigate to portal.azure.com, sign in, and click "Resource Groups" in the left navigation (or search for it). Find the resource group you just created.

Take a screenshot showing:

- The resource group name
- The location
- The tags you applied

Include this screenshot in your submission.

### Step 3: Create a Second Resource Group in a Different Region (5 Points)

```bash
az group create \
  --name "cis4331-lab02-[your-initials]-eastus-rg" \
  --location "eastus" \
  --tags "course=CIS4331" "module=02" "purpose=lab-eastus"
```

Answer the following questions:

1. You now have two resource groups in two different regions. Can a single virtual machine span both resource groups? Can a virtual network span both regions?
2. What is the purpose of having resource groups in different regions if resources are bound to their resource group's region?

### Step 4: List All Resource Groups (5 Points)

```bash
az group list --output table
```

Include the terminal output in your submission. Verify both resource groups appear.

### Step 5: Delete Both Resource Groups (5 Points)

When you are done with the lab resources, delete them to avoid consuming your student subscription budget:

```bash
az group delete --name "cis4331-lab02-[your-initials]-rg" --yes --no-wait
az group delete --name "cis4331-lab02-[your-initials]-eastus-rg" --yes --no-wait
```

Include terminal output showing the delete commands executed. Note that `--no-wait` returns immediately while deletion continues in the background. Confirm deletion in the Portal within 5 minutes.

---

## Part C: Management Hierarchy Diagram Exercise (30 Points)

### Part C Instructions

You will design a management hierarchy for a fictional organization and document your design decisions.

### Organization Profile

Rampart Industries is a mid-sized technology company with the following structure:

- Three business divisions: Commercial Software, Government Contracts, and Research & Development
- Government Contracts division must meet FedRAMP Moderate compliance requirements
- Each division has Production and Development environments
- Finance requires separate billing reports for each division
- The corporate security team must be able to enforce a policy requiring MFA on all accounts across the entire organization
- R&D is experimenting with multiple Azure services and needs budget isolation to prevent accidental overspending

### Hierarchy Design Task (20 Points)

Design an Azure management hierarchy for Rampart Industries that satisfies all stated requirements. Your design must include:

- The Tenant Root Management Group
- Division-level Management Groups (one per division)
- Subscriptions (minimum of one per division-environment combination)
- At least two Resource Groups per subscription with descriptive names

Draw or describe your hierarchy. If drawing, include a diagram image or an ASCII text diagram in your submission document. If describing in text, use indented bullet points to represent the hierarchy levels.

For each subscription you create, provide:

- A descriptive name that follows a naming convention
- The reason this subscription is separate (billing isolation, compliance boundary, or environment separation)

### Justification Questions (10 Points)

Answer the following questions based on your design:

1. How does your design ensure that the corporate security team can enforce the MFA policy across all divisions without configuring it separately in each subscription?
2. The Government Contracts division needs FedRAMP Moderate compliance. Does Azure Government need to be used, or can standard Azure regions be used with appropriate compliance configurations? Explain.
3. The R&D division's budget isolation requirement — which element of the hierarchy (management group, subscription, or resource group) is the most effective tool for enforcing a spending limit? Why?

---

## Part D: Region Selection Analysis (20 Points)

### Part D Instructions

For each scenario below, identify the most appropriate Azure region and justify your choice using the four region selection criteria from the reading guide (latency, compliance, service availability, pricing).

### Scenario 1 (5 Points)

A Dallas-based hospital system is deploying a patient portal application. All patient health information (PHI) must comply with HIPAA. The application needs to serve 5,000 concurrent users across Texas and Oklahoma with minimal latency.

**Your region recommendation and justification:**

### Scenario 2 (5 Points)

A US Department of Defense agency is building a classified workload management system. The system must meet DoD Impact Level 5 requirements and may only be operated by US citizens.

**Your region recommendation and justification:**

### Scenario 3 (5 Points)

A global e-commerce company is expanding to serve customers in Germany. EU data protection law (GDPR) requires that German customer personal data remain within the European Union. The company's developers are based in Ireland.

**Your region recommendation and justification:**

### Scenario 4 (5 Points)

A startup is launching a new mobile game. They expect players primarily in Southeast Asia. The game requires ultra-low latency for real-time multiplayer. Budget is limited and the team wants to choose the lowest-cost region that meets latency requirements.

**Your region recommendation and justification:**

---

## Submission Requirements

Your submission must include:

1. Terminal output for all CLI commands in Part A (Steps 1-3)
2. Answers to all Part A questions
3. Terminal output and screenshot for Part B (Steps 1-5)
4. Answers to all Part B questions
5. Management hierarchy diagram or description for Part C
6. Justification answers for Part C questions
7. Region recommendations and justifications for all four Part D scenarios

Format as a single PDF or Word document. Include your full name, student ID, and "CIS-4331 Module 02 Lab" in the header.

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A: CLI region list output + questions | 20 | Output captured, 3 questions answered accurately |
| Part B: Resource group creation (CLI + Portal) | 30 | Commands run, outputs documented, screenshot present, cleanup confirmed |
| Part C: Hierarchy design diagram | 20 | All required elements present, naming convention applied, subscriptions justified |
| Part C: Justification questions | 10 | All 3 questions answered with accurate technical reasoning |
| Part D: Four scenario recommendations | 20 | Correct region named, all four criteria addressed in justification |
| **Total** | **100** | |

---

## Troubleshooting

**`az login` opens browser but returns error:** Try `az login --use-device-code` for environments where browser redirect does not work.

**Resource group creation fails with "Location not available":** Verify the region name exactly matches the CLI identifier (`southcentralus`, not `South Central US`). Use `az account list-locations --output table` to find the exact name.

**Cannot see resource group in Portal:** Confirm you are signed in to the correct subscription. Check the subscription filter in the Portal top bar — the Portal may be filtering to show only resources from a different subscription.
