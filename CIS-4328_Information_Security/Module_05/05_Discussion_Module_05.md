# Discussion Forum — Module 05: Cryptography and PKI

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This discussion connects Module 05's cryptographic concepts to real-world PKI failures, algorithm transitions, and the practical decisions security professionals face when deploying or auditing cryptographic systems.

**Initial Post Due:** Wednesday at 11:59 PM

**Peer Responses Due:** Sunday at 11:59 PM

**Minimum Participation:** One original post (250–350 words) and two substantive replies (100+ words each).

---

## Scenario A — The Certificate Expiration Cascade

A large healthcare organization experienced a widespread outage when an internal TLS certificate expired without warning. Automated monitoring had not been configured, the administrator who managed that system had left the organization, and the certificate had been issued with a five-year validity period — long enough that nobody remembered it existed. When the certificate expired, all internal services that relied on it stopped functioning, affecting clinical operations for four hours.

In 250–350 words, respond to all three of the following:

1. From a PKI lifecycle perspective, what specific process failure allowed this incident to occur? Identify at least two distinct process gaps, using the correct certificate lifecycle terminology from Module 05.

2. What technical controls could have prevented or significantly reduced the impact of this outage? Describe at least two controls, and explain the mechanism by which each would have helped.

3. Some organizations are now advocating for very short certificate validity periods — 90 days or even 30 days — rather than one-year or multi-year certificates. What is the security rationale for short-lived certificates? What operational challenges do short-lived certificates create, and how can automation address those challenges?

---

## Scenario B — Post-Quantum Cryptography

NIST finalized its first post-quantum cryptographic standards in 2024, including CRYSTALS-Kyber (ML-KEM) for key encapsulation and CRYSTALS-Dilithium (ML-DSA) for digital signatures. This is in direct response to the threat that a sufficiently powerful quantum computer could break RSA and ECC using Shor's algorithm, rendering most current asymmetric cryptography obsolete.

The threat is not immediate — large-scale quantum computers capable of breaking RSA-2048 do not yet exist — but nation-state adversaries are already engaged in "harvest now, decrypt later" attacks, collecting encrypted traffic today with the intent to decrypt it once quantum capability is available.

In 250–350 words, respond to all three of the following:

1. Explain why Shor's algorithm threatens RSA and ECC but does not similarly threaten AES. What property of symmetric encryption makes it relatively more resistant to quantum attacks?

2. What does "harvest now, decrypt later" mean as an attack strategy? Which current cryptographic mechanism, covered in Module 05, would mitigate the risk to past sessions even if RSA is eventually broken? Explain the mechanism.

3. Should organizations begin migrating their cryptographic infrastructure to post-quantum algorithms now, given that practical quantum computers are not yet available? Argue for or against early migration, and identify the specific risks on each side of the decision.

---

## Peer Reply Guidance

When replying to classmates, engage with one of these angles:

- If your classmate advocated for very short certificate validity periods, ask them to address the operational challenges in environments where automation is not feasible (embedded devices, air-gapped networks, legacy systems).

- If your classmate argued against early post-quantum migration, challenge them with the harvest-now-decrypt-later threat model and ask them to quantify how long current encrypted data needs to remain confidential.

- If your classmate identified specific technical controls for the certificate expiration scenario, evaluate whether those controls would have helped given the organizational context described (administrator departure, lack of monitoring).

---

## Research Starting Points

- NIST Post-Quantum Cryptography: [https://csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)

- Let's Encrypt Certificate Transparency: [https://letsencrypt.org/docs/ct-logs/](https://letsencrypt.org/docs/ct-logs/)

- Mozilla Root CA Program: [https://wiki.mozilla.org/CA](https://wiki.mozilla.org/CA)

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Original post addresses all prompt questions | 40 |
| Demonstrates correct use of Module 05 terminology | 25 |
| Arguments are supported with specific technical reasoning | 15 |
| Two substantive replies that add new reasoning | 20 |
| **Total** | **100** |

---

Module 05 Discussion — End
