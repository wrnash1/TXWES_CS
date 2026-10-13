# Lab Activity: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Scenario: Northgate Community College

Northgate Community College (NCC) is a mid-sized institution with 8,200 enrolled students, 340 full-time employees, and 12 academic buildings. The IT department supports approximately 1,400 managed devices. Following a state IT audit, NCC's IT Director has been directed to establish a formal IT Asset Management program. The audit found the following:

- The IT department maintains a spreadsheet of hardware, but it was last updated 14 months ago
- Software license records exist for six of the eighteen software products in use; the other twelve have no entitlement documentation
- Three laptops reported stolen two years ago are still listed as active in the directory
- End-of-life computers being sent to a recycling vendor are not being sanitized before transfer
- Discovery scans have never been performed; there is no mechanism to detect unauthorized software

You are the newly assigned IT Asset Manager. You will work through four exercises to build the foundation of NCC's ITAM program.

---

## Exercise 1: Asset Lifecycle Classification (25 points)

Review the asset records below. For each asset, identify its current lifecycle stage (Planning, Procurement, Deployment, Maintenance/Operation, Retirement, or Disposal) and write one sentence justifying your classification.

**Asset 1:** A Cisco network switch purchased 18 months ago, currently installed in Building 7, actively routing traffic, covered by a current SmartNet maintenance contract.

- Lifecycle stage: _______________
- Justification: _______________

**Asset 2:** Twenty Dell laptops ordered last week to support the new nursing program launching next semester. The purchase order has been approved; the hardware has not yet arrived.

- Lifecycle stage: _______________
- Justification: _______________

**Asset 3:** A file server that was decommissioned six months ago after its data was migrated to cloud storage. The physical server is sitting in a storage room. Its hard drives have not been sanitized. It is still listed as "active" in the spreadsheet.

- Lifecycle stage: _______________
- Justification: _______________

**Asset 4:** The IT Director wants to replace all computer lab desktops in three buildings over the next fiscal year. A proposal is being developed to estimate the cost and required licensing.

- Lifecycle stage: _______________
- Justification: _______________

**Asset 5:** Forty tablets issued to adjunct faculty. The tablets are two years into a three-year lifecycle and are receiving regular OS updates.

- Lifecycle stage: _______________
- Justification: _______________

---

## Exercise 2: Software License Compliance Audit (25 points)

The IT department has completed a software discovery scan. The table below shows licensed entitlements versus discovered installations for five software products.

| Software Product | License Model | Entitlements Owned | Installations Discovered | Compliance Status |
|---|---|---|---|---|
| Adobe Acrobat Pro | Per-device | 45 | 67 | ? |
| Microsoft Office 365 | Per-user (named) | 340 | 298 | ? |
| AutoCAD 2024 | Per-device | 20 | 18 | ? |
| Zoom Education | Concurrent (50 users) | 50 concurrent | Peak usage: 71 | ? |
| Antivirus Platform | Subscription (expires 2025-06-30) | 1,400 seats | 1,387 installations | ? |

### Task 2a: Compliance Assessment

For each product, determine the compliance status. Use one of three designations: **Compliant**, **Under-licensed** (compliance risk), or **Over-licensed** (financial waste). Enter the status in the Compliance Status column and write one sentence explaining the basis for your determination.

### Task 2b: Risk Prioritization

Two of the five products represent legal compliance risk. Rank them by severity of risk and write a 100–150 word explanation of which should be remediated first and why. Consider both the magnitude of the gap and the license model's audit exposure.

### Task 2c: Over-licensing Action

One product is over-licensed. Write a 75–100 word recommendation describing what action NCC should take regarding the over-licensed entitlements and when it should take that action.

---

## Exercise 3: CMDB Gap Analysis (25 points)

NCC's IT Director wants to understand the gap between the current spreadsheet and a properly functioning CMDB. Review the following information about the existing spreadsheet and answer the questions below.

**Current spreadsheet contents:**

- Hardware list: 1,247 rows (asset tag, device type, model, serial number, building, last-known user)
- No software installations recorded
- No relationships between hardware assets and services
- Three rows flagged as "stolen — under investigation" from two years ago; no removal action taken
- Last updated: 14 months ago

### Task 3a: Key CMDB capabilities missing

List four specific CMDB capabilities that the spreadsheet does not provide. For each, write one sentence explaining why that missing capability creates a risk or cost to NCC.

### Task 3b: Discovery tool integration

NCC is considering purchasing a discovery tool to feed its new CMDB. Write a 100–150 word description of how a discovery tool would improve CMDB accuracy over the current spreadsheet approach. Include at least one example of a risk that discovery-fed CMDB data would detect that the spreadsheet cannot.

### Task 3c: Stolen asset records

The three laptops reported stolen two years ago are still listed as active in the spreadsheet. What two actions should be taken regarding these records, and why does leaving them as active create a compliance and security risk?

---

## Exercise 4: Secure Disposal Procedure (25 points)

NCC is preparing to retire 85 computer lab desktops. These machines contain student academic records, faculty grades, and locally cached login credentials from student users. The college's recycling vendor will pick up the hardware and either refurbish it for resale or shred it.

### Task 4a: Data sanitization selection

For each of the three sanitization methods described below, evaluate whether it is appropriate for NCC's situation. Provide a one-sentence justification for each evaluation.

- **Physical destruction (shredding/degaussing):** Appropriate or not? Justification: _______________
- **Cryptographic erasure:** Appropriate or not? Justification: _______________
- **Software-based overwriting (NIST SP 800-88):** Appropriate or not? Justification: _______________

### Task 4b: Disposal procedure

Write a step-by-step disposal procedure for the 85 desktops. Your procedure must include at minimum:

1. Pre-disposal verification (confirming the asset is authorized for disposal and not pending investigation)
2. Data backup confirmation (verifying any needed data has been migrated before sanitization)
3. Sanitization step with the method selected from Task 4a
4. CMDB record update
5. Documentation — what record is created and retained

### Task 4c: Regulatory consideration

NCC is subject to FERPA (Family Educational Rights and Privacy Act), which governs the protection of student education records. Write 75–100 words explaining how FERPA's data protection requirements relate to NCC's hardware disposal procedure and what documentation NCC should retain to demonstrate compliance.

---

## Submission

Submit your completed lab document to the Canvas assignment portal by the due date shown in the course schedule. Include all four exercises with substantive responses. One-word or one-phrase answers will not receive full credit — each response should demonstrate understanding of ITAM principles.

**Grading:** Each exercise is worth 25 points, distributed across the tasks within each exercise based on completeness, accuracy, and application of ITAM concepts.

---

## Part 9 — Challenge Exercise

### Challenge 1: CMDB Accuracy Recovery

A logistics company has operated without a formal CMDB for seven years. Asset information lives in three separate spreadsheets maintained by different teams, none of which are synchronized. An incident last month took 6.5 hours to resolve because the responders did not know which servers hosted the affected application and had to map dependencies manually during the outage.

The IT Director has approved a 90-day CMDB implementation project. The environment contains approximately 800 physical and virtual servers, 3,200 end-user devices, 140 network devices, and software licenses for 67 products across an estimated 2,400 users.

1. Define a CMDB scoping strategy for this organization. Which asset categories should be included as full configuration items with relationship mapping? Which should be tracked in a separate asset register with limited CMDB integration? Justify each decision using IT Asset Management and Service Configuration Management principles.

2. The three existing spreadsheets contain conflicting data — the same server appears in two spreadsheets with different hostnames, two different IP addresses, and two different owner assignments. Design a data reconciliation process for consolidating this data into the new CMDB. Your process should include at least four steps and address how conflicts are resolved when spreadsheet records contradict each other.

3. Calculate and explain the business case for CMDB accuracy, using the 6.5-hour incident as a reference point. What specific CMDB capabilities would have reduced the resolution time, and what is the organizational cost of continuing without those capabilities?

### Challenge 2: SAM Program Design

A 600-person professional services firm has never conducted a formal software asset management program. An IT team member recently discovered that the firm has active licenses for 14 software products that appear to have no active users in the past 12 months. The total annual cost of these 14 products is $380,000.

1. Design a SAM program launch plan for this organization. Your plan should include at minimum: (a) the data sources needed for an initial license baseline, (b) the reconciliation process for comparing entitlements to actual usage, and (c) the governance mechanism for ensuring new software purchases and deployments are captured going forward.

2. For the $380,000 in potentially unused software: describe the investigation process you would follow before recommending cancellation. What factors other than usage data would you consider, and why does each matter to the cancellation decision?

3. The firm's CEO asks: "We have a small IT team. Is a formal SAM program worth the overhead?" Construct a business case for SAM investment that addresses: license compliance risk, cost optimization opportunity, and the specific risk posed by the firm's current unmanaged state. Use quantitative reasoning where possible.

### Reflection Questions

1. The Module 13 reading guide states that CMDB inaccuracy creates risk, not just inconvenience. Using a specific example from either the lab scenario or the challenge exercise, explain a situation where CMDB inaccuracy would cause a worse outcome than simply not having a CMDB at all.

2. Software Asset Management is sometimes described as both a compliance function and a cost optimization function. Explain why these two objectives occasionally conflict with each other — identify a scenario where the action that best satisfies compliance is not the action that best optimizes cost — and explain how a mature SAM program resolves that tension.
