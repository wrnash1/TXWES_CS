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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **CIDR prefix matching.**?
C) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
B) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **CIDR prefix matching.**.
    * *Why A is correct:* This describes the exact role and function of **CIDR prefix matching.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **CIDR prefix matching.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **CIDR prefix matching.**.


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
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **Subnetting and VLSM Configurations**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

