# Discussion Forum: Module 09 — Azure Storage

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 10 | Initial Post Due: Wednesday 11:59 PM | Peer Responses Due: Sunday 11:59 PM

---

## Instructions

Read all three scenarios below. Choose **one** scenario that interests you most and write your initial post responding to that scenario. Your initial post must be 175–225 words. Then respond to **two classmates** who chose different scenarios. Each peer response must be at least 75 words and add substantive insight beyond agreement.

---

## Scenario 1: Healthcare Data Archival Strategy

A regional hospital system generates approximately 4 TB of medical imaging data (MRI, CT scans, X-rays) per month. Under HIPAA regulations, medical records must be retained for a minimum of 7 years from the date of the patient's last visit. The hospital's IT director wants to minimize storage costs while meeting retention requirements. Regulatory auditors access records occasionally — maybe twice per year per patient — and typically need access within 24 hours. The hospital currently stores all images on local SAN storage costing $0.08/GB/month. Azure Blob Storage Hot tier costs approximately $0.018/GB/month; Cool costs $0.01/GB/month; Archive costs $0.00099/GB/month.

**Discussion Prompt:** Design a blob storage tiering strategy for this hospital. Which access tier would you assign to newly uploaded images? After how many months would you transition to Cool, and after how many months to Archive? Would Archive tier be appropriate given the 24-hour access requirement? Calculate the approximate monthly storage cost savings versus keeping everything in Hot tier for one year of data (4 TB/month × 12 = 48 TB). Show your reasoning.

---

## Scenario 2: Startup Global Redundancy Decision

A fast-growing SaaS startup has its primary Azure infrastructure in East US. They store customer data, user-uploaded files, and application backups in Azure Blob Storage. The startup's legal team has reviewed their customer SLA and determined that any data loss event would trigger $250,000 in contract penalties. The engineering team is debating which redundancy option to use: LRS ($0.0184/GB), ZRS ($0.0230/GB), GRS ($0.0368/GB), or GZRS ($0.0460/GB). They currently store 10 TB of total data. The CTO argues that GRS is overkill and LRS is sufficient because Azure's physical infrastructure is already reliable.

**Discussion Prompt:** Do you agree with the CTO's assessment that LRS is sufficient? What risks does LRS not protect against that GRS or GZRS would? Calculate the monthly cost difference between LRS and GRS for 10 TB of data. Given the $250,000 penalty risk, how do you frame the cost-benefit analysis of choosing GRS over LRS? Would you recommend GRS or GZRS, and why?

---

## Scenario 3: File Sharing Architecture Decision

A professional services firm has 200 employees spread across three offices (Dallas, Houston, Austin). Employees share proposal templates, contract templates, and project files using an aging Windows Server 2016 file server in the Dallas office. Employees in Houston and Austin experience slow access speeds because all SMB traffic routes through Dallas. The IT director wants to modernize the file sharing infrastructure and is considering two options: (1) Azure Files with Azure File Sync on each office's existing server, or (2) replacing the file server entirely with SharePoint Online (Microsoft 365). The firm works heavily with large CAD files (50–500 MB each) that are frequently opened, edited, and saved by multiple users.

**Discussion Prompt:** Compare Azure Files with Azure File Sync versus SharePoint Online for this scenario. Which solution would you recommend for the CAD file workflow, and why? How does Azure File Sync's cloud tiering feature address the bandwidth concerns of the Houston and Austin offices? What limitation of SharePoint Online makes it less suitable for large CAD files opened via SMB? Reference at least one specific Azure Files or Azure File Sync feature in your response.

---

## Peer Response Guidelines

When responding to a classmate:

- Add at least one consideration they did not address — cost calculation, compliance, latency, or a specific Azure feature
- If their cost calculation contains an error, point it out constructively and show the corrected figures
- If you would make a different tiering or redundancy decision, explain your reasoning with reference to specific Azure Storage behaviors
- Avoid responses that merely restate the original post or express general agreement without adding new analysis

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post directly addresses the scenario's specific constraints and requirements | 4 |
| Initial post references specific Azure Storage tiers, redundancy options, or features with technical accuracy | 2 |
| Peer response 1: substantive, adds new analysis, 75+ words | 2 |
| Peer response 2: substantive, adds new analysis, 75+ words | 2 |
| **Total** | **10** |

---

## Professor Nash Note

Storage architecture decisions look deceptively simple on the surface — "just store it in Azure" — but the real work is in understanding the cost structure, access patterns, compliance requirements, and failure scenarios that determine the right tier and redundancy option. Scenario 1 involves actual cost calculations; I encourage you to do the math and show your work. The numbers are real, and the difference between Hot and Archive over 7 years is striking. In Scenario 2, notice that the CTO's argument is not entirely wrong — Azure infrastructure is highly reliable — but "reliable enough for most cases" and "meets our SLA obligations" are different standards. That tension is worth exploring.

---

*Discussion 09 — Module 09: Azure Storage | CIS-4331 | Texas Wesleyan University*
