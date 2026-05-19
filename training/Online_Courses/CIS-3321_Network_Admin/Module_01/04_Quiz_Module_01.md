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

---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
D) nslookup
C) netstat -ano
B) ping
A) traceroute
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.


---

**Question 4**
While working on **OSI Model** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **OSI Model**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

