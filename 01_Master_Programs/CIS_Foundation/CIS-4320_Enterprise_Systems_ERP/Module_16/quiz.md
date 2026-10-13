# Quiz: Module 16 — ERP Certification Exam Preparation and Capstone

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

This final quiz contains 10 synthesis questions drawn from all course modules. Each question is worth 10 points. Questions are designed to mirror the cross-topic integration style of professional certification exams. Select the single best answer. Distractor analysis is provided for instructor and student review.

---

## Question 1

An enterprise uses Salesforce for CRM and SAP S/4HANA for finance. A financial analyst reports that the Salesforce pipeline dashboard shows $42M but the SAP financial forecast shows $38M for the same period. What is the most likely root cause?

A. Salesforce dashboards always show inflated data due to how the running user is configured.

B. The Salesforce REST API rounds currency values, causing discrepancies.

C. The two systems define the metric differently — Salesforce likely shows total pipeline regardless of close probability, while SAP may show committed forecast only.

D. The SAP General Ledger is not updated in real time when Salesforce opportunities close.

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Running user settings affect which records are visible, not the accuracy of currency values within those records. A running user misconfiguration would cause wrong records to appear, not a consistent $4M discrepancy across a pipeline metric.
- **B:** Salesforce does not round currency values in a way that would produce a $4M discrepancy on a $42M figure. Currency precision settings exist but are not the standard cause of cross-system metric differences.
- **C — Metric definition mismatch (Correct):** This is the most common real-world cause of cross-system reporting discrepancies. Salesforce "pipeline" typically includes all open opportunities regardless of stage. SAP financial forecasting may use a weighted or committed-only view. Without aligned metric definitions and a common data dictionary, the same concept produces different numbers in each system.
- **D:** The SAP General Ledger records actual financial postings — invoices paid, revenue recognized. It would not contain forward-looking pipeline data at all. The discrepancy is not between a forecast and actuals; it is between two different forecasting methodologies applied to the same pipeline data.

---

## Question 2

A company is implementing both SAP S/4HANA and Salesforce simultaneously. The project team is debating whether to go live with both systems on the same date or to phase the go-live — SAP first, then Salesforce three months later. What is the strongest argument for a phased approach?

A. Salesforce and SAP cannot share the same organizational structure, so they must be implemented separately.

B. Phasing reduces the volume of change affecting users and staff simultaneously, lowering the risk of failed adoption for both systems.

C. SAP requires a Business Blueprint document that takes longer than Salesforce discovery, so a phased go-live is required by ASAP methodology.

D. A simultaneous go-live would exceed the Salesforce API call limits.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Nothing prevents Salesforce and SAP from sharing organizational structures or going live simultaneously. The systems can coexist and be integrated.
- **B — Change management risk reduction (Correct):** The strongest argument for phasing is change management. Asking users to simultaneously learn two new enterprise systems — both of which change how they do their jobs — doubles the cognitive and organizational burden. Adoption failures on one or both platforms are more likely when the change is this large. Phasing allows the organization to stabilize on one system before absorbing the second wave of change.
- **C:** ASAP methodology does not require phased go-live between separate systems. ASAP governs the SAP implementation process independently of any Salesforce project.
- **D:** API call limits are a per-org daily limit. A simultaneous go-live does not automatically exceed API limits. Integration volume is a design consideration but not a structural blocker.

---

## Question 3

An SAP GRC Access Risk Analysis identifies that a Finance user has both authorization object F_BKPF_BUK (post financial documents) and the authorization to create vendor master records. The GRC rulebook flags this as a critical SoD conflict. The Finance Manager says removing either authorization will prevent the user from doing their job. What is the most appropriate response?

A. Accept the risk and document it without taking any action.

B. Remove both authorizations and reassign the tasks to two separate users.

C. Implement a compensating control — such as a supervisory review of all vendor master changes made by this user — and document it as a formal mitigation in GRC.

D. Grant the user System Administrator access so the SoD rules no longer apply.

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Simply accepting the risk without documentation or mitigation is not compliant with SOX or most internal audit standards. All accepted risks must be formally documented in the GRC system with rationale and compensating controls.
- **B:** Removing both authorizations and reassigning is the ideal design-level solution. However, the Finance Manager has indicated that both are required for this user to perform their job. In small teams where full role separation is not possible, compensating controls are the recognized alternative. Option B may not be operationally feasible.
- **C — Compensating control with formal mitigation (Correct):** When an SoD conflict cannot be eliminated through role redesign, the standard approach is to implement a compensating control that detects or deters the abuse that the conflict enables. A supervisory review of all vendor master changes — comparing who created the vendor to who approved payments to that vendor — detects the fraud scenario that this SoD rule targets. The mitigation must be documented in GRC with the control owner, review frequency, and evidence retention requirements.
- **D:** Granting System Administrator access eliminates the SoD alert only because it makes the user's access too broad for GRC to flag individual conflicts — this is not a solution, it is an escalation of the problem. System Administrator access is almost never appropriate for business users.

---

## Question 4

A Salesforce Administrator is building a data integration to load 200,000 Contact records from a legacy HR system. The legacy system uses a numeric employee ID as the primary key. Salesforce does not have a matching field. What Salesforce configuration enables the Data Loader upsert to update existing contacts without creating duplicates?

A. Create a custom field on Contact with the "External ID" attribute; populate it with the employee ID during the initial load.

B. Use the standard Salesforce Contact ID field as the upsert key.

C. Enable duplicate management matching rules on Contact before loading.

D. Set the Contact OWD to Public Read/Write to allow the Data Loader to access all records.

**Correct Answer: A**

**Distractor Analysis:**

- **A — External ID field (Correct):** An External ID field on Contact holds the legacy system's key value. During upsert, Data Loader uses this field to match incoming records to existing Contacts. If a Contact with the specified external ID already exists, the record is updated. If not, a new record is created. This is the standard, recommended approach for integrating data from external systems with their own keys.
- **B:** The Salesforce Contact ID (18-character Salesforce ID) exists only after a record is created in Salesforce. For a legacy system that has never been integrated with Salesforce, these IDs do not exist in the source system. Using the standard ID as an upsert key requires first knowing the Salesforce IDs — which defeats the purpose of upsert.
- **C:** Duplicate management matching rules identify potential duplicates and show an alert or block the save — they do not serve as upsert keys for the Data Loader. Matching rules and External IDs serve different purposes.
- **D:** OWD settings control record visibility and edit access for users — they have no bearing on the Data Loader's ability to match records during an upsert. The Data Loader uses the running user's permissions, which must include access to the Contact object.

---

## Question 5

A company has implemented Salesforce dashboards for its executive team. The CFO opens the "Quarterly Revenue Dashboard" and sees different numbers than the VP of Sales sees when opening the same dashboard. Both executives have identical Salesforce profiles. What is the most likely cause?

A. The dashboard is a Dynamic Dashboard using "Run as logged-in user," and the CFO and VP of Sales own different Opportunity records.

B. The Salesforce Report is broken and shows random data for each viewer.

C. The two executives have different permission sets that grant different field-level access.

D. The dashboard was last refreshed at different times for each viewer.

**Correct Answer: A**

**Distractor Analysis:**

- **A — Dynamic Dashboard (Correct):** A Dynamic Dashboard renders using the logged-in user's own access permissions. If the CFO and VP of Sales have different role hierarchy positions (the VP sees their team's records; the CFO might have a separate role with different visibility), they will see different numbers even on the same dashboard. This is the expected and intended behavior of a dynamic dashboard. The scenario is the classic illustration of why running user configuration matters.
- **B:** Salesforce dashboards are deterministic — they show the data from the underlying report, filtered by the running user's access. They do not show random data.
- **C:** Permission sets can affect field-level access, which could cause certain field values to be hidden. However, the scenario specifically notes that both executives have identical profiles. If the dashboard is showing revenue totals that differ by millions of dollars, the cause is almost certainly record visibility (which records each person can see), not a hidden field.
- **D:** Dashboard refresh timing would show the same data to both viewers, just as of different points in time. The data would differ by the amount of change since the last refresh — not by the pattern of role-based ownership differences described here.

---

## Question 6

A company is building its SAP S/4HANA and Salesforce security models simultaneously. An access architect notes that the word "Role" means something completely different in each system. Which statement correctly describes the difference?

A. SAP Roles control object-level access; Salesforce Roles control field-level access.

B. SAP Roles are bundles of transaction codes and authorization profiles; Salesforce Roles are record-sharing positions in a hierarchy that have no impact on object or field permissions.

C. Salesforce Roles are equivalent to SAP Authorization Profiles.

D. Both systems use "Role" to mean the same thing — a named set of access rights assigned to users.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** In Salesforce, object-level access is controlled by Profiles and Permission Sets — not Roles. Roles in Salesforce are exclusively about record sharing. In SAP, Roles do control transaction access (via authorization profiles), but the comparison in option A is still incorrect.
- **B — Correct distinction (Correct):** This is the precise differentiator. An SAP Role (created in PFCG) bundles transaction codes and the authorization profile generated from them — it directly governs what transactions a user can execute. A Salesforce Role is a position in a hierarchy used only for record visibility (granting upward access to managers). The Salesforce Role has zero impact on which objects a user can access or which fields they can see — those are governed by profiles and permission sets.
- **C:** SAP Authorization Profiles are auto-generated from roles in PFCG. Salesforce permission sets are the closest Salesforce analog to an SAP authorization profile (a collection of access rights), not Salesforce roles.
- **D:** This is explicitly wrong. The same word means fundamentally different things in the two systems, which is a common source of confusion for professionals working across both platforms.

---

## Question 7

A 3PL company is retiring a legacy customer portal and replacing it with Salesforce Service Cloud. 500 enterprise customers currently log in to the legacy portal daily to check shipment status and raise service requests. What is the most important change management consideration for this migration?

A. Getting the IT team trained on Salesforce Service Cloud before go-live

B. Ensuring the Salesforce API limits are sufficient for 500 concurrent external users

C. Communicating the change to customers — external users who are not employees — early, clearly, and repeatedly; and providing a parallel-run period to build confidence

D. Scheduling the go-live during a low-traffic period such as a holiday weekend

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Internal IT training is important but is an internal operational readiness concern, not the most critical change management challenge. The harder problem is the external user adoption.
- **B:** API limits are a technical architecture concern, not a change management consideration. Capacity planning for 500 concurrent users is addressed in the design phase, not change management.
- **C — External customer communication (Correct):** Change management for a customer-facing system is qualitatively different from internal ERP change management. Customers are not employees — you cannot mandate training attendance, enforce adoption, or provide daily coaching support. If external customers are confused by the new portal, they call your support line, post on social media, or leave. Early, clear, repeated communication combined with a parallel-run period (where both old and new portals are available) gives customers time to learn the new interface before the old one is removed.
- **D:** Scheduling go-live during low-traffic periods reduces the volume of initial issues but does not address the adoption and communication challenge. It is a risk mitigation tactic, not a change management strategy.

---

## Question 8

A company's Salesforce implementation team is deciding between Change Sets and Salesforce DX for deploying metadata from sandbox to production. The team has five developers working on different features simultaneously, and they need the ability to review each other's changes before they are deployed. Which approach is better suited to this requirement?

A. Change Sets, because they support multi-developer simultaneous deployment workflows natively.

B. Salesforce DX with Git branching and pull request reviews, which enables code review before merging and deployment.

C. Data Loader, which can export and import metadata across orgs.

D. Importing the metadata directly via the Metadata API without a deployment tool.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Change Sets have significant limitations for multi-developer teams. They cannot track which sandbox a component came from, do not support branching or version control, and do not have a native code review workflow. Simultaneous development on change sets frequently leads to deployment conflicts and overwritten work.
- **B — Salesforce DX with Git branching and pull requests (Correct):** Salesforce DX stores metadata in a Git repository. Each developer works on a separate feature branch. When a feature is ready for review, the developer creates a pull request — a request to merge their branch into the main branch. Team members review the changes in the PR, leave comments, and approve before merging. This is the industry-standard development workflow that enables exactly the peer review requirement described in the scenario.
- **C:** Data Loader is designed for data records (Accounts, Contacts, Opportunities) — not for metadata (objects, fields, workflows, Apex classes). Using Data Loader to move metadata between orgs is not a supported deployment method.
- **D:** The Metadata API is the underlying mechanism that both Change Sets and Salesforce DX use. Using it directly without a deployment tool is possible for developers but does not provide the workflow management, version control, or code review capabilities the scenario requires.

---

## Question 9

Horizon Logistics is evaluating which Salesforce report format to use for a monthly executive dashboard showing: each regional director's total closed won revenue, broken down by customer industry sector, for the current fiscal year. The CFO wants to compare both dimensions simultaneously at a glance.

A. Tabular report exported to Excel, where the CFO can build a pivot table manually.

B. Summary Report with Director as the row grouping.

C. Matrix Report with Director on rows and Industry Sector on columns.

D. Joined Report with one block per Director.

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Exporting to Excel and using a pivot table is a manual workaround that undermines the purpose of a Salesforce dashboard. It requires the CFO to perform analysis steps that the reporting tool should automate.
- **B:** A summary report with a single row grouping by Director would show each director's total revenue in a vertical list. To see the industry breakdown, the CFO would need to expand nested groups — not the simultaneous comparison across both dimensions described in the scenario.
- **C — Matrix Report (Correct):** A matrix report with Director on rows and Industry Sector on columns creates a cross-tab grid where every cell shows the revenue for a specific director-industry combination. The CFO can immediately compare all directors side-by-side and see which industries drive the most revenue for each director — exactly the simultaneous two-dimension comparison requested.
- **D:** Joined reports combine multiple report types from different object sources. Using a separate block per director (up to five) would be unnecessarily complex and would not produce the grid format the CFO wants. A joined report is the wrong tool when the goal is a two-dimension comparison within a single report type.

---

## Question 10

An experienced SAP consultant advises a new client that "fit-to-standard" should be the guiding principle for their S/4HANA implementation. The client's CFO pushes back, saying "we have unique processes that SAP doesn't support." What is the best response to the CFO's concern?

A. Agree with the CFO — all unique processes must be replicated exactly in SAP, regardless of cost.

B. Explain that fit-to-standard means reviewing SAP's best practice processes first; custom development is reserved for truly differentiating capabilities that standard SAP cannot support at any reasonable configuration level.

C. Tell the CFO that SAP Activate eliminates the need for any customization.

D. Propose reverting to ASAP methodology, which requires full custom configuration.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Replicating all legacy processes exactly in SAP is the most expensive, highest-risk implementation approach. Many legacy processes exist because of limitations of the old system, not because they are inherently optimal. Fit-to-standard challenges the assumption that all legacy processes are worth preserving.
- **B — Fit-to-standard balanced with justified exceptions (Correct):** Fit-to-standard does not mean the organization has no choices. It means the default assumption is: use SAP's built-in process first; only customize when there is a documented business case that standard SAP cannot meet and the differentiation justifies the cost. The Discover phase of SAP Activate allows the client to evaluate standard processes in a working system before deciding whether they need customization. This is the nuanced, professional response to the CFO's concern.
- **C:** SAP Activate does not eliminate customization. It reduces unnecessary customization by making standard processes visible and accessible through pre-configured content. Complex or unique business requirements still require development.
- **D:** ASAP methodology does not "require full custom configuration." ASAP phases include a Blueprint phase that documents the client's process requirements against standard SAP capabilities. Customization decisions are made based on gaps identified in the Blueprint. Returning to ASAP does not address the CFO's concern at all.

---

## Quiz Summary

| Question | Topic | Correct Answer |
|----------|-------|----------------|
| 1 | Cross-system metric discrepancy — definition mismatch | C |
| 2 | Phased go-live — change management risk reduction | B |
| 3 | SoD compensating control with GRC documentation | C |
| 4 | External ID field for Data Loader upsert | A |
| 5 | Dynamic dashboard shows different data per viewer | A |
| 6 | SAP Role vs. Salesforce Role fundamental distinction | B |
| 7 | External customer change management for portal migration | C |
| 8 | Salesforce DX with Git for multi-developer review workflow | B |
| 9 | Matrix report for two-dimension executive comparison | C |
| 10 | Fit-to-standard balanced approach for unique processes | B |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*
