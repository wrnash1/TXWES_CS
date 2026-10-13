# Lab Activity: Module 09 — Azure Storage

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 100 | AZ-900 Alignment: Describe Azure storage services

---

## Lab Overview

In this lab you will create an Azure Storage account, work with Blob Storage containers and access tiers, upload and manage files in an Azure File Share, and configure a Lifecycle Management policy to automate tier transitions. This lab gives you direct hands-on experience with the storage concepts most heavily tested on AZ-900.

**Estimated Time:** 60–75 minutes

**Prerequisites:**

- Active Azure account (free trial or student subscription)
- Azure Cloud Shell access
- Completion of Lab Modules 07 and 08

---

## Learning Objectives

By completing this lab you will be able to:

- Create an Azure Storage account with specific redundancy settings
- Create a Blob container and upload blobs using the Portal and CLI
- Change a blob's access tier and observe the tier change
- Configure a Lifecycle Management policy
- Create an Azure File Share and generate a mount command
- Describe the cost and access tradeoffs of each blob tier

---

## Part 1: Create the Resource Group and Storage Account (10 minutes)

**Step 1.1 — Create the Resource Group**

Open Azure Cloud Shell (Bash) and run:

```bash
az group create \
  --name lab09-rg \
  --location eastus
```

**Step 1.2 — Create the Storage Account**

Replace `[initials]` with your initials to ensure a globally unique name. Storage account names must be 3–24 characters, lowercase letters and numbers only.

```bash
az storage account create \
  --name lab09storage[initials] \
  --resource-group lab09-rg \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2 \
  --access-tier Hot
```

**Step 1.3 — Verify the Storage Account**

```bash
az storage account show \
  --name lab09storage[initials] \
  --resource-group lab09-rg \
  --query "{name:name, kind:kind, sku:sku.name, accessTier:accessTier}" \
  --output table
```

Confirm the output shows: kind = StorageV2, sku = Standard_LRS, accessTier = Hot.

[SHOW AZURE PORTAL] Navigate to Storage Accounts > lab09storage[initials] > Overview. Point out the Replication (LRS), Performance (Standard), and Access tier (Hot) fields.

---

## Part 2: Work with Blob Storage (20 minutes)

**Step 2.1 — Create a Blob Container via Portal**

1. In the Azure Portal, navigate to your storage account
2. Under **Data storage**, click **Containers**
3. Click **+ Container**
4. Name: `lab09-blobs`
5. Public access level: **Private (no anonymous access)**
6. Click **Create**

**Step 2.2 — Create Sample Files for Upload**

In Azure Cloud Shell:

```bash
# Create three sample text files
echo "This is a hot tier file - accessed daily." > hot-file.txt
echo "This is a cool tier file - accessed monthly." > cool-file.txt
echo "This is an archive tier file - accessed yearly." > archive-file.txt
```

**Step 2.3 — Get the Storage Account Key**

```bash
STORAGE_KEY=$(az storage account keys list \
  --resource-group lab09-rg \
  --account-name lab09storage[initials] \
  --query "[0].value" \
  --output tsv)

echo "Key retrieved successfully"
```

**Step 2.4 — Upload Blobs via CLI**

```bash
# Upload hot-file.txt
az storage blob upload \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --container-name lab09-blobs \
  --name hot-file.txt \
  --file hot-file.txt \
  --tier Hot

# Upload cool-file.txt
az storage blob upload \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --container-name lab09-blobs \
  --name cool-file.txt \
  --file cool-file.txt \
  --tier Cool

# Upload archive-file.txt
az storage blob upload \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --container-name lab09-blobs \
  --name archive-file.txt \
  --file archive-file.txt \
  --tier Archive
```

**Step 2.5 — List Blobs and Verify Tiers**

```bash
az storage blob list \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --container-name lab09-blobs \
  --query "[].{name:name, tier:properties.blobTier}" \
  --output table
```

All three blobs should be listed with their respective tiers (Hot, Cool, Archive).

**Step 2.6 — Change a Blob's Tier via Portal**

1. Navigate to your storage account > Containers > lab09-blobs
2. Click on `hot-file.txt`
3. Click **Change tier** in the toolbar
4. Change the tier from Hot to **Cool**
5. Click **Save**
6. Wait 10 seconds, then refresh the Properties tab and verify the tier changed to Cool

[SHOW AZURE PORTAL] Show the blob's Properties tab with the Access Tier field. Demonstrate changing the tier in the Portal.

**Step 2.7 — Attempt to Read an Archive Tier Blob**

In Cloud Shell:

```bash
# Attempt to download the archive blob (this will fail with ArchiveBlobRehydrationRequired)
az storage blob download \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --container-name lab09-blobs \
  --name archive-file.txt \
  --file downloaded-archive.txt
```

You should receive an error indicating that the blob is in the Archive tier and cannot be read without rehydration. This demonstrates why Archive tier has restrictions.

---

## Part 3: Configure Lifecycle Management (10 minutes)

**Step 3.1 — Create a Lifecycle Policy**

In the Azure Portal:

1. Navigate to your storage account > **Data management** > **Lifecycle management**
2. Click **+ Add a rule**
3. Rule name: `cost-optimization-rule`
4. Scope: **Apply rule to all blobs in your storage account**
5. Blob type: **Block blobs**
6. Click **Next: Base blobs**
7. Configure base blob transitions:
   - Tier to cool storage: **30** days after last modification
   - Tier to archive storage: **90** days after last modification
   - Delete the blob: **365** days after last modification
8. Click **Add**

**Step 3.2 — Verify the Policy**

```bash
az storage account management-policy show \
  --account-name lab09storage[initials] \
  --resource-group lab09-rg
```

The JSON output should show the three transition rules you configured.

[SHOW AZURE PORTAL] Show the Lifecycle Management policy diagram that visualizes the Hot → Cool → Archive → Delete timeline.

---

## Part 4: Create an Azure File Share (10 minutes)

**Step 4.1 — Create a File Share via CLI**

```bash
az storage share create \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --name lab09-fileshare \
  --quota 5
```

The `--quota 5` sets a 5 GiB storage limit on the file share.

**Step 4.2 — Upload a File to the Share**

```bash
# Create a sample file
echo "Azure Files lab test - $(date)" > fileshare-test.txt

# Upload to the file share
az storage file upload \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --share-name lab09-fileshare \
  --source fileshare-test.txt
```

**Step 4.3 — List Files in the Share**

```bash
az storage file list \
  --account-name lab09storage[initials] \
  --account-key $STORAGE_KEY \
  --share-name lab09-fileshare \
  --output table
```

**Step 4.4 — Get the Mount Command**

In the Azure Portal:

1. Navigate to your storage account > **File shares** > **lab09-fileshare**
2. Click **Connect**
3. Select **Windows** or **Linux** depending on your OS
4. Copy the displayed mount command (do not run it — just save it in your notes)

[SHOW AZURE PORTAL] Show the Connect panel with the automatically generated PowerShell or Linux mount command. Point out the SMB 3.0 connection string and the port (445).

---

## Part 5: Explore Storage Redundancy Options (5 minutes)

**Step 5.1 — View Redundancy Options**

In the Azure Portal:

1. Navigate to your storage account > **Configuration**
2. Note the current Replication setting (Standard_LRS)
3. Click the dropdown to see all available redundancy options

[SHOW AZURE PORTAL] Show the Replication dropdown with LRS, GRS, RA-GRS, ZRS, GZRS, RA-GZRS options. Show the primary and secondary region display for GRS.

**Step 5.2 — Change Redundancy via CLI**

For learning purposes, change the storage account from LRS to GRS:

```bash
az storage account update \
  --name lab09storage[initials] \
  --resource-group lab09-rg \
  --sku Standard_GRS
```

Verify the change:

```bash
az storage account show \
  --name lab09storage[initials] \
  --resource-group lab09-rg \
  --query "{name:name, sku:sku.name, secondaryLocation:secondaryLocation}" \
  --output table
```

Note the secondaryLocation — this is the paired region where GRS replicates your data.

---

## Part 6: Reflection Questions (5 minutes)

Answer in your lab submission document (2–3 sentences each):

**Question 1:** When you attempted to download the archive-file.txt in Part 2, you received an error. What would you need to do before that blob can be read? How does this behavior affect application design decisions about using the Archive tier?

**Question 2:** You created a Lifecycle Management policy that moves blobs to Archive after 90 days. What type of data would be a good candidate for this policy? What business or compliance scenario would benefit from the automatic Delete rule at 365 days?

**Question 3:** You changed the storage account's redundancy from LRS to GRS. What does GRS protect against that LRS does not? What additional cost is your organization accepting by making this change, and what business risk does that cost mitigate?

---

## Part 7: Cleanup Resources (5 minutes)

```bash
az group delete \
  --name lab09-rg \
  --yes \
  --no-wait
```

---

## Deliverables

Submit the following to Canvas:

1. **Screenshot 1** — CLI output of `az storage blob list` showing all three blobs with their tiers (Hot, Cool, Archive)
2. **Screenshot 2** — Azure Portal showing the blob's Properties tab after changing hot-file.txt to Cool tier
3. **Screenshot 3** — Error message received when attempting to download the Archive tier blob
4. **Screenshot 4** — Azure Portal showing the Lifecycle Management policy you configured
5. **Screenshot 5** — CLI output showing the storage account with GRS redundancy and the secondaryLocation field
6. **Reflection Document** — Answers to the three reflection questions

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Screenshot 1: All three blobs uploaded with correct tiers | 20 |
| Screenshot 2: Blob tier changed to Cool in Portal | 10 |
| Screenshot 3: Archive tier download error | 10 |
| Screenshot 4: Lifecycle Management policy configured | 20 |
| Screenshot 5: GRS redundancy with secondaryLocation | 15 |
| Reflection Q1: Archive rehydration explanation | 8 |
| Reflection Q2: Lifecycle policy use case | 8 |
| Reflection Q3: LRS vs. GRS risk and cost | 9 |
| **Total** | **100** |

---

## Troubleshooting Tips

**Storage account name invalid:** Account names must be 3–24 characters, lowercase letters and numbers only. No hyphens, underscores, or uppercase characters.

**Storage key command fails:** If `az storage account keys list` fails with an authorization error, ensure you are logged in to the correct Azure subscription with `az account show`.

**Blob upload fails with authentication error:** Verify the `$STORAGE_KEY` variable is set correctly. Re-run the key retrieval command and verify the output is a 512-character base64 string.

**Lifecycle policy not visible in CLI output:** Allow 30–60 seconds after creation before running the show command.

**File share port 445 blocked:** On university or corporate networks, port 445 (SMB) may be blocked. You can still create the file share and view it in the portal — just note that mounting it from a restricted network would require Azure VPN or ExpressRoute.

---

*Lab 09 — Module 09: Azure Storage | CIS-4331 | Texas Wesleyan University*

---

## Part 9 — Challenge Exercise

### Challenge 1: Blob Immutability Policy
Enable blob versioning on your storage account with `az storage account blob-service-properties update --enable-versioning true`. Then create a time-based immutability policy on the `lab09-container` container using `az storage container immutability-policy create --period 1` (1-day retention). Attempt to delete a blob in the container and document the error you receive. Lock the policy with `az storage container immutability-policy lock` and attempt the delete again. Document both error messages and explain in 2–3 sentences why a locked immutability policy is required for compliance use cases (such as SEC 17a-4 financial records retention) compared to an unlocked policy.

### Challenge 2: AzCopy Performance Test
Download the AzCopy tool from the Azure documentation (https://aka.ms/downloadazcopy). Generate a test file of approximately 100 MB using your OS tools. Use `azcopy copy` to upload the file to your storage account blob container, timing the transfer. Then use `azcopy sync` to sync a local directory containing 10 small files (create them with a script) to a blob container. Document the transfer speeds for both operations. Compare these speeds to the theoretical time to transfer 800 TB over a 200 Mbps internet connection (show your calculation) and explain why the Data Box approach used in Question 3 of this module's quiz is justified for large offline migrations.

### Reflection Questions
1. In the lab you changed the storage account redundancy from LRS to GRS. GRS replicates data asynchronously to a secondary region, meaning there may be a small replication lag (typically seconds). What is the implication of this asynchronous replication for the Recovery Point Objective (RPO) of a storage account if the primary region suffers a sudden complete failure? How does RA-GRS change the Recovery Time Objective (RTO) compared to GRS during a regional failover?
2. A developer proposes storing all application configuration secrets (API keys, database passwords) in Azure Blob Storage with a private container and a SAS token for access. Describe two specific security weaknesses of this approach compared to storing secrets in Azure Key Vault, and explain what Key Vault features address each weakness.
