# Quiz: Module 16 - Final Exam Prep & AZ-900 Certification

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service should you use when you need to enforce that all Azure VMs deployed across your organization must use only approved VM SKU sizes, automatically blocking non-compliant deployments?

* A) Azure Advisor
* B) Azure Policy with a "Deny" effect
* C) Azure Resource Manager tags
* D) Microsoft Defender for Cloud Secure Score
* **Correct Answer:** B) Azure Policy with a "Deny" effect evaluates resource deployments against defined rules and blocks any that do not conform to the approved SKU list.
* **Distractor Analysis:**
  * *Why B is correct:* Azure Policy with Deny effect is the only mechanism that actively blocks non-compliant deployments at submission time.
  * *Why A is incorrect:* Azure Advisor provides recommendations — it cannot block deployments.
  * *Why C is incorrect:* Tags are metadata labels — they have no enforcement capability and cannot block deployments.
  * *Why D is incorrect:* Defender for Cloud's Secure Score measures overall security posture — it does not enforce deployment restrictions.

---

**Question 2**
A VM deployed in a single Azure datacenter fails due to a power outage in that datacenter. Which architecture change would most cost-effectively meet a 99.99% SLA for this VM workload going forward?

* A) Add a second VM in the same datacenter within the same Availability Set
* B) Deploy two identical VMs across two different Availability Zones in the same Azure region
* C) Enable auto-shutdown on the VM to reduce operational costs
* D) Move the VM to a Spot Instance to improve resilience
* **Correct Answer:** B) Two VMs deployed across separate Availability Zones within the same region achieve 99.99% SLA by ensuring no single datacenter failure can take down both instances.
* **Distractor Analysis:**
  * *Why B is correct:* Availability Zones are physically separate datacenters within a region. Two instances across zones gives 99.99% SLA per Microsoft's published guarantees.
  * *Why A is incorrect:* An Availability Set distributes VMs across fault/update domains within one datacenter or cluster area — it achieves 99.95% SLA but does not protect against full datacenter failure.
  * *Why C is incorrect:* Auto-shutdown reduces costs but has no effect on availability or SLA.
  * *Why D is incorrect:* Spot Instances are the least reliable option — they can be evicted with 30-second notice and are explicitly not suitable for high-availability workloads.

---

**Question 3**
A developer accidentally committed the Azure storage account access key to a public GitHub repository. Using Azure best practices, which immediate remediation steps are correct?

* A) Delete the GitHub repository and hope the key was not seen before deletion
* B) Rotate the storage account access key immediately to invalidate the exposed key, then store the new key in Azure Key Vault and update the application to retrieve it via Managed Identity
* C) Apply a CanNotDelete lock to the storage account to prevent unauthorized deletion
* D) Enable Azure DDoS Protection on the storage account's VNet
* **Correct Answer:** B) Rotating the key immediately invalidates the exposed credential. Storing the replacement key in Key Vault and using Managed Identity prevents future hardcoding.
* **Distractor Analysis:**
  * *Why B is correct:* This is the complete Microsoft-recommended response: rotate immediately (revoke exposure), then adopt Key Vault + Managed Identity (prevent recurrence).
  * *Why A is incorrect:* The key was already exposed publicly — simply deleting the repository does not invalidate the key. Anyone who saw it can still use it.
  * *Why C is incorrect:* A CanNotDelete lock prevents accidental resource deletion — it does not revoke an exposed access key or protect against unauthorized API calls using that key.
  * *Why D is incorrect:* DDoS Protection defends against volumetric network attacks — it does not protect storage accounts from API-level access using a valid (though stolen) key.

---

**Question 4**
Which combination of Azure cost management features best supports an organization that wants to (1) estimate costs before migrating to Azure, (2) monitor ongoing cloud spending, and (3) reduce costs on stable, predictable workloads?

* A) TCO Calculator + Azure Cost Management budgets + Azure Spot Instances
* B) Azure Pricing Calculator + Azure Cost Management budgets + Azure Reservations
* C) Azure Advisor + Azure Monitor + Azure Blueprints
* D) TCO Calculator + Azure Cost Management budgets + Azure Reservations
* **Correct Answer:** D) The TCO Calculator builds the pre-migration business case; Cost Management monitors ongoing spending; Reservations reduce costs for stable workloads.
* **Distractor Analysis:**
  * *Why D is correct:* TCO Calculator = pre-migration comparison. Cost Management budgets = ongoing monitoring and alerts. Reservations = commitment-based savings for predictable workloads.
  * *Why B is incorrect:* The Pricing Calculator estimates individual Azure service costs — for comparing total on-premises vs. Azure costs before migration, the TCO Calculator is the correct choice.
  * *Why A is incorrect:* Spot Instances are for interruptible workloads with no reliability guarantee — they are not appropriate for stable, predictable production workloads.
  * *Why C is incorrect:* Advisor, Monitor, and Blueprints are governance and observability tools — none of them address pre-migration cost estimation or commitment-based discounts.

---

**Question 5**
Looking across all AZ-900 domains, which statement correctly pairs each Azure service with its primary purpose?

* A) Azure Policy = proactive cost saving recommendations; Azure Advisor = blocking non-compliant deployments; Azure Monitor = managing identity and access.
* B) Azure Key Vault = storing secrets and certificates securely; Azure Bastion = browser-based RDP/SSH without VM public IPs; Azure ExpressRoute = private dedicated connectivity bypassing the public internet.
* C) Azure Availability Zones = disaster recovery across regions 300 miles apart; Azure Region Pairs = datacenter-level fault isolation within one region; ARM Templates = real-time cost monitoring.
* D) Microsoft Sentinel = proactive VM security posture scoring; Defender for Cloud = enterprise SIEM for multi-source log analysis; Azure Service Health = managing user identities.
* **Correct Answer:** B) Key Vault stores secrets; Bastion provides secure VM access without public IPs; ExpressRoute provides private dedicated connectivity — all three descriptions are accurate.
* **Distractor Analysis:**
  * *Why B is correct:* All three service-to-purpose mappings in option B are factually accurate and align with AZ-900 exam definitions.
  * *Why A is incorrect:* The services are swapped — Azure Advisor provides recommendations; Azure Policy blocks non-compliant deployments; Azure Monitor handles telemetry, not identity.
  * *Why C is incorrect:* The definitions are reversed — Availability Zones are datacenter-level isolation within one region; Region Pairs span geographic distances for regional disaster recovery.
  * *Why D is incorrect:* The services are swapped — Sentinel is the enterprise SIEM; Defender for Cloud provides security posture and Secure Score; Service Health reports Azure platform incidents, not identity management.
