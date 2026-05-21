# Quiz: Module 11 - Social Engineering and Phishing Simulation
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which wireless security standard is vulnerable to offline dictionary attacks against its four-way handshake, allowing an attacker who captures the handshake to attempt password cracking without further interaction with the access point?
*   A) WPA3
*   B) WPA2-Personal (PSK)
*   C) WPA2-Enterprise (802.1X)
*   D) WEP
*   **Correct Answer:** B) WPA2-Personal (PSK)
*   **Distractor Analysis:**
    *   *Why B is correct:* WPA2-Personal uses a Pre-Shared Key (PSK) and a four-way handshake during client authentication. The handshake contains material derived from the PSK through PBKDF2 key derivation. An attacker who captures this handshake can attempt offline dictionary attacks — using tools like `aircrack-ng` or Hashcat — without any further contact with the AP. The strength of the protection depends entirely on the complexity of the passphrase.
    *   *Why A is incorrect:* WPA3 replaces the four-way handshake with SAE (Simultaneous Authentication of Equals), which provides forward secrecy and is resistant to offline dictionary attacks. Even if network traffic is captured, the PSK cannot be derived from it.
    *   *Why C is incorrect:* WPA2-Enterprise uses 802.1X with a RADIUS authentication server — there is no shared PSK to crack. Each user authenticates with individual credentials via EAP protocols. The primary attack against Enterprise is a rogue AP capturing EAP credential exchanges.
    *   *Why D is incorrect:* WEP is also crackable, but through a different mechanism — RC4 IV collision attacks that require collecting a large number of data packets, not a handshake capture. WEP cracking is a distinct technique from WPA2 offline dictionary attacks.

---

**Question 2**
In the context of social engineering penetration testing, which of the following best defines **spear phishing**?
*   A) A mass email campaign sent to thousands of recipients using generic lures such as prize notifications or account security alerts, relying on volume rather than personalization to achieve a small percentage of successes.
*   B) A targeted phishing attack directed at a specific individual or organization, using personalized reconnaissance data — such as the target's name, role, colleagues, or recent organizational events — to craft a highly convincing pretext.
*   C) A phone-based social engineering attack in which the attacker impersonates IT support, a bank, or another trusted authority to manipulate the target into revealing credentials or performing an action.
*   D) A physical social engineering technique in which an attacker follows an authorized employee through a secured door without using their own credentials, gaining unauthorized physical access to a facility.
*   **Correct Answer:** B) A targeted phishing attack directed at a specific individual or organization, using personalized reconnaissance data — such as the target's name, role, colleagues, or recent organizational events — to craft a highly convincing pretext.
*   **Distractor Analysis:**
    *   *Why B is correct:* Spear phishing is distinguished from generic phishing by its use of targeted reconnaissance. The attacker leverages OSINT (LinkedIn profiles, organizational charts, recent press releases) to make the email appear legitimate and relevant to the specific recipient. This dramatically increases success rates compared to mass phishing. PT0-002 tests the ability to distinguish spear phishing from its related variants.
    *   *Why A is incorrect:* This describes generic (mass) phishing — untargeted email campaigns sent in bulk. The defining characteristic is volume rather than personalization, which is the opposite of spear phishing.
    *   *Why C is incorrect:* This describes vishing (voice phishing) — a social engineering attack conducted over the phone. While it shares manipulation techniques with spear phishing, it uses a different delivery channel (voice) and is a distinct attack category.
    *   *Why D is incorrect:* This describes tailgating (or piggybacking) — a physical social engineering technique involving unauthorized physical access. It does not involve email, digital credentials, or online deception.

---

**Question 3**
A penetration tester is conducting an authorized social engineering engagement and wants to set up a fake login page that captures credentials when the target clicks a phishing link. Which tool automates this credential harvesting technique?
*   A) `nmap -sV target_ip`
*   B) The Social Engineering Toolkit (SET) using the Website Attack Vector → Credential Harvester → Site Cloner
*   C) `sqlmap -u "http://target/login" --forms`
*   D) `aircrack-ng -w wordlist.txt capture.cap`
*   **Correct Answer:** B) The Social Engineering Toolkit (SET) using the Website Attack Vector → Credential Harvester → Site Cloner
*   **Distractor Analysis:**
    *   *Why B is correct:* SET is an open-source Python framework purpose-built for social engineering simulations. Its Credential Harvester with Site Cloner automatically replicates a legitimate login page and hosts it on the attacker's server. When a victim navigates to the phishing URL and enters credentials, SET captures them and (optionally) redirects the victim to the real site so the attack goes unnoticed. This is the standard tool for credential harvesting simulations in authorized engagements.
    *   *Why A is incorrect:* `nmap -sV` performs service version detection against network ports. It is a network reconnaissance tool with no capability to host fake login pages or harvest credentials.
    *   *Why C is incorrect:* `sqlmap` is an automated SQL injection tool used to exploit database vulnerabilities in existing web applications. It does not create phishing pages or harvest credentials through social engineering.
    *   *Why D is incorrect:* `aircrack-ng` performs offline dictionary attacks against captured WPA2 wireless handshakes. It is a wireless cracking tool with no social engineering or web-based credential harvesting functionality.

---

**Question 4**
During a social engineering engagement, a penetration tester calls the target organization's help desk, claims to be a new remote employee having trouble accessing their account, and persuades the help desk agent to reset the password without following the normal verification process. Which social engineering principle is being primarily exploited?
*   A) Scarcity — creating the impression that the opportunity to help is limited and must be acted on immediately.
*   B) Authority — impersonating a figure of power whose instructions must be followed without question.
*   C) Pretexting combined with the principle of Liking/Familiarity — building a relatable persona to lower the target's suspicion and invoke a desire to be helpful.
*   D) Reciprocity — offering something of value to the target in exchange for the password reset.
*   **Correct Answer:** C) Pretexting combined with the principle of Liking/Familiarity — building a relatable persona to lower the target's suspicion and invoke a desire to be helpful.
*   **Distractor Analysis:**
    *   *Why C is correct:* The attacker constructs a pretext (new employee, remote, having trouble) that is inherently sympathetic and relatable. Help desk agents are conditioned to assist employees, and a struggling new remote worker triggers a desire to be helpful. The "new employee" framing also explains why verification processes might not apply — new users often legitimately lack proper credentials during onboarding. This scenario is a textbook pretexting attack exploiting familiarity and the desire to help.
    *   *Why A is incorrect:* Scarcity creates urgency around a limited resource or opportunity. While the tester may add urgency ("I need this for a meeting in 10 minutes"), the primary manipulation here is the sympathetic persona — not a scarcity trigger. Urgency would be a secondary element if present.
    *   *Why B is incorrect:* Authority involves impersonating someone with power over the target (e.g., an executive, IT security officer, auditor). Claiming to be a new employee is the opposite of an authority figure — it is a low-status, help-seeking persona.
    *   *Why D is incorrect:* Reciprocity involves offering something to create a sense of obligation. In this scenario the attacker is asking for help without offering anything in return — they are leveraging sympathy and helpfulness, not reciprocal exchange.

---

**Question 5**
A penetration tester receives written authorization to conduct a phishing simulation against a client's employees. The tester sends an email impersonating the client's IT department, stating that all employees must click a link to verify their credentials before the end of business day or their account will be locked. Which two psychological influence principles are being leveraged in this phishing pretext?
*   A) Scarcity and Social Proof
*   B) Authority and Urgency
*   C) Reciprocity and Intimidation
*   D) Familiarity and Pretexting
*   **Correct Answer:** B) Authority and Urgency
*   **Distractor Analysis:**
    *   *Why B is correct:* The email impersonates the IT department — an internal authority figure whose security directives employees are trained to follow. This is the Authority principle. The deadline ("before end of business day or account will be locked") creates time pressure that forces the target to act without careful deliberation. This is the Urgency principle. Together, Authority and Urgency are the two most effective and commonly combined social engineering triggers in phishing campaigns — PT0-002 tests recognition of these principles in scenario questions.
    *   *Why A is incorrect:* Scarcity implies a limited resource (not relevant here — account access is not scarce). Social Proof implies others are doing the same thing (not implied in this pretext). Neither is the primary mechanism of this scenario.
    *   *Why C is incorrect:* Reciprocity involves offering something to create obligation (the email is not offering anything). Intimidation involves explicit threats of punishment — the account lockout warning is closer to urgency than intimidation, as it frames the consequence as a technical outcome rather than a personal threat.
    *   *Why D is incorrect:* Familiarity involves building rapport before a request (not present in a cold phishing email). Pretexting is the technique being used (impersonating IT), but it is the mechanism of the attack — not one of the six psychological influence principles that PT0-002 tests by name.
