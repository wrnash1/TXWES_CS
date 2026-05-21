# Reading Guide: Module 13 - Password Attacks – Hashcat and John the Ripper
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 13 - Password Attacks – Hashcat and John the Ripper**! Password attacks are a foundational skill in penetration testing — whether cracking offline hashes extracted from a compromised system, testing a web application's authentication strength, or evaluating an organization's password policy. This module covers the tools, techniques, and hash types that PT0-002 tests directly. Password cracking maps to the **Attacks and Exploits** domain (**30% of exam weight**) and the **Tools and Code Analysis** domain (**16% of exam weight**), making it one of the most cross-domain topics in the certification.

Understanding password attacks allows pentesters to demonstrate the real-world risk of weak password policies, credential reuse, and improperly stored password hashes — converting technical hash-cracking results into concrete business impact statements.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Dictionary Attack**: A password cracking technique that submits words from a pre-built wordlist as password candidates against a hash or authentication service. The most commonly used wordlist in penetration testing is `rockyou.txt` — a list of over 14 million real passwords from a major data breach. Dictionary attacks are fast and effective against common or previously compromised passwords. Both Hashcat and John the Ripper support dictionary mode.

*   **Brute-Force Attack**: A password cracking technique that systematically tries every possible character combination up to a specified length. While guaranteed to find any password given enough time, brute-force is computationally expensive and practical only for short passwords or when character sets are constrained. Hashcat uses mask attacks (e.g., `?u?l?l?l?d?d?d?s`) to implement efficient brute-force with known password patterns.

*   **Hash Types and Identification**: Different systems store passwords using different hashing algorithms. Common hash types tested on PT0-002 include: NTLM (Windows SAM/Active Directory), MD5, SHA-1, SHA-256, bcrypt, and Net-NTLMv2. Identifying the hash type before cracking is critical — tools like `hashid` or `hash-identifier` analyze hash format and suggest the algorithm. Hashcat uses numeric mode IDs (e.g., `-m 1000` for NTLM, `-m 0` for MD5, `-m 3200` for bcrypt).

*   **Hashcat**: The industry-standard GPU-accelerated password cracking tool. Hashcat can leverage the parallel processing power of modern graphics cards to attempt billions of hash comparisons per second. Key modes: `-a 0` (dictionary), `-a 3` (brute-force/mask), `-a 6` (hybrid wordlist + mask). Hashcat is the primary cracking tool for offline hash cracking in professional pentests. Example: `hashcat -m 1000 -a 0 hashes.txt rockyou.txt` cracks NTLM hashes using a dictionary attack.

*   **John the Ripper (JtR)**: An open-source password cracking tool that supports a wide range of hash formats and includes automatic hash format detection. John is particularly useful for cracking password-protected files (ZIP, PDF, SSH keys) using companion tools (`zip2john`, `ssh2john`, `pdf2john`) that convert protected files into crackable hash format. While generally slower than Hashcat for GPU-accelerated cracking, John's auto-detection and file format support make it the preferred choice for diverse hash scenarios.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Password attacks appear in both Attacks and Exploits (30%) and Tools and Code Analysis (16%) domains. Know the tools, hash types, and attack modes by name.
*   **Hashcat vs. John the Ripper:** Hashcat is GPU-accelerated and faster for large hash lists — the professional standard for offline cracking. John the Ripper auto-detects hash formats and handles file-based cracking (ZIP, SSH keys) via companion tools. PT0-002 tests when to use each.
*   **Credential Stuffing vs. Password Spraying vs. Brute-Force:** These are three distinct online attack techniques. Credential stuffing uses username/password pairs from previous breach databases. Password spraying tries one common password (e.g., `Summer2024!`) against many accounts to avoid lockout. Brute-force tries all combinations against a single account. PT0-002 tests the differences.
*   **Rainbow Tables vs. Salted Hashes:** Rainbow tables are precomputed hash-to-plaintext lookup tables that make cracking fast — but only work against unsalted hashes. A salt (random value added before hashing) makes rainbow tables ineffective. Modern systems (bcrypt, scrypt, Argon2) use salts by design. PT0-002 tests awareness of why salted hashes resist rainbow table attacks.
*   **Hydra for Online Attacks:** While Hashcat and John crack hashes offline, Hydra performs online brute-force against live services (SSH, FTP, HTTP login forms, RDP). The command `hydra -l admin -P rockyou.txt ssh://target` tests SSH credential strength. PT0-002 tests the online vs. offline distinction.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "John the Ripper," "Hashcat," and "Password Attacks" rooms provide browser-based guided practice with both tools against real hash samples, wordlists, and password-protected files in a legal lab environment without requiring a local GPU.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Password Attacks section for content covering hash types, cracking tools, attack modes, and online vs. offline attack distinctions mapped to PT0-002 domains.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the John the Ripper, Hashcat, and Password Attacks rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — all labs run in your browser without requiring a local GPU or Kali Linux installation. The password attack rooms guide you through hash identification, wordlist selection, Hashcat mode configuration, and John the Ripper file cracking with hands-on exercises.
*   **Required Video:** Watch the Password Attacks segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the password cracking content covering hash types, Hashcat, John the Ripper, and the online vs. offline attack distinction.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Identify hash types: `hashid <hash>` or `hash-identifier`**: You will analyze sample hashes from a compromised system to determine their algorithm (NTLM, MD5, SHA-256, bcrypt) before attempting to crack them — a required step since Hashcat and John require the correct hash mode to function.
*   **Dictionary attack with Hashcat: `hashcat -m 1000 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt`**: You will run a dictionary attack against a set of NTLM hashes using the rockyou.txt wordlist, observe the cracking speed and results, and document which passwords were recovered — noting what the recovered passwords reveal about the organization's password policy compliance.
*   **File-based cracking with John the Ripper: `zip2john protected.zip > zip.hash` then `john zip.hash --wordlist=rockyou.txt`**: You will use John's companion tool to extract the hash from a password-protected ZIP file, then crack it with a wordlist attack — demonstrating that file encryption is only as strong as the password protecting it.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the John the Ripper and Hashcat rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Password Attacks section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
