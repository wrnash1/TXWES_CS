# Quiz: Module 15 - Azure Resource Manager (ARM) & CLI

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What file format is used to write Azure Resource Manager (ARM) templates?

* A) XML
* B) JSON
* C) YAML
* D) CSV
* **Correct Answer:** B) ARM templates are written in JSON (JavaScript Object Notation), representing resources declaratively.
* **Distractor Analysis:**
  * *Why correct:* Native ARM templates use JSON format. Bicep is a higher-level language that compiles to ARM JSON but is not itself the ARM template format.
  * *Why C is incorrect:* YAML is used for Kubernetes manifests and some CI/CD pipeline definitions but is not the native format for ARM templates.

---

**Question 2**
Which of the following most accurately describes **Azure Cloud Shell**?

* A) A browser-based, pre-authenticated shell environment accessible from the Azure portal or shell.azure.com that provides Bash (with Azure CLI) and PowerShell without requiring any local software installation.
* B) A local command-line tool installed on Windows, macOS, or Linux that requires `az login` authentication before managing Azure resources.
* C) A cloud storage service that persists shell scripts and configuration files between Azure CLI sessions on a local machine.
* D) A virtual machine SKU optimized for running automation scripts and ARM template deployments at scale.
* **Correct Answer:** A) Azure Cloud Shell is a browser-based, pre-authenticated shell providing Bash and PowerShell without any local installation required.
* **Distractor Analysis:**
  * *Why A is correct:* Cloud Shell's key characteristics on AZ-900 are: browser-based, pre-authenticated to your subscription, no local install required, supports both Bash and PowerShell.
  * *Why B is incorrect:* That describes the locally installed Azure CLI — it requires `az login`, unlike Cloud Shell.
  * *Why C is incorrect:* Cloud Shell does use Azure Files for file persistence, but that is a feature of Cloud Shell, not its definition.
  * *Why D is incorrect:* Cloud Shell is a browser-based shell, not a VM SKU.

---

**Question 3**
An operations team needs to deploy the same virtual network configuration to 50 different Azure subscriptions reliably, with no risk of configuration drift between deployments. Which Azure tool is best suited for this?

* A) Azure CLI interactive commands run manually in each subscription
* B) Azure ARM template deployed using a Management Group-scope deployment
* C) Azure Advisor recommendations for each subscription
* D) Azure portal manual configuration for each subscription
* **Correct Answer:** B) ARM templates are declarative and idempotent — deploying the same template to all subscriptions guarantees consistent configuration with no drift.
* **Distractor Analysis:**
  * *Why B is correct:* ARM templates' declarative nature means the same JSON file produces identical results across all subscriptions. Management Group scope deployments can target multiple subscriptions simultaneously.
  * *Why A is incorrect:* Manual CLI commands across 50 subscriptions are error-prone and not idempotent — small variations in command execution can cause configuration drift.
  * *Why C is incorrect:* Advisor provides recommendations — it cannot deploy or configure network resources.
  * *Why D is incorrect:* Manual portal configuration across 50 subscriptions is highly error-prone and time-consuming — not suitable for consistent at-scale deployment.

---

**Question 4**
What is the key advantage of ARM templates being **declarative** compared to imperative scripting with Azure CLI or PowerShell?

* A) ARM templates are faster to execute than CLI commands because they bypass Azure Resource Manager.
* B) ARM templates allow you to define the desired end-state of infrastructure, and Azure determines how to achieve it — running the same template multiple times produces the same result (idempotency).
* C) ARM templates are written in Python, making them more readable than JSON-based CLI scripts.
* D) ARM templates require no Azure permissions — any user can deploy them regardless of RBAC role assignments.
* **Correct Answer:** B) ARM templates are declarative and idempotent — you specify what you want, Azure handles the how, and re-running the template never creates duplicates.
* **Distractor Analysis:**
  * *Why B is correct:* Declarative + idempotent is the core advantage of ARM templates over imperative scripting. This makes deployments safe to repeat for audits, disaster recovery, or re-deployment scenarios.
  * *Why A is incorrect:* ARM templates are processed through Azure Resource Manager — they do not bypass it.
  * *Why C is incorrect:* ARM templates are JSON, not Python. Bicep is a DSL that compiles to ARM JSON.
  * *Why D is incorrect:* ARM template deployments require appropriate RBAC permissions (at minimum Contributor at the target scope).

---

**Question 5**
An administrator needs to quickly list all Resource Groups in their Azure subscription using a command-line tool, without installing anything locally. Which combination of tool and command achieves this?

* A) Locally installed Azure CLI: `az group list --output table`
* B) Azure Cloud Shell (Bash): `az group list --output table`
* C) Azure PowerShell local install: `Get-AzResourceGroup`
* D) Azure portal search bar: type "Resource Groups"
* **Correct Answer:** B) Azure Cloud Shell provides a pre-authenticated, browser-based Bash environment — `az group list --output table` lists all Resource Groups with no local installation required.
* **Distractor Analysis:**
  * *Why B is correct:* Cloud Shell requires no local software, is pre-authenticated, and supports the `az` CLI commands — it is the tool that satisfies both "command-line" and "no local installation."
  * *Why A is incorrect:* A locally installed Azure CLI requires installation and `az login` authentication — it does not meet the "no local installation" requirement.
  * *Why C is incorrect:* Azure PowerShell local install also requires installation — it does not meet the no-install requirement.
  * *Why D is incorrect:* The portal search bar is a GUI, not a command-line tool — it does not execute CLI commands.
