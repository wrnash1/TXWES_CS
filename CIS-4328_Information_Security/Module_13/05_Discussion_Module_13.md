# Discussion: Module 13 — Risk Management

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

Risk management is where security intersects with business strategy and resource allocation. Organizations make risk decisions every day — sometimes consciously, sometimes by default. This discussion asks you to apply the risk management frameworks from this module to a realistic scenario and engage with the difficult trade-offs that security professionals must navigate.

---

## Discussion Prompt

Read the following scenario, then respond to all three parts.

### Scenario

Meridian Logistics is a regional freight and warehousing company with 340 employees. Their IT environment includes an on-premises ERP system, a warehouse management system, fleet GPS tracking, and a customer-facing shipment tracking portal.

The security team completes a risk assessment and identifies three significant risks:

**Risk A — Ransomware against ERP system**

The ERP system tracks all financial transactions, invoicing, and customer contracts. ALE calculated at $480,000. The current control environment (antivirus only, no EDR, backups to the same on-prem NAS as the server) is rated as inadequate. Proposed mitigation: EDR solution + immutable off-site backup at $62,000/year. This would reduce ALE to $45,000.

**Risk B — GPS fleet tracking system accessible with default credentials**

All 47 fleet vehicles use a third-party GPS tracking system. An audit reveals the management console is accessible from the internet using the vendor's default admin password (unchanged since installation two years ago). ALE calculated at $38,000. Proposed mitigation: immediate password change + IP allowlist restriction, estimated at $0 additional cost.

**Risk C — Single ISP dependency**

All operations depend on a single ISP. An extended outage would halt customer portal access, GPS tracking, and ERP access for remote workers. ALE calculated at $215,000. Proposed mitigation: secondary ISP failover at $14,400/year. This would reduce ALE to $32,000.

The CEO reviews the risk register and says: "We're a logistics company, not a bank. I think we can accept Risk A and Risk B for now and maybe look at Risk C next year when budget frees up."

---

## Part 1 — Quantitative Analysis (Required)

For each of the three risks, calculate the Value of Safeguard (also called return on security investment) for the proposed mitigation.

Use the formula:

```
Value of Safeguard = Pre-mitigation ALE − Post-mitigation ALE − Annual cost of control
```

Show your work for each calculation. State which mitigations are economically justified based on the results.

---

## Part 2 — Response to the CEO (Required)

The CEO has proposed accepting all three risks. You are the security manager. Write a concise professional response (200 to 250 words) that:

- Acknowledges the CEO's authority to make risk acceptance decisions.
- Differentiates the risks: which one(s) are defensible to accept and which one(s) are not, and why.
- Addresses Risk B specifically — explain why accepting Risk B may not be possible even if leadership wants to.
- Uses at least one concept from the module (e.g., formal acceptance documentation, inherent vs. residual risk, regulatory context, or the economic justification from Part 1).

Your tone should be professional and advisory, not confrontational.

---

## Part 3 — Peer Response (Required)

Read at least two classmates' posts. For each:

- State whether you agree with their assessment of which risks are acceptable and which are not.
- Identify one risk management principle or formula they used correctly or incorrectly.
- Your reply to each classmate should be 75 to 100 words.

---

## Initial Post Guidelines

- Post your initial response (Parts 1 and 2) by the date listed in the course schedule.
- Peer responses (Part 3) are due 48 hours after the initial post deadline.
- Your initial post should be approximately 400 to 500 words total.
- Cite at least one external source — a NIST publication, industry report, regulatory guidance, or published risk management framework.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part 1 — Value of Safeguard calculations, all three risks, work shown | 35 |
| Part 2 — Professional memo differentiating risks and addressing CEO | 35 |
| Part 3 — Two substantive peer replies | 30 |
| **Total** | **100** |

---

## Instructor Note

The CEO scenario in this discussion reflects a real tension that security professionals face regularly. Leadership is not wrong to be cost-conscious. But not all risk acceptance decisions carry equal consequences. Part of the security profession's value is translating technical and regulatory risk into terms that allow leadership to make genuinely informed decisions — not to override leadership, but to ensure that "we accept this risk" is a choice, not a gap. Your post should demonstrate that distinction.

---

*End of Discussion — Module 13*
