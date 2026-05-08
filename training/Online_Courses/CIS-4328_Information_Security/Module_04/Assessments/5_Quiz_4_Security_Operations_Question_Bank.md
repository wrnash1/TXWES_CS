### 5. Quiz 4: Security Operations (Question Bank)
**Question 1**
During an active malware outbreak, the incident response team decides to physically disconnect the infected web server from the corporate network switch, but leaves the server powered on to preserve memory artifacts. Which phase of the Incident Response Lifecycle does this action represent?
A) Identification
B) Containment
C) Eradication
D) Recovery
*   **Correct Answer:** B) Containment
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Identification is the phase where the team confirms an incident is actually occurring. Disconnecting the server is an action taken *after* it has been identified.
    *   *Why C is incorrect:* Eradication involves removing the malware (e.g., wiping the drive, running antivirus). Disconnecting the cable stops the spread, but the malware is still on the machine.
    *   *Why D is incorrect:* Recovery is the process of restoring the server to normal business operations, which cannot happen until the threat is eradicated.

**Question 2**
A security analyst needs to collect forensic evidence from a compromised workstation. According to the standard order of volatility, which of the following data sources should the analyst collect FIRST?
A) The local hard drive (HDD/SSD)
B) The routing tables and ARP cache
C) System Memory (RAM)
D) Archival backup tapes
*   **Correct Answer:** C) System Memory (RAM)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hard drives represent non-volatile storage. Data on a hard drive will survive a reboot, so it is collected *after* highly volatile sources.
    *   *Why B is incorrect:* While routing tables are volatile, RAM (which includes CPU registers and cache in broader definitions) is generally prioritized as the primary source of volatile running processes and encryption keys. (Note: CPU registers are technically higher than RAM, but among these options, RAM is the highest).
    *   *Why D is incorrect:* Backup tapes are the least volatile form of storage and can be collected at any time.
