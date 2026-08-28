# Reading Guide: Module 01 - Penetration Testing Methodology and Scoping

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4333 &BULL; PENETRATION TESTING & ETHICAL HACKING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash

---

## Introduction

Welcome to Module 01. This reading guide establishes the professional and procedural foundation for all penetration testing work. Before a single packet is sent or tool is run, a professional penetration tester must define the scope, secure written authorization, and agree on the rules of engagement with the client.

These planning activities map directly to the **Planning and Scoping** domain of the CompTIA PenTest+ PT0-002 exam, which carries **14 percent of the exam weight**. Understanding scoping and methodology is critical not only for the exam but also for working legally and professionally in real environments. A penetration test performed without proper authorization is indistinguishable from a criminal intrusion — authorization documents are what separate ethical testers from attackers.

---

## Section 1: Core Vocabulary

### Definitions You Must Know

**Rules of Engagement (RoE):** A formal document agreed upon by the penetration tester and the client that specifies the permitted testing methods, time windows, authorized targets, communication protocols, and emergency stop conditions. The RoE is operationally binding and protects both parties by defining exactly what is in and out of scope before testing begins.

**Scoping Document:** A written agreement that defines the precise boundaries of a penetration test, including IP address ranges, domain names, physical locations, and specific systems authorized for testing. Scoping prevents testers from accidentally touching systems outside the client's authorization, reducing legal and operational risk.

**Target Classification:** The process of categorizing in-scope assets by type (web application, network infrastructure, wireless, physical, social engineering) and sensitivity level so that the penetration tester can prioritize testing efforts and apply the appropriate methodology. Classifications also influence the risk rating of discovered vulnerabilities.

**Authorization Letter:** A pre-engagement document — sometimes called the "get-out-of-jail card" — that a penetration tester carries during an engagement. It provides written proof from an authorized representative of the client organization that the tester is permitted to conduct the described security activities. This document is essential for preventing misunderstandings with internal security teams, law enforcement, or third-party providers.

**Non-Disclosure Agreement (NDA):** A legal contract requiring all parties to maintain confidentiality of sensitive information shared during the engagement. The NDA protects both the client's data and the tester's proprietary methods.

**Master Service Agreement (MSA):** A general commercial contract that governs the ongoing relationship between a security firm and a client, covering payment terms, liability, and warranties. The MSA is distinct from the RoE and does not itself authorize testing.

**Statement of Work (SOW):** A document tied to the MSA that describes the specific deliverables, timeline, and costs for a particular engagement. The SOW identifies what is being tested but the RoE defines the technical boundaries and rules.

**Black Box Test:** A penetration test in which the tester is given no prior knowledge of the target environment. This simulates an external attacker approaching the organization cold.

**White Box Test:** A penetration test in which the tester is given full knowledge of the environment, including network diagrams, source code access, and credentials. This allows the most thorough and efficient test.

**Gray Box Test:** A penetration test in which the tester has partial knowledge — for example, a standard user account and basic network documentation. This is the most common real-world scenario.

**Computer Fraud and Abuse Act (CFAA):** 18 U.S.C. § 1030, the primary US federal law criminalizing unauthorized access to computers. Written authorization is the legal instrument that makes penetration testing activities lawful under this statute.

**Penetration Testing Execution Standard (PTES):** An industry framework defining six phases of a professional penetration test: pre-engagement interactions, intelligence gathering, threat modeling, vulnerability analysis, exploitation, and post-exploitation. The CompTIA PT0-002 methodology aligns closely with PTES.

**Vulnerability Assessment:** A security review that identifies and classifies weaknesses in systems without actively attempting to exploit them. Distinguished from a penetration test by the absence of exploitation.

**Red Team Engagement:** A long-duration, full-scope adversarial simulation that may include physical access attempts, social engineering, and custom malware development — all within authorized boundaries. More comprehensive than a standard penetration test.

**Bug Bounty Program:** A program offered by organizations that invites external security researchers to find and responsibly disclose vulnerabilities, typically in exchange for monetary rewards. Governed by a public or private program scope document.

---

## Section 2: The Five-Phase Methodology

### Phase Overview

The PT0-002 exam consistently tests the correct sequence of penetration testing phases. Understanding what belongs in each phase — and what does not — is essential for answering scenario questions correctly.

| Phase | Name | Key Activities |
|---|---|---|
| 1 | Planning and Scoping | RoE, NDA, SOW, authorization, target classification |
| 2 | Reconnaissance | Passive OSINT, active scanning, enumeration |
| 3 | Vulnerability Analysis | Automated scanning, manual analysis, CVE mapping |
| 4 | Exploitation | Active exploitation, credential attacks, web app attacks |
| 5 | Reporting | Executive summary, technical findings, CVSS ratings, remediation |

### What Makes Each Phase Distinct

Phase 1 is entirely administrative and legal. No technical testing occurs. If a tester starts scanning before Phase 1 is complete and signed, they are operating without authorization.

Phase 2 gathers information about the target. Passive reconnaissance does not directly interact with target systems (using public records, WHOIS, LinkedIn, Google). Active reconnaissance does interact with target systems (Nmap scans, banner grabbing). Both require authorization to be in place first.

Phase 3 uses tools like Nessus and OpenVAS to systematically identify weaknesses. The output is a prioritized list of potential attack vectors. No exploitation occurs in this phase without explicit RoE authorization.

Phase 4 is where exploitation occurs. This is what most people picture when they think "hacking." Every action in this phase must fall within the authorized scope and methods defined in the RoE.

Phase 5 is the final deliverable. Without a report, no value is delivered to the client. The report must be clear, accurate, and actionable for both technical and executive audiences.

---

## Section 3: Pre-Engagement Document Comparison

### Document Hierarchy Table

| Document | When Signed | Primary Purpose | Authorizes Testing? |
|---|---|---|---|
| NDA | First | Confidentiality | No |
| MSA | Early | Commercial relationship | No |
| SOW | Before engagement | Deliverables and cost | No |
| RoE | Before testing | Technical boundaries and rules | Yes (with SOW) |
| Authorization Letter | Before testing | Proof of permission on-site | Yes |

### Key Distinctions for the Exam

The PT0-002 exam frequently tests whether candidates can distinguish between these documents. Memorize the following:

- An NDA protects information. It does not authorize testing.
- An MSA governs the business relationship. It does not authorize testing.
- A SOW describes the work. It does not specify technical testing rules.
- The RoE specifies exactly what is permitted technically. It is the operational authorization document.
- The Authorization Letter is the document carried on-site to prove legitimacy in real time.

---

## Section 4: Scoping in Depth

### Network Scope Documentation

Professional scoping uses CIDR notation to define authorized IP ranges unambiguously. For example:

- 10.0.1.0/24 authorizes 256 addresses (10.0.1.0 through 10.0.1.255)
- 192.168.50.0/28 authorizes 16 addresses (192.168.50.0 through 192.168.50.15)
- A single host is expressed as 10.0.1.15/32

Any IP address not listed or not within a listed range is out of scope. There is no implied authorization from proximity to an in-scope host.

### Application Scope Documentation

Web application scope should list:

- The exact domain names and subdomains in scope (e.g., app.example.com, api.example.com)
- Whether authentication bypass testing is permitted
- Whether denial-of-service conditions are permitted or prohibited
- Whether third-party components (CDN, payment processor) are in or out of scope

### Physical and Social Engineering Scope

Physical and social engineering scope must be explicitly defined and agreed upon. Never assume physical access attempts or phishing campaigns are authorized simply because network testing is authorized. These are distinct scope elements that require separate written approval.

### Handling Out-of-Scope Discoveries

When a tester discovers a system or vulnerability outside the agreed scope, the correct procedure is:

1. Stop all testing activity related to the out-of-scope asset
2. Document what was observed (IP address, system type, nature of discovery)
3. Notify the client point of contact immediately
4. Wait for written authorization before conducting any further activity on that asset

This procedure is tested extensively on the PT0-002 exam. The wrong answers always involve continuing testing, running even passive scans, or documenting findings from unauthorized exploitation.

---

## Section 5: Legal and Compliance Framework

### The CFAA and Authorization

The Computer Fraud and Abuse Act defines unauthorized access as a federal crime. Authorization — specifically written authorization from someone with legal authority over the systems — is the dividing line between a penetration test and a criminal act. Verbal agreements do not provide the same legal protection as written, signed documents.

### Industry Compliance Standards

| Standard | Industry | Relevant Requirement |
|---|---|---|
| PCI DSS | Payment card | Requirement 11.3 mandates external and internal penetration testing annually |
| HIPAA | Healthcare | Risk analysis must include assessment of technical safeguards |
| GDPR | EU data handlers | Requires appropriate technical security measures; breach notification obligations |
| SOC 2 | Service organizations | Penetration testing supports evidence for security trust service criteria |

### Third-Party Authorization

Cloud providers, CDNs, and ISPs are third parties that may have their own penetration testing policies. Before testing any system hosted by a third party, both the client and the tester must:

- Review the third party's acceptable use and security testing policies
- Obtain any required prior notification or approval from the third party
- Ensure the SOW and RoE explicitly address third-party considerations

Failure to obtain third-party authorization can violate those providers' terms of service, potentially exposing the client and tester to contractual and legal consequences.

---

## Section 6: Target Classification Detail

### Classification Categories and Methodology Alignment

| Asset Type | Example Systems | Primary Methodology |
|---|---|---|
| Web application | E-commerce site, internal portal, API | OWASP Testing Guide |
| Network infrastructure | Firewall, router, switch, VPN gateway | Network pentesting methodology |
| Wireless | Corporate Wi-Fi, guest network | Wireless pentesting (IEEE 802.11) |
| Endpoint | Workstations, laptops, kiosks | Client-side attack methodology |
| Server | Web server, database server, mail server | Service exploitation methodology |
| Physical | Badge readers, locks, cameras | Physical assessment methodology |
| Social engineering | Employees, help desk staff | Social engineering methodology |
| Cloud | AWS EC2 instances, Azure VMs, S3 buckets | Cloud security assessment methodology |

Classification is performed during the scoping phase and influences how the tester allocates time, which tools are used, and how findings are rated in the final report.

---

## Section 7: Engagement Types Compared

### Comparison Table

| Type | Tester Knowledge | Simulates | Typical Use Case |
|---|---|---|---|
| Black box | None | External attacker | External perimeter assessment |
| White box | Full (diagrams, code, creds) | Malicious insider or thorough audit | Code-level security review |
| Gray box | Partial (user account, some docs) | Compromised credential scenario | Most real-world assessments |
| Red team | Varies; typically minimal | Advanced persistent threat (APT) | Mature security programs |
| Bug bounty | None | Independent researcher | Continuous ongoing testing |

---

## Section 8: PenTest+ PT0-002 Exam Tips

### Tip 1 — Domain Weight

Planning and Scoping is 14 percent of the PT0-002 exam. Expect eight to ten questions directly from this domain. Questions test the why behind pre-engagement steps, not just tool names.

### Tip 2 — Authorization Boundary Scenarios

The exam frequently presents scenarios where a tester encounters an unscoped system. The correct answer is almost always: stop activity on that system and notify the client. Proceeding without updated authorization is unauthorized access regardless of how the system was discovered.

### Tip 3 — Document Identification

Know each document's specific purpose. If a question describes a document that "defines the permitted testing methods and IP ranges," that is the RoE — not the NDA or SOW.

### Tip 4 — Methodology Phase Order

Questions that ask "what should you do first?" or "what should the tester do next?" almost always expect a planning or authorization step before any technical activity. The sequence: Plan → Recon → Scan → Exploit → Report.

### Tip 5 — Verbal vs. Written Authorization

Written, signed authorization is required. Verbal agreements, recorded conversations, and email threads do not provide the same legal protection as a signed RoE. The exam will always favor written documentation.

### Tip 6 — Third-Party Cloud Considerations

If a target uses a cloud provider, the cloud provider's penetration testing policy applies. This is a commonly tested nuance. The client's authorization does not extend to cloud provider infrastructure without that provider's consent.

### Tip 7 — CFAA as the Legal Baseline

For US-based exam questions about legality, the CFAA is the primary law. Authorization is the element that determines whether an activity is lawful.

### Tip 8 — Test Type Defaults

When an exam scenario does not specify the test type, gray box is typically the assumed default for internal assessments. Black box is the default assumption for external assessments.

---

## Section 9: Required Study Resources

For exam preparation aligned to PT0-002 objectives, use these authorized resources:

- CompTIA official exam objectives document: available at **comptia.org**
- Professor Messer's free PT0-002 study materials: available at **professormesser.com**
- PTES technical guidelines: the Penetration Testing Execution Standard documentation

---

## Study Checklist

- [ ] Define Rules of Engagement, scoping document, authorization letter, NDA, MSA, and SOW without referring to notes
- [ ] Explain the five phases of the PTES-aligned methodology in order and describe one key activity per phase
- [ ] Distinguish black box, white box, and gray box test types by tester knowledge level and use case
- [ ] Describe the correct procedure when a tester encounters an out-of-scope system
- [ ] Identify the CFAA as the primary US law governing unauthorized computer access
- [ ] List three compliance standards (PCI DSS, HIPAA, GDPR) and describe the penetration testing requirement for each
- [ ] Explain why cloud provider authorization is a separate requirement from client authorization
- [ ] Review the document hierarchy table and memorize which document authorizes testing vs. which protects confidentiality
- [ ] Complete the Module 01 lab: draft a scope of work and Rules of Engagement for the hypothetical scenario
- [ ] Attempt all ten Module 01 quiz questions before checking answers

---

## 9. Supplemental Resources

**1. PTES Technical Guidelines — Penetration Testing Execution Standard**
[http://www.pentest-standard.org/index.php/Main_Page](http://www.pentest-standard.org/index.php/Main_Page)
The official PTES documentation defines the six phases of a professional penetration test in detail. Reading the Pre-Engagement Interactions section directly supports Module 01 scoping and RoE concepts.

**2. CompTIA PenTest+ Exam Objectives (PT0-002) — Official Objective List**
[https://www.comptia.org/certifications/pentest](https://www.comptia.org/certifications/pentest)
The official CompTIA objective document for PT0-002 maps every exam domain and sub-objective. Reviewing the Planning and Scoping domain (14% weight) alongside this reading guide ensures complete coverage of tested concepts.

**3. TCM Security — Practical Ethical Hacking Course: Pre-Engagement Module**
[https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course](https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course)
TCM Security's free and paid course content includes practical walkthroughs of pre-engagement documentation, scoping decisions, and authorization frameworks aligned to real-world consulting practice and eJPT/OSCP preparation.
