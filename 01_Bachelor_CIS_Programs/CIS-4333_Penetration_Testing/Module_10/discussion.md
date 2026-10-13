# Discussion: Module 10 — Wireless and Network Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Choose ONE of the three scenarios below. Write a primary response of 175–225 words addressing the scenario's questions. Then post substantive peer responses to TWO classmates who chose different scenarios. Peer responses must be 75–100 words and include a specific technical point of agreement, disagreement, or extension.

Initial post due: Thursday 11:59 PM. Peer responses due: Sunday 11:59 PM.

---

## Scenario A: The Coffee Shop Incident

A junior penetration tester on your team was conducting a wireless assessment at a corporate client's headquarters. The scope of work authorized testing of all access points listed in an appendix. While sitting in the building's lobby, the tester's airodump-ng captured a handshake from an SSID not on the list. The tester saved the capture file and began cracking it offline, reasoning that "since we're already on site and it's in our capture range, it's fair game."

Address the following: Was the tester's reasoning correct? What specific laws or regulations were potentially violated? As the project lead, what steps would you take immediately? What policy would you implement to prevent this situation in future engagements?

---

## Scenario B: The Weak Enterprise Wi-Fi

A penetration test of a healthcare organization reveals that their WPA2-Enterprise deployment does not enforce certificate validation on client supplicants. You set up a rogue AP with hostapd-wpe and within 20 minutes capture PEAP-MSCHAPv2 challenge-response hashes from three employee laptops — including one that belongs to the IT Director. You crack one hash and confirm it is a valid Active Directory credential.

Address the following: How would you rate this finding (Critical/High/Medium/Low) and justify your CVSS scoring? What is the complete remediation path from immediate mitigation to long-term fix? How would you communicate this sensitive finding — specifically the IT Director's credential — to the client in a way that is professional, clear, and avoids creating unnecessary alarm?

---

## Scenario C: The Segmentation Test

A client believes their wireless guest network is completely isolated from the corporate LAN. Your engagement authorizes testing of both networks. After connecting to the guest Wi-Fi, you discover that ARP broadcasts are leaking between the guest VLAN and an internal printer subnet. You establish a pivot to the printer subnet and discover it is a flat network that includes several Windows servers and a file share containing sensitive documents.

Address the following: What chain of vulnerabilities enabled you to reach the file share from the guest network? List each step. How does this finding change the risk profile of the guest Wi-Fi (which previously had no identified vulnerabilities)? What remediation steps would you recommend in priority order? What does this scenario demonstrate about the difference between point vulnerabilities and vulnerability chains?

---

## Peer Response Guidance

A strong peer response does more than agree. Consider:

- Identifying a technical detail your classmate omitted or misstated
- Extending their remediation recommendation with an additional control
- Providing a counterargument to their risk rating with specific justification
- Connecting their scenario to a real-world breach or CVE you researched

---

## Grading Rubric (10 points)

| Criterion | Points |
|-----------|--------|
| Primary response addresses all scenario questions | 3 |
| Technical accuracy of security concepts | 2 |
| Demonstrates understanding of legal and ethical boundaries | 2 |
| Peer Response 1 — substantive technical contribution | 1.5 |
| Peer Response 2 — substantive technical contribution | 1.5 |
| **Total** | **10** |

**Note:** Responses that advocate for or describe testing without authorization, regardless of framing, will receive zero points for the affected criterion.
