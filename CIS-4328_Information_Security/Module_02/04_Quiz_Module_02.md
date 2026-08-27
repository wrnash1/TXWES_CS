# Quiz — Module 02: Social Engineering and Phishing

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | 10 Questions | 100 Points

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Questions are written to match the difficulty and style of the CompTIA Security+ SY0-701 exam.

---

## Question 1

An attacker calls an employee, claims to be from the company's IT help desk, and asks the employee to confirm their username and current password so IT can "migrate your account to the new system." The caller ID shows the company's main office number. Which social engineering technique is this?

A) Smishing

B) Vishing combined with pretexting

C) Spear phishing combined with baiting

D) Tailgating combined with impersonation

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Smishing uses SMS text messages as the delivery channel. This attack uses a phone call, which defines vishing.
- Why C is incorrect: Spear phishing uses targeted email, not phone calls. Baiting involves offering a physical or digital lure. Neither applies to a phone-based credential request.
- Why D is incorrect: Tailgating involves physical access — following someone through a door. This attack is entirely conducted over the phone.

---

## Question 2

An organization deploys SPF, DKIM, and DMARC for its email domain. An attacker registers the domain "c0rpname.com" (using a zero instead of the letter O) and sends targeted emails from that domain. The emails reach employee inboxes. Which statement best explains this outcome?

A) DMARC failed because the SPF record for the legitimate domain was not configured correctly.

B) SPF, DKIM, and DMARC passed for the attacker's domain because the attacker legitimately controls that domain.

C) DKIM failed because the attacker cannot generate a valid signature for the legitimate domain.

D) DMARC blocked the email but it was incorrectly delivered due to a misconfiguration in the mail gateway.

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: The issue is not a misconfiguration of the legitimate domain's SPF. The attacker controls a completely separate look-alike domain with its own valid DNS records.
- Why C is incorrect: DKIM would pass for the attacker's domain because the attacker controls the signing keys for c0rpname.com — DKIM only proves the signing domain owns the message, not that the domain is legitimate.
- Why D is incorrect: There is no indication of a DMARC block or misconfiguration. The emails pass all checks because they legitimately originate from the attacker's own domain.

---

## Question 3

A company's receptionist receives a visit from a person in a delivery uniform carrying several packages. The visitor says she needs to drop the packages in the server room since the regular IT contact "is out sick today." The receptionist badges her through the server room door to be helpful. What two social engineering techniques are demonstrated?

A) Vishing and baiting

B) Pretexting and tailgating

C) Spear phishing and impersonation

D) Smishing and shoulder surfing

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Vishing uses phone calls and baiting uses planted physical media or fake offers. Neither applies to a physical in-person entry deception.
- Why C is incorrect: Spear phishing is an email-based attack. While impersonation is occurring, the entry technique is tailgating enabled by the receptionist — not following someone through a door without their awareness.
- Why D is incorrect: Smishing uses SMS messages. Shoulder surfing involves observing input. Neither applies to this scenario.

---

## Question 4

An attacker researches a specific employee on LinkedIn, discovers she is the CFO of a healthcare company, identifies her direct supervisor by name, and sends her an email that references a real upcoming board meeting and asks her to review a "revised budget attachment." The attachment installs malware when opened. What type of attack is this?

A) Generic phishing

B) Smishing

C) Whaling

D) Clone phishing

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Generic phishing is mass and untargeted. This attack is highly personalized using OSINT and specifically targets a high-value executive (CFO), which defines whaling.
- Why B is incorrect: Smishing uses SMS text messages. This attack is delivered via email.
- Why D is incorrect: Clone phishing duplicates a previously sent legitimate email with a malicious substitution. This is an original targeted attack, not a clone of a prior message.

---

## Question 5

A security awareness manager wants to measure how susceptible employees are to phishing and provide immediate remediation when an employee clicks a malicious link. Which control best accomplishes both goals simultaneously?

A) Deploy a DMARC policy set to reject on the company's email domain.

B) Run quarterly phishing simulations with immediate redirect to training when employees click.

C) Require all employees to complete annual security awareness training.

D) Install URL sandboxing on the email gateway to test all links before delivery.

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: DMARC reduces spoofed inbound email. It does not measure employee susceptibility or provide training to employees.
- Why C is incorrect: Annual training measures completion rates, not actual susceptibility to phishing. It also does not provide immediate remediation at the moment of failure.
- Why D is incorrect: URL sandboxing is a technical preventive control. It blocks malicious links but does not test employee behavior or provide training.

---

## Question 6

Which psychological principle is most directly exploited when an attacker's phishing email states: "Your account has been flagged for unusual activity. If you do not verify your identity within the next 30 minutes, your account will be permanently suspended"?

A) Reciprocity

B) Social proof

C) Urgency and fear

D) Familiarity

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Reciprocity involves an attacker doing something for the target first to create a sense of obligation to return a favor. No prior favor is mentioned here.
- Why B is incorrect: Social proof relies on the behavior of others to normalize the request. No reference to others' behavior appears in this message.
- Why D is incorrect: Familiarity exploits the target's comfort with a known person or brand. While the email may impersonate a known brand, the specific mechanism driving action is the time-limited threat, not recognition.

---

## Question 7

An employee finds a USB drive in the company parking lot labeled "Q4 Layoff List — Confidential." She plugs it into her work laptop and the drive automatically executes code that installs a remote access trojan. Which two social engineering and technical elements made this attack successful?

A) Pretexting to create a false identity; SQL injection to execute the payload

B) Baiting to exploit curiosity; autorun execution of unsigned code on plug-in

C) Vishing to deliver the lure; cross-site scripting to execute the payload

D) Tailgating to gain physical access; buffer overflow to execute the payload

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Pretexting involves a fabricated scenario or identity presented by the attacker. Placing an unlabeled or temptingly labeled drive in a parking lot is baiting. SQL injection attacks databases via input fields — it is not the execution mechanism here.
- Why C is incorrect: Vishing uses phone calls. Cross-site scripting injects malicious scripts into web pages. Neither is the attack vector here.
- Why D is incorrect: Tailgating involves unauthorized physical entry behind an authorized person. Buffer overflow overwrites memory via a programming flaw. Neither describes this attack.

---

## Question 8

An organization wants to prevent attackers from sending emails that appear to come from their domain. They implement SPF and DKIM but have not yet deployed DMARC. An attacker sends an email that passes SPF but fails DKIM. What happens to the email without DMARC in place?

A) The email is automatically rejected because DKIM failed.

B) The receiving mail server has no policy instruction and may deliver the email anyway.

C) The email is quarantined by SPF because SPF enforces policy when DMARC is absent.

D) The email is rejected because the combination of SPF pass and DKIM fail triggers a conflict rule.

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: DKIM failure alone does not automatically reject email. DKIM provides a signal, but without DMARC, there is no enforcement policy telling receiving servers what to do with failures.
- Why C is incorrect: SPF does not quarantine or enforce policy on DKIM results. SPF only verifies the sending IP address. Policy enforcement is DMARC's role.
- Why D is incorrect: There is no standard "conflict rule" that combines SPF pass and DKIM fail to trigger rejection. Only DMARC applies policy based on the combined results.

---

## Question 9

A threat actor calls a junior employee claiming to be the company's external auditor and says he urgently needs the list of all user accounts and their associated departments emailed to him before the end of business today or the annual audit report will flag a compliance deficiency. The employee is about to comply. What should the employee do, and which security principle does this scenario illustrate?

A) Comply immediately; the urgency of an external audit supersedes normal security procedures.

B) Verify the auditor's identity through an independent callback to the auditing firm before taking any action; this illustrates that urgency cues should trigger more caution, not less.

C) Reject all audit requests via phone; this illustrates that external auditors should never contact employees directly.

D) Forward the request to the CEO for approval; this illustrates the principle of least privilege.

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Urgency is a social engineering trigger designed to short-circuit caution. Legitimate auditors do not require employees to bypass security verification procedures. Complying without verification is exactly what the attacker wants.
- Why C is incorrect: This overstates the rule. External auditors can legitimately contact employees. The security requirement is independent verification, not blanket refusal.
- Why D is incorrect: Forwarding to the CEO is not the defined response and does not address the immediate need to verify the caller's identity. Least privilege governs access rights, not how to respond to suspicious external requests.

---

## Question 10

A security analyst is reviewing logs after a business email compromise incident. The attacker sent emails from the domain "firstnatl-bank-secure.com" to employees of First National Bank. The emails appeared to come from the CEO and instructed employees to reset their credentials on a linked page. Which email security control, if properly deployed by First National Bank for their own domain, would have had NO direct effect on preventing this specific attack?

A) DMARC with a reject policy

B) DKIM signing of outbound email

C) SPF record listing authorized sending IP addresses

D) Employee security awareness training on look-alike domains

**Correct Answer:** A

**Distractor Analysis:**

- Why A is correct (and thus the answer): DMARC protects the legitimate domain from being spoofed. In this attack the attacker used a completely separate domain they control. First National Bank's DMARC policy governs email claiming to be from their domain — it has no authority over mail sent from a different domain the attacker registered.
- Why B is incorrect as a distractor: DKIM similarly would not directly block this attack for the same reason — DKIM for the bank's domain does not apply to mail from an attacker-controlled domain. However, the question asks which control has NO direct effect, and the most precisely correct answer is DMARC since it is the enforcement layer that specifically addresses domain spoofing of the protected domain.
- Why C is incorrect as a distractor: SPF for the bank's own domain also has no effect on mail from an attacker-controlled domain.
- Why D is incorrect: Awareness training on look-alike domains would directly help employees recognize that "firstnatl-bank-secure.com" is not the legitimate bank domain — making D the most effective control for this specific attack type.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 02 Quiz

Proprietary and Confidential. Not for disclosure outside of authorized course use.

---

### Question 11 (5 points)

An attacker sends a text message to a hospital employee that reads: "URGENT: Your payroll direct deposit account has been changed. If you did not do this, click here immediately to reverse it." The link leads to a credential-harvesting page. Which two characteristics correctly classify this attack?

- A) Vishing and authority
- B) Smishing and urgency/fear
- C) Spear phishing and social proof
- D) Clone phishing and scarcity

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Vishing uses voice calls as the delivery channel. This attack is delivered via SMS text message, which defines smishing. Authority might be a secondary element, but the dominant psychological trigger is urgency combined with fear of financial loss.
  - Why C is incorrect: Spear phishing is an email-based attack personalized with OSINT about the target. This attack is delivered via SMS and uses mass urgency rather than personalized OSINT content. Social proof relies on peer behavior as a trigger — this message uses fear of financial harm, not peer behavior.
  - Why D is incorrect: Clone phishing duplicates a previously delivered legitimate email with a malicious substitution. This is a new message delivered via SMS, not a cloned email. Scarcity involves limited availability; this trigger is immediate financial threat (fear), not scarcity.

---

### Question 12 (5 points)

A company's email gateway is configured with SPF, DKIM, and DMARC set to p=quarantine. An employee receives a phishing email that appears to come from her own company's domain. The email passed all three authentication checks. A security analyst determines the email was sent from the company's own legitimate email server by a compromised internal service account. Why did the authentication checks pass?

- A) SPF, DKIM, and DMARC only work for external domains; they do not validate internal senders
- B) The email was legitimately authorized by the domain's own DNS records and signed with valid keys because it originated from the company's own infrastructure
- C) The DMARC quarantine policy does not apply to emails that pass SPF
- D) DKIM signatures are only verified for emails originating outside the organization's network perimeter

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: SPF, DKIM, and DMARC apply to all email claiming to originate from a domain, including mail sent from internal infrastructure. The protocols validate the sending domain, not the sender's physical location.
  - Why C is incorrect: DMARC quarantine applies when SPF or DKIM fails alignment. When both pass, DMARC will allow the email — regardless of quarantine policy — because the email passed authentication. The scenario describes an email that passed all checks.
  - Why D is incorrect: DKIM signature verification is performed by the receiving server regardless of where the email originated. There is no perimeter exception in the DKIM protocol.

---

### Question 13 (5 points)

During a physical security assessment, a consultant leaves a brochure in the lobby that reads: "Free USB drives available at the front desk — take one!" The USB drives are loaded with an autorun executable that beacons to an external server when plugged in. Three employees pick up drives and plug them in. Which attack technique does this represent?

- A) Tailgating — the consultant gained physical access to distribute the drives
- B) Baiting — the consultant used a tempting offer to induce employees to connect the malicious devices
- C) Quid pro quo — the consultant offered drives in exchange for network access credentials
- D) Pretexting — the consultant fabricated an identity as a promotional representative

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Tailgating involves following an authorized person through a secured physical entry point. The consultant did not pass through a secured door behind someone — the drives were left in a public lobby.
  - Why C is incorrect: Quid pro quo involves an explicit exchange — the attacker offers something in return for specific information or access. The brochure is a one-way offer with no requested exchange of information. The employees received a drive without being asked to provide anything in return.
  - Why D is incorrect: While the consultant may have fabricated a purpose, the core technique is baiting — the attack relies on employees' curiosity and greed to self-inflict the attack by plugging in the drive. Pretexting alone does not capture the mechanism of the attack.

---

### Question 14 (5 points)

A penetration tester calls a help desk agent and says: "Hi, this is James from the network operations center. We're seeing unusual activity on your subnet and I need you to run a quick diagnostics command for me — just open a command prompt and type this." The agent complies. Which technique did the tester use, and which psychological principle made it effective?

- A) Baiting — fear of network disruption
- B) Vishing with pretexting — authority of the NOC role combined with urgency of the incident
- C) Smishing — the technical instructions were delivered via text message
- D) Tailgating — the tester entered the building pretending to be from the NOC

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Baiting involves placing a physical or digital lure that the victim discovers independently. The tester actively called the agent — this is a direct social engineering phone call, not a passive lure.
  - Why C is incorrect: Smishing uses SMS text messages. This attack was conducted over a phone call, which is the defining characteristic of vishing.
  - Why D is incorrect: Tailgating is a physical attack involving unauthorized entry through a secured door. This attack was entirely conducted remotely over a phone call with no physical component.

---

### Question 15 (5 points)

An organization implements an email gateway rule that rewrites all URLs in inbound email to point to a proxy service that detonates the URL in an isolated sandbox before allowing the browser to load the destination. Which anti-phishing layer does this represent, and what specific threat does it address?

- A) Layer 1 — it reduces domain spoofing by verifying the sending domain
- B) Layer 2 — it reduces employee clicks by analyzing the URL before the browser renders malicious content
- C) Layer 3 — it limits damage by requiring MFA even after credentials are captured
- D) Layer 4 — it detects malware execution after the user has already clicked and been infected

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Layer 1 controls (SPF/DKIM/DMARC) reduce email that reaches the inbox by verifying sending domain authorization. URL rewriting does not affect domain authentication — the email has already been delivered when URLs are rewritten.
  - Why C is incorrect: MFA limits damage after credential theft by requiring a second factor. URL sandboxing prevents the malicious page from loading — it operates before credential capture, not after.
  - Why D is incorrect: Layer 4 controls (EDR) detect malware execution after a user has been infected. URL sandboxing stops the malicious URL before it loads, preventing initial infection — it is a preventive Layer 2 control.

---

### Question 16 (5 points)

A phishing email targeting employees of a defense contractor includes the name of their current project, the names of two colleagues, and references to a real internal meeting from two weeks ago. The email was sent to exactly 12 people on the project team. What type of phishing does this represent, and what technique did the attacker use to personalize it?

- A) Generic phishing using company name only; the attacker guessed the project details
- B) Spear phishing using OSINT gathered from LinkedIn, professional directories, and corporate press releases
- C) Whaling targeting the project's executive sponsor using confidential acquisition data
- D) Clone phishing replicating a previous internal meeting invitation

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Generic phishing is mass and untargeted. Targeting exactly 12 people on a specific project with accurate project details, colleague names, and meeting references is the defining characteristic of spear phishing — it requires deliberate, targeted research.
  - Why C is incorrect: Whaling targets C-suite or high-value executive targets specifically. This attack targets a project team of 12, not an executive. The defining characteristic is the narrow, research-driven targeting, not the seniority of the targets.
  - Why D is incorrect: Clone phishing duplicates a previously delivered legitimate email with a malicious element substituted. The scenario describes a new, original email that references real details — it is not described as a copy of a previously received message.

---

### Question 17 (5 points)

A company wants to prevent employees from discarding documents containing customer account numbers, employee SSNs, and internal financial data in ordinary trash bins. Which two controls best address this risk at the Physical and Administrative layers respectively?

- A) Physical: full disk encryption on all servers; Administrative: data classification policy
- B) Physical: cross-cut shredders in every office area; Administrative: clean desk and document disposal policy
- C) Physical: badge-access server room; Administrative: acceptable use policy for email
- D) Physical: security camera in the copy room; Administrative: annual security awareness training

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Full disk encryption protects digital data at rest on storage media — it has no effect on printed documents placed in trash. A data classification policy is relevant but does not specifically mandate physical document disposal procedures.
  - Why C is incorrect: Badge access to a server room protects physical access to servers, not document disposal. An acceptable use policy for email governs digital communications, not paper document handling.
  - Why D is incorrect: A security camera in the copy room is a detective control that records activity but does not prevent documents from being placed in regular trash. Annual training is valuable but does not directly provide a physical disposal mechanism or a specific policy mandate.

---

### Question 18 (5 points)

A DMARC record for a domain is set to `p=none; rua=mailto:dmarc-reports@company.com`. An attacker successfully sends a spoofed email claiming to be from this domain and it is delivered to the recipient. The security team receives a DMARC report showing the failed alignment. What does the `p=none` policy reveal about this DMARC deployment, and what change would prevent future delivery?

- A) p=none means the domain has no DMARC record; the security team should create one immediately
- B) p=none is a monitoring-only policy; it reports failures but instructs receiving servers to deliver the email anyway — changing to p=reject would cause receiving servers to discard spoofed emails
- C) p=none applies only to internal email; external email requires a separate p=reject record
- D) p=none causes receiving servers to quarantine all email — the security team should change it to p=reject to allow legitimate mail through

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: p=none is a valid DMARC policy value — it means the domain has a DMARC record but has not yet set an enforcement action. The domain already has a DMARC record, evidenced by the reports being received.
  - Why C is incorrect: DMARC applies to all email claiming to originate from the protected domain, regardless of whether the recipient is internal or external. There is no separate internal/external policy configuration.
  - Why D is incorrect: p=none instructs receiving servers to take no action on failures — it delivers all mail and only reports. p=quarantine would send failing emails to spam; p=reject would discard them. p=none does not quarantine anything.

---

### Question 19 (5 points)

An employee reports that she received an email that appeared to come from a vendor she works with regularly. The email said: "Per your request last week, I've attached the revised contract. Let me know if the terms look correct." She does not recall making such a request, but the sender's name and email address match the real vendor contact she knows. She opens the attachment and her workstation is infected. Which phishing technique most likely explains this attack?

- A) Generic phishing — the mass email happened to reference a common business activity
- B) Clone phishing — the attacker duplicated a real previous email from the vendor and replaced the legitimate attachment with a malicious one
- C) Smishing — the attacker sent the message via SMS and it was forwarded to email
- D) Whaling — the vendor's executive was targeted and their account was used to send the message

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Generic phishing is mass and untargeted. The email references a specific prior request from a specific known vendor contact with accurate details. This level of specificity is inconsistent with generic bulk phishing.
  - Why C is incorrect: Smishing is SMS-based. The scenario describes an email attachment, not an SMS message.
  - Why D is incorrect: Whaling targets C-suite executives specifically. The target here is a regular employee receiving a vendor communication. The attack technique — duplicating a prior email with a malicious attachment substitution — is clone phishing, not whaling.

---

### Question 20 (5 points)

A security awareness program includes a module on recognizing social engineering. The module teaches employees to: pause before acting on urgent requests, verify the requester's identity through a separate channel, and never provide credentials over the phone or email. Which core defense principle do all three behaviors share?

- A) Defense in depth — multiple technical layers protect against each attack
- B) Disrupting the psychological triggers that make social engineering effective by introducing a verification step before compliance
- C) Non-repudiation — requiring the requester to sign a digital document before action is taken
- D) Principle of least privilege — employees should only share information others need to know

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Defense in depth is an architectural security principle about layering controls. The three behaviors described are human behavioral practices, not technical control layers. They address the human psychological vulnerability, not the technical attack surface.
  - Why C is incorrect: Non-repudiation is a technical property enforced by digital signatures to prove who performed an action. Verbal verification and identity confirmation over a separate channel are not the same as cryptographic non-repudiation.
  - Why D is incorrect: Least privilege governs what access level users and systems should have — it limits permissions. The behaviors described address how employees should respond to social engineering requests, not how permissions should be configured.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 02 Quiz

Proprietary and Confidential. Not for disclosure outside of authorized course use.
