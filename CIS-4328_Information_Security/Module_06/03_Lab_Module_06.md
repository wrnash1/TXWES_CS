# Lab Activity — Module 06: IAM Configuration and Analysis

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | Authorized Educational Use Only

---

## Lab Overview

**Lab Title:** Identity and Access Management Analysis and Design

**Estimated Completion Time:** 90 minutes

**Submission:** Upload your completed deliverables to Canvas before the module deadline.

**Learning Objectives:**

- Evaluate an organization's IAM configuration against least-privilege principles.

- Analyze SAML assertions and OAuth 2.0 flows to identify their components.

- Design an access control model for a realistic organizational scenario.

- Identify PAM deficiencies and recommend specific remediation.

- Trace an authentication flow using correct protocol terminology.

---

## Background

In this lab you will act as an IAM security analyst reviewing and designing access control systems. This is a document-based analysis lab — no systems are modified. The analysis skills practiced here directly map to Security+ performance-based questions and to real-world IAM audit engagements.

---

## Required Tools

All tools are free and browser-based:

- JWT Decoder: [https://jwt.io](https://jwt.io)

- SAML Decoder: [https://www.samltool.com/decode.php](https://www.samltool.com/decode.php)

- Any text editor

---

## Part 1 — Access Review: Least Privilege Audit (25 minutes)

### Part 1 Background

The following table shows current access assignments for five employees at a mid-size healthcare company. You are conducting a least-privilege access review.

| User | Current Role | Access Assigned | Notes |
|---|---|---|---|
| Alice Chen | HR Coordinator | HR records, Payroll system, Finance reports, IT admin portal | Previously worked in IT |
| Bob Martinez | Software Developer | Source code repository, Dev database, Production database, HR records | "Needs HR access for a project" |
| Carol Johnson | Finance Analyst | Finance reports, Payroll system, Executive compensation data, All-staff directory | Standard role |
| David Park | IT Help Desk | User account reset, Ticketing system, Domain admin rights, All file shares | "Makes his job easier" |
| Eve Williams | Marketing Manager | Marketing tools, CRM, Customer PII database, Competitor intelligence files | No documented justification on file |

### Part 1 Tasks

1. For each user, identify which access assignments violate the principle of least privilege. Explain why each flagged assignment is excessive for the stated role.

2. For Alice Chen specifically, identify the IAM failure mode that explains why she has IT admin access in addition to HR access. Name this failure mode using the correct IAM term.

3. David Park has domain admin rights on a help desk account. Identify the specific risk this creates. What PAM architecture would provide him the access he needs for specific tasks without persistent domain admin privileges?

4. Design a revised access assignment table with the minimum necessary access for each user. Include a justification column explaining what business function requires each access grant you retained.

5. What process control should be implemented to prevent access accumulation from recurring? Describe the process, its recommended frequency, and who should be responsible for approving retained access.

### Part 1 Deliverable

A written analysis for tasks 1–3, a revised access table for task 4, and a process description for task 5.

---

## Part 2 — JWT Analysis (20 minutes)

### Part 2 Background

A developer has provided you with an ID token from an OIDC authentication flow. JWT tokens are base64URL-encoded and consist of three sections: header, payload, and signature.

### Part 2 Tasks

Navigate to [https://jwt.io](https://jwt.io) and decode the following token by pasting it into the "Encoded" field:

```text
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjEyMzQ1NiJ9.eyJzdWIiOiJ1c2VyXzEyMzQ1IiwiaXNzIjoiaHR0cHM6Ly9pZHAuZXhhbXBsZS5jb20iLCJhdWQiOiJjbGllbnRfYXBwXzAwMSIsImV4cCI6MTcxNzAwMDAwMCwiaWF0IjoxNzE2OTk2NDAwLCJlbWFpbCI6ImFsaWNlQGV4YW1wbGUuY29tIiwibmFtZSI6IkFsaWNlIENoZW4iLCJyb2xlcyI6WyJ1c2VyIiwiZmluYW5jZV9yZWFkIl19.SIGNATURE_PLACEHOLDER
```

1. Identify the algorithm used to sign this token (from the header section).

2. From the payload, identify and record the values of: `sub`, `iss`, `aud`, `exp`, `email`, and `roles`.

3. The `exp` claim represents a Unix timestamp. Using any Unix timestamp converter, determine when this token expires. Based on the current date, is this token valid or expired?

4. What does the `aud` (audience) claim specify, and why is it important for security? What vulnerability could occur if a service did not validate the `aud` claim?

5. This token contains `roles` claims. Is including authorization roles in an ID token a good practice? What security consideration must be addressed when using JWT claims for access control decisions?

### Part 2 Deliverable

Written answers to all five tasks with specific references to the decoded token values.

---

## Part 3 — Authentication Protocol Selection (20 minutes)

### Part 3 Background

You are the IAM architect for a mid-size enterprise. Five integration requirements have been submitted for your review. For each requirement, you must select the appropriate authentication or authorization protocol and justify your selection.

### Part 3 Requirements

**Requirement A:** A third-party expense management SaaS application (Concur) needs to integrate with the company's on-premises Active Directory so that employees use their corporate credentials to log in. The vendor's documentation shows their product supports SAML 2.0 and OIDC.

**Requirement B:** A mobile expense reporting app (iOS and Android) needs to allow employees to log in with their corporate identity and submit expense reports. The app is a native mobile app with no server-side component for the login flow.

**Requirement C:** A microservice in the company's internal API platform needs to call another microservice to retrieve data. No user is involved — the calling service needs to authenticate itself and obtain an access token.

**Requirement D:** A partner company needs to grant your employees read access to their project management portal without creating accounts for your employees in their system. Your company uses Azure AD; the partner uses Google Workspace.

**Requirement E:** A legacy on-premises application from 2008 only supports LDAP bind authentication. Employees currently use a separate username and password for this system.

### Part 3 Tasks

1. For each requirement, select the most appropriate protocol from: SAML 2.0, OIDC, OAuth 2.0 Authorization Code + PKCE, OAuth 2.0 Client Credentials, or LDAP.

2. For each selection, write two to three sentences explaining why that protocol is best suited for the requirement.

3. For Requirement E specifically, what security risks does LDAP bind authentication introduce compared to a modern protocol? What configuration change would at minimum reduce the risk of credential exposure?

### Part 3 Deliverable

A five-row table with columns for Requirement, Selected Protocol, and Justification. Plus a written paragraph for task 3.

---

## Part 4 — PAM Gap Analysis (25 minutes)

### Part 4 Background

A security audit of a 500-person financial services company has produced the following findings related to privileged access:

**Finding A:** The domain administrator account (`DOMAIN\Administrator`) is used by three different IT staff members, who share the password via a team chat application.

**Finding B:** When an IT engineer needs to perform maintenance on a production server, they remote desktop from their regular workstation (which they also use for email and web browsing) to the server using their personal admin account.

**Finding C:** Service accounts for 23 different applications all use the same password, which has not been changed in four years. The password is stored in a shared spreadsheet accessible to all IT staff.

**Finding D:** There is no process for removing privileged access when an IT employee changes roles or departs. A former network administrator who left six months ago still has an active account with domain admin rights.

**Finding E:** Administrative actions are performed via RDP sessions that are not recorded. When an audit questioned what changes were made to a firewall two months ago, no one could determine who made the change.

### Part 4 Tasks

1. For each finding, identify the specific IAM or PAM principle that has been violated.

2. Assign a severity (Critical, High, Medium) to each finding. Justify your ranking.

3. For each finding, recommend a specific, actionable remediation. Name the specific PAM control or IAM process that would address it.

4. Finding A and Finding C both involve shared credentials. Explain why shared administrative credentials are particularly dangerous in a financial services environment. What regulatory frameworks require individual accountability for privileged access?

### Part 4 Deliverable

A five-row findings table with columns for Finding, Violated Principle, Severity, and Remediation. Plus a written paragraph for task 4.

---

## Lab Submission Checklist

Before submitting, verify:

- Part 1: Written analysis for tasks 1–3, revised access table for task 4, process description for task 5.

- Part 2: Written answers to all five JWT analysis tasks with decoded values referenced.

- Part 3: Five-row protocol selection table and written paragraph for task 3.

- Part 4: Five-row PAM findings table and written paragraph for task 4.

---

Module 06 Lab — End
