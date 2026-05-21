# Quiz: Module 08 - Lateral Movement and Persistence
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which Active Directory attack involves requesting Kerberos service tickets for SPN-registered accounts and attempting to crack the encrypted tickets offline to recover service account passwords?
*   A) Pass-the-Hash
*   B) Kerberoasting
*   C) AS-REP Roasting
*   D) SMB Relay
*   **Correct Answer:** B) Kerberoasting
*   **Distractor Analysis:**
    *   *Why B is correct:* Kerberoasting exploits the Kerberos protocol by allowing any authenticated domain user to request service tickets (TGS) for accounts with Service Principal Names (SPNs). The ticket is encrypted with the service account's NTLM hash, so it can be extracted and cracked offline using Hashcat or John the Ripper — no elevated privileges are required to request the ticket.
    *   *Why A is incorrect:* Pass-the-Hash uses a captured NTLM hash to authenticate directly to services without cracking it. It does not involve Kerberos tickets or offline password cracking.
    *   *Why C is incorrect:* AS-REP Roasting also extracts encrypted material for offline cracking, but it targets accounts with Kerberos pre-authentication disabled — no valid credentials are needed to initiate the attack, which distinguishes it from Kerberoasting.
    *   *Why D is incorrect:* An SMB Relay attack intercepts NTLM authentication attempts and relays them to another host in real time to gain unauthorized access. It does not involve requesting or cracking Kerberos service tickets.

---

**Question 2**
In the context of Windows Active Directory lateral movement, which of the following best defines **Pass-the-Hash (PtH)**?
*   A) A technique that requests Kerberos service tickets for offline password cracking using the service account's encryption key.
*   B) A lateral movement technique that uses a captured NTLM password hash to authenticate to remote services without knowing the plaintext password.
*   C) A method of injecting a DLL into a running process to inherit its authentication tokens and escalate privileges on the local system.
*   D) An attack that intercepts NTLM authentication traffic in transit and forwards it to a different target host to impersonate the victim.
*   **Correct Answer:** B) A lateral movement technique that uses a captured NTLM password hash to authenticate to remote services without knowing the plaintext password.
*   **Distractor Analysis:**
    *   *Why B is correct:* Pass-the-Hash exploits the NTLM challenge-response protocol, which accepts the hash itself as the credential. An attacker who captures an NTLM hash (via LSASS dump, registry extraction, or network capture) can use tools like Impacket's `psexec.py` or Metasploit's `psexec` module to authenticate to SMB, WMI, or other services on remote hosts without ever cracking the hash.
    *   *Why A is incorrect:* This describes Kerberoasting — the extraction and offline cracking of Kerberos TGS tickets. Kerberoasting involves Kerberos, not NTLM, and targets service account passwords.
    *   *Why C is incorrect:* This describes DLL injection and token impersonation — a privilege escalation technique performed locally. It does not involve using password hashes for remote authentication.
    *   *Why D is incorrect:* This describes an NTLM Relay attack (also called SMB Relay), where intercepted authentication is forwarded in real time. PtH uses a pre-captured hash directly in a new authentication attempt — it is not a relay of intercepted traffic.

---

**Question 3**
A penetration tester has obtained a SYSTEM-level Meterpreter session on a Windows domain-joined workstation. Which command sequence extracts cached credentials — including NTLM hashes and Kerberos tickets — from LSASS memory?
*   A) `hashdump`
*   B) `load kiwi` followed by `creds_all`
*   C) `run post/multi/recon/local_exploit_suggester`
*   D) `getsystem`
*   **Correct Answer:** B) `load kiwi` followed by `creds_all`
*   **Distractor Analysis:**
    *   *Why B is correct:* `load kiwi` loads the Kiwi module (a Meterpreter implementation of Mimikatz) into the active session. `creds_all` then dumps all credential material from LSASS memory — including NTLM hashes, cleartext passwords cached in memory, and Kerberos tickets. This is the most comprehensive credential extraction command available in Meterpreter and requires SYSTEM-level access.
    *   *Why A is incorrect:* `hashdump` reads NTLM hashes from the Windows SAM (Security Account Manager) database for local accounts only. It does not extract domain credentials, Kerberos tickets, or credentials cached in LSASS memory from domain users who have logged in.
    *   *Why C is incorrect:* `post/multi/recon/local_exploit_suggester` identifies potential privilege escalation exploits for the target OS version. It is a reconnaissance module, not a credential extraction tool.
    *   *Why D is incorrect:* `getsystem` attempts to escalate the current session to SYSTEM privileges. It is a prerequisite step — not a credential extraction command.

---

**Question 4**
A penetration tester has Domain Admin credentials and wants to remotely execute a command on another Windows host in the same domain using SMB. Which tool from the Impacket suite is designed for this purpose?
*   A) `BloodHound`
*   B) `GetUserSPNs.py`
*   C) `psexec.py`
*   D) `hashcat`
*   **Correct Answer:** C) `psexec.py`
*   **Distractor Analysis:**
    *   *Why C is correct:* Impacket's `psexec.py` authenticates to a remote Windows host over SMB using valid credentials or an NTLM hash (Pass-the-Hash), uploads a service binary, and executes commands remotely — returning an interactive shell. It is the primary Impacket tool for SMB-based lateral movement and remote code execution. Similar alternatives in the suite include `wmiexec.py` and `smbexec.py`.
    *   *Why A is incorrect:* BloodHound is an Active Directory attack path analysis and visualization tool. It ingests AD relationship data (collected by SharpHound) and maps the shortest path to Domain Admin. It does not execute commands on remote hosts.
    *   *Why B is incorrect:* `GetUserSPNs.py` enumerates Active Directory accounts with Service Principal Names (SPNs) and requests their Kerberos service tickets for Kerberoasting. It is a reconnaissance and ticket-extraction tool, not a remote execution tool.
    *   *Why D is incorrect:* Hashcat is an offline password cracking tool. It processes captured hashes but has no capability to authenticate to or execute commands on remote systems.

---

**Question 5**
After completing an engagement, a penetration tester wants to document the persistence mechanisms they installed on a Windows target. Which of the following is a common Windows persistence technique that survives system reboots?
*   A) Running `getsystem` to re-escalate privileges after each reboot.
*   B) Adding a malicious executable path to the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` registry key.
*   C) Migrating the Meterpreter session into `explorer.exe` to maintain process stability.
*   D) Using `hashdump` to extract and store credentials for re-authentication after each reboot.
*   **Correct Answer:** B) Adding a malicious executable path to the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` registry key.
*   **Distractor Analysis:**
    *   *Why B is correct:* Registry Run keys cause a specified program to execute automatically every time the current user logs in. The `HKCU\...\Run` key requires only user-level write access, making it accessible even without administrator privileges. This is one of the most common and widely documented Windows persistence techniques, alongside scheduled tasks (`schtasks`), startup folder entries, and Windows service creation.
    *   *Why A is incorrect:* `getsystem` is a Meterpreter command that attempts privilege escalation in real time — it is not a persistence mechanism and does not survive a reboot. After a reboot, the Meterpreter session itself would be gone.
    *   *Why C is incorrect:* Migrating into `explorer.exe` improves session stability and stealth within the current session, but it does not persist across reboots. When the system restarts, the migrated process terminates along with everything else.
    *   *Why D is incorrect:* `hashdump` extracts credential hashes for offline cracking or Pass-the-Hash reuse. While having credentials enables re-authentication, this is not a persistence mechanism — it requires the attacker to actively re-exploit or re-authenticate after every reboot rather than the backdoor automatically re-establishing itself.
