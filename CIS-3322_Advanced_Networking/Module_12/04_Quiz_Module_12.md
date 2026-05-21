# Quiz: Module 12 - Wireless LANs (WLAN) & WLC
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which protocol is used by lightweight access points to communicate with a central Wireless LAN Controller?
*   A) LACP
*   B) CAPWAP
*   C) SNMP
*   D) 802.1Q
*   **Correct Answer:** B) Control and Provisioning of Wireless Access Points (CAPWAP) encapsulates AP-to-WLC management and data traffic.
*   **Distractor Analysis:**
    *   *Why correct:* Control and Provisioning of Wireless Access Points (CAPWAP) encapsulates AP-to-WLC management and data traffic.
    *   LACP is link aggregation. SNMP is management. 802.1Q is trunking.

---

**Question 2**
Which of the following most accurately describes the role of a **Wireless LAN Controller (WLC)** in an enterprise network?
*   A) A centralized device that manages multiple lightweight APs, pushing SSID configurations, security policies, and RF settings to all associated APs while handling client authentication and roaming.
*   B) A standalone access point that manages its own SSID configuration, authentication, and security settings independently without requiring a central management device.
*   C) A Layer 2 switch that aggregates wireless traffic from multiple access points and forwards it to the distribution layer using 802.1Q trunk links.
*   D) A RADIUS authentication server that stores wireless user credentials and responds to 802.1X EAP authentication requests from wireless clients.
*   **Correct Answer:** A) A centralized device that manages multiple lightweight APs, pushing SSID configurations, security policies, and RF settings to all associated APs while handling client authentication and roaming.
*   **Distractor Analysis:**
    * *Why A is correct:* The WLC is the defining component of a centralized wireless architecture — it uses CAPWAP to control lightweight APs and provides single-pane management for the entire wireless deployment.
    * *Why B is incorrect:* This describes an autonomous AP, which operates independently — the opposite of the lightweight/WLC model.
    * *Why C is incorrect:* This describes a standard Layer 2 switch used in the wired infrastructure — not a wireless LAN controller.
    * *Why D is incorrect:* This describes a RADIUS server (such as Cisco ISE), which handles authentication but is a separate device from the WLC.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
D) traceroute
C) ping
A) nslookup
B) netstat -ano
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Wireless LANs (WLAN) & WLC** in a production environment, you encounter a system alert indicating a **Subnet Mask Mismatch** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why D is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why C is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why A is correct:* Because A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses. The appropriate fix is to Correct the subnet mask configuration on the interface to match the network segment parameters.


---

**Question 5**
When configuring **Wireless LANs (WLAN) & WLC**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
D) Enable Rogue AP detection on the WLC to automatically identify and alert on unauthorized access points in the airspace.
C) Configure WPA3-Enterprise with 802.1X on all SSIDs to require individual user authentication before granting wireless network access.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security directly blocks unauthorized devices from connecting to switch ports and gaining wired network access, which is the specific risk described.
    * *Why B is incorrect:* SSH/HTTPS secures management sessions but does not prevent unauthorized devices from physically plugging into switch ports.
    * *Why D is incorrect:* Rogue AP detection identifies unauthorized wireless devices in the RF environment — it does not prevent wired switch port connections from unauthorized laptops.
    * *Why C is incorrect:* WPA3-Enterprise secures wireless client authentication but does not address unauthorized physical wired connections to switch ports.
