# Quiz: Module 13 - Password Attacks – Hashcat and John the Ripper
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which technique allows a penetration tester to route attack traffic through a compromised host to reach internal network segments that are not directly accessible from the attacker's machine?
*   A) Privilege Escalation
*   B) Pivoting
*   C) Vulnerability Scanning
*   D) Password Spraying
*   **Correct Answer:** B) Pivoting
*   **Distractor Analysis:**
    *   *Why B is correct:* Pivoting uses a compromised host as a relay point to access network segments that are otherwise unreachable from the attacker's system. The compromised host acts as a bridge — tools like SSH port forwarding, Metasploit's `route` command, and `proxychains` route attack traffic through the pivot host into internal subnets. This technique demonstrates how a single perimeter breach can expose the entire internal network.
    *   *Why A is incorrect:* Privilege escalation increases the access level on the current compromised host — from standard user to administrator or root. It does not provide access to other network segments or hosts.
    *   *Why C is incorrect:* Vulnerability scanning is a reconnaissance activity performed earlier in the methodology to identify potential weaknesses. It does not involve routing traffic through a compromised host or accessing isolated network segments.
    *   *Why D is incorrect:* Password spraying is an online credential attack that submits one common password against many accounts to avoid lockout thresholds. It is an initial access technique, not a network routing or pivoting technique.

---

**Question 2**
In the context of password attacks, which of the following best defines a **dictionary attack**?
*   A) A technique that systematically generates every possible character combination up to a specified length, guaranteeing password recovery given sufficient time and computational resources.
*   B) A technique that uses precomputed hash-to-plaintext lookup tables to instantly reverse a hash without performing live cracking computations.
*   C) A password cracking technique that submits words from a pre-built wordlist as password candidates against a captured hash or authentication service.
*   D) A technique that intercepts and captures password hashes from network authentication traffic for later offline cracking.
*   **Correct Answer:** C) A password cracking technique that submits words from a pre-built wordlist as password candidates against a captured hash or authentication service.
*   **Distractor Analysis:**
    *   *Why C is correct:* A dictionary attack uses a wordlist of common passwords, dictionary words, and known breach passwords — such as the `rockyou.txt` list with over 14 million entries — as candidates. Each word is hashed and compared against the target hash. Dictionary attacks are fast, effective against common passwords, and are the default starting point for both Hashcat (`-a 0`) and John the Ripper before escalating to brute-force if the wordlist fails.
    *   *Why A is incorrect:* This describes a brute-force attack — exhaustive enumeration of all possible combinations. Brute-force is not limited to a wordlist and guarantees coverage at the cost of time. It is a distinct attack mode from dictionary attacks.
    *   *Why B is incorrect:* This describes a rainbow table attack — using precomputed hash chains to instantly look up plaintext values. Rainbow tables are only effective against unsalted hashes and are a separate technique from dictionary attacks, which compute hashes live from a wordlist.
    *   *Why D is incorrect:* This describes network hash capture — a passive reconnaissance technique (e.g., capturing Net-NTLMv2 hashes via Responder). Capturing hashes is a prerequisite step that produces material for offline cracking, but it is not itself a dictionary attack.

---

**Question 3**
A penetration tester has extracted NTLM password hashes from a compromised Windows system's SAM database. Which Hashcat command performs a dictionary attack against these hashes using the rockyou.txt wordlist?
*   A) `john --format=NT hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt`
*   B) `hashcat -m 1000 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt`
*   C) `hydra -L hashes.txt -P rockyou.txt smb://target`
*   D) `aircrack-ng -w rockyou.txt -b <BSSID> capture.cap`
*   **Correct Answer:** B) `hashcat -m 1000 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt`
*   **Distractor Analysis:**
    *   *Why B is correct:* In Hashcat, `-m 1000` specifies the NTLM hash type (Windows NT hash), `-a 0` selects dictionary attack mode, `hashes.txt` is the file containing the extracted NTLM hashes, and `/usr/share/wordlists/rockyou.txt` is the wordlist. Hashcat uses GPU acceleration to test millions or billions of candidates per second. This is the standard command for cracking NTLM hashes from a Windows SAM database dump.
    *   *Why A is incorrect:* This is a valid John the Ripper command for the same task — `--format=NT` specifies NTLM and `--wordlist` specifies the dictionary. However, the question specifically asks for a Hashcat command. John and Hashcat use different syntax and different acceleration approaches.
    *   *Why C is incorrect:* Hydra performs online brute-force attacks against live authentication services — in this case, SMB. It does not process offline hash files and cannot crack hashes from a SAM database dump. It would also require valid credentials format, not hash format.
    *   *Why D is incorrect:* `aircrack-ng` cracks WPA2 wireless handshake captures, not NTLM password hashes. It is a wireless-specific tool that processes 802.11 packet captures, not Windows authentication hashes.

---

**Question 4**
A penetration tester wants to crack the password protecting a ZIP archive found on a compromised system. Which John the Ripper workflow correctly accomplishes this?
*   A) `hashcat -m 17210 -a 0 protected.zip rockyou.txt` — Hashcat directly processes ZIP archives in dictionary mode.
*   B) `zip2john protected.zip > zip.hash` followed by `john zip.hash --wordlist=rockyou.txt` — extract the hash first, then crack it.
*   C) `john --format=zip --stdin protected.zip < rockyou.txt` — John reads the ZIP file directly with stdin input.
*   D) `unzip -P $(cat rockyou.txt) protected.zip` — pass each password from the wordlist directly to the unzip command.
*   **Correct Answer:** B) `zip2john protected.zip > zip.hash` followed by `john zip.hash --wordlist=rockyou.txt` — extract the hash first, then crack it.
*   **Distractor Analysis:**
    *   *Why B is correct:* John the Ripper cannot directly process binary file formats. The `zip2john` companion tool extracts the password hash from the ZIP archive's encryption header and outputs it in a format John can process. The resulting hash file is then fed to `john` with a wordlist for dictionary cracking. The same pattern applies to other protected file types: `ssh2john` for SSH keys, `pdf2john` for PDFs, `office2john` for Microsoft Office documents. This two-step workflow is the standard John the Ripper approach for file-based password cracking.
    *   *Why A is incorrect:* While Hashcat does support some ZIP hash modes (PKZIP is `-m 17200`), the question asks about the John the Ripper workflow. More importantly, Hashcat cannot directly process a `.zip` file — it also requires extracting the hash first using a compatible tool before cracking.
    *   *Why C is incorrect:* John does not accept `--stdin` input for password candidates in this manner, and it cannot read the ZIP file directly as a binary input. The `--stdin` option reads password candidates from standard input for a hash file, not a ZIP archive directly.
    *   *Why D is incorrect:* This is a shell scripting approach that would call `unzip` for each line in the wordlist — extremely slow, generates excessive process overhead, and is not a recognized penetration testing workflow. It would also fail to handle passwords with special characters correctly without careful shell escaping.

---

**Question 5**
During an engagement, a penetration tester wants to test authentication strength across all domain user accounts without triggering account lockout policies. Which attack technique is most appropriate?
*   A) Credential stuffing — using username/password pairs from previous breach databases against the domain's authentication service.
*   B) Offline brute-force with Hashcat — generating all character combinations against captured NTLM hashes until a match is found.
*   C) Password spraying — attempting one or two common passwords against all accounts, staying below the lockout threshold.
*   D) Rainbow table attack — using precomputed hash chains to instantly look up Active Directory password hashes.
*   **Correct Answer:** C) Password spraying — attempting one or two common passwords against all accounts, staying below the lockout threshold.
*   **Distractor Analysis:**
    *   *Why C is correct:* Password spraying deliberately inverts the traditional brute-force approach: instead of many passwords against one account (which triggers lockout), it tries one or a few common passwords (e.g., `Welcome1!`, `CompanyName2024!`) against every account in the domain. This stays under typical lockout thresholds (usually 5–10 failed attempts per account) while testing the entire user population. It is highly effective against organizations that use predictable password patterns and is a standard PT0-002-tested technique.
    *   *Why A is incorrect:* Credential stuffing uses previously breached username/password pairs from other sites — testing whether users have reused passwords across services. It is distinct from password spraying because it uses full credential pairs from external breaches rather than common password patterns tested against all accounts.
    *   *Why B is incorrect:* Offline brute-force with Hashcat requires already-captured password hashes — it is an offline cracking technique, not an online authentication test. It also does not risk triggering lockout since it does not interact with live authentication services. The question asks about testing live authentication strength.
    *   *Why D is incorrect:* Rainbow table attacks work offline against captured hashes and require unsalted hashes to be effective. Active Directory hashes use NTLM (unsalted), so rainbow tables are theoretically applicable, but this is still an offline technique — it does not test live authentication and does not address the lockout concern at all.
