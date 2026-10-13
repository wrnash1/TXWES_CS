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

---

### Question 11

An organization's EDR platform detects that a process named `svchost.exe` is running from the path `C:\Users\Public\svchost.exe` and is making outbound connections to an external IP address. Why is this detection significant, and what category of threat does this represent?

A. The process is a standard Windows service host and the detection is a false positive

B. The process is masquerading as a legitimate Windows process but running from an unusual path, indicating potential masquerading malware

C. The detection represents normal svchost behavior because svchost frequently connects to external IPs

D. The EDR has misconfigured signature rules and should be tuned to exclude this alert

**Correct Answer:** B

**Explanation:** The legitimate Windows `svchost.exe` runs from `C:\Windows\System32\`. When EDR detects a process with the same name running from a user-writable directory like `C:\Users\Public\`, it is a strong indicator of process masquerading — malware that uses a trusted process name to evade casual inspection. Outbound C2 connections from this path reinforce the finding. This is a behavioral detection that signature-based AV would not catch if the binary lacks a known signature. This technique maps to MITRE ATT&CK T1036 (Masquerading).

---

### Question 12

A Windows administrator runs the command `netstat -ano` on a server and observes a listening service on port 4444 that is associated with an unknown PID. When the administrator runs `tasklist` to identify the process, no process appears for that PID. What does this anomaly indicate?

A. The service is a standard Windows RPC endpoint that is not always visible in the task list

B. A rootkit may have hidden the process from the operating system's userland task enumeration

C. The port 4444 is reserved for Windows Update and is expected behavior

D. The netstat output is outdated and the connection has since closed

**Correct Answer:** B

**Explanation:** When `netstat` shows a listening port on a PID that does not appear in `tasklist`, a rootkit is the most likely explanation. Rootkits operate at a level below normal OS visibility — they hook system calls to hide specific processes from enumeration tools running in user space. This is why live forensics on potentially compromised systems require boot-from-clean-media analysis or EDR tools that use kernel-level drivers to detect hidden processes. Port 4444 has no standard Windows service association.

---

### Question 13

A security team discovers that their Windows domain's Group Policy is not being consistently applied to laptops because users are working from home and not connecting to the corporate VPN. Which technology allows centralized endpoint policy enforcement for off-network devices without requiring a VPN connection?

A. Active Directory Group Policy processed at next logon

B. Microsoft Intune MDM with cloud-based policy delivery

C. On-premises SCCM push installation triggered by VPN connection

D. Manual registry edits distributed via email instructions

**Correct Answer:** B

**Explanation:** Microsoft Intune (and cloud MDM platforms generally) deliver device management policies over the internet without requiring VPN connectivity. Devices communicate directly with the cloud management plane regardless of location. Active Directory Group Policy only applies when the device can reach a domain controller — which requires either direct network access or VPN. SCCM is primarily on-premises and depends on network connectivity. Manual registry edits are not scalable and are not a management platform.

---

### Question 14

An organization's patch management policy requires that all Critical CVSS vulnerabilities be patched within 30 days. A new Critical vulnerability is disclosed on a Monday. The affected vendor releases a patch on Thursday. The organization's change management process requires a two-week testing and approval cycle before production deployment. Will this organization meet its policy deadline?

A. Yes, because 30 days from disclosure allows sufficient time for testing and deployment

B. No, because the two-week testing cycle plus deployment time will likely exceed 30 days from patch release

C. Yes, because the clock starts when the patch is released, not when the vulnerability is disclosed

D. No, because Critical vulnerabilities require same-day patching under all standard frameworks

**Correct Answer:** A

**Explanation:** The 30-day window runs from vulnerability disclosure. The patch was released four days after disclosure (Thursday). A two-week (14-day) testing cycle starting Thursday would complete approximately 18 days after disclosure, leaving time for production deployment before the 30-day deadline — assuming no further delays. The key timing: disclosure (day 0) → patch release (day 4) → testing complete (day 18) → deployment window (days 19–30). This is tight but achievable. The organization should review whether two weeks of testing for critical patches is appropriate given the risk.

---

### Question 15

A Unified Endpoint Management (UEM) platform flags a managed smartphone because it has been jailbroken. The organization's mobile security policy requires that jailbroken devices be blocked from accessing corporate resources. Which technical enforcement mechanism implements this policy?

A. The MDM sends a remote wipe command to erase the device

B. The MDM enforces a compliance policy that blocks corporate app access or removes the management profile when jailbreak is detected

C. The MDM alerts the administrator, who manually revokes the user's Active Directory account

D. The MDM installs a monitoring agent that patches the jailbreak vulnerability

**Correct Answer:** B

**Explanation:** UEM/MDM platforms detect jailbreak indicators through the management agent and can automatically enforce compliance policies — blocking access to corporate email, removing managed applications, or removing the enrollment profile. This is an automated response that does not require manual intervention. Remote wipe erases the device entirely, which is a more drastic action than blocking access. Manual AD revocation is slow and does not address device access at the mobile layer. MDM cannot patch a jailbroken device.

---

### Question 16

A security engineer is implementing application allowlisting using Windows Defender Application Control (WDAC). During testing, a legitimate vendor application fails to launch because its executable was updated and the new binary hash is not yet in the allowlist. Which allowlisting policy option would reduce this disruption while maintaining security?

A. Switch to signature-based allowlisting using the vendor's code-signing certificate

B. Disable allowlisting for all applications from that vendor

C. Add the specific binary hash of the new version to the allowlist and remove the old hash

D. Configure WDAC in audit mode, which permits all applications while logging violations

**Correct Answer:** A

**Explanation:** Code-signing certificate-based allowlisting permits any application signed by a trusted vendor certificate rather than requiring a specific binary hash. This means that when the vendor releases a new version and signs it with the same certificate, the new binary is automatically permitted without policy updates. Hash-based policies (option C) require updating the allowlist with every new binary — operationally intensive for frequently updated applications. Disabling allowlisting for a vendor removes the control entirely. Audit mode permits all applications and provides no active protection.

---

### Question 17

An employee's laptop is enrolled in MDM and is reported stolen. The device is configured with BitLocker, TPM, and a PIN requirement, and is enrolled in Microsoft Intune. The employee's manager asks the security team to remotely wipe the device. What is the MOST important step the security team should take BEFORE issuing the remote wipe command?

A. Confirm that BitLocker is enabled and the recovery key is stored in Azure AD

B. Preserve a forensic image of the device's current state if the device may be evidence in a legal proceeding

C. Revoke the employee's Active Directory credentials to prevent use of their account

D. Notify local law enforcement before any remote commands are issued

**Correct Answer:** B

**Explanation:** If the theft may involve criminal charges or civil litigation, the device's content could be digital evidence. Issuing a remote wipe before evidence is preserved could destroy evidence and create legal liability for the organization. The security team should evaluate whether forensic preservation of the device state is required before wiping. Account credential revocation is also important but does not need to precede the remote wipe decision. BitLocker status is relevant to data protection risk assessment. Law enforcement notification is situational, not universally required before a remote wipe.

---

### Question 18

Secure Boot is enabled on a laptop. A sophisticated attacker installs a modified bootloader on the device's EFI partition that loads before the OS. What does Secure Boot do when the laptop is next powered on?

A. Secure Boot ignores unsigned bootloaders and proceeds with normal startup

B. Secure Boot verifies the bootloader's digital signature against keys stored in UEFI firmware and refuses to boot if the signature is invalid

C. Secure Boot notifies the user by email that an unauthorized bootloader was detected

D. Secure Boot boots into a recovery environment and automatically restores the original bootloader

**Correct Answer:** B

**Explanation:** Secure Boot verifies that each component of the boot sequence — bootloader, OS loader, and drivers — is signed with a certificate trusted by the UEFI firmware's Secure Boot database (db). If the attacker's modified bootloader is not signed with a trusted key, Secure Boot will refuse to execute it and halt the boot process. This directly prevents bootkits and rootkits that attempt to persist by replacing or modifying the boot chain. It does not send notifications, auto-restore files, or silently ignore the unsigned component.

---

### Question 19

A company wants to ensure that endpoint configurations do not drift from the approved CIS Benchmark baseline over time. Which tool category is SPECIFICALLY designed to detect and remediate configuration drift on an ongoing basis?

A. Vulnerability scanner

B. Security Configuration Management (SCM) / Compliance scanning tool

C. Endpoint Detection and Response (EDR)

D. Security Information and Event Management (SIEM)

**Correct Answer:** B

**Explanation:** Security Configuration Management tools (also called compliance scanners or configuration assessment tools — examples include CIS-CAT, Microsoft Endpoint Configuration Manager, and similar platforms) continuously compare endpoint configurations against defined security baselines and report or remediate drift. A vulnerability scanner identifies software vulnerabilities (CVEs) but does not assess configuration settings like password policy or unnecessary services. EDR detects malicious activity but does not assess configuration compliance. A SIEM aggregates logs but does not assess system configuration.

---

### Question 20

An attacker executes a Living-off-the-Land Binaries (LOLBin) technique by using `certutil.exe` — a legitimate Windows certificate management tool — to download a malicious payload from an external server. Traditional antivirus does not flag this activity. Which detection approach would MOST effectively identify this technique?

A. Update AV signatures to block certutil.exe entirely

B. Behavioral detection in EDR that flags certutil.exe making outbound HTTP/HTTPS connections to external IPs

C. Apply a firewall rule blocking all traffic from certutil.exe

D. Disable certutil.exe on all workstations to prevent its misuse

**Correct Answer:** B

**Explanation:** LOLBin attacks abuse legitimate, trusted system tools to evade signature-based detection. The tool itself (certutil.exe) is legitimate, so blocking or removing it would break legitimate certificate management operations. EDR behavioral detection identifies anomalous use of trusted tools — certutil.exe making outbound connections to non-Microsoft external IPs is not normal behavior and is a detectable behavioral anomaly. A perimeter firewall cannot filter based on which process initiated traffic without application-aware controls. Blocking certutil.exe entirely would break certificate enrollment and revocation checking.

---

Module 08 Quiz — End
