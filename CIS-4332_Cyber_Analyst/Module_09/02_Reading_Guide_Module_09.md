# Reading Guide: Module 09 - Incident Response – Containment and Recovery
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 09 - Incident Response – Containment and Recovery**! This module covers the third phase of the NIST incident response lifecycle: the actions analysts and responders take after a confirmed incident to stop the attack from spreading, eliminate the threat from affected systems, and restore operations to a verified-clean state. You will learn containment strategies, eradication techniques, and recovery validation procedures. These topics are tested under **Domain 3: Incident Response and Management (20%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn the distinction between short-term and long-term containment, eradication steps, and the criteria for declaring recovery complete. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Containment (Short-Term vs. Long-Term)**: Short-term containment stops the immediate bleeding — isolating a compromised host via EDR network isolation, blocking a malicious IP at the firewall, or disabling a compromised account — to halt active attacker access without disturbing evidence. Long-term containment involves more durable measures such as rebuilding the affected system or deploying hardened configurations while the organization continues operating. CySA+ questions frequently ask which containment type is appropriate given specific time and business continuity constraints.
*   **Eradication**: The process of completely removing the threat from the environment after containment — deleting malware files, removing attacker-created accounts, revoking compromised credentials, patching the exploited vulnerability, and verifying no persistence mechanisms remain. Eradication must be completed before recovery begins; recovering a system that still contains malware reintroduces the threat.
*   **Recovery and Validation**: Recovery restores affected systems to normal operations from a known-good state — reimaging from a clean baseline, restoring from a pre-infection backup, or rebuilding from scratch. Validation confirms the system is clean before it is returned to production: rescanning with EDR and AV tools, verifying no suspicious network connections, and confirming the patched vulnerability is no longer exploitable.

---

### 2. Certification Exam Tips
*   **Focus Area – Containment Order (Domain 3):** CySA+ CS0-003 scenario questions test the correct sequence: Contain first (stop the spread), then Eradicate (remove the threat), then Recover (restore operations). Skipping containment to begin recovery immediately is a common exam trap — systems restored before containment will be reinfected.
*   **Scenario Trap – Isolation vs. Shutdown:** Network isolation (EDR quarantine) is correct for containment — it preserves volatile memory evidence while stopping attacker access. Shutting down the system destroys volatile memory. CySA+ consistently tests this distinction in containment scenarios.
*   **Eradication Completeness:** CySA+ questions ask what must be completed before recovery can begin. The answer always includes: removing all malware artifacts, closing the initial attack vector (patching the exploited vulnerability), and verifying no attacker persistence mechanisms remain. Recovering without addressing the root cause leads to reinfection.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers containment strategies, eradication checklists, and recovery validation procedures mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes scenario walkthroughs of the full IR lifecycle.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Incident Response – Containment, Eradication, and Recovery** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details containment strategies, eradication steps, and recovery validation techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Incident Response – Containment and Recovery** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of EDR isolation workflows and post-recovery validation procedures.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Execute EDR network isolation on a simulated compromised host**: Using a lab EDR console or simulated tool, apply network isolation to a target VM, verify the host loses network connectivity while remaining powered on, and document the isolation timestamp and method in the incident ticket.
*   **Perform eradication steps on the isolated host**: Identify and remove the simulated malware artifact (a planted executable in `%TEMP%`), delete the attacker-created scheduled task or registry run key used for persistence, and reset the compromised local account credentials — then verify each step with a follow-up scan.
*   **Validate recovery and confirm the attack vector is closed**: Restore the host from a clean snapshot or baseline image, verify the EDR agent reports no active threats, confirm the patched vulnerability (simulated unpatched service) is no longer exploitable with a targeted nmap service version scan, and document the recovery validation results.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Incident Response – Containment, Eradication, and Recovery** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Incident Response – Containment and Recovery** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the containment, eradication, and recovery steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
