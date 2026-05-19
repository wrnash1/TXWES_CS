# Quiz: Module 03 - Routing
## Course: CIS-3321_Network_Admin (3321_Network_Admin - CompTIA Network+ (N10-008))

---

**Question 1**
Your company wants to move away from hosting its own email servers to a model where a third-party provider manages the hardware, the operating system, the email software, and the maintenance. Which cloud service model does this represent?
A) IaaS
B) PaaS
C) SaaS
D) DaaS
*   **Correct Answer:** C) SaaS
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Infrastructure as a Service (IaaS) only provides the virtual hardware; you must install and manage the OS and the email server software yourself.
    *   *Why B is incorrect:* Platform as a Service (PaaS) provides the environment for developers to write code, not a finished, ready-to-use application like email.
    *   *Why D is incorrect:* Desktop as a Service (DaaS) provides a virtual desktop operating system, not a specific software application.

---

**Question 2**
Which IEEE wireless standard operates exclusively in the 5 GHz frequency band and introduced standardized support for MU-MIMO (Multi-User Multiple-Input Multiple-Output)?
A) 802.11b
B) 802.11g
C) 802.11n
D) 802.11ac
*   **Correct Answer:** D) 802.11ac
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 802.11b operates exclusively in the 2.4 GHz band.
    *   *Why B is incorrect:* 802.11g operates exclusively in the 2.4 GHz band.
    *   *Why C is incorrect:* 802.11n operates in both 2.4 GHz and 5 GHz bands, but 802.11ac operates *exclusively* in the 5 GHz band and heavily utilized MU-MIMO.

---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
B) nslookup
C) ping
A) traceroute
D) netstat -ano
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Routing** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **Routing**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
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

