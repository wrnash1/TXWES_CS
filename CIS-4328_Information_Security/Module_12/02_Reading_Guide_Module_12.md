# Reading Guide: Module 12 - Incident Response
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 12 – Incident Response**! Incident response (IR) is the structured process organizations use to detect, contain, eradicate, and recover from security incidents. SY0-701 tests IR heavily in Domain 4 (Security Operations, 28%) — expect scenario questions on selecting the correct IR phase action, classifying incident types, and understanding the roles of IR tools.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Incident Response Lifecycle (NIST SP 800-61)**: The four-phase NIST framework for incident response: (1) Preparation — establishing IR policies, playbooks, and tooling before incidents occur; (2) Detection and Analysis — identifying and confirming that a security event is a genuine incident; (3) Containment, Eradication, and Recovery — stopping the spread, removing the threat, and restoring systems; (4) Post-Incident Activity — conducting lessons-learned reviews and updating controls. SY0-701 scenario questions frequently ask which phase a described action belongs to.
*   **Containment Strategies**: Incident containment limits the damage while preserving evidence. Short-term containment (immediate isolation — disconnecting an infected host from the network) stops active spread. Long-term containment (patching, hardening) prepares for recovery. Forensic imaging should occur before eradication to preserve evidence. SY0-701 tests the order: contain first, then eradicate, then recover — never skip containment to go straight to restoration.
*   **Indicators of Compromise (IOCs)**: Artifacts and observable evidence that a system has been breached or attacked. Common IOCs include unusual outbound network connections, unexpected process executions, new administrator accounts, modified system files, and large data transfers at unusual hours. IOCs are used to detect incidents, hunt for threats in the environment, and share intelligence with other organizations via formats like STIX/TAXII.
*   **Security Information and Event Management (SIEM)**: A platform that aggregates, normalizes, and correlates log data from across the environment (firewalls, endpoints, servers, cloud services) and generates alerts when rules or behavioral baselines are violated. SIEM is the primary tool used during the Detection and Analysis phase of IR. SY0-701 tests SIEM in scenarios involving centralized log management, alert triage, and compliance reporting.
*   **Playbooks and Runbooks**: A playbook is a documented, step-by-step response procedure for a specific incident type (e.g., ransomware playbook, phishing playbook). A runbook is a more technical document describing how to execute specific operational tasks within a playbook (e.g., how to isolate a host in the EDR console). Playbooks ensure consistent, repeatable responses and reduce decision fatigue during high-stress incidents.
*   **Lessons Learned and Post-Incident Review**: The final phase of NIST IR, conducted after the incident is fully resolved. The team documents what happened, what worked, what failed, and what controls should be added or changed to prevent recurrence. Lessons learned reports feed back into the Preparation phase to improve future IR capability. SY0-701 tests this as the correct action after recovery is complete.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Incident response falls under **Domain 4 – Security Operations (28%)** of SY0-701, the highest-weighted domain. IR phase questions are among the most frequently tested scenario types on the exam.
*   **IR Phase Order Trap:** SY0-701 frequently tests whether a student knows the correct sequence. The order is: Preparation → Detection and Analysis → Containment → Eradication → Recovery → Post-Incident Activity. If a question describes an analyst isolating an infected system, that is Containment. If the analyst is reviewing logs to determine if an event is real, that is Detection and Analysis. If the team is patching the exploited vulnerability, that is Eradication.
*   **Containment Before Eradication:** Never eradicate (wipe/rebuild) before containing — doing so destroys forensic evidence. Never recover before eradicating — restoring a system while the threat is still present means it will be reinfected immediately.
*   **SIEM vs. SOAR:** SIEM collects and correlates logs and generates alerts (detection). SOAR (Security Orchestration, Automation, and Response) automates response actions in response to SIEM alerts — such as automatically isolating a host when ransomware is detected. SY0-701 distinguishes between detection tools (SIEM) and response automation tools (SOAR).
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include NIST IR lifecycle diagrams and phase-action mapping tables that directly mirror SY0-701 scenario question formats.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Incident Response" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on the NIST IR lifecycle phases, containment strategies, and the role of SIEM in detection.
*   **Required Video:** Watch the incident response video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos walk through realistic IR scenarios and map each action to the correct NIST phase.

---

### Lab & Command Integration
In this week's hands-on lab, you will analyze simulated SIEM alerts to classify incidents, practice host isolation procedures, review a sample incident timeline, and draft a post-incident lessons-learned summary. Mapping observed activity to the correct IR phase is a direct SY0-701 performance-based question skill.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to assign any described IR action to the correct NIST phase.
- [ ] Read the "Incident Response" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the incident response video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize the NIST IR phase order: Preparation → Detection → Containment → Eradication → Recovery → Post-Incident Activity.
- [ ] Proceed to the weekly hands-on lab activity.
