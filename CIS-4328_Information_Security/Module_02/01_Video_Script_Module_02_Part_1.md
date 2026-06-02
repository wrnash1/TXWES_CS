# Video Script — Module 02, Part 1: Social Engineering and Phishing (Theory)

## CIS-4328 Information Security | Texas Wesleyan University

### Instructor: Professor Nash | CompTIA Security+ SY0-701 Alignment

### Estimated Duration: 13 minutes

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome to Module 02 — Social Engineering and Phishing. I'm Professor Nash.

Here is the most important sentence I will say in this entire module: the most sophisticated firewall in the world cannot stop an employee who willingly hands their password to an attacker who asked nicely. Social engineering is the exploitation of human psychology rather than technical vulnerabilities — and it is the most commonly used attack vector in real-world breaches. Industry data breach reports consistently show that over 70 percent of breaches involve a human element, and phishing is the leading delivery mechanism.

The SY0-701 exam maps social engineering heavily to Domain 2 — Threats, Vulnerabilities, and Mitigations. If you understand the taxonomy of social engineering attacks and the psychological principles that make them work, you can answer these questions reliably.

---

## Section 1 — What Is Social Engineering?

**[SHOW DIAGRAM: Central circle labeled Social Engineering. Six satellite circles labeled: Phishing, Vishing, Smishing, Pretexting, Tailgating, Baiting. Each satellite circle includes a one-line description of its delivery method.]**

**[Alt-text: Hub-and-spoke diagram. Center: Social Engineering. Six spokes extending to: Phishing — email-based deception targeting credentials or malware delivery; Vishing — voice call impersonation of trusted authorities; Smishing — SMS text messages with malicious links; Pretexting — attacker fabricates a believable identity or scenario; Tailgating — following authorized personnel through secured doors; Baiting — infected USB drives or fraudulent offers.]**

**Social engineering** is the practice of manipulating people into performing actions or disclosing confidential information by exploiting psychological tendencies rather than technical flaws. Unlike a buffer overflow or a SQL injection, a social engineering attack does not require any vulnerability in software — the human is the attack surface.

Social engineering attacks are effective because they exploit deeply wired human behaviors:

- **Authority** — people comply with requests from perceived authority figures. An attacker impersonating a CEO or IT administrator triggers compliance instinctively.
- **Urgency and Scarcity** — "Your account will be suspended in 24 hours unless you verify your credentials immediately." Urgency short-circuits critical thinking.
- **Familiarity and Liking** — people are more likely to comply with requests from people they like or recognize. Attackers research targets on social media to build rapport.
- **Social Proof** — "Everyone on your team has already updated their credentials; we just need yours." The assumption that others have complied creates pressure.
- **Fear** — threats of legal action, account suspension, or job loss trigger panic responses that bypass rational evaluation.
- **Reciprocity** — after doing something small for the target, the attacker leverages the social obligation to receive a favor in return.

---

## Section 2 — Phishing Attack Taxonomy

**[SHOW DIAGRAM: Hierarchy tree titled Phishing Attack Types. Root: Phishing. Four child nodes: Spear Phishing, Whaling, Vishing, Smishing. Each child has two sub-node tags describing the target profile and delivery method.]**

**[Alt-text: Hierarchy diagram. Root: Phishing — mass email deception. Child 1: Spear Phishing — targeted personalized email using OSINT. Child 2: Whaling — spear phishing targeting executives. Child 3: Vishing — voice call impersonation. Child 4: Smishing — SMS text message deception. Each child has two sub-node tags.]**

**Phishing** in its broadest form is any attempt to deceive a target into revealing credentials, clicking a malicious link, or opening a malicious attachment — most commonly delivered via electronic communication.

**Generic Phishing** casts a wide net. An attacker sends thousands or millions of identical emails impersonating a trusted brand — a bank, a shipping company, or a cloud service provider. The attacker does not know the targets personally. Because of the enormous volume, even a fraction-of-a-percent success rate yields thousands of compromised accounts.

**Spear Phishing** is targeted and personalized. The attacker researches the target using OSINT — social media, LinkedIn, company websites, press releases — and crafts an email that references specific real details: the target's manager's name, a current project, or a recent company event. Spear phishing is dramatically more effective than generic phishing because the personalization is convincing.

**Whaling** is spear phishing that specifically targets high-value individuals — executives, board members, financial controllers. The term plays on the "big fish" metaphor. A successful whaling attack against a CFO can authorize fraudulent wire transfers of millions of dollars. Business Email Compromise is a closely related technique.

**Vishing** — Voice Phishing — uses phone calls rather than email. An attacker might call an employee claiming to be from the IT help desk and ask them to confirm their username and password for "urgent maintenance." Caller ID spoofing allows attackers to display any number they choose, making the call appear to originate from within the organization.

**Smishing** — SMS Phishing — uses text messages. A common example is a fake package delivery notification with a link that leads to a credential harvesting page. Mobile users are often less cautious about link inspection on small screens.

**Exam Tip:** The SY0-701 exam will give you a scenario and ask you to identify the specific type of phishing. The key differentiator is the target profile and the delivery channel. Targeted and personalized = spear phishing. Executive target = whaling. Phone call = vishing. SMS = smishing.

---

## Section 3 — Pretexting and Impersonation

**[SHOW DIAGRAM: Five-step process flow titled Pretexting Attack Lifecycle. Step 1: Research — OSINT gathering. Step 2: Pretext Creation — building a believable false identity. Step 3: Contact — approaching target via chosen channel. Step 4: Exploitation — extracting information or access. Step 5: Exit — disengaging without raising suspicion. Arrows connect each step left to right.]**

**[Alt-text: Five-step horizontal process flow. Step 1 Research, Step 2 Pretext Creation, Step 3 Contact, Step 4 Exploitation, Step 5 Exit. Each step has a one-line description. Arrows connect each step in sequence.]**

**Pretexting** is the creation of a fabricated scenario that provides a believable reason for the attacker's request. The attacker adopts a false identity: an IT auditor, a new vendor representative, a regulatory compliance officer, a colleague from another office.

Classic pretexting scenarios:

- An attacker calls the help desk, claims to be a high-ranking executive who forgot their password while traveling, and pressures the operator to reset the account without completing identity verification.
- An attacker visits a data center dressed in work clothes with a clipboard, claims to be from an HVAC maintenance company, and asks to be escorted through secured doors.
- An attacker emails a request for network diagrams and IP ranges, claiming to be a new vendor preparing for an upcoming infrastructure assessment.

**Impersonation** is a related technique where the attacker specifically claims to be a real, known person — the CEO, the IT director, a specific colleague — rather than a generic role. Effective impersonation requires research to know enough specific details to remain convincing under questioning.

---

## Section 4 — Tailgating and Physical Social Engineering

**[SHOW DIAGRAM: Top-down floor plan of a secured building entrance. A badge reader is on the left wall. An authorized employee badge figure is shown passing through the security door. Directly behind the authorized employee, an attacker figure follows without badging. Dashed arrow shows the attacker's path through the open door. Label: Tailgating / Piggybacking.]**

**[Alt-text: Top-down floor plan. Badge reader on the left wall. Security door in the center. Authorized employee figure shown using badge reader as door opens. Attacker figure immediately behind, passing through without a badge. Dashed line traces attacker's path. Caption: Tailgating or Piggybacking.]**

Physical social engineering attacks bypass technical controls by exploiting courtesy and social norms.

**Tailgating** — also called **piggybacking** — occurs when an attacker follows an authorized employee through a secured door without independently authenticating. Most people feel uncomfortable challenging someone who appears to belong, especially if they are carrying boxes or dressed professionally. The countermeasure is a mantrap — a double-door system where only one person can pass at a time and identity is verified before the second door opens.

**Baiting** exploits curiosity. The classic technique is leaving USB drives labeled "Salary Information Q3" or "HR Confidential" in a parking lot or lobby. An employee who plugs the drive into a workstation executes malware automatically. The defense is disabling USB autorun, blocking unmanaged USB devices via endpoint policy, and training employees not to plug in unknown media.

**Dumpster Diving** is the retrieval of sensitive information from discarded materials — printed documents, old hard drives, written notes with credentials. The defense is a cross-cut shredding policy and secure disposal of all electronic media.

**Shoulder Surfing** is observing sensitive input — passwords, PINs, confidential documents — over a target's shoulder. The defense is privacy screens and training employees about the risks of working in public environments.

---

## Section 5 — Indicators and Defenses

**[SHOW DIAGRAM: Two-column table titled Social Engineering Red Flags and Countermeasures. Left column: Red Flags. Right column: Countermeasure. Five rows covering the most common indicators.]**

**[Alt-text: Two-column table. Left: Red Flags — Unsolicited urgency or fear; Request to bypass security procedures; Request for credentials via email or phone; Unknown person requesting physical access; Mismatched sender domain. Right: Countermeasures — Slow down and verify through official channels; Never bypass; escalate to supervisor; Credential requests are never valid via phone or email; Challenge without authorization or escort policy; Verify via independent callback.]**

Key indicators of a social engineering attempt:

- Unsolicited contact creating urgency or fear.
- Requests to bypass normal security procedures "just this once."
- Requests for passwords, PINs, or account credentials via phone or email.
- An unknown person requesting physical access or escort through secured areas.
- Sender email address that appears close to but does not exactly match a trusted domain.
- Excessive flattery or rapport-building before making a specific request.

Primary defenses:

- **Security awareness training** — the single most important defense. Employees who recognize these techniques are resistant to them.
- **Verification procedures** — a policy requiring independent callback verification before any sensitive action based on a phone or email request.
- **Least privilege** — limiting what any single compromised account can access reduces the impact of a successful attack.
- **Reporting culture** — making it easy and safe to report suspicious contacts without fear of embarrassment or discipline.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

In Part 1 we covered social engineering fundamentals and psychological principles, the complete phishing taxonomy including spear phishing, whaling, vishing, and smishing, pretexting and impersonation, physical social engineering techniques, and recognition and defense strategies.

In Part 2 we will walk through technical email security controls, analyze how social engineering chains into larger attacks, and work through SY0-701 exam scenarios.

For additional study, visit **professormesser.com** and review the official exam objectives at **comptia.org**.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 02 Part 1

Proprietary and Confidential. Not for disclosure outside of authorized course use.
