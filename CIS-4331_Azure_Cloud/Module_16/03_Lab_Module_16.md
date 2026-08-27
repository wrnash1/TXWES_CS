# Lab Activity: Module 16 — AZ-900 Capstone Lab and Certification Submission

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Alignment: All three exam domains (comprehensive review)

---

## Lab Overview

This is the final lab of CIS-4331. It has two components.

**Component 1 (Technical):** You will design, deploy, and document a multi-service Azure solution that integrates services from all three AZ-900 exam domains — Cloud Concepts, Azure Architecture and Services, and Azure Management and Governance. The scenario is a small company migrating a web workload to Azure. You will provision compute, storage, and networking resources; apply governance controls; and build a cost estimate. This directly mirrors the type of integration scenario tested on the AZ-900 exam.

**Component 2 (Certification):** You will register for and sit the official Microsoft AZ-900 exam, then submit your score report. Passing the exam earns you a Microsoft credential and satisfies the course's industry certification requirement.

### Learning Objectives

By completing this lab you will be able to:

- Deploy a multi-tier Azure solution using Portal and CLI
- Apply RBAC, tags, and a budget to enforce governance on a real subscription
- Build and interpret a Pricing Calculator estimate for the deployed workload
- Demonstrate the shared responsibility model with concrete examples from the lab
- Pass the Microsoft AZ-900 certification exam

### Estimated Time

- Component 1 (Technical Lab): 90–120 minutes
- Component 2 (Exam Prep and Scheduling): 30–60 minutes
- Component 2 (Exam Sitting): 45 minutes (scheduled separately at the testing center)

### Tools Required

- Azure free account at portal.azure.com
- Azure Cloud Shell (no local install required)
- Browser access to azure.microsoft.com/en-us/pricing/calculator/

---

## Scenario

You are setting up the Azure infrastructure for a small company called **Lone Star Tech** that is migrating its web presence to Azure. The workload consists of:

- A Linux web server VM serving a static site (IaaS)
- An Azure Storage Account for static asset hosting (PaaS)
- An Azure Virtual Network with a subnet for the VM
- A monthly budget alert to ensure the free trial is not overrun
- RBAC roles for a developer who needs to deploy but not manage billing
- Resource tags for cost tracking

---

## Component 1: Multi-Service Capstone Deployment (80 points)

---

## Part A: Environment Setup (10 minutes)

### Step A1: Create the Resource Group with Tags

Open Azure Cloud Shell (Bash) from the Azure Portal. Run the following command. Replace `[initials]` with your initials.

```bash
az group create \
  --name cap16-rg \
  --location eastus \
  --tags Environment=Lab Project=CIS4331-Capstone Owner=[YourName]
```

### Step A2: Verify the Tags

```bash
az group show \
  --name cap16-rg \
  --query "tags" \
  --output json
```

Confirm all three tags appear in the output.

### Deliverable A

Screenshot of the Cloud Shell showing the `az group show` output with all three tags visible. Label it **CapA-ResourceGroup-Tags**.

---

## Part B: Networking Foundation (15 minutes)

Before deploying compute, you will create a Virtual Network with a dedicated subnet. This reflects the real-world pattern where networking is configured before VMs are placed.

### Step B1: Create the Virtual Network and Subnet

```bash
az network vnet create \
  --name cap16-vnet \
  --resource-group cap16-rg \
  --location eastus \
  --address-prefix 10.0.0.0/16 \
  --subnet-name cap16-subnet \
  --subnet-prefix 10.0.1.0/24
```

### Step B2: Verify the VNet

```bash
az network vnet show \
  --name cap16-vnet \
  --resource-group cap16-rg \
  --query "{name:name, addressSpace:addressSpace.addressPrefixes, subnet:subnets[0].addressPrefix}" \
  --output json
```

### Step B3: Navigate to the VNet in the Portal

1. In the Azure Portal, navigate to **Virtual networks** > **cap16-vnet**.
2. Click **Subnets** in the left menu to confirm the subnet `cap16-subnet` is present with the correct address range.

### Deliverable B

Screenshot of the Azure Portal showing the VNet Subnets page with `cap16-subnet` (10.0.1.0/24) visible. Label it **CapB-VNet-Subnet**.

---

## Part C: Deploy a Linux Web Server VM (20 minutes)

### Step C1: Create the VM

This command creates a B1s VM (free-tier eligible) in the VNet created in Part B.

```bash
az vm create \
  --resource-group cap16-rg \
  --name cap16-vm \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s \
  --vnet-name cap16-vnet \
  --subnet cap16-subnet \
  --public-ip-sku Standard \
  --tags Environment=Lab Project=CIS4331-Capstone
```

The command outputs the VM's public IP address. Copy and save it.

### Step C2: Open HTTP Port

```bash
az vm open-port \
  --resource-group cap16-rg \
  --name cap16-vm \
  --port 80
```

### Step C3: SSH In and Install a Web Server

Replace `<PUBLIC_IP>` with the IP from Step C1.

```bash
ssh -o StrictHostKeyChecking=no azureuser@<PUBLIC_IP>
```

Inside the SSH session:

```bash
sudo apt-get update -y
sudo apt-get install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Create a custom index page
sudo bash -c 'cat > /var/www/html/index.html << EOF
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lone Star Tech — Powered by Azure</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; padding: 60px; background: #e8f4fd; }
    h1 { color: #0078d4; }
  </style>
</head>
<body>
  <h1>Welcome to Lone Star Tech</h1>
  <p>Deployed on Azure App Infrastructure</p>
  <p>CIS-4331 Capstone Lab | Texas Wesleyan University</p>
</body>
</html>
EOF'

exit
```

### Step C4: Verify the Web Server

In your browser, navigate to `http://<PUBLIC_IP>`. You should see the Lone Star Tech welcome page.

### Deliverable C

1. Screenshot of the browser showing the custom web page at the VM's public IP. Label it **CapC-WebServer-Browser**.
2. Screenshot of the Azure Portal showing `cap16-vm` in the Running state. Label it **CapC-VM-Running**.

---

## Part D: Create a Storage Account for Static Assets (10 minutes)

### Step D1: Create the Storage Account

Replace `[initials]` with your initials. Storage account names must be 3–24 characters, lowercase letters and numbers only, globally unique.

```bash
az storage account create \
  --name cap16storage[initials] \
  --resource-group cap16-rg \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2 \
  --access-tier Hot \
  --tags Environment=Lab Project=CIS4331-Capstone
```

### Step D2: Upload a Sample Asset

Create a sample file and upload it to a blob container.

```bash
# Create the container
az storage container create \
  --name assets \
  --account-name cap16storage[initials] \
  --public-access blob

# Create a sample file
echo "Lone Star Tech static asset file - CIS4331 Capstone" > sample.txt

# Upload the file
az storage blob upload \
  --account-name cap16storage[initials] \
  --container-name assets \
  --name sample.txt \
  --file sample.txt
```

### Step D3: Verify the Blob URL

```bash
az storage blob url \
  --account-name cap16storage[initials] \
  --container-name assets \
  --name sample.txt
```

Copy the URL and open it in a browser to confirm the file is publicly accessible.

### Deliverable D

1. Screenshot of the Azure Portal showing the storage account with the `assets` container. Label it **CapD-Storage-Container**.
2. Screenshot of the browser displaying the sample.txt content at the blob URL. Label it **CapD-Blob-Public-URL**.

---

## Part E: Apply Governance Controls (15 minutes)

### Step E1: Assign Reader Role to a Developer Account

Assign the Reader role on the resource group to simulate giving a developer read-only access.

```bash
# If you have a second account, replace <USER_EMAIL> with that email address
# If you do not have a second account, use any valid Azure email as a placeholder
az role assignment create \
  --assignee "<USER_EMAIL>" \
  --role "Reader" \
  --scope "/subscriptions/$(az account show --query id --output tsv)/resourceGroups/cap16-rg"
```

### Step E2: Verify the Role Assignment

```bash
az role assignment list \
  --resource-group cap16-rg \
  --output table
```

### Step E3: Create a Budget Alert

1. In the Azure Portal, navigate to **Cost Management + Billing** > **Cost Management** > **Budgets**.
2. Click **+ Add** and configure:
   - Name: `cap16-budget`
   - Reset period: Monthly
   - Amount: $10.00
3. Click **Next: Alerts** and add:
   - Condition 1: Actual — 80% — your university email
   - Condition 2: Forecasted — 100% — your university email
4. Click **Create**.

### Step E4: Verify Resource Tags

```bash
az resource list \
  --resource-group cap16-rg \
  --query "[].{Name:name, Type:type, Tags:tags}" \
  --output table
```

Confirm that the VM and storage account both show the `Environment=Lab` and `Project=CIS4331-Capstone` tags.

### Deliverable E

1. Screenshot of `az role assignment list` output showing the Reader assignment. Label it **CapE-RBAC-Assignment**.
2. Screenshot of the Azure Portal showing the completed budget with two alert conditions. Label it **CapE-Budget-Config**.
3. Screenshot of `az resource list` output showing resource tags. Label it **CapE-Resource-Tags**.

---

## Part F: Pricing Calculator Estimate (15 minutes)

Using the Azure Pricing Calculator at azure.microsoft.com/en-us/pricing/calculator/, build an estimate for the Lone Star Tech workload you just deployed.

### Step F1: Add the Virtual Machine

- Region: East US
- Operating System: Linux
- Instance: Standard_B1s (1 vCPU, 1 GiB RAM)
- Hours: 730 (full month, pay-as-you-go)

Record the monthly VM cost: **$___________**

### Step F2: Add the Storage Account

- Region: East US
- Type: Block Blob Storage
- Redundancy: LRS
- Capacity: 100 GB
- Write operations: 1,000 per month
- Read operations: 10,000 per month

Record the monthly storage cost: **$___________**

### Step F3: Record Total

Total estimated monthly cost for both services: **$___________**

### Step F4: Export the Estimate

Click **Export** and download the Excel file. Open it and confirm the line items appear.

### Deliverable F

1. Screenshot of the Pricing Calculator showing both services and the total estimate. Label it **CapF-Pricing-Estimate**.
2. The two individual cost values and the total, filled in above.

---

## Part G: Architecture Summary and AZ-900 Domain Mapping (10 minutes)

Complete the following table in your lab document. For each resource you deployed, identify the AZ-900 exam domain it falls under and the service model (IaaS, PaaS, or SaaS).

| Resource Deployed | Azure Service | AZ-900 Domain | Service Model |
|---|---|---|---|
| cap16-rg | Resource group | Azure Management and Governance | N/A |
| cap16-vnet / cap16-subnet | Azure Virtual Network | Azure Architecture and Services | IaaS |
| cap16-vm | Azure Virtual Machine | Azure Architecture and Services | IaaS |
| cap16storage[initials] | Azure Blob Storage | Azure Architecture and Services | PaaS |
| Reader role assignment | Azure RBAC | Azure Management and Governance | N/A |
| cap16-budget | Azure Cost Management | Azure Management and Governance | N/A |
| Resource tags | Azure Tags | Azure Management and Governance | N/A |

Write a 2–3 sentence explanation of how this lab illustrates the shared responsibility model. Specifically: for the Linux VM, which security responsibilities belong to you (the customer) and which belong to Microsoft?

### Deliverable G

Completed domain mapping table with the shared responsibility explanation written below it.

---

## Part H: Cleanup (5 minutes)

After submitting your lab, delete all resources.

```bash
az group delete \
  --name cap16-rg \
  --yes \
  --no-wait
```

Confirm the resource group appears with status "Deleting" in the Azure Portal under Resource groups. You do not need to wait for deletion to complete before submitting.

---

## Submission Requirements

Submit all of the following to Canvas by the posted deadline.

| Screenshot / Document | Label |
|---|---|
| Resource group with tags | CapA-ResourceGroup-Tags |
| VNet Subnets page | CapB-VNet-Subnet |
| Browser showing custom web page | CapC-WebServer-Browser |
| Portal showing VM in Running state | CapC-VM-Running |
| Storage account with assets container | CapD-Storage-Container |
| Browser showing blob public URL | CapD-Blob-Public-URL |
| az role assignment list output | CapE-RBAC-Assignment |
| Budget with two alert conditions | CapE-Budget-Config |
| az resource list showing tags | CapE-Resource-Tags |
| Pricing Calculator estimate | CapF-Pricing-Estimate |
| Pricing Calculator individual + total costs (filled in) | Part F values |
| AZ-900 domain mapping table | Part G |
| Shared responsibility explanation | Part G |

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A — Resource group with tags | 5 | All three tags visible |
| Part B — VNet and subnet | 10 | Correct address ranges; subnet confirmed in portal |
| Part C — VM and web server | 20 | VM running; nginx serving custom page; both screenshots submitted |
| Part D — Storage account and blob | 15 | Container created; blob publicly accessible at URL |
| Part E — Governance controls | 15 | RBAC assignment shown; budget with two alerts created; tags on all resources |
| Part F — Pricing Calculator | 10 | Both services estimated; costs recorded; export screenshot included |
| Part G — Architecture mapping and Shared Responsibility | 5 | Table completed accurately; shared responsibility explanation is correct |
| **Total** | **80** | Component 1 portion of Module 16 grade |

---

## Component 2: AZ-900 Certification Exam (20 points)

### Instructions

1. Register for the official Microsoft AZ-900 exam through the on-campus Pearson VUE testing center or an authorized online proctoring provider. Use your .edu email to access any available academic discount.
2. Complete the exam.
3. Obtain your official score report PDF. The report will show your full name, the exam name (AZ-900 Microsoft Azure Fundamentals), your scaled score (passing = 700/1000), pass/fail status, and the exam date.
4. Upload the score report PDF to the Canvas assignment box for this module.

### Exam Registration Resources

- Microsoft Certification portal: learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/
- Exam skills outline: learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900
- Free practice assessment (50 questions): learn.microsoft.com/en-us/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23
- John Savill's AZ-900 Study Cram (YouTube): youtube.com/watch?v=tQp1YkB2Tgs

### Grading

| Component | Points |
|---|---|
| Official AZ-900 score report submitted (any score) | 10 |
| Official AZ-900 score report showing passing status (700+) | 10 additional |
| **Total** | **Up to 20** |

Students who do not pass on their first attempt will receive 10 points for attempting the exam and submitting the score report. The additional 10 points require a passing score.

---

## Part 9 — Challenge Exercise

### Challenge 1: AZ-900 Domain Gap Analysis and Targeted Review

Take the official Microsoft Learn AZ-900 Practice Assessment (50 questions) and record your score by domain. For each of the three exam domains — Cloud Concepts, Azure Architecture and Services, and Azure Management and Governance — record how many questions you answered correctly versus incorrectly. For the domain with the lowest score, identify the three specific topic areas within that domain where you missed the most questions. For each of those three topic areas, locate the corresponding Microsoft Learn module, read it in full, and document the two most important concepts you reinforced. Then retake the practice assessment a second time and record the score improvement. Submit: your first and second practice assessment scores by domain, the three targeted topic areas you studied, the two key concepts per topic area, and a 2–3 sentence reflection on which study approach (reading module content, hands-on lab practice, or flashcard review of key terms) was most effective for your learning style and why.

### Challenge 2: AZ-900 Scenario Practice — Service Selection Justification

For each of the following six real-world business scenarios, identify the single most appropriate Azure service or feature, state which AZ-900 exam domain the scenario falls under, and write 2–3 sentences justifying your answer by explaining why the chosen service fits and why the most plausible alternative does not.

(a) A startup needs to host a static website with global low-latency delivery and no server management.

(b) A bank requires that all Azure resource deletions in production subscriptions require two-person approval and cannot be executed immediately.

(c) A logistics company needs to send millions of telemetry events per second from IoT sensors to a processing pipeline without losing any messages.

(d) A hospital needs to run SQL Server workloads in Azure while maintaining near-100% SQL Server feature compatibility and without changing their existing application connection strings.

(e) A media company wants to automatically reduce costs on 2 TB of video archive files that have not been accessed in 180 days.

(f) A development team wants to test infrastructure changes in an isolated copy of their production environment that is automatically destroyed after 8 hours.

### Reflection Questions

1. The AZ-900 exam tests three domains weighted at approximately 25–30%, 35–40%, and 30–35%. A student who has completed all 16 modules of this course asks: "If I only have 4 hours left to study, how should I allocate my time across the three domains to maximize my score?" Provide a specific time allocation recommendation with justification. In your answer, reference which specific topic clusters within the highest-weighted domain have the most real-world exam scenario coverage, and explain why understanding the relationships between services — for example, how Azure Policy, Management Groups, and RBAC work together — is more valuable for the AZ-900 exam than memorizing isolated service definitions.

2. After passing the AZ-900 exam, a student asks what Azure certification to pursue next. Compare AZ-104 (Azure Administrator), AZ-204 (Azure Developer), and AZ-305 (Azure Solutions Architect Expert) in terms of: the role they prepare for, the prerequisite knowledge they build on from AZ-900, the approximate additional study time required beyond AZ-900, and one specific skill from this course (CIS-4331) that directly prepares you for each certification. Then recommend which certification path is most appropriate for a student planning a career as a cloud infrastructure engineer versus a student planning a career as a cloud application developer.

---

End of Lab — Module 16
