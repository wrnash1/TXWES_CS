# Reading Guide: Module 01 - Penetration Testing Methodology and Scoping
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 01 - Penetration Testing Methodology and Scoping**! This module establishes the professional and procedural foundation for all penetration testing work. Before a single packet is sent or tool is run, a professional penetration tester must define the scope, secure written authorization, and agree on the rules of engagement with the client. These planning activities directly map to the **Planning and Scoping** domain of the CompTIA PenTest+ PT0-002 exam, which carries **14% of the exam weight**.

Understanding scoping and methodology is critical not only for the exam but also for working legally and professionally in real environments. A penetration test performed without proper authorization is indistinguishable from a criminal intrusion — authorization documents are what separate ethical hackers from attackers.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Rules of Engagement (RoE)**: A formal document agreed upon by the penetration tester and the client that specifies the permitted testing methods, time windows, authorized targets, communication protocols, and emergency stop conditions. The RoE is operationally binding and protects both parties by defining exactly what is in and out of scope before testing begins.

*   **Scoping Document**: A written agreement that defines the precise boundaries of a penetration test, including IP address ranges, domain names, physical locations, and specific systems authorized for testing. Scoping prevents testers from accidentally (or intentionally) touching systems outside the client's authorization, reducing legal and operational risk.

*   **Target Classification**: The process of categorizing in-scope assets by type (web application, network infrastructure, wireless, physical, social engineering) and sensitivity level so that the penetration tester can prioritize testing efforts and apply the appropriate methodology. Classifications also influence the risk rating of discovered vulnerabilities.

*   **Permission Checklist / Authorization Letter**: A pre-engagement document — sometimes called a "get-out-of-jail" card — that a penetration tester carries during an engagement. It provides written proof from an authorized representative of the client organization that the tester is permitted to conduct the described security activities. This document is essential for preventing misunderstandings with internal security teams, law enforcement, or third-party providers.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Planning and Scoping is **14% of the PT0-002 exam**. Expect 8–10 questions directly from this domain. Every question in this domain tests whether you understand the *why* behind pre-engagement steps, not just the tools.
*   **Exam Trap — Authorization vs. Scope:** PT0-002 frequently presents scenarios where a tester discovers an unscoped system during testing. The correct answer is almost always to **stop and notify the client** rather than proceed. Proceeding without updated authorization is unauthorized access.
*   **Exam Trap — RoE vs. NDA vs. MSA:** Know the difference. An NDA protects sensitive information shared between parties. An MSA is a master commercial agreement. An SLA defines service uptime. The **RoE specifically defines testing boundaries and permitted actions** — that is what makes it unique.
*   **Methodology Order:** PT0-002 tests the five-phase methodology: Planning/Scoping → Reconnaissance → Scanning/Enumeration → Exploitation → Post-Exploitation → Reporting. Questions that ask "what should you do first?" almost always expect a planning or authorization step before any technical activity.
*   **Legal Frameworks Tested:** Know the Computer Fraud and Abuse Act (CFAA) as the primary US federal law governing unauthorized computer access. Authorization is what makes testing legal.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — TryHackMe is a browser-based cybersecurity training platform with guided rooms covering each phase of the penetration testing methodology. The Pentest Learning Path includes dedicated rooms on pre-engagement, scoping, and authorization fundamentals that align directly with PT0-002 objectives.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — A comprehensive free video walkthrough of all PT0-002 domains. Seek to the Planning and Scoping section for this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the pre-engagement and scoping rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe provides interactive, browser-based labs that let you practice concepts without needing a local VM setup.
*   **Required Video:** Watch the Planning and Scoping segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This free course covers all PT0-002 domains in a single video; use the chapter markers to navigate to Module 01 content.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Draft a mock Rules of Engagement (RoE) document**: You will create a realistic RoE that includes testing window, authorized IP ranges, prohibited techniques, emergency contact procedures, and escalation paths — mirroring what professional testers deliver to clients before an engagement begins.
*   **Define IP range boundaries for pen test target scope**: Using CIDR notation, you will document the specific subnets authorized for scanning and exploitation, and practice identifying which systems fall inside vs. outside the agreed scope.
*   **Review target disclosure guidelines**: You will analyze how sensitive findings (e.g., critical CVEs, PII exposure) must be handled, including immediate notification requirements and data handling rules to protect the client during a live engagement.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the pre-engagement rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Planning and Scoping section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
