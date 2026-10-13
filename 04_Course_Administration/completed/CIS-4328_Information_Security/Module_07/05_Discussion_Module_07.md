# Discussion Forum — Module 07: Network Security Architecture

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This discussion applies Module 07's network architecture concepts to current organizational challenges — specifically the death of the traditional network perimeter and the real-world tension between security, availability, and operational complexity in network design decisions.

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM

**Minimum Participation:** One original post (250–350 words) and two substantive replies (100+ words each).

---

## Scenario A — The Perimeter is Dead (or Is It?)

Security professionals have declared "the perimeter is dead" for more than a decade — arguing that the traditional model of trusting inside the network and distrusting outside is obsolete in a world of cloud applications, remote work, and supply chain compromises. Zero trust has emerged as the architectural response.

However, some practitioners push back: perimeter controls are still necessary, still effective, and zero trust introduces enormous operational complexity that many organizations cannot manage. Some have noted that poorly implemented zero trust can actually introduce new attack surfaces while dismantling well-understood perimeter controls.

In 250–350 words, respond to all three of the following:

1. Take a position: is the traditional network perimeter obsolete, still necessary, or does the answer depend on the organization? Defend your position using specific examples from the Module 07 concepts (firewall zones, DMZ, IPS, segmentation).

2. If you were advising a small healthcare clinic (50 employees, on-premises servers, one IT generalist) on network architecture, would you recommend zero trust or a well-implemented perimeter model? What is your reasoning given their specific resource constraints?

3. Zero trust requires continuous verification of identity and device posture for every access request. What specific challenges does this create for operational technology (OT) networks — factory floors, medical devices, building automation systems — where devices often cannot run agents and cannot be patched?

---

## Scenario B — The IPS Failure

A regional bank deployed an inline IPS configured to fail-closed on its core banking network. During a routine software update, the IPS vendor pushed an update that contained a bug causing the device to crash. The IPS went to fail-closed state, blocking all traffic. Online banking, ATM processing, and internal communications were unavailable for 2.5 hours during peak business hours.

The bank's CISO is now reviewing the fail behavior configuration and the overall resilience architecture.

In 250–350 words, respond to all three of the following:

1. Was fail-closed the correct configuration for a bank's core network? Argue both sides — the security rationale for fail-closed and the business continuity rationale against it — before stating your final recommendation.

2. Regardless of the fail behavior decision, what architectural change could have prevented a single IPS failure from taking down the entire network? Describe the specific design using the terminology from Module 07.

3. The vendor's software update caused the failure. What supply chain and change management controls should the bank have had in place to prevent this scenario? Reference concepts from both Module 04 (supply chain) and Module 07 (network architecture).

---

## Peer Reply Guidance

When replying to classmates, engage with one of these angles:

- If your classmate argued that the perimeter is obsolete, ask them to explain how they would handle networks where zero trust is not technically feasible (OT, legacy systems, resource-constrained environments).

- If your classmate recommended fail-open for the banking network, challenge them to explain how they would compensate for the reduced security during an extended failure period.

- If your classmate proposed a redundant IPS design, ask them whether redundancy addresses the root cause (a bad vendor update) or only the symptom (a single point of failure).

---

## Research Starting Points

- CISA Zero Trust Maturity Model: [https://www.cisa.gov/zero-trust-maturity-model](https://www.cisa.gov/zero-trust-maturity-model)

- NIST SP 800-207 Zero Trust Architecture: [https://csrc.nist.gov/publications/detail/sp/800-207/final](https://csrc.nist.gov/publications/detail/sp/800-207/final)

- CISA ICS Security: [https://www.cisa.gov/topics/industrial-control-systems](https://www.cisa.gov/topics/industrial-control-systems)

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Original post addresses all prompt questions | 40 |
| Demonstrates correct use of Module 07 terminology | 25 |
| Arguments are specific and technically grounded | 15 |
| Two substantive replies that add new reasoning | 20 |
| **Total** | **100** |

---

Module 07 Discussion — End
