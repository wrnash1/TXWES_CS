# Discussion Forum: Module 11 — Wireless Network Assessment

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Discussion Prompt

Wireless networks present a unique challenge because the attack surface extends beyond physical boundaries. Unlike a wired port behind a locked door, a wireless access point radiates in all directions — potentially reaching parking lots, adjacent buildings, or public spaces. This creates both a broader attack surface and more complex scoping decisions for penetration testers.

At the same time, wireless security protocols have improved significantly over time. The transition from WEP to WPA to WPA2 to WPA3 reflects decades of cryptographic lessons learned. Yet many organizations still operate networks using older protocols, particularly in industrial, healthcare, and retail environments where upgrading infrastructure is difficult or expensive.

### Initial Post (Due Wednesday at 11:59 PM)

In 200–250 words, address the following scenario:

You are a penetration tester engaged by a mid-size manufacturing company. During your wireless reconnaissance, you discover three separate wireless networks:

- Network 1: "CorpWiFi" — WPA2-Personal, SSID broadcast enabled, moderate signal
- Network 2: "ManufacturingFloor" — WEP encryption, strong signal originating from the production area
- Network 3: "GuestPortal" — Open network (no encryption), strong signal, appears to be a guest portal

For each network, address the following:

1. What attack technique from this module would you apply to assess the security of that network? Be specific — name the tool and describe the attack.

2. What is the business risk if that network is compromised? Consider what systems or data might be reachable from each segment.

3. What remediation would you recommend for each network?

Conclude your post with one sentence explaining why you would prioritize the ManufacturingFloor network in your report, even if its password is strong.

### Peer Responses (Due Sunday at 11:59 PM)

Write a substantive reply (at least 75 words) to at least two classmates. In each reply, address one of the following:

- Your classmate recommended a specific attack tool. Describe a defensive control that would prevent or detect that specific attack.
- Your classmate discussed the business risk of a specific network. Add context — what specific types of data or systems are commonly found in manufacturing environments that would make wireless access particularly dangerous?
- Challenge or expand on your classmate's remediation recommendation. Is migration to WPA3 always feasible in industrial environments? What alternative controls exist when hardware replacement is not immediately possible?

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5–6 pts: Addresses all three networks with specific attack techniques (correct tool names), realistic business risk analysis, and technically sound remediation recommendations. Includes the concluding prioritization sentence. Meets word count. Uses module terminology accurately.
- 3–4 pts: Addresses some networks or provides vague attack descriptions (e.g., "crack the password" without naming the tool or technique). Business risk or remediation analysis is superficial.
- 0–2 pts: Post is incomplete, addresses fewer than two networks, or demonstrates minimal engagement with module content.

### Peer Responses (4 Points)

- 4 pts: Responds to two peers with substantive technical contributions. Engages with the specific networks, tools, or risks the peer described.
- 2 pts: Responds to only one peer, or both responses are generic without technical engagement.
- 0 pts: No peer responses submitted by the deadline.

---

## Background Reading

If you would like additional context on wireless security in industrial environments, the following free resources are useful:

- CISA ICS Security: cisa.gov/ics (covers wireless security in industrial control system environments)
- Wi-Fi Alliance WPA3 specification overview: wi-fi.org/discover-wi-fi/security
- NIST SP 800-153 Guidelines for Securing Wireless Local Area Networks: csrc.nist.gov

---

*End of Module 11 Discussion Forum*
