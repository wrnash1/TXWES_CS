# Lab Activity: Module 13 - ERP Security & Roles
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

## Objective
Configure and verify systems matching the operational parameters of **ERP Security & Roles**.

---

## Prerequisites
*   Ensure you have access to a terminal or a runtime environment matching the course requirements (e.g., Linux, macOS, Windows, or a cloud/web terminal).
*   Ensure you have administrative privileges if required to install packages or configure system services.

---

## Step-by-Step Instructions
1. **Create user roles mapping permissions**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
2. **Audit roles for Separation of Duties (SoD) conflicts**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
3. **Document profile access scopes**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.

---

## Troubleshooting Guide
*   *Error:* `Permission Denied`
    * *Fix:* Remember to run administrative command sequences using `sudo` or execute with administrative privileges (e.g., Run as Administrator on Windows).
*   *Error:* `Command Not Found`
    * *Fix:* Verify your environmental path settings, or double-check if the utility package is installed.

---

## Deliverables
1. Document your completed steps with screenshots or terminal output logs showing successful execution.
2. Submit your completion report to your Canvas LMS assignment portal for grading.

---

## Part 9 — Challenge Exercise

### Challenge 1: Salesforce Security Architecture Design

A regional bank is deploying Salesforce Financial Services Cloud to manage retail banking relationships. The bank has four user groups: Retail Bankers (view and edit their own customer accounts), Branch Managers (view and edit all accounts in their branch), Regional Directors (view all accounts in their region — read only), and Compliance Officers (read all accounts and cases in the entire org — no edit rights). All customer Account records contain a sensitive "Credit Score" field that only Retail Bankers and their managers should see — Regional Directors and Compliance Officers must not see this field.

1. Design the complete Salesforce security configuration for this scenario. Specify: the OWD setting for the Account object, the Role Hierarchy structure (name the roles and their parent-child relationships), any Sharing Rules required, and the Field-Level Security configuration for the Credit Score field. Justify each decision.
2. A new requirement arrives: Compliance Officers need to run a report showing all Cases where a customer filed a dispute in the last 90 days, but they must not be able to see the case notes (a rich text field). How would you configure Case object security and Field-Level Security to meet this requirement without creating a new user license type?
3. The bank's IT audit team requests a list of all users who viewed any Account record containing a Credit Score above 750 in the past 30 days. Can Salesforce's standard audit tools (Setup Audit Trail, Login History, Field History Tracking) fulfill this request? Explain what each tool does capture and identify the gap in the request — what would need to be built (e.g., a custom trigger, Event Monitoring) to capture record-level view events?
4. Six months after go-live, a Retail Banker is promoted to Branch Manager. List every security configuration change the Salesforce administrator must make to complete this user's access transition — include Role Hierarchy, Profile, Permission Sets (if any), and any implications for records the user previously owned as a Retail Banker.

### Challenge 2: SAP SoD Conflict Resolution and Compensating Controls

A mid-size manufacturing company runs SAP S/4HANA. An external audit identifies the following SoD conflicts in the current role assignments:

* User ASMITH: has FB60 (Enter Vendor Invoice) AND F110 (Run Automatic Payment Program) — can create fictitious invoices and pay them
* User BJONES: has FK01 (Create Vendor Master) AND FB60 (Enter Vendor Invoice) — can create a fictitious vendor and immediately invoice it
* User CWILSON: has MIGO (Post Goods Receipt) AND MIRO (Post Vendor Invoice) — can receive goods and approve the matching invoice without a second reviewer
* User DJOHNSON: has CO03 (Display Production Order) AND KO88 (Settle Production Order) — can settle production orders and post variances to GL accounts

1. For each of the four users, identify: (a) the specific fraud or error scenario enabled by the conflict, (b) which authorization object(s) in PFCG must be separated to resolve the conflict, and (c) which of the four conflicts represents the highest financial risk and why.
2. The company has only six people in the finance and procurement team. Redesign the role assignments for the team to eliminate all four SoD conflicts. Specify which SAP transaction codes each of the six roles should include. You do not need to name all transactions — focus on separating the four conflicting pairs identified above and explain your assignment logic.
3. The CWILSON conflict (MIGO + MIRO) is particularly difficult to separate because the warehouse team is small and both steps happen rapidly after each other. Design a compensating control using SAP workflow or tolerance limits that reduces the fraud risk of this conflict without requiring full role separation. Be specific about the SAP configuration or feature used.
4. Write a one-paragraph risk assessment (75–100 words) for the CFO describing the ASMITH conflict (FB60 + F110) as the highest-risk violation, quantifying the potential financial exposure, and recommending the timeline for remediation.

### Reflection Questions

1. In Challenge 1, the Credit Score field-level security requirement illustrates that record-level sharing (who sees the record) and field-level security (who sees specific data within the record) are separate controls. Describe a real-world business scenario — outside of banking — where the same record must be visible to two different user groups but each group should see a different subset of fields on that record.
2. In Challenge 2, the CWILSON conflict (MIGO + MIRO) is common in small finance teams where staffing does not allow full role separation. Compensating controls reduce risk but do not eliminate it. At what point does a compensating control become insufficient — what conditions would force the company to hire an additional employee to achieve true SoD separation rather than relying on detective controls?
