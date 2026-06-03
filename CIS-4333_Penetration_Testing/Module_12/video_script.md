# Video Script: Module 12 — Physical Security Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Segments:** 6
- **Visual Aids:** Access control system diagrams, physical security layers diagram, RFID reader photos
- **Lab Environment:** Concept-only — no physical trespass. Lab uses documented methodology and case analysis.

---

## Segment 1: Physical Security in the Pen Test Framework (Lines 1–35)

[SLIDE: Module 12 Title Card]

Welcome to Module 12. This module covers a dimension of penetration testing that sometimes surprises students: physical security assessment.

Physical security testing evaluates whether an organization's physical access controls — locks, badges, guards, surveillance — can be bypassed by an adversary. Many organizations invest heavily in network security while underinvesting in the physical controls that protect the very hardware running those networks.

[SLIDE: Why Physical Access Is the Ultimate Escalation]

Consider this: every network security control you have studied — firewalls, IDS, encryption, authentication — is irrelevant once an attacker is physically in front of an unattended workstation. USB keyloggers, cold boot attacks, direct disk access, and physical credential theft all require only a moment of unobserved physical access.

Physical security testing is authorized assessment of whether those physical controls hold.

[SLIDE: Authorization Requirements Are Critical]

Physical security testing without explicit written authorization is criminal trespass at minimum. It may also constitute breaking and entering, theft, vandalism, or fraud depending on the specific techniques used.

The authorization requirements for physical testing are more demanding than for network testing because:

The test involves physical presence in the client's property.

Third parties (guards, employees) will interact with the tester, creating real human consequences.

The "get out of jail" letter — a letter on client letterhead confirming the tester's authorization — must be carried at all times. This is a physical document, not just a contract clause. If challenged by security or law enforcement, this letter is the tester's protection.

[PAUSE for transition]

---

## Segment 2: Physical Security Assessment Methodology (Lines 36–75)

[SLIDE: Physical Security Layers]

Professional physical security assessments evaluate security through the concept of concentric rings of protection:

The outermost ring is perimeter security — fencing, gates, vehicle barriers, lighting, and surveillance cameras protecting the property boundary.

The second ring is facility access — the building envelope, including doors, windows, loading docks, utility entrances, and the access controls (locks, badge readers) protecting them.

The third ring is interior security — access controls within the building: secured server rooms, executive areas, HR and finance spaces, and data center cages.

The innermost ring is asset security — physical protection of specific assets: laptop locks, cable locks on servers, locked cabinets for removable media.

[SLIDE: Pre-Assessment Reconnaissance]

Before any physical assessment, reconnaissance establishes what the tester is walking into.

Open-source reconnaissance includes:

- Google Maps and satellite imagery to study facility layout, entrances, parking, and external features
- Google Street View to study entrance configurations, guard positions, and visible security measures
- LinkedIn to identify physical security personnel, reception staff, and likely badge designs
- Company website for visitor information, office photos, and organizational structure
- Public records for building permits, floor plans filed with local authorities, and tenant information

Social media reconnaissance: Employees frequently post photos inside facilities, inadvertently revealing badge designs, access control system models, and internal layouts.

[SLIDE: The Pre-Text for Physical Tests]

Physical tests almost always involve a pretext — a cover story that explains the tester's presence. Common pretexts include:

Vendor/contractor: Arriving as an IT vendor, elevator technician, copier repair person, or delivery driver.

New employee: Claiming to be a recently hired employee who has not yet received their badge.

Executive visitor: Claiming to be meeting with a senior executive.

Survey/audit team: Claiming to conduct a safety audit, fire inspection, or facilities assessment.

The pretext determines what the tester wears, what they carry, how they speak, and what their objective is. Preparation for objections is critical.

[PAUSE for transition]

---

## Segment 3: Badge Cloning and Access Control Attacks (Lines 76–115)

[SLIDE: RFID Access Control Fundamentals]

Most modern access control systems use RFID (Radio Frequency Identification) cards or fobs. Low-frequency 125 kHz systems (HID Prox, EM4100) are widely deployed and are unfortunately trivially vulnerable to cloning.

High-frequency 13.56 MHz systems (HID iCLASS, MIFARE) offer better security but are also vulnerable to various attacks depending on configuration.

[SLIDE: The Proxmark Attack]

The Proxmark is the standard tool for authorized RFID assessment. It can read, analyze, emulate, and write RFID cards.

The attack model: An attacker with a concealed RFID reader can sniff a card within a few inches, depending on antenna strength. Low-frequency HID Prox cards transmit their ID without authentication. The attacker reads the card ID, writes it to a blank T5577 card, and has a functional clone.

Proxmark commands (for authorized lab use):

```
pm3 --> lf hid read         # Read a 125kHz HID card
pm3 --> lf hid clone --r [card_data]  # Write to blank card
```

[SLIDE: Defensible RFID Countermeasures]

As a security tester, your role includes recommending countermeasures:

Upgrade to high-security systems: iCLASS SE, SEOS, or smart card systems using mutual authentication.

Enable anti-passback: Prevents using the same credential to enter multiple times without exiting.

Deploy access control monitoring: Alert on unusual patterns (same card used at multiple readers within seconds — a cloning indicator).

Physical card shielding: Faraday wallets block unauthorized RFID reading of cards being carried.

Multi-factor access control: Combine card with PIN for sensitive areas.

[SLIDE: Lock Picking Concepts]

Lock picking is a legitimate skill within authorized physical security testing. It is important to understand the concepts even if hands-on practice requires a specific locksmith or specialized training context.

Pin tumbler locks work by aligning spring-loaded driver pins at the shear line when the correct key lifts them to the right height. Lock picking exploits manufacturing tolerances: pins bind sequentially under light rotational tension, allowing the picker to set each pin individually.

The two tools are the tension wrench (applies rotational torque) and the pick (manipulates individual pins).

Bump keys are specially cut keys that, when struck while applying tension, can cause all pins to briefly jump to the shear line simultaneously.

[SLIDE: Beyond Locks — Other Physical Entry Vectors]

Physical assessments reveal entry vectors that are often overlooked:

Under-door tools: A gap at the bottom of a door may allow reaching through to depress a push-bar handle from the outside.

Loiding: Using a thin flexible tool (traditionally a credit card or "loid") to retract a spring latch.

Door hinge attacks: Hinge bolts on external hinges can be removed to pivot the door from the hinge side.

Loading dock access: Loading docks often have minimal badge control, receiving visitors during business hours without verification.

Tailgating: Following an authorized person through a secured door. The most common and simplest physical bypass.

[PAUSE for transition]

---

## Segment 4: Tailgating, Dumpster Diving, and Environmental Attacks (Lines 116–150)

[SLIDE: Tailgating Assessment]

Tailgating (also called piggybacking) exploits social norms — specifically, the discomfort employees feel challenging strangers. In most workplace cultures, holding a door for the person behind you is polite. Security training must override this instinct.

In an authorized assessment, the tester approaches a controlled access door at natural times: as employees enter after a scheduled break, during busy morning arrival periods, or while carrying items that make it difficult to badge.

Testing variables include:

- How often employees challenge unfamiliar individuals before opening the door
- Whether any employees report the tailgating attempt afterward
- Whether security cameras are positioned to detect tailgating
- Whether anti-tailgating systems (mantrap, security vestibule) are installed

[SLIDE: Mantrap and Security Vestibule Testing]

A mantrap is a controlled airlock-style entry with two doors, where only one can be open at a time. If tailgating is attempted, the inner door will not open. This is a high-assurance physical control.

Testing focuses on whether the mantrap is properly configured: Does it enforce one-person-at-a-time entry? Are the cameras properly positioned? Can the inner door be forced while the outer door is closing?

[SLIDE: Dumpster Diving Assessment]

Dumpster diving — examining an organization's discarded materials — is a legitimate assessment technique. Poorly controlled document disposal creates significant risk: printed reports, employee directories, network diagrams, building access procedures, and even credentials can be found in uncontrolled trash.

Legal note: Dumpster diving is generally legal for materials placed in public trash collection. However, searching trash within the facility perimeter (inside a fence line, inside a building) requires specific authorization. Confirm jurisdiction and obtain explicit authorization covering dumpster diving.

What to look for:

- Unshredded documents containing employee names, internal processes, or system information
- Obsolete badges or access credentials
- Old hard drives or storage media
- Network equipment manuals or configuration printouts
- Vendor invoices revealing technology in use

[SLIDE: Shoulder Surfing and Environmental Observation]

Environmental observation during physical testing reveals information without any bypass or intrusion:

Shoulder surfing: Observing a screen from over or beside the user. Common in open offices, cafeterias, and conference rooms near public spaces.

Sensitive information visible on screens: Assess whether monitors face high-traffic areas or windows.

Physical security policy violations: Unlocked computers, printed documents left on desks, whiteboards showing sensitive diagrams.

Clean desk policy compliance: Documents, access control information, and visitor logs left visible on desks.

[PAUSE for transition]

---

## Segment 5: Authorized Physical Pen Test Methodology (Lines 151–195)

[SLIDE: Physical Test Phases]

A properly conducted physical penetration test follows a structured methodology.

Phase 1 — Authorization and Documentation: Confirm written authorization. Prepare the get-out-of-jail letter. Establish an emergency contact at the client. Define abort conditions. Define what will and will not be photographed or recorded.

Phase 2 — Reconnaissance: External surveillance (from public areas only). OSINT on facility, personnel, and schedule. Review available floor plans, visitor procedures, and security staff information.

Phase 3 — Target Identification: Identify specific physical targets: server room, network closets, executive offices, data center cage, HR offices.

Phase 4 — Pretext and Approach Development: Design the cover story, appropriate costume/attire, supporting props (clipboard, tools, fake ID badge), and communication scripts.

Phase 5 — Assessment Execution: Attempt physical access using authorized techniques. Document each attempt with notes and authorized photography. Record timestamps and security control responses.

Phase 6 — Reporting: Document all findings with evidence, access paths, security gaps, and remediation recommendations.

[SLIDE: The Get-Out-of-Jail Letter]

The get-out-of-jail letter (sometimes called the authorization letter or safety card) is a physical document carried by the tester that confirms the authorized nature of the assessment.

It should include:

- Name of the testing organization
- Name of the authorizing client executive (with title)
- Description of the authorized activities
- Dates of authorized testing
- Client emergency contact name and phone number
- Client organization letterhead and signature

If a security guard, building security, or law enforcement officer challenges the tester, present this letter and provide the contact number. The client contact should be available to answer calls during active testing.

[SLIDE: Documenting Physical Findings]

Physical findings are documented differently from technical findings. Key documentation requirements:

Access path: Describe the exact entry path, from the property perimeter to the target location.

Entry method: Note which control was bypassed and how (e.g., "Tailgated through the main lobby door by following a group of employees").

Time and duration: Record when access was obtained and how long it was maintained before detection or voluntary departure.

Evidence: Note any sensitive information observed (not photographed without authorization) — document type, general content, location.

Risk assessment: What could an adversary accomplish with the access obtained?

[PAUSE for transition]

---

## Segment 6: Reporting Physical Findings and PT0-002 Alignment (Lines 196–235)

[SLIDE: Physical Security Findings Examples]

Common findings from physical penetration tests:

Badge system using 125 kHz HID Prox — Critical. Cards can be cloned at range without the cardholder's knowledge. Upgrade to mutual-authentication smart card system.

No anti-tailgating controls at main entrance — High. Tested successfully on 4 of 5 attempts during business hours. Implement security vestibule or deploy reception officer.

Clean desk policy non-compliance — Medium. Network diagram and active directory credential printout found on unattended desk. Enforce clean desk policy with spot check program.

Dumpster contained unshredded payroll documents — High. Names, titles, salary information, and partial SSNs visible. Implement cross-cut shredding policy for all documents.

Server room accessible from unlocked utility corridor — Critical. No badge control on utility corridor door. Server room accessible without badge after entering corridor. Secure utility corridor access.

[SLIDE: CVSS for Physical Findings]

Physical findings present a CVSS scoring challenge because CVSS is designed for software vulnerabilities. For physical findings, use:

Attack Vector: Physical (AV:P) for findings that require physical presence.

Note that AV:P findings score lower than network-accessible findings, which may not accurately reflect the business risk of physical access to a server room. Many organizations supplement CVSS with custom risk ratings for physical findings.

[SLIDE: PT0-002 Exam — Physical Security Objectives]

For the PT0-002 exam, physical security topics appear in:

Domain 2.5: Perform physical security reconnaissance.

Domain 3.5: Perform social engineering and physical attacks. Specific techniques: tailgating, badge cloning, shoulder surfing, dumpster diving, lock picking.

Know the difference between tailgating and piggybacking: In some exam contexts, tailgating implies the unauthorized person enters without the authorized person's knowledge; piggybacking implies the authorized person is aware and passively allows entry.

[SLIDE: Module Summary]

Module 12 covered the full physical security assessment methodology: reconnaissance of facilities using OSINT, RFID badge reading and cloning concepts using Proxmark, lock picking principles, tailgating and mantrap testing, dumpster diving, environmental observation, and the critical legal and documentation requirements — specifically the get-out-of-jail letter.

Physical security testing is perhaps the most viscerally impressive assessment type because it demonstrates that sophisticated network security is rendered irrelevant by unlocked doors and unaware employees.

The lab for this module is a case analysis exercise — reviewing documented physical penetration test findings and developing remediation recommendations, since hands-on physical entry testing requires specific facility and authorization arrangements beyond the classroom.

[END RECORDING]
