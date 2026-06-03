# Quiz: Module 08 — Endpoint Security

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

### Question 1

After a security incident, an analyst needs to determine the exact sequence of events on a compromised workstation — every process that executed, every file that was written, and every network connection that was made — over the past 72 hours. Which tool BEST provides this capability?

A. Traditional signature-based antivirus

B. Host-based IDS

C. Endpoint Detection and Response (EDR)

D. SIEM

**Correct Answer:** C

**Explanation:** EDR continuously records endpoint telemetry — process executions, file operations, registry changes, and network connections — and retains this data for threat hunting and forensic investigation. Traditional AV detects malware at point of execution but does not maintain a continuous activity record. A host-based IDS generates alerts on specific signatures but does not provide a complete forensic timeline. A SIEM aggregates logs from multiple sources but depends on what each source logs — an endpoint's EDR agent provides richer and more granular endpoint data than a standard Windows event log forwarded to a SIEM.

---

### Question 2

An organization wants to prevent any application that has not been explicitly approved from executing on its ATM kiosks. The ATMs run a limited set of fixed applications that rarely change. Which control BEST meets this requirement?

A. Next-generation antivirus with behavioral detection

B. Application allowlisting

C. Host-based IPS

D. Signature-based antivirus

**Correct Answer:** B

**Explanation:** Application allowlisting permits only explicitly approved executables and blocks all others by default — including unknown malware, zero-day exploits, and any unauthorized software. In a controlled environment like ATM kiosks where the application set is small and stable, the operational overhead of maintaining the allowlist is manageable. NGAV and IPS detect suspicious behavior but operate on a deny-known-bad or detect-suspicious model — they cannot guarantee that only approved applications run.

---

### Question 3

A laptop with BitLocker encryption and TPM integration is stolen from an employee's car. The drive is removed and inserted into a different computer. What is the status of the data?

A. The data is accessible because BitLocker uses a software key stored in the OS

B. The data is accessible once the attacker enters the Windows login password

C. The data is encrypted and unreadable because the TPM on the original laptop holds the key

D. The data is accessible because removing the drive disables the encryption

**Correct Answer:** C

**Explanation:** BitLocker with TPM integration stores the volume encryption key in the TPM chip on the original laptop. When the drive is connected to a different system, that system's TPM does not have the key — the drive remains encrypted and the data is unreadable. The Windows login password is separate from the disk encryption key. The drive's encryption state does not change when it is removed.

---

### Question 4

A new ransomware variant is discovered that uses a polymorphic engine to modify its own code, producing a unique binary hash for every infection. Traditional antivirus reports no threats. Which detection approach would MOST likely identify this threat?

A. Updating antivirus signatures within 24 hours

B. Behavioral detection that identifies the mass file encryption activity pattern

C. File hash comparison against known threat databases

D. Port scanning to detect ransomware command-and-control traffic

**Correct Answer:** B

**Explanation:** Polymorphic malware specifically defeats signature-based and hash-based detection by producing unique binaries. Behavioral detection — identifying the pattern of reading files and rewriting them with encryption — does not depend on knowing the malware's signature. The behavioral pattern of ransomware (mass file read, encrypt, rename with new extension) is detectable by NGAV and EDR even for completely novel samples. Updating signatures does not help against a previously unknown variant. Port scanning detects network activity but would not catch encryption occurring on the local file system.

---

### Question 5

An organization's security team receives a report of a vulnerability with a CVSS score of 6.5 (Medium severity). The same day, a different vulnerability with a CVSS score of 5.8 (Medium severity) is added to the CISA Known Exploited Vulnerabilities catalog. Which should be patched first?

A. The CVSS 6.5 vulnerability because it has a higher severity score

B. The CVSS 5.8 vulnerability because it is being actively exploited in the wild

C. Both simultaneously since both are Medium severity

D. Neither — Medium severity vulnerabilities do not require emergency patching

**Correct Answer:** B

**Explanation:** The CISA KEV catalog indicates that a vulnerability is currently being actively exploited by threat actors. Active exploitation is a higher-priority indicator than CVSS score alone — CVSS measures theoretical severity, while the KEV catalog confirms real-world attack activity. The 5.8 KEV vulnerability represents a higher immediate risk than the 6.5 non-exploited vulnerability. Organizations should treat KEV-listed vulnerabilities as requiring urgent remediation regardless of their CVSS score.

---

### Question 6

A company issues corporate smartphones to all employees and allows personal use within an acceptable use policy. IT needs full visibility and control over the device, including the ability to locate and wipe the entire device if lost. Which mobile device management model is MOST appropriate?

A. MAM

B. BYOD with app containerization

C. MDM

D. COPE with MAM-only enrollment

**Correct Answer:** C

**Explanation:** MDM (Mobile Device Management) provides full device management — policy enforcement, geolocation, full remote wipe, application management, and complete visibility. This is appropriate for corporate-owned devices where the organization has full authority over the device. MAM manages only specific applications and cannot wipe the entire device. COPE (Corporate-Owned Personally Enabled) is actually managed via MDM — but if the question is specifically asking about the management model providing full device wipe capability, MDM is the direct answer.

---

### Question 7

An employee connects their personal laptop to a coffee shop Wi-Fi network. The laptop's corporate-issued security software includes an antivirus, but the host-based firewall has been disabled. Which threat does the disabled host-based firewall MOST directly expose the employee to?

A. Malware delivered via drive-by download from a web browser

B. Unsolicited inbound connections from other devices on the same network

C. Phishing emails delivered to the employee's inbox

D. Keylogging by a rogue access point

**Correct Answer:** B

**Explanation:** A host-based firewall blocks unsolicited inbound connection attempts from other devices — a particularly relevant threat on shared public networks where other connected devices may be malicious. Without the host-based firewall, the laptop's open ports are accessible to any other device on the coffee shop Wi-Fi. Antivirus addresses malware delivered by file or web content. Phishing is an email-layer attack not affected by the host firewall. Keylogging via a rogue access point is a network-layer attack against traffic, not against the host's open ports.

---

### Question 8

A CIS Benchmark Level 1 control recommends disabling the LLMNR (Link-Local Multicast Name Resolution) protocol on Windows workstations. What is the PRIMARY security rationale for this recommendation?

A. LLMNR uses unencrypted DNS traffic that can be intercepted

B. LLMNR queries can be hijacked to capture NTLM credential hashes via responder tools

C. LLMNR consumes excessive network bandwidth

D. LLMNR is incompatible with modern Active Directory environments

**Correct Answer:** B

**Explanation:** LLMNR is exploited by tools like Responder, which listen for LLMNR broadcast queries and respond with a spoofed answer, redirecting the client's authentication request to the attacker's system. The client's NTLM credentials are then captured during the authentication attempt. These captured hashes can be cracked or used in Pass-the-Hash attacks. Disabling LLMNR eliminates this attack vector. It is a well-known and frequently exploited protocol for credential harvesting in internal networks.

---

### Question 9

Employees at a law firm use personal iPhones to access corporate email and document systems. The firm wants to protect client documents stored in corporate applications without restricting what employees do with their personal photos, contacts, or personal apps. Which approach BEST meets this requirement?

A. Enroll all devices in full MDM with remote wipe capability

B. Require all employees to use corporate-issued devices only

C. Deploy MAM to containerize corporate applications and their data

D. Implement a VPN requirement and rely on server-side access controls

**Correct Answer:** C

**Explanation:** MAM (Mobile Application Management) manages only the corporate application container — protecting corporate documents, email, and data within those applications while leaving the employee's personal content untouched. If a device is compromised or an employee leaves, only the corporate container can be wiped. Full MDM would give the firm visibility and control over personal content, creating privacy concerns and limiting employee willingness to enroll. VPN and server-side controls do not protect data already stored on the device.

---

### Question 10

A security team is hardening a new Windows server. According to the CIS Benchmark, which of the following is a Level 1 hardening action?

A. Enabling all Windows features for maximum compatibility

B. Disabling the Guest account and default local administrator account

C. Installing a real-time antivirus solution on every service

D. Requiring biometric authentication for all remote desktop sessions

**Correct Answer:** B

**Explanation:** Disabling default accounts — the Guest account and the default local administrator account (or renaming and disabling it) — is a fundamental Level 1 CIS hardening recommendation. Default accounts have well-known names that attackers target in credential attacks and brute-force attempts. Enabling all Windows features increases attack surface rather than reducing it. Installing AV on every service is not a specific CIS control. Biometric RDP authentication is not a standard CIS Level 1 recommendation and is not supported by default Windows RDP.

---

Module 08 Quiz — End
