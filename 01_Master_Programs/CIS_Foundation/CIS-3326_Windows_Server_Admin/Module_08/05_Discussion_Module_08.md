# Discussion Forum: Module 08 — Group Policy Objects (GPOs)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

This week's discussion applies Group Policy concepts to real-world enterprise
design and troubleshooting scenarios. Choose one scenario below, answer all
three sub-questions, and engage substantively with at least two classmates.

---

## Scenario A — GPO Design for a Multi-Department Organization

A medium-sized accounting firm has three departments: Accountants, Auditors, and
IT Administrators. The firm's security policy requires the following:

- All domain computers must display a legal notice before logon.

- Accountants must not be able to access Control Panel or run command-line tools.

- Auditors need read-only access to specific audit shares but no other desktop
  restrictions.

- IT Administrators must have unrestricted access to all tools on their
  workstations.

1. Design a GPO structure — name each GPO, describe where it is linked, and
   explain what settings it contains. Identify how you would prevent the
   domain-level legal notice GPO from being blocked if a junior admin enables
   Block Inheritance on one of the department OUs.

2. The IT department OU currently has Block Inheritance enabled so that domain
   GPOs do not apply to IT workstations. However, the legal notice GPO must still
   apply to IT computers for compliance reasons. Explain the specific GPO link
   setting you would apply to the legal notice GPO, and describe the relationship
   between that setting and Block Inheritance.

3. After deploying the Accountant restrictions GPO, three accountants report
   they can still access Control Panel from their computers. Describe the
   troubleshooting steps you would perform in order, including the specific
   tool or cmdlet you would use at each step, to determine why the policy is
   not applying.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Scenario B — LSDOU Conflict Resolution and Policy Priority

A university domain has the following GPO configuration:

- A domain-linked GPO sets the desktop wallpaper to the university logo.

- A GPO linked to `OU=Faculty` sets the wallpaper to a faculty-specific image.

- A GPO linked to `OU=Faculty\OU=ChemistryDept` sets the wallpaper to a
  chemistry department image.

- Two GPOs are linked to `OU=Faculty\OU=ChemistryDept` in GPMC: Chem-GPO-A
  (link order 1) and Chem-GPO-B (link order 2). Chem-GPO-A sets the wallpaper
  to "blue.jpg" and Chem-GPO-B sets it to "green.jpg."

1. Walk through LSDOU processing for a faculty member in the ChemistryDept OU
   and identify which wallpaper setting is ultimately applied. Explain the
   reasoning at each step of the processing chain.

2. The university wants the domain-level wallpaper (university logo) to always
   apply to Chemistry faculty computers, overriding both the Faculty OU and
   ChemistryDept OU GPOs. What change must be made to the domain-linked GPO
   link, and what effect does this have on any Block Inheritance settings in
   the OU hierarchy?

3. A new professor in Chemistry opens a support ticket reporting that the
   wallpaper they configured manually through personalization settings is being
   overwritten at every logon. Explain what is causing this behavior and under
   which node of the GPO (Computer Configuration or User Configuration) the
   wallpaper setting most likely resides, and why that matters for when the
   setting is applied.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Scenario C — Loopback Processing and Kiosk Computer Design

A hospital network has a fleet of 80 public-access kiosk computers in patient
waiting areas. Any staff member can log on to a kiosk to check schedules or
patient status. When on a kiosk, staff should receive a heavily restricted
desktop — no Control Panel, no command prompt, a specific corporate wallpaper,
and auto-logoff after 10 minutes of inactivity. When the same staff members log
on to their regular desk workstations, they should receive their normal policy.

1. Explain why standard Group Policy behavior (without Loopback Processing)
   cannot satisfy this requirement. Specifically, describe how Group Policy
   normally determines which User Configuration settings a user receives and
   why that creates the problem in the kiosk scenario.

2. Describe how you would configure Loopback Processing to solve the problem.
   Identify whether you would use Merge or Replace mode and justify your choice.
   Describe exactly where the Loopback Processing setting is located in the GPO
   structure and which configuration node (Computer or User) it lives in.

3. After deploying the kiosk GPO with Loopback Processing, a staff member reports
   that the auto-logoff timer is not triggering on the kiosk. You run
   `gpresult /r` on a kiosk computer and the kiosk GPO is listed under
   "Applied GPOs." What additional troubleshooting steps would you take to
   determine why the auto-logoff setting specifically is not working?

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario,
  answer all three sub-questions.

- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates;
  minimum 60 words each.

- In peer replies: evaluate the accuracy of their GPO design or troubleshooting
  approach, and add one consideration or edge case they did not mention.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

## Professor Nash's Note

Group Policy troubleshooting is where juniors and seniors in IT diverge most
sharply. A junior admin runs `gpupdate /force` and declares "the policy is
applied." A senior admin runs `gpresult /h`, finds the specific setting, traces
it to the winning GPO, and verifies the RSoP shows the intended value. Scenario
B is based on a real ticket I worked where a wallpaper setting was inexplicably
reverting — turned out to be a second GPO with link order 1 that nobody
remembered linking. `gpresult /h` found it in 30 seconds. For Scenario C, the
Loopback Processing design pattern is used extensively in healthcare and retail
environments. If you have never seen it before, the key insight is that it
inverts the normal "user's OU drives user policy" assumption.
