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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **IP allocation strategies**?
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
B) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **IP allocation strategies**.
    * *Why A is correct:* This describes the exact role and function of **IP allocation strategies**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **IP allocation strategies**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **IP allocation strategies**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
D) nslookup
B) netstat -ano
C) traceroute
A) ping
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.


---

**Question 4**
While working on **Subnetting and VLSM Configurations** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..


---

**Question 5**
When designing a system for **Subnetting and VLSM Configurations**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
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

