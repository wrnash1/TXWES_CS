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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **mismatch symptoms.**?
C) The node or router interface on a network that serves as an access point to other logical networks or the internet.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) A data table stored in a router or network host that lists the paths and network destinations to determine where packets should be forwarded.
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **mismatch symptoms.**.
    * *Why A is correct:* This describes the exact role and function of **mismatch symptoms.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **mismatch symptoms.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **mismatch symptoms.**.


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
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **CCNA Review and Diagnostics**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
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

