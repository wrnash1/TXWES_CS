# Discussion: Module 12 — Digital Forensics

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Discussion Overview

**Forum Title:** Digital Forensics at the Intersection of Technology and Law

**Points:** 50 points total (Initial post: 30 points | Two peer responses: 10 points each)

**Deadline:** Initial post due by Day 4 of the module week; peer responses due by Day 7

---

## Background

Digital forensics exists at the intersection of computer science, law, and ethics. Technical competence alone is not sufficient — a forensic examiner whose work does not withstand legal scrutiny produces findings that may never reach a courtroom. At the same time, the law has struggled to keep pace with technology.

The 2014 US Supreme Court decision in *Riley v. California* (573 U.S. 373) held that police generally cannot search a cell phone without a warrant, even when the phone is seized incident to a lawful arrest. The court noted that a modern smartphone "could just as easily be called a camera, video player, rolodex, calendar, tape recorder, library, diary, album, television, map, or newspaper" and that "the sum of an individual's private life can be reconstructed through a thousand photographs labeled with dates, locations, and descriptions." The unanimous court ruled that the digital data on phones requires the same constitutional protection as data in homes.

More recently, companies facing government data requests have had to balance cooperation with law enforcement against protecting user privacy, often at significant reputational and legal risk.

---

## Initial Post Prompt

Choose ONE of the two scenarios below. Identify your choice at the top of your post.

### Scenario A — The Forensic Examiner as Expert Witness

You are a corporate digital forensics examiner who has been asked to testify as an expert witness in an employment lawsuit. Your employer (a company) claims that a departing executive stole trade secrets by copying files to a personal USB drive before leaving. You conducted the forensic investigation and found:

- Windows Event Logs showing USB drive insertion events during the executive's last week of employment
- Files in the executive's user profile recently accessed from a path matching a removable drive
- A gap in the Security Event Log where EventID 1102 appeared — the log was cleared on the executive's last day

However, your investigation also found that the company's IT team had mounted the drive in read/write mode without a write blocker before your investigation began, and the drive itself is no longer in evidence.

Address all of the following in your post:

1. What specific problems does the IT team's handling of the evidence create for your expert testimony? Reference the forensic principles from this module in your answer.

2. Can you still testify to the findings from the Event Logs? Are those findings affected by the improper handling of the USB drive? Explain your reasoning.

3. How does the cleared Event Log (EventID 1102) serve as evidence even though the underlying Security events were deleted?

4. If you were rebuilding this investigation methodology from scratch — with full company cooperation this time — describe three specific procedures you would require before examining any evidence.

### Scenario B — Forensic Ethics: Scope, Privacy, and Competing Obligations

A forensic investigator at a hospital is investigating a suspected HIPAA data breach by a system administrator. During the investigation, the investigator analyzes the administrator's work computer and discovers:

- Evidence supporting the original HIPAA investigation (files copied to external media)
- Evidence that the administrator was accessing child abuse material (illegal content) on a work computer
- Evidence of a personal relationship between the administrator and the hospital's CISO (who authorized the investigation) that suggests the CISO had a conflict of interest

Address all of the following in your post:

1. The investigator now holds evidence of three potentially separate matters. What is the legally and ethically correct course of action for each of the three discoveries? Consider: who gets notified, when, and by whom?

2. The CISO's conflict of interest raises concerns about whether the investigation itself was properly authorized and conducted in good faith. What specific steps should the investigator take to protect the integrity of all collected evidence, given that the person who authorized the investigation may now be a subject of an investigation?

3. The hospital is a covered entity under HIPAA. The investigator believes the illegal content discovery triggers mandatory reporting obligations. However, doing so before completing the HIPAA investigation may allow the administrator to destroy evidence. How do you balance these competing obligations? Is there a correct sequence of actions?

4. What does this scenario reveal about the importance of investigation scope authorization documents (legal hold letters, investigation authorization forms) in forensic work?

---

## Initial Post Requirements

- Minimum length: 400 words
- Maximum length: 700 words
- Use proper paragraph structure
- Reference at least one assigned reading from the Module 12 Reading Guide
- Engage seriously with the legal and ethical dimensions — these are not purely technical questions

---

## Peer Response Requirements

Respond substantively to two classmates. Each response must:

- Minimum length: 150 words
- Either add a substantive point the original poster did not address, or respectfully challenge a conclusion with supporting reasoning
- Responses that only affirm ("I agree") without adding substance earn zero points

---

## Grading Rubric

### Initial Post (30 points)

| Criterion | Excellent (Full Credit) | Satisfactory (Partial) | Insufficient |
|---|---|---|---|
| Technical forensic analysis (Q1 + Q3 / Q1 + Q3) | Accurately applies forensic principles; demonstrates understanding of evidence integrity (8 pts) | Correct concepts named without deep application (5 pts) | Vague or incorrect (0–2 pts) |
| Legal/procedural analysis (Q2 / Q2) | Correctly distinguishes what can and cannot be used; applies legal reasoning (7 pts) | Correct conclusion without reasoning (4 pts) | Avoids the question (0–2 pts) |
| Ethical analysis (Q4 / Q3 + Q4) | Identifies competing obligations; proposes a principled course of action (8 pts) | States what should happen without justification (4 pts) | Missing (0–2 pts) |
| Process improvement (Q4 / Q4) | Specific, actionable improvements grounded in forensic best practice (7 pts) | General improvements without specifics (4 pts) | Missing (0–2 pts) |

### Peer Responses (10 points each)

| Criterion | Full Credit | Partial | Minimal |
|---|---|---|---|
| Substantive extension or challenge | New point or reasoned challenge (7 pts) | Minor addition or restatement (4 pts) | Compliment only (0 pts) |
| Length and professionalism | 150+ words, respectful (3 pts) | Under 150 words or informal (1 pt) | Under 75 words (0 pts) |

---

## Instructor Notes

Scenario A is technically focused and works well for students with stronger IT backgrounds — the chain of custody failure is clear and the Event ID analysis is concrete. Scenario B is more ethically complex and generates richer discussion. The child abuse material discovery in Scenario B always raises mandatory reporting questions — instructors should note that requirements vary by jurisdiction and professional role (IT professionals, unlike doctors, are not universally mandated reporters in all states, though the federal PROTECT Our Children Act covers certain online service providers). The CISO conflict angle is deliberately challenging because it requires students to think about who authorizes investigations and what happens when the authorizer is compromised.

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 12*
