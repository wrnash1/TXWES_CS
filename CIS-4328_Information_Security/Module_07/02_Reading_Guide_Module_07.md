# Reading Guide: Module 07 — Network Security Architecture

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This reading guide supports Module 07 of CIS-4328. It covers firewall types, IDS/IPS, DMZ design, proxy servers, load balancers, network segmentation, microsegmentation, zero-trust network architecture, NAC, and VPN configurations.

All readings use zero-cost, openly licensed resources.

---

## Learning Objectives

By the end of this module, you will be able to:

- Classify firewall types by capability (stateless, stateful, application-layer, NGFW, WAF).

- Distinguish IDS from IPS by deployment model, detection method, and function.

- Describe DMZ design using the dual-firewall architecture.

- Explain the difference between forward proxy and reverse proxy.

- Describe how load balancers contribute to availability and DDoS mitigation.

- Apply network segmentation and microsegmentation to reduce lateral movement.

- Describe the principles of zero-trust network architecture and contrast them with the perimeter model.

- Explain NAC posture assessment and quarantine VLAN.

- Compare site-to-site and remote access VPN, and evaluate the security implications of split tunneling.

---

## Primary Readings

### Reading 1 — NIST SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy

Source: [https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final](https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final)

Read: Chapter 2 (Firewall Overview) and Chapter 3 (Firewall Policy).

Focus areas:

- The evolution from packet filtering to stateful inspection to application-layer gateways.

- The principle of implicit deny and default-deny policy design.

- Ingress versus egress filtering and why both are necessary.

### Reading 2 — CISA Zero Trust Maturity Model

Source: [https://www.cisa.gov/zero-trust-maturity-model](https://www.cisa.gov/zero-trust-maturity-model)

Read: The full document (approximately 24 pages).

Focus areas:

- The five pillars of zero trust: Identity, Devices, Networks, Applications/Workloads, Data.

- The maturity stages: Traditional, Initial, Advanced, Optimal.

- How microsegmentation relates to the Network pillar.

### Reading 3 — NIST SP 800-207: Zero Trust Architecture

Source: [https://csrc.nist.gov/publications/detail/sp/800-207/final](https://csrc.nist.gov/publications/detail/sp/800-207/final)

Read: Section 2 (Zero Trust Basics) and Section 3 (Zero Trust Architecture Logical Components).

Focus areas:

- The Policy Enforcement Point (PEP) and Policy Decision Point (PDP) concepts.

- How zero trust applies to enterprise network design.

- The contrast between perimeter-based security and ZTA.

---

## Supplemental Readings

### Reading 4 — CISA IDS/IPS Overview

Source: [https://www.cisa.gov/uscert/ncas/tips/ST04-015](https://www.cisa.gov/uscert/ncas/tips/ST04-015)

Read: The full article.

Focus areas:

- Signature-based vs. anomaly-based detection trade-offs.

- Network-based vs. host-based deployment models.

- The role of IDS/IPS in a layered defense architecture.

### Reading 5 — NIST SP 800-77 Rev. 1: Guide to IPsec VPNs

Source: [https://csrc.nist.gov/publications/detail/sp/800-77/rev-1/final](https://csrc.nist.gov/publications/detail/sp/800-77/rev-1/final)

Read: Chapter 2 (IPsec Architecture Overview).

Focus areas:

- IPsec Transport mode vs. Tunnel mode.

- IKE (Internet Key Exchange) protocol overview.

- Comparison to TLS-based VPN approaches.

---

## Concept Reference Tables

### Table 1 — Firewall Type Comparison

| Firewall Type | OSI Layer | Key Capability | Exam Trigger |
|---|---|---|---|
| Packet Filter | Layer 3/4 | IP/port-based rules; stateless | Legacy; simple ACLs |
| Stateful Firewall | Layer 3/4 | Connection state tracking | Baseline for modern firewalls |
| Application-Layer Gateway | Layer 7 | Protocol-aware; proxy function | Deep content inspection |
| NGFW | Layer 3–7 | App ID, user identity, integrated IPS | "Identify apps regardless of port" |
| WAF | Layer 7 (HTTP) | Web app protection; OWASP Top 10 | SQL injection, XSS protection |

### Table 2 — IDS vs. IPS

| Characteristic | IDS | IPS |
|---|---|---|
| Function | Detect and alert | Detect and block |
| Placement | Out-of-band (SPAN/tap) | Inline (traffic flows through) |
| Impact on traffic | None | Can block; inline failure affects traffic |
| Fail behavior | N/A (passive) | Fail-open or fail-closed |
| False positive risk | Alerts only; no traffic impact | Can block legitimate traffic |

### Table 3 — Segmentation Models

| Model | Scope | Technology | Security Benefit |
|---|---|---|---|
| VLAN segmentation | Zone-level | Managed switch VLANs | Separate broadcast domains |
| Firewall zones | Zone-level | Firewall policies | Enforced traffic policy between zones |
| Microsegmentation | Workload-level | SDN, host-based agents | Policy between individual workloads |
| Zero Trust | End-to-end | Identity + device + policy | No implicit trust; verify all access |

### Table 4 — VPN Comparison

| Type | Scope | Protocol | Common Use |
|---|---|---|---|
| Site-to-site | Network-to-network | IPsec Tunnel mode | Branch office connectivity |
| Remote access (IPsec) | Client-to-network | IPsec Transport mode | Legacy corporate remote access |
| Remote access (TLS) | Client-to-application | TLS/HTTPS | Modern remote access; firewall-friendly |
| ZTNA | Client-to-application | TLS + identity | Zero trust remote access; replaces VPN |

---

## Key Terms and Definitions

**Firewall** — A network security device that monitors and controls incoming and outgoing traffic based on configured rules.

**NGFW** — Next-Generation Firewall; combines stateful inspection with application awareness, user identity, and integrated IPS.

**WAF** — Web Application Firewall; inspects HTTP/HTTPS traffic to protect web applications from application-layer attacks.

**IDS** — Intrusion Detection System; passively monitors traffic and generates alerts on suspicious activity.

**IPS** — Intrusion Prevention System; inline device that monitors and actively blocks suspicious traffic.

**Signature-Based Detection** — Compares traffic against known attack signatures; cannot detect novel attacks.

**Anomaly-Based Detection** — Compares traffic against a baseline; can detect novel attacks but generates more false positives.

**False Positive** — An alert triggered by benign activity.

**False Negative** — A failure to alert on actual malicious activity.

**Fail-Open** — Device failure allows traffic to pass uninspected; prioritizes availability.

**Fail-Closed** — Device failure blocks all traffic; prioritizes security.

**DMZ** — Demilitarized Zone; a network segment hosting internet-accessible servers, isolated from the internal network.

**Screened Subnet** — The technical term for a DMZ; a subnet filtered by one or more firewalls.

**Forward Proxy** — Intermediary between internal users and the internet.

**Reverse Proxy** — Intermediary between external clients and internal servers.

**SSL Offloading** — Terminating TLS at the load balancer or reverse proxy to reduce backend server load.

**Network Segmentation** — Dividing a network into separate zones with enforced access policies between them.

**Microsegmentation** — Applying access policies between individual workloads, not just network zones.

**Zero Trust** — Security model based on "never trust, always verify" regardless of network location.

**ZTNA** — Zero Trust Network Access; provides application-specific access based on identity and device posture, replacing broad VPN access.

**SDP** — Software-Defined Perimeter; makes resources invisible until authenticated; implements ZTNA principles.

**NAC** — Network Access Control; enforces device security posture before granting network access.

**Quarantine VLAN** — A restricted network segment for non-compliant devices where they can access only remediation resources.

**Implicit Deny** — The default rule at the end of a firewall policy that denies all traffic not explicitly permitted.

**Ingress Filtering** — Controlling inbound traffic.

**Egress Filtering** — Controlling outbound traffic.

**Split Tunneling** — VPN configuration where only corporate-bound traffic is encrypted through the VPN; internet traffic bypasses.

**Full Tunneling** — VPN configuration where all traffic routes through the corporate VPN gateway.

**VLAN** — Virtual LAN; a logical network segment within a physical switch infrastructure.

---

## Security+ Exam Alignment

The following SY0-701 exam objectives are covered in this module:

- 3.2 — Given a scenario, apply infrastructure security best practices.

- 3.3 — Compare and contrast concepts and strategies to protect data.

- 4.5 — Given a scenario, implement network security infrastructure.

---

## Critical Thinking Questions

1. An organization has placed its web server in the DMZ and its database server on the internal network. The web application needs to query the database. What firewall rule would you add to the inner firewall to enable this? How would you write the rule to apply least privilege?

2. A security team wants to detect lateral movement within the internal network. They have a SIEM, a NGFW at the perimeter, and no internal segmentation. What additional controls would most improve their ability to detect east-west (internal) lateral movement?

3. An attacker has compromised a workstation in the finance department of a fully microsegmented network. The workstation can communicate with finance servers but cannot reach HR, IT, or payroll servers. Compare the blast radius of this attack in a microsegmented network versus a flat network with no internal segmentation.

4. A company is evaluating replacing their remote access VPN with a ZTNA solution. What are the specific security advantages of ZTNA over traditional VPN? What challenges might the organization face during the transition?

5. An IPS deployed inline at a hospital network is set to fail-closed. During a software update, the IPS crashes and all network traffic stops, including communications to patient monitoring systems. Evaluate this design decision. What change would you recommend, and how would you compensate for the reduced security that change introduces?

---

## 9. Supplemental Resources

**1. NIST SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy**
<https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final>
NIST's authoritative guidance on firewall types, rule-set design, and policy management covering packet filtering, stateful inspection, and application-layer gateways. Directly supports Module 07 coverage of firewall classification, implicit deny, and ingress/egress filtering principles.

**2. NIST SP 800-207 — Zero Trust Architecture**
<https://csrc.nist.gov/publications/detail/sp/800-207/final>
The authoritative NIST publication defining Zero Trust Architecture (ZTA) components, design models, and deployment scenarios. Covers Policy Enforcement Points, Policy Decision Points, and the contrast between perimeter-based and zero-trust network models — directly aligning with Module 07 zero trust and ZTNA content.

**3. NSA Network Infrastructure Security Guide**
<https://media.defense.gov/2022/Jun/15/2003018261/-1/-1/0/CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDE_20220615.PDF>
The NSA's practical network hardening guide covering segmentation, out-of-band management, routing protocol security, and switch/router hardening. Provides real-world implementation detail for the network security architecture principles covered in Module 07.

---

## Review Checklist

Before taking the Module 07 quiz, verify you can do each of the following without notes:

- Name the five firewall types and state the key capability that distinguishes each from the previous.

- Explain why an IDS is out-of-band and an IPS is inline, and what consequence each placement has.

- Describe the dual-firewall DMZ and explain which servers belong in it.

- Distinguish forward proxy from reverse proxy by what each protects.

- Explain implicit deny in your own words without using the term "firewall."

- Describe microsegmentation and explain how it limits lateral movement compared to VLAN segmentation.

- State the three zero-trust principles and apply them to a specific network scenario.

---

Module 07 Reading Guide — End
