# Video Script: Module 07 — Security Architecture and Controls

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Pre-Roll Slide

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Introduction (0:00–1:30)

[SHOW SLIDE: Module 07 Title Card — Security Architecture and Controls]

Welcome back, everyone. Professor Nash here, and this is Module 07 of CIS-4315.

In Module 06 we built the foundation of a security program — the charter, the policy hierarchy, the strategy, and the resource plan. Now we're going to talk about what that program actually produces: the security architecture and the controls that protect your organization.

[PAUSE]

Security architecture is one of those terms that sounds highly technical but is fundamentally a management concept. Architecture answers the question: how do we organize our security controls so they work together effectively? And controls are the mechanisms — technical, administrative, and physical — that reduce risk to acceptable levels.

[SHOW SLIDE: Module 07 Learning Objectives]

Today we're covering four areas. First, the defense-in-depth philosophy and why it matters. Second, security control frameworks and how to use them. Third, the NIST Cybersecurity Framework in practical depth. And fourth, the major control categories: network, endpoint, and data controls.

Let's get into it.

---

## Section 1: Defense-in-Depth (1:30–6:00)

[SHOW SLIDE: What Is Defense-in-Depth?]

Defense-in-depth is the foundational architectural philosophy of information security. The core idea is simple: no single control is perfect, so you layer multiple controls so that when one fails, others compensate.

[PAUSE]

The concept comes from military strategy. A medieval castle didn't rely on just one wall — it had a moat, an outer wall, an inner wall, a keep, and armed defenders at each layer. If attackers breached the moat, they still faced the outer wall. If they scaled that, the inner wall awaited them. Each layer bought time and imposed cost on the attacker.

[SHOW SLIDE: Defense-in-Depth Applied to Information Security]

In information security, we build similar layers. The outermost layer is perimeter security — firewalls, intrusion prevention systems, and network segmentation. The next layer is host-based security — endpoint protection, host firewalls, and application whitelisting. Inside that, we have application security — authentication, input validation, and secure coding. And at the core, we have data security — encryption, access controls, and data loss prevention.

[PAUSE]

[SHOW DIAGRAM: Concentric Circles — Perimeter, Network, Host, Application, Data]

Think of these as concentric rings. An attacker who penetrates your perimeter still faces network controls. If they compromise a host, application controls constrain what they can access. If they reach an application, data controls limit what they can exfiltrate.

The key insight is that defense-in-depth is about resilience, not perfection. You're not trying to make any one control impenetrable. You're making the overall attack path expensive enough that attackers either fail or are detected before they reach their objective.

[SHOW SLIDE: Defense-in-Depth and Control Types]

Defense-in-depth works across three dimensions: control types, control categories, and deployment layers.

Control types are: preventive controls that stop attacks before they succeed, detective controls that identify attacks in progress, and corrective controls that restore normal operations after an attack. A comprehensive architecture includes all three types at each layer.

Control categories are: technical controls implemented in systems and software, administrative controls expressed in policies and procedures, and physical controls protecting facilities and hardware.

[PAUSE]

A mature security architecture addresses all three types and all three categories across all relevant layers. Gaps in any combination create exploitable weaknesses.

---

## Section 2: Security Control Frameworks (6:00–11:00)

[SHOW SLIDE: Why Use a Framework?]

Building a security architecture from scratch, without reference to established frameworks, is inefficient and risky. You'll miss controls that experienced practitioners have identified as essential. Control frameworks solve this problem by providing structured, comprehensive catalogs of security controls that organizations can adopt, adapt, and implement.

[PAUSE]

The major frameworks you need to know for CISM and for professional practice are: NIST SP 800-53, ISO/IEC 27001, CIS Controls, and the NIST Cybersecurity Framework. Each has a different emphasis and use case, but they complement each other well.

[SHOW SLIDE: NIST SP 800-53 — Control Catalog]

NIST SP 800-53 is the most comprehensive control catalog in the industry. It currently contains over 1,000 controls organized into 20 control families. Originally developed for U.S. federal agencies, it has become the de facto standard for any organization seeking a rigorous security program.

The 20 control families cover everything from Access Control to System and Communications Protection. For the CISM exam, you don't need to memorize all 1,000 controls. You need to understand the family structure and be able to identify which family addresses a given security requirement.

[PAUSE]

Key families to recognize: Access Control (AC), Audit and Accountability (AU), Incident Response (IR), Risk Assessment (RA), Security Assessment (CA), and System and Communications Protection (SC).

[SHOW SLIDE: ISO/IEC 27001 and CIS Controls]

ISO/IEC 27001 is the international standard for information security management systems. Where NIST 800-53 is a control catalog, ISO 27001 is a management system standard — it tells you how to build the management framework around your controls, not just which controls to implement.

ISO 27001 Annex A contains 93 controls organized into four themes: Organizational, People, Physical, and Technological. Organizations can pursue ISO 27001 certification, which provides external validation of their security management system.

[PAUSE]

The CIS Controls — now at version 8 — take a different approach. They identify the 18 most critical security actions, prioritized by which controls have the highest impact against the most common attack techniques. The CIS Controls are particularly useful for organizations that need to prioritize with limited resources. The first six controls — often called Implementation Group 1 — are described as the essential cyber hygiene that every organization should have regardless of size.

---

## Section 3: NIST Cybersecurity Framework (11:00–16:00)

[SHOW SLIDE: NIST CSF — Overview]

The NIST Cybersecurity Framework deserves its own section because it's become the lingua franca of security program communication. Released in 2014, updated in 2018, and significantly revised in version 2.0 in 2024, the CSF provides a common structure for describing security program activities that works equally well for technical teams and executive leadership.

[PAUSE]

The original CSF 1.1 organizes activities into five functions: Identify, Protect, Detect, Respond, and Recover. CSF 2.0 adds a sixth function: Govern. Let's walk through each.

[SHOW SLIDE: CSF Function — Identify]

Identify is the foundation. Before you can protect anything, you must know what you have. The Identify function covers asset management, business environment understanding, governance, risk assessment, and risk management strategy. If you can't answer "what systems do we have, what data do they process, and what risks do they face" — you're not doing Identify well.

[SHOW SLIDE: CSF Function — Protect]

Protect contains the preventive controls. Identity management and access control, awareness and training, data security, information protection processes, maintenance, and protective technology all live in the Protect function. This is where most security spending concentrates.

[PAUSE]

[SHOW SLIDE: CSF Function — Detect]

Detect covers the ability to identify cybersecurity events. Anomalies and events detection, security continuous monitoring, and detection processes. The critical insight here is that many organizations over-invest in Protect and under-invest in Detect. A sophisticated attacker will eventually penetrate your preventive controls. If you can't detect them, you can't respond.

[SHOW SLIDE: CSF Function — Respond and Recover]

Respond covers what happens when you do detect an event: response planning, communications, analysis, mitigation, and improvements. Recover covers restoration: recovery planning, improvements, and communications.

[PAUSE]

And CSF 2.0's new addition, Govern, addresses organizational context, risk management strategy, roles, policies, and oversight — essentially the governance function that enables all other functions to operate effectively.

[SHOW SLIDE: CSF Tiers and Profiles]

Beyond the functions and categories, the CSF has two additional tools: Tiers and Profiles.

Tiers describe the rigor of an organization's risk management practices on a four-point scale: Partial, Risk Informed, Repeatable, and Adaptive. Tiers are used for maturity assessment and target-setting.

Profiles describe the current or desired state of the security program expressed in CSF terms. A Current Profile documents what the organization does today. A Target Profile documents where it wants to be. The gap between them drives the roadmap.

---

## Section 4: Network, Endpoint, and Data Controls (16:00–21:30)

[SHOW SLIDE: Control Categories in Practice]

Let's now look at the major control categories you'll implement in a real security architecture. We'll cover network controls, endpoint controls, and data controls — the three domains where most security investment is concentrated.

[SHOW SLIDE: Network Controls]

Network controls establish the foundation of your security architecture. The primary categories include:

Perimeter controls: Next-generation firewalls with application-layer inspection, intrusion prevention systems, and DDoS mitigation. The perimeter is not dead — even in a cloud-first environment, network segmentation remains critical.

Network segmentation: Dividing the network into security zones — trusted, semi-trusted, and untrusted — with controlled traffic flows between them. Flat networks where every device can communicate freely are a nightmare for lateral movement during an incident.

[PAUSE]

Zero Trust Network Access: The emerging architecture paradigm that replaces implicit trust based on network location with explicit verification of every access request. ZTNA assumes the network is already compromised and requires authentication and authorization for every connection.

Network monitoring: Security information and event management systems, NetFlow analysis, and network detection and response tools that identify anomalous traffic patterns.

[SHOW SLIDE: Endpoint Controls]

Endpoint controls protect the devices — laptops, servers, mobile phones — where work actually happens. Key categories include:

Endpoint Detection and Response, or EDR: Next-generation endpoint protection that goes beyond signature-based antivirus to behavioral detection, threat hunting, and automated response capabilities.

Application control: Preventing unauthorized software from executing. Allowlisting — only approved applications run — is more secure but operationally demanding. Denylisting — known bad applications are blocked — is easier but less comprehensive.

[PAUSE]

Patch management: Keeping operating systems and applications current to eliminate known vulnerabilities. Most successful attacks exploit vulnerabilities for which patches have existed for months. Patch management is unglamorous but enormously effective.

Device encryption: Encrypting the full disk on all endpoints so that lost or stolen devices don't result in data breaches.

[SHOW SLIDE: Data Controls]

Data controls protect information throughout its lifecycle — at rest, in transit, and in use.

Data classification: Tagging data by sensitivity level (e.g., Public, Internal, Confidential, Restricted) so that controls can be applied proportionally. You can't protect everything equally — classification tells you what deserves your strongest controls.

Data Loss Prevention, or DLP: Technology that identifies, monitors, and prevents unauthorized transmission of sensitive data. DLP can operate at the network layer (blocking outbound email with SSN patterns), at the endpoint (blocking USB transfers of classified files), or in the cloud.

[PAUSE]

Encryption: Data at rest should be encrypted in databases, file systems, and backups. Data in transit should use TLS 1.2 or higher. The key management program is as important as the encryption itself — encrypted data with poorly protected keys is not secure.

Rights management: Information Rights Management, or IRM, extends access control into the documents themselves, preventing unauthorized forwarding, printing, or editing even after a file leaves the organization's systems.

---

## Section 5: Integrating Architecture and Controls (21:30–23:30)

[SHOW SLIDE: Putting It Together — Security Architecture Review]

A security architecture isn't a static diagram. It's a living design that must be reviewed regularly against the threat landscape, business changes, and technology evolution.

Security architecture review processes typically include:

New project reviews, where security requirements are built into systems during design rather than bolted on after deployment. This is the "shift left" principle — catching security issues earlier in the development lifecycle is dramatically cheaper than fixing them after production.

[PAUSE]

Periodic architecture reviews, where the overall design is assessed against the current threat landscape. What was an adequate architecture three years ago may have significant gaps today.

Exception management, where deviations from the approved architecture are formally tracked, risk-accepted, and remediated on a schedule.

[SHOW SLIDE: CISM Exam Connection — Module 07]

For your CISM exam, the key Module 07 concepts map directly to Domain 3 exam questions.

Defense-in-depth is tested in scenario questions where you must identify why a single control failure led to a breach. The correct answer almost always involves a missing compensating control at another layer.

Framework selection questions test your ability to match an organizational need to the right framework — NIST 800-53 for comprehensive control selection, CSF for program communication and maturity, CIS Controls for prioritized implementation.

[PAUSE]

Control categorization questions ask you to classify controls as preventive, detective, or corrective, and as technical, administrative, or physical.

[SHOW SLIDE: Module 07 Summary]

Let's recap Module 07.

We covered defense-in-depth — the layered control philosophy that builds resilience through redundancy. We examined the major security control frameworks: NIST SP 800-53 for comprehensive control selection, ISO 27001 for management system certification, and CIS Controls for prioritized implementation.

We went deep on the NIST Cybersecurity Framework, including its six functions — Govern, Identify, Protect, Detect, Respond, and Recover — and the Tiers and Profiles tools. And we surveyed the major control domains: network, endpoint, and data controls, with emphasis on the controls that matter most for defending real organizations.

[PAUSE]

Your lab this week asks you to map a sample organization's control inventory to the NIST CSF and identify gaps. Your quiz will test your ability to classify controls and select appropriate frameworks. The discussion asks you to evaluate a defense-in-depth failure in a real-world breach scenario.

See you in Module 08, where we tackle security awareness and training programs.

[SHOW SLIDE: End Card]

---

*End of Video Script — Module 07*
