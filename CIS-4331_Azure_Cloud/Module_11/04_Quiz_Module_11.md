# Quiz: Module 11 - Azure Security Tools

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service is designed to securely store and control access to tokens, passwords, certificates, and API keys?

* A) Azure Bastion
* B) Azure Key Vault
* C) Microsoft Entra ID
* D) Azure Security Center
* **Correct Answer:** B) Key Vault provides centralized secrets, keys, and certificate storage with strict access controls.
* **Distractor Analysis:**
  * *Why correct:* Key Vault is purpose-built for secrets management — it stores sensitive values encrypted and provides audited, authenticated access via Azure APIs.
  * *Why A is incorrect:* Azure Bastion provides secure browser-based RDP/SSH to VMs — it does not store secrets or keys.

---

**Question 2**
Which of the following most accurately describes **Microsoft Sentinel**?

* A) A cloud-native SIEM and SOAR solution that collects security data across the organization, uses AI to detect threats, investigates incidents, and can automate responses through playbooks.
* B) A proactive security posture management tool that evaluates Azure resource configurations against security best practices and provides a Secure Score.
* C) A managed service that stores application secrets, cryptographic keys, and SSL certificates with audit logging and RBAC-based access control.
* D) A network firewall service that filters and inspects traffic flowing between Azure VNets and the public internet.
* **Correct Answer:** A) Microsoft Sentinel is a cloud-native SIEM/SOAR that collects and analyzes security signals across the organization to detect, investigate, and respond to threats.
* **Distractor Analysis:**
  * *Why A is correct:* Sentinel is Azure's enterprise SIEM — it ingests logs from Azure, Microsoft 365, on-premises, and third-party sources for threat detection and automated response.
  * *Why B is incorrect:* That describes Microsoft Defender for Cloud (formerly Security Center), which focuses on security posture and Secure Score within Azure.
  * *Why C is incorrect:* That describes Azure Key Vault, which stores secrets and certificates.
  * *Why D is incorrect:* That describes Azure Firewall, a managed network security service.

---

**Question 3**
An application hosted in Azure App Service needs to retrieve a database password at runtime without storing the credential in the application's source code or configuration files. Which combination of Azure services implements this as the most secure best practice?

* A) Store the password in an Azure Storage Blob with a private access policy
* B) Use Azure Key Vault to store the password and a Managed Identity on the App Service to authenticate to Key Vault
* C) Encode the password in Base64 and store it in an Azure App Service application setting
* D) Store the password in an Azure SQL Database table with column-level encryption
* **Correct Answer:** B) Azure Key Vault stores the secret securely, and Managed Identity allows the App Service to authenticate to Key Vault without any credentials stored in the application.
* **Distractor Analysis:**
  * *Why B is correct:* This is the Microsoft-recommended pattern: Key Vault holds the secret, and Managed Identity provides credential-free authentication — no secrets are stored anywhere in the application.
  * *Why A is incorrect:* Blob Storage is not a secrets management service and does not provide the audit trail, versioning, or access controls of Key Vault.
  * *Why C is incorrect:* Base64 is encoding, not encryption — a plaintext password encoded in Base64 is still easily readable by anyone with access to App Service settings.
  * *Why D is incorrect:* Storing an application credential inside the database that credential is used to access creates a circular dependency and is not a secrets management pattern.

---

**Question 4**
A security team wants to understand the overall security health of their Azure environment and get prioritized recommendations to reduce risk. Which Azure service provides this capability through a Secure Score?

* A) Microsoft Sentinel
* B) Azure Key Vault
* C) Microsoft Defender for Cloud
* D) Azure Monitor
* **Correct Answer:** C) Microsoft Defender for Cloud continuously evaluates Azure resources against security best practices and provides a Secure Score with prioritized recommendations.
* **Distractor Analysis:**
  * *Why C is correct:* Defender for Cloud's Secure Score (0-100%) measures overall security posture and provides actionable recommendations ranked by impact.
  * *Why A is incorrect:* Sentinel is a SIEM for threat detection and investigation — it does not provide Secure Score or proactive configuration recommendations.
  * *Why B is incorrect:* Key Vault stores secrets — it does not evaluate security posture or produce recommendations.
  * *Why D is incorrect:* Azure Monitor collects performance and operational telemetry — it does not assess security configuration or provide a Secure Score.

---

**Question 5**
Which Azure security service should an organization use to collect logs from Azure VMs, Microsoft 365, on-premises firewalls, and third-party security tools into a single platform for threat hunting and automated incident response?

* A) Microsoft Defender for Cloud
* B) Azure Key Vault audit logs
* C) Azure Network Watcher
* D) Microsoft Sentinel
* **Correct Answer:** D) Microsoft Sentinel is a cloud-native SIEM/SOAR designed to aggregate security data from diverse sources across the organization for unified threat detection, investigation, and automated response.
* **Distractor Analysis:**
  * *Why D is correct:* Sentinel's data connectors support Azure, Microsoft 365, on-premises, and hundreds of third-party sources — it is purpose-built for the multi-source, enterprise-scale scenario described.
  * *Why A is incorrect:* Defender for Cloud focuses on Azure workload protection and posture management — it is not a SIEM for aggregating multi-source logs.
  * *Why B is incorrect:* Key Vault audit logs track secret access events in Key Vault specifically — not a platform for aggregating cross-organization security signals.
  * *Why C is incorrect:* Azure Network Watcher diagnoses network connectivity and performance issues — it does not provide SIEM or SOAR capabilities.
