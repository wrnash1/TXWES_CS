# Discussion Forum — Module 02: Social Engineering and Phishing

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This discussion connects Module 02 content to real organizational security challenges around social engineering. You will analyze a scenario, apply module concepts, and engage critically with classmates. Strong posts demonstrate accurate terminology, specific reasoning, and genuine engagement with peer arguments.

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM

---

## Scenario A — The Helpful Help Desk

Cascade Manufacturing has 600 employees across three facilities. The IT help desk handles roughly 80 tickets per day. A new help desk policy requires staff to verify caller identity through a three-step process before resetting any account credentials: confirm employee ID, confirm manager's name, and send a verification code to the employee's registered mobile number.

Two weeks after the policy was implemented, a senior manager submitted a complaint to the CIO stating that the new verification process is "slowing down productivity" and that the help desk should "just trust employees who call in." He argues that none of their employees would ever try to social engineer the help desk.

In 175–225 words, address all three of the following:

1. Explain specifically why the manager's argument is flawed from a security perspective. Use at least one specific social engineering technique from Module 02 to support your argument with a realistic example.
2. Explain what the verification policy is designed to prevent and which social engineering psychological principle it counteracts.
3. Recommend one additional control — beyond the verification policy — that the help desk should implement, and classify it using the correct category and function labels.

---

## Scenario B — The USB Drop Campaign

A red team assessment firm is hired by Westbrook Health System to test employee susceptibility to physical social engineering. The firm plants 20 USB drives in hospital parking lots, break rooms, and the main lobby over two days. Each drive is labeled "Employee Benefits Open Enrollment — 2024." Within 48 hours, 11 of the 20 drives were plugged into hospital workstations. Six of those workstations would have been compromised if the drives contained real malware.

The hospital's CISO is shocked. She had assumed that because the hospital runs annual security awareness training, employees would know not to plug in unknown media.

In 175–225 words, address all three of the following:

1. Identify the specific social engineering technique used and explain which psychological principle made it effective in this environment.
2. Explain why annual training alone was insufficient to prevent this outcome, and what a more effective training approach would look like.
3. Recommend two specific technical controls that would reduce the risk of this attack succeeding even if an employee does plug in an unknown USB drive. For each control, state the category and function.

---

## Scenario C — The Vendor Email

Northpoint Legal Partners receives an email appearing to be from one of their longtime document storage vendors. The email explains that the vendor is updating their billing system and all clients need to update their payment information through a link in the email. The link leads to a convincing replica of the vendor's real client portal. Three employees at Northpoint entered their portal credentials before the firm's IT administrator noticed the email domain was "vendorname-billing-update.com" rather than the vendor's real domain.

The IT administrator contacts the real vendor and confirms the email is fraudulent. The vendor states they did not send any such communication. The real vendor's domain does have SPF and DKIM configured but does not have DMARC deployed.

In 175–225 words, address all three of the following:

1. Identify the phishing variant and explain what OSINT the attacker likely used to craft a convincing lure targeting this specific firm.
2. Explain how a properly configured DMARC policy on the vendor's domain would — or would not — have prevented this specific attack. Be precise about what DMARC can and cannot protect against.
3. Identify two red flags in this scenario that trained employees should have recognized before entering their credentials. For each red flag, name the awareness topic that would have prepared employees to notice it.

---

## Peer Response Guidelines

After posting your initial response, reply substantively to at least two classmates. Each reply must:

- Add a specific technical point, counter-argument, or real-world extension.
- Reference at least one concept from the Module 02 Reading Guide by name.
- Respectfully challenge any classification or recommendation you believe is incorrect, with your reasoning.

Replies consisting only of agreement or encouragement without technical substance receive zero peer response points.

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 6 | Addresses all three questions for the chosen scenario with technical accuracy. Uses correct Security+ terminology throughout. Meets the 175–225 word requirement. |
| 4–5 | Addresses most questions with mostly correct terminology. Minor errors or missing detail on one question. |
| 2–3 | Addresses some questions but contains significant technical errors or omissions. |
| 0–1 | Incomplete, off-topic, or missing. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 | Two substantive replies with specific technical additions, references to Reading Guide content, or reasoned challenges. |
| 2–3 | Two replies posted but one or both lack substantive technical content. |
| 1 | Only one peer reply submitted. |
| 0 | No peer responses or all responses are generic. |

---

## Professor Nash's Note

Scenario B is the one I see students debate most. The instinct is to blame employees for clicking. I want you to think harder than that — blame the system design. A well-designed security program does not rely on every single employee making the right decision every single time. That is not a realistic expectation. The question is: what does the system look like when a human makes a mistake and the attack still fails? That is the design challenge. Bring that thinking into the discussion.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 02 Discussion

Proprietary and Confidential. Not for disclosure outside of authorized course use.
