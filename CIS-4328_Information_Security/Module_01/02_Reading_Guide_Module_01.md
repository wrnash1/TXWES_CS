# Reading Guide: Module 01 - Threats, Attacks, and Vulnerabilities
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 01 – Threats, Attacks, and Vulnerabilities**! This module establishes the foundation of the entire Security+ exam. You will learn to categorize threat actors by motivation and capability, distinguish attack types, and apply the CIA triad to real-world scenarios. These concepts appear throughout every domain of the SY0-701 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Threat Actor**: An individual or group that poses a potential danger to an organization's information systems. SY0-701 classifies actors by attributes: nation-state (highly resourced, long-term espionage), hacktivist (ideologically motivated), insider threat (authorized access misused), and script kiddie (low skill, uses pre-built tools). Knowing the actor determines the likely motive and capability of an attack.
*   **Vulnerability**: A weakness in a system, application, or process that can be exploited by a threat actor to cause harm. Vulnerabilities include unpatched software, misconfigured services, and weak passwords. SY0-701 expects you to distinguish between a vulnerability (the weakness), a threat (the actor or event that could exploit it), and risk (the likelihood and impact of exploitation).
*   **Zero-Day Exploit**: An attack that leverages a previously unknown vulnerability for which no vendor patch exists, leaving defenders zero days of advance warning. Because signature-based detection cannot identify a zero-day, organizations rely on behavioral analysis and EDR tools to detect anomalous activity before a patch is released.
*   **CIA Triad**: The three core objectives of information security — **Confidentiality** (data accessible only to authorized parties, enforced by encryption), **Integrity** (data is accurate and unaltered, enforced by hashing and digital signatures), and **Availability** (systems and data are accessible when needed, enforced by redundancy and backups). Every security control maps back to one or more of these pillars.
*   **Attack Surface**: The total set of entry points where an attacker can attempt to compromise a system or extract data. Reducing the attack surface through hardening — disabling unused services, closing open ports, and removing unnecessary software — is a core defensive practice tested on SY0-701.
*   **Threat Intelligence**: Processed information about current and emerging threats used to inform defensive decisions. Sources include OSINT (Open-Source Intelligence), ISACs (Information Sharing and Analysis Centers), and commercial threat feeds. SY0-701 Domain 4 (Security Operations, 28%) tests applied use of threat intelligence.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Module 01 topics fall primarily under **Domain 2 – Threats, Vulnerabilities, and Mitigations (22%)** of the SY0-701 exam. Expect approximately 16–18 questions touching this domain across the full exam.
*   **Trap – Threat vs. Risk vs. Vulnerability:** SY0-701 scenario questions frequently use all three terms in the same stem. A vulnerability is the weakness; a threat is the actor or event that exploits it; risk equals likelihood multiplied by impact. Never confuse these.
*   **Memorize Threat Actor Attributes:** The exam distinguishes actors by sophistication, resources, and motive. Nation-state = high sophistication + espionage; hacktivist = moderate skill + ideology; insider = authorized access + intent; script kiddie = low skill + opportunistic.
*   **Active vs. Passive Attacks:** Passive attacks (eavesdropping, traffic analysis) observe without modification; active attacks (replay, injection, MITM) modify or inject data. The exam tests this distinction in network scenario questions.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) cover every exam objective with concise, exam-focused explanations — specifically designed for the current exam version.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Threats, Attacks, and Vulnerabilities" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). These free notes are written to match exam objectives and updated for the current exam version.
*   **Required Video:** Watch the corresponding video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). Each video is 5–15 minutes and aligns directly to a specific exam objective.

---

### Lab & Command Integration
In this week's hands-on lab, you will use reconnaissance and enumeration tools to identify vulnerabilities in a controlled environment. Focus on understanding what information each tool reveals and how an attacker would leverage it — this connects directly to SY0-701 performance-based questions (PBQs).

---

### 3. Study Checklist
- [ ] Read the glossary terms above and write each definition in your own words.
- [ ] Read the "Threats, Attacks, and Vulnerabilities" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the corresponding video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Be able to classify any attack scenario by: threat actor type, CIA triad pillar targeted, and active vs. passive category.
- [ ] Proceed to the weekly hands-on lab activity.
