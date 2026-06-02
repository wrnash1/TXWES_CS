# Lab Activity: Module 07 — Service Management Practices: Change Enablement

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Total Points:** 100
**Certification Alignment:** ITIL 4 Foundation

---

## Overview

This lab requires you to apply Change Enablement concepts to realistic IT service management scenarios. No software tools or terminal commands are required. All work is analytical and written.

Submit all exercises as a single document to the Canvas assignment portal by the posted deadline.

---

## Scenario: Ironclad Financial Services

Ironclad Financial Services is a regional bank with 1,400 employees, 22 branch locations, and a central IT department of 35 staff. Ironclad's core systems include a banking platform, an online customer portal, a loan origination system, and a network of 900 branch workstations running Windows.

IT leadership has recently adopted ITIL 4 practices. The change management process that existed under ITIL v3 is being replaced by the Change Enablement practice. The IT director has identified several upcoming changes and situations that the team must work through as it stands up the new practice.

---

## Exercise 1: Change Classification (25 points)

Read each of the ten proposed changes below. For each change:

* Classify it as standard, normal, or emergency.
* State the authorization model — who authorizes it and what process applies.
* Write one sentence explaining the key factor that determined your classification.

Do not use bullet lists for your responses. Write each answer as a brief paragraph.

Change 1: A new hire joins the bank on Monday. The IT team needs to create a user account in Active Directory, assign standard role-based access permissions, and provision a workstation using the pre-configured image.

Change 2: A critical vulnerability in the online banking portal's authentication library is being actively exploited. Security has confirmed active attacks in the wild. A vendor-provided patch is available and must be applied to stop the ongoing breach.

Change 3: The bank is migrating its core banking platform from an on-premises data center to a private cloud hosted by a third-party provider. The migration will affect all 22 branch locations, the customer portal, and the loan origination system. Estimated downtime is six hours during a weekend maintenance window.

Change 4: A teller at Branch 7 reports that their browser is outdated and blocking access to an internal HR portal. The IT team needs to update the browser to the current approved version, which is on the pre-approved software list.

Change 5: The loan origination system vendor has released a major version upgrade that includes new regulatory compliance features required by the state banking commission. The upgrade requires a database schema change and has never been tested in this environment.

Change 6: A firewall rule at the main data center is blocking a new API integration with a partner institution. The network team needs to add a single inbound rule permitting traffic from the partner's IP range on a specified port. The change has not been performed before and the full impact on existing firewall policies is unknown.

Change 7: The IT team needs to reset a forgotten password for a branch manager who is locked out of their workstation and cannot start their workday. This is handled through the standard IT service desk process.

Change 8: A network switch at the main data center fails overnight, taking three branch locations offline. The network team needs to re-route traffic through a redundant switch that was not part of the original design, requiring an immediate configuration change to restore service.

Change 9: The server team needs to increase the allocated RAM on a development server from 8 GB to 16 GB. The server hosts only development and testing workloads and has no production dependencies.

Change 10: An audit finding requires the bank to implement multi-factor authentication for all administrative accounts within 30 days. The security team needs to deploy MFA across all privileged accounts in Active Directory, covering approximately 80 accounts across IT, compliance, and executive leadership.

### Rubric — Exercise 1

| Score | Criteria |
|---|---|
| 23–25 | All ten changes correctly classified with accurate authorization model and clear explanation |
| 18–22 | Eight or nine correctly classified; authorization model mostly accurate; explanations present |
| 13–17 | Six or seven correctly classified; some authorization models incorrect or missing |
| 0–12 | Fewer than six correctly classified; criteria not applied |

---

## Exercise 2: Change Record — Normal Change (35 points)

Using the change record template below, document Change 10 from Exercise 1 as a full normal change record. Complete every field. Write substantive content in each field — do not leave fields blank or write placeholder text.

### Change Record Template

**Change ID:** CHG-2024-047

**Change title:** (Write a concise descriptive title for this change.)

**Change type:** (Standard / Normal / Emergency — state which applies and why.)

**Requested by:** (Name the role that would initiate this change in the Ironclad scenario.)

**Date submitted:** (Use a realistic date in the context of a 30-day compliance deadline.)

**Target implementation date:** (Choose a date that allows time for assessment, CAB review, and scheduling.)

**Change description:** (Write 3–5 sentences describing what the change will do, what systems it affects, and why it is being made.)

**Business justification:** (Write 2–3 sentences explaining the business driver for this change — connect it to the audit finding and regulatory compliance requirement.)

**Scope:** (List the systems, services, and user populations affected by this change.)

**Risk assessment:** (Identify at least three specific risks associated with this change. For each risk, note its likelihood and potential impact.)

**Rollback plan:** (Describe what will be done if the change fails or causes unacceptable disruption. Be specific about the rollback steps and who is responsible.)

**Implementation steps:** (List the key steps required to implement this change in logical order.)

**CAB review required:** (State yes or no, and explain your reasoning based on the risk level and impact of this change.)

**Change authority:** (Identify the role that holds authorization power for this change.)

**Post-implementation review:** (Describe what will be checked after implementation to confirm success, and within what timeframe.)

### Rubric — Exercise 2

| Score | Criteria |
|---|---|
| 32–35 | All fields completed with substantive, realistic content; risk assessment identifies three or more specific risks; rollback plan is actionable; CAB reasoning is correct |
| 25–31 | All fields completed; one or two fields thin; risk assessment identifies two risks; rollback plan present |
| 18–24 | Most fields completed; risk assessment or rollback plan is superficial; CAB reasoning unclear |
| 0–17 | Multiple fields blank or with placeholder content; change record structure not demonstrated |

---

## Exercise 3: CAB Analysis (20 points)

Return to the ten changes from Exercise 1. For each of the following five changes (3, 5, 6, 8, and 10), answer the following questions in a brief paragraph for each change:

1. Would this change require CAB advisory review? Why or why not?
2. If CAB review applies, who should sit on the CAB for this specific change? Name at least three roles by title.
3. What specific information should the CAB review before making its recommendation?

Write your analysis in paragraph form. Do not use bullet lists.

### Rubric — Exercise 3

| Score | Criteria |
|---|---|
| 18–20 | All five changes analyzed; CAB decision correctly reasoned for each; membership and review criteria are specific and realistic |
| 14–17 | Four of five changes analyzed; CAB reasoning mostly correct; membership or review criteria thin on one or two |
| 10–13 | Three or four analyzed; CAB/no-CAB decisions mostly correct but reasoning is general |
| 0–9 | Fewer than three adequately analyzed; CAB role not clearly understood |

---

## Exercise 4: Guiding Principles Applied to Change Enablement (20 points)

Read each of the five situations below. For each one, identify the ITIL 4 Guiding Principle most directly applicable to the Change Enablement context, and write two sentences explaining how applying that principle would change the organization's behavior.

Situation 1: Ironclad's IT director wants to require full CAB review for every single change — including password resets, browser updates, and new user account creation — to ensure maximum governance oversight.

Situation 2: The development team wants to deploy the new MFA system all at once across all 80 accounts in a single Saturday evening window, rather than rolling it out in phases.

Situation 3: The network team has been making configuration changes to branch firewalls without informing the service desk or the branch managers. The service desk is receiving calls about unexpected behavior that they cannot explain because they were not aware changes were being made.

Situation 4: Before designing a new change assessment process, the IT director reviews the current process to understand what is already working well and what specific steps are causing delays.

Situation 5: The change record process currently requires 14 separate approval signatures on a paper form. Most signatures are from people who do not read the form — they simply sign because they were asked to. The IT director wants to redesign the process.

### Rubric — Exercise 4

| Score | Criteria |
|---|---|
| 18–20 | All five situations correctly mapped to a principle; both sentences for each situation are specific and accurate |
| 14–17 | Four correctly mapped; explanations present but one or two are vague |
| 10–13 | Three correctly mapped; some explanations missing the principle application |
| 0–9 | Fewer than three correctly mapped; Guiding Principles not clearly applied |

---

## Submission Instructions

Compile all four exercises into a single document with clear headings. Label each change number or situation number before your response. Submit to the Module 07 Lab assignment in Canvas by the posted deadline.
