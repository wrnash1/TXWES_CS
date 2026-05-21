# Quiz: Module 16 - Final Exam Preparation & CompTIA CySA+ CS0-003 Certification
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
A SOC analyst receives a SIEM alert indicating a workstation in the finance department is sending repeated DNS queries to a newly registered domain with a high-entropy name. Threat intelligence confirms the domain is associated with a known ransomware C2 infrastructure. No other hosts show similar activity. Which action should the analyst take first?

*   A) Shut down the workstation immediately to prevent the ransomware payload from executing and spreading to network shares
*   B) Isolate the workstation from the network using EDR host isolation, preserving the system's volatile memory for forensic analysis, and escalate to Tier 2 for incident response
*   C) Update the SIEM correlation rule to alert on all DNS queries to domains registered within the past 30 days and monitor for additional affected hosts before taking any containment action
*   D) Notify the finance department manager that their employee's workstation may be compromised and ask the employee to stop using the system until IT can investigate next business day
*   **Correct Answer:** B) Isolate the workstation from the network using EDR host isolation, preserving the system's volatile memory for forensic analysis, and escalate to Tier 2 for incident response.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Shutting down a compromised system destroys volatile memory (RAM), which contains active process data, network connections, encryption keys, and attacker artifacts that are unrecoverable after power-off. EDR isolation achieves containment without destroying forensic evidence. Host shutdown is specifically the wrong action in CySA+ incident response scenarios.
    *   *Why B is correct:* EDR network isolation severs the workstation's C2 communication channel while keeping the system powered on and forensically intact. This satisfies the containment objective (Domain 3, Containment phase) while preserving volatile evidence for analysis. Escalation to Tier 2 initiates the formal incident response process. This answer correctly integrates Domain 1 (EDR capability), Domain 3 (containment action), and forensic evidence preservation.
    *   *Why C is incorrect:* Updating detection rules is a valuable post-incident improvement action, but it does not address the active C2-connected host that requires immediate containment. Delaying containment to observe additional hosts allows the ransomware to establish persistence, exfiltrate data, or spread laterally.
    *   *Why D is incorrect:* Delegating containment to a non-security employee and deferring action until the next business day is not an appropriate incident response action. A confirmed C2 connection from a workstation requires immediate analyst-controlled containment, not informal user notification.

---

**Question 2**
In the context of the CompTIA CySA+ CS0-003 exam, which of the following most accurately describes the difference between a **true negative** and a **false negative** in SIEM alert classification?

*   A) A true negative occurs when the SIEM generates an alert for a real attack that is later confirmed by the analyst; a false negative occurs when the SIEM generates an alert for benign activity that the analyst incorrectly escalates as a real threat
*   B) A true negative occurs when the SIEM does not alert on benign activity — correctly identifying that no threat is present; a false negative occurs when the SIEM fails to alert on real malicious activity — missing a genuine threat entirely
*   C) A true negative and a false negative are both categories of incorrect SIEM classification; a true negative means the analyst closed the alert too quickly, while a false negative means the analyst escalated too slowly
*   D) A true negative occurs when an IDS rule fires on traffic that matches a known attack signature; a false negative occurs when the same rule fires on traffic that does not match the attack signature due to a misconfigured threshold
*   **Correct Answer:** B) A true negative occurs when the SIEM does not alert on benign activity — correctly identifying that no threat is present; a false negative occurs when the SIEM fails to alert on real malicious activity — missing a genuine threat entirely.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Option A describes a true positive (alert on real attack confirmed) and a false positive (alert on benign activity) — not true negative or false negative. Confusing these four classifications is one of the most common CySA+ exam traps. True/false negatives involve the absence of an alert, not the presence of one.
    *   *Why B is correct:* True negative = no alert, no threat (correct). False negative = no alert, real threat present (incorrect — the worst outcome). False negatives represent detection gaps where actual attacks go undetected. CySA+ tests all four classifications because each has a different operational consequence: false positives waste analyst time; false negatives allow adversaries to operate undetected and are operationally the most dangerous classification.
    *   *Why C is incorrect:* True and false negatives are not both categories of incorrect classification — a true negative is a correct classification (system correctly identified no threat). Only false negatives (and false positives) represent classification errors. Analyst response speed is not part of the true/false positive/negative classification framework.
    *   *Why D is incorrect:* An IDS rule firing on matching traffic describes a true positive; the same rule firing incorrectly describes a false positive. Neither involves the absence of an alert, which is what defines a negative (true or false) classification.

---

**Question 3**
An analyst is reviewing CVSS scores during a vulnerability management prioritization meeting. A web application vulnerability has a CVSS base score of 7.5 (High). However, the affected system is an internal developer sandbox that is not connected to the internet, contains no production data, and has a compensating control — network segmentation — that prevents lateral movement to production systems. How should the analyst correctly interpret this finding for prioritization purposes?

*   A) The CVSS base score of 7.5 is authoritative — all High-severity vulnerabilities must be patched within the organization's standard 30-day SLA for High findings regardless of system context
*   B) The CVSS base score measures technical severity in isolation; the analyst should apply environmental and contextual factors (non-internet-facing, no production data, compensating network segmentation) to produce a lower organizational risk rating, which justifies deprioritizing this finding relative to High-severity vulnerabilities on production systems
*   C) Because a compensating control (network segmentation) is in place, the vulnerability is fully remediated and can be closed in the vulnerability tracker without further action or documentation
*   D) The analyst should escalate this finding to Critical severity because developer sandboxes are frequently targeted by insider threats and the CVSS base score underestimates the actual organizational risk
*   **Correct Answer:** B) The CVSS base score measures technical severity in isolation; the analyst should apply environmental and contextual factors to produce a lower organizational risk rating, which justifies deprioritizing this finding relative to High-severity vulnerabilities on production systems.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CVSS base scores do not automatically determine remediation SLAs in all contexts. Organizations apply environmental and temporal metrics to adjust CVSS scores based on actual deployment context. A High-severity finding on an isolated, non-production system with compensating controls presents lower actual organizational risk than the same finding on an internet-facing production server.
    *   *Why B is correct:* This is one of the highest-yield CySA+ exam concepts: CVSS base score ≠ organizational risk rating. CVSS measures the technical severity of a vulnerability as if it existed on a generic internet-facing system. Environmental metrics (Modified Attack Vector, Modified Scope, existing compensating controls) allow analysts to adjust the score to reflect actual deployment context. Applying these adjustments is the correct analyst action — not blindly applying SLAs based on base scores alone.
    *   *Why C is incorrect:* A compensating control reduces risk but does not remediate the vulnerability. The vulnerability still exists and must remain open in the tracker with documented compensating control status and a planned remediation date. Closing a known vulnerability because a compensating control is in place is a compliance and audit finding.
    *   *Why D is incorrect:* There is no technical basis for escalating this finding to Critical based on insider threat speculation. CVSS environmental adjustments must be based on documented system characteristics (internet exposure, data classification, compensating controls) — not hypothetical threat scenarios that are not supported by the system context provided.

---

**Question 4**
During a post-incident review following a ransomware event, the lessons-learned team identifies that the attacker gained initial access through a phishing email, established persistence using a scheduled task created at 2:47 AM, moved laterally using valid domain credentials, and began encrypting files 72 hours after initial access. The SIEM generated no alerts during this period. Which two specific improvements most directly address the detection gaps revealed by this incident?

*   A) Require all employees to complete annual phishing awareness training and add a phishing simulation to the quarterly security testing schedule
*   B) Create a SIEM correlation rule alerting on scheduled task creation events (Windows Event ID 4698) outside business hours with non-standard task names, and enable MFA on all domain accounts to prevent credential reuse from enabling lateral movement
*   C) Deploy full-disk encryption on all endpoints to prevent ransomware from accessing file contents, and implement an email gateway with attachment sandboxing to block malicious payloads before delivery
*   D) Increase SIEM log retention from 90 days to 365 days to enable longer historical lookback for future ransomware investigations, and deploy a network access control (NAC) solution to enforce device compliance before allowing domain logon
*   **Correct Answer:** B) Create a SIEM correlation rule alerting on scheduled task creation outside business hours, and enable MFA on all domain accounts to prevent credential reuse from enabling lateral movement.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Phishing awareness training and simulations are valuable preventive controls that address the initial access vector — but they do not address the two specific detection gaps revealed: (1) no alert fired on the after-hours scheduled task persistence, and (2) no control prevented lateral movement via valid credentials. Training does not detect adversary activity already inside the environment.
    *   *Why B is correct:* The lessons-learned analysis identified two specific gaps: persistence via scheduled task went undetected (no SIEM rule for Event ID 4698 with after-hours filter), and lateral movement succeeded because valid credentials required no additional verification. Creating the SIEM rule directly closes the detection gap for the persistence technique (ATT&CK T1053.005). Enabling MFA directly addresses the lateral movement enabler — stolen credentials alone become insufficient for domain authentication. Both improvements are specific, measurable, and directly tied to the incident's attack chain.
    *   *Why C is incorrect:* Full-disk encryption prevents unauthorized access to data at rest on powered-off systems — it does not prevent ransomware from encrypting files on a running, authenticated system. Email gateway sandboxing is a preventive control for the initial delivery vector, but it does not address the persistence and lateral movement detection gaps that allowed the attacker to operate for 72 hours undetected.
    *   *Why D is incorrect:* Extended log retention improves retrospective forensic capability after a future incident but does not improve real-time detection — it would not have triggered an alert during the 72-hour dwell period. NAC enforces device compliance posture at logon but does not prevent lateral movement by a threat actor using valid domain credentials on a compliant device.

---

**Question 5**
An organization is preparing for its first CompTIA CySA+ certification exam sitting for its analyst team. The security manager asks which study approach best prepares analysts for the scenario-heavy CS0-003 exam format. Which recommendation is most aligned with the CySA+ CS0-003 exam design and the skills it measures?

*   A) Focus exclusively on memorizing port numbers, protocol acronyms, and command syntax — the exam primarily tests recall of technical specifications and configuration parameters
*   B) Practice applying analyst decision-making to realistic scenario descriptions — identifying the correct NIST IR phase, selecting the appropriate action for the stated objective, and eliminating distractors by recognizing which answers describe the right concept at the wrong phase or the wrong audience
*   C) Prioritize Domain 4 (Reporting and Communication) study time because it has the highest point value on the exam and covers executive communication skills that differentiate senior analysts
*   D) Complete as many practice exams as possible from third-party test banks without reviewing incorrect answers — volume of questions attempted is the strongest predictor of exam success
*   **Correct Answer:** B) Practice applying analyst decision-making to realistic scenario descriptions — identifying the correct NIST IR phase, selecting the appropriate action, and eliminating distractors by recognizing which answers describe the right concept at the wrong phase or the wrong audience.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CySA+ CS0-003 is not a memorization exam. CompTIA explicitly designs CySA+ to test applied analytical thinking — most questions present a scenario and ask what an analyst should do, not what a port number is. Analysts who memorize facts without understanding how to apply them in context will struggle with the scenario-based question format.
    *   *Why B is correct:* The CySA+ CS0-003 exam is scenario-driven by design. The most effective preparation strategy mirrors the exam format: reading a scenario, identifying which domain and phase it tests, applying the correct analyst decision framework, and eliminating distractors by recognizing common traps (right action/wrong phase, correct technical term/wrong audience, preventive control when a detective control is asked for). This approach builds the applied reasoning skill the exam measures.
    *   *Why C is incorrect:* Domain 4 (Reporting and Communication) is 17% of the exam — the smallest domain. Domain 1 (Security Operations) is 33% and Domain 2 (Vulnerability Management) is 30%. Study time should be allocated proportional to domain weight, with the largest domains receiving the most preparation. Prioritizing the smallest domain is an inefficient use of exam preparation time.
    *   *Why D is incorrect:* Completing practice questions without reviewing incorrect answers is the least effective exam preparation method. Understanding why a wrong answer is wrong — and which concept it was testing — is where exam learning occurs. Volume without analysis builds pattern-matching habits rather than the conceptual understanding needed to answer novel scenario variations on the actual exam.
