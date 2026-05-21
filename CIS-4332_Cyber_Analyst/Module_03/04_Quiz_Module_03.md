# Quiz: Module 03 - Vulnerability Management – Scanning and Prioritization
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which type of scan provides the most accurate view of patch levels and installed software on a target host?
*   A) Non-credentialed scan
*   B) Credentialed scan
*   C) Passive network sniff
*   D) Stealth SYN scan
*   **Correct Answer:** B) Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.
*   **Distractor Analysis:**
    *   *Why correct:* Credentialed scans log into the system to read local registry settings and files directly, preventing false positives.
    *   Non-credentialed scans can only analyze open network ports and banners, missing locally installed software vulnerabilities.

---

**Question 2**
In a vulnerability management context, which of the following most accurately defines **credentialed vs. non-credentialed scans**?
*   A) Credentialed scans use supplied login credentials to inspect a system internally for patch levels and configurations, while non-credentialed scans can only probe open network ports and service banners from the outside
*   B) Credentialed scans are performed by an external penetration tester with written authorization, while non-credentialed scans are run by internal staff without formal approval
*   C) Credentialed scans encrypt all traffic between the scanner and target, while non-credentialed scans transmit results in plaintext
*   D) Credentialed scans identify only network-layer vulnerabilities, while non-credentialed scans identify both host-based and network-layer issues
*   **Correct Answer:** A) Credentialed scans use supplied login credentials to inspect a system internally for patch levels and configurations, while non-credentialed scans can only probe open network ports and service banners from the outside.
*   **Distractor Analysis:**
    *   *Why A is correct:* The defining distinction is whether the scanner authenticates to the target system. With credentials, the scanner reads local data (registry, installed packages, services); without credentials, it is limited to externally visible information.
    *   *Why B is incorrect:* The credential distinction refers to system login credentials provided to the scanner, not to analyst authorization levels or organizational roles.
    *   *Why C is incorrect:* Encryption of scan traffic is a separate configuration concern unrelated to whether the scanner authenticates to the target host.
    *   *Why D is incorrect:* This reverses the actual capabilities — credentialed scans find more vulnerabilities including host-based ones, not fewer.

---

**Question 3**
A vulnerability analyst needs to identify which services are running on a target host and determine their exact version numbers in order to cross-reference against a vulnerability database. Which command is most appropriate?
*   A) `nmap -sV -p 1-1024 target_ip` — service version detection scan across the first 1024 ports
*   B) `openssl s_client -connect target_ip:443` — tests the SSL/TLS handshake on port 443
*   C) `wireshark -i eth0 -k` — launches a live packet capture on the network interface
*   D) `netstat -an` — displays active TCP/UDP connections on the local machine only
*   **Correct Answer:** A) `nmap -sV -p 1-1024 target_ip` — service version detection scan across the first 1024 ports.
*   **Distractor Analysis:**
    *   *Why A is correct:* The `-sV` flag instructs Nmap to probe open ports and report the service name and version string, which is exactly what is needed to match against CVE databases.
    *   *Why B is incorrect:* `openssl s_client` tests a single SSL/TLS connection; it does not enumerate services across multiple ports or return version strings for non-TLS services.
    *   *Why C is incorrect:* Wireshark captures live network traffic passively; it does not actively probe a target to enumerate running services or their versions.
    *   *Why D is incorrect:* `netstat` shows connections on the local machine where it is run; it cannot remotely enumerate services on a separate target host.

---

**Question 4**
A SOC analyst notices that after a credentialed vulnerability scan ran against a legacy SCADA host, the device became unresponsive. Which lesson-learned action best prevents this in future scans?
*   A) Switch to a non-credentialed scan so the scanner cannot directly interact with system processes
*   B) Create a separate scan policy with reduced scan intensity and excluded plugins known to crash fragile systems, and test it in a maintenance window
*   C) Disable all vulnerability scanning for operational technology (OT) networks permanently
*   D) Increase the scan frequency so the system has less time to become unstable between checks
*   **Correct Answer:** B) Create a separate scan policy with reduced scan intensity and excluded plugins known to crash fragile systems, and test it in a maintenance window.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Switching to non-credentialed scans reduces accuracy but does not guarantee the device will not be impacted by aggressive network probing; the root cause is scan policy configuration, not credentials.
    *   *Why B is correct:* Fragile OT/SCADA devices require custom scan policies that disable intrusive plugins, reduce scan speed, and are tested during planned maintenance windows to avoid production impact.
    *   *Why C is incorrect:* Completely disabling scanning leaves OT assets without vulnerability visibility; the correct approach is to adapt the scan policy, not eliminate scanning.
    *   *Why D is incorrect:* Increasing scan frequency would increase the stress on the device and raise the risk of repeated outages.

---

**Question 5**
A security team discovers that an attacker who breached a workstation deleted the local Windows Event Logs before being detected. Which control would have best preserved evidence for the investigation?
*   A) Deploying a host-based intrusion detection system (HIDS) on the workstation
*   B) Enabling BitLocker full-disk encryption on the workstation
*   C) Forwarding Windows Event Logs in real time to a centralized, write-protected SIEM platform
*   D) Requiring a screensaver password lock after five minutes of inactivity
*   **Correct Answer:** C) Forwarding Windows Event Logs in real time to a centralized, write-protected SIEM platform.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A HIDS can alert on suspicious activity but does not inherently prevent an attacker with local admin rights from deleting the local log store.
    *   *Why B is incorrect:* Disk encryption protects data confidentiality if the drive is removed; it does not prevent an authenticated local session from deleting log files.
    *   *Why C is correct:* Streaming logs off the host to a centralized immutable SIEM ensures that even if the attacker clears local logs, the off-host copy remains intact and available for forensic review.
    *   *Why D is incorrect:* A screensaver lock addresses physical access risk at an unattended console; it has no effect on log preservation after a system has already been compromised remotely.

