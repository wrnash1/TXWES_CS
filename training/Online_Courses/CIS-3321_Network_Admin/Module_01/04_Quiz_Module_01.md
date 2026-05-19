# Quiz: Module 01 - OSI Model
## Course: CIS-3321_Network_Admin (3321_Network_Admin - CompTIA Network+ (N10-008))

---

**Question 1**
Which layer of the OSI model is responsible for routing packets across multiple logical networks using IP addressing?
A) Layer 2 (Data Link Layer)
B) Layer 3 (Network Layer)
C) Layer 4 (Transport Layer)
D) Layer 7 (Application Layer)
*   **Correct Answer:** B) Layer 3 (Network Layer)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Layer 2 handles MAC addressing and framing on the same physical link, not routing across logical networks.
    *   *Why C is incorrect:* Layer 4 manages end-to-end transport protocols (TCP/UDP) and port numbers, not routing.
    *   *Why D is incorrect:* Layer 7 handles application-specific protocols (HTTP, SMTP), not network routing.

---

**Question 2**
What is the Protocol Data Unit (PDU) processed at Layer 2 of the OSI model?
A) Segment
B) Packet
C) Frame
D) Bit
*   **Correct Answer:** C) Frame
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Segments are the PDU of Layer 4 (Transport Layer).
    *   *Why B is incorrect:* Packets are the PDU of Layer 3 (Network Layer).
    *   *Why D is incorrect:* Bits are the PDU of Layer 1 (Physical Layer).

---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
D) nslookup
A) netstat -ano
C) ping
B) traceroute
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **OSI Model** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **OSI Model**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

