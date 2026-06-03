# Quiz: Module 16 — PenTest+ PT0-002 Exam Preparation and Capstone

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

This quiz serves as the 20-question capstone assessment for CIS-4333, covering all PT0-002 exam domains. Each question is worth 5 points. Time limit: 45 minutes. This assessment is administered under closed-book conditions.

---

## Questions

**Question 1**

A penetration tester has authorization to test a company's web application at app.example.com. During testing, a JavaScript file reveals an internal API endpoint at api.internal.example.com on a private IP. The tester successfully reaches the internal API from the public internet. What is the FIRST action the tester should take?

A. Exploit the internal API endpoint to demonstrate the full impact.

B. Verify whether api.internal.example.com falls within the authorized scope and consult the scope document before proceeding.

C. Stop the engagement and contact law enforcement since an internal endpoint is exposed.

D. Ignore the finding since internal endpoints are not part of external web application testing.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Exploiting a system before confirming it is in scope is a potential CFAA violation even within an otherwise authorized engagement. Scope confirmation is the first step.
- B is correct. The tester must determine whether the internal API is within the authorized scope. If the scope document includes the IP range containing the API, it may be in scope. If not, the finding is documented as an out-of-scope informational note and the client is notified.
- C is incorrect. An exposed internal endpoint is a finding for the client, not a law enforcement matter. The tester's role is to document and report, not escalate to law enforcement.
- D is incorrect. Ignoring a significant finding — especially one that may be in scope — fails the client and the professional obligation of the engagement.

---

**Question 2**

An attacker compromises a developer's workstation and finds a `.git/config` file containing: `url = https://access_token:ghp_[redacted]@github.com/corp/private-repo.git`. What is the MOST significant security risk this represents?

A. The git configuration file is corrupted and the repository will fail to sync.

B. The embedded GitHub Personal Access Token can provide access to the private repository and potentially other repositories the developer has access to.

C. The attacker has found the developer's SSH private key.

D. The `.git/config` file exposes the developer's commit history.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The configuration format is valid — it embeds the token in the remote URL. This is a security issue, not a corruption issue.
- B is correct. GitHub Personal Access Tokens embedded in git remote URLs persist in the configuration and provide access equivalent to the user's GitHub permissions. They can access any repository the user can access, not just the one in the config.
- C is incorrect. The token in the URL is a Personal Access Token (PAT), not an SSH private key. SSH keys have a distinct format.
- D is incorrect. Commit history is available through the git log, not exposed specifically by the config file. The config file's security risk is the embedded credential.

---

**Question 3**

During a Kerberoasting attack, a tester requests a service ticket for SVC_SQL using their low-privilege domain account. Which component of the Kerberos protocol is cracked offline?

A. The TGT (Ticket Granting Ticket) encrypted with the krbtgt account's NTLM hash

B. The TGS (Ticket Granting Service ticket) encrypted with the service account's NTLM hash

C. The AS-REQ pre-authentication hash from the requesting user's account

D. The session key negotiated between the KDC and the client during initial authentication

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The TGT is encrypted with the krbtgt hash. Kerberoasting does not target the TGT — that is a different attack (Golden Ticket). Kerberoasting targets service tickets.
- B is correct. Kerberoasting requests a TGS (service ticket) for an SPN-registered service account. The ticket is encrypted with the service account's NTLM hash. An attacker with any domain account can request this ticket and crack it offline to recover the service account's password.
- C is incorrect. AS-REQ pre-authentication hash cracking is AS-REP Roasting, a different attack that targets accounts with pre-authentication disabled.
- D is incorrect. Session keys are ephemeral values negotiated per session and are not stored or accessible for offline cracking.

---

**Question 4**

A penetration tester runs the following Nmap command: `nmap -sS -sV -p 80,443,8080,8443 -oA report_prefix 10.10.10.0/24`. Which of the following best describes the outputs produced?

A. A single XML file containing only the hosts with ports 80, 443, 8080, and 8443 open.

B. Three output files (normal .nmap, XML .xml, and greppable .gnmap) containing SYN scan results with service version detection for the four specified ports.

C. A single HTML report with service banners for the /24 subnet.

D. Results only for hosts that responded to ICMP ping (host discovery only).

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. `-oA` produces three output formats: normal (`.nmap`), XML (`.xml`), and greppable (`.gnmap`). It does not produce a single XML file. Additionally, Nmap output includes all scanned hosts, not only those with specific ports open.
- B is correct. `-sS` is a TCP SYN scan. `-sV` adds service version detection. `-p 80,443,8080,8443` limits scanning to these four ports. `-oA report_prefix` generates all three output formats.
- C is incorrect. Nmap does not generate HTML output natively with `-oA`. An `.xsl` stylesheet can convert XML to HTML, but this is not a standard `-oA` output.
- D is incorrect. Nmap performs host discovery by default, but `-sS` and `-sV` perform port scanning and version detection, not just host discovery.

---

**Question 5**

LLMNR (Link-Local Multicast Name Resolution) poisoning using Responder captures NTLMv2 hashes. Which of the following best describes how the captured hashes are used in a Pass-the-Hash attack?

A. NTLMv2 hashes can be passed directly using Impacket psexec, the same as NTLMv1 hashes.

B. NTLMv2 hashes cannot be used in Pass-the-Hash attacks directly. They are cracked offline with Hashcat to recover the cleartext password, which is then used for authentication.

C. NTLMv2 hashes are used in Pass-the-Ticket attacks but not Pass-the-Hash.

D. NTLMv2 hashes can be relayed in real-time but cannot be cracked offline.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. NTLMv2 hashes cannot be directly passed. Pass-the-Hash uses NTLM (v1-format) credential material — specifically the NT hash. NTLMv2 is a challenge-response hash and cannot be directly injected into the authentication protocol.
- B is correct. NTLMv2 challenge-response hashes captured by Responder are offline cracking targets (Hashcat mode 5600). They are not directly passable. The NT hash (not NTLMv2) is used in Pass-the-Hash attacks. NTLMv2 hashes can be relayed (NTLM relay attacks) but not passed directly.
- C is incorrect. Pass-the-Ticket uses Kerberos tickets, not NTLM hashes of any version.
- D is incorrect. NTLMv2 hashes can absolutely be cracked offline. That is the primary use case for Responder in a penetration test: capture and crack to recover domain credentials.

---

**Question 6**

A web application returns the following response to a test request: `SELECT * FROM users WHERE email='test@test.com' -- ' AND password='test'` visible in a 500 error. Which vulnerability is demonstrated and what is its MOST significant risk?

A. Reflected XSS — risk is session hijacking.

B. Verbose error messages revealing SQL query structure — risk is aiding SQL injection exploitation.

C. SSRF — risk is access to internal network resources.

D. Insecure direct object reference — risk is accessing another user's data.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The output is a SQL query in an error message, not a JavaScript payload. This is not XSS.
- B is correct. Verbose error messages that reveal SQL query structure enable an attacker to understand the database schema and craft targeted SQL injection payloads. This is OWASP Top 10 A05 — Security Misconfiguration. The visible SQL also confirms that SQL injection is possible (the `--` comment truncated the password check). The most significant risk is facilitating full SQL injection exploitation.
- C is incorrect. SSRF causes the server to make requests to internal resources. The output shown is a SQL error message, not evidence of an outbound server request.
- D is incorrect. IDOR involves accessing another user's object by manipulating identifiers. The output shows a SQL error exposing query structure, not an object access.

---

**Question 7**

A tester discovers that a company's internal web application is vulnerable to SSRF, and the company uses AWS EC2 for hosting. The SSRF can reach the IMDSv1 endpoint. Which sequence of requests would retrieve the temporary IAM role credentials?

A. `GET /?url=http://169.254.169.254/latest/meta-data/` then `GET /?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/` then `GET /?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE-NAME]`

B. `GET /?url=http://169.254.169.254/v1/credentials/` then parse the JSON response.

C. `PUT /?url=http://169.254.169.254/latest/api/token` with TTL header, then `GET /?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/`

D. `GET /?url=http://169.254.169.254/latest/user-data/` returns all instance credentials.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct. The three-step enumeration: first list available metadata categories, then navigate to IAM security credentials, then specify the role name to retrieve the temporary credentials (Access Key ID, Secret Access Key, Token).
- B is incorrect. `/v1/credentials/` is not an IMDSv1 path. This resembles HashiCorp Vault syntax.
- C is incorrect. The IMDSv2 flow requires a PUT to `/latest/api/token` with a `X-aws-ec2-metadata-token-ttl-seconds` header. This is the mitigated version. The scenario specifies IMDSv1, which does not require a session token. IMDSv1 is directly accessible without the PUT step.
- D is incorrect. `/latest/user-data/` contains instance user data (startup scripts, configuration) but does not directly return IAM credentials.

---

**Question 8**

A client asks the penetration testing firm to exclude a finding from the final report because the client says "we've already fixed it." The fix was applied the day before the report was scheduled. The tester has not re-tested the fix. What is the MOST appropriate response?

A. Remove the finding since the client has authority over their own report.

B. Keep the finding in the report, note the client's claimed remediation, and offer to perform a re-test. Update the finding status to "Remediation Claimed — Unverified" until re-testing confirms the fix.

C. Remove the finding and note in the engagement record that it was removed at client request.

D. Change the finding's severity from Critical to Informational since the client believes it is fixed.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The client does not have authority to direct removal of confirmed findings. The penetration test report reflects what was found during the testing period. Removing confirmed findings misrepresents the security posture at the time of assessment.
- B is correct. The finding remains in the report (it was confirmed during the assessment period). The client's claimed remediation is noted. A re-test offer allows the tester to verify and update the finding status to "Remediated — Confirmed" with evidence. This is the professional standard approach.
- C is incorrect. Removing the finding and noting it was removed at client request creates a misleading report and a liability concern — the final report would not accurately represent the assessment findings.
- D is incorrect. Changing severity based on an unverified client claim is not appropriate. Severity reflects the vulnerability's characteristics, not the claimed remediation status.

---

**Question 9**

Which PT0-002 exam domain would MOST directly address the question: "A tester uses sqlmap --dbs to enumerate database names and recovers a list of databases including `customer_pii`. What should the tester do next?"

A. Domain 1 — Planning and Scoping: The tester must confirm the database is within the authorized scope.

B. Domain 3 — Attacks and Exploits: The tester should proceed to dump the customer_pii database.

C. Domain 4 — Reporting and Communication: The tester should write the finding immediately.

D. Domain 5 — Tools and Code Analysis: The tester should verify the sqlmap command syntax.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct. The FIRST action when discovering a database containing PII is to confirm whether accessing its contents is within the authorized scope and whether extracting PII is explicitly authorized. The scope may authorize SQL injection testing without permitting actual data extraction. Domain 1 principles apply.
- B is incorrect. Dumping the database without confirming authorization violates CFAA scope requirements and may create liability for unauthorized access to PII. Domain 3 technique knowledge is relevant, but the priority is the Domain 1 authorization question.
- C is incorrect. Writing the finding is a Domain 4 activity that comes after the exploitation phase. It does not answer what the tester should do next when they have the list of databases.
- D is incorrect. Tool syntax verification (Domain 5) is not the issue here. The command worked — sqlmap returned database names. The issue is the authorization and scope question of what to do with the access.

---

**Question 10**

A penetration tester intercepts a JWT in a Bearer token header: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiam9obiIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzAwMDAwMDAwfQ.[signature]`. The tester decodes the payload to find `{"user": "john", "role": "user", "exp": 1700000000}`. What test should the tester attempt FIRST?

A. Attempt to modify `"role": "user"` to `"role": "admin"` and re-sign with the RS256 public key using HS256 (algorithm confusion).

B. Submit the token without modification to test if the server accepts it despite the expired `exp` timestamp.

C. Use Hashcat to brute-force the RS256 private key.

D. Decode the signature to extract the encryption key.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. The algorithm confusion attack is a valid test, but it is not the first test to attempt. The simplest test — checking if expiration is enforced — should come first. The `exp: 1700000000` is November 14, 2023. If the current date is after that, the token is expired. Testing whether the server rejects expired tokens is a fast, risk-free initial check.
- B is correct. Verifying whether the server enforces the `exp` claim is the simplest and least invasive test. Many JWT implementations fail to validate expiration. Testing with an expired token costs nothing and reveals a significant vulnerability if the server accepts it.
- C is incorrect. RS256 uses asymmetric cryptography. The private key cannot be brute-forced from the signature — the private key is never transmitted. Hashcat can brute-force HS256 shared secrets but not RSA private keys.
- D is incorrect. JWT signatures are not encrypted — they are signed. The signature is a hash (or RSA/ECDSA operation) of the header and payload. Decoding it does not reveal a key.

---

**Question 11**

A company has implemented multi-factor authentication (MFA) for all VPN connections. During an authorized penetration test, the tester sends a phishing email to an employee containing a link to a reverse-proxy phishing page that transparently proxies the company's real login page. The employee enters their credentials and MFA code. The phishing page captures the session cookie. What class of attack is this, and what is the MOST significant remediation?

A. Credential stuffing — remediation is to require longer passwords.

B. MFA bypass via adversary-in-the-middle (AiTM) phishing — remediation is to implement phishing-resistant MFA (FIDO2/hardware keys).

C. Brute force attack — remediation is to implement account lockout after failed attempts.

D. Pass-the-hash — remediation is to enforce NTLMv2.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Credential stuffing uses previously breached username/password combinations. This attack captures real-time credentials through deception, not through reusing breached lists.
- B is correct. AiTM phishing proxies the real authentication page, capturing both credentials and the MFA code or post-authentication session cookie. The MFA code is used in real-time against the real site, bypassing MFA entirely. FIDO2/hardware security keys are cryptographically bound to the legitimate origin domain and cannot be phished by a proxy, making them the strongest remediation.
- C is incorrect. Brute force attacks attempt many password combinations. This attack captures real credentials through social engineering, not through brute force.
- D is incorrect. Pass-the-hash is a Windows Active Directory attack using NTLM credential material. The attack described is web-based credential phishing, not NTLM.

---

**Question 12**

A client's security team asks why the penetration test report's CVSS Base Score for a finding is 9.8 but the tester recommends treating it as High (7.0–8.9) in the remediation prioritization. Which explanation is MOST accurate?

A. The tester made a calculation error — CVSS scores cannot be adjusted for context.

B. The environmental score, reflecting that the vulnerable system is isolated from sensitive data and has network access controls, reduces the effective risk to the organization.

C. The tester disagrees with the CVSS methodology and is applying a custom scale.

D. A 9.8 is always treated as Critical regardless of environmental factors.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Environmental CVSS metrics exist specifically to allow the base score to be adjusted for the specific deployment context. The framework explicitly supports this.
- B is correct. Environmental metrics (Modified CIA Requirements) allow the base score to be adjusted downward when the specific deployment reduces the actual risk. A 9.8 vulnerability in an isolated, non-internet-facing development system with no sensitive data has a meaningfully lower environmental score than the same vulnerability on a public-facing production system.
- C is incorrect. Environmental CVSS scoring is the standard methodology, not a custom scale. The tester is applying CVSS correctly.
- D is incorrect. CVSS base scores are not mandatory override ratings. The full CVSS framework includes environmental adjustments specifically to avoid this scenario.

---

**Question 13**

Which tool is BEST suited for visualizing Active Directory attack paths, identifying high-value targets, and determining the shortest route from a compromised standard user account to Domain Admin?

A. Mimikatz

B. Impacket

C. BloodHound

D. Responder

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. Mimikatz is a credential extraction tool — it dumps password hashes, Kerberos tickets, and cleartext credentials from Windows memory. It does not visualize attack paths.
- B is incorrect. Impacket is a Python toolkit for Windows network protocol implementation — psexec, secretsdump, smbclient. Excellent for exploitation, not for attack path visualization.
- C is correct. BloodHound ingests Active Directory data (collected by SharpHound or BloodHound.py) and visualizes the relationships between users, groups, computers, and permissions as a directed graph. It identifies attack paths from any compromised account to Domain Admin, helping testers and defenders understand the most critical privilege escalation risks.
- D is incorrect. Responder captures NTLM hashes via LLMNR/NBT-NS poisoning. It is a credential capture tool, not an AD visualization tool.

---

**Question 14**

A penetration tester running Nikto against a web server receives this output line: `OSVDB-3268: /backup/: Directory indexing found`. What is the security significance of this finding?

A. The server has a backup process that creates temporary files vulnerable to data tampering.

B. Directory indexing on `/backup/` allows unauthenticated listing and downloading of files in the backup directory, potentially exposing database dumps, configuration files, and application backups.

C. The OSVDB-3268 identifier indicates this is a zero-day vulnerability with no available patch.

D. Directory indexing is a low-severity informational finding with no security impact.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Directory indexing does not describe the backup process itself — it describes the web server's behavior of listing file contents when no index file exists. The security issue is file exposure, not tampering.
- B is correct. Directory indexing on a `/backup/` directory is a high-severity finding because backup directories often contain database dumps (`.sql`), configuration files (`.conf`, `.env`), and archived source code (`.zip`, `.tar.gz`) — all with sensitive content. Unauthenticated access to a `/backup/` directory listing frequently leads to critical data exposure.
- C is incorrect. OSVDB-3268 is a database identifier for a known configuration issue, not a zero-day. Directory indexing is a web server misconfiguration, not a software vulnerability.
- D is incorrect. Directory indexing on any sensitive directory is not low severity. On a `/backup/` path specifically, the realistic impact (database credential exposure, configuration file access, source code disclosure) is typically High or Critical depending on what files are present.

---

**Question 15**

During a penetration test, the tester uses `smbclient -L //10.10.5.100 -N` and finds an open share called `ADMIN$`. The tester connects and lists files. What does this finding indicate?

A. The system has an IPC$ share, which is normal for Windows systems.

B. Null session access to ADMIN$ is possible — the system allows unauthenticated listing of the administrative share, which provides access to the Windows system drive.

C. The system is running a Linux Samba server with default guest access.

D. The tester has enumerated a normal Windows administrative share with no security significance.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. IPC$ is a different share type used for inter-process communication. ADMIN$ is the administrative share mapped to the Windows system directory.
- B is correct. `ADMIN$` maps to `C:\Windows`. Null session (unauthenticated) access to ADMIN$ should not be possible in a properly configured Windows environment. If a null session can connect to and list ADMIN$, the system has a significant access control misconfiguration, potentially allowing file system access to the Windows directory without credentials.
- C is incorrect. ADMIN$ is a Windows administrative share name. Linux Samba servers can create shares, but ADMIN$ is specifically a Windows default administrative share concept.
- D is incorrect. ADMIN$ with null session access is not "normal with no security significance." Administrative shares should require authentication. Unauthenticated access to ADMIN$ is a significant misconfiguration.

---

**Question 16**

Which of the following combinations represents BOTH the tool for physical RFID card cloning AND the tool for wireless WPA2 handshake capture?

A. Proxmark3 and Airodump-ng

B. Flipper Zero and Hashcat

C. HID Global and Aircrack-ng

D. RFID Reader Pro and Kismet

**Correct Answer:** A

**Distractor Analysis:**

- A is correct. The Proxmark3 is the standard professional RFID assessment tool used for reading and cloning RFID cards. Airodump-ng is the capture component of the Aircrack-ng suite, used to capture 802.11 traffic including WPA2 four-way handshakes.
- B is incorrect. The Flipper Zero is a multi-purpose portable security tool that can read RFID cards, but it is not the primary professional assessment tool (Proxmark3 is). Hashcat is the cracking tool, not the capture tool.
- C is incorrect. HID Global is the manufacturer of HID Prox access control systems — not a security testing tool. Aircrack-ng cracks WPA2 hashes but does not capture packets; Airodump-ng does the capture.
- D is incorrect. "RFID Reader Pro" is not a standard security assessment tool name. Kismet is a wireless network detector and packet sniffer, not specifically optimized for WPA2 handshake capture (though it can capture packets).

---

**Question 17**

A penetration tester is using Metasploit's `auxiliary/scanner/smb/smb_ms17_010` module. What is this module checking for?

A. Whether the target is vulnerable to EternalBlue (MS17-010), the SMB vulnerability used by WannaCry and NotPetya.

B. Whether the SMB service is running on the target.

C. Whether the target has default SMB credentials.

D. Whether SMB signing is disabled on the target, enabling relay attacks.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct. `smb_ms17_010` is the Metasploit scanner module that checks whether a target is vulnerable to MS17-010 (EternalBlue). It sends specific probes to detect the SMBv1 vulnerability that allows unauthenticated remote code execution. This vulnerability was famously exploited by WannaCry and NotPetya ransomware.
- B is incorrect. Checking whether SMB is running is a basic port scan (port 445). The `smb_ms17_010` module specifically checks for the EternalBlue vulnerability, not just SMB availability.
- C is incorrect. Default credential testing is handled by modules like `smb_login`. `smb_ms17_010` checks for the specific protocol-level vulnerability, not credential weaknesses.
- D is incorrect. SMB signing detection is handled by `smb_signing` auxiliary module. `smb_ms17_010` specifically targets the MS17-010 buffer overflow vulnerability.

---

**Question 18**

An OT security assessment reveals that the SCADA server (Windows Server 2012 R2, end-of-support) is directly connected to both the corporate IT network and the operational control network. The SCADA server has Remote Desktop Protocol (RDP) exposed to the corporate IT network for remote operations. What is the MOST significant risk this configuration presents?

A. Windows Server 2012 R2 may not support modern TLS versions, degrading HTTPS encryption.

B. An IT-side attacker who compromises the SCADA server via RDP gains a direct pivot point to send commands to operational equipment on the OT network, potentially causing physical consequences.

C. RDP uses bandwidth-intensive graphical connections that degrade SCADA system performance.

D. The end-of-support status means vendor support calls cannot be made.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. TLS version support is a concern but is not the MOST significant risk in an IT/OT bridged architecture. The primary risk is the attack path to operational equipment.
- B is correct. The SCADA server bridges the IT and OT networks. An attacker with access to the corporate IT network who exploits RDP (or any vulnerability on the SCADA server) now has a network-adjacent position to communicate with PLCs and RTUs on the OT network. This represents a path from a standard corporate intrusion to the ability to issue commands that control physical processes, with potential safety consequences.
- C is incorrect. RDP performance impact is an operational concern, not a security risk.
- D is incorrect. End-of-support is a significant security concern (no patches for future vulnerabilities) but the immediately most significant risk in the described configuration is the IT/OT bridge attack path.

---

**Question 19**

A penetration tester uses Hashcat to crack a captured NTLM hash. The crack is successful and the password is recovered as `Summer2024!`. This password meets the organization's minimum complexity requirements (8+ characters, uppercase, number, special character). What finding should the tester document?

A. No finding — the password meets the policy requirements.

B. A finding that the password is in the rockyou.txt wordlist, demonstrating that policy-compliant passwords can be weak if predictable. Recommend supplementing length/complexity requirements with prohibited common password lists.

C. A Critical finding — all NTLM hashes are crackable and the AD password policy must be replaced entirely.

D. A finding that NTLM is in use — recommend upgrading to NTLMv2.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Meeting minimum complexity is insufficient protection if the password is in a common wordlist. A policy-compliant but crackable password is a genuine finding.
- B is correct. `Summer2024!` is a predictable seasonal pattern. It is in or easily derived from common wordlists using rules (base word + season + year + symbol). The finding is that complexity requirements alone are insufficient — organizations should also implement dictionary checks against common password lists (Azure AD Password Protection, Have I Been Pwned, custom banned lists).
- C is incorrect. Calling all NTLM hash cracking a Critical finding overstates the situation. The specific finding is the weak/predictable password, which is Medium to High depending on the account privilege level. NTLM protocol concerns are a separate finding.
- D is incorrect. NTLM vs. NTLMv2 is a separate topic. The issue here is password predictability, not protocol version.

---

**Question 20**

Which of the following BEST summarizes the professional and ethical obligation that distinguishes an authorized penetration tester from a malicious actor, when both may use the same technical techniques?

A. The tester uses open-source tools while attackers use custom malware.

B. The tester has written authorization from the system owner, operates within defined scope, reports findings honestly to improve security, and maintains confidentiality of client data.

C. The tester holds a CompTIA certification proving their intentions are legitimate.

D. The tester stops testing before causing any actual damage, while attackers proceed further.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Both testers and attackers use both open-source and custom tools. Tool category does not define the distinction.
- B is correct. The defining characteristics of authorized penetration testing are: written authorization from the legitimate system owner, operation within defined scope, honest and complete reporting of findings, and confidentiality of client information. These obligations define professional security testing as distinct from unauthorized access regardless of the techniques used.
- C is incorrect. A certification demonstrates competency but does not grant authorization for any specific test. An uncertified tester with proper authorization is conducting legitimate testing; a certified professional testing without authorization is committing a crime.
- D is incorrect. This is a simplified and inaccurate description. Authorized testers do cause access and may demonstrate impact — the distinction is not "stops before damage" but rather the presence of authorization and professional obligations.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | B |
| 6 | B |
| 7 | A |
| 8 | B |
| 9 | A |
| 10 | B |
| 11 | B |
| 12 | B |
| 13 | C |
| 14 | B |
| 15 | B |
| 16 | A |
| 17 | A |
| 18 | B |
| 19 | B |
| 20 | B |
