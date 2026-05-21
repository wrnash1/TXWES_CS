# Quiz: Module 02 - Subnetting and VLSM Configurations
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
How many usable host IP addresses are available in a `/28` subnet mask?
*   A) 16
*   B) 14
*   C) 30
*   D) 6
*   **Correct Answer:** B) A `/28` mask has 4 host bits (32-28 = 4). 2^4 = 16. Subtracting network and broadcast addresses leaves 14.
*   **Distractor Analysis:**
    *   *Why correct:* A `/28` mask has 4 host bits (32-28 = 4). 2^4 = 16. Subtracting network and broadcast addresses leaves 14.
    *   16 is total addresses. 30 is for `/27`. 6 is for `/29`.

---

**Question 2**
Which of the following most accurately describes **CIDR prefix matching** as used in IP routing?
*   A) The process by which a router selects the routing table entry with the longest (most specific) matching prefix when forwarding a packet to its destination.
*   B) A method for assigning Class A, B, or C addresses based on the first octet value, without support for variable-length subnet boundaries.
*   C) A technique for splitting a large broadcast domain into smaller subnets by borrowing host bits to create additional network bits.
*   D) The process of summarizing multiple contiguous network prefixes into a single, shorter prefix advertisement to reduce routing table size.
*   **Correct Answer:** A) The process by which a router selects the routing table entry with the longest (most specific) matching prefix when forwarding a packet to its destination.
*   **Distractor Analysis:**
    * *Why A is correct:* CIDR prefix matching (longest-prefix match) is the fundamental lookup rule all IP routers use — the most specific route wins.
    * *Why B is incorrect:* This describes classful addressing (pre-CIDR), which does not support variable-length subnet masks.
    * *Why C is incorrect:* This describes subnetting — borrowing host bits — not prefix matching during packet forwarding.
    * *Why D is incorrect:* This describes route summarization (supernetting), which is a related but distinct concept from prefix matching.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
B) nslookup
C) netstat -ano
A) traceroute
D) ping
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Subnetting and VLSM Configurations** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing subnets for **Subnetting and VLSM Configurations**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable SNMP version 3 with authentication and privacy (authPriv) to encrypt network management traffic.
D) Deploy a dedicated out-of-band management network to isolate administrative traffic from user data traffic.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH and HTTPS encrypt management sessions in transit, directly preventing credential capture by packet sniffers. Use `transport input ssh` on VTY lines.
    * *Why B is incorrect:* Port Security restricts MAC addresses at access ports — it does not protect against sniffing of credentials sent in plaintext over the network.
    * *Why C is incorrect:* SNMPv3 authPriv is a good practice for SNMP security, but does not address SSH/Telnet credential exposure.
    * *Why D is incorrect:* An out-of-band management network adds isolation but does not encrypt credentials — Telnet over an isolated network is still plaintext.
