# Discussion Forum: Module 13 — Network Security Fundamentals

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Overview

This discussion forum asks you to apply Module 13 security concepts to realistic enterprise scenarios. Choose one of the three scenarios below, write an original post of 175–225 words, and respond substantively to at least one classmate's post on a different scenario.

---

## Scenario 1: Choosing Between RADIUS and TACACS+

A mid-sized company is deploying a new network with 40 Cisco switches, 12 routers, and a wireless infrastructure serving 500 employees. The security team is debating whether to use RADIUS or TACACS+ for AAA. The network engineer argues that RADIUS is sufficient because it is an open standard supported by all vendors. The security architect counters that TACACS+ is needed because the team must audit every privileged command executed on any network device.

In your post, take a position and defend it. Address the following in your response:

* Which protocol would you recommend and why?
* How does the encryption difference between the two protocols influence your recommendation?
* Is there a scenario where deploying both protocols simultaneously makes sense?
* What business or compliance requirements might drive the choice?

Consider real-world factors such as vendor lock-in, licensing costs for Cisco ISE, and the operational overhead of managing two AAA systems.

---

## Scenario 2: Port Security Incident Response

A junior network engineer receives an alert that port Gi0/12 on a distribution switch has entered err-disabled state. Investigation reveals that a contractor plugged a personal laptop into a conference room wall jack connected to that port. The port was configured with `switchport port-security violation shutdown` and a maximum of one MAC address.

In your post, address the following:

* What immediate steps should the engineer take to restore connectivity for legitimate users?
* Should the violation mode be changed to restrict or protect going forward? Justify your recommendation.
* What longer-term access control strategy would reduce the likelihood of this incident recurring?
* How does sticky MAC learning factor into your recommended remediation?

Think about the balance between security enforcement and operational disruption. Consider whether 802.1X might be a better long-term solution than port security alone for conference room ports.

---

## Scenario 3: Defending Against ARP Poisoning in a Healthcare Network

A hospital network administrator discovers that a workstation on the nursing station VLAN is performing an ARP poisoning attack, redirecting traffic between nurses' PCs and the electronic health records server. The switch infrastructure supports DHCP snooping and DAI, but neither feature is currently enabled.

In your post, address the following:

* Describe the steps to enable DHCP snooping and DAI on the affected VLAN, identifying which ports should be trusted.
* The EHR server has a static IP address. What additional configuration is required to ensure DAI does not block the server's legitimate ARP traffic?
* What is the impact on patient care if ARP poisoning goes undetected, and how does DAI mitigate this risk?
* Beyond DAI and DHCP snooping, what other security controls would you recommend for a healthcare VLAN?

Consider HIPAA compliance implications and the criticality of network availability in a clinical environment.

---

## Peer Response Guidelines

When responding to a classmate's post:

* Engage with their specific recommendation — do not simply restate the scenario.
* Add a technical detail, counterargument, or real-world example they did not mention.
* Keep your response between 75 and 125 words.
* Be professional and constructive.

---

## Grading Rubric

| Criterion | Points | Description |
|---|---|---|
| Technical accuracy | 4 | Security concepts applied correctly; commands or protocols cited accurately |
| Depth of analysis | 3 | Addresses all prompt questions; reasoning is clear and specific |
| Original post length | 1 | 175–225 words (verified by word count) |
| Peer response | 2 | Substantive reply to a classmate on a different scenario; adds new insight |
| **Total** | **10** | |

---

## Submission Deadline

Initial post due by 11:59 PM on the Wednesday of Module 13 week. Peer response due by 11:59 PM on Sunday of the same week.
