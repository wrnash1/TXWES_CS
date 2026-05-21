# Quiz: Module 04 - Active Reconnaissance – Nmap and Enumeration
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which Nmap scan type is known as "stealth" or "half-open" scanning because it does not complete the TCP three-way handshake?
*   A) TCP Connect Scan (-sT)
*   B) TCP SYN Scan (-sS)
*   C) UDP Scan (-sU)
*   D) Ping Sweep (-sn)
*   **Correct Answer:** B) SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK to keep connections half-open.
*   **Distractor Analysis:**
    *   *Why correct:* SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK — never completing the handshake, which leaves minimal log entries on the target.
    *   *Why A is incorrect:* Connect scans (-sT) complete the full three-way handshake using the OS socket API, creating established connection records in target logs — the opposite of stealth.
    *   *Why C is incorrect:* UDP scans probe UDP ports (not TCP), using a fundamentally different protocol. They are not classified as "stealth" or "half-open" scans.
    *   *Why D is incorrect:* A ping sweep (-sn) discovers live hosts via ICMP — it does not scan ports at all and is not related to half-open TCP scanning.

---

**Question 2**
In Nmap, which flag enables **OS detection** by analyzing TCP/IP stack fingerprinting characteristics such as TTL values and TCP window sizes?
*   A) `-sV` — probes open ports to identify the software name and version number of running services.
*   B) `-O` — sends specially crafted probe packets and analyzes response characteristics to fingerprint the target operating system.
*   C) `-sC` — runs the default NSE script set against discovered open ports to enumerate services and check for common vulnerabilities.
*   D) `-A` — enables aggressive mode combining OS detection, version detection, script scanning, and traceroute in one scan.
*   **Correct Answer:** B) `-O` — sends specially crafted probe packets and analyzes response characteristics to fingerprint the target operating system.
*   **Distractor Analysis:**
    *   *Why B is correct:* The `-O` flag specifically enables OS detection. Nmap sends TCP/IP probes and compares the responses against its OS fingerprint database to identify the target OS and version. It requires at least one open and one closed port, and needs root/admin privileges.
    *   *Why A is incorrect:* `-sV` is service version detection — it identifies what software is running on open ports, not the underlying operating system.
    *   *Why C is incorrect:* `-sC` runs the default NSE scripts (equivalent to `--script=default`). It performs service enumeration and vulnerability checks, not OS fingerprinting.
    *   *Why D is incorrect:* `-A` is an umbrella flag that includes `-O` among other options, but `-A` alone is not the specific OS detection flag — and it also includes much more, making it the "aggressive" option.

---

**Question 3**
A penetration tester needs to scan a target for open ports and determine the software versions running on those ports in a single Nmap command. Which command is most appropriate?
*   A) `nmap -sn target_ip`
*   B) `nmap -O target_ip`
*   C) `nmap -sV target_ip`
*   D) `nmap --script vuln target_ip`
*   **Correct Answer:** C) `nmap -sV target_ip`
*   **Distractor Analysis:**
    *   *Why C is correct:* The `-sV` flag enables service version detection. Nmap probes each discovered open port with protocol-specific banners to identify the software name and version (e.g., "Apache httpd 2.4.51"). This is the standard flag for combining port scanning with version identification.
    *   *Why A is incorrect:* `-sn` performs a ping sweep (host discovery only) — it does not scan ports or detect service versions.
    *   *Why B is incorrect:* `-O` performs OS detection only. It does not report individual service versions running on open ports.
    *   *Why D is incorrect:* `--script vuln` runs NSE vulnerability scripts against discovered ports. It requires ports to be discovered first and does not itself combine port scanning with version identification in a clean single-purpose way.

---

**Question 4**
During an authorized penetration test, a tester needs maximum stealth while scanning a target. Which Nmap timing template should they use?
*   A) `-T5` (Insane) — fastest scan, best for stealth because it completes before IDS signatures trigger.
*   B) `-T3` (Normal) — the default timing; appropriate for all engagements.
*   C) `-T1` (Sneaky) — very slow scan rate that reduces detection probability by spacing probes far apart.
*   D) `-T0` (Paranoid) — sends one probe every 5 minutes, designed to evade nearly all IDS rate-based detection.
*   **Correct Answer:** C) `-T1` (Sneaky) — very slow scan rate that reduces detection probability by spacing probes far apart.
*   **Distractor Analysis:**
    *   *Why C is correct:* PT0-002 tests that slower timing templates (-T0, -T1, -T2) are used for stealth because they send fewer packets per second, making it harder for rate-based IDS/IPS rules to trigger. `-T1` (Sneaky) is practical for authorized engagements requiring stealth without the extreme slowness of `-T0`.
    *   *Why A is incorrect:* `-T5` (Insane) is the fastest and loudest template — it generates high traffic volume that easily triggers IDS alerts. Speed does not equal stealth.
    *   *Why B is incorrect:* `-T3` is the default general-purpose timing. It makes no attempt at stealth and will trigger many common IDS signatures.
    *   *Why D is incorrect:* `-T0` (Paranoid) is technically stealthier than `-T1` but is impractical for most engagements because one probe every 5 minutes means a full port scan could take days. `-T1` is the practical stealth choice tested by PT0-002.

---

**Question 5**
A tester runs `nmap --script smb-vuln-ms17-010 target_ip` against a Windows host and receives a positive result. What does this finding indicate?
*   A) The target has SMB port 445 open but no vulnerability was confirmed — further manual testing is required.
*   B) The target is likely vulnerable to the EternalBlue exploit, which can allow unauthenticated remote code execution via SMBv1.
*   C) The target's SMB service is misconfigured and is broadcasting its NetBIOS name in cleartext.
*   D) The target has outdated SSL/TLS certificates on port 443 that need to be renewed immediately.
*   **Correct Answer:** B) The target is likely vulnerable to the EternalBlue exploit, which can allow unauthenticated remote code execution via SMBv1.
*   **Distractor Analysis:**
    *   *Why B is correct:* MS17-010 is the Microsoft SMB vulnerability exploited by EternalBlue (used in WannaCry and NotPetya). The NSE script `smb-vuln-ms17-010` actively checks whether the target responds to the specific SMBv1 probe that confirms vulnerability. A positive result indicates high confidence the target is unpatched and exploitable for unauthenticated RCE.
    *   *Why A is incorrect:* The `smb-vuln-ms17-010` script performs an active check beyond just confirming the port is open — a positive result is a meaningful vulnerability indicator, not an inconclusive finding.
    *   *Why C is incorrect:* NetBIOS name broadcasting is a separate issue tested by different scripts (e.g., `nbstat`). It is unrelated to MS17-010.
    *   *Why D is incorrect:* MS17-010 is an SMB vulnerability on port 445. It has no connection to SSL/TLS certificates or port 443 web services.
