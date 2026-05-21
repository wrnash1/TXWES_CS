# Quiz: Module 13 - Network Monitoring and Troubleshooting Tools
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network administrator receives reports that users can access internal servers by IP address but cannot browse external websites by hostname. Which command should be run first to determine if the DNS server is responding to queries?
A) ping 8.8.8.8 — tests basic ICMP connectivity to Google's public DNS server IP address
B) traceroute www.google.com — maps the hop path to Google's web servers to identify where packets are being dropped
C) nslookup www.google.com — directly queries the configured DNS server to verify whether hostname resolution is functioning
D) netstat -ano — displays all active TCP/UDP connections and listening ports on the local machine
*   **Correct Answer:** C) nslookup www.google.com — directly queries the configured DNS server to verify whether hostname resolution is functioning
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Pinging 8.8.8.8 by IP tests internet connectivity but bypasses DNS entirely. If the ping succeeds, it only confirms IP routing works — it does not test whether the DNS server is resolving hostnames, which is the specific failure being investigated.
    *   *Why B is incorrect:* Running traceroute to www.google.com would itself require DNS resolution — if DNS is failing, traceroute would fail to resolve the hostname before it could even start tracing. Additionally, traceroute maps routing paths, not DNS server behavior.
    *   *Why D is incorrect:* `netstat -ano` shows local connections and listening ports — it has no ability to query DNS servers or test hostname resolution. It would not provide any information about whether external DNS is functioning.

---

**Question 2**
A network operations center analyst needs to identify which application on a Windows server is listening on TCP port 443 and establish whether unauthorized services have opened unexpected ports. Which command provides this information?
A) ping localhost — tests the local loopback interface to verify the TCP/IP stack is functioning on the server
B) ipconfig /all — displays all network interface configurations including IP address, subnet mask, and DNS server assignments
C) netstat -ano — displays all active connections and listening ports with the associated process identifier (PID) for each
D) arp -a — displays the ARP cache showing IP-to-MAC address mappings for recently contacted network hosts
*   **Correct Answer:** C) netstat -ano — displays all active connections and listening ports with the associated process identifier (PID) for each
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Pinging localhost (127.0.0.1) tests whether the local TCP/IP stack is functioning — it provides no information about which applications are listening on which ports or whether unauthorized services are running.
    *   *Why B is incorrect:* `ipconfig /all` shows IP addressing configuration (address, subnet mask, gateway, DNS, MAC) — it does not show which ports are open, which services are listening, or which process is associated with each port.
    *   *Why D is incorrect:* `arp -a` shows the ARP cache — IP-to-MAC address mappings for devices the host has recently communicated with. It provides Layer 2 address resolution information, not application port and process information.

---

**Question 3**
A technician is applying the CompTIA Network+ troubleshooting methodology to a connectivity problem. After identifying the problem (Step 1), they develop a theory that a misconfigured default gateway is causing the issue (Step 2). What is the correct next action according to the methodology?
A) Immediately reconfigure the default gateway on the affected workstation to the correct IP address to restore connectivity
B) Escalate the issue to senior network staff and document the theory in the ticketing system before taking any action
C) Test the theory by running `ping` to the default gateway IP address and `ipconfig /all` to verify the current gateway configuration
D) Establish a plan of action to correct the gateway and identify any potential side effects before making changes
*   **Correct Answer:** C) Test the theory by running `ping` to the default gateway IP address and `ipconfig /all` to verify the current gateway configuration
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Immediately implementing a fix skips Step 3 (test the theory) and Step 4 (establish an action plan). The methodology requires confirming the theory is correct before implementing any changes — acting without testing may fix the wrong problem or introduce new issues.
    *   *Why B is incorrect:* Escalation and documentation are not Step 3. Escalation is appropriate if the theory cannot be tested or the fix is beyond the technician's authority — but the first action after developing a theory is to test it, not to escalate.
    *   *Why D is incorrect:* Establishing an action plan is Step 4, which comes after the theory is tested and confirmed in Step 3. Planning before testing would skip the verification step that confirms whether the theory is actually correct.

---

**Question 4**
A network manager wants to implement centralized monitoring to receive automated alerts when a router's CPU utilization exceeds 80% or an interface goes down, and to collect periodic performance statistics from all switches. The solution must use encrypted authentication for all device communications. Which monitoring solution and version meets both requirements?
A) SNMPv1 with read-only community strings configured on all devices and a central NMS polling every 5 minutes
B) SNMPv3 with authentication and privacy (authPriv) mode, using the NMS to poll devices and receive encrypted traps for threshold alerts
C) SNMPv2c with read-write community strings and SNMP traps configured to send alerts to the NMS on interface state changes
D) Syslog with severity level 7 (debug) configured on all devices to send all log messages to a central syslog server for analysis
*   **Correct Answer:** B) SNMPv3 with authentication and privacy (authPriv) mode, using the NMS to poll devices and receive encrypted traps for threshold alerts
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SNMPv1 uses plaintext community strings with no authentication or encryption. Community strings can be intercepted and used to query or modify device configurations. This fails the encrypted authentication requirement.
    *   *Why C is incorrect:* SNMPv2c improves on SNMPv1 with 64-bit counters and bulk operations, but still uses plaintext community strings — no authentication or encryption. Read-write community strings are especially dangerous because they allow configuration changes via SNMP, violating the security requirement.
    *   *Why D is incorrect:* Syslog at severity level 7 (debug) sends all log messages — this is extremely verbose and would generate enormous log volume, most of it irrelevant. More importantly, standard syslog (UDP 514) transmits messages in plaintext without authentication or encryption. Syslog also does not poll devices for performance metrics — it only receives messages devices choose to send.

---

**Question 5**
A security team needs to implement a monitoring infrastructure that: (1) captures raw packet data on critical network segments for protocol-level forensic analysis, (2) collects and correlates security event logs from firewalls, IDS sensors, and servers to detect attack patterns, and (3) analyzes traffic flow data to identify bandwidth-hogging applications and unusual data exfiltration patterns. Which combination of tools addresses all three requirements?
A) Wireshark (or a tap/SPAN-fed packet capture system) for protocol analysis, a SIEM platform for log correlation and security event detection, and NetFlow/IPFIX collection for traffic flow analysis.
B) SNMP polling with an NMS for all three requirements — SNMP can collect interface statistics, receive trap alerts from security devices, and provide packet-level data from managed switches.
C) Syslog server for all three requirements — all devices send their log data to the syslog server, which can be searched for protocol errors, security events, and bandwidth utilization records.
D) Wireshark for all three requirements — it captures packets, correlates security events across multiple devices, and generates flow reports from the captured traffic in real time.
*   **Correct Answer:** A) Wireshark (or a tap/SPAN-fed packet capture system) for protocol analysis, a SIEM platform for log correlation and security event detection, and NetFlow/IPFIX collection for traffic flow analysis.
*   **Distractor Analysis:**
    *   *Why A is correct:* Packet capture (Wireshark/tap) provides raw protocol-level forensic analysis (requirement 1); a SIEM aggregates and correlates security logs from multiple sources to detect attack patterns (requirement 2); NetFlow/IPFIX exports flow records from routers and switches to identify application bandwidth usage and anomalous data transfers (requirement 3). Each tool is purpose-built for its requirement.
    *   *Why B is incorrect:* SNMP collects interface performance counters (bandwidth, error rates) and receives device alerts via traps — it does not capture raw packet data for protocol analysis and cannot correlate security events across multiple devices. SNMP is a monitoring protocol, not a forensic or SIEM tool.
    *   *Why C is incorrect:* Syslog receives text-based log messages from devices — it does not capture raw packets, and basic syslog servers do not perform correlation across multiple log sources. A syslog server collects logs but does not provide the correlation engine that a SIEM does, nor does it provide flow-level traffic analysis.
    *   *Why D is incorrect:* Wireshark captures packets on a single interface or from a SPAN port — it cannot aggregate logs from multiple devices (firewalls, IDS, servers) or correlate security events across them, which is the SIEM's function. Wireshark can analyze flows within a capture file but is not designed for continuous real-time flow monitoring across an enterprise network.
