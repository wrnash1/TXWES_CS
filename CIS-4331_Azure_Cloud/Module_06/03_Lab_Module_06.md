# Lab Activity: Module 06 - Azure Storage Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 60-75 minutes
**Submission:** Canvas LMS — Module 06 Lab Assignment
**Prerequisite:** Azure for Students subscription, Azure CLI authenticated

---

## Learning Objectives

By completing this lab you will be able to:

- Create an Azure Storage Account using Azure CLI
- Create blob containers and manage access permissions
- Upload, list, and download blobs using Azure CLI
- Change blob access tiers and observe the settings
- Explore Storage Browser in the Azure Portal

---

## Part A: Create Storage Account and Container (25 Points)

### Step 1: Create Resource Group and Storage Account (10 Points)

```bash
az group create \
  --name "cis4331-lab06-[your-initials]-rg" \
  --location "eastus"

az storage account create \
  --name "cis4331lab06[your-initials]" \
  --resource-group "cis4331-lab06-[your-initials]-rg" \
  --location "eastus" \
  --sku "Standard_LRS" \
  --kind "StorageV2" \
  --access-tier Hot
```

Note: Storage account names must be globally unique, 3-24 lowercase characters, no hyphens. If your initials cause a conflict, add two random digits.

Include both command outputs and answer:

1. What does the `--sku Standard_LRS` parameter specify? What type of redundancy is configured?
2. What does the `--access-tier Hot` parameter set as the default for blob storage?
3. The storage account name must be globally unique across all Azure customers worldwide. Why does Azure enforce this uniqueness requirement?

### Step 2: Create a Blob Container (10 Points)

```bash
az storage container create \
  --name "lab06-container" \
  --account-name "cis4331lab06[your-initials]" \
  --public-access off
```

Include the output and answer:

1. The container was created with `--public-access off`. What does this mean for anonymous access to blobs in this container?
2. What are the three options for container public access, and what does each allow?

### Step 3: Explore the Storage Account in Azure Portal (5 Points)

**[SHOW PORTAL — Navigate to portal.azure.com > Storage Accounts > your account]**

Navigate to your storage account in the Azure Portal. Take a screenshot of the "Overview" blade showing:

- Storage account name
- Resource group
- Location
- Performance tier
- Redundancy (should show "Locally redundant storage (LRS)")

---

## Part B: Blob Upload, List, and Download (30 Points)

### Step 1: Create Sample Files to Upload (5 Points)

Create two text files locally to use as test blobs. On Windows PowerShell or Command Prompt:

```bash
echo "This is test file 1 for CIS-4331 Module 06 lab" > testfile1.txt
echo "This is test file 2 for CIS-4331 Module 06 lab" > testfile2.txt
```

Confirm both files exist by listing the current directory.

### Step 2: Upload Blobs to the Container (10 Points)

```bash
az storage blob upload \
  --container-name "lab06-container" \
  --name "testfile1.txt" \
  --file "testfile1.txt" \
  --account-name "cis4331lab06[your-initials]"

az storage blob upload \
  --container-name "lab06-container" \
  --name "testfile2.txt" \
  --file "testfile2.txt" \
  --account-name "cis4331lab06[your-initials]"
```

Include both command outputs and answer:

1. Blobs in Azure Storage are identified by a combination of container name and blob name (path). What is the full blob path for testfile1.txt?
2. The `--name` parameter specifies the blob name within the container. If you used `--name "subfolder/testfile1.txt"`, where would the blob appear in the Azure Portal's Storage Browser?

### Step 3: List Blobs (5 Points)

```bash
az storage blob list \
  --container-name "lab06-container" \
  --account-name "cis4331lab06[your-initials]" \
  --output table
```

Include the table output. Confirm both blobs appear with their names and sizes.

### Step 4: Download a Blob (5 Points)

```bash
az storage blob download \
  --container-name "lab06-container" \
  --name "testfile1.txt" \
  --file "downloaded_testfile1.txt" \
  --account-name "cis4331lab06[your-initials]"
```

Include the output and verify the downloaded file contains the expected content.

### Step 5: Explore Storage Browser in Azure Portal (5 Points)

**[SHOW PORTAL — Navigate to Storage Account > Storage Browser]**

Navigate to your storage account, click "Storage browser" in the left menu, then click "Blob containers" and open `lab06-container`.

Take a screenshot showing both blobs listed in the Storage Browser.

---

## Part C: Blob Access Tiers and Redundancy Analysis (25 Points)

### Step 1: Change a Blob's Access Tier (10 Points)

Change testfile2.txt to the Cool access tier:

```bash
az storage blob set-tier \
  --container-name "lab06-container" \
  --name "testfile2.txt" \
  --tier Cool \
  --account-name "cis4331lab06[your-initials]"
```

Then verify the tier change:

```bash
az storage blob show \
  --container-name "lab06-container" \
  --name "testfile2.txt" \
  --account-name "cis4331lab06[your-initials]" \
  --query "properties.blobTier" \
  --output tsv
```

Include both command outputs and answer:

1. The blob was changed to Cool tier. What is the minimum retention period for Cool tier, and what happens if the blob is deleted before that period?
2. If this blob needed to be accessed every hour throughout the business day, would Cool tier be cost-effective? Explain using the access cost vs. storage cost trade-off.

### Step 2: Redundancy Analysis Exercise (15 Points)

Answer the following questions based on the redundancy comparison table in the reading guide:

**Scenario 1 (5 Points):** A nonprofit organization stores donation records in Azure Storage. The records are legally required to be retained for 7 years. A regional disaster in Texas could potentially destroy the primary datacenter. The organization has a very limited budget and cannot afford high storage costs. They can tolerate up to 1 hour of data loss (RPO = 1 hour) in a regional disaster scenario. Which redundancy option is most appropriate, and why?

**Scenario 2 (5 Points):** A financial trading platform stores real-time transaction logs that must be readable from both the primary and secondary regions simultaneously for regulatory audit purposes. The platform cannot tolerate any data loss (RPO = 0). Which redundancy option is most appropriate, and why? (Note: RA-GRS and RA-GZRS allow reading from the secondary region.)

**Scenario 3 (5 Points):** A university lab stores student project files. The data is reproducible (students can re-submit if lost). The lab pays per GB and wants the absolute lowest storage cost. High durability within a single datacenter is sufficient. Which redundancy option is most appropriate, and why?

---

## Part D: Storage Service Selection Analysis (20 Points)

For each scenario, identify the most appropriate Azure Storage service (Blob Storage, Azure Files, Queue Storage, or Table Storage) and provide a 2-3 sentence justification.

### Scenario 1 (5 Points)

A media streaming company stores millions of video files (MP4 format, averaging 4 GB each). The files are uploaded once and then served to end users through a CDN. The team needs an HTTP-accessible object store with lifecycle management to automatically move older videos to cheaper storage tiers.

**Your selection and justification:**

### Scenario 2 (5 Points)

A manufacturing company's legacy ERP system (running on Windows Server VMs) needs to access shared configuration files and report templates using a drive letter (e.g., Z: drive) mapped to a network share. Multiple VMs must read and write to the same files simultaneously.

**Your selection and justification:**

### Scenario 3 (5 Points)

An IoT platform collects temperature readings from 50,000 sensors. Each reading is a small record (sensor ID, timestamp, temperature value). The platform needs to store all readings for 2 years for trend analysis queries. Queries always look up a specific sensor's readings by sensor ID and time range. Cost must be minimized for this high-volume data.

**Your selection and justification:**

### Scenario 4 (5 Points)

A retail website processes online orders. When a customer completes checkout, the order details need to be passed to the inventory management system and the shipping system independently. Both systems are occasionally slow and may be temporarily unavailable during maintenance windows. No orders should be lost during these windows.

**Your selection and justification:**

---

## Resource Cleanup

```bash
az group delete \
  --name "cis4331-lab06-[your-initials]-rg" \
  --yes \
  --no-wait
```

Verify deletion in the Portal after 5 minutes.

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A: Storage account and container creation | 25 | Commands run, outputs included, questions answered |
| Part B: Blob upload, list, download | 30 | All commands run, outputs included, Portal screenshot |
| Part C: Access tier change + redundancy analysis | 25 | Tier change confirmed, all 3 redundancy scenarios answered accurately |
| Part D: Four scenario selections | 20 | Correct service selected (3 pts each) with adequate justification (2 pts each) |
| **Total** | **100** | |

---

## Troubleshooting

**Storage account name already taken:** Storage account names are globally unique. Add two random digits to your initials suffix.

**Authentication error on blob upload:** Run `az storage account show-connection-string --name [account-name] --resource-group [rg-name]` and use the connection string with `--connection-string` parameter instead of `--account-name`.

**Cool tier set-tier command fails:** The `set-tier` command on individual blobs requires the account to support blob-level tiering. GPv2 StorageV2 accounts support this. Verify your account was created with `--kind StorageV2`.
