# Quiz: Module 11 - NAT and PAT Configurations
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which NAT terminology describes the public IP address of an inside host as seen by external devices on the internet?
*   A) Inside Local
*   B) Inside Global
*   C) Outside Local
*   D) Outside Global
*   **Correct Answer:** B) Inside Global is the public address mapped to the internal host's Inside Local private address.
*   **Distractor Analysis:**
    *   *Why correct:* Inside Global is the public address mapped to the internal host's Inside Local private address.
    *   Inside Local is the private IP. Outside Global is the target public IP.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **inside local/global definitions.**?
B) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **inside local/global definitions.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **inside local/global definitions.**.
    * *Why A is correct:* This describes the exact role and function of **inside local/global definitions.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **inside local/global definitions.**.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
B) netstat -ano
D) ping
A) traceroute
C) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **NAT and PAT Configurations** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..


---

**Question 5**
When designing a system for **NAT and PAT Configurations**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..

