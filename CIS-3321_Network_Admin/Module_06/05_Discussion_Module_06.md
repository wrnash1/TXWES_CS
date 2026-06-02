# Discussion Forum: Module 06 – Wireless Networking: 802.11 Standards and Security

## CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects wireless networking concepts — 802.11 standards, security protocols, and wireless threats — to practical deployment and design decisions. You will choose one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, respond to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: Wireless Security Upgrade for a Healthcare Clinic

A regional healthcare clinic currently uses WPA2-Personal (PSK) for all wireless connectivity, including the network that clinical staff use to access electronic health records (EHR). The clinic has 45 employees across three departments. The IT manager is concerned because two employees recently left the organization, and changing the shared passphrase requires reconfiguring every wireless device in the building. A compliance officer has also flagged that the current setup provides no per-user audit trail, which is required under the organization's security policy.

Respond to all three questions:

1. Why is WPA2-Personal (PSK) inadequate for this environment from both a security and a compliance standpoint? Specifically address the issues of per-user credential revocation and audit trail requirements.
2. What wireless security architecture would you recommend to replace WPA2-PSK in this environment? Name the specific authentication standard, the server component required, and at least one EAP method appropriate for a healthcare setting.
3. The compliance officer asks whether upgrading to WPA3 instead of WPA2-Enterprise would satisfy the audit trail requirement. How would you respond? What does WPA3 add that WPA2-Enterprise does not, and what does it not address?

---

#### Scenario B: Channel Planning for a Multi-Floor Office Deployment

A mid-sized company is deploying a new wireless network across a four-floor office building. Each floor will have four access points operating in the 2.4 GHz band only (the budget does not allow for dual-band APs). The network contractor submitted a design proposal assigning channels 1, 2, 3, and 4 to the four APs on each floor, reasoning that these are the four lowest available channels and therefore the cleanest. The IT director has asked you to review the proposal before it is approved.

Respond to all three questions:

1. Identify the specific technical error in the contractor's channel assignment plan. Explain why assigning channels 1, 2, 3, and 4 to neighboring APs causes problems, using the terms "co-channel interference" and the 2.4 GHz channel spacing specifications.
2. Propose a corrected channel assignment plan for four APs on the same floor. Only three non-overlapping channels exist in the US 2.4 GHz band — explain how you would handle four APs with only three usable channels and what the tradeoff is.
3. The IT director asks whether upgrading to dual-band APs and using 5 GHz would eliminate the channel planning problem. How would you respond? Describe the key difference in the number of non-overlapping channels between 2.4 GHz and 5 GHz, and identify one trade-off of 5 GHz that the IT director should understand.

---

#### Scenario C: Wireless Threat Investigation

A university IT security team receives reports from students that they were prompted to enter their campus login credentials while connected to the campus Wi-Fi network, but the login page looked slightly different from the official portal. Separately, the team's wireless intrusion prevention system (WIPS) has been generating alerts about a high volume of deauthentication frames being sent from an unknown MAC address. The WIPS alert and the credential harvesting reports occurred on the same day, in the same building.

Respond to all three questions:

1. Identify the two wireless attacks that are likely occurring simultaneously. For each attack, explain the mechanism — how the attacker executes it, what the attacker is trying to accomplish, and which 802.11 frame type or vulnerability is being exploited.
2. Explain how the two attacks may be working together as a combined attack sequence. What does the first attack enable for the second? Walk through the sequence from the attacker's perspective.
3. For each of the two attacks, identify the specific technical control that would prevent or detect it. Name the 802.11 standard amendment or system that addresses each attack, and explain what it does at a technical level.

---

### Response Requirements

Initial Post (due Wednesday at 11:59 PM):

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct wireless terminology (WPA2/WPA3, 802.1X, RADIUS, channel numbers, EAP method names, 802.11w, WIPS)

Peer Responses (due Sunday at 11:59 PM):

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, correction, or alternative design perspective — do not simply agree

---

### Grading Rubric (10 Points Total)

Initial Post — 6 Points:

- 5–6 points: All three sub-questions answered with accurate technical detail, correct wireless security terminology, appropriate protocol names, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical detail or contains a specification error.
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

Peer Responses — 4 Points:

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding specific technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

Wireless security decisions are among the most consequential in network administration because wireless signals do not stop at the walls of the building. Every deployment decision — which authentication mode to use, which channels to assign, whether to enable Management Frame Protection — has real consequences for both security and performance. The scenarios this week reflect genuine mistakes I have seen in real deployments: clinics using shared passphrases for EHR access, contractors assigning adjacent channels to neighboring APs, and security teams encountering combined deauth-plus-evil-twin attacks without recognizing the connection between the two alerts. Your responses should demonstrate that you can connect the technical specifications from the lecture to the practical decisions a network administrator actually has to make.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
