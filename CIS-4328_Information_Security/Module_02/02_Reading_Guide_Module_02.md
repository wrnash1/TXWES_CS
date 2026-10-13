# Reading Guide — Module 02: Social Engineering and Phishing

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 | Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

---

## Introduction

Module 02 covers the human side of information security — social engineering and its most prevalent form, phishing. These attacks bypass technical controls entirely by targeting the human element. The SY0-701 exam expects you to identify social engineering techniques by scenario, understand the psychological principles that make them effective, and recommend appropriate technical and administrative countermeasures.

---

## 1. Core Concepts and Definitions

**Social Engineering** is the manipulation of individuals into performing actions or divulging confidential information by exploiting psychological tendencies rather than technical vulnerabilities. The attacker exploits trust, authority, urgency, and fear rather than software flaws.

**Phishing** is any deceptive communication — typically email — designed to trick the recipient into revealing credentials, clicking a malicious link, or opening a malicious attachment. Phishing is the most common initial access vector in enterprise breaches.

**Pretexting** is the creation of a fabricated identity, scenario, or backstory that provides a believable justification for the attacker's request. The pretext makes the request seem legitimate and reduces the target's suspicion.

**Impersonation** is a specific form of pretexting where the attacker claims to be a real, known individual rather than a generic role. Impersonating the CEO, IT director, or a named colleague requires targeted research but is highly effective.

**Baiting** is a social engineering technique that exploits curiosity or greed. Leaving infected USB drives labeled with enticing titles in a target's environment is the classic example. Online baiting includes fraudulent offers of free software or media that deliver malware upon download.

**Quid Pro Quo** is a social engineering technique where the attacker offers something of value in exchange for information or access. An example is calling employees and offering to help solve a computer problem in exchange for login credentials.

---

## 2. Phishing Variant Comparison Table

| Variant | Delivery Channel | Target Profile | Key Distinguishing Feature | Example |
|---|---|---|---|---|
| Phishing | Email | Mass, untargeted | Generic lure sent to thousands | Fake bank email to all customers |
| Spear Phishing | Email | Specific individual or org | Personalized with OSINT details | Email referencing target's boss and project |
| Whaling | Email | Executives, high-value targets | Targets "big fish" for large impact | BEC attack targeting CFO for wire transfer |
| Vishing | Phone / VoIP | Varies | Voice delivery with caller ID spoofing | IT help desk impersonation call |
| Smishing | SMS / text message | Mobile users | Link in text message | Fake package delivery notification |
| Clone Phishing | Email | Previous email recipients | Duplicates a legitimate prior email with malicious substitution | Resent invoice email with swapped attachment |

---

## 3. Psychological Principles Exploited by Social Engineers

| Principle | Definition | Attack Example |
|---|---|---|
| Authority | People comply with perceived authority figures without question | Caller claims to be the CEO and demands immediate action |
| Urgency | Time pressure short-circuits critical thinking | "Your account will be locked in one hour" |
| Scarcity | Limited availability drives impulsive action | "This is the only way to restore access before the deadline" |
| Familiarity | People trust those they recognize or feel connected to | Attacker references the target's colleague's name and project |
| Social Proof | People assume others' behavior represents the correct action | "All your teammates have already updated their credentials" |
| Fear | Threat of negative consequences triggers panic | "Legal action will be taken unless you verify immediately" |
| Reciprocity | People feel obligated to return favors | Attacker helps with a minor issue then asks for credentials in return |
| Intimidation | Aggressive pressure prevents logical evaluation | Impersonated executive berating a help desk employee |

---

## 4. Physical Social Engineering Techniques

**Tailgating (Piggybacking)** — An unauthorized person follows an authorized employee through a secured door or access point without independently authenticating. Social norms discourage people from challenging others who appear to belong in a space. The technical countermeasure is a mantrap — a double-door vestibule where only one person can enter per authentication cycle. Administrative countermeasures include a tailgating awareness policy and training.

**Dumpster Diving** — Retrieving sensitive information from discarded physical materials including printed documents, old hard drives, sticky notes with passwords, and printed organizational charts. Countermeasures: mandatory cross-cut shredding policy for all documents, secure disposal procedures for electronic media, and clean desk policy.

**Shoulder Surfing** — Visually observing sensitive information as a target enters it — passwords at a keyboard, PINs at an ATM, documents on a screen in a public space. Countermeasures: privacy screens on laptops and monitors, screen orientation awareness, and training for public workspace security.

**Badge Cloning** — Copying the data from a proximity card or RFID badge using a concealed reader to create a duplicate that allows unauthorized physical access. Countermeasures: shielded badge holders (Faraday cage wallets), upgraded access card technology with stronger encryption, and continuous access log review.

---

## 5. Email Security Protocol Reference

| Protocol | Full Name | What It Does | DNS Record Type | Protection Against |
|---|---|---|---|---|
| SPF | Sender Policy Framework | Lists authorized sending IP addresses for a domain | TXT | Unauthorized servers sending email as your domain |
| DKIM | DomainKeys Identified Mail | Adds a cryptographic signature to outgoing email headers | TXT | Message tampering in transit; confirms authorized sending server |
| DMARC | Domain-based Message Authentication, Reporting and Conformance | Enforcement policy combining SPF and DKIM; specifies reject/quarantine/none action | TXT | Domain spoofing; provides aggregate reports on spoofing attempts |

**How they work together:** SPF verifies the sending IP. DKIM verifies the message content and header integrity. DMARC uses the results of both to apply an enforcement action and report on failures. A complete anti-spoofing deployment requires all three.

---

## 6. Anti-Phishing Technical Controls Summary

| Control | Category | Function | How It Addresses Phishing |
|---|---|---|---|
| Email filtering / anti-spam gateway | Technical | Preventive | Blocks known malicious messages before delivery |
| URL sandboxing | Technical | Preventive / Detective | Detonates links in isolation to detect malicious redirects |
| Attachment sandboxing | Technical | Preventive / Detective | Opens attachments in isolation to observe malicious behavior |
| SPF / DKIM / DMARC | Technical | Preventive | Reduces domain spoofing; enables rejection of spoofed email |
| Multi-factor authentication | Technical | Compensating | Prevents credential use even when phishing captures username and password |
| Endpoint detection and response (EDR) | Technical | Detective / Corrective | Detects malware installed via phishing click and enables response |
| Phishing simulation | Administrative | Detective / Corrective | Measures human susceptibility; triggers just-in-time training |
| Security awareness training | Administrative | Preventive | Builds employee ability to recognize and report phishing |
| Incident reporting procedure | Administrative | Detective | Enables rapid containment when phishing succeeds |

---

## 7. Social Engineering Defense-in-Depth Framework

Effective defense requires controls at every layer because no single control eliminates phishing risk.

**Layer 1 — Reduce email reaching the inbox:** SPF, DKIM, DMARC configured correctly. Email gateway with sandboxing. URL rewriting and reputation checking.

**Layer 2 — Reduce clicks by trained humans:** Security awareness training conducted at least annually, with phishing simulations run quarterly. Employees trained to inspect sender addresses, hover over links before clicking, and report suspicious messages.

**Layer 3 — Limit damage when credentials are captured:** Multi-factor authentication deployed on all externally accessible systems. Even with captured credentials, the attacker cannot authenticate without the second factor.

**Layer 4 — Detect and respond when malware executes:** EDR on all endpoints. SIEM correlating alerts. Incident response plan with defined steps for phishing compromise. Procedures for rapid password reset and account quarantine.

---

## 8. Security+ Exam Tips for Module 02

**Exam Tip 1:** The exam will describe a scenario and ask you to name the social engineering type. Focus on the delivery channel first: email = phishing variant, phone = vishing, SMS = smishing. Then assess targeting: personalized = spear phishing, executive target = whaling.

**Exam Tip 2:** Pretexting is almost always combined with another technique. Pretexting + phone call = vishing + pretexting. Pretexting + physical entry = impersonation + tailgating. Name all applicable techniques.

**Exam Tip 3:** On email security protocols — SPF = IP authorization; DKIM = digital signature on message; DMARC = policy enforcement layer combining both. If the question asks what allows a domain owner to specify that receiving servers should reject spoofed email, the answer is DMARC.

**Exam Tip 4:** The best defense against phishing at the human level is security awareness training. The best technical control that limits damage after credentials are captured is MFA. Know which answer fits which question context.

**Exam Tip 5:** Baiting questions commonly describe a USB drive found in a parking lot. The attacker is relying on curiosity and autorun functionality. The countermeasure is disabling autorun/autoplay via Group Policy and blocking unmanaged USB devices via endpoint policy.

**Exam Tip 6:** Quid pro quo is a social engineering technique where the attacker offers something in exchange for information. This is different from baiting (which offers something and does not require information in return) — quid pro quo is an exchange.

**Exam Tip 7:** Tailgating and piggybacking are the same technique — an unauthorized person follows an authorized person through a secured entry. The technical countermeasure is a mantrap. The administrative countermeasure is a challenge policy and training.

**Exam Tip 8:** Shoulder surfing targets the Confidentiality pillar of the CIA Triad and is a passive attack — the attacker does not modify any data, only observes it.

---

## 9. Supplemental Resources

**1. CISA Phishing Guidance — "Phishing"**
<https://www.cisa.gov/topics/cyber-threats-and-advisories/malicious-cyber-activity/phishing>
CISA's authoritative overview of phishing attack types, indicators of compromise, and recommended organizational defenses. Directly supports the phishing variant comparison table and anti-phishing control framework covered in Module 02.

**2. Anti-Phishing Working Group (APWG) eCrime Trends Reports**
<https://apwg.org/resources/apwg-reports/>
Industry-leading quarterly reports tracking phishing attack volumes, targeted brands, malicious domain patterns, and attack vector trends. Use these reports to ground the Module 02 threat landscape in current real-world data and to support gap analysis arguments.

**3. Google Safe Browsing Transparency Report**
<https://safebrowsing.google.com/safebrowsing/report_phish/>
Google's public reporting tool and associated transparency data on phishing site detection. Useful for understanding how URL sandboxing and reputation-based URL filtering services identify and block malicious links at scale, as covered in the Module 02 Layer 1 defense-in-depth discussion.

---

## 9. Required Study Resources

- Professor Messer's SY0-701 study notes and video lectures for Domain 2 social engineering objectives, available free at professormesser.com.
- CompTIA's official SY0-701 exam objectives document, available at comptia.org. Review all Domain 2 objectives related to social engineering.

---

## 10. Study Checklist

- [ ] Define social engineering and list the six psychological principles it exploits.
- [ ] Name and describe all six phishing variants with their delivery channel and target profile.
- [ ] Explain pretexting, impersonation, baiting, quid pro quo, tailgating, and dumpster diving.
- [ ] Describe SPF, DKIM, and DMARC and explain how they work together to prevent email spoofing.
- [ ] List at least four technical controls that reduce phishing risk and state the function of each.
- [ ] Explain why MFA is the highest-impact control for limiting credential phishing damage.
- [ ] Describe the full attack chain that starts with a phishing email and ends with data exfiltration.
- [ ] Identify the CIA Triad property targeted by each phishing variant.
- [ ] Complete the Module 02 Lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.
- [ ] Post two peer replies by Sunday at 11:59 PM.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 02 Reading Guide

Proprietary and Confidential. Not for disclosure outside of authorized course use.
