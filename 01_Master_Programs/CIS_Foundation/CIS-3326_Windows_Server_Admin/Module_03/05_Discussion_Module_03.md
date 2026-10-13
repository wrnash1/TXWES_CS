# Discussion Forum: Module 03 - Installing and Configuring AD DS

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects AD DS installation and configuration decisions to real-world deployment and troubleshooting scenarios. Choose one scenario below, answer all three sub-questions in your initial post, and engage substantively with at least two classmates.

---

### Scenario A — Two-DC Deployment Planning

Your company currently has a single Domain Controller for its `txwes.local` domain. The IT director asks you to plan the deployment of a second DC to eliminate the single point of failure. The director also asks whether the second DC should be placed in the same server room or at a different physical location.

1. Explain the specific risks of operating a domain with only one DC. What happens to user authentication, GPO processing, and FSMO-dependent operations if that single DC goes offline?
2. Describe the PowerShell command sequence you would use to install the AD DS role and promote the second server as an additional DC in the existing domain. Identify the key parameters and explain why each is needed.
3. After promotion, what two command-line tools would you use to verify that replication is working correctly? What specific output would you look for to confirm a healthy state?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — Functional Level Upgrade Risk Assessment

A company's domain has been running at Windows Server 2008 R2 functional level for years. The IT team wants to enable Privileged Access Management (PAM) features, which require Windows Server 2016 forest functional level. The domain currently has three DCs: two running Windows Server 2016 and one running Windows Server 2012 R2 that hosts a legacy application.

1. What specific obstacle prevents the functional level from being raised immediately, and why does the oldest DC's OS version matter?
2. The team proposes decommissioning the 2012 R2 DC and migrating the legacy application to a newer server. Before raising the functional level, what verification steps should be performed to ensure all domain functions remain intact after the old DC is removed?
3. Once all DCs are at Windows Server 2016, describe the two commands needed to raise both functional levels. In what order must they be executed, and why is reversibility an important concern during this operation?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — Branch Office RODC Deployment

A retail company has 30 branch stores, each with a small server running local point-of-sale systems. Store managers report that when the WAN link to headquarters goes down, employees cannot log in to domain-joined POS workstations. The security team is concerned about deploying full writable DCs to stores because server rooms are not physically secured.

1. What type of Domain Controller resolves both the WAN dependency and the physical security concerns simultaneously? Explain how this DC type addresses each concern.
2. The security team wants to ensure that no IT administrator or Domain Admin passwords are ever cached at branch stores, but local store-worker accounts should cache normally. How does the Password Replication Policy accomplish this, and which built-in group should be used to deny high-privilege accounts?
3. If a branch store server is stolen, walk through the specific AD DS cleanup steps an administrator should take immediately to contain the security exposure.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates; minimum 60 words each
- In peer replies: evaluate their PowerShell command syntax or deployment sequence accuracy, and add one practical consideration they did not mention

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

The difference between a well-planned DC deployment and a reactive one shows up most clearly during failure scenarios. I have seen organizations with a single DC lose all domain authentication for two days while waiting for hardware replacement. I have also seen organizations deploy RODCs to every branch office and sleep soundly because they know a stolen server cannot compromise headquarters. The scenarios in this discussion are drawn from real situations. Think carefully about not just the technical steps but the business impact of each decision. Looking forward to your posts this week.
