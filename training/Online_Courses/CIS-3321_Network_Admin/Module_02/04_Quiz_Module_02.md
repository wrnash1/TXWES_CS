# Quiz: Module 02 - VLANs
## Course: CIS-3321_Network_Admin (3321_Network_Admin - CompTIA Network+ (N10-008))

---

**Question 1**
An administrator wants to segment a switch's ports logically into separate broadcast domains. Which technology should they configure?
A) NAT (Network Address Translation)
B) DHCP (Dynamic Host Configuration Protocol)
C) VLAN (Virtual Local Area Network)
D) STP (Spanning Tree Protocol)
*   **Correct Answer:** C) VLAN (Virtual Local Area Network)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* NAT translates between public and private IP addresses, it does not segment local switch broadcast domains.
    *   *Why B is incorrect:* DHCP assigns IP addresses dynamically, it does not create broadcast boundaries.
    *   *Why D is incorrect:* STP prevents switching loops, it does not segment a switch into logical broadcast domains.

---

---

**Question 2**
Which of the following IP addresses falls within the private ranges defined by RFC 1918?
A) 172.32.10.5
B) 192.168.4.25
C) 11.0.0.1
D) 192.169.1.1
*   **Correct Answer:** B) 192.168.4.25
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The private Class B range is 172.16.0.0 to 172.31.255.255. 172.32.x.x is public.
    *   *Why C is incorrect:* The private Class A range is 10.0.0.0/8. 11.0.0.1 is public.
    *   *Why D is incorrect:* The private Class C range is 192.168.0.0/16. 192.169.x.x is public.

---

---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
A) traceroute
C) ping
B) netstat -ano
D) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **VLANs** in a production environment, you encounter a system alert indicating a **Subnet Mask Mismatch** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Correct the subnet mask configuration on the interface to match the network segment parameters.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Distractor Analysis:**
    * *Why A is correct:* Because A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses. The appropriate fix is to Correct the subnet mask configuration on the interface to match the network segment parameters..
    * *Why C is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why B is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why D is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.


---

**Question 5**
When designing a system for **VLANs**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..

