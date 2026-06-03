# Video Script: Module 16 — CySA+ CS0-003 Exam Preparation and Capstone

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Slide 1 — Welcome to the Final Module

Welcome to Module 16. I am Professor Nash, and this is our final session together in CIS-4332 Cyber Security Analysis.

Congratulations on reaching the end of this course. You have covered 15 modules of material spanning threat intelligence, vulnerability management, network security monitoring, log analysis, incident response, digital forensics, compliance, automation, and threat hunting. That is the full professional toolkit of a working security analyst.

This final module has one purpose: to make sure you are ready to pass the CompTIA CySA+ CS0-003 exam. We will review every domain, walk through exam strategy, and close with 20 practice questions.

---

## Slide 2 — CySA+ CS0-003 Exam Overview

The CompTIA CySA+ CS0-003 exam consists of a maximum of 85 questions, with a 165-minute time limit. The passing score is 750 on a 900-point scale. Questions are a mix of multiple-choice (single answer), multiple-select (multiple correct answers), and performance-based questions (drag-and-drop, simulations).

The exam covers four domains:

- Domain 1: Security Operations — 33%
- Domain 2: Vulnerability Management — 30%
- Domain 3: Incident Response and Digital Forensics — 20%
- Domain 4: Reporting and Communication — 17%

Notice that Domain 1 carries the highest weight. Security Operations covers your daily analyst work — SIEM, threat intelligence, log analysis, automation, and threat hunting. Invest the most review time here.

---

## Slide 3 — Domain 1: Security Operations Review

Security Operations covers the tools, techniques, and workflows that analysts use every day.

System and network architecture — you must understand network topologies, cloud architectures, and how they affect analyst visibility.

Log analysis and monitoring — you must understand log types, SIEM correlation, and how to extract indicators from log data. Know syslog, Windows event logs, firewall logs, and DNS logs.

Threat intelligence — you must understand intelligence types (strategic, operational, tactical, technical), sharing standards (STIX/TAXII), and how to apply intelligence to detection.

Tools — know the purpose of SIEM, EDR, XDR, SOAR, IDS/IPS, vulnerability scanners, and threat intelligence platforms.

Threat hunting — know the hunting loop, hypothesis structure, and ATT&CK as a hunting framework.

---

## Slide 4 — Domain 2: Vulnerability Management Review

Vulnerability Management covers the full lifecycle of identifying, prioritizing, remediating, and verifying security weaknesses.

Scanning — understand agent-based versus agentless scanning, credentialed versus non-credentialed scans, and the difference between vulnerability assessment and penetration testing.

Prioritization — know CVSS scoring (base, temporal, environmental), EPSS (Exploit Prediction Scoring System), and how business context modifies technical severity.

Remediation — know patching workflows, configuration hardening, compensating controls, and remediation SLAs.

Reporting — understand how to produce vulnerability reports for technical and executive audiences.

Special environments — cloud vulnerability management, OT/ICS environments, and IoT devices have unique challenges. Know the key differences.

---

## Slide 5 — Domain 3: Incident Response and Digital Forensics Review

This domain tests your knowledge of structured IR processes and forensic investigation techniques.

NIST SP 800-61 phases — know all four phases: Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity. Know what analysts do in each phase.

Triage and scoping — know the NIST severity framework (functional impact, information impact, recoverability) and how scoping differs from triage.

Digital forensics — know the order of volatility, chain of custody requirements, Volatility plugins for memory forensics, key Windows disk artifacts, and Wireshark for network forensics.

Documentation — know what an incident record must contain and what constitutes proper chain of custody.

Anti-forensics — know timestomping, log clearing, and living-off-the-land as anti-forensic techniques.

---

## Slide 6 — Domain 4: Reporting and Communication Review

This is the domain students most often under-study. It carries 17% of the exam weight and rewards practical communication skills.

Vulnerability reports — know the difference between executive summary and technical findings sections. Know how to communicate risk without overstating severity.

Incident reports — know what a formal incident report contains: timeline, scope, impact, root cause, lessons learned, remediation actions.

Metrics and KPIs — know MTTD, MTTR, MTTC, mean time between incidents, and vulnerability SLA compliance metrics.

Stakeholder communication — know how to tailor technical content for executive audiences versus technical teams.

Compliance reporting — know how compliance dashboards, audit evidence packages, and gap reports serve different audiences.

---

## Slide 7 — Exam Strategy: Reading Questions

The CySA+ exam is scenario-based. Questions describe a situation and ask what to do. This tests applied knowledge, not memorization.

When reading a question, identify these elements before looking at the answers:

What is the context? (Industry, environment, incident type)

What is the constraint? (Limited budget, production environment, specific tool available)

What is being asked? (What should the analyst do NEXT? What is the BEST action? What MOST LIKELY explains?)

Words like "first," "next," "most appropriate," and "best" often distinguish the correct answer from a plausible but incorrect one.

---

## Slide 8 — Exam Strategy: Eliminating Distractors

CompTIA writes four answers: one correct, one plausible-but-wrong, one partially right, and one obviously wrong.

Eliminate the obviously wrong answer first — this is usually an action that causes harm, involves an unrealistic step, or describes the wrong domain entirely.

Eliminate the partially right answer — this is the answer that is correct in a different context or correct for a different question. Read the question carefully to identify what specifically is wrong about it.

Between the remaining two, apply the principle of the question. "Most appropriate" usually means the answer that follows the correct process order (for example, triage before containment, containment before eradication). "Best first step" almost always means the most conservative or evidence-preserving action.

---

## Slide 9 — Exam Strategy: Performance-Based Questions

Performance-based questions (PBQs) appear at the beginning of the exam. They involve drag-and-drop, simulations, or fill-in-the-blank with a technical scenario.

PBQ tips:

Do not spend more than 3–4 minutes on a single PBQ. If you are stuck, mark it for review and come back.

Read the entire scenario before making selections. PBQs often contain the answer context within the scenario description itself.

In drag-and-drop questions, start with the items you are most confident about. Correct placements often make the remaining items obvious.

Performance-based questions are worth more points than multiple-choice questions. Invest proportional time.

---

## Slide 10 — Exam Strategy: Time Management

165 minutes for up to 85 questions gives you approximately 2 minutes per question. This is more generous than most exams, but PBQs consume more time.

Recommended pacing:

- First pass: answer all questions you are confident about in under 90 seconds each
- Flag uncertain questions for review — do not agonize on the first pass
- Second pass: return to flagged questions with remaining time
- Final 10 minutes: verify all questions are answered, no blanks

Never leave a question blank. There is no penalty for guessing. If you must guess, eliminate what you can and pick from the remainder.

---

## Slide 11 — High-Yield Study Topics

Based on the current CS0-003 exam objectives and question patterns, these are the highest-yield topics per domain.

Domain 1 high yield: SIEM use cases, log analysis scenarios, threat intelligence application, SOAR playbook logic, ATT&CK-based hunting.

Domain 2 high yield: CVSS scoring, scan type selection (credentialed vs. non-credentialed), vulnerability prioritization frameworks, remediation tracking.

Domain 3 high yield: NIST 800-61 phases, order of volatility, chain of custody, key Windows forensic artifacts, Wireshark analysis scenarios.

Domain 4 high yield: metric definitions (MTTD, MTTR), incident report components, communicating risk to executives, vulnerability report structure.

---

## Slide 12 — Common Exam Mistakes

These are the most common mistakes CySA+ candidates make:

Confusing SIEM and SOAR — SIEM detects; SOAR acts. Know the distinction precisely.

Mixing up NIST 800-61 phase order — Post-Incident Activity is after recovery, not during it.

Selecting "penetration test" when "vulnerability scan" is the correct answer — know the difference in scope, authorization, and output.

Forgetting that chain of custody gaps can invalidate evidence — if a transfer is undocumented, custody is broken.

Misidentifying control types — read the control description carefully before classifying as technical, administrative, or physical.

---

## Slide 13 — Final Exam Registration and Logistics

The CySA+ CS0-003 exam is administered by Pearson VUE at testing centers and via online proctoring.

To register: go to comptia.org, purchase a voucher, then schedule through Pearson VUE.

Exam vouchers can often be found at discounted rates through CompTIA's academic partner program, corporate training programs, or periodic sales.

Testing center: arrive 30 minutes early. Bring two forms of ID. No personal items in the testing room.

Online proctored: test from a private location with a clear desk and no interruptions. Run the system compatibility check before your exam date.

---

## Slide 14 — What to Do the Day Before

The day before your exam:

Review your notes for the four domains in order. Do one pass through each high-yield topic.

Do not cram new material. Attempting to learn new topics the day before is counterproductive.

Review 10–15 practice questions to stay sharp, not to learn new content.

Sleep well. Sleep deprivation measurably impairs recall and reasoning.

Know where you are going and how you will get there (for in-person exams).

---

## Slide 15 — Summary and Closing

You have completed CIS-4332 Cyber Security Analysis. In 16 modules you have built the foundational skills of a professional security analyst:

Detection, correlation, and SIEM operations. Vulnerability management from scanning to remediation. Threat intelligence collection, analysis, and application. Network security monitoring and anomaly detection. Incident response from triage through lessons learned. Digital forensics across memory, disk, and network. Compliance validation and audit evidence collection. Security automation with Python and SOAR. Advanced threat hunting with MITRE ATT&CK.

The CySA+ CS0-003 certification demonstrates that you have mastered this skill set to an industry-recognized standard. Take the exam. Pass it. Then get to work.

---

## Slide 16 — Go Build Something

Security operations is one of the most important disciplines in the modern economy. Every organization needs analysts who can detect threats, investigate incidents, hunt for hidden adversaries, and communicate risk clearly to those who make decisions.

That is the career you have prepared for. Go build it.

Good luck on the exam, and thank you for the semester.

---

End of Module 16 Video Script — 230 lines
