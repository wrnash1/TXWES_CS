# Discussion Forum: Module 14 — Wireless Networking

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Overview

This discussion forum asks you to apply Module 14 wireless networking concepts to realistic enterprise deployment scenarios. Choose one of the three scenarios below, write an original post of 175–225 words, and respond substantively to at least one classmate's post on a different scenario.

---

## Scenario 1: WPA2 vs. WPA3 Upgrade Decision

A university IT department is evaluating whether to upgrade its wireless infrastructure from WPA2-Personal to WPA3 across all campus buildings. The CISO is concerned about the security vulnerabilities in WPA2-PSK, particularly after hearing about offline dictionary attacks against captured handshakes. However, the operations team notes that several older devices (laboratory equipment, printers, and legacy laptops) do not support WPA3. The budget allows for a phased approach over two years.

In your post, address the following:

* What specific WPA2 vulnerability most concerns you, and how does WPA3-SAE address it?
* How would you design a transition strategy that maintains security while supporting legacy devices?
* Should the university use WPA3-Personal or WPA3-Enterprise, and why?
* What role does OWE play for the campus guest network during the transition period?

Consider the practical balance between security improvements and operational compatibility in a mixed-device environment like a university campus.

---

## Scenario 2: Autonomous vs. Controller-Based Decision for a Retail Chain

A regional retail chain has 45 store locations, each with 3–5 wireless access points serving both point-of-sale terminals and customer guest Wi-Fi. The IT director is deciding between deploying autonomous APs managed via a cloud-based dashboard or investing in a Cisco WLC architecture. The chain's PCI-DSS compliance auditor has flagged inconsistent security configurations across stores as a risk.

In your post, address the following:

* What are the specific advantages of a controller-based WLC architecture for this retail scenario?
* How does centralized management address the PCI-DSS configuration consistency concern?
* What AP mode would you assign to one AP per store that is dedicated to detecting rogue access points?
* What are the risks of FlexConnect mode in a retail environment where the WAN link is unreliable?

Consider how the CAPWAP architecture changes the IT team's operational workflow compared to managing 45 sites individually.

---

## Scenario 3: Channel Planning in a High-Density Venue

A convention center hosting technology conferences wants to deploy wireless to serve up to 2,000 concurrent users in a single large exhibit hall. The RF engineer must choose between a 2.4 GHz-only, 5 GHz-only, or dual-band deployment. Preliminary site surveys show significant co-channel interference in the 2.4 GHz band from neighboring access points and Bluetooth devices.

In your post, address the following:

* Which band or combination of bands would you recommend and why?
* How many non-overlapping channels are available in each band, and how does this affect your AP placement plan?
* What channel width (20 MHz, 40 MHz, or 80 MHz) would you use for 5 GHz in this high-density environment, and why?
* How does Cisco RRM (Radio Resource Management) help manage a deployment of this scale?

Consider the tradeoffs between raw throughput per AP and the total capacity available across the full deployment.

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
| Technical accuracy | 4 | Wireless concepts applied correctly; standards and protocols cited accurately |
| Depth of analysis | 3 | All prompt questions addressed; reasoning is clear and specific |
| Original post length | 1 | 175–225 words (verified by word count) |
| Peer response | 2 | Substantive reply to a classmate on a different scenario; adds new insight |
| **Total** | **10** | |

---

## Submission Deadline

Initial post due by 11:59 PM on the Wednesday of Module 14 week. Peer response due by 11:59 PM on Sunday of the same week.
