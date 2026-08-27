# Lab Activity: Module 03 - Azure Virtual Machines and Scale Sets

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 75-90 minutes
**Submission:** Canvas LMS — Module 03 Lab Assignment
**Prerequisite:** Azure for Students subscription, Azure CLI installed and authenticated

---

## Learning Objectives

By completing this lab you will be able to:

- Create an Azure resource group and deploy a Linux virtual machine using `az vm create`
- List VMs and inspect their properties using `az vm list` and `az vm show`
- Demonstrate the difference between stopped and deallocated VM states
- Start, stop, and deallocate VMs using CLI commands
- Verify VM power state using `az vm get-instance-view`
- Delete VMs and resource groups to avoid unnecessary charges

---

## Prerequisites

- Azure for Students subscription active (verify with `az account show`)
- Azure CLI version 2.50 or later (`az --version`)
- SSH client available (built into macOS, Linux; use Windows Terminal or Git Bash on Windows)

If your CLI is not authenticated, run:

```bash
az login
```

---

## Cost Warning

The lab VM uses the `Standard_B1s` size, which costs approximately $0.012 per hour (about $0.30 per day). Always deallocate your VM when you are not using it and delete the resource group at the end of the lab to stop all charges.

---

## Part A: Create a Resource Group and Deploy a Linux VM (30 Points)

### Step 1: Create a Resource Group (5 Points)

Create a dedicated resource group for this lab. Replace `[your-initials]` with your initials throughout:

```bash
az group create \
  --name "cis4331-lab03-[your-initials]-rg" \
  --location "eastus" \
  --tags "course=CIS4331" "module=03"
```

Include the full JSON output in your submission document. Identify the `provisioningState` value in the output.

### Step 2: Deploy a Linux VM (15 Points)

Deploy an Ubuntu 22.04 LTS virtual machine:

```bash
az vm create \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]" \
  --image "Ubuntu2204" \
  --size "Standard_B1s" \
  --admin-username "azureuser" \
  --generate-ssh-keys \
  --output json
```

This command may take 2-5 minutes to complete. When it finishes, include the full JSON output in your submission and answer:

1. What is the value of the `"powerState"` field in the output?
2. What is the public IP address assigned to the VM?
3. The VM was created with `--generate-ssh-keys`. Where on your local system are these keys stored (provide the file path)?

### Step 3: Verify Deployment in the Azure Portal (10 Points)

**[SHOW PORTAL — Navigate to portal.azure.com > Virtual Machines]**

Navigate to the Azure Portal and find your newly created VM under "Virtual Machines."

Take a screenshot of the VM Overview blade showing:

- VM name
- Resource group
- Location
- Size (Standard_B1s)
- Operating system
- Status (Running)

Include this screenshot in your submission.

---

## Part B: List and Inspect VMs (20 Points)

### Step 1: List All VMs in the Resource Group (5 Points)

```bash
az vm list \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --output table
```

Include the output in your submission. How many VMs are listed?

### Step 2: Show Detailed VM Information (10 Points)

```bash
az vm show \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]" \
  --show-details \
  --output json
```

From the JSON output, identify and document:

1. The value of `"storageProfile.osDisk.diskSizeGb"` — what is the OS disk size in GB?
2. The value of `"storageProfile.osDisk.managedDisk.storageAccountType"` — what storage tier is the OS disk?
3. The `"hardwareProfile.vmSize"` value — confirm this matches the size you specified
4. The `"provisioningState"` value

### Step 3: Get Current Power State (5 Points)

```bash
az vm get-instance-view \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]" \
  --query "instanceView.statuses" \
  --output json
```

Include the output. You should see two status entries:

- `ProvisioningState/succeeded` — deployment status
- `PowerState/running` — current power state

What does the `"PowerState/running"` status indicate about whether you are being billed for compute?

---

## Part C: Stop vs. Deallocate — The Cost Experiment (30 Points)

This is the most important part of the lab. You will observe the difference between stopping a VM (OS shutdown) and deallocating a VM (releasing compute resources), and verify the power state change.

### Step 1: Stop the VM (OS Shutdown) — Note Still Billed (10 Points)

```bash
az vm stop \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]"
```

Wait for the command to complete (approximately 30-60 seconds), then check the power state:

```bash
az vm get-instance-view \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]" \
  --query "instanceView.statuses[1]" \
  --output json
```

Include the power state output in your submission. Answer:

1. What is the `"PowerState"` value after running `az vm stop`?
2. According to the reading guide, is compute still being billed at this point?
3. How does this state differ from deallocation from a cost perspective?

### Step 2: Deallocate the VM — Compute Billing Stops (10 Points)

```bash
az vm deallocate \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]"
```

Wait for the command to complete (approximately 60-90 seconds), then check the power state:

```bash
az vm get-instance-view \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]" \
  --query "instanceView.statuses[1]" \
  --output json
```

Include the power state output in your submission. Answer:

1. What is the `"PowerState"` value after `az vm deallocate`?
2. Is compute now being billed? What about storage?
3. If you start this VM again after deallocation, which component of the VM might change compared to when it was first created?

### Step 3: Start the VM (5 Points)

```bash
az vm start \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]"
```

Wait for the command to complete, then verify the VM is running:

```bash
az vm get-instance-view \
  --resource-group "cis4331-lab03-[your-initials]-rg" \
  --name "lab03vm[your-initials]" \
  --query "instanceView.statuses[1]" \
  --output json
```

Confirm the power state is `"PowerState/running"` and include the output.

### Step 4: Summary Analysis (5 Points)

Write a 100-150 word explanation of why the `az vm deallocate` command is more cost-effective than `az vm stop` for a student developer who uses a lab VM during class hours (9 AM - 3 PM) but not overnight. Use the specific billing components from the reading guide in your explanation.

---

## Part D: Scale Set Awareness Exercise (20 Points)

This part does not require creating a Scale Set (which would exceed lab budget), but instead uses Portal exploration and scenario analysis to build understanding.

### Step 1: Explore Scale Set Configuration in the Azure Portal (10 Points)

**[SHOW PORTAL — Navigate to portal.azure.com > Virtual Machine Scale Sets > Create]**

Navigate to the Azure Portal and start the Virtual Machine Scale Set creation wizard (you do not need to complete the creation — stop before clicking "Review + Create"). Explore the configuration options and answer the following:

1. On the "Scaling" tab, what are the three instance count values you must configure? What does each one represent?
2. On the "Scaling" tab, what is the default "Scale-out" CPU threshold, and what does it mean in plain language?
3. What is the "Cool-down" period default, and why does it exist?
4. Take a screenshot of the Scaling tab showing these configuration options.

### Step 2: Scale Set Scenario Analysis (10 Points)

Read the following scenario and answer all three questions:

Tailwind Traders operates an e-commerce website that runs on a VM Scale Set with minimum 2 instances, maximum 10 instances, and default 3 instances. The Scale Set has the following autoscale rules:

- Scale-out: Add 2 instances when average CPU exceeds 80% for 5 minutes. Cool-down: 5 minutes.
- Scale-in: Remove 1 instance when average CPU drops below 20% for 10 minutes. Cool-down: 5 minutes.

The following CPU measurements occur over 30 minutes:

| Time | Average CPU |
|---|---|
| 9:00 AM | 15% |
| 9:05 AM | 82% |
| 9:10 AM | 86% |
| 9:15 AM | 78% |
| 9:20 AM | 14% |
| 9:25 AM | 16% |
| 9:30 AM | 18% |

Starting instance count at 9:00 AM is 3.

Answer:

1. At what time does the first scale-out event trigger, and how many instances does the Scale Set have immediately after?
2. The CPU drops below the scale-in threshold of 20% starting at 9:20 AM. At what time does a scale-in event fire (accounting for the cool-down period from any scale-out)?
3. What is the instance count at 9:30 AM?

---

## Part E: Resource Cleanup (Required — No Points, but required for completion)

Delete all resources created in this lab to avoid ongoing charges:

```bash
az group delete \
  --name "cis4331-lab03-[your-initials]-rg" \
  --yes \
  --no-wait
```

After approximately 5 minutes, verify the resource group has been deleted:

```bash
az group show --name "cis4331-lab03-[your-initials]-rg"
```

The expected output is an error stating the resource group was not found. Include this verification in your submission.

---

## Submission Requirements

Your submission must include:

1. Resource group creation output (Part A, Step 1)
2. VM creation JSON output and three questions answered (Part A, Step 2)
3. VM Overview Portal screenshot (Part A, Step 3)
4. VM list output (Part B, Step 1)
5. VM show JSON output and four fields identified (Part B, Step 2)
6. Power state output and question answered (Part B, Step 3)
7. Stop command output and three questions answered (Part C, Step 1)
8. Deallocate command output and three questions answered (Part C, Step 2)
9. Start command output confirming running state (Part C, Step 3)
10. Summary analysis paragraph (Part C, Step 4)
11. Scale Set Portal screenshot and four questions answered (Part D, Step 1)
12. Scale Set scenario analysis with three answers (Part D, Step 2)
13. Resource group deletion verification (Part E)

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A: Resource group creation | 5 | Output included, provisioningState identified |
| Part A: VM creation output + questions | 15 | Full output, all 3 questions answered accurately |
| Part A: Portal screenshot | 10 | Screenshot present with all required fields visible |
| Part B: VM list output | 5 | Output included |
| Part B: VM show output + fields identified | 10 | All 4 fields identified correctly from JSON |
| Part B: Power state output + question | 5 | Output included, billing question answered correctly |
| Part C: Stop command + questions | 10 | Output included, all 3 questions answered accurately |
| Part C: Deallocate command + questions | 10 | Output included, all 3 questions answered accurately |
| Part C: Start command verification | 5 | PowerState/running confirmed |
| Part C: Summary analysis | 5 | 100-150 words, billing components cited |
| Part D: Scale Set Portal screenshot + questions | 10 | Screenshot present, all 4 questions answered |
| Part D: Scale Set scenario analysis | 10 | All 3 scenario questions answered correctly |
| **Total** | **100** | |

---

## Troubleshooting

**VM creation fails with "Quota exceeded":** Student subscriptions have vCPU quotas per region. Try a different region (`westus2` or `centralus`) or select a smaller VM size.

**SSH key already exists warning:** If `~/.ssh/id_rsa` already exists, add `--ssh-key-values ~/.ssh/id_rsa.pub` instead of `--generate-ssh-keys`.

**`az vm get-instance-view` returns no powerState:** The VM may still be transitioning states. Wait 30 seconds and retry.

**Portal does not show VM:** Confirm you are viewing the correct subscription. Use the subscription filter in the Portal top navigation bar.

---

## Part 9 — Challenge Exercise

### Challenge 1: Compare Stop vs. Deallocate Billing States
Using Azure CLI, create a Standard_B1s Linux VM. Record its public IP address. Run `az vm stop` and then query the power state and public IP. Then run `az vm deallocate` and query both again. Document the difference in power state, public IP assignment, and — using the Azure Pricing Calculator — calculate the hourly cost difference between Stopped (allocated) and Deallocated states for the Standard_B1s size. Clean up the VM and resource group when finished.

### Challenge 2: Design a Scale Set Autoscale Policy
Without deploying resources, design a complete autoscale policy for a retail website that must handle the following traffic pattern: 9 AM–5 PM weekdays at moderate load (60% CPU), 5 PM–9 PM weekdays at peak load (85% CPU), and overnight at minimal load (10% CPU). Specify the minimum, default, and maximum instance counts, the scale-out and scale-in CPU thresholds and time windows, and the cool-down periods. Justify each value with a sentence explaining your reasoning. Then explain what the `--no-wait` flag does in `az vmss scale` and why it matters for automation scripts.

### Reflection Questions
1. During the lab you observed that `az vm stop` does not stop compute billing but `az vm deallocate` does. Why does Azure charge for a stopped-but-allocated VM? What physical resource is Azure reserving on your behalf that justifies the charge?
2. A colleague argues that VM Scale Sets are unnecessary because you can manually add VMs to a load balancer backend pool when traffic increases. What operational problems would arise with manual scaling that Scale Sets solve automatically?
