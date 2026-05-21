# Reading Guide: Module 11 - Azure Security Tools

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 11 - Azure Security Tools**! This module covers Azure's cloud security services as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. AZ-900 tests your understanding of what each security tool does, not deep configuration details. You need to match a described security requirement to the correct Azure service.

You will learn what Microsoft Defender for Cloud does for security posture management and threat protection, how Azure Key Vault secures secrets and keys, and how Microsoft Sentinel operates as a cloud-native SIEM/SOAR. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Microsoft Defender for Cloud**: A cloud security posture management (CSPM) and cloud workload protection platform (CWPP) that continuously monitors Azure resources for security misconfigurations, provides a Secure Score to measure the overall security posture, and generates actionable recommendations. Defender for Cloud also provides threat protection (formerly Azure Security Center and Azure Defender combined). The free tier provides CSPM for Azure; paid plans add threat detection for specific resource types.

* **Security Center**: The former name for Microsoft Defender for Cloud's CSPM component. It assessed the security configuration of Azure resources against security best practices and provided a Secure Score. On AZ-900, Security Center and Defender for Cloud may appear as synonyms — both refer to Azure's unified security management dashboard.

* **Azure Key Vault**: A managed service for securely storing and controlling access to secrets (API keys, passwords, connection strings), cryptographic keys, and SSL/TLS certificates. Applications retrieve secrets from Key Vault via Azure-authenticated API calls, eliminating the need to hardcode sensitive values in source code or configuration files. Key Vault provides audit logs for every access attempt.

* **Microsoft Sentinel (SIEM/SOAR)**: A cloud-native Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) solution. Sentinel collects security data from across the organization (Azure resources, Microsoft 365, on-premises, and third-party solutions), detects threats using analytics and AI, investigates incidents, and can automate responses through playbooks. It is the AZ-900 answer for enterprise-scale threat detection and response.

---

### 2. Certification Exam Tips

* **Key Vault use case**: AZ-900 frequently presents a scenario where an application needs to access a database password or API key. The best practice answer is always Azure Key Vault — never hardcode secrets in source code or configuration files.
* **Defender for Cloud vs. Sentinel**: Both are security services but different in scope. Defender for Cloud = proactive security posture management and workload-level threat protection within Azure. Sentinel = reactive SIEM for collecting, analyzing, and responding to security events across the entire organization (multi-cloud, on-premises).
* **Secure Score**: Defender for Cloud provides a Secure Score (0-100%) that measures how closely your Azure environment follows security best practices. AZ-900 may ask which service provides this metric — the answer is Microsoft Defender for Cloud.
* **Key Vault and Managed Identity**: The most secure way for an Azure resource (e.g., a VM or App Service) to access Key Vault is through a Managed Identity — no credentials are stored in the application. AZ-900 tests that this is the recommended approach.
* **Study Resource**: The Microsoft Learn security module covers Defender for Cloud, Key Vault, and Sentinel with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Security](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure security tools including Defender for Cloud, Key Vault, and Sentinel. Access it at [Microsoft Learn – AZ-900 Azure Security](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers Azure security tools for AZ-900 — watch the security section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Provision an Azure Key Vault resource**: Create a Key Vault in the Azure portal, configuring access policies (or RBAC mode) to restrict which identities can read or manage secrets.
* **Securely add a secret to the vault**: Add a secret (e.g., a database connection string) to the Key Vault using the portal. Observe that the value is stored encrypted and is not visible in plain text after creation.
* **Retrieve a secret using Azure CLI**: Use the Azure CLI command `az keyvault secret show --vault-name <name> --name <secret>` to retrieve the secret value, demonstrating authenticated programmatic access without hardcoding credentials.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure security tools unit in [Microsoft Learn – AZ-900 Azure Security](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the security section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for Key Vault provisioning, secret storage, and CLI retrieval.
* [ ] Proceed to the weekly hands-on lab activity.
