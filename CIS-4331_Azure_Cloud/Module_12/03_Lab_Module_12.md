# Lab Activity: Module 12 - Azure Governance and Compliance

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 60-75 minutes
**Submission:** Canvas LMS — Module 12 Lab Assignment
**Prerequisite:** Azure for Students subscription, Azure CLI authenticated

---

## Learning Objectives

By completing this lab you will be able to:

- Assign a built-in Azure Policy definition using the Azure CLI and Portal
- Observe policy compliance evaluation on existing and new resources
- Interpret the Azure Policy compliance dashboard
- Describe the relationship between management groups and policy inheritance
- Explain how Azure Policy and Azure RBAC work together for governance

---

## Part A: Azure Policy — Create and Assign a Policy (40 Points)

### Step 1: Create a Resource Group (5 Points)

Open Azure Cloud Shell (Bash) and run:

```bash
az group create \
  --name lab12-rg \
  --location eastus
```

Verify the resource group was created:

```bash
az group show \
  --name lab12-rg \
  --query "{name:name, location:location}" \
  --output table
```

Include the output.

### Step 2: Find and Assign the "Allowed Locations" Policy (15 Points)

Find the built-in "Allowed locations" policy definition ID:

```bash
az policy definition list \
  --query "[?displayName=='Allowed locations'].{name:name, displayName:displayName}" \
  --output table
```

Note the `name` field (a GUID) from the output. Assign the policy to your resource group, restricting allowed locations to East US and West US 2:

```bash
az policy assignment create \
  --name "lab12-allowed-locations" \
  --display-name "Lab 12: Allowed Locations" \
  --policy "e56962a6-4747-49cd-b67b-bf8b01975c4f" \
  --scope "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/lab12-rg" \
  --params '{"listOfAllowedLocations": {"value": ["eastus", "westus2"]}}'
```

Verify the assignment:

```bash
az policy assignment list \
  --resource-group lab12-rg \
  --output table
```

Include all three command outputs.

Answer:

1. The policy was assigned at the resource group scope. If you wanted this policy to apply to every resource group in your subscription without creating separate assignments, at what scope would you reassign it? What happens to resources in resource groups where the policy is not assigned?

2. The "Allowed locations" policy uses the Deny effect. What exactly happens when a user with the Contributor role tries to create a storage account in Brazil South in lab12-rg after this policy is assigned? Walk through both the RBAC check and the policy evaluation step.

### Step 3: Test the Policy — Attempt a Non-Compliant Deployment (10 Points)

Attempt to create a storage account in a region not in the allowed list:

```bash
az storage account create \
  --name lab12test[your-initials] \
  --resource-group lab12-rg \
  --location japaneast \
  --sku Standard_LRS
```

This command should fail with a policy violation error. Capture the error output.

Now attempt to create a storage account in an allowed region:

```bash
az storage account create \
  --name lab12allow[your-initials] \
  --resource-group lab12-rg \
  --location eastus \
  --sku Standard_LRS
```

This command should succeed.

Include both command outputs (error for japaneast, success for eastus).

Answer:

1. The error message from the failed deployment references the policy assignment name. What information does the error provide to the developer who triggered it? Why is providing this information in the error message valuable from an operational standpoint?

2. The successful deployment in eastus confirms the policy allows that location. If you wanted to also allow West Europe as an approved location, what change would you need to make, and at what level would you make it?

### Step 4: View Policy Compliance in the Portal (10 Points)

Navigate to the Azure Portal: Policy > Compliance.

[PORTAL STEPS: Azure Policy > Compliance > select the "Lab 12: Allowed Locations" assignment]

Wait 5-10 minutes after creating the policy assignment for the compliance scan to run. The storage account you created in eastus should show as Compliant.

Take a screenshot of the Policy Compliance view for your "Lab 12: Allowed Locations" assignment.

Answer:

1. The Policy Compliance view shows a compliance percentage. What is the compliance percentage for your assignment, and what resources are listed? Why might a resource group that has never had any resources show 100% compliance?

2. In a large enterprise with hundreds of resources across dozens of resource groups, how would the Policy Compliance dashboard help a governance team identify which teams or workloads have non-compliant configurations? What action would they take after identifying a non-compliant resource?

---

## Part B: Tag Policy — Require Resource Tagging (25 Points)

### Step 1: Assign the "Require a Tag" Policy (10 Points)

Assign a policy that requires all resources to have a "CostCenter" tag:

```bash
az policy assignment create \
  --name "lab12-require-tag" \
  --display-name "Lab 12: Require CostCenter Tag" \
  --policy "1e30110a-5ceb-460c-a204-c1c3969c6d62" \
  --scope "/subscriptions/$(az account show --query id -o tsv)/resourceGroups/lab12-rg" \
  --params '{"tagName": {"value": "CostCenter"}}'
```

Verify both policy assignments are active:

```bash
az policy assignment list \
  --resource-group lab12-rg \
  --output table
```

Include the output showing both assignments.

Answer:

1. The storage account you created in Step 3 of Part A does not have a CostCenter tag. After assigning this new tag requirement policy, does the existing storage account immediately get blocked or deleted? Explain what the Audit and Deny effects mean for existing resources vs. new resources.

2. Look up the policy definition `1e30110a-5ceb-460c-a204-c1c3969c6d62`. What is the effect of this policy — Deny or Audit? How does this affect what happens when someone creates a resource without the CostCenter tag?

### Step 2: Test the Tag Policy (10 Points)

Attempt to create a resource group-scoped resource without the required tag:

```bash
# Try to create a storage account without the CostCenter tag
az storage account create \
  --name lab12notag[your-initials] \
  --resource-group lab12-rg \
  --location eastus \
  --sku Standard_LRS
```

Then attempt with the required tag:

```bash
# Create with the required CostCenter tag
az storage account create \
  --name lab12tagged[your-initials] \
  --resource-group lab12-rg \
  --location eastus \
  --sku Standard_LRS \
  --tags CostCenter=IT-Lab
```

Include both command outputs.

Answer:

1. Depending on the policy effect (Deny vs. Audit), one of two things happened when you tried to create the untagged storage account. Describe what you observed. If the policy uses Audit effect, what is the operational implication — can the untagged resource stay indefinitely, or is there a next step a governance team should take?

2. Resource tagging is a governance practice used for cost allocation, ownership tracking, and compliance reporting. Name two specific reports or business processes that would use the CostCenter tag value, and explain how mandatory tagging via policy enables those use cases.

### Step 3: Governance Analysis (5 Points)

Answer:

1. You now have two policies assigned to lab12-rg: an Allowed Locations policy and a Require Tag policy. A developer with the Contributor role wants to create a VM in West Europe with no tags. Walk through the complete evaluation sequence — RBAC check first, then each policy in turn — and describe the final outcome.

2. These two policies together represent a common governance pattern. In a real enterprise, what additional policies would you expect to see alongside location and tagging policies? Name at least two other policy categories that enterprises commonly enforce, and for each one give a specific example policy.

---

## Part C: Management Groups and Policy Inheritance Analysis (20 Points)

This part does not require resource deployment. Answer the scenario questions using your knowledge of Azure Policy and Management Group scope inheritance.

### Scenario: Contoso's Governance Structure (20 Points)

Contoso Corporation has the following Azure governance structure:

- Root Management Group: "Contoso Root"
- Child Management Group: "Contoso Production" (under Contoso Root)
- Child Management Group: "Contoso Development" (under Contoso Root)
- Subscription A: "Prod-Finance" (under Contoso Production)
- Subscription B: "Prod-Operations" (under Contoso Production)
- Subscription C: "Dev-Engineering" (under Contoso Development)
- Resource Group "RG-FinanceApp" in Prod-Finance subscription

The following Azure Policy assignments exist:

- Policy 1: "Allowed locations = East US only" — assigned at Contoso Root management group
- Policy 2: "Require tag: Environment" — assigned at Contoso Production management group
- Policy 3: "Allowed VM sizes = Standard_D2_v3, Standard_D4_v3 only" — assigned at Prod-Finance subscription
- Policy 4: "Audit: Storage accounts should restrict public access" — assigned at RG-FinanceApp resource group

Answer each question:

**Question 1 (5 Points):** A developer in the Dev-Engineering subscription wants to create a storage account in West Europe. Which policy, if any, prevents this? Explain the scope inheritance chain that makes this policy applicable to Dev-Engineering.

**Question 2 (5 Points):** A developer in the Dev-Engineering subscription creates a storage account without an "Environment" tag. Does Policy 2 apply to them? Explain your reasoning about scope and inheritance. What would need to change to require the Environment tag in Dev-Engineering as well?

**Question 3 (5 Points):** A developer in Prod-Finance wants to create a Standard_D8_v3 VM (a size not in the allowed list). Policy 3 is assigned at the Prod-Finance subscription. Will this VM creation succeed? Does Policy 3 affect developers in Prod-Operations or Dev-Engineering? Explain.

**Question 4 (5 Points):** Policy 4 uses the Audit effect and is assigned at the RG-FinanceApp resource group. A storage account in RG-FinanceApp is currently configured with public access enabled. What is the immediate result of this policy assignment? If the policy had been assigned with the Deny effect instead, how would the outcome differ for existing resources vs. new resource creation?

---

## Part D: Governance Reflection (15 Points)

Answer in your submission document (3-4 sentences each):

**Question 1 (5 Points):** You learned that Azure Policy Deny blocks operations even for users with the Owner role. This is a significant departure from how traditional RBAC-only environments work. From a security and compliance perspective, why is it important that Policy can override even highly privileged role assignments? Give a specific example of a scenario where this override capability protects the organization.

**Question 2 (5 Points):** Microsoft Purview scans Azure data sources and classifies sensitive data automatically. How does Purview's function differ from Azure Policy's function? Give a specific scenario where an organization would need both Purview AND Azure Policy to achieve their compliance goals — explain what each service contributes.

**Question 3 (5 Points):** Azure Blueprints is being deprecated in favor of using Azure Policy, ARM templates, and Management Groups individually. What does this tell you about the direction of Azure governance tooling? From a practical standpoint, what is the advantage of governance being composed of individual services rather than a monolithic "governance package" like Blueprints?

---

## Resource Cleanup

```bash
# Remove policy assignments
az policy assignment delete \
  --name "lab12-allowed-locations" \
  --resource-group lab12-rg

az policy assignment delete \
  --name "lab12-require-tag" \
  --resource-group lab12-rg

# Delete the resource group and all resources
az group delete \
  --name lab12-rg \
  --yes \
  --no-wait
```

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A Step 1: Resource group creation | 5 | Command output included |
| Part A Step 2: Policy assignment and verification | 15 | All three outputs included, scope and effect questions answered |
| Part A Step 3: Non-compliant deployment test | 10 | Error output captured, success output captured, questions answered |
| Part A Step 4: Portal compliance view | 10 | Screenshot captured, compliance percentage explained, enterprise use case addressed |
| Part B Step 1: Tag policy assignment | 10 | Output showing both assignments, Audit vs. Deny explained, existing resource behavior explained |
| Part B Step 2: Tag policy test | 10 | Both command outputs included, governance implications explained |
| Part B Step 3: Combined policy analysis | 5 | RBAC + two-policy evaluation correctly sequenced, additional policy categories identified |
| Part C: Management group scenario analysis | 20 | All four questions answered with correct scope inheritance reasoning |
| Part D: Governance reflection | 15 | All three questions answered with substantive analysis |
| **Total** | **100** | |

---

## Troubleshooting

**Policy assignment fails with "does not have authorization":** You need at least Contributor at the target scope plus permission to read policy definitions. If this fails, verify your subscription role with `az role assignment list --assignee $(az ad signed-in-user show --query userPrincipalName -o tsv) --all --output table`.

**Policy compliance not updating:** Policy compliance evaluation can take 10-30 minutes after assignment. Navigate to Azure Policy > Compliance and click "Trigger evaluation" if available, or wait for the automatic scan.

**Storage account name taken:** Storage account names must be globally unique. Change `[your-initials]` to include a number if needed.

**Policy ID not found:** The policy definition GUIDs in this lab are built-in Microsoft policies. If the GUID lookup fails, search by name: `az policy definition list --query "[?displayName=='Allowed locations']"`.

---

Lab 12 | CIS-4331 Azure Cloud | Texas Wesleyan University
