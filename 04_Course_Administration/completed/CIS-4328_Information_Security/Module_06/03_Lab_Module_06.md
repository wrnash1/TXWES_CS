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

## Part 9 — Challenge Exercise

### Challenge 1: SAML vs. OAuth 2.0 vs. OIDC Protocol Comparison and Attack Surface Analysis

Using the Module 06 reading guide and publicly available documentation, complete the following analysis without accessing or testing any live systems.

1. Create a side-by-side comparison table for SAML 2.0, OAuth 2.0, and OIDC covering: primary purpose (authentication vs. authorization vs. both), token format, typical use case, whether the protocol provides identity claims to the client application, and one known attack or misconfiguration risk specific to each protocol.
2. A SaaS vendor proposes using OAuth 2.0 implicit flow for their new single-page application. Research why the implicit flow is considered deprecated and what the recommended replacement is. Explain the specific security risk that the implicit flow introduces that the replacement addresses.
3. An enterprise deploys SAML 2.0 SSO federated to their IdP. A security researcher demonstrates that by modifying the SAML assertion XML and re-encoding it in Base64, they can change the username value in the assertion and authenticate as a different user. What class of vulnerability does this represent? What cryptographic control should be in place to prevent it, and why does that control prevent this specific manipulation?
4. Describe the OIDC Authorization Code Flow with PKCE in four steps, identifying at each step: what data is exchanged, between which parties, and what security property is provided by that exchange.

### Challenge 2: Access Control Model Selection and Privilege Audit

A healthcare organization manages the following three systems and must select the most appropriate access control model for each. Analyze each system and justify your recommendation.

**System A — Electronic Health Record (EHR) system:** 500 physicians, nurses, and administrators need access. Physicians need full read/write to their own patients. Nurses need read access to assigned patients. Administrators need access to billing records but not clinical notes. Access needs change frequently as patients are admitted and discharged.

**System B — Classified research database:** Contains federally funded research with three sensitivity tiers: Unclassified, Sensitive, and Restricted. Users are assigned clearance levels that do not change unless formally reviewed. No user may access data above their clearance level regardless of job function.

**System C — Cloud infrastructure management console:** Access decisions must factor in the user's department, their device compliance posture, time of day, geographic location, and whether the specific resource is tagged as production or development.

1. For each system, recommend one access control model (DAC, MAC, RBAC, or ABAC) and justify your choice with at least two specific reasons drawn from the system's requirements.
2. For System A, design a simple RBAC role matrix. Define four roles, list the permissions each role holds, and specify which role(s) should exist for the administrator accessing billing but not clinical notes.
3. The healthcare organization discovers that three employees who were transferred between departments over the past year still retain access from their previous roles. Name this IAM condition using the correct terminology, identify which IAM process failure allowed it to occur, and recommend two specific process or technical controls to prevent it going forward.
4. The organization wants to implement PAM for the 12 system administrators who manage the EHR infrastructure. Identify three PAM controls from Module 06, describe how each control is implemented for this specific use case, and explain which attack each control directly mitigates.

### Reflection Questions

1. After completing both challenges, explain why an organization that uses SAML 2.0 SSO for all applications has a fundamentally different risk profile for account compromise compared to an organization where each application has its own local accounts. Address both the risk reduction and the risk concentration aspects of centralized identity federation.
2. In Challenge 2, you analyzed the distinction between RBAC and ABAC. A security manager argues that ABAC is always superior to RBAC because it is more flexible and granular. Identify two specific scenarios where RBAC is the more appropriate choice despite ABAC's flexibility, and explain why adding unnecessary complexity to an access control model can itself create security risk.

---

Module 06 Lab — End
