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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Troubleshooting methodology**?
C) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
B) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Troubleshooting methodology**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Troubleshooting methodology**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Troubleshooting methodology**.
    * *Why A is correct:* This describes the exact role and function of **Troubleshooting methodology**.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
D) nslookup
B) ping
C) traceroute
A) netstat -ano
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.


---

**Question 4**
While working on **CCNA Review and Diagnostics** in a production environment, you encounter a system alert indicating a **Subnet Mask Mismatch** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Distractor Analysis:**
    * *Why A is correct:* Because A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses. The appropriate fix is to Correct the subnet mask configuration on the interface to match the network segment parameters..
    * *Why D is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why B is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why C is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.


---

**Question 5**
When designing a system for **CCNA Review and Diagnostics**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

