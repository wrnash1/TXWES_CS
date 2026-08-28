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

---

### Question 11

A user reports that their computer is running unusually slowly. Investigation reveals that a background process is consuming high CPU and GPU resources at night, generating outbound connections to a cryptocurrency mining pool. No files were encrypted and no data appears stolen. Which malware category BEST describes this threat?

A. Ransomware

B. Cryptominer

C. Spyware

D. Rootkit

**Correct Answer:** B

**Explanation:** Cryptomining malware (cryptominer/cryptojacker) hijacks system resources to mine cryptocurrency for the attacker's benefit without encrypting data or exfiltrating files. Ransomware encrypts data for extortion. Spyware silently collects and transmits information. A rootkit hides its presence but is not primarily defined by resource consumption for mining.

---

### Question 12

A threat actor sends an SMS text message to a bank customer that reads: "Your account has been locked. Click here to verify your identity: [link]." The link leads to a spoofed bank login page. Which attack type is this?

A. Vishing

B. Spear phishing

C. Smishing

D. Pharming

**Correct Answer:** C

**Explanation:** Smishing is phishing delivered via SMS (text message). Vishing uses voice/telephone calls. Spear phishing uses personalized email targeting specific individuals. Pharming redirects users through DNS or hosts file manipulation without requiring a link click — the user is redirected even when typing the correct URL.

---

### Question 13

An attacker compromises a widely used open-source JavaScript package by gaining access to a maintainer's account and inserting malicious code into a new version. Thousands of applications that automatically pull the latest version are now infected. Which attack type does this represent?

A. Zero-day exploit

B. Supply chain attack

C. Ransomware-as-a-Service

D. Watering hole attack

**Correct Answer:** B

**Explanation:** A supply chain attack compromises a target through a trusted third party — in this case, a legitimate package repository. The malicious code reaches victims through the normal software update mechanism. A zero-day targets an unknown vulnerability. RaaS is a criminal business model for distributing ransomware. A watering hole compromises websites that target users are likely to visit.

---

### Question 14

An organization's EDR platform detects that `PowerShell.exe` is executing encoded commands, connecting to an external IP address, and downloading additional payloads — all using tools already present on the operating system. No malware binary was written to disk. Which attacker technique does this describe?

A. Fileless malware using living-off-the-land binaries (LOLBins)

B. A worm propagating via network shares

C. A trojan masquerading as a legitimate application

D. A rootkit hiding its presence in the kernel

**Correct Answer:** A

**Explanation:** Fileless malware executes entirely in memory using legitimate OS tools (LOLBins) such as PowerShell, WMI, or certutil rather than writing executable files to disk. This evades traditional signature-based AV tools. A worm self-propagates across the network. A trojan disguises itself as legitimate software. A rootkit conceals itself at the OS or kernel level rather than operating via scripting engines.

---

### Question 15

A threat intelligence analyst observes outbound DNS queries from internal hosts to randomly generated domain names (e.g., `xkj3ma.evil.net`, `q9z2rt.evil.net`) occurring at regular intervals. No user interaction precedes the queries. Which malware behavior does this MOST likely indicate?

A. DNS cache poisoning by an external attacker

B. Command-and-control beaconing using a domain generation algorithm (DGA)

C. Pharming attack redirecting internal traffic

D. ARP poisoning on the internal network segment

**Correct Answer:** B

**Explanation:** Domain generation algorithms (DGAs) automatically generate large numbers of pseudo-random domain names that the malware uses for C2 communication, making it difficult to blocklist all possible C2 domains. The regular interval pattern is characteristic of automated beaconing. DNS cache poisoning and pharming alter DNS responses rather than generate new query domains. ARP poisoning operates at Layer 2 and does not involve DNS queries.

---

### Question 16

A security analyst reviews endpoint logs and finds that a process named `explorer.exe` spawned `cmd.exe`, which then launched `net.exe` to enumerate domain users. The parent-child process relationship is unexpected for legitimate system behavior. Which IoC category does this describe?

A. File IoC

B. Network IoC

C. Account IoC

D. Behavioral IoC

**Correct Answer:** D

**Explanation:** An unusual parent-child process relationship (such as Explorer spawning cmd which spawns net) is a behavioral indicator of compromise — it describes suspicious process execution patterns rather than a specific file hash, network connection, or account action. File IoCs involve hashes or file attributes. Network IoCs involve IP addresses, domains, or traffic patterns. Account IoCs involve login anomalies or unauthorized account creation.

---

### Question 17

An organization discovers that an attacker who compromised a workstation six weeks ago has been quietly collecting internal documents, screenshots, and credentials without triggering any alerts. The attacker has not yet exfiltrated or destroyed data. Which term BEST describes the stage the attacker is currently in?

A. Initial access

B. Lateral movement

C. Dwell time during post-exploitation reconnaissance

D. Exfiltration

**Correct Answer:** C

**Explanation:** Dwell time refers to the period an attacker remains undetected on a network after initial compromise. The described behavior — passive collection without triggering alerts — is consistent with post-exploitation reconnaissance during an extended dwell period. Initial access is the moment of first entry. Lateral movement involves moving between systems. Exfiltration has not yet occurred.

---

### Question 18

A user receives an email that appears to be an exact copy of a legitimate invoice email they received last week from a known vendor. The attachment has been replaced with a malicious file, but the sender address, subject line, and body text are identical. Which phishing variant is this?

A. Whaling

B. Clone phishing

C. Smishing

D. Vishing

**Correct Answer:** B

**Explanation:** Clone phishing duplicates a legitimate previously delivered email and replaces the attachment or link with a malicious version. The defining characteristic is that the email is a near-perfect copy of a real prior communication. Whaling targets executives. Smishing uses SMS. Vishing uses voice/phone.

---

### Question 19

After a ransomware incident, a forensic investigator determines the initial infection vector was a malicious macro in a Word document attached to a phishing email. The macro downloaded and executed a second-stage payload. Which sequence of MITRE ATT&CK tactics correctly describes this attack chain?

A. Reconnaissance → Lateral Movement → Exfiltration

B. Initial Access → Execution → Command and Control

C. Persistence → Privilege Escalation → Defense Evasion

D. Discovery → Collection → Impact

**Correct Answer:** B

**Explanation:** The phishing email with the malicious attachment represents Initial Access. The macro executing to download and run a second-stage payload represents Execution. The second-stage payload connecting to an attacker-controlled server represents Command and Control. The other options describe later-stage tactics that do not match the described infection sequence.

---

### Question 20

An attacker registers the domain `micros0ft-support.com` and sends emails directing users to this site for a fake security update. Which social engineering technique does the domain name illustrate?

A. Pharming

B. Typosquatting

C. DNS poisoning

D. Clone phishing

**Correct Answer:** B

**Explanation:** Typosquatting registers domain names that are visually similar to legitimate domains — in this case substituting the letter "o" with the numeral "0" to mimic `microsoft-support.com`. The goal is for inattentive users to follow the link without noticing the substitution. Pharming manipulates DNS or hosts files to redirect legitimate URLs. DNS poisoning alters DNS cache records. Clone phishing duplicates legitimate emails.

---

Module 04 Quiz — End
