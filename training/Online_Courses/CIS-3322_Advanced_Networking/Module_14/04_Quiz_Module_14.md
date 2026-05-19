# Quiz: Module 14 - Network Automation & REST APIs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a Software-Defined Networking architecture, which API is used to communicate between the controller and the application layer?
*   A) Southbound API
*   B) Northbound API
*   C) Eastbound API
*   D) OpenFlow
*   **Correct Answer:** B) Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.
*   **Distractor Analysis:**
    *   *Why correct:* Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.
    *   OpenFlow is a southbound protocol.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **JSON/XML data formats.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
C) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
D) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
B) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **JSON/XML data formats.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **JSON/XML data formats.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **JSON/XML data formats.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **JSON/XML data formats.**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
A) ping
B) traceroute
C) netstat -ano
D) nslookup
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Network Automation & REST APIs** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..


---

**Question 5**
When designing a system for **Network Automation & REST APIs**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

