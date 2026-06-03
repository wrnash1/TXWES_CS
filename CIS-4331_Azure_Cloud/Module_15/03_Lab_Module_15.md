# Lab Activity: Module 15 — Azure Compliance, Privacy, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Lab Overview

**Estimated Time:** 60–75 minutes
**Difficulty:** Beginner–Intermediate
**Azure Account Required:** Yes — Free Trial or Azure for Students account
**Prerequisites:** Module 14 completed; Azure portal access confirmed

In this lab you will explore the Microsoft Trust Center and Service Trust Portal, examine Azure Policy built-in definitions and assign a policy to a resource group, review the Azure Policy compliance dashboard, explore Microsoft Purview's data governance capabilities, and analyze a compliance scenario involving data residency and GDPR.

---

## Learning Objectives

By completing this lab you will be able to:

- Navigate the Microsoft Trust Center and locate compliance documentation
- Assign a built-in Azure Policy to a resource group and observe compliance evaluation
- Interpret the Azure Policy compliance dashboard
- Describe the capabilities of Microsoft Purview for data governance
- Apply data residency and GDPR concepts to a real-world scenario

---

## Part 1 — Microsoft Trust Center and Service Trust Portal (15 minutes)

### Task 1.1 — Explore the Trust Center

1. Open a browser and navigate to `https://www.microsoft.com/en-us/trust-center`
2. No sign-in is required for this step.
3. On the Trust Center home page, identify the four main sections.

   Record them here:

   - Section 1: _________________
   - Section 2: _________________
   - Section 3: _________________
   - Section 4: _________________

4. Click the **Compliance** section.
5. Locate the compliance offerings search or filter. Search for or locate **HIPAA**.
6. Read the HIPAA compliance overview page. Record the following:

   - Does Azure have a formal HIPAA certification? (Yes / No): _________________
   - What document must be executed before processing PHI in Azure?: _________________

7. Return to the Compliance section and locate **FedRAMP**. Record:

   - What is the highest FedRAMP authorization level Azure holds?: _________________
   - Which Azure cloud environment has FedRAMP High authorization?: _________________

8. Take a screenshot of the Trust Center Compliance page for your lab report.

### Task 1.2 — Explore the Service Trust Portal

1. Navigate to `https://servicetrust.microsoft.com/`
2. Sign in with your university Microsoft account or a personal Microsoft account.
3. On the home page, locate the **Audit Reports** section.
4. Browse to the **SOC Reports** category.
5. Identify whether SOC 2 Type II reports are available for download. Record what you find:

   - SOC 2 Type II report available?: _________________
   - Most recent report period listed (approximate): _________________

6. Navigate to the **Compliance Guides** section and locate any guide related to HIPAA or healthcare compliance.
7. Record the title of one compliance guide you find: _________________
8. Take a screenshot of the Service Trust Portal for your lab report.

### Reflection Question 1

> What is the difference between using the Trust Center and the Service Trust Portal in a compliance review process? In what situation would each be used?

---

## Part 2 — Azure Policy (25 minutes)

### Task 2.1 — Explore Built-In Policy Definitions

1. Sign in to the Azure portal at `https://portal.azure.com/`
2. In the search bar, type **Policy** and select the Policy service.
3. In the left navigation, click **Definitions**.
4. In the search box, type **tag** to find tag-related policies.
5. Locate the policy named **Require a tag on resources** (or similar). Click it to open the definition.
6. Review the policy JSON. Record the following:

   - What is the policy effect?: _________________
   - What parameter does this policy require you to configure?: _________________

7. Navigate back to Definitions and search for **allowed locations**.
8. Open the **Allowed locations** policy definition. Record:

   - What does this policy do when a resource is deployed outside the allowed locations?: _________________
   - What type of parameter does it use (single value or array)?: _________________

9. Take a screenshot of one policy definition detail page.

### Task 2.2 — Create a Resource Group for Testing

1. In the Azure portal, navigate to **Resource Groups**.
2. Click **+ Create**.
3. Configure:

   - **Subscription:** Your subscription
   - **Resource group name:** lab15-policy-rg
   - **Region:** East US

4. Click **Review + create**, then **Create**.
5. Confirm the resource group appears in your resource group list.

### Task 2.3 — Assign a Policy to the Resource Group

1. Navigate back to **Policy** in the Azure portal.
2. In the left navigation, click **Assignments**.
3. Click **+ Assign policy**.
4. Configure the assignment:

   - **Scope:** Click the scope selector. Select your subscription, then select **lab15-policy-rg** as the resource group.
   - **Policy definition:** Click the field and search for **Require a tag on resources**. Select it.
   - **Assignment name:** Lab15-RequireTagPolicy
   - **Parameters — Tag name:** Department

5. Leave all other settings at defaults.
6. Click **Review + create**, then **Create**.
7. Confirm the assignment appears in the Assignments list.
8. Take a screenshot of the completed policy assignment.

### Task 2.4 — Test the Policy

1. Navigate to **Resource Groups** and open **lab15-policy-rg**.
2. Click **+ Create** to create a resource. Choose **Storage account**.
3. Configure the minimum required fields:

   - **Storage account name:** lab15policy[your initials][4 random digits] (must be globally unique, all lowercase)
   - **Region:** East US
   - **Redundancy:** LRS

4. Do NOT add any tags.
5. Click **Review + create**, then **Create**.
6. Observe the result. Record what happens:

   - Was the storage account created successfully?: _________________
   - If it was blocked, what error message appeared?: _________________

7. Now try creating the storage account again, but this time add a tag:

   - **Tag Name:** Department
   - **Tag Value:** CloudLab

8. Click **Review + create**, then **Create**. Record the result:

   - Was the storage account created with the tag applied?: _________________

9. Take a screenshot of either the policy denial error or the successful tagged deployment.

### Task 2.5 — Review the Compliance Dashboard

1. Navigate to **Policy** and click **Compliance** in the left navigation.
2. Find the **Lab15-RequireTagPolicy** assignment in the list.
3. Click on it to see the compliance details.
4. Record:

   - Total resources in scope: _________________
   - Compliant resources: _________________
   - Non-compliant resources: _________________
   - Overall compliance percentage: _________________

5. Take a screenshot of the compliance detail page.

### Reflection Question 2

> The policy you assigned uses the "Deny" effect. What are the trade-offs between using Deny versus Audit for a new policy you are rolling out in a production environment for the first time? What approach would you recommend and why?

---

## Part 3 — Microsoft Purview Overview (10 minutes)

*Note: Microsoft Purview requires Microsoft 365 licensing for full access. In this part you will explore Purview's public documentation and the portal interface with read-only observation.*

### Task 3.1 — Explore Purview in the Azure Portal

1. In the Azure portal search bar, type **Microsoft Purview** and select it.
2. On the Purview overview page, observe the available capabilities listed.
3. Record three capabilities shown on the overview page:

   - Capability 1: _________________
   - Capability 2: _________________
   - Capability 3: _________________

### Task 3.2 — Purview Documentation Research

1. Navigate to `https://learn.microsoft.com/en-us/purview/purview`
2. Read the overview of Microsoft Purview.
3. Answer the following based on your reading:

   - What are the two main solution areas within Microsoft Purview?: _________________
   - What is the Data Map in Purview used for?: _________________
   - What does data lineage tracking show?: _________________
   - Name two types of sensitive data that Purview's built-in classifiers can detect: _________________

4. Take a screenshot of the Purview Learn documentation page.

### Reflection Question 3

> A healthcare organization stores patient records in Azure Data Lake Storage, processes them with Azure Data Factory pipelines, and loads results into Azure Synapse Analytics for reporting. How would Microsoft Purview help this organization with HIPAA compliance? Be specific about which Purview capabilities apply.

---

## Part 4 — Data Residency and GDPR Scenario Analysis (10 minutes)

Read the following scenario and answer the questions below.

### Scenario

TechRetail Inc. is a US-based e-commerce company that launched a website serving customers in Germany, France, and the Netherlands. Customer data — including names, email addresses, shipping addresses, and purchase history — is stored in Azure SQL Database. The company's Azure subscription is currently configured with all resources deployed to the East US region. The company's legal team has raised concerns about GDPR compliance.

### Questions

Answer each question in 3–5 sentences.

1. **Data Residency Issue:** What specific GDPR concern is raised by storing EU personal data in the East US region? What Azure configuration change should TechRetail make?

   Response: _________________

2. **GDPR Rights:** A customer in France submits a request to have all their personal data deleted from TechRetail's systems. What is this type of request called under GDPR, and what Azure tools or practices support fulfilling it?

   Response: _________________

3. **Contractual Requirements:** The legal team asks whether Microsoft has made any formal GDPR commitments to Azure customers. What document governs this and where can TechRetail find it?

   Response: _________________

4. **Policy Enforcement:** TechRetail's cloud architect wants to prevent any future resource deployments from being made outside the EU regions. Which Azure governance tool should they use and how would they configure it?

   Response: _________________

---

## Part 5 — Clean Up Resources (5 minutes)

To avoid incurring charges on your free trial account, delete the resources created in this lab.

1. Navigate to **Resource Groups** in the Azure portal.
2. Select **lab15-policy-rg**.
3. Click **Delete resource group**.
4. Type the resource group name to confirm deletion.
5. Click **Delete**.
6. Navigate to **Policy > Assignments** and confirm the policy assignment is removed automatically when the resource group is deleted.

---

## Lab Deliverables

Submit the following to the course LMS:

1. **Screenshots** (minimum 5): Trust Center Compliance page, Service Trust Portal, policy definition detail, policy assignment with compliance dashboard, Purview documentation page
2. **Recorded values** from Tasks 1.1, 1.2, 2.1, 2.4, and 2.5 filled in completely
3. **Reflection responses** for all three reflection questions (3–5 sentences each)
4. **GDPR scenario analysis** for all four questions in Part 4

---

## Grading Rubric

| Component | Points |
|---|---|
| Trust Center and Service Trust Portal exploration with screenshots | 15 |
| Policy assignment created and tested with screenshots | 30 |
| Compliance dashboard values recorded accurately | 15 |
| Purview capabilities documented | 10 |
| Reflection questions answered with depth and accuracy | 20 |
| GDPR scenario analysis answers | 10 |
| **Total** | **100** |

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 15 Lab*
