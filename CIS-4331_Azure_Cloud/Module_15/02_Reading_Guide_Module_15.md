# Reading Guide: Module 15 - Azure Resource Manager (ARM) & CLI

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 15 - Azure Resource Manager (ARM) & CLI**! This module covers Azure's infrastructure management and deployment tools as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Understanding how to interact with Azure programmatically — through ARM templates, CLI, and Cloud Shell — is essential for real-world administration and appears on AZ-900 as tool identification questions.

You will learn how ARM templates enable declarative, repeatable infrastructure deployment, how Azure CLI and PowerShell provide command-line control of Azure resources, and how Azure Cloud Shell provides a browser-accessible shell without local installation. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **ARM Templates (Declarative JSON)**: Azure Resource Manager templates are JSON files that define the desired end-state of Azure infrastructure (resources, configurations, dependencies) in a declarative format. When you submit an ARM template, Azure ARM provisions all defined resources to match the specified state. ARM templates enable Infrastructure as Code (IaC) — repeatable, version-controlled, idempotent deployments. Bicep is a newer domain-specific language (DSL) that compiles to ARM JSON.

* **Azure CLI**: A cross-platform, command-line interface for managing Azure resources. Azure CLI commands start with `az` and run on Windows, macOS, and Linux. CLI is scripting-friendly and integrates well with CI/CD pipelines. Example: `az vm create` to provision a virtual machine. AZ-900 tests that CLI is a tool option alongside PowerShell and the Azure portal.

* **Azure Cloud Shell**: A browser-based shell environment accessible from the Azure portal (the `>_` icon at the top) or shell.azure.com. Cloud Shell provides both Bash (with Azure CLI) and PowerShell environments, pre-authenticated to your Azure subscription, without requiring any local software installation. It uses Azure Files to persist files between sessions.

* **PowerShell Module (Az module)**: The Azure PowerShell module (`Az`) provides cmdlets for managing Azure resources using PowerShell syntax. Commands follow the `Verb-AzNoun` pattern (e.g., `New-AzVM`, `Get-AzResourceGroup`). Like Azure CLI, it runs cross-platform and integrates with automation workflows. AZ-900 tests that PowerShell is an alternative to CLI for Azure management.

---

### 2. Certification Exam Tips

* **ARM Template file format**: AZ-900 tests that ARM templates are written in JSON. Bicep is a newer abstraction over ARM that compiles to JSON — Bicep files do not need to be hand-written JSON. If the exam asks about the native ARM template format, the answer is JSON.
* **Declarative vs. Imperative**: ARM templates are declarative (you define what you want; Azure figures out how to get there). CLI and PowerShell commands are imperative (you specify each step). AZ-900 may ask which approach is idempotent (running it multiple times produces the same result) — declarative ARM templates are idempotent.
* **Cloud Shell authentication**: Cloud Shell is automatically authenticated to your Azure subscription when you open it from the portal — no `az login` required. AZ-900 may ask which tool requires no local installation and is pre-authenticated — the answer is Azure Cloud Shell.
* **Idempotency of ARM**: Running the same ARM template multiple times does not create duplicate resources — it applies the defined configuration. This makes ARM templates safe to run repeatedly for compliance or re-deployment scenarios.
* **Study Resource**: The Microsoft Learn management tools module covers ARM templates, CLI, PowerShell, and Cloud Shell with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure management tools including ARM templates, Azure CLI, Cloud Shell, and PowerShell. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers Azure management tools for AZ-900 — watch the ARM and CLI section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Launch Azure Cloud Shell**: Open the Azure portal, click the Cloud Shell icon (`>_`) in the top navigation bar, and select Bash. Observe that you are pre-authenticated and that a storage account is created to persist your files.
* **Run `az group list --output table`**: In Cloud Shell, execute `az group list --output table` to list all Resource Groups in your subscription in a formatted table. Observe the Name, Location, and ProvisioningState columns.
* **Deploy a resource using a basic ARM template**: Create a simple ARM template JSON file in Cloud Shell that defines a storage account. Deploy it using `az deployment group create --resource-group <rg-name> --template-file <file.json>`. Verify the storage account appears in the portal.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure management tools unit in [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the ARM and CLI section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for Cloud Shell setup, CLI commands, and ARM template deployment.
* [ ] Proceed to the weekly hands-on lab activity.
