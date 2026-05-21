# Quiz: Module 06 - Endpoint Detection and Response (EDR)
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which of the following best describes how EDR differs from traditional signature-based antivirus?

*   A) EDR relies exclusively on hash-based file matching against a known-malware database, while antivirus uses machine learning to detect unknown threats
*   B) EDR provides continuous behavioral monitoring, process telemetry, memory inspection, and remote isolation capabilities that antivirus signature scanning does not offer
*   C) EDR is a network-based tool that inspects packets inline, while antivirus operates only on email attachments
*   D) EDR and antivirus are functionally identical; the terms are interchangeable in modern endpoint security platforms
*   **Correct Answer:** B) EDR provides continuous behavioral monitoring, process telemetry, memory inspection, and remote isolation capabilities that antivirus signature scanning does not offer.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The description is reversed. Traditional AV uses hash/signature matching; EDR uses behavioral analysis and telemetry — not the other way around.
    *   *Why B is correct:* EDR platforms record endpoint events (process creation, network connections, registry changes, memory allocation) continuously and correlate them behaviorally. Remote isolation — severing a host from the network while keeping it running — is an EDR-specific response capability absent from traditional AV.
    *   *Why C is incorrect:* EDR is a host-based agent, not a network inline device. Network inline blocking describes an IPS, not EDR.
    *   *Why D is incorrect:* EDR and AV are distinctly different capability tiers. CySA+ specifically tests this distinction, and treating them as equivalent would be incorrect on the exam.

---

**Question 2**
In endpoint security monitoring, which of the following most accurately defines **anomaly-based detection**?

*   A) A detection method that compares file hashes against a continuously updated database of known malware signatures to identify malicious executables at write time
*   B) A detection method that establishes a behavioral baseline of normal endpoint activity and generates alerts when observed activity deviates significantly from that baseline
*   C) A detection method that intercepts network packets at the perimeter and blocks traffic matching predefined rule sets before it reaches endpoint systems
*   D) A detection method that scans removable media for previously catalogued malicious byte sequences when a USB device is connected to an endpoint
*   **Correct Answer:** B) A detection method that establishes a behavioral baseline of normal endpoint activity and generates alerts when observed activity deviates significantly from that baseline.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Comparing file hashes against a known-malware database describes signature-based detection, not anomaly-based detection. The two methods are conceptual opposites on CySA+.
    *   *Why B is correct:* Anomaly-based detection works by learning what "normal" looks like for a given endpoint (processes, network connections, memory usage patterns) and alerting when behavior deviates meaningfully. It can detect zero-days and novel threats that have no signature but produces more false positives than signature methods.
    *   *Why C is incorrect:* Intercepting and blocking network packets at the perimeter describes an inline IPS, which is a network-layer control — not endpoint anomaly detection.
    *   *Why D is incorrect:* Scanning removable media for known byte sequences describes signature-based USB scanning, not behavioral anomaly detection.

---

**Question 3**
An EDR platform alerts that a PowerShell process on a workstation has spawned a child process, connected to an external IP on port 443, and written an executable to `%TEMP%`. The analyst needs to contain the threat immediately while preserving evidence for investigation. Which action is correct?

*   A) Immediately shut down the workstation to stop the attack and prevent further damage
*   B) Uninstall the EDR agent from the workstation to stop the false alerts from interfering with the user's productivity
*   C) Use the EDR platform to network-isolate the workstation, severing its network connectivity while keeping it powered on for forensic memory collection
*   D) Delete the executable from `%TEMP%` and restart the PowerShell service to clear the malicious process
*   **Correct Answer:** C) Use the EDR platform to network-isolate the workstation, severing its network connectivity while keeping it powered on for forensic memory collection.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Shutting down the workstation destroys volatile memory contents (running processes, network connections, encryption keys in RAM) — evidence that is irretrievable after power-off. CySA+ specifically tests this as a high-frequency exam trap.
    *   *Why B is incorrect:* Uninstalling the EDR agent removes the containment and investigation capability during an active incident; this would worsen the situation significantly.
    *   *Why C is correct:* EDR network isolation severs the host's network access (stopping C2 communication and lateral movement) while keeping the system running so that volatile memory, running processes, and the malicious executable in `%TEMP%` can be collected forensically. This is the standard EDR containment workflow.
    *   *Why D is incorrect:* Deleting the executable destroys evidence and restarting the service does not address the root compromise; the attacker likely has persistence mechanisms beyond the single file.

---

**Question 4**
A security analyst reviews EDR telemetry and finds that `mshta.exe` spawned `cmd.exe`, which executed a base64-encoded PowerShell command that downloaded a payload from an external server. Which attack category does this execution chain most strongly indicate?

*   A) Credential dumping — the attacker is extracting stored password hashes from the Windows Security Account Manager database
*   B) A living-off-the-land attack — the attacker is using legitimate, pre-installed Windows binaries to execute malicious code and avoid signature-based AV detection
*   C) SQL injection — the attacker is exploiting a database input field to execute operating system commands through the web application tier
*   D) ARP poisoning — the attacker is intercepting network traffic between the workstation and its default gateway at Layer 2
*   **Correct Answer:** B) A living-off-the-land attack — the attacker is using legitimate, pre-installed Windows binaries to execute malicious code and avoid signature-based AV detection.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Credential dumping targets the SAM database or LSASS process memory to extract password hashes; the described chain (mshta → cmd → PowerShell download) is an execution and delivery chain, not a credential harvesting operation.
    *   *Why B is correct:* Living-off-the-land (LotL) attacks use built-in OS tools (mshta.exe, powershell.exe, wscript.exe, certutil.exe) to execute attacker-controlled code. Because no novel malware binary is written initially, signature-based AV cannot detect the attack. EDR behavioral telemetry — specifically the parent-child process chain — is required to identify it.
    *   *Why C is incorrect:* SQL injection exploits database input fields on web application servers; it does not describe a Windows process execution chain on a workstation.
    *   *Why D is incorrect:* ARP poisoning is a Layer 2 network attack that redirects traffic on a LAN segment; it has no connection to the described Windows process chain.

---

**Question 5**
An analyst wants to detect fileless malware on endpoints across the organization. Which two controls together best implement this detection capability?

*   A) Deploy full-disk encryption on all endpoints and configure automatic BitLocker recovery key escrow to Azure AD
*   B) Deploy EDR agents configured to monitor PowerShell and WMI execution events, and create SIEM correlation rules that alert when encoded PowerShell commands are executed by non-administrative users
*   C) Enforce application whitelisting using AppLocker policies that block all unsigned executables from running in user-writable directories
*   D) Require multi-factor authentication for all domain accounts and configure conditional access policies that block logins from unmanaged devices
*   **Correct Answer:** B) Deploy EDR agents configured to monitor PowerShell and WMI execution events, and create SIEM correlation rules that alert when encoded PowerShell commands are executed by non-administrative users.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full-disk encryption protects data confidentiality at rest; it does not monitor or detect in-memory code execution, which is the defining characteristic of fileless malware.
    *   *Why B is correct:* Fileless malware executes entirely in memory using LOLBins such as PowerShell and WMI — leaving no file on disk for AV to scan. EDR process telemetry captures the execution events, and SIEM correlation rules on encoded PowerShell (a common obfuscation indicator) provide the alerting layer. Together they address the detection gap that signature-based AV cannot fill.
    *   *Why C is incorrect:* AppLocker whitelisting blocks unsigned executable files; it does not prevent or detect in-memory PowerShell or WMI abuse because those are signed, legitimate OS components.
    *   *Why D is incorrect:* MFA and conditional access address authentication security and device compliance; they do not detect malicious code executing in memory on an already-authenticated endpoint.
