# Quiz: Module 04 — Threats, Attacks, and Vulnerabilities

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

### Question 1

A piece of malware has infected 47 workstations across a corporate network over a four-hour period. Log analysis shows no user interaction was required for the malware to spread from system to system. Which malware category BEST describes this threat?

A. Virus

B. Trojan

C. Worm

D. Rootkit

**Correct Answer:** C

**Explanation:** A worm self-propagates across networks without requiring user interaction or a host file. A virus requires user action to spread. A trojan disguises itself as legitimate software but does not self-replicate. A rootkit is designed to hide its presence, not to spread.

---

### Question 2

An attacker spent two weeks researching a target company using LinkedIn, the company website, and social media. The attacker then sent a personalized email to a single financial analyst referencing her specific project and her manager's name. Which attack type BEST describes this?

A. Phishing

B. Spear phishing

C. Whaling

D. Vishing

**Correct Answer:** B

**Explanation:** Spear phishing targets a specific individual using personalized information gathered through research. Generic phishing uses mass emails. Whaling targets C-suite executives specifically. Vishing uses voice/telephone as the delivery channel.

---

### Question 3

A security analyst suspects a rootkit is present on a workstation. When a full antivirus scan is run from within the operating system, no threats are detected. What is the MOST appropriate next step?

A. Update antivirus definitions and scan again.

B. Run the scan in Safe Mode.

C. Boot from trusted external media and scan the drive offline.

D. Reinstall the antivirus software.

**Correct Answer:** C

**Explanation:** A rootkit subverts OS-level reporting, meaning scans run from within the compromised OS cannot be trusted. Out-of-band scanning using trusted external media bypasses the compromised OS and can detect what in-OS tools cannot. Safe Mode still loads a potentially compromised kernel.

---

### Question 4

A software vendor releases a security update. After customers install the update, incident responders discover that the update package contained malware. The vendor confirms that the update was cryptographically signed with their legitimate certificate. Which type of attack BEST explains this incident?

A. Zero-day exploit

B. Man-in-the-middle attack

C. Supply chain attack

D. Code injection attack

**Correct Answer:** C

**Explanation:** A supply chain attack compromises the distribution channel rather than the end product directly. The attacker compromised the vendor's build or packaging process before signing occurred. The valid signature confirms the integrity of the delivery mechanism was not broken — the malicious code was inserted upstream of signing.

---

### Question 5

A user types their bank's URL correctly and is presented with a convincing but fraudulent login page. The URL in the browser address bar shows the correct bank domain. Which attack is MOST likely responsible?

A. Spear phishing

B. Typosquatting

C. Pharming

D. Credential stuffing

**Correct Answer:** C

**Explanation:** Pharming redirects legitimate web requests to fraudulent sites by poisoning the DNS cache or modifying the local hosts file. The user performs no suspicious action — they type the correct URL. Phishing requires a malicious link. Typosquatting relies on the user mistyping the URL.

---

### Question 6

An organization wants to reduce the risk that its employees will be deceived by fraudulent emails impersonating the company's own domain. Which combination of email authentication controls provides the MOST comprehensive protection?

A. SPF only

B. DKIM only

C. SPF and DKIM without DMARC

D. SPF, DKIM, and DMARC

**Correct Answer:** D

**Explanation:** SPF validates the sending IP, DKIM validates message integrity via cryptographic signature, and DMARC provides the enforcement policy that determines what receiving servers do with emails that fail SPF or DKIM. Without DMARC, there is no enforcement action. All three are required for comprehensive protection.

---

### Question 7

An employee receives a phone call from someone claiming to be from the corporate IT helpdesk. The caller says the employee's account will be locked in 10 minutes unless they immediately provide their credentials to complete an emergency security patch. Which social engineering technique is PRIMARILY being used?

A. Baiting

B. Vishing with authority and urgency

C. Pretexting with quid pro quo

D. Tailgating

**Correct Answer:** B

**Explanation:** This is vishing (voice phishing) using the combined psychological triggers of authority (IT helpdesk) and urgency (10-minute deadline). While pretexting is also present, the telephone delivery channel and the specific combination of authority plus urgency make B the most complete and accurate answer. Baiting uses physical or digital lures. Tailgating is a physical security attack.

---

### Question 8

A security team discovers that a trusted contractor's software library used in the company's payment processing application contains a backdoor that has been present for six months. The library was obtained from the official package repository. Which risk management concept would have BEST mitigated this risk before deployment?

A. Penetration testing the payment application

B. Requiring a Software Bill of Materials (SBOM) and scanning dependencies for known vulnerabilities

C. Implementing a web application firewall

D. Encrypting all payment data at rest

**Correct Answer:** B

**Explanation:** An SBOM provides an inventory of all software components including third-party libraries. Scanning those components against vulnerability databases and reviewing them before deployment addresses open-source supply chain risk directly. Penetration testing may not detect a well-hidden backdoor. A WAF and encryption address different threat vectors.

---

### Question 9

During a threat hunt, an analyst identifies a file with a creation date of three days ago in a system temp directory. The file name is `svchost.exe` but it is located in `C:\Users\Public\Temp\` rather than `C:\Windows\System32\`. Which category of indicator is this?

A. Network IoC

B. Behavioral IoC

C. File IoC

D. Host IoC

**Correct Answer:** D

**Explanation:** An unexpected executable in an unusual directory is a host-based indicator of compromise — it involves the file system and local configuration of the host. File IoCs specifically refer to hash values or known malicious signatures. Network IoCs involve traffic patterns. Behavioral IoCs involve process or execution chain anomalies. The location anomaly of a system-named binary is a host IoC.

---

### Question 10

A vulnerability researcher discovers a critical flaw in a widely used VPN product. The researcher notifies the vendor, who has not yet released a patch. An attacker simultaneously discovers and exploits the same flaw before any patch is available. How should this vulnerability be classified?

A. Known vulnerability

B. Zero-day exploit

C. Unpatched vulnerability

D. Legacy vulnerability

**Correct Answer:** B

**Explanation:** A zero-day exploit targets a vulnerability for which no patch exists at the time of exploitation. Once the vendor releases a patch, it transitions to a known/unpatched vulnerability. The defining characteristic of a zero-day is the absence of a vendor-supplied fix at the moment of exploitation, regardless of whether the researcher or attacker discovered it first.

---

Module 04 Quiz — End
