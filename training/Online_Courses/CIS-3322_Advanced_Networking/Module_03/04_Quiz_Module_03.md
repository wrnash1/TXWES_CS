# Quiz: Module 03 - IPv6 Addressing and Configuration
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
What command enables a Cisco router to forward IPv6 traffic?
*   A) ip routing
*   B) ipv6 address autoconfig
*   C) ipv6 unicast-routing
*   D) ipv6 routing enable
*   **Correct Answer:** C) Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.
*   **Distractor Analysis:**
    *   *Why correct:* Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.
    *   ip routing is for IPv4. autoconfig sets up client address learning. routing enable is invalid syntax.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **EUI-64 configuration**?
D) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
C) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **EUI-64 configuration**.
    * *Why A is correct:* This describes the exact role and function of **EUI-64 configuration**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **EUI-64 configuration**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **EUI-64 configuration**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
A) ping
C) netstat -ano
D) nslookup
B) traceroute
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IPv6 Addressing and Configuration** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **IPv6 Addressing and Configuration**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

