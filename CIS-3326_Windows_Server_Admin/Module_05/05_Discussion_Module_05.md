# Discussion Forum: Module 05 - Group Policy Objects: Creation and Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies Group Policy concepts to real-world enterprise scenarios. Choose one scenario below, answer all three sub-questions, and engage substantively with at least two classmates.

---

### Scenario A — Conflicting GPO Inheritance Design

A retail company has a corporate AD domain with three levels of OU: the domain root, a Stores OU, and individual store OUs nested inside it. The corporate security team has linked a GPO at the domain level to enforce screensaver lock and USB storage restriction. One store manager has requested that the store's OU policy override the USB restriction so staff can use USB barcode scanners.

1. Using your knowledge of LSDOU processing, explain whether an OU-level GPO can override the domain-level GPO in normal circumstances. What specific flag would the security team need to set on the domain GPO to prevent any OU from overriding these settings?
2. If the store's USB restriction exception is approved by the security team and the domain GPO is set to Enforced, what alternative design approach could satisfy both the store's operational need (USB scanners work) and the security team's requirement (USB storage drives are blocked)?
3. The store manager also reports that the screensaver policy is not applying to the store manager's own workstation even though it applies to all other machines in the OU. Walk through the three most likely causes you would investigate using `gpresult /r`, in priority order.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — Kiosk and Shared Workstation Policy

A university library has 60 public access workstations in a Kiosks OU. Students log in with their personal domain accounts to access library resources. The IT team wants to ensure that every student who logs into these kiosks gets a locked-down desktop — no Task Manager, no Run dialog, no CMD prompt, a 10-minute screensaver timeout — regardless of what policies apply to the student's personal account OU.

1. Which Group Policy feature and specific mode setting makes user settings follow the computer's OU location rather than the user's personal OU? Explain the difference between the two mode options and which one is appropriate for this scenario.
2. If a faculty member who has a separate Faculty OU with elevated desktop permissions logs into a library kiosk, what should happen to their desktop environment under the correct Loopback configuration? How does this differ if Merge mode is used instead?
3. A student reports that the kiosk restrictions are not applying on one specific workstation even though all other kiosks are working correctly. Identify the most likely cause related to GPO components and describe which diagnostic command would confirm or rule out this cause.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — GPO Troubleshooting and Security Filtering

An administrator creates a GPO to deploy a desktop background image to all members of the Marketing department. The GPO is linked to the Marketing OU. After deploying, several Marketing users report the background has not changed. The administrator removes "Authenticated Users" from Security Filtering and adds the `G_Marketing` group. The background still does not apply to all Marketing users.

1. Explain the two most common reasons why a GPO would appear in the Denied GPOs section of `gpresult /r` as "Inaccessible," and describe how you would diagnose and fix each one.
2. Some Marketing users are contractors whose accounts live in a Contractors OU rather than the Marketing OU. Would the Marketing OU-linked GPO apply to them even if they are members of `G_Marketing`? Explain why or why not, and what change would make the GPO apply to them.
3. The administrator wants to verify the GPO is applying correctly on a specific contractor's workstation without logging into that machine. Which PowerShell command generates a remote RSoP report for a specific user and computer combination, and what file format should be requested for maximum detail?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates; minimum 60 words each
- In peer replies: evaluate the accuracy of their GPO filtering or Loopback explanation, and add one consideration they did not mention

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

Group Policy is the single most powerful configuration management tool in a Windows environment, and it is also the tool I see most often misconfigured. The two most common GPO mistakes I encounter in real environments are: one, relying on Security Filtering without accounting for computer Read permissions, and two, applying an Enforced policy without realizing it is going to override something that legitimately needs to be overridden at a lower level. Scenario B's Loopback Processing question is something I set up personally in a computer lab — it works exactly as described and is one of the cleanest GPO features Microsoft ever designed. Looking forward to your posts.
