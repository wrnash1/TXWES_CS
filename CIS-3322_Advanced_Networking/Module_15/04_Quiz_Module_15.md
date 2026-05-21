# Quiz: Module 15 - CCNA Review and Diagnostics
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
What interface status indicates a physical layer cable disconnection on a Cisco device?
*   A) administratively down, line protocol is down
*   B) up, line protocol is down
*   C) down, line protocol is down
*   D) up, line protocol is up
*   **Correct Answer:** C) Down/Down indicates a layer 1 (cabling or connector) problem. Up/Down is Layer 2.
*   **Distractor Analysis:**
    *   *Why correct:* Down/Down indicates a layer 1 (cabling or connector) problem. Up/Down is Layer 2.
    *   Administratively down means the interface has been shut down via the `shutdown` command.

---

**Question 2**
Which of the following most accurately describes **mismatch symptoms** in the context of Cisco network troubleshooting?
*   A) Configuration inconsistencies between directly connected devices — such as duplex, speed, native VLAN, or encapsulation mismatches — that prevent or degrade communication and produce characteristic error counters or log messages.
*   B) A condition where packets loop between two or more routers indefinitely because each router's routing table incorrectly points to the other as the best path to a destination.
*   C) The set of IOS `show` commands used to verify interface state, routing table entries, OSPF neighbor adjacency, and VLAN assignments during systematic fault isolation.
*   D) A Layer 3 addressing error in which two devices on the same physical segment are configured with the same IP address, causing unpredictable packet delivery and ARP table inconsistencies.
*   **Correct Answer:** A) Configuration inconsistencies between directly connected devices — such as duplex, speed, native VLAN, or encapsulation mismatches — that prevent or degrade communication and produce characteristic error counters or log messages.
*   **Distractor Analysis:**
    * *Why A is correct:* Mismatch symptoms describe the observable effects of misconfigured parameters between peer devices — duplex mismatches cause late collisions; native VLAN mismatches cause CDP warnings; encapsulation mismatches cause `up/down` status on serial links.
    * *Why B is incorrect:* This describes a routing loop, which is a separate networking condition — not a "mismatch" between directly connected devices.
    * *Why C is incorrect:* This describes a set of diagnostic `show` commands (a troubleshooting toolkit), not the concept of mismatch symptoms.
    * *Why D is incorrect:* This describes an IP address conflict, which is a specific misconfiguration — one type of problem, not the broader category of mismatch symptoms.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
C) netstat -ano
D) traceroute
B) ping
A) nslookup
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.


---

**Question 4**
While working on **CCNA Review and Diagnostics** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When performing **CCNA Review and Diagnostics**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Configure DHCP Snooping on all VLANs to block unauthorized DHCP server responses from rogue devices connected to untrusted switch ports.
D) Enable Dynamic ARP Inspection (DAI) to validate ARP packets against the DHCP snooping binding table and drop spoofed ARP replies.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security directly prevents unauthorized devices from connecting to switch ports by enforcing a maximum MAC count and/or specific allowed MACs — the most direct preventive control against the described risk.
    * *Why C is incorrect:* DHCP Snooping protects against rogue DHCP servers (a related but different attack) — it does not prevent unauthorized devices from physically connecting to switch ports.
    * *Why D is incorrect:* DAI (Dynamic ARP Inspection) protects against ARP spoofing/poisoning attacks — not physical unauthorized port connections.
    * *Why B is incorrect:* SSH/HTTPS secures management sessions in transit but does not prevent unauthorized devices from connecting to switch ports.
