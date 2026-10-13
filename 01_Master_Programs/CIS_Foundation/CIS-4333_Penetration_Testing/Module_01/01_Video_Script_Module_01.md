# Video Script: Module 01 - Penetration Testing Methodology and Scoping

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Estimated Duration:** 20-24 minutes
**Professor:** Nash

---

## Pre-Recording Checklist

- [ ] Title slide loaded: "Module 01 - Penetration Testing Methodology and Scoping"
- [ ] Terminal window open with dark theme
- [ ] Sample RoE template document ready to display
- [ ] PenTest+ PT0-002 domain map visible on second monitor

---

## [00:00 - 01:30] Opening and Module Overview

**[SLIDE: CIS-4333 Module 01 — Penetration Testing Methodology and Scoping]**

Welcome to CIS-4333 Penetration Testing at Texas Wesleyan University. I'm Professor Nash, and this is Module 01: Penetration Testing Methodology and Scoping.

This module covers the first and arguably most important phase of any penetration test — the work that happens before you ever touch a keyboard to launch a scan or run a tool. If you skip this phase, you are not doing a penetration test. You are committing a crime.

Everything we discuss today maps directly to the **Planning and Scoping** domain of the CompTIA PenTest+ PT0-002 exam, which accounts for **14 percent of the exam**. That is a significant slice, and the questions in this domain tend to be conceptual and scenario-based — exactly the kind of questions where understanding the *why* behind a process matters as much as memorizing a definition.

By the end of this module you will be able to:

- Explain the five phases of the penetration testing lifecycle
- Describe the purpose and contents of a Rules of Engagement document
- Distinguish between the scoping document, NDA, MSA, and authorization letter
- Apply target classification to organize in-scope assets
- Identify the key legal frameworks that govern authorized penetration testing in the United States

---

## [01:30 - 04:00] What Is Penetration Testing?

**[SLIDE: Definition and Purpose]**

A penetration test — often called a pentest — is a **simulated cyberattack performed with explicit written authorization** from the owner of the target systems. The goal is to find and safely exploit vulnerabilities before real attackers do, and then report those findings so they can be remediated.

Notice the phrase "explicit written authorization." That is not optional. Without it, every technical action a penetration tester takes is potentially a federal crime under the Computer Fraud and Abuse Act, or CFAA. We'll talk more about the legal framework in Module 02, but I want you to understand from the very first lesson: authorization is everything.

Penetration testing is distinct from vulnerability scanning. A vulnerability scanner, like Nessus or OpenVAS, identifies potential weaknesses. A penetration tester actively attempts to exploit those weaknesses to determine whether they are genuinely exploitable and what the real-world impact would be. We will cover vulnerability scanning in Module 05 and active exploitation in Module 06.

**[SLIDE: Pentest vs. Vulnerability Assessment vs. Red Team]**

You should also know these distinctions for the exam:

- A **vulnerability assessment** identifies and classifies weaknesses but does not exploit them
- A **penetration test** actively exploits vulnerabilities to demonstrate impact
- A **red team engagement** simulates a full adversary campaign, often including physical access attempts, social engineering, and long-duration persistence — all within authorization
- A **bug bounty program** crowdsources vulnerability discovery from external researchers under a public or private program scope

The PenTest+ exam may present scenarios asking you to identify which type of engagement is most appropriate for a given situation. The key differentiators are scope depth, exploitation intent, and duration.

---

## [04:00 - 08:00] The Five-Phase Penetration Testing Methodology

**[SLIDE: Five Phases — PTES Framework]**

Professional penetration testing follows a structured methodology. The most widely referenced framework is the Penetration Testing Execution Standard, or PTES. For the PT0-002 exam, CompTIA uses a five-phase model that closely aligns with PTES. Knowing this sequence is critical — exam questions frequently ask "what should the tester do next?" and the answer almost always follows this order.

### Phase 1: Planning and Scoping

This is what we cover today. Planning and scoping establishes the legal and operational boundaries of the engagement. It includes:

- Defining the scope of the test (what systems, IP ranges, and applications are in scope)
- Creating and signing the Rules of Engagement
- Executing the Non-Disclosure Agreement
- Determining the type of test (black box, white box, gray box)
- Setting the testing window and emergency contact procedures

No technical testing occurs during this phase. The entire phase is administrative and legal.

### Phase 2: Information Gathering and Reconnaissance

Once authorization is signed, the tester begins gathering information about the target. Reconnaissance is divided into passive (using publicly available sources without directly touching target systems) and active (interacting with target systems to gather technical details). We cover passive reconnaissance in Module 03 and active reconnaissance with Nmap in Module 04.

### Phase 3: Vulnerability Scanning and Analysis

In this phase, the tester uses automated tools and manual techniques to identify vulnerabilities in the target systems. We cover this in Module 05 with Nessus and OpenVAS. The output of this phase is a prioritized list of potential weaknesses to attempt in the next phase.

### Phase 4: Exploitation

This is where the tester attempts to exploit the identified vulnerabilities to gain unauthorized access, escalate privileges, or demonstrate the impact of a weakness. We cover Metasploit in Module 06, privilege escalation in Module 07, and lateral movement in Module 08. Every exploit attempt in this phase must stay within the authorized scope.

### Phase 5: Reporting

The final phase is producing a professional written report that documents the methodology, findings, evidence, risk ratings, and remediation recommendations. A penetration test without a report provides no value to the client. We dedicate Module 15 entirely to report writing.

**[SLIDE: Phase Sequence Diagram]**

Think of these phases as a pipeline. Each phase feeds into the next. You cannot skip phases — or rather, you can, but you will miss things, and the exam will test you on this. The most common trap question is: "A tester discovers a critical vulnerability during active scanning. Should they immediately attempt to exploit it?" The answer is almost always no — return to the methodology. Validate the finding, consult the RoE to confirm exploitation is authorized within the current phase boundaries, then proceed.

---

## [08:00 - 12:30] Pre-Engagement Documents

**[SLIDE: Pre-Engagement Document Hierarchy]**

This is the section that trips up a lot of exam candidates. There are multiple documents involved in a penetration testing engagement, and each one serves a distinct purpose. You need to know all of them.

### Non-Disclosure Agreement

The NDA is usually the first document signed. It creates a legal obligation for both the penetration tester and the client to keep all information shared during the engagement confidential. This protects the client's sensitive data and protects the tester from being accused of misusing information they encounter during testing.

### Master Service Agreement

If you work for a security firm that has an ongoing relationship with a client, the MSA is the overarching commercial contract that governs the relationship — payment terms, liability, warranty disclaimers, and general terms and conditions. The MSA does not authorize specific testing activities. It just establishes the commercial framework.

### Statement of Work

The SOW is attached to or incorporated into the MSA for a specific engagement. It defines what work will be performed, when, and for how much. For a pentest, the SOW would say something like: "Perform a black-box external network penetration test of the systems listed in Appendix A between the dates of X and Y."

### Rules of Engagement

This is the most important technical document and the one the PenTest+ exam tests most heavily. The RoE defines:

- The exact IP addresses, subnets, domains, and applications that are in scope
- The testing techniques that are permitted (and explicitly prohibited)
- The authorized testing window — specific dates and hours
- Communication protocols: who to contact if something goes wrong, how often to provide status updates
- Emergency stop conditions: circumstances under which testing must halt immediately
- Data handling rules: how to treat sensitive data discovered during testing
- Third-party notification requirements: if the target uses cloud providers or ISPs, their permission may also be required

### Authorization Letter

This is the document sometimes called the "get-out-of-jail card." It is a signed letter from an authorized executive of the client organization that explicitly states: the named individual or team is authorized to conduct the described penetration testing activities against the listed systems on the specified dates. The tester carries this document throughout the engagement and presents it if challenged by internal security staff, physical security, or law enforcement.

**[SLIDE: Document Summary Table]**

| Document | Purpose | Who Signs |
|---|---|---|
| NDA | Confidentiality | Both parties |
| MSA | Commercial terms | Both parties |
| SOW | Specific deliverables | Both parties |
| RoE | Testing boundaries and rules | Both parties |
| Authorization Letter | Proof of permission | Client executive |

Memorize this table. The exam will present scenarios describing a situation and ask which document is being referenced.

---

## [12:30 - 16:00] Scoping — Defining the Boundaries

**[SLIDE: Scoping in Detail]**

Scoping is the process of precisely defining what is and is not included in the penetration test. Good scoping documentation is unambiguous — it leaves no room for interpretation about whether a particular system, application, or network segment is authorized for testing.

### Types of Scope

Scope is defined along several dimensions:

- **Network scope**: specific IP addresses, CIDR ranges (e.g., 192.168.1.0/24), or named network segments
- **Application scope**: named web applications, APIs, or mobile apps that are in scope for testing
- **Physical scope**: are physical premises, badge readers, and building access systems in scope?
- **Social engineering scope**: is the tester permitted to call employees, send phishing emails, or tailgate into buildings?
- **Third-party scope**: are cloud provider systems, CDNs, or ISP infrastructure in scope? This often requires separate authorization from those third parties.

**[SLIDE: In-Scope vs. Out-of-Scope Example]**

Let's look at a concrete example. A client hires you to test their e-commerce web application. The scoping document says:

In scope:

- The web application at shop.example.com
- The API at api.example.com
- The database server at 10.10.1.50

Out of scope:

- All other internal servers
- The corporate email system
- Any third-party payment processor systems

During your test you discover that the database server at 10.10.1.50 connects to a backup server at 10.10.1.51. Even though you can see 10.10.1.51 from the database server, it is not in scope. You stop, document what you observed, and notify the client. You do not touch 10.10.1.51.

This is a critical concept on the PT0-002 exam. Proximity to an authorized system does not grant authorization.

### Target Classification

Once scope is defined, you classify in-scope assets. Classification helps you apply the right testing methodology and allocate time appropriately. Common classification categories include:

- Web applications (OWASP methodology applies)
- Network infrastructure (firewall, switches, routers)
- Wireless networks (Module 10)
- Endpoints (workstations, laptops)
- Servers (web servers, database servers, application servers)
- Physical (badge systems, locks, cameras)

Each category has different testing techniques, different tools, and different risk implications.

### Test Types

The PenTest+ exam also tests the three main test types:

- **Black box**: the tester has no prior knowledge of the target systems. This simulates an external attacker with no insider information.
- **White box**: the tester has full knowledge — network diagrams, source code, credentials. This allows thorough testing in the shortest time.
- **Gray box**: the tester has partial knowledge — perhaps a user-level account and some network diagrams. This is the most common real-world scenario.

---

## [16:00 - 19:00] Legal and Compliance Considerations

**[SLIDE: Legal Framework — CFAA and Related Laws]**

The Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030, is the primary US federal law governing computer intrusions. The CFAA makes it a crime to access a computer without authorization or to exceed authorized access. The phrase "without authorization" is critical — the authorization documents we discussed earlier are what make a penetration test legal under the CFAA.

Other relevant legal frameworks you should know for the exam:

- **GDPR**: Applies if the target handles personal data of EU residents. A penetration tester who discovers personal data during testing must handle it appropriately to avoid violating GDPR.
- **HIPAA**: Applies to healthcare organizations. If you are testing a healthcare client, you may encounter Protected Health Information (PHI). Your engagement documents must address how PHI is handled.
- **PCI DSS**: Payment Card Industry Data Security Standard. If the client processes credit card data, the penetration test scope and methodology may need to align with PCI DSS requirement 11.3.
- **State computer crime laws**: Many states have laws that parallel or extend the CFAA. Penetration testers working across state lines should understand that multiple state laws may apply.

**[SLIDE: Permission from Third Parties]**

One nuance the exam tests frequently: if the client's systems are hosted on a cloud provider, that cloud provider may have its own policies about penetration testing conducted against their infrastructure. For example, AWS has an acceptable use policy that allows customers to perform security testing on their own instances for specific service categories — but there are constraints. The penetration tester and client must review and comply with any such third-party policies before testing begins.

Similarly, if an ISP or CDN sits in front of the target, their permission may be required. A DDoS simulation or aggressive scanning campaign against a CDN node could violate the CDN provider's terms of service even if the client has authorized it.

---

## [19:00 - 22:00] Putting It Together — The Pre-Engagement Workflow

**[SLIDE: Pre-Engagement Workflow Steps]**

Let's walk through what a professional pre-engagement workflow looks like from start to finish.

Step 1: Initial scoping call with the client. Understand what they want to test, why, and what their concerns are.

Step 2: Draft and sign the NDA so that sensitive information shared during scoping discussions is protected.

Step 3: Conduct a thorough scoping interview. Document every system, application, IP range, and location the client wants included. Identify exclusions. Discuss test type.

Step 4: Draft the Statement of Work. Propose the testing approach, timeline, team, and deliverables.

Step 5: Draft the Rules of Engagement. This is the detailed technical document. Get it reviewed by legal counsel if necessary.

Step 6: Both parties sign the SOW and RoE. These signatures constitute formal written authorization.

Step 7: Obtain the Authorization Letter from an executive with authority to authorize the testing.

Step 8: Confirm third-party notifications are complete (cloud providers, ISPs, etc.).

Step 9: Begin technical testing — starting with reconnaissance.

**[SHOW TERMINAL]**

Let me show you what a simple scope definition looks like in a working document. In your lab this week, you will create a complete RoE document for a hypothetical engagement. Here is an example of the IP range documentation section:

```text
AUTHORIZED TARGETS — APPENDIX A
================================
Network Ranges:
  10.0.1.0/24   — Internal web application servers
  10.0.2.0/24   — Database tier
  203.0.113.10  — External-facing load balancer (public IP)

Specific Hosts:
  10.0.1.15     — staging.example.com (Apache 2.4, Ubuntu 22.04)
  10.0.2.20     — db-primary.internal (PostgreSQL 14)

EXCLUDED TARGETS:
  10.0.3.0/24   — Production HR systems (explicitly out of scope)
  203.0.113.0/28 — CDN provider edge nodes (requires separate auth)
```

This level of specificity is what separates a professional RoE from a vague agreement. Every system needs to be either explicitly included or explicitly excluded.

---

## [22:00 - 23:30] Exam Tips and Module Summary

**[SLIDE: PT0-002 Exam Tips — Module 01]**

Before we close, here are the exam tips that will help you score points on the PT0-002.

First: **Planning and Scoping is 14% of the exam**. Do not underestimate it. Every question in this domain is scenario-based. Read the scenario carefully and look for keywords like "before testing begins," "authorization," "out of scope," or "third-party systems."

Second: When in doubt, stop and ask. If an exam scenario presents a situation where a tester has found something unexpected — an unscoped system, a live production database, PII — the correct action is almost always to stop and notify the client before proceeding.

Third: Know the document hierarchy. NDA then MSA then SOW then RoE then Authorization Letter. Each document serves a distinct purpose and no document substitutes for another.

Fourth: Test type terminology matters. Black box means no knowledge. White box means full knowledge. Gray box means partial knowledge.

Fifth: The CFAA is the baseline US law. Authorization is what makes testing legal.

For additional study, I recommend the PenTest+ resources at **professormesser.com** and the official exam objectives at **comptia.org**. Both are free and comprehensive.

---

## [23:30 - 24:00] Closing

Your lab this week asks you to draft a complete scope of work and Rules of Engagement document for a hypothetical engagement scenario. Take it seriously — the document structure you practice in this lab is exactly what you would produce in a real professional engagement.

Your quiz covers the vocabulary and concepts from today's lecture. Your discussion post asks you to reason through a pre-engagement scenario.

I'll see you in Module 02, where we take a deeper dive into the legal and ethical framework of penetration testing, including the specific laws, compliance standards, and ethical obligations every professional penetration tester must understand.

Good luck, and remember: authorization first, always.

---

*All demonstrations and commands shown in this course are performed in authorized, isolated lab environments. No techniques demonstrated should be applied to systems without explicit written authorization from the system owner.*
