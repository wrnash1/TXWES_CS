# Discussion Board: Module 04 – Enterprise Security & Infrastructure Hardening
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 15, 2026 at 11:59 PM CST

---

## Graduate Discussion Instructions
Initial post: **400+ words**, all prompt components addressed, at least **1 credible technical citation**.
Peer responses: **Substantive replies to 2+ classmates** — challenge assumptions, offer alternative mitigations, or extend the analysis.

---

## Discussion Prompt: The Zero-Trust Network Access Debate in Enterprise Security

**Scenario:**
Your organization is a mid-sized financial services firm with 2,500 employees across 8 office locations. The CISO has received a proposal from two competing security teams:

**Team Alpha's Proposal — "Harden What We Have":**
Implement the full CIS Cisco IOS Benchmark on all 47 network devices. Deploy DHCP Snooping, DAI, and 802.1X on all wired access ports. Apply Control Plane Policing on all routers and multilayer switches. Tighten BGP filters on all edge routers. Estimated cost: $180,000 in professional services + 6 months of implementation. No new hardware required.

**Team Beta's Proposal — "Zero Trust Network Access (ZTNA)":**
Replace the traditional perimeter model with a Zero Trust architecture. All internal users must authenticate with MFA before accessing any application, regardless of network location. Network microsegmentation is enforced by a software-defined policy engine. No implicit trust is granted even to users inside the corporate network. Estimated cost: $1.2 million in licensing + 18 months of implementation. Requires new NAC and identity infrastructure.

**Write a graduate-level post (400+ words) addressing ALL of the following:**

1. **Evaluate Team Alpha's Proposal:** The CIS Benchmark and Layer 2 controls address network-level threats (ARP spoofing, DHCP attacks, control plane flooding). Are these controls still relevant in a modern enterprise where most applications are SaaS and hosted in the cloud? What threats do they address that ZTNA does not?

2. **Evaluate Team Beta's ZTNA Proposal:** What specific security problems does Zero Trust solve that traditional network hardening cannot? What is the core architectural difference between "trust once inside the perimeter" and "never trust, always verify"? In the context of hybrid work (some employees remote, some in-office), which model is better and why?

3. **The Complementary Argument:** Some security architects argue that ZTNA and traditional network hardening are not competing alternatives — they are complementary. Make the technical argument for why a mature enterprise might need BOTH. What specific attack scenarios require network-layer controls even in a ZTNA environment?

4. **Your Recommendation:** Given the $180K vs. $1.2M cost difference and 6-month vs. 18-month timelines, which proposal would you recommend to the CISO — or would you propose a phased approach? Justify your recommendation with specific technical and business reasoning.

**Citation:** Cite at least one of:
- NIST SP 800-207 — Zero Trust Architecture (free: csrc.nist.gov)
- CIS Benchmarks for Cisco IOS (free: cisecurity.org)
- NIST SP 800-41 Rev 1 — Firewalls and Firewall Policy
- A peer-reviewed paper on enterprise ZTNA deployment (IEEE Xplore via TXWES West Library)

---

## Peer Response Guidance
After posting your recommendation, respond to two classmates whose position differs from yours. If a classmate recommends ZTNA only, challenge them with a specific Layer 2 attack that ZTNA does not address. If a classmate recommends hardening only, challenge them with a specific lateral movement scenario that Layer 2 controls cannot prevent.

---

## Grading Rubric (100 Points)
| Component | Points |
|---|---|
| Team Alpha evaluation — relevance of network hardening controls | 20 |
| Team Beta evaluation — ZTNA principles and advantages | 25 |
| Complementary argument — technical justification for both | 20 |
| Recommendation — justified with technical and business reasoning | 20 |
| Citation — credible, properly integrated | 5 |
| Peer responses — substantive, technically advances discussion | 10 |
| **Total** | **100** |
