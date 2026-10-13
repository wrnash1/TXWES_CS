# Reading Guide: Module 12 — Physical Security Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

Physical security testing evaluates whether an organization's physical access controls can be bypassed by an adversary. This module provides the conceptual foundation, methodology, legal requirements, and reporting standards for authorized physical penetration testing. All physical testing requires explicit written authorization; entry without authorization is criminal trespass regardless of security testing intent.

---

## Learning Objectives

After completing this module, students will be able to:

1. Explain the concentric rings model of physical security and identify common vulnerabilities at each layer.
2. Describe RFID access control technology and explain how 125 kHz cards are vulnerable to cloning.
3. Explain lock picking principles and identify common lock vulnerabilities.
4. Apply a structured methodology for authorized physical security assessments.
5. Identify the legal requirements specific to physical testing, including the get-out-of-jail letter.
6. Document physical security findings with appropriate risk ratings and remediation recommendations.
7. Map physical security testing techniques to PT0-002 exam objectives.

---

## Section 1: Physical Security Architecture

### 1.1 Defense in Depth — Physical Layer

Physical security defense in depth applies the same layered approach as network security:

**Layer 1 — Perimeter:** The outermost boundary. Includes fencing, barriers, lighting, CCTV, and vehicle access control. A strong perimeter deters opportunistic threats and channels legitimate access through monitored points.

**Layer 2 — Facility boundary:** Building walls, doors, windows, and the access control systems protecting them. This layer is the primary barrier against unauthorized entry.

**Layer 3 — Interior zones:** Controlled areas within the building. Server rooms, data centers, executive areas, and HR spaces represent higher-sensitivity zones requiring additional controls beyond general facility access.

**Layer 4 — Asset protection:** Direct protection of specific high-value assets. Laptop cable locks, server cage locks, locked filing cabinets, and media destruction procedures operate at this layer.

**Layer 5 — Process and culture:** Security awareness training, clean desk policies, visitor escort requirements, and security reporting culture. Human behavior is both a layer of security and the most common vulnerability.

### 1.2 Physical Security Standards

Several standards govern physical security practices in regulated environments:

**ISO/IEC 27001:** Annex A, Control 7 (Physical and Environmental Security) addresses secure areas, physical entry controls, and equipment security.

**PCI DSS:** Requirement 9 addresses physical access to cardholder data environments, including access control logs, visitor management, and physical media protection.

**HIPAA:** Physical safeguards under 45 CFR § 164.310 address facility access controls, workstation use and security, and device and media controls.

**NIST SP 800-53:** PE (Physical and Environmental Protection) controls cover access control, monitoring, visitor access, and emergency procedures.

---

## Section 2: Access Control Technology

### 2.1 RFID Technology Categories

RFID access control divides into frequency bands with very different security profiles:

**Low frequency (125 kHz) — Proximity cards:**

HID Prox, EM4100, and similar systems transmit a fixed card ID without any authentication or encryption. Any reader that comes within range can obtain the card ID. The ID can be copied to a blank card to create a functional clone.

These systems are ubiquitous in older facilities and are widely considered obsolete from a security standpoint. However, replacement requires significant investment in infrastructure (readers, cards, controllers) and organizations often delay upgrades.

**High frequency (13.56 MHz) — Smart cards:**

MIFARE Classic is vulnerable to cryptographic attacks (the CRYPTO1 cipher is broken). MIFARE DESFire and HID iCLASS SE implement AES encryption and mutual authentication. Properly configured HF cards are significantly harder to clone.

**Ultra-high frequency (UHF, 860–960 MHz):**

Used primarily for inventory tracking (EPC Gen2), not access control. Readable at much longer ranges (meters vs. centimeters for LF), which creates significant privacy risks if misapplied to access control.

### 2.2 Proxmark3 Capabilities

The Proxmark3 is the standard research and testing tool for RFID security assessment. Key capabilities in authorized assessments:

- Read and decode 125 kHz proximity cards
- Read and analyze 13.56 MHz smart cards
- Emulate read cards without writing to a physical blank
- Write cloned credentials to compatible blank cards
- Perform replay attacks to test reader behavior
- Perform fuzzing attacks against readers to test for denial-of-service conditions

The Proxmark3 RDV4 is the current professional version with improved antenna design and Bluetooth connectivity.

### 2.3 Multi-Factor Physical Access

The most secure access control combines:

- Something you have: RFID card, smart card, physical key
- Something you know: PIN code
- Something you are: Biometric (fingerprint, iris, facial recognition)

PIN-protected card readers (card + PIN) significantly reduce cloning risk because the cloned card alone is insufficient. Biometric systems provide strong assurance but introduce privacy considerations (biometric data is permanent — you can change a password, not a fingerprint).

Anti-passback rules prevent using the same credential to enter a controlled area multiple times without intermediate exit. This makes card cloning detectable: if a card appears to enter simultaneously from two different doors, the access control system alerts.

---

## Section 3: Lock Technology and Vulnerabilities

### 3.1 Pin Tumbler Lock Mechanics

The most common lock in commercial environments is the pin tumbler lock. Understanding how it works is fundamental to evaluating lock security:

The cylinder (plug) rotates when the correct key is inserted. The key pushes a series of driver pins and key pins to different heights. When all key pins are lifted exactly to the shear line between the plug and the housing, the plug rotates freely.

Manufacturing tolerances mean that pins bind sequentially rather than simultaneously under slight rotational tension. Lock picking exploits this: applying tension with a tension wrench causes one pin to bind. Setting that pin with a pick allows the next pin to bind. Repeating for all pins (typically 5–6) opens the lock.

### 3.2 Lock Security Ratings

ANSI/BHMA grading rates lock hardware:

- Grade 1: Commercial grade, highest durability
- Grade 2: Heavy-duty residential/light commercial
- Grade 3: Residential grade, lightest

Security ratings (separate from durability) evaluate resistance to physical attacks. High-security locks (Medeco, Abloy, Mul-T-Lock) use additional security features: security pins (spool, serrated, mushroom pins) that make picking significantly harder, hardened steel components that resist drilling, and restricted keyways that prevent unauthorized key duplication.

### 3.3 Bump Keys and Alternative Attacks

A bump key is a key cut to maximum depth at all positions. When inserted one position out and struck (bumped) with a mallet while applying rotational tension, the kinetic energy transfers to the driver pins, causing them to briefly jump above the shear line simultaneously. High-security pins (spool pins) resist bumping.

**Impressioning:** A soft blank key is inserted and manipulated to mark the contact points of the pins. The blank is filed at the marked points and tested repeatedly until it operates the lock. This attack creates a working key rather than requiring continuous access to the lock.

**Bypass tools:** Many doors can be bypassed without attacking the lock:

- Under-door tools reach the handle or thumb turn
- Loid/shim tools retract spring latches
- Door gaps allow entry with a simple loop of wire to press fire bar handles

---

## Section 4: Common Physical Attack Vectors

### 4.1 Tailgating and Piggybacking

**Tailgating** (the unauthorized person follows the authorized person without their knowledge) and **piggybacking** (the authorized person is aware and permits entry) are the most common physical security bypasses.

Countermeasures:

- Security vestibule (mantrap): Two-door airlock that prevents tailgating through the inner door.
- Turnstiles: Allow exactly one person per credential presentation.
- Security awareness training: Train employees to challenge unfamiliar people and avoid holding doors.
- Guard presence at controlled entrances.
- Anti-tailgating sensors: Detect multiple bodies passing through a single badge read.

### 4.2 Dumpster Diving

Physical media and documents discarded without proper destruction represent significant intelligence value for attackers.

Documented finds from real assessments include:

- Printed employee directories with phone numbers
- Network topology diagrams
- Application source code printouts
- Meeting notes discussing security vulnerabilities
- Old authentication tokens and badge templates
- Decommissioned hard drives
- Vendor invoices revealing specific technology products

The regulatory requirement for proper document destruction varies by industry. HIPAA requires destruction of PHI. FACTA requires destruction of consumer report information. PCI DSS requires destruction of cardholder data.

### 4.3 OSINT-Supported Physical Reconnaissance

Before physical assessment, OSINT builds a detailed picture of the target facility:

**Satellite and aerial imagery** (Google Maps, Google Earth): Identifies facility layout, entrances, parking areas, shipping docks, HVAC areas, and external cameras.

**Street View**: Reveals ground-level detail of entrances, intercom systems, window configurations, and visible security measures.

**Building permit records**: Many municipalities post permit records including floor plans online. Structural drawings can be obtained through public records requests.

**Glassdoor and employee reviews**: Employees sometimes describe security procedures in workplace reviews.

**Social media**: Employees post photos from inside facilities, often including views of access badge designs, server room doors, and workstation layouts.

---

## Section 5: Legal Framework for Physical Testing

### 5.1 Criminal Law Exposure

Physical penetration testing without proper authorization exposes testers to criminal liability for:

- Trespass (misdemeanor to felony depending on jurisdiction)
- Breaking and entering
- Theft (if any property is removed, even temporarily)
- Fraud (impersonating vendors, contractors, or employees)
- Wiretapping/recording (if interactions are recorded without consent)

The authorization letter is the tester's legal protection. Without it, criminal charges are possible even if the client later confirms authorization, because law enforcement and prosecutors may not accept verbal authorization as a defense.

### 5.2 The Get-Out-of-Jail Letter

The authorization letter must be physically carried during all testing. Required elements:

1. Organization letterhead of the authorizing client
2. Authorizing executive's name, title, and signature
3. Specific description of authorized activities
4. Testing dates and times
5. Tester names (or testing firm name)
6. 24/7 emergency contact name and direct phone number
7. Statement that the tester is authorized to conduct security assessment activities on the premises

The emergency contact must be someone with authority to confirm authorization and be accessible at all times during active testing. Multiple contacts are advisable.

### 5.3 Third-Party Property Considerations

Physical assessments frequently involve third-party property:

- Leased office space: The building owner may have access rights independent of the tenant's authorization
- Shared facilities: Testing in a shared office building requires awareness that other tenants' property is not in scope
- Parking lots and common areas: Adjacent property owned by third parties is never in scope

Clearly document the physical boundaries of the authorized scope and stay within them.

---

## Section 6: PT0-002 Exam Alignment

### 6.1 Physical Attack Vocabulary

For the PT0-002 exam, know these terms precisely:

| Term | Definition |
|------|-----------|
| Tailgating | Unauthorized entry by following authorized person without their knowledge |
| Piggybacking | Unauthorized entry with the (passive or active) awareness of the authorized person |
| Dumpster diving | Examining discarded materials for intelligence |
| Shoulder surfing | Observing sensitive information by watching the user |
| Badge cloning | Copying RFID credential to a blank card |
| Lock picking | Manipulating lock mechanisms without the key |
| Bump key | Specially cut key used for kinetic lock opening |
| Loiding | Using a flexible tool to retract a spring latch |
| Mantrap | Two-door security vestibule preventing tailgating |

### 6.2 Reporting Physical Findings

Physical findings use the same report structure as technical findings but require additional fields:

- Access path from perimeter to target
- Time required to achieve access
- Controls bypassed vs. controls that held
- Evidence of access (authorized documentation method)

---

## Key Terms

**RFID:** Radio Frequency Identification — wireless technology used in access control cards.

**HID Prox:** 125 kHz proximity card standard; no encryption, vulnerable to cloning.

**Proxmark3:** Professional RFID assessment tool capable of reading, emulating, and cloning cards.

**Pin tumbler lock:** The most common lock type, vulnerably to picking, bumping, and bypass attacks.

**Anti-passback:** Access control rule preventing sequential entries without intermediate exits.

**Get-out-of-jail letter:** Written authorization carried during physical testing to present to challenging parties.

**Mantrap:** Two-door airlock enforcing one-person-at-a-time entry.

---

## Review Questions

1. Explain why 125 kHz HID Prox cards are considered a security liability and what upgrade path you would recommend.

2. Describe the mechanical sequence in lock picking. What are security pins, and how do they resist picking?

3. A company's dumpster is located inside a fenced area behind their building. You have written authorization for physical testing. Can you perform a dumpster dive without additional authorization? Explain.

4. A physical assessment finds that 3 of 5 tailgating attempts at the server room entrance were successful. Write the finding in standard penetration test finding format (Risk Rating, Description, Evidence, Impact, Remediation).

5. What information must be included in a get-out-of-jail letter, and why is a phone number for the authorizing contact particularly important?

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives, Domain 2.5, 3.5
- NIST SP 800-53 Rev 5, PE Physical and Environmental Protection controls
- ISO/IEC 27001:2022, Annex A, Control 7 (Physical and Environmental Security)
- Granneman, S., & Carey, M. (2015). *Hacking: The Art of Exploitation.* No Starch Press.
- Proxmark3 Documentation: https://github.com/RfidResearchGroup/proxmark3
- ANSI/BHMA A156.30 High Security Locks Standard
