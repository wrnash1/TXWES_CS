# Lab Activity: Module 11 — Azure Identity, Security, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 100 | AZ-900 Alignment: Describe Azure identity, access, and security

---

## Lab Overview

In this lab you will explore Azure Role-Based Access Control by viewing and creating role assignments, create an Azure Key Vault, store a secret, and retrieve it using the Azure CLI. You will also explore Microsoft Defender for Cloud's security recommendations and Secure Score. This lab gives you hands-on experience with the identity and security services that are critical to every real Azure deployment.

**Estimated Time:** 60–75 minutes

**Prerequisites:**

- Active Azure account (free trial or student subscription)
- Azure Cloud Shell access
- Completion of Lab Modules 07–10

---

## Learning Objectives

By completing this lab you will be able to:

- View and interpret existing RBAC role assignments in the Azure Portal
- Create a new RBAC role assignment at the resource group scope
- Create an Azure Key Vault using the Azure CLI
- Store a secret in Key Vault and retrieve its value
- Configure Key Vault access using Azure RBAC
- Navigate Microsoft Defender for Cloud and interpret the Secure Score

---

## Part 1: Create the Resource Group (3 minutes)

```bash
az group create \
  --name lab11-rg \
  --location eastus
```

---

## Part 2: Explore RBAC in the Azure Portal (15 minutes)

**Step 2.1 — Navigate to IAM for the Resource Group**

1. In the Azure Portal, navigate to **Resource groups** > **lab11-rg**
2. In the left menu, click **Access control (IAM)**
3. Click the **Role assignments** tab

You will see the current role assignments on this resource group. Your account has the Owner or Contributor role because you created it.

**Step 2.2 — Check Your Effective Access**

1. Click the **Check access** tab
2. Under "Check access for a user, group, or service principal," click **User, group, or service principal**
3. Search for your own account name
4. Select your account

You should see "Check access" showing all roles you have on this resource group, including inherited roles from the subscription level.

[SHOW AZURE PORTAL] Show the Check Access panel with the list of roles and their assignment scopes (direct vs. inherited from subscription).

**Step 2.3 — View Available Built-In Roles**

1. On the Access control (IAM) page, click **+ Add** > **Add role assignment**
2. On the Role tab, scroll through the list of available built-in roles
3. Click on "Contributor" to see the permissions it grants
4. Click on "Reader" and compare its permissions to Contributor
5. Click on "Virtual Machine Contributor" — note that it is scoped to VM actions only

Do not complete the role assignment — click **Cancel** after exploring the role list.

**Step 2.4 — Assign Reader Role to a Test User**

For this step, if you have access to a second Azure account (a classmate or a test account), assign them the Reader role on the lab11-rg resource group. If you do not have a second account, use a placeholder email for learning purposes.

```bash
# Assign Reader role to a user at resource group scope
# Replace <USER_EMAIL> with the user's Azure email
az role assignment create \
  --assignee "<USER_EMAIL>" \
  --role "Reader" \
  --scope "/subscriptions/$(az account show --query id --output tsv)/resourceGroups/lab11-rg"
```

**Step 2.5 — Verify the Role Assignment**

```bash
az role assignment list \
  --resource-group lab11-rg \
  --output table
```

Review the output. Note the RoleDefinitionName, PrincipalName, and Scope columns.

[SHOW AZURE PORTAL] Navigate back to lab11-rg > Access control (IAM) > Role assignments tab. Show the Reader assignment you created.

---

## Part 3: Create an Azure Key Vault and Manage Secrets (25 minutes)

**Step 3.1 — Create the Key Vault**

Replace `[initials]` with your initials. Key Vault names must be globally unique, 3–24 characters.

```bash
az keyvault create \
  --name lab11kv[initials] \
  --resource-group lab11-rg \
  --location eastus \
  --sku standard \
  --enable-rbac-authorization true
```

The `--enable-rbac-authorization true` flag enables Azure RBAC for Key Vault access control (the recommended modern approach).

**Step 3.2 — Assign Key Vault Administrator Role to Yourself**

Get your user object ID:

```bash
MY_USER_ID=$(az ad signed-in-user show --query id --output tsv)
echo "My user object ID: $MY_USER_ID"

KEYVAULT_ID=$(az keyvault show \
  --name lab11kv[initials] \
  --resource-group lab11-rg \
  --query id \
  --output tsv)
echo "Key Vault Resource ID: $KEYVAULT_ID"
```

Assign the Key Vault Administrator role:

```bash
az role assignment create \
  --assignee $MY_USER_ID \
  --role "Key Vault Administrator" \
  --scope $KEYVAULT_ID
```

Wait 60 seconds for the role assignment to propagate before proceeding.

**Step 3.3 — Create Secrets in Key Vault**

```bash
# Store a database connection string as a secret
az keyvault secret set \
  --vault-name lab11kv[initials] \
  --name "DatabaseConnectionString" \
  --value "Server=lab10sqlserver.database.windows.net;Database=lab10db;User=sqladmin;Password=TxWes@2024!;"

# Store an API key as a secret
az keyvault secret set \
  --vault-name lab11kv[initials] \
  --name "ExternalApiKey" \
  --value "sk-test-abc123xyz789-cis4331"
```

**Step 3.4 — List Secrets in Key Vault**

```bash
az keyvault secret list \
  --vault-name lab11kv[initials] \
  --output table
```

Notice the output shows the secret names and metadata but NOT the secret values. This is by design — listing secrets does not reveal values.

**Step 3.5 — Retrieve a Secret Value**

```bash
az keyvault secret show \
  --vault-name lab11kv[initials] \
  --name "DatabaseConnectionString" \
  --query "value" \
  --output tsv
```

The secret value is returned. In a real application, this CLI pattern would be replaced by an SDK call from application code using a managed identity.

**Step 3.6 — Explore Key Vault in the Azure Portal**

1. In the Azure Portal, navigate to your Key Vault (lab11kv[initials])
2. Under **Objects**, click **Secrets**
3. Click on "DatabaseConnectionString"
4. Click on the current version
5. Click **Show Secret Value** — note that accessing the secret value here is an audited operation

[SHOW AZURE PORTAL] Show the Key Vault secrets list. Show the secret version details page. Show the "Show Secret Value" button. Navigate to Monitoring > Insights to show the Key Vault access activity log.

**Step 3.7 — Create a Key Vault Secret with Expiration**

```bash
# Set a secret that expires in 90 days
az keyvault secret set \
  --vault-name lab11kv[initials] \
  --name "TemporaryToken" \
  --value "temp-token-exp-90days" \
  --expires "$(date -u -d '+90 days' '+%Y-%m-%dT%H:%M:%SZ')"
```

On macOS/Cloud Shell, date syntax may vary. This demonstrates that Key Vault secrets can have expiration dates — important for rotating credentials.

---

## Part 4: Explore Microsoft Defender for Cloud (10 minutes)

**Step 4.1 — Navigate to Defender for Cloud**

1. In the Azure Portal search bar, type **Microsoft Defender for Cloud** and select it
2. Review the **Overview** page

Note the Secure Score percentage. If your subscription is new, the score may be low because few recommendations have been acted on.

**Step 4.2 — Explore Security Recommendations**

1. Click **Recommendations** in the left menu
2. Review the recommendations list — they are organized by security control areas
3. Click on one recommendation to see:
   - The affected resources
   - The remediation steps
   - The Secure Score impact if the recommendation is implemented

[SHOW AZURE PORTAL] Show the Recommendations list. Click on a specific recommendation (for example, "Enable MFA for accounts with write permissions on your subscription"). Show the affected resources and remediation steps.

**Step 4.3 — View Regulatory Compliance**

1. Click **Regulatory compliance** in the left menu
2. Review the compliance standards available (Microsoft Cloud Security Benchmark, PCI DSS, NIST SP 800-53, etc.)
3. Click on one standard to see individual control compliance status

Note: Many controls may show as non-compliant on a new subscription — this is expected and shows the work needed to achieve full compliance.

---

## Part 5: Reflection Questions (5 minutes)

Answer in your submission document (2–3 sentences each):

**Question 1:** You assigned the Reader role to a user at the resource group scope. What actions can this user perform on resources in lab11-rg? What actions are they specifically prevented from taking? If you assigned them the Reader role at the Subscription scope instead, how would their access differ?

**Question 2:** The Key Vault secret list command showed secret names but not values. Why does this design choice improve security? How does this contrast with storing a password in a configuration file or environment variable?

**Question 3:** Your Microsoft Defender for Cloud Secure Score is probably not 100%. Pick one recommendation you saw on the Recommendations page and explain: (a) what security risk it addresses, (b) what the remediation steps are, and (c) whether you would implement it in a production environment and why.

---

## Part 6: Cleanup Resources (5 minutes)

```bash
az group delete \
  --name lab11-rg \
  --yes \
  --no-wait
```

Note: Key Vault soft delete is enabled by default. Even after the resource group is deleted, the Key Vault enters a "soft-deleted" state for 90 days. If you need to immediately purge it:

```bash
az keyvault purge \
  --name lab11kv[initials] \
  --location eastus
```

---

## Deliverables

Submit the following to Canvas:

1. **Screenshot 1** — Azure Portal showing Access control (IAM) > Role assignments for lab11-rg (with Reader assignment visible)
2. **Screenshot 2** — CLI output of `az role assignment list` for lab11-rg
3. **Screenshot 3** — Azure Portal showing Key Vault secrets list (showing both secret names without values)
4. **Screenshot 4** — CLI output showing the retrieved DatabaseConnectionString value
5. **Screenshot 5** — Microsoft Defender for Cloud Recommendations page (showing at least one recommendation)
6. **Reflection Document** — Answers to the three reflection questions

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Screenshot 1: RBAC role assignments with Reader role visible | 15 |
| Screenshot 2: CLI az role assignment list output | 10 |
| Screenshot 3: Key Vault secrets list (names visible, values hidden) | 15 |
| Screenshot 4: CLI output showing retrieved secret value | 15 |
| Screenshot 5: Defender for Cloud recommendations page | 15 |
| Reflection Q1: RBAC scope and access explanation | 10 |
| Reflection Q2: Key Vault security design rationale | 10 |
| Reflection Q3: Defender for Cloud recommendation analysis | 10 |
| **Total** | **100** |

---

## Troubleshooting Tips

**Role assignment propagation delay:** Azure RBAC changes can take 1–5 minutes to propagate. If a role assignment is not appearing immediately, wait and refresh.

**Key Vault "Forbidden" error when setting secrets:** If you receive a 403 Forbidden error when setting secrets, the role assignment may not have propagated yet. Wait 60–90 seconds after the role assignment and try again.

**Key Vault name already exists:** Key Vault names are globally unique. If the name is taken, add more characters or a random number. Even soft-deleted Key Vaults reserve the name.

**Defender for Cloud shows no data:** If your subscription is brand new, Defender for Cloud may take up to 24 hours to populate recommendations. If the Recommendations list is empty, navigate to Overview and show the Secure Score section instead.

**`date` command syntax on Cloud Shell (Linux):** Cloud Shell uses Bash on Linux. The date command format shown should work. If it does not, use an explicit ISO date string: `"2024-12-31T00:00:00Z"`.

---

*Lab 11 — Module 11: Azure Identity, Security, and Governance | CIS-4331 | Texas Wesleyan University*
