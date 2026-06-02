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
