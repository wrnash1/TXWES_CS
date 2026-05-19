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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Port Address Translation (PAT) / Overload**?
C) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
B) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Port Address Translation (PAT) / Overload**.
    * *Why A is correct:* This describes the exact role and function of **Port Address Translation (PAT) / Overload**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Port Address Translation (PAT) / Overload**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Port Address Translation (PAT) / Overload**.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
C) ping
B) traceroute
A) nslookup
D) netstat -ano
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **NAT and PAT Configurations** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **NAT and PAT Configurations**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

