# Discussion: Module 03 - OSINT and Passive Reconnaissance

**Course:** CIS-4333 Penetration Testing
**Certification Target:** CompTIA PenTest+ PT0-002
**Professor:** Nash

---

## Instructions

Post your initial response to one of the three scenarios below by Wednesday at 11:59 PM. Then reply to at least two classmates by Sunday at 11:59 PM. Your initial post should be 175 to 225 words. Each peer reply should be at least 75 words and contribute new analysis, a counterpoint, or a real-world connection.

Professor Nash will participate mid-week with follow-up questions. Be prepared to defend your analysis with specific references to OSINT techniques and tools covered in Module 03.

---

## Scenario A — The Oversharing Organization

During passive reconnaissance for an authorized engagement, a penetration tester performs Google dorking against the target organization and discovers: an indexed internal network diagram in PDF format, a job posting describing the exact firewall model and version in use, and a LinkedIn profile of the IT Director listing every technology platform the organization runs. None of these sources required any interaction with the target's systems.

Discuss: What does this scenario reveal about the organization's information security posture beyond technical vulnerabilities? How does each of these three OSINT findings affect the active testing strategy? What recommendations would you include in the final report about information hygiene, and how would you classify these findings in terms of severity?

---

## Scenario B — The GitHub Secret

A penetration tester performing OSINT for an authorized client discovers a public GitHub repository belonging to a current employee of the target organization. The repository contains a `.env` file committed eight months ago with what appear to be live database credentials, an internal API endpoint, and an AWS region designation. The repository has 12 stars, meaning others have likely seen it.

Discuss: What is the correct immediate action upon discovering this repository? How does the public visibility of the repository affect the severity classification of this finding? Does this discovery change the testing plan for the active phases? How does the tester handle the fact that other external parties may have already seen these credentials?

---

## Scenario C — The Shodan Discovery

A tester queries Shodan during passive reconnaissance for an authorized engagement. The search reveals that the target organization has 14 internet-facing devices. Three of them are running remote desktop services (RDP) directly exposed on port 3389 with software versions consistent with known unpatched vulnerabilities. Two others appear to be industrial control system (ICS) web interfaces. The target organization is a regional utility company.

Discuss: How does this passive discovery change the risk profile of the engagement? If the ICS systems are not listed in the authorized scope of the RoE, what steps must occur before they can be tested? Why are internet-exposed RDP services with unpatched software a particularly high-severity finding even before active testing begins? What immediate communication should the tester send to the client?

---

## Grading Rubric (10 Points)

| Component | Points | Criteria |
|---|---|---|
| Initial Post — Content | 4 | Directly addresses the scenario; applies correct OSINT concepts and tools accurately |
| Initial Post — Depth | 2 | Goes beyond surface-level description; includes specific technical analysis or professional consequence |
| Word Count | 0 or -1 | Posts under 175 words or over 225 words receive a one-point deduction |
| Peer Reply 1 | 2 | At least 75 words; adds new analysis, a counterpoint, or a real-world connection |
| Peer Reply 2 | 2 | At least 75 words; same standard as Peer Reply 1 |
| **Total** | **10** | |
